#!/usr/bin/env python3
"""Outcome-independent fixed-q equivalence control for SF055A3Q5."""
import json
from pathlib import Path
import numpy as np
import sf055a3q5_piecewise_baseline as q5
import sf055a3_figure2_contraction_assembly as fig

OUT = Path(__file__).resolve().parents[1] / "results/raw/SF055A3Q5_FIXEDQ_CONTROL.json"
TOL = 2e-9


def single_fast(ps, hs, q):
    q = np.asarray(q, float)
    Bq = q5.analytic_landau_basis(q)
    Sq = q5.grav_S_q_diag()
    V5 = q5.vertex_tensor([ps[0],ps[1],ps[2],q,-q], [[hs[0]],[hs[1]],[hs[2]],Bq,Bq], q5.LAMBDA3)[0,0,0]
    t5 = -0.5 * float(np.sum(np.diag(V5) * Sq))

    ell = q + ps[0] + ps[1]
    Bl = q5.analytic_landau_basis(ell)
    Gl = q5.grav_G_diag(ell)
    V4 = q5.vertex_tensor([ps[0],ps[1],q,-ell], [[hs[0]],[hs[1]],Bq,Bl], q5.LAMBDA3)[0,0]
    V3b = q5.vertex_tensor([ps[2],-q,ell], [[hs[2]],Bq,Bl], q5.LAMBDA3)[0]
    bub = 3.0 * float(np.einsum("ij,i,ij,j->", V4,Sq,V3b,Gl,optimize=True))

    e23, e31 = q-ps[1], q+ps[0]
    B23, B31 = q5.analytic_landau_basis(e23), q5.analytic_landau_basis(e31)
    V1 = q5.vertex_tensor([ps[0],q,-e31], [[hs[0]],Bq,B31], q5.LAMBDA3)[0]
    V2 = q5.vertex_tensor([ps[1],-q,e23], [[hs[1]],Bq,B23], q5.LAMBDA3)[0]
    V3 = q5.vertex_tensor([ps[2],-e23,e31], [[hs[2]],B23,B31], q5.LAMBDA3)[0]
    tri = -3.0 * float(np.einsum("ij,i,ik,k,kj,j->", V1,Sq,V2,q5.grav_G_diag(e23),V3,q5.grav_G_diag(e31),optimize=True))

    A=q5.ghost_matrix(ps[0],hs[0],q); B=q5.ghost_matrix(ps[1],hs[1],e23); C=q5.ghost_matrix(ps[2],hs[2],e31)
    gh = 6.0*q5.ghost_S_q_scalar()*q5.ghost_G_scalar(e23)*q5.ghost_G_scalar(e31)*float(np.trace(A@B@C))
    return {"T5_GRAV":t5,"B43_GRAV":bub,"T333_GRAV":tri,"T333_GHOST":gh}


def main():
    ps, hs = fig.sym_external()
    rows=[]
    for q in fig.q_controls():
        got=single_fast(ps,hs,q)
        ref={
          "T5_GRAV":fig.t5_value(ps,hs,q)[0],
          "B43_GRAV":fig.bubble_value(ps,hs,q)[0],
          "T333_GRAV":fig.triangle_value(ps,hs,q)[0],
          "T333_GHOST":fig.ghost_value(ps,hs,q)[0],
        }
        errs={k:abs(got[k]-ref[k]) for k in ref}
        passed=all(errs[k] <= TOL*(1+abs(ref[k])) for k in ref)
        rows.append({"q":np.asarray(q,float).tolist(),"got":got,"reference":ref,"abs_errors":errs,"pass":passed})
    scientific_pass=all(r["pass"] for r in rows)
    data={"classification":"PASS_Q5_FIXEDQ_TOPOLOGY_EQUIVALENCE" if scientific_pass else "BLOCKED_Q5_FIXEDQ_TOPOLOGY_EQUIVALENCE",
          "scientific_pass":scientific_pass,"records":rows,"C3_enabled":False}
    OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(data,indent=2,sort_keys=True)+"\n")
    print(json.dumps(data,indent=2,sort_keys=True))
    if not scientific_pass: raise SystemExit(1)

if __name__=="__main__": main()
