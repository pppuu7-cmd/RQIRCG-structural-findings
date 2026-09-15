#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
import json, hashlib
import numpy as np

BITS=list(product([0,1], repeat=3))
RSEL=[60,160,400]
LAM=[Fraction(0),Fraction(1,2),Fraction(1)]
TAU=[0.05,0.10,0.20]
M=Fraction(5)

def d3(vals):
    return (vals[(1,1,1)]-vals[(1,1,0)]-vals[(1,0,1)]-vals[(0,1,1)]
            +vals[(1,0,0)]+vals[(0,1,0)]+vals[(0,0,1)]-vals[(0,0,0)])

def fr(x):
    if isinstance(x,Fraction):
        return f"{x.numerator}/{x.denominator}" if x.denominator!=1 else str(x.numerator)
    return x

def model(R,lam,shifts=(Fraction(1),Fraction(2),Fraction(3))):
    masses=[Fraction(1),Fraction(1),Fraction(1),M]
    da,db,dc=shifts
    def positions(a,b,c):
        xa=lam*da*a
        xb=Fraction(4)+db*b
        xc=Fraction(10)+dc*c
        xd=Fraction(R)-(lam*da*a+db*b+dc*c)/M
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
                g[i]-=mu/(r*r); g[j]+=mu/(r*r)
        return g
    def Aval(xs):
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
    A={b:Aval(pos[b]) for b in BITS}
    W={b:W1(pos[b]) for b in BITS}
    return d3(V),d3(A),d3(W)

coeff={}
for R in RSEL:
    coeff[str(R)]={}
    for lam in LAM:
        v,a,w=model(R,lam)
        coeff[str(R)][fr(lam)]={
            'delta3_VN':fr(v),'delta3_A':fr(a),'delta3_W1':fr(w),
            'delta3_VN_float':float(v),'delta3_A_float':float(a),'delta3_W1_float':float(w)
        }

controls={}
for name,idx in [('A',0),('B',1),('C',2)]:
    ok=True
    maxabs=0.0
    for R in RSEL:
        for lam in LAM:
            sh=[Fraction(1),Fraction(2),Fraction(3)]
            sh[idx]=Fraction(0)
            v,a,w=model(R,lam,tuple(sh))
            maxabs=max(maxabs,abs(float(v)),abs(float(a)),abs(float(w)))
            ok = ok and (v==0 and a==0 and w==0)
    controls[f'delete_{name}']={'exact_zero_all_cells':ok,'max_abs_float':maxabs}

def cget(R,lam):
    c=coeff[str(R)][fr(lam)]
    return -c['delta3_VN_float'], c['delta3_A_float']/12.0, -c['delta3_W1_float']

def build(lams, Rs=RSEL, taus=TAU, quadratic=False):
    rows=[]
    for lamF in lams:
        lf=float(lamF)
        for R in Rs:
            fa,ff,fp=cget(R,lamF)
            for t in taus:
                row=[fa*t, ff*t**3, fp*t, t, lf*t]
                if quadratic: row.append(lf*lf*t)
                rows.append(row)
    return np.array(rows,float)

def metrics(X):
    norms=np.linalg.norm(X,axis=0)
    nonzero=norms>0
    if not np.all(nonzero):
        Y=np.zeros_like(X)
        Y[:,nonzero]=X[:,nonzero]/norms[nonzero]
    else:
        Y=X/norms
    s=np.linalg.svd(Y,compute_uv=False)
    rank=int(np.sum(s>1e-10*s[0])) if len(s) and s[0]>0 else 0
    cond=float(s[0]/s[-1]) if len(s) and s[-1]>0 else float('inf')
    return {'shape':list(X.shape),'rank':rank,'singular_values':[float(x) for x in s],
            'condition_number':cond,'column_norms':[float(x) for x in norms]}

full_L1=metrics(build(LAM,quadratic=False))
full_Q2=metrics(build(LAM,quadratic=True))
endpoint_L1=metrics(build([Fraction(0),Fraction(1)],quadratic=False))
endpoint_Q2=metrics(build([Fraction(0),Fraction(1)],quadratic=True))
lam1_L1=metrics(build([Fraction(1)],quadratic=False))
lam1_Q2=metrics(build([Fraction(1)],quadratic=True))

single_R_L1={str(R):metrics(build(LAM,Rs=[R],quadratic=False)) for R in RSEL}
single_R_Q2={str(R):metrics(build(LAM,Rs=[R],quadratic=True)) for R in RSEL}
single_tau_L1={str(t):metrics(build(LAM,taus=[t],quadratic=False)) for t in TAU}
single_tau_Q2={str(t):metrics(build(LAM,taus=[t],quadratic=True)) for t in TAU}

classify=lambda m,n: ('FULL_RANK_MODERATE' if m['rank']==n and m['condition_number']<=50 else
                      'FULL_RANK_ILL_CONDITIONED' if m['rank']==n else 'DEGENERATE')

out={
 'prereg_commit':'854c33c5fde4092b76c506d39f6eea056784a182',
 'frozen_design':{'R':RSEL,'lambda_A':[fr(x) for x in LAM],'tau':TAU,'rows':27},
 'exact_coefficients':coeff,
 'delete_one_label_controls':controls,
 'L1':{
    'full':full_L1,'classification':classify(full_L1,5),
    'endpoint_0_1':endpoint_L1,
    'lambda1_only_negative_control':lam1_L1,
    'single_R':single_R_L1,'single_tau':single_tau_L1,
 },
 'Q2':{
    'full':full_Q2,'classification':classify(full_Q2,6),
    'endpoint_0_1':endpoint_Q2,
    'lambda1_only_negative_control':lam1_Q2,
    'single_R':single_R_Q2,'single_tau':single_tau_Q2,
 },
 'endpoint_checks':{
    'lambda0_all_gravity_exact_zero': all(coeff[str(R)]['0']['delta3_VN']=='0' and coeff[str(R)]['0']['delta3_A']=='0' and coeff[str(R)]['0']['delta3_W1']=='0' for R in RSEL),
 },
}
raw=json.dumps(out,indent=2,sort_keys=True)
print(raw)
print('SCRIPT_SHA256',hashlib.sha256(open(__file__,'rb').read()).hexdigest())
