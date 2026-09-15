#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
import json, hashlib
import numpy as np

BITS=list(product([0,1], repeat=3))
RSEL=[60,160,400]
LAM=[Fraction(0),Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1)]
TAU=[0.05,0.10,0.20]
M=Fraction(5)
BASE_K=899.7091025733095
BASE_S=0.002445567828550082

def d3(vals):
    return (vals[(1,1,1)]-vals[(1,1,0)]-vals[(1,0,1)]-vals[(0,1,1)]
            +vals[(1,0,0)]+vals[(0,1,0)]+vals[(0,0,1)]-vals[(0,0,0)])

def key(l):
    if l==0:return '0'
    if l==1:return '1'
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
                r=xs[j]-xs[i]; assert r>0
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
    return d3({b:V(P[b]) for b in BITS}), d3({b:A(P[b]) for b in BITS}), d3({b:W(P[b]) for b in BITS})

coeff={}
for R in RSEL:
    coeff[str(R)]={}
    for l in LAM:
        v,a,w=model(R,l)
        coeff[str(R)][key(l)]={'delta3_VN_float':float(v),'delta3_A_float':float(a),'delta3_W1_float':float(w)}

controls={}
for nm,idx in [('A',0),('B',1),('C',2)]:
    ok=True
    for R in RSEL:
        for l in LAM:
            sh=[Fraction(1),Fraction(2),Fraction(3)]; sh[idx]=0
            v,a,w=model(R,l,tuple(sh)); ok=ok and (v==0 and a==0 and w==0)
    controls[nm]=ok

def getc(R,l):
    c=coeff[str(R)][key(l)]
    return -c['delta3_VN_float'], c['delta3_A_float']/12.0, -c['delta3_W1_float']

def build(lams=LAM,Rs=RSEL,taus=TAU):
    rows=[]
    for l in lams:
        lf=float(l)
        for R in Rs:
            a,f,p=getc(R,l)
            for t in taus:
                rows.append([a*t,f*t**3,p*t,t,lf*t,lf*lf*t])
    return np.array(rows,float)

def metrics(X):
    n=np.linalg.norm(X,axis=0); Y=X/n
    _,s,Vt=np.linalg.svd(Y,full_matrices=False)
    rank=int(np.sum(s>1e-10*s[0])); k=float(s[0]/s[-1])
    return {'rank':rank,'condition_number':k,'smin':float(s[-1]),'singular_values':[float(x) for x in s],
            'near_null_vector':[float(x) for x in Vt[-1]]}

full=metrics(build())
three=metrics(build([Fraction(0),Fraction(1,2),Fraction(1)]))
leave={key(l):metrics(build([x for x in LAM if x!=l])) for l in [Fraction(1,4),Fraction(1,2),Fraction(3,4)]}
single_R={str(R):metrics(build(Rs=[R])) for R in RSEL}
single_tau={str(t):metrics(build(taus=[t])) for t in TAU}
strong=(full['rank']==6 and full['condition_number']<=BASE_K/3 and full['smin']>=3*BASE_S)
modest=(full['rank']==6 and full['condition_number']<BASE_K)
classification=('FIVE_POINT_AMPLITUDE_LADDER_STRONGLY_IMPROVES_Q2_CONDITIONING_SCOPED' if strong else
                'FIVE_POINT_AMPLITUDE_LADDER_MODESTLY_IMPROVES_Q2_CONDITIONING_SCOPED' if modest else
                'ADDITIONAL_UNIFORM_AMPLITUDE_POINTS_DO_NOT_MATERIALLY_BREAK_Q2_NEAR_DEGENERACY_SCOPED')
out={
 'prereg_commit':'b75f25c587ba32c55750ab40ce77a11edf4a6c34',
 'design':{'R':RSEL,'lambda_A':[key(x) for x in LAM],'tau':TAU,'rows':45},
 'classification':classification,
 'full':full,
 'three_point_comparator':three,
 'improvement':{'kappa_factor':BASE_K/full['condition_number'],'smin_factor':full['smin']/BASE_S},
 'leave_one_interior':leave,
 'single_R':single_R,
 'single_tau':single_tau,
 'controls':{'lambda0_gravity_exact_zero':all(coeff[str(R)]['0'][k]==0.0 for R in RSEL for k in ['delta3_VN_float','delta3_A_float','delta3_W1_float']),
             'delete_one_label_exact_zero':controls},
 'coefficients_float':coeff
}
raw=json.dumps(out,indent=2,sort_keys=True)
print(raw)
print('SCRIPT_SHA256',hashlib.sha256(open(__file__,'rb').read()).hexdigest())
