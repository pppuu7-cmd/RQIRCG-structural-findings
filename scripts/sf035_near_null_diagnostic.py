#!/usr/bin/env python3
import json, numpy as np, hashlib

D=json.load(open('SF035_CHECKS.json'))
Rs=D['frozen_design']['R']; taus=D['frozen_design']['tau']; lams=[0.0,0.5,1.0]

def coeff(R,lam):
    k='0' if lam==0 else ('1/2' if lam==0.5 else '1')
    c=D['coefficients_float'][str(R)][k]
    return -c['delta3_VN_float'], c['delta3_A_float']/12.0, -c['delta3_W1_float']

def build(q=False):
    rows=[]
    for l in lams:
        for R in Rs:
            a,f,p=coeff(R,l)
            for t in taus:
                row=[a*t,f*t**3,p*t,t,l*t]
                if q: row.append(l*l*t)
                rows.append(row)
    return np.array(rows,float)

def near(X,names):
    n=np.linalg.norm(X,axis=0); Y=X/n
    _,s,Vt=np.linalg.svd(Y,full_matrices=False)
    return {'smin':float(s[-1]),'condition_number':float(s[0]/s[-1]),
            'near_null_vector':{k:float(v) for k,v in zip(names,Vt[-1])}}

out={
 'L1_full':near(build(False),['app','fb','1PN','z0','z1']),
 'Q2_full':near(build(True),['app','fb','1PN','z0','z1','z2'])
}
print(json.dumps(out,indent=2,sort_keys=True))
print('SCRIPT_SHA256',hashlib.sha256(open(__file__,'rb').read()).hexdigest())
