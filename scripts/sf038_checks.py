#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
import json, hashlib
import numpy as np

BITS=list(product([0,1], repeat=3))
RSEL=[60,160,400]
TAU=[0.05,0.10,0.20]
SIGNED=[Fraction(-1),Fraction(-1,2),Fraction(0),Fraction(1,2),Fraction(1)]
POS=[Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1)]
M=Fraction(5)
KPOS=219.1476037531367
SMINPOS=0.010076217942614964
VIFPOS=909.166134380049
QPOS=1.2636705529477296e-5

def d3(vals):
    return vals[(1,1,1)]-vals[(1,1,0)]-vals[(1,0,1)]-vals[(0,1,1)]+vals[(1,0,0)]+vals[(0,1,0)]+vals[(0,0,1)]-vals[(0,0,0)]

def key(l):
    if l.denominator==1:return str(l.numerator)
    return f'{l.numerator}/{l.denominator}'

def model(R,lam,shifts=(Fraction(1),Fraction(2),Fraction(3))):
    masses=[Fraction(1),Fraction(1),Fraction(1),M]
    da,db,dc=shifts
    def pos(a,b,c):
        xa=lam*da*a
        xb=Fraction(4)+db*b
        xc=Fraction(10)+dc*c
        xd=Fraction(R)-(lam*da*a+db*b+dc*c)/M
        return [xa,xb,xc,xd]
    def V(xs):
        s=Fraction(0)
        for i in range(4):
            for j in range(i+1,4):
                r=xs[j]-xs[i]
                if r<=0: raise ValueError(('ordering',R,lam,xs))
                s-=masses[i]*masses[j]/r
        return s
    def grad(xs):
        g=[Fraction(0)]*4
        for i in range(4):
            for j in range(i+1,4):
                r=xs[j]-xs[i]; mu=masses[i]*masses[j]
                g[i]-=mu/(r*r); g[j]+=mu/(r*r)
        return g
    def A(xs):
        g=grad(xs); return sum(g[i]*g[i]/masses[i] for i in range(4))
    def W(xs):
        s=Fraction(0)
        for i in range(4):
            for j in range(4):
                if i==j:continue
                rij=abs(xs[i]-xs[j])
                for k in range(4):
                    if i==k:continue
                    rik=abs(xs[i]-xs[k])
                    s+=masses[i]*masses[j]*masses[k]/(rij*rik)
        return s/Fraction(2)
    P={b:pos(*b) for b in BITS}
    mind=min(float(P[b][j]-P[b][i]) for b in BITS for i in range(4) for j in range(i+1,4))
    return d3({b:V(P[b]) for b in BITS}), d3({b:A(P[b]) for b in BITS}), d3({b:W(P[b]) for b in BITS}), mind

def coeff_table(lams):
    out={}; minsep=1e99
    for R in RSEL:
        out[str(R)]={}
        for l in lams:
            v,a,w,m=model(R,l); minsep=min(minsep,m)
            out[str(R)][key(l)]={'VN':float(v),'A':float(a),'W':float(w)}
    return out,minsep

Cs,mins=coeff_table(SIGNED)
Cp,minp=coeff_table(POS)

def getc(C,R,l):
    c=C[str(R)][key(l)]
    return -c['VN'],c['A']/12.0,-c['W']

def build(C,lams,eps=1.0,known_only=False):
    rows=[]
    for l in lams:
        lf=float(l)
        for R in RSEL:
            a,f,p=getc(C,R,l)
            for t in TAU:
                row=[a*t,f*t**3,eps*p*t]
                if not known_only: row += [t,lf*t,lf*lf*t]
                rows.append(row)
    return np.array(rows,float)

def structural(X):
    n=np.linalg.norm(X,axis=0);Y=X/n
    _,s,Vt=np.linalg.svd(Y,full_matrices=False)
    rank=int(np.sum(s>1e-10*s[0]))
    return {'rank':rank,'kappa':float(s[0]/s[-1]),'smin':float(s[-1]),'singular_values':[float(x) for x in s],'near_null':[float(x) for x in Vt[-1]]}

def fisher(X):
    n=np.linalg.norm(X,axis=0);Y=X/n
    G=Y.T@Y; invG=np.linalg.inv(G);D=np.diag(1/n);C=D@invG@D
    return float(C[2,2])

ss=structural(build(Cs,SIGNED,1.0,False))
sp=structural(build(Cp,POS,1.0,False))
noise={}
for eps in [1e-6,1e-8]:
    qs=fisher(build(Cs,SIGNED,eps,False)); ks=fisher(build(Cs,SIGNED,eps,True))
    qp=fisher(build(Cp,POS,eps,False)); kp=fisher(build(Cp,POS,eps,True))
    noise[str(eps)]={
      'signed_Q2_vif':qs/ks,
      'signed_q_over_eps':(1/np.sqrt(qs))/eps,
      'positive_Q2_vif':qp/kp,
      'positive_q_over_eps':(1/np.sqrt(qp))/eps,
      'vif_improvement_positive_over_signed':(qp/kp)/(qs/ks),
      'variance_improvement_positive_Q2_over_signed_Q2':qp/qs,
    }
z1=[];z2=[]
for l in SIGNED:
    lf=float(l)
    for R in RSEL:
      for t in TAU:
        z1.append(lf*t);z2.append(lf*lf*t)
parity=float(np.dot(z1,z2))
controls={}
for nm,idx in [('A',0),('B',1),('C',2)]:
    ok=True
    for R in RSEL:
      for l in SIGNED:
        sh=[Fraction(1),Fraction(2),Fraction(3)];sh[idx]=0
        v,a,w,_=model(R,l,tuple(sh));ok=ok and (v==0 and a==0 and w==0)
    controls[nm]=ok
crit=[ss['kappa']<=KPOS/3,ss['smin']>=3*SMINPOS,noise['1e-06']['signed_Q2_vif']<=VIFPOS/3]
classification='SIGNED_AMPLITUDE_PARITY_STRONGLY_IMPROVES_Q2_CALIBRATION_SCOPED' if ss['rank']==6 and sum(crit)>=2 else ('SIGNED_AMPLITUDE_PARITY_MODESTLY_IMPROVES_Q2_CALIBRATION_SCOPED' if ss['rank']==6 and (ss['kappa']<KPOS or ss['smin']>SMINPOS or noise['1e-06']['signed_Q2_vif']<VIFPOS) else 'SIGNED_AMPLITUDE_PARITY_DOES_NOT_IMPROVE_Q2_CALIBRATION_SCOPED')
out={'prereg_commit':'08d16e0c75192345f196cb82f0aaf0bb5c6eb04b','classification':classification,'signed_structural':ss,'positive_recomputed':sp,'noise':noise,'strong_criteria':crit,'controls':{'min_signed_pair_separation_over_ell':mins,'min_positive_pair_separation_over_ell':minp,'lambda0_gravity_exact_zero':all(Cs[str(R)]['0'][x]==0.0 for R in RSEL for x in ['VN','A','W']),'positive_endpoint_matches':all(abs(Cs[str(R)]['1'][x]-Cp[str(R)]['1'][x])<1e-30 for R in RSEL for x in ['VN','A','W']),'delete_one_label_exact_zero':controls,'pure_z1_z2_inner_product':parity},'signed_coefficients':Cs}
raw=json.dumps(out,indent=2,sort_keys=True)
print(raw)
print('SCRIPT_SHA256',hashlib.sha256(open(__file__,'rb').read()).hexdigest())
