#!/usr/bin/env python3
"""Aggregate the frozen SF055A3 quadrature matrix and classify Lane-A baseline."""
import argparse
import json
import math
from pathlib import Path

NSEQ = [8, 12, 16, 24]
PS = [0.0, 0.125, 0.0625, 0.03125]
PFD = 1.0
NG_INV = 0.00052874519051635
NL_INV = 0.0026385724906858796
NG = 1.0 / NG_INV
NL = 1.0 / NL_INV
LAM = -0.7
TARGET = {
    "beta_g": -7.529658781722162,
    "beta_lambda3": -4.433872942167074,
    "beta_mu": 0.32246506237129074,
}


def conv(a, b):
    delta = abs(float(b) - float(a))
    scale = abs(float(b))
    if scale < 1e-3:
        passed = delta <= 2e-6
        metric = delta
        threshold = 2e-6
        kind = "absolute"
    else:
        metric = delta / scale
        threshold = 2e-3
        passed = metric <= threshold
        kind = "relative"
    return {"N16": float(a), "N24": float(b), "delta": delta,
            "metric": metric, "threshold": threshold, "kind": kind, "pass": bool(passed)}


def relerr(got, target):
    return abs(float(got) - float(target)) / abs(float(target))


def load_matrix(root):
    three = {}
    two = {}
    for path in Path(root).rglob("*.json"):
        try:
            data = json.loads(path.read_text())
        except Exception:
            continue
        mode = data.get("mode")
        if mode == "three":
            three[(int(data["N"]), round(float(data["p"]), 8))] = data
        elif mode == "two":
            two[int(data["N"])] = data
    return three, two


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    three, two = load_matrix(args.root)

    missing = []
    for N in NSEQ:
        for p in PS:
            if (N, round(p, 8)) not in three:
                missing.append(f"three:p={p}:N={N}")
        if N not in two:
            missing.append(f"two:N={N}")
    for N in [16, 24]:
        if (N, round(PFD, 8)) not in three:
            missing.append(f"three:p=1:N={N}")

    result = {
        "gate": "SF055A3_SOURCE_FOURIER_BASELINE_LOOP_REPRODUCTION",
        "C3_enabled": False,
        "required_N": NSEQ,
        "missing": missing,
    }
    if missing:
        result.update({
            "classification": "INVALID_SF055A3_BASELINE_MATRIX_INCOMPLETE",
            "scientific_pass": False,
            "lane_A_terminal_pass": False,
            "sf055_terminal_pass": False,
        })
        text = json.dumps(result, indent=2, sort_keys=True) + "\n"
        out = Path(args.out); out.parent.mkdir(parents=True, exist_ok=True); out.write_text(text); print(text, end="")
        raise SystemExit(1)

    betas = {}
    for N in NSEQ:
        fg0 = float(three[(N, 0.0)]["Flow_G"])
        f8 = float(three[(N, 0.125)]["Flow_G"])
        f16 = float(three[(N, 0.0625)]["Flow_G"])
        f32 = float(three[(N, 0.03125)]["Flow_G"])
        fl0 = float(three[(N, 0.0)]["Flow_Lambda"])
        D8 = (f8 - fg0) / (0.125 ** 2)
        D16 = (f16 - fg0) / (0.0625 ** 2)
        D32 = (f32 - fg0) / (0.03125 ** 2)
        deriv_old = (4.0 * D16 - D8) / 3.0
        deriv = (4.0 * D32 - D16) / 3.0
        bg = 2.0 + 2.0 * NG * deriv
        bl = (-1.0 - bg / 2.0) * LAM + NL * fl0
        bm = float(two[N]["beta_mu"])
        betas[str(N)] = {
            "Flow_G_0": fg0,
            "Flow_G_1_8": f8,
            "Flow_G_1_16": f16,
            "Flow_G_1_32": f32,
            "Flow_Lambda_0": fl0,
            "D_1_8": D8,
            "D_1_16": D16,
            "D_1_32": D32,
            "Flow_G_prime_preceding": deriv_old,
            "Flow_G_prime_0": deriv,
            "beta_g": bg,
            "beta_lambda3": bl,
            "beta_mu": bm,
            "Flow_TT2_0": float(two[N]["Flow_TT2_0"]),
        }

    convergence = {}
    for p in PS:
        key = f"Flow_G_p{p}"
        convergence[key] = conv(three[(16, round(p,8))]["Flow_G"], three[(24, round(p,8))]["Flow_G"])
    convergence["Flow_Lambda_0"] = conv(three[(16,0.0)]["Flow_Lambda"], three[(24,0.0)]["Flow_Lambda"])
    convergence["Flow_TT2_0"] = conv(two[16]["Flow_TT2_0"], two[24]["Flow_TT2_0"])
    for key in ["beta_g", "beta_lambda3", "beta_mu"]:
        convergence[key] = conv(betas["16"][key], betas["24"][key])
    convergence_pass = all(v["pass"] for v in convergence.values())

    final = betas["24"]
    target_checks = {}
    for key, target in TARGET.items():
        err = relerr(final[key], target)
        target_checks[key] = {"value": final[key], "target": target, "relative_error": err,
                              "threshold": 1e-2, "pass": bool(err <= 1e-2)}
    target_pass = all(v["pass"] for v in target_checks.values())

    fd16 = three[(16,1.0)]
    fd24 = three[(24,1.0)]
    fd_conv = conv(fd16["Flow_G"], fd24["Flow_G"])
    bgfd = 2.0 + 2.0 * NG * (float(fd24["Flow_G"]) - float(three[(24,0.0)]["Flow_G"]))
    blfd = (-1.0 - bgfd / 2.0) * LAM + NL * float(three[(24,0.0)]["Flow_Lambda"])
    finite_difference = {
        "Flow_G_p1_convergence": fd_conv,
        "beta_g_finite_difference": bgfd,
        "beta_lambda3_finite_difference": blfd,
        "not_compared_to_Eq14": True,
        "pass": bool(fd_conv["pass"] and math.isfinite(bgfd) and math.isfinite(blfd)),
    }

    if not convergence_pass:
        classification = "BLOCKED_LANE_A_BASELINE_QUADRATURE_NOT_CONVERGED_SCOPED"
        scientific_pass = False
    elif not finite_difference["pass"]:
        classification = "BLOCKED_LANE_A_FINITE_DIFFERENCE_EXTRACTION_CONTROL_SCOPED"
        scientific_pass = False
    elif not target_pass:
        classification = "FAIL_LANE_A_BASELINE_REPRODUCTION_SCOPED"
        scientific_pass = False
    else:
        classification = "PASS_LANE_A_BASELINE_EH_GHOST_THREE_POINT_FLOW_REPRODUCTION_SCOPED"
        scientific_pass = True

    result.update({
        "classification": classification,
        "beta_sequence": betas,
        "convergence": convergence,
        "convergence_pass": convergence_pass,
        "target_checks": target_checks,
        "target_pass": target_pass,
        "finite_difference_control": finite_difference,
        "topology_N24": {
            "three_p0_G": three[(24,0.0)]["topology_G"],
            "three_p0_Lambda": three[(24,0.0)]["topology_Lambda"],
            "two": two[24]["topology_TT"],
        },
        "scientific_pass": scientific_pass,
        "lane_A_terminal_pass": scientific_pass,
        "sf055_terminal_pass": scientific_pass,
        "hard_stop_before_C3": not scientific_pass,
        "next_if_pass": "TERMINALIZE_LANE_A_AND_SF055_THEN_COMPUTE_PROJECTED_DYNAMICAL_C3_FLOW",
        "next_if_not_pass": "STOP_PROGRAMME_BEFORE_SUBSTANTIVE_C3_FLOW",
    })
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    out = Path(args.out); out.parent.mkdir(parents=True, exist_ok=True); out.write_text(text); print(text, end="")
    if not scientific_pass:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
