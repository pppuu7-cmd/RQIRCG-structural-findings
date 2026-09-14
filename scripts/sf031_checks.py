#!/usr/bin/env python3
import json, hashlib
import numpy as np

RSEL=[60,160,400]
TAUSEL=[0.05,0.1,0.2]
EPS=[1e-2,1e-4,1e-6,1e-8]

# Frozen authoritative SF029 coefficients for the exact SF030/SF031 design rows.
# Source: results/raw/SF029_CHECKS.json, commit fc11740ea476253b6755d2af90a0cd763ee6ee36.
COEFF={
  60: {'dV':-3.355587720633548e-06,'dA':-0.0001328485660646396,'dW':0.0019807147976313496},
  160:{'dV':-4.6825312027803854e-08,'dA':-0.00013311145959924833,'dW':0.002098924215918627},
  400:{'dV':-1.0799848261120293e-09,'dA':-0.00013311569896983712,'dW':0.0021137018589146993},
}

def base(eps):
    rows=[]
    for R in RSEL:
        c=COEFF[R]
        for t in TAUSEL:
            rows.append([-c['dV']*t,(c['dA']/12.0)*t**3,(-c['dW']*eps)*t])
    return np.asarray(rows,float)

def nuis(which):
    cols=[]
    if which in ('B','D'):
        cols.append(np.ones(9))
    if which in ('C','D'):
        cols.append(np.asarray([t for R in RSEL for t in TAUSEL],float))
    return np.column_stack(cols) if cols else np.empty((9,0))

def stable_metrics(A,pn_index=2):
    norms=np.linalg.norm(A,axis=0)
    if np.any(norms==0):
        return {'rank':0,'condition_number_norm':float('inf'),'singular_values_norm':[],'g_PN':float('inf')}
    B=A/norms
    s=np.linalg.svd(B,compute_uv=False)
    rank=int(np.sum(s > 1e-10*s[0]))
    cond=float(s[0]/s[-1]) if s[-1]>0 else float('inf')
    g=float('inf')
    if rank==A.shape[1]:
        # A = B diag(norms).  Compute the CRLB in the normalized coordinates,
        # then rescale back.  This avoids falsely treating a very small but
        # nonzero epsilon_PN column as a mathematical rank loss.
        covB=np.linalg.inv(B.T@B)
        g=float(np.sqrt(covB[pn_index,pn_index])/norms[pn_index])
    return {
        'rank':rank,
        'condition_number_norm':cond,
        'singular_values_norm':[float(x) for x in s],
        'column_norms':[float(x) for x in norms],
        'g_PN':g,
        'sigma_y_SNR1':(1.0/g if np.isfinite(g) else 0.0),
        'sigma_y_SNR5':(1.0/(5.0*g) if np.isfinite(g) else 0.0),
    }

models={}
for eps in EPS:
    models[str(eps)]={}
    A0=base(eps)
    ma=stable_metrics(A0)
    gA=ma['g_PN']
    for label in ['A','B','C','D']:
        A=np.column_stack([A0,nuis(label)]) if label!='A' else A0
        m=stable_metrics(A)
        m['VIF_PN']=float((m['g_PN']/gA)**2) if np.isfinite(m['g_PN']) else float('inf')
        models[str(eps)][label]=m

all_full=all(
    models[str(e)][m]['rank']==(3 + (1 if m in ('B','C') else 2 if m=='D' else 0))
    for e in EPS for m in ['A','B','C','D']
)
strong=max(models[str(e)]['D']['VIF_PN'] for e in EPS)>10
classification=(
    'PN_CALIBRATION_REMAINS_ESTIMABLE_UNDER_FROZEN_COMMON_MODE_NUISANCES_SCOPED'
    if all_full else 'PN_CALIBRATION_DEGENERATE_WITH_FROZEN_COMMON_MODE_SCOPED'
)
secondary=(
    'COMMON_MODE_NUISANCE_STRONGLY_INFLATES_PN_PRECISION_SCOPED'
    if strong else 'NO_STRONG_COMMON_MODE_VARIANCE_INFLATION_ON_FROZEN_GRID'
)

scaling={}
for label in ['A','B','C','D']:
    scaling[label]={str(e):models[str(e)][label]['sigma_y_SNR1']/e for e in EPS}

out={
    'prereg_commit':'f825f57e4a57b47effed68e34d2ab747a4881d15',
    'sf029_source_commit':'fc11740ea476253b6755d2af90a0cd763ee6ee36',
    'design':{'R_over_ell':RSEL,'tau':TAUSEL,'epsilon_PN':EPS},
    'models':models,
    'sigma_y_SNR1_over_epsilon':scaling,
    'classification':classification,
    'secondary':secondary,
    'rank_method':'column-normalized SVD; CRLB from normalized Gram matrix rescaled by physical column norms',
    'implementation_note':'An unnormalized-SVD rank check was rejected before terminalization because nonzero epsilon column scaling must not change mathematical rank.'
}
raw=json.dumps(out,indent=2,sort_keys=True)
print(raw)
with open('SF031_CHECKS.json','w') as f: f.write(raw+'\n')
with open(__file__,'rb') as f: print('SCRIPT_SHA256',hashlib.sha256(f.read()).hexdigest())
