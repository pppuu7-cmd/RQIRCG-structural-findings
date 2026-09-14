#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
import json, hashlib, math
import numpy as np

BITS=list(product([0,1], repeat=3))
R_GRID=[30,40,60,80,120,160,250,400,800]
SIGMA_GRID=[Fraction(1,200),Fraction(1,100),Fraction(1,50),Fraction(1,25),Fraction(1,20)]
TAU_GRID=[Fraction(1,100),Fraction(1,50),Fraction(1,20),Fraction(1,10),Fraction(1,5)]
RHO_GRID=[Fraction(0),Fraction(1,200),Fraction(1,100),Fraction(1,50),Fraction(1,20)]
M=Fraction(5)
SHIFTS=(Fraction(1),Fraction(2),Fraction(3))
SRC_A_LIMIT=Fraction(-82,616005)
SRC_W_LIMIT=Fraction(2,945)

def d3(vals):
    return (vals[(1,1,1)]-vals[(1,1,0)]-vals[(1,0,1)]-vals[(0,1,1)]
            +vals[(1,0,0)]+vals[(0,1,0)]+vals[(0,0,1)]-vals[(0,0,0)])

def fs(x):
    if isinstance(x,Fraction):
        return f"{x.numerator}/{x.denominator}" if x.denominator!=1 else str(x.numerator)
    return x

def positions(R,a,b,c,shifts=SHIFTS):
    da,db,dc=shifts
    return [da*a, Fraction(4)+db*b, Fraction(10)+dc*c, Fraction(R)-(da*a+db*b+dc*c)/M]

def masses(): return [Fraction(1),Fraction(1),Fraction(1),M]

def Vn(xs):
    ms=masses(); v=Fraction(0)
    for i in range(4):
        for j in range(i+1,4):
            r=xs[j]-xs[i]
            if r<=0: raise ValueError((xs,i,j,r))
            v -= ms[i]*ms[j]/r
    return v

def grad(xs):
    ms=masses(); g=[Fraction(0) for _ in range(4)]
    for i in range(4):
        for j in range(i+1,4):
            r=xs[j]-xs[i]; mu=ms[i]*ms[j]
            g[i]-=mu/(r*r); g[j]+=mu/(r*r)
    return g

def Avec(xs):
    ms=masses(); g=grad(xs)
    return sum(g[i]*g[i]/ms[i] for i in range(4))

def W1(xs):
    ms=masses(); s=Fraction(0)
    for i in range(4):
        for j in range(4):
            if i==j: continue
            rij=abs(xs[i]-xs[j])
            for k in range(4):
                if i==k: continue
                rik=abs(xs[i]-xs[k])
                s += ms[i]*ms[j]*ms[k]/(rij*rik)
    return s/Fraction(2)

def hessian_massnorm(xs):
    ms=np.array([1.0,1.0,1.0,5.0])
    H=np.zeros((4,4),float)
    for i in range(4):
        for j in range(i+1,4):
            r=float(xs[j]-xs[i]); mu=ms[i]*ms[j]
            c=2.0*mu/(r**3)
            H[i,i]-=c; H[j,j]-=c; H[i,j]+=c; H[j,i]+=c
    Minvhalf=np.diag(1/np.sqrt(ms))
    S=Minvhalf@H@Minvhalf
    ev=np.linalg.eigvalsh(S)
    return H, ev

def cell(R, shifts=SHIFTS):
    pos={b:positions(R,*b,shifts=shifts) for b in BITS}
    V={b:Vn(pos[b]) for b in BITS}
    G={b:grad(pos[b]) for b in BITS}
    A={b:Avec(pos[b]) for b in BITS}
    W={b:W1(pos[b]) for b in BITS}
    g0=G[(0,0,0)]
    Q={b:sum((G[b][i]-g0[i])**2 for i in range(4)) for b in BITS}
    minsep=min(float(pos[b][j]-pos[b][i]) for b in BITS for i in range(4) for j in range(i+1,4))
    maxacc=0.0; lam=0.0
    ms=[1.0,1.0,1.0,5.0]
    for b in BITS:
        gg=G[b]
        maxacc=max(maxacc,max(abs(float(gg[i]))/ms[i] for i in range(4)))
        _,ev=hessian_massnorm(pos[b])
        lam=max(lam,max(abs(ev)))
    return {
        'pos':pos,'V':V,'A':A,'W':W,'Q':Q,
        'dV':d3(V),'dA':d3(A),'dW':d3(W),'dQ':d3(Q),
        'minsep':minsep,'maxacc':maxacc,'lambda_H':lam,
    }

rdata={}
all_signs={'dA':set(),'dW':set(),'dQ':set()}
for R in R_GRID:
    c=cell(R)
    dV,dA,dW,dQ=c['dV'],c['dA'],c['dW'],c['dQ']
    for name,val in [('dA',dA),('dW',dW),('dQ',dQ)]:
        all_signs[name].add(0 if val==0 else (1 if val>0 else -1))
    eps_app=abs(dV/dW)
    frac_A=abs((dA-SRC_A_LIMIT)/SRC_A_LIMIT)
    frac_W=abs((dW-SRC_W_LIMIT)/SRC_W_LIMIT)
    tau_cells={}
    for tau in TAU_GRID:
        tf=float(tau)
        eta_disp=0.5*c['maxacc']*tf*tf/c['minsep']
        eta_H=tf*tf*c['lambda_H']
        eps_fb=abs(float(dA/dW))*tf*tf/12.0
        tau_cells[fs(tau)]={
            'eta_disp':eta_disp,'eta_H':eta_H,'controlled':bool(eta_disp<=0.02 and eta_H<=0.05),
            'epsilon_fb':eps_fb,
        }
    rdata[str(R)]={
        'delta3_VN':fs(dV),'delta3_VN_float':float(dV),
        'delta3_A':fs(dA),'delta3_A_float':float(dA),
        'delta3_W1':fs(dW),'delta3_W1_float':float(dW),
        'delta3_Q':fs(dQ),'delta3_Q_float':float(dQ),
        'frac_depart_A_from_source':float(frac_A),
        'frac_depart_W_from_source':float(frac_W),
        'epsilon_app':float(eps_app),
        'min_pair_center_separation_over_ell':c['minsep'],
        'max_dimensionless_acceleration':c['maxacc'],
        'lambda_H':c['lambda_H'],
        'tau_cells':tau_cells,
    }

sigma_data={}
# use R=100 inherited primary dQ only for the scaling identity; no new center coefficient is selected here
c100=cell(100)
for sig in SIGMA_GRID:
    sf=float(sig)
    sigma_data[fs(sig)]={
        'eta_sigma_using_global_minsep':sf/c100['minsep'],
        'gamma_prefactor_without_T2_hbar2':0.5*sf*sf*float(c100['dQ']),
        'gamma_over_sigma2':0.5*float(c100['dQ']),
    }

size_data={}
for rho in RHO_GRID:
    rf=float(rho)
    worst_margin=min(rdata[str(R)]['min_pair_center_separation_over_ell']-2*rf for R in R_GRID)
    size_data[fs(rho)]={
        'worst_nonoverlap_margin_over_ell':worst_margin,
        'all_center_supports_nonoverlap':bool(worst_margin>0),
        'newtonian_spherical_monopole_scope':'applicable if externally spherical/nonoverlapping',
        '1PN_scope':'inherited nonspinning monopole/effacement applicability only; no new material/control coefficient assigned',
    }

# deletion controls on entire new R grid
deletes={}
for idx,name in enumerate(['A','B','C']):
    shifts=list(SHIFTS); shifts[idx]=Fraction(0); shifts=tuple(shifts)
    lane={}
    exact_zero=True
    for R in R_GRID:
        c=cell(R,shifts=shifts)
        vals=(c['dV'],c['dA'],c['dW'],c['dQ'])
        exact_zero=exact_zero and all(v==0 for v in vals)
        lane[str(R)]={'dV':fs(vals[0]),'dA':fs(vals[1]),'dW':fs(vals[2]),'dQ':fs(vals[3])}
    deletes[name]={'exact_zero_all_R':exact_zero,'cells':lane}

# prereg PASS check: exact controls, signs, tau <=0.1 controlled all R
controls_pass=all(deletes[n]['exact_zero_all_R'] for n in deletes)
signs_pass=(all_signs['dA']=={-1} and all_signs['dW']=={1} and len(all_signs['dQ'])==1 and 0 not in all_signs['dQ'])
tau_pass=True
for R in R_GRID:
    for tau in [Fraction(1,100),Fraction(1,50),Fraction(1,20),Fraction(1,10)]:
        tau_pass=tau_pass and rdata[str(R)]['tau_cells'][fs(tau)]['controlled']
size_pass=all(v['all_center_supports_nonoverlap'] for v in size_data.values())
classification=('ROBUST_KNOWN_PHYSICS_COHERENCE_BASELINE_HIERARCHY_SCOPED'
                if controls_pass and signs_pass and tau_pass and size_pass else
                'ROBUSTNESS_BOUNDARY_IDENTIFIED_SCOPED')

out={
    'prereg_commit':'ee392560debda35c0fbe51ca65112d1939fb3cfb',
    'inherited_head':'4e9d1d243d666d7d0db44f31f1b0851b720cccc0',
    'frozen_grids':{
        'R_over_ell':R_GRID,
        'sigma_over_ell':[fs(x) for x in SIGMA_GRID],
        'tau':[fs(x) for x in TAU_GRID],
        'rho_over_ell':[fs(x) for x in RHO_GRID],
    },
    'source_limits':{'dA':fs(SRC_A_LIMIT),'dA_float':float(SRC_A_LIMIT),'dW':fs(SRC_W_LIMIT),'dW_float':float(SRC_W_LIMIT)},
    'R_lane':rdata,
    'sigma_lane_R100':sigma_data,
    'finite_size_applicability_lane':size_data,
    'delete_one_label_controls':deletes,
    'aggregate_checks':{
        'delete_controls_pass':bool(controls_pass),
        'sign_stability_pass':bool(signs_pass),
        'observed_sign_sets':{k:sorted(v) for k,v in all_signs.items()},
        'tau_le_0p1_controlled_all_R':bool(tau_pass),
        'finite_size_nonoverlap_pass':bool(size_pass),
    },
    'classification':classification,
}
raw=json.dumps(out,indent=2,sort_keys=True)
print(raw)
with open('SF029_CHECKS.json','w') as f: f.write(raw+'\n')
with open(__file__,'rb') as f: print('SCRIPT_SHA256',hashlib.sha256(f.read()).hexdigest())
