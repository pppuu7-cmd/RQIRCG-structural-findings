#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
import json, hashlib

BITS=list(product([0,1], repeat=3))

def d3(vals):
    return (vals[(1,1,1)]-vals[(1,1,0)]-vals[(1,0,1)]-vals[(0,1,1)]
            +vals[(1,0,0)]+vals[(0,1,0)]+vals[(0,0,1)]-vals[(0,0,0)])

def fr(x):
    if isinstance(x, Fraction):
        return f"{x.numerator}/{x.denominator}" if x.denominator != 1 else str(x.numerator)
    return x

def model(R=Fraction(100), M=Fraction(5), shifts=(Fraction(1),Fraction(2),Fraction(3))):
    masses=[Fraction(1),Fraction(1),Fraction(1),M]
    da,db,dc=shifts
    def positions(a,b,c):
        xa=da*a
        xb=Fraction(4)+db*b
        xc=Fraction(10)+dc*c
        xd=R-(da*a+db*b+dc*c)/M
        return [xa,xb,xc,xd]
    def Vn(xs):
        v=Fraction(0)
        for i in range(4):
            for j in range(i+1,4):
                r=xs[j]-xs[i]
                assert r>0
                v -= masses[i]*masses[j]/r
        return v
    def grad(xs):
        g=[Fraction(0) for _ in range(4)]
        for i in range(4):
            for j in range(i+1,4):
                r=xs[j]-xs[i]
                mu=masses[i]*masses[j]
                g[i] -= mu/(r*r)
                g[j] += mu/(r*r)
        return g
    def A(xs):
        g=grad(xs)
        return sum(g[i]*g[i]/masses[i] for i in range(4))
    def W1(xs):
        s=Fraction(0)
        for i in range(4):
            for j in range(4):
                if j==i: continue
                rij=abs(xs[i]-xs[j])
                for k in range(4):
                    if k==i: continue
                    rik=abs(xs[i]-xs[k])
                    s += masses[i]*masses[j]*masses[k]/(rij*rik)
        return s/Fraction(2)
    pos={b:positions(*b) for b in BITS}
    V={b:Vn(pos[b]) for b in BITS}
    Gd={b:grad(pos[b]) for b in BITS}
    AA={b:A(pos[b]) for b in BITS}
    WW={b:W1(pos[b]) for b in BITS}
    g0=Gd[(0,0,0)]
    Q={b:sum((Gd[b][i]-g0[i])**2 for i in range(4)) for b in BITS}
    return dict(masses=masses,pos=pos,V=V,Gd=Gd,A=AA,W=WW,Q=Q)

def source_only(shifts=(Fraction(1),Fraction(2),Fraction(3))):
    da,db,dc=shifts
    def positions(a,b,c): return [da*a, Fraction(4)+db*b, Fraction(10)+dc*c]
    def Vn(xs):
        return -sum(Fraction(1, xs[j]-xs[i]) for i in range(3) for j in range(i+1,3))
    def grad(xs):
        g=[Fraction(0)]*3
        for i in range(3):
            for j in range(i+1,3):
                r=xs[j]-xs[i]
                g[i]-=Fraction(1,r*r); g[j]+=Fraction(1,r*r)
        return g
    def A(xs): return sum(x*x for x in grad(xs))
    def W1(xs):
        s=Fraction(0)
        for i in range(3):
            for j in range(3):
                if j==i: continue
                for k in range(3):
                    if k==i: continue
                    s += Fraction(1, abs(xs[i]-xs[j])*abs(xs[i]-xs[k]))
        return s/Fraction(2)
    V={b:Vn(positions(*b)) for b in BITS}
    Avals={b:A(positions(*b)) for b in BITS}
    W={b:W1(positions(*b)) for b in BITS}
    return d3(V), d3(Avals), d3(W)

main=model()
sV,sA,sW=source_only()

controls={}
for idx,name in enumerate(['A','B','C']):
    sh=[Fraction(1),Fraction(2),Fraction(3)]
    sh[idx]=Fraction(0)
    mm=model(shifts=tuple(sh))
    controls[f'delete_{name}']={
        'delta3_VN':fr(d3(mm['V'])),
        'delta3_A':fr(d3(mm['A'])),
        'delta3_W1':fr(d3(mm['W'])),
        'delta3_Q':fr(d3(mm['Q'])),
    }

R_ladder={}
for R in [50,100,200,1000]:
    mm=model(R=Fraction(R))
    R_ladder[str(R)]={
        'delta3_VN':fr(d3(mm['V'])),
        'delta3_A':fr(d3(mm['A'])),
        'delta3_W1':fr(d3(mm['W'])),
        'delta3_VN_float':float(d3(mm['V'])),
        'delta3_A_float':float(d3(mm['A'])),
        'delta3_W1_float':float(d3(mm['W'])),
    }

out={
    'frozen_inputs':{
        'geometry':'3D Gaussian packets with collinear centers; center coefficients computed on x-axis',
        'R_over_ell':100,
        'M_D_over_m':5,
        'sigma_over_ell':'1/100',
        'source_centers':'A=a, B=4+2b, C=10+3c',
        'D_center':'100-(a+2b+3c)/5',
    },
    'finite_R_primary':{
        'delta3_VN_in_Gm2_over_ell':fr(d3(main['V'])),
        'delta3_VN_float':float(d3(main['V'])),
        'delta3_A_in_G2m3_over_ell4':fr(d3(main['A'])),
        'delta3_A_float':float(d3(main['A'])),
        'delta3_W1_in_G2m3_over_c2ell2':fr(d3(main['W'])),
        'delta3_W1_float':float(d3(main['W'])),
        'delta3_force_difference_square_Q':fr(d3(main['Q'])),
        'delta3_Q_float':float(d3(main['Q'])),
    },
    'source_only_control_R_infinity':{
        'delta3_VN':fr(sV),
        'delta3_A':fr(sA),
        'delta3_A_float':float(sA),
        'delta3_W1':fr(sW),
        'delta3_W1_float':float(sW),
    },
    'delete_one_displacement_controls':controls,
    'R_ladder_control':R_ladder,
    'analytic_coherence_formula':{
        'Theta3_N':'-(T/hbar) Delta3[V_N] + (T^3/(12 hbar)) Delta3[A_N] + higher orders at leading semiclassical eta^0',
        'Gamma3_N':'(sigma^2 T^2/(2 hbar^2)) Delta3[sum_I |grad V_s-grad V_000|^2] + O(T^4, eta-dependent stability corrections)',
        'Delta1PN_Theta3':'-(T/hbar) Delta3[V_static_1PN] + O(G^3 T^3/(hbar c^2), c^-4, eta^2 epsilon_PN)',
    },
    'power_counting':{
        'initial_branch_velocities':'zero',
        'v_N_scaling':'O(G T)',
        'EIH_velocity_terms':'G v^2/c^2 integrated over T = O(G^3 T^3/c^2); v^4/c^2 integrated = O(G^4 T^5/c^2)',
        'static_1PN_trajectory_pullback':'grad(V_1PN) delta q_N integrated = O(G^3 T^3/c^2)',
        '1PN_trajectory_correction_inside_LN':'O(G^3 T^3/c^2)',
        'retained_1PN_difference':'only initial static EIH potential contributes at O(G^2 T/c^2)',
    },
    'domain_control':{
        '3D_1_over_r_local_integrability':'PASS: r^2 dr / r ~ r dr',
        '3D_1_over_r2_local_integrability':'PASS: r^2 dr / r^2 ~ dr',
        'simultaneous_distinct_triple_product':'locally integrable in six relative dimensions for separated Gaussian centers; no 1D logarithmic defect',
    },
}

raw=json.dumps(out, indent=2, sort_keys=True)
print(raw)
with open('SF028B_CHECKS.json','w') as f: f.write(raw+'\n')
with open(__file__,'rb') as f: print('SCRIPT_SHA256',hashlib.sha256(f.read()).hexdigest())
