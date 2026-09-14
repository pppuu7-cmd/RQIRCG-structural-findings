#!/usr/bin/env python3
import json, hashlib
import numpy as np

RSEL=[60,160,400]
TAUSEL=[0.05,0.1,0.2]
EPS=[1e-2,1e-4,1e-6,1e-8]

with open('results/raw/SF029_CHECKS.json') as f:
    D=json.load(f)

def coeffs(R):
    c=D['R_lane'][str(R)]
    return -c['delta3_VN_float'], c['delta3_A_float']/12.0, -c['delta3_W1_float']

def build(Rs,taus,physical_eps=None):
    rows=[]
    for R in Rs:
        fa,ff,fp=coeffs(R)
        for t in taus:
            rows.append([fa*t, ff*t**3, (physical_eps if physical_eps is not None else 1.0)*fp*t])
    return np.array(rows,float)

def normalize_cols(X):
    n=np.linalg.norm(X,axis=0)
    return X/n,n

def metrics(X, normalize=True):
    Y,n=(normalize_cols(X) if normalize else (X,np.ones(X.shape[1])))
    s=np.linalg.svd(Y,compute_uv=False)
    tol=1e-10*s[0]
    rank=int(np.sum(s>tol))
    cond=float(s[0]/s[-1]) if s[-1]>0 else float('inf')
    C=np.corrcoef(Y,rowvar=False)
    return {
        'rank':rank,
        'singular_values':[float(x) for x in s],
        'condition_number':cond,
        'column_norms':[float(x) for x in n],
        'correlation_matrix':C.tolist(),
    }

full=metrics(build(RSEL,TAUSEL),True)
leave_R={}
for drop in RSEL:
    leave_R[str(drop)]=metrics(build([r for r in RSEL if r!=drop],TAUSEL),True)
leave_tau={}
for drop in TAUSEL:
    leave_tau[str(drop)]=metrics(build(RSEL,[t for t in TAUSEL if t!=drop]),True)
single_R={str(r):metrics(build([r],TAUSEL),True) for r in RSEL}
single_tau={str(t):metrics(build(RSEL,[t]),True) for t in TAUSEL}
physical={str(e):metrics(build(RSEL,TAUSEL,e),False) for e in EPS}

pass_full=full['rank']==3 and full['condition_number']<=10
pass_leave_R=all(v['rank']==3 and v['condition_number']<=25 for v in leave_R.values())
pass_leave_tau=all(v['rank']==3 and v['condition_number']<=25 for v in leave_tau.values())
pass_single_R=all(v['rank']<=2 for v in single_R.values())
classification=(
    'KNOWN_PHYSICS_COHERENCE_COMPONENTS_STRUCTURALLY_IDENTIFIABLE_SCOPED'
    if pass_full and pass_leave_R and pass_leave_tau and pass_single_R
    else ('IDENTIFIABLE_BUT_ILL_CONDITIONED_SCOPED' if full['rank']==3
          else 'KNOWN_PHYSICS_COMPONENT_DEGENERACY_SURVIVES_SCOPED')
)

out={
    'prereg_commit':'0fa7251021afc5c230578c5c933b1e11d78c3a3d',
    'design':{'R_over_ell':RSEL,'tau':TAUSEL,'rows':9},
    'basis_definition':{
        'app':'-Delta3 V_N(R) * tau',
        'feedback':'Delta3 A_N(R)/12 * tau^3',
        '1PN':'-Delta3 V_static^1PN(R) * tau; multiply by epsilon_PN only in physical dynamic-range matrix',
    },
    'full_shape':full,
    'leave_one_R_out':leave_R,
    'leave_one_tau_out':leave_tau,
    'single_R_negative_controls':single_R,
    'single_tau_R_only_controls':single_tau,
    'physical_dynamic_range':physical,
    'aggregate_checks':{
        'full_pass':bool(pass_full),
        'leave_one_R_pass':bool(pass_leave_R),
        'leave_one_tau_pass':bool(pass_leave_tau),
        'single_R_negative_control_pass':bool(pass_single_R),
    },
    'classification':classification,
}
raw=json.dumps(out,indent=2,sort_keys=True)
print(raw)
with open('results/raw/SF030_CHECKS.json','w') as f: f.write(raw+'\n')
with open(__file__,'rb') as f: print('SCRIPT_SHA256',hashlib.sha256(f.read()).hexdigest())
