#!/usr/bin/env python3
import json, hashlib
import numpy as np

RSEL=[60,160,400]
TAUSEL=[0.05,0.1,0.2]
EPS=[1e-2,1e-4,1e-6,1e-8]
COEFF={
  60: {'dV':-3.355587720633548e-06,'dA':-0.0001328485660646396,'dW':0.0019807147976313496},
  160:{'dV':-4.6825312027803854e-08,'dA':-0.00013311145959924833,'dW':0.002098924215918627},
  400:{'dV':-1.0799848261120293e-09,'dA':-0.00013311569896983712,'dW':0.0021137018589146993},
}
TAU=np.array([t for R in RSEL for t in TAUSEL],float)
ONES=np.ones(9)

def science(eps):
    rows=[]
    for R in RSEL:
        c=COEFF[R]
        for t in TAUSEL:
            rows.append([-c['dV']*t,(c['dA']/12.0)*t**3,(-c['dW']*eps)*t])
    return np.asarray(rows,float)

def metrics(A,pn=2):
    norms=np.linalg.norm(A,axis=0)
    B=A/norms
    s=np.linalg.svd(B,compute_uv=False)
    rank=int(np.sum(s>1e-10*s[0]))
    out={'rank':rank,'ncol':A.shape[1],'cond_norm':float(s[0]/s[-1]),'s_norm':[float(x) for x in s]}
    if rank==A.shape[1]:
        covB=np.linalg.inv(B.T@B)
        g=float(np.sqrt(covB[pn,pn])/norms[pn])
        out.update(g_PN=g,sigma_y_SNR1=1/g,sigma_y_SNR5=1/(5*g))
    else:
        out.update(g_PN=float('inf'),sigma_y_SNR1=0.0,sigma_y_SNR5=0.0)
    return out

def build(eps, model):
    X=science(eps)
    Z=np.zeros((9,3))
    if model=='S0':
        return np.c_[X,ONES,TAU]
    if model=='S1':
        return np.r_[np.c_[X,ONES,TAU], np.c_[Z,ONES,TAU]]
    if model=='S2':
        # shared offset; independent science/control tau-linear nuisance
        top=np.c_[X,ONES,TAU,np.zeros(9)]
        bot=np.c_[Z,ONES,np.zeros(9),TAU]
        return np.r_[top,bot]
    if model=='S3':
        # shared tau-linear nuisance; independent science/control offsets
        top=np.c_[X,TAU,ONES,np.zeros(9)]
        bot=np.c_[Z,TAU,np.zeros(9),ONES]
        return np.r_[top,bot]
    if model=='S4':
        # independent offset and tau-linear nuisance in science/control
        top=np.c_[X,ONES,TAU,np.zeros(9),np.zeros(9)]
        bot=np.c_[Z,np.zeros(9),np.zeros(9),ONES,TAU]
        return np.r_[top,bot]
    raise ValueError(model)

out={'prereg_commit':'66e7b301200ca7b450f0bba38b4edce872166762','models':{},'design':{'science_rows':9,'control_rows':9,'R':RSEL,'tau':TAUSEL,'epsilon':EPS}}
for eps in EPS:
    iid=metrics(science(eps)); gA=iid['g_PN']
    cells={}
    for model in ['S0','S1','S2','S3','S4']:
        m=metrics(build(eps,model))
        m['VIF_vs_iid_A']=(m['g_PN']/gA)**2 if np.isfinite(m['g_PN']) else float('inf')
        cells[model]=m
    v0=cells['S0']['g_PN']**2
    for model in ['S1','S2','S3','S4']:
        cells[model]['variance_improvement_vs_S0']=v0/(cells[model]['g_PN']**2) if np.isfinite(cells[model]['g_PN']) else 0.0
    cells['S0']['variance_improvement_vs_S0']=1.0
    out['models'][str(eps)]=cells

fullS1=all(out['models'][str(e)]['S1']['rank']==out['models'][str(e)]['S1']['ncol'] for e in EPS)
vifS1=max(out['models'][str(e)]['S1']['VIF_vs_iid_A'] for e in EPS)
impS1=min(out['models'][str(e)]['S1']['variance_improvement_vs_S0'] for e in EPS)
impS4=max(abs(out['models'][str(e)]['S4']['variance_improvement_vs_S0']-1) for e in EPS)
if fullS1 and vifS1<100 and impS1>=100 and impS4<=0.01:
    cls='MATCHED_NULL_CONTROL_BREAKS_COMMON_MODE_PN_NEAR_DEGENERACY_SCOPED'
elif fullS1 and impS1>10:
    cls='NULL_CONTROL_PARTIALLY_CALIBRATES_COMMON_MODE_SCOPED'
else:
    cls='MATCHED_NULL_CONTROL_DOES_NOT_RESOLVE_PN_PRECISION_BOTTLENECK_SCOPED'

out['aggregate']={
    'S1_full_rank_all_epsilon':fullS1,
    'S1_max_VIF_vs_iid':vifS1,
    'S1_min_variance_improvement_vs_S0':impS1,
    'S4_max_fractional_improvement_departure_from_one':impS4
}
out['classification']=cls
out['interpretation_qualification']='NULL_CONTROL_CALIBRATION_BLOCKED_BY_UNVALIDATED_SHARED_NUISANCE_MAP'
raw=json.dumps(out,indent=2,sort_keys=True)
print(raw)
with open('SF032_CHECKS.json','w') as f: f.write(raw+'\n')
with open(__file__,'rb') as f: print('SCRIPT_SHA256',hashlib.sha256(f.read()).hexdigest())
