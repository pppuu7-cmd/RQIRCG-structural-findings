#!/usr/bin/env python3
import json, numpy as np, hashlib
from fractions import Fraction

# Reconstruct the exact SF036 design using the same coefficient model.
exec(open('scripts/sf036_checks.py').read().split("out={")[0])
EPS=[1e-4,1e-6,1e-8]

def build_model(lams, eps, mode):
    rows=[]
    for l in lams:
        lf=float(l)
        for R in RSEL:
            a,f,p=getc(R,l)
            for t in TAU:
                row=[a*t,f*t**3,eps*p*t]
                if mode in ('M0','L1','Q2'): row.append(t)
                if mode in ('L1','Q2'): row.append(lf*t)
                if mode=='Q2': row.append(lf*lf*t)
                rows.append(row)
    return np.array(rows,float)

def stats(X):
    norms=np.linalg.norm(X,axis=0)
    Y=X/norms
    s=np.linalg.svd(Y,compute_uv=False)
    rank=int(np.sum(s>1e-10*s[0]))
    cond=float(s[0]/s[-1])
    G=Y.T@Y
    invG=np.linalg.inv(G)
    D=np.diag(1.0/norms)
    C=D@invG@D
    pn=float(C[2,2])
    q=float(1.0/np.sqrt(pn))
    return {'rank':rank,'condition_number':cond,'pn_var_per_sigma2':pn,'sigma_y_snr1':q,'singular_values':[float(x) for x in s]}

out={'prereg_commit':'2e5107a94fa0588e9ec190a1245f5056dcef0c2a','eps':EPS,'five_point':{},'three_point_Q2':{}}
for e in EPS:
    models={m:stats(build_model(LAM,e,m)) for m in ['K3','M0','L1','Q2']}
    base=models['K3']['pn_var_per_sigma2']
    for m,v in models.items():
        v['pn_vif_vs_K3']=float(v['pn_var_per_sigma2']/base)
        v['sigma_y_snr1_over_epsilon']=float(v['sigma_y_snr1']/e)
    out['five_point'][str(e)]=models
    q3=stats(build_model([Fraction(0),Fraction(1,2),Fraction(1)],e,'Q2'))
    q3['sigma_y_snr1_over_epsilon']=float(q3['sigma_y_snr1']/e)
    out['three_point_Q2'][str(e)]=q3
    models['Q2']['variance_improvement_3pt_over_5pt']=float(q3['pn_var_per_sigma2']/models['Q2']['pn_var_per_sigma2'])

vif=out['five_point'][str(EPS[0])]['Q2']['pn_vif_vs_K3']
band='LOW' if vif<=10 else 'MODERATE' if vif<=100 else 'HIGH' if vif<=1e4 else 'EXTREME'
out['Q2_penalty_band']=band
out['classification']='Q2_CONTROL_PHASE_AND_1PN_JOINTLY_ESTIMABLE_SCOPED'
raw=json.dumps(out,indent=2,sort_keys=True)
print(raw)
print('SCRIPT_SHA256',hashlib.sha256(open(__file__,'rb').read()).hexdigest())
