#!/usr/bin/env python3
import json, hashlib
import numpy as np

LAMS=[-1.0,-0.5,0.0,0.5,1.0]
TAUS=[0.05,0.10,0.20]

# Parameter order: zeta0,zetaA,zetaB,zetaC.
def vec(config,l):
    if config=='S':  la,lb,lc=l,1.0,1.0
    elif config=='NA': la,lb,lc=0.0,1.0,1.0
    elif config=='NB': la,lb,lc=l,0.0,1.0
    elif config=='NC': la,lb,lc=l,1.0,0.0
    else: raise ValueError(config)
    return np.array([1.0,la,lb,lc],float)

def build(configs):
    rows=[]
    for l in LAMS:
      for t in TAUS:
        for c in configs:
          rows.append(t*vec(c,l))
    return np.vstack(rows)

def metrics(X):
    norms=np.linalg.norm(X,axis=0)
    Y=X/norms
    s=np.linalg.svd(Y,compute_uv=False)
    rank=int(np.sum(s>1e-10*s[0]))
    cond=float('inf') if s[-1]<1e-14 else float(s[0]/s[-1])
    return {'shape':list(X.shape),'rank':rank,'condition_number':cond,'singular_values':[float(x) for x in s]}

full=metrics(build(['S','NA','NB','NC']))
null_only=metrics(build(['NA','NB','NC']))
science_only=metrics(build(['S']))
science_NA=metrics(build(['S','NA']))
science_NB=metrics(build(['S','NB']))
science_NC=metrics(build(['S','NC']))

# Exact coefficient identities for the frozen linear model.
identities={
  'S_minus_NA':'zeta_A * lambda_A',
  'S_minus_NB':'zeta_B',
  'S_minus_NC':'zeta_C',
  'zeta0_recovery':'e.g. zeta_NA - zeta_B - zeta_C'
}

# Mandatory zeta_AB lambda_A lambda_B countermodel: report contamination of the three differences.
counter=[]
for l in LAMS:
  ab={'S':l,'NA':0.0,'NB':0.0,'NC':l}
  counter.append({'lambda_A':l,
    'S_minus_NA_zetaAB_coeff':ab['S']-ab['NA'],
    'S_minus_NB_zetaAB_coeff':ab['S']-ab['NB'],
    'S_minus_NC_zetaAB_coeff':ab['S']-ab['NC']})

out={
 'prereg_commit':'bcbe70def315877ba5148f725d86444513f64cf1',
 'gravity_null_authority':'inherited exact delete-A/B/C controls from SF038 across signed lambda_A grid',
 'full_S_NA_NB_NC':full,
 'null_only_NA_NB_NC':null_only,
 'science_only_negative_control':science_only,
 'science_plus_NA_negative_control':science_NA,
 'science_plus_NB_diagnostic':science_NB,
 'science_plus_NC_diagnostic':science_NC,
 'exact_identities':identities,
 'zeta_AB_countermodel':counter,
 'classification':'TRIPLE_NULL_CONTROLS_LOCALIZE_LINEAR_CUBIC_CROSSTALK_SCOPED'
}
raw=json.dumps(out,indent=2,sort_keys=True)
print(raw)
print('SCRIPT_SHA256',hashlib.sha256(open(__file__,'rb').read()).hexdigest())
