import json
import numpy as np
from sf055b_direct_c3_verifier import tt_basis, mixed_derivative

target=2.791666666666668
ps=[np.array([1.,0,0,0]),np.array([0,1.,0,0]),np.array([0,0,1.,0]),np.array([-1.,-1.,-1.,0])]
hs=[tt_basis(p)[1] for p in ps]
pairs=[(0.04,0.02),(0.02,0.01),(0.01,0.005),(0.008,0.004)]
rows=[]
for h1,h2 in pairs:
    d1,_=mixed_derivative(ps,hs,h1); d2,_=mixed_derivative(ps,hs,h2); dr=(4*d2-d1)/3.0
    rows.append({'h1':h1,'h2':h2,'D_h1':d1,'D_h2':d2,'D_R':dr,'error_vs_nilpotent':dr-target})
print(json.dumps({'scope':'POSTOUTCOME_DIAGNOSTIC_ONLY_DOES_NOT_CHANGE_SF055B_CLASSIFICATION','target':target,'rows':rows},indent=2,sort_keys=True))
