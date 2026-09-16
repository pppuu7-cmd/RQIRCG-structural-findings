#!/usr/bin/env python3
"""Source/JIT n=2..5 equivalence control for SF055A3Q6."""
import json
from pathlib import Path
import numpy as np
import sf055a3q5_piecewise_baseline as q5

OUT=Path(__file__).resolve().parents[1]/'results/raw/SF055A3Q6_SOURCE_JIT_CONTROL.json'

def main():
    base=q5.base; seed=q5.seed; fast=q5.fast
    p2=[np.array([.37,-.22,.19,.41]),np.array([-.37,.22,-.19,-.41])]
    cases=[(p2,[base.dense_tt(p2[0],0),base.dense_tt(p2[1],1)],-.05),
           (q5.UNIT_PS,[base.dense_tt(p,i) for i,p in enumerate(q5.UNIT_PS)],-.7)]
    p4=[np.array([1.,0,0,0]),np.array([0,1.,0,0]),np.array([0,0,1.,0]),np.array([-1.,-1.,-1.,0])]
    p5=[np.array([1.,0,0,0]),np.array([0,1.,0,0]),np.array([0,0,1.,0]),np.array([0,0,0,1.]),np.array([-1.,-1.,-1.,-1.])]
    cases += [(p4,[base.dense_tt(p,i) for i,p in enumerate(p4)],-.7),(p5,[base.dense_tt(p,i) for i,p in enumerate(p5)],-.7)]
    rows=[]
    for ps,hs,lam in cases:
        ref=seed.eh_vertex_fourier(ps,hs,lam); got=float(fast.eh_vertex_fourier(np.asarray(ps),np.asarray(hs),lam)); err=abs(got-ref)
        rows.append({'n':len(ps),'reference':ref,'jit':got,'abs_error':err,'pass':bool(err<=2e-11*(1+abs(ref)))})
    ok=all(r['pass'] for r in rows)
    d={'classification':'PASS_Q6_SOURCE_JIT_EQUIVALENCE' if ok else 'BLOCKED_Q6_SOURCE_JIT_EQUIVALENCE','scientific_pass':ok,'records':rows,'C3_enabled':False}
    OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(d,indent=2,sort_keys=True)+'\n'); print(json.dumps(d,indent=2,sort_keys=True))
    if not ok: raise SystemExit(1)
if __name__=='__main__': main()
