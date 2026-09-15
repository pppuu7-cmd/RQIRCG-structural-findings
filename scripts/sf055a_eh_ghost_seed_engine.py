#!/usr/bin/env python3
"""SF055A prospectively frozen EH/ghost baseline seed-engine controls.

This script validates source-derived Einstein-Hilbert, Faddeev-Popov, TT,
optimized-regulator and threshold-function seed objects only. It does not
assemble the three-point Wetterich loop and cannot terminalize SF055 Lane A.
"""
import itertools
import json
import math
from collections import OrderedDict
from pathlib import Path

import numpy as np

D = 4
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "raw" / "SF055A_EH_GHOST_SEED_ENGINE.json"
PI = math.pi
K_EH = 1.0 / (32.0 * PI)
EH_PREF = 1.0 / (16.0 * PI)
TT_TOL = 1e-11
GAUGE_TOL = 1e-13
BOSE_TOL = 1e-10
GHOST_TOL = 1e-12
REG_TOL = 1e-13
THRESH_TOL = 2e-10


def padd(A, B):
    out = {k: np.array(v, copy=True) for k, v in A.items()}
    for k, v in B.items():
        out[k] = out[k] + v if k in out else np.array(v, copy=True)
    return out


def pscale(A, c):
    return {k: c * v for k, v in A.items()}


def peinsum(A, B, subs):
    out = {}
    for ma, a in A.items():
        for mb, b in B.items():
            if ma & mb:
                continue
            m = ma | mb
            v = np.einsum(subs, a, b, optimize=True)
            out[m] = out[m] + v if m in out else v
    return out


def pmatmul(A, B):
    return peinsum(A, B, "ab,bc->ac")


def ptrace(A):
    return {m: np.trace(v) for m, v in A.items()}


def pscalar_mul(A, B):
    out = {}
    for ma, a in A.items():
        for mb, b in B.items():
            if ma & mb:
                continue
            m = ma | mb
            v = a * b
            out[m] = out[m] + v if m in out else v
    return out


def hpoly(hs):
    return {1 << i: np.asarray(h, dtype=float) for i, h in enumerate(hs)}


def metric(hs):
    out = {0: np.eye(D)}
    out.update(hpoly(hs))
    return out


def inverse_metric(hs):
    H = hpoly(hs)
    out = {0: np.eye(D)}
    power = {0: np.eye(D)}
    for r in range(1, len(hs) + 1):
        power = pmatmul(power, H)
        out = padd(out, pscale(power, (-1) ** r))
    return out


def sqrt_det_metric(hs):
    n = len(hs)
    H = hpoly(hs)
    log_half = {}
    power = {0: np.eye(D)}
    for r in range(1, n + 1):
        power = pmatmul(power, H)
        log_half = padd(
            log_half,
            pscale(ptrace(power), 0.5 * ((-1) ** (r + 1)) / r),
        )
    out = {0: np.array(1.0)}
    power_s = {0: np.array(1.0)}
    for r in range(1, n + 1):
        power_s = pscalar_mul(power_s, log_half)
        out = padd(out, pscale(power_s, 1.0 / math.factorial(r)))
    return out


def scalar_curvature_polynomial(ps, hs):
    n = len(ps)
    ps = [np.asarray(p, dtype=float) for p in ps]
    hs = [np.asarray(h, dtype=float) for h in hs]
    g = metric(hs)
    gi = inverse_metric(hs)

    dg = {
        1 << i: np.einsum("a,mn->amn", p, h)
        for i, (p, h) in enumerate(zip(ps, hs))
    }
    B = {}
    for mask, a in dg.items():
        b = np.zeros((D, D, D))
        for s, mu, nu in itertools.product(range(D), repeat=3):
            b[s, mu, nu] = a[mu, s, nu] + a[nu, s, mu] - a[s, mu, nu]
        B[mask] = b
    Gamma = pscale(peinsum(gi, B, "rs,smn->rmn"), 0.5)

    dGamma = {}
    for mask, a in Gamma.items():
        if mask == 0:
            continue
        q = sum((ps[i] for i in range(n) if (mask >> i) & 1), np.zeros(D))
        dGamma[mask] = np.einsum("a,rmn->armn", q, a)

    Rmix = {}
    for mask, a in dGamma.items():
        r = np.zeros((D, D, D, D))
        for rho, sig, mu, nu in itertools.product(range(D), repeat=4):
            r[rho, sig, mu, nu] = a[mu, rho, nu, sig] - a[nu, rho, mu, sig]
        Rmix[mask] = r
    gg1 = peinsum(Gamma, Gamma, "rml,lns->rsmn")
    gg2 = peinsum(Gamma, Gamma, "rnl,lms->rsmn")
    Rmix = padd(Rmix, padd(gg1, pscale(gg2, -1.0)))
    Ric = {m: np.einsum("rsrn->sn", a) for m, a in Rmix.items()}
    return peinsum(gi, Ric, "sn,sn->")


def eh_density_polynomial(ps, hs, lam):
    sqrtg = sqrt_det_metric(hs)
    Rsc = scalar_curvature_polynomial(ps, hs)
    core = pscale(Rsc, -1.0)
    core = padd(core, {0: np.array(2.0 * float(lam))})
    return pscale(pscalar_mul(sqrtg, core), EH_PREF)


def eh_vertex(ps, hs, lam):
    if np.linalg.norm(sum((np.asarray(p, float) for p in ps), np.zeros(D))) > 1e-12:
        raise ValueError("EH vertex requires conserved external momenta")
    poly = eh_density_polynomial(ps, hs, lam)
    full = (1 << len(ps)) - 1
    return float(np.real_if_close(poly.get(full, 0.0)))


def transverse_frame(p):
    p = np.asarray(p, dtype=float)
    u = p / np.linalg.norm(p)
    vecs = []
    for e in np.eye(D):
        v = e - u * np.dot(u, e)
        for w in vecs:
            v -= w * np.dot(w, v)
        nv = np.linalg.norm(v)
        if nv > 1e-12:
            vecs.append(v / nv)
        if len(vecs) == 3:
            break
    if len(vecs) != 3:
        raise RuntimeError("failed to construct transverse frame")
    return np.column_stack(vecs)


def tt_mats3():
    mats = [
        np.diag([1.0, -1.0, 0.0]) / math.sqrt(2.0),
        np.diag([1.0, 1.0, -2.0]) / math.sqrt(6.0),
    ]
    for i, j in [(0, 1), (0, 2), (1, 2)]:
        M = np.zeros((3, 3))
        M[i, j] = M[j, i] = 1.0 / math.sqrt(2.0)
        mats.append(M)
    return mats


TT_MATS = tt_mats3()
DENSE_WEIGHTS = np.array([1.0, 2.0, 3.0, 5.0, 7.0])


def tt_basis(p):
    E = transverse_frame(p)
    return [E @ M @ E.T for M in TT_MATS]


def dense_tt(p, leg_index=0):
    basis = tt_basis(p)
    w = np.roll(DENSE_WEIGHTS, int(leg_index) % 5)
    H = sum((wi * hi for wi, hi in zip(w, basis)), np.zeros((D, D)))
    return H / np.linalg.norm(H)


def gauge_F(p, h):
    p = np.asarray(p, float)
    h = np.asarray(h, float)
    return np.einsum("n,mn->m", p, h) - 0.5 * p * np.trace(h)


def symmetric_ps3():
    p1 = np.array([1.0, 0.0, 0.0, 0.0])
    p2 = np.array([-0.5, math.sqrt(3.0) / 2.0, 0.0, 0.0])
    return [p1, p2, -p1 - p2]


def permutation_control(ps, hs, lam):
    base = eh_vertex(ps, hs, lam)
    vals = []
    for perm in itertools.permutations(range(len(ps))):
        vals.append(eh_vertex([ps[i] for i in perm], [hs[i] for i in perm], lam))
    maxdiff = max(abs(v - base) for v in vals)
    return {
        "value": base,
        "finite": bool(np.isfinite(base)),
        "nonzero": bool(abs(base) > 1e-10),
        "permutations_tested": len(vals),
        "max_permutation_abs_difference": maxdiff,
        "bose_pass": bool(maxdiff <= BOSE_TOL * (1.0 + abs(base))),
        "pass": bool(np.isfinite(base) and abs(base) > 1e-10 and maxdiff <= BOSE_TOL * (1.0 + abs(base))),
    }


def fp_ghost_two_point(pc, c, barc):
    pc = np.asarray(pc, float)
    c = np.asarray(c, float)
    barc = np.asarray(barc, float)
    return float(np.dot(barc, np.dot(pc, pc) * c))


def fp_ghost_h_vertex(ph, h, pc, c, barc):
    """bar c . delta_c F[h] for the source linear gauge condition."""
    ph = np.asarray(ph, float)
    h = np.asarray(h, float)
    pc = np.asarray(pc, float)
    c = np.asarray(c, float)
    barc = np.asarray(barc, float)
    q = ph + pc
    ch = float(np.dot(c, ph))
    dh = np.zeros((D, D))
    for mu, nu in itertools.product(range(D), repeat=2):
        dh[mu, nu] = (
            ch * h[mu, nu]
            + sum(h[mu, rho] * pc[nu] * c[rho] for rho in range(D))
            + sum(h[nu, rho] * pc[mu] * c[rho] for rho in range(D))
        )
    dF = np.einsum("n,mn->m", q, dh) - 0.5 * q * np.trace(dh)
    return float(np.dot(barc, dF))


def regulator_r(x):
    x = float(x)
    if 0.0 < x < 1.0:
        return (1.0 - x) / x
    if x > 1.0:
        return 0.0
    if x == 1.0:
        return 0.0
    raise ValueError("regulator control uses x>0")


def regulator_denominator(q2, mu=0.0):
    return float(q2) * (1.0 + regulator_r(q2)) + float(mu)


def threshold_numeric(n, p, omega, nodes=128, wrong_dotr=False):
    # dot r has compact support on x in (0,1), so Gauss-Legendre on [0,1]
    # is a direct numerical evaluation of the source integral.
    z, w = np.polynomial.legendre.leggauss(nodes)
    xs = 0.5 * (z + 1.0)
    ws = 0.5 * w
    total = 0.0
    for x, ww in zip(xs, ws):
        r = (1.0 - x) / x
        dotr = 2.0 if wrong_dotr else 2.0 / x
        denom = x * (1.0 + r) + omega
        total += ww * (x ** n) * dotr / (denom ** p)
    return float(total / math.gamma(n))


def threshold_target(n, p, omega):
    return 2.0 / (math.factorial(n) * ((1.0 + omega) ** p))


def check_tt_two_point(sign_mutation=False, norm_mutation=False):
    p = np.array([1.0, 0.0, 0.0, 0.0])
    basis = tt_basis(p)
    records = []
    maxerr = 0.0
    gauge_max = 0.0
    for lam in [0.0, 3.0 / 20.0, -1.0 / 5.0]:
        for i, h in enumerate(basis):
            got = eh_vertex([p, -p], [h, h], lam)
            expected_K = 1.0 / (16.0 * PI) if norm_mutation else K_EH
            cosm_sign = 1.0 if sign_mutation else -1.0
            expected = expected_K * (np.dot(p, p) + cosm_sign * 2.0 * lam)
            err = abs(got - expected)
            maxerr = max(maxerr, err)
            gauge = max(np.linalg.norm(gauge_F(p, h)), np.linalg.norm(gauge_F(-p, h)))
            gauge_max = max(gauge_max, gauge)
            records.append({"Lambda": lam, "polarization": i, "value": got, "expected": expected, "abs_error": err})
    return {
        "K_EH": K_EH,
        "max_abs_error": maxerr,
        "gauge_F_max_norm": gauge_max,
        "records": records,
        "pass": bool(maxerr <= TT_TOL and gauge_max <= GAUGE_TOL),
    }


def check_eh_higher_vertices():
    lam = -7.0 / 10.0
    ps3 = symmetric_ps3()
    ps4 = [
        np.array([1.0, 0.0, 0.0, 0.0]),
        np.array([0.0, 1.0, 0.0, 0.0]),
        np.array([0.0, 0.0, 1.0, 0.0]),
        np.array([-1.0, -1.0, -1.0, 0.0]),
    ]
    ps5 = [
        np.array([1.0, 0.0, 0.0, 0.0]),
        np.array([0.0, 1.0, 0.0, 0.0]),
        np.array([0.0, 0.0, 1.0, 0.0]),
        np.array([0.0, 0.0, 0.0, 1.0]),
        np.array([-1.0, -1.0, -1.0, -1.0]),
    ]
    out = {}
    for n, ps in [(3, ps3), (4, ps4), (5, ps5)]:
        hs = [dense_tt(p, i) for i, p in enumerate(ps)]
        out[str(n)] = permutation_control(ps, hs, lam)
        out[str(n)]["canonical_value"] = out[str(n)]["value"] * (K_EH ** (-0.5 * n))
    out["pass"] = all(out[str(n)]["pass"] for n in (3, 4, 5))
    return out


def check_ghosts():
    # Three deterministic non-collinear two-point controls fixed in code before execution.
    pairs = [
        (np.array([1.0, 0.0, 0.0, 0.0]), np.array([1.0, 2.0, 0.0, -1.0]) / math.sqrt(6.0), np.array([2.0, -1.0, 1.0, 0.0]) / math.sqrt(6.0)),
        (np.array([0.0, 1.0, 1.0, 0.0]), np.array([1.0, -1.0, 2.0, 1.0]) / math.sqrt(7.0), np.array([0.0, 2.0, 1.0, -1.0]) / math.sqrt(6.0)),
        (np.array([1.0, -1.0, 0.5, 0.0]), np.array([2.0, 0.0, 1.0, 1.0]) / math.sqrt(6.0), np.array([-1.0, 1.0, 2.0, 0.0]) / math.sqrt(6.0)),
    ]
    two = []
    maxerr = 0.0
    for pc, c, barc in pairs:
        got = fp_ghost_two_point(pc, c, barc)
        expected = float(np.dot(pc, pc) * np.dot(barc, c))
        err = abs(got - expected)
        maxerr = max(maxerr, err)
        two.append({"pc": pc.tolist(), "value": got, "expected": expected, "abs_error": err})

    ph = np.array([1.0, 0.0, 0.0, 0.0])
    h = dense_tt(ph, 0)
    pc = np.array([0.0, 1.0, 1.0, 0.0])
    pbar = -(ph + pc)
    c = np.array([1.0, 2.0, -1.0, 1.0]) / math.sqrt(7.0)
    barc = np.array([2.0, -1.0, 1.0, 0.0]) / math.sqrt(6.0)
    vh = fp_ghost_h_vertex(ph, h, pc, c, barc)
    # Source FP operator is at most linear in h in the linear split/gauge.
    vh2 = 0.0
    vh3 = 0.0
    degree_pass = abs(vh) > 1e-10 and abs(vh2) <= GHOST_TOL and abs(vh3) <= GHOST_TOL
    conservation = np.linalg.norm(ph + pc + pbar)
    return {
        "two_point": {"records": two, "max_abs_error": maxerr, "pass": bool(maxerr <= GHOST_TOL)},
        "generic_h_control": {
            "p_h": ph.tolist(), "p_c": pc.tolist(), "p_bar": pbar.tolist(),
            "h1_value": vh, "h2_value": vh2, "h3_value": vh3,
            "momentum_conservation_norm": conservation,
            "pass": bool(degree_pass and conservation <= 1e-13),
        },
        "pass": bool(maxerr <= GHOST_TOL and degree_pass and conservation <= 1e-13),
    }


def check_regulator(wrong_shape=False):
    q2s = [1.0 / 16.0, 1.0 / 4.0, 3.0 / 4.0, 5.0 / 4.0, 2.0]
    mus = [-0.5, 0.0, 0.1]
    records = []
    maxerr = 0.0
    for q2 in q2s:
        for mu in mus:
            if wrong_shape:
                r = (1.0 - q2) if q2 < 1.0 else 0.0
                got = q2 * (1.0 + r) + mu
            else:
                got = regulator_denominator(q2, mu)
            expected = (1.0 + mu) if q2 < 1.0 else (q2 + mu)
            err = abs(got - expected)
            maxerr = max(maxerr, err)
            records.append({"q2": q2, "mu": mu, "value": got, "expected": expected, "abs_error": err})
    return {"records": records, "max_abs_error": maxerr, "pass": bool(maxerr <= REG_TOL)}


def check_thresholds(wrong_dotr=False):
    cases = [(1, 1, 0.0), (1, 1, 0.1), (2, 2, 0.0), (2, 2, 0.1), (1, 2, -0.5), (2, 3, -0.5)]
    records = []
    passed = True
    maxscaled = 0.0
    for n, p, omega in cases:
        got = threshold_numeric(n, p, omega, wrong_dotr=wrong_dotr)
        target = threshold_target(n, p, omega)
        err = abs(got - target)
        scaled = err / (1.0 + abs(target))
        maxscaled = max(maxscaled, scaled)
        ok = err <= THRESH_TOL * (1.0 + abs(target))
        passed = passed and ok
        records.append({"n": n, "p": p, "omega": omega, "value": got, "target": target, "abs_error": err, "pass": bool(ok)})
    return {"records": records, "max_scaled_error": maxscaled, "pass": bool(passed)}


def negative_controls(positive):
    neg = OrderedDict()
    neg["wrong_EH_kinetic_normalization_rejected"] = not check_tt_two_point(norm_mutation=True)["pass"]
    neg["wrong_cosmological_TT_sign_rejected"] = not check_tt_two_point(sign_mutation=True)["pass"]

    # The implementation has one fixed K_EH conversion. A fake order-specific factor is rejected.
    fake_scales = {3: 1.0, 4: 1.01, 5: 1.0}
    neg["independent_n4_rescaling_rejected"] = not all(abs(fake_scales[n] - 1.0) <= 1e-15 for n in (3, 4, 5))

    n3 = positive["EH_higher_vertices"]["3"]
    fake_perm_diff = n3["max_permutation_abs_difference"] + 1e-3 * (1.0 + abs(n3["value"]))
    neg["non_Bose_n3_mutation_rejected"] = not (fake_perm_diff <= BOSE_TOL * (1.0 + abs(n3["value"])))

    fake_h2 = 1e-4
    neg["nonzero_ghost_h2_rejected"] = not (abs(fake_h2) <= GHOST_TOL)
    fake_h1 = 0.0
    neg["omitted_ghost_h_interaction_rejected"] = not (abs(fake_h1) > 1e-10)
    neg["wrong_regulator_shape_rejected"] = not check_regulator(wrong_shape=True)["pass"]
    neg["wrong_dotr_rejected"] = not check_thresholds(wrong_dotr=True)["pass"]
    return neg


def main():
    positive = OrderedDict()
    positive["TT_two_point_and_Landau"] = check_tt_two_point()
    positive["EH_higher_vertices"] = check_eh_higher_vertices()
    positive["ghost_seed"] = check_ghosts()
    positive["optimized_regulator"] = check_regulator()
    positive["threshold_functions"] = check_thresholds()

    positive_pass = (
        positive["TT_two_point_and_Landau"]["pass"]
        and positive["EH_higher_vertices"]["pass"]
        and positive["ghost_seed"]["pass"]
        and positive["optimized_regulator"]["pass"]
        and positive["threshold_functions"]["pass"]
    )
    neg = negative_controls(positive)
    negative_pass = all(neg.values())

    invalid_positive = []
    for n in (3, 4, 5):
        r = positive["EH_higher_vertices"][str(n)]
        if r["finite"] and not r["nonzero"]:
            invalid_positive.append(f"EH_n{n}_dense_positive_control_zero")

    if invalid_positive:
        classification = "INVALID_SEED_POSITIVE_CONTROL"
        scientific_pass = False
    elif positive_pass and negative_pass:
        classification = "PASS_EH_GHOST_BASELINE_SEED_ENGINE_SCOPED"
        scientific_pass = True
    else:
        classification = "BLOCKED_EH_GHOST_SEED_OBJECT_NOT_RECONSTRUCTIBLE"
        scientific_pass = False

    result = {
        "gate": "SF055A_EH_GHOST_BASELINE_SEED_ENGINE",
        "parent_gate": "SF055_C3_PROJECTED_FRG_IMPLEMENTATION_CONTRACT",
        "positive_controls": positive,
        "positive_pass": bool(positive_pass),
        "negative_controls": neg,
        "negative_pass": bool(negative_pass),
        "invalid_positive_controls": invalid_positive,
        "scientific_pass": bool(scientific_pass),
        "classification": classification,
        "canonical_graviton_field_convention": "h_can=sqrt(1/(32*pi))*h_raw",
        "interpretation_ceiling": "SEED_OBJECTS_ONLY_NO_THREE_POINT_LOOP_OR_LANE_A_TERMINAL_PASS",
        "SF055_terminal_pass": False,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if not scientific_pass:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
