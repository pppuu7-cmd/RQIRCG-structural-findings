#!/usr/bin/env python3
"""Aggregate SF055A3Q5 piecewise matrix under the historical frozen criteria."""
import argparse
import json
import math
from pathlib import Path

NSEQ=[8,12,16,24]
PS=[0.0,0.125,0.0625,0.03125]
PFD=1.0
NG_INV=0.00052874519051635
NL_INV=0.0026385724906858796
NG=1.0/NG_INV
NL=1.0/NL_INV
LAM=-0.7
TARGET={"beta_g":-7.529658781722162,"beta_lambda3":-4.433872942167074,"beta_mu":0.32246506237129074}


def conv(a,b):
    delta=abs(float(b)-float(a)); scale=abs(float(b))
    if scale<1e-3:
        metric=delta; threshold=2e-6; kind="absolute"; passed=metric<=threshold
    else:
        metric=delta/scale; threshold=2e-3; kind="relative"; passed=metric<=threshold
    return {"N16":float(a),"N24":float(b),"delta":delta,"metric":metric,"threshold":threshold,"kind":kind,"pass":bool(passed)}


def relerr(a,b): return abs(float(a)-float(b))/abs(float(b))


def load_matrix(root):
    three={}; two={}
    for p in Path(root).rglob("*.json"):
        try: d=json.loads(p.read_text())
        except Exception: continue
        if d.get("mode")=="three": three[(int(d["N"]),round(float(d["p"]),8))]=d
        elif d.get("mode")=="two": two[int(d["N"])]=d
    return three,two


def p0_equivalence(three,two,historical):
    rows={}; passed=True
    for N in NSEQ:
        h=historical["beta_sequence"][str(N)]
        n=three[(N,0.0)]
        t=two[N]
        checks={
          "Flow_G_0":abs(n["Flow_G"]-h["Flow_G_0"]),
          "Flow_Lambda_0":abs(n["Flow_Lambda"]-h["Flow_Lambda_0"]),
          "Flow_TT2_0":abs(t["Flow_TT2_0"]-h["Flow_TT2_0"]),
        }
        limits={
          "Flow_G_0":2e-9*(1+abs(h["Flow_G_0"])),
          "Flow_Lambda_0":2e-9*(1+abs(h["Flow_Lambda_0"])),
          "Flow_TT2_0":2e-9*(1+abs(h["Flow_TT2_0"])),
        }
        rp=all(checks[k]<=limits[k] for k in checks); passed &= rp
        rows[str(N)]={"abs_errors":checks,"limits":limits,"pass":rp}
    return {"records":rows,"pass":bool(passed)}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--root",required=True); ap.add_argument("--historical",required=True); ap.add_argument("--out",required=True); args=ap.parse_args()
    three,two=load_matrix(args.root); historical=json.loads(Path(args.historical).read_text())
    missing=[]
    for N in NSEQ:
        for p in PS:
            if (N,round(p,8)) not in three: missing.append(f"three:p={p}:N={N}")
        if N not in two: missing.append(f"two:N={N}")
    for N in (16,24):
        if (N,round(PFD,8)) not in three: missing.append(f"three:p=1:N={N}")
    result={"gate":"SF055A3Q5_FULL_TENSOR_PIECEWISE_BASELINE_RETRY","C3_enabled":False,"required_N":NSEQ,"missing":missing}
    if missing:
        result.update({"classification":"INVALID_Q5_MATRIX_INCOMPLETE","scientific_pass":False,"lane_A_terminal_pass":False,"sf055_terminal_pass":False})
        Path(args.out).write_text(json.dumps(result,indent=2,sort_keys=True)+"\n"); print(json.dumps(result,indent=2)); raise SystemExit(1)

    node_budget_pass=all(three[(N,round(p,8))].get("node_budget_exact") is True for N in NSEQ for p in PS)
    p0=p0_equivalence(three,two,historical)

    betas={}
    for N in NSEQ:
        fg0=float(three[(N,0.0)]["Flow_G"]); f8=float(three[(N,.125)]["Flow_G"]); f16=float(three[(N,.0625)]["Flow_G"]); f32=float(three[(N,.03125)]["Flow_G"]); fl0=float(three[(N,0.0)]["Flow_Lambda"])
        D8=(f8-fg0)/(.125**2); D16=(f16-fg0)/(.0625**2); D32=(f32-fg0)/(.03125**2)
        old=(4*D16-D8)/3; deriv=(4*D32-D16)/3
        bg=2+2*NG*deriv; bl=(-1-bg/2)*LAM+NL*fl0; bm=float(two[N]["beta_mu"])
        betas[str(N)]={"Flow_G_0":fg0,"Flow_G_1_8":f8,"Flow_G_1_16":f16,"Flow_G_1_32":f32,"Flow_Lambda_0":fl0,
                       "D_1_8":D8,"D_1_16":D16,"D_1_32":D32,"Flow_G_prime_preceding":old,"Flow_G_prime_0":deriv,
                       "beta_g":bg,"beta_lambda3":bl,"beta_mu":bm,"Flow_TT2_0":float(two[N]["Flow_TT2_0"])}

    convergence={}
    for p in PS: convergence[f"Flow_G_p{p}"]=conv(three[(16,round(p,8))]["Flow_G"],three[(24,round(p,8))]["Flow_G"])
    convergence["Flow_Lambda_0"]=conv(three[(16,0.0)]["Flow_Lambda"],three[(24,0.0)]["Flow_Lambda"])
    convergence["Flow_TT2_0"]=conv(two[16]["Flow_TT2_0"],two[24]["Flow_TT2_0"])
    for k in ("beta_g","beta_lambda3","beta_mu"): convergence[k]=conv(betas["16"][k],betas["24"][k])
    convergence_pass=all(v["pass"] for v in convergence.values())

    final=betas["24"]; targets={}
    for k,t in TARGET.items():
        e=relerr(final[k],t); targets[k]={"value":final[k],"target":t,"relative_error":e,"threshold":1e-2,"pass":bool(e<=1e-2)}
    target_pass=all(v["pass"] for v in targets.values())

    fd16=three[(16,1.0)]; fd24=three[(24,1.0)]; fdc=conv(fd16["Flow_G"],fd24["Flow_G"])
    bgfd=2+2*NG*(float(fd24["Flow_G"])-float(three[(24,0.0)]["Flow_G"])); blfd=(-1-bgfd/2)*LAM+NL*float(three[(24,0.0)]["Flow_Lambda"])
    fd={"Flow_G_p1_convergence":fdc,"beta_g_finite_difference":bgfd,"beta_lambda3_finite_difference":blfd,"not_compared_to_Eq14":True,
        "pass":bool(fdc["pass"] and math.isfinite(bgfd) and math.isfinite(blfd))}

    controls_pass=bool(node_budget_pass and p0["pass"])
    if not controls_pass:
        classification="BLOCKED_LANE_A_PIECEWISE_IMPLEMENTATION_CONTROL_SCOPED"; scientific_pass=False
    elif not convergence_pass:
        classification="BLOCKED_LANE_A_PIECEWISE_BASELINE_QUADRATURE_NOT_CONVERGED_SCOPED"; scientific_pass=False
    elif not fd["pass"]:
        classification="BLOCKED_LANE_A_PIECEWISE_FINITE_DIFFERENCE_CONTROL_SCOPED"; scientific_pass=False
    elif not target_pass:
        classification="FAIL_LANE_A_PIECEWISE_BASELINE_REPRODUCTION_SCOPED"; scientific_pass=False
    else:
        classification="PASS_LANE_A_PIECEWISE_BASELINE_REPRODUCTION_SCOPED"; scientific_pass=True

    result.update({"classification":classification,"implementation_controls":{"node_budget_pass":node_budget_pass,"historical_p0_equivalence":p0,"pass":controls_pass},
      "beta_sequence":betas,"convergence":convergence,"convergence_pass":convergence_pass,"target_checks":targets,"target_pass":target_pass,
      "finite_difference_control":fd,"topology_N24":{"three_p0_G":three[(24,0.0)]["topology_G"],"three_p0_Lambda":three[(24,0.0)]["topology_Lambda"],"two":two[24]["topology_TT"]},
      "scientific_pass":scientific_pass,"lane_A_terminal_pass":scientific_pass,"sf055_terminal_pass":False,
      "hard_stop_before_C3":True,"derivative_truncation_control_still_required":True})
    out=Path(args.out); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n"); print(json.dumps(result,indent=2,sort_keys=True))
    if not scientific_pass: raise SystemExit(1)

if __name__=="__main__": main()
