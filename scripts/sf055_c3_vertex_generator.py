#!/usr/bin/env python3
"""SF055 Lane-B common-origin C^3 vertex generator and controls.

Generates the multilinear flat-background pure-graviton vertices of
    int d^4x sqrt(g) C_{rs}^{mn} C_{mn}^{ab} C_{ab}^{rs}
through n=5 from one covariant operator, using a square-free multivariate
formal expansion. The square-free algebra is exact for the coefficient of
one power of each external leg parameter: terms containing epsilon_i^2 can
never contribute to the fully multilinear functional derivative.

Momentum derivatives use the stripped Euclidean convention d -> p, matching
SF050/SF052. The omitted Fourier i^6 is one global convention factor.
This script is a Lane-B calibration only; it does not evaluate FRG loops.
"""
import itertools
import json
import math
from pathlib import Path

import numpy as np

D = 4
TOL = 1e-10
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "raw" / "SF055_C3_VERTEX_GENERATOR.json"


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
        out = padd(out, pscale(power_s, 1 / math.factorial(r)))
    return out


def c3_density_polynomial(ps, hs):
    n = len(ps)
    ps = [np.asarray(p, dtype=float) for p in ps]
    hs = [np.asarray(h, dtype=float) for h in hs]
    g = metric(hs)
    gi = inverse_metric(hs)
    sqrtg = sqrt_det_metric(hs)

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
        q = sum(
            (ps[i] for i in range(n) if (mask >> i) & 1),
            np.zeros(D),
        )
        dGamma[mask] = np.einsum("a,rmn->armn", q, a)

    Rmix = {}
    for mask, a in dGamma.items():
        r = np.zeros((D, D, D, D))
        for rho, sig, mu, nu in itertools.product(range(D), repeat=4):
            r[rho, sig, mu, nu] = a[mu, rho, nu, sig] - a[nu, rho, mu, sig]
        Rmix[mask] = r

    gg1 = peinsum(Gamma, Gamma, "rml,lns->rsmn")
    gg2 = peinsum(Gamma, Gamma, "rnl,lms->rsmn")
    Rmix = padd(Rmix, padd(gg1, pscale(gg2, -1)))

    Rlow = peinsum(g, Rmix, "ar,rsmn->asmn")
    Ric = {m: np.einsum("rsrn->sn", a) for m, a in Rmix.items()}
    Rsc = peinsum(gi, Ric, "sn,sn->")

    C = {m: np.array(a, copy=True) for m, a in Rlow.items()}
    t1 = peinsum(g, Ric, "ac,db->abcd")
    t2 = peinsum(g, Ric, "ad,cb->abcd")
    t3 = peinsum(g, Ric, "bc,da->abcd")
    t4 = peinsum(g, Ric, "bd,ca->abcd")
    riccomb = padd(padd(t1, pscale(t2, -1)), padd(pscale(t3, -1), t4))
    C = padd(C, pscale(riccomb, -1 / (D - 2)))

    ggA = peinsum(g, g, "ac,db->abcd")
    ggB = peinsum(g, g, "ad,cb->abcd")
    sgg = peinsum(Rsc, padd(ggA, pscale(ggB, -1)), ",abcd->abcd")
    C = padd(C, pscale(sgg, 1 / ((D - 1) * (D - 2))))

    tmp = peinsum(gi, C, "mc,abcd->abmd")
    Cmix = peinsum(gi, tmp, "nd,abmd->abmn")
    prod2 = peinsum(Cmix, Cmix, "rsmn,mnab->rsab")
    I3 = peinsum(prod2, Cmix, "rsab,abrs->")
    return pscalar_mul(sqrtg, I3)


def vertex(ps, hs, coupling=1.0):
    dens = c3_density_polynomial(ps, hs)
    full = (1 << len(ps)) - 1
    value = dens.get(full, 0.0)
    return coupling * float(np.real_if_close(value))


def symmetric_ps3():
    p1 = np.array([1.0, 0.0, 0.0, 0.0])
    p2 = np.array([-0.5, math.sqrt(3) / 2, 0.0, 0.0])
    return [p1, p2, -p1 - p2]


def tt_basis(p):
    p = np.asarray(p, dtype=float)
    p = p / np.linalg.norm(p)
    _, _, vh = np.linalg.svd(p.reshape(1, -1))
    E = vh[1:].T
    mats = [
        np.diag([1.0, -1.0, 0.0]) / math.sqrt(2),
        np.diag([1.0, 1.0, -2.0]) / math.sqrt(6),
    ]
    for i, j in [(0, 1), (0, 2), (1, 2)]:
        M = np.zeros((3, 3))
        M[i, j] = M[j, i] = 1 / math.sqrt(2)
        mats.append(M)
    return [E @ M @ E.T for M in mats]


def linear_weyl(p, h):
    p = np.asarray(p, dtype=float)
    h = np.asarray(h, dtype=float)
    R = np.zeros((D, D, D, D))
    for mu, nu, rho, sig in itertools.product(range(D), repeat=4):
        R[mu, nu, rho, sig] = 0.5 * (
            p[rho] * p[nu] * h[mu, sig]
            + p[sig] * p[mu] * h[nu, rho]
            - p[sig] * p[nu] * h[mu, rho]
            - p[rho] * p[mu] * h[nu, sig]
        )
    Ric = np.einsum("mnms->ns", R)
    Sc = np.trace(Ric)
    C = np.zeros_like(R)
    I = np.eye(D)
    for a, b, c, d in itertools.product(range(D), repeat=4):
        C[a, b, c, d] = (
            R[a, b, c, d]
            - 1 / (D - 2)
            * (
                I[a, c] * Ric[d, b]
                - I[a, d] * Ric[c, b]
                - I[b, c] * Ric[d, a]
                + I[b, d] * Ric[c, a]
            )
            + Sc
            / ((D - 1) * (D - 2))
            * (I[a, c] * I[d, b] - I[a, d] * I[c, b])
        )
    return C


def sf052_c3_component(ps, hs):
    Cs = [linear_weyl(p, h) for p, h in zip(ps, hs)]

    def contr(A, B, C):
        return np.einsum("rsmn,mnab,abrs->", A, B, C, optimize=True)

    return sum(
        contr(Cs[a], Cs[b], Cs[c])
        for a, b, c in itertools.permutations(range(3))
    ) / 6


def generic_momenta(n, seed):
    rng = np.random.default_rng(seed)
    ps = [rng.normal(size=D) for _ in range(n - 1)]
    ps.append(-sum(ps, np.zeros(D)))
    return ps


def generic_tts(ps, seed):
    rng = np.random.default_rng(seed)
    hs = []
    for p in ps:
        P = np.eye(D) - np.outer(p, p) / np.dot(p, p)
        A = rng.normal(size=(D, D))
        A = (A + A.T) / 2
        H = P @ A @ P
        H = H - P * (np.trace(H) / (D - 1))
        H = H / np.linalg.norm(H)
        hs.append(H)
    return hs


def tt_quality(ps, hs):
    return {
        "max_abs_trace": max(abs(np.trace(h)) for h in hs),
        "max_transversality_norm": max(np.linalg.norm(p @ h) for p, h in zip(ps, hs)),
        "momentum_conservation_norm": np.linalg.norm(sum(ps, np.zeros(D))),
    }


def main():
    result = {
        "gate": "SF055_C3_PROJECTED_FRG_IMPLEMENTATION_CONTRACT",
        "lane": "B_COMMON_ORIGIN_C3_VERTEX_GENERATOR",
        "scope": "FLAT_EUCLIDEAN_PURE_GRAVITON_VERTEX_CALIBRATION_NO_FRG_LOOPS",
        "method": {
            "operator": "int sqrt(g) C_rhosigma^munu C_munu^alphabeta C_alphabeta^rhosigma",
            "expansion": "square_free_multivariate_formal_series_through_full_multilinear_mask",
            "momentum_derivative_convention": "d_to_p_stripped_Euclidean_matching_SF050_SF052",
            "single_common_coupling_parameter": True,
        },
    }

    ps2 = [np.array([1.0, 0, 0, 0]), np.array([-1.0, 0, 0, 0])]
    hs2 = generic_tts(ps2, 12)
    gamma2 = vertex(ps2, hs2)
    result["Gamma2_control"] = {
        "value": gamma2,
        "pass": abs(gamma2) < TOL,
        "tt_quality": tt_quality(ps2, hs2),
    }

    ps3 = symmetric_ps3()
    bases = [tt_basis(p) for p in ps3]
    ratios = []
    zero_ref_max = 0.0
    gen_norm_div6 = 0.0
    ref_norm = 0.0
    nonzero = 0
    for i, j, k in itertools.product(range(5), repeat=3):
        hs = [bases[0][i], bases[1][j], bases[2][k]]
        ref = sf052_c3_component(ps3, hs)
        got = vertex(ps3, hs)
        ref_norm += ref * ref
        gen_norm_div6 += (got / 6.0) ** 2
        if abs(ref) > TOL:
            ratios.append(got / ref)
            nonzero += 1
        else:
            zero_ref_max = max(zero_ref_max, abs(got))
    ratio_med = float(np.median(ratios))
    ratio_span = max(abs(r - ratio_med) for r in ratios)
    inherited = json.loads(
        (ROOT / "results" / "raw" / "SF052_DERIVATIVE_REDUNDANT_QUOTIENT.json").read_text()
    )
    cubic_pass = (
        abs(ratio_med - 6.0) < TOL
        and ratio_span < TOL
        and zero_ref_max < TOL
        and abs(ref_norm - 95 / 768) < TOL
        and abs(gen_norm_div6 - 95 / 768) < TOL
        and inherited["normalized_projector_responses"]["C3"] == 1
    )
    result["Gamma3_SF052_match"] = {
        "tt_components": 125,
        "nonzero_reference_components": nonzero,
        "functional_derivative_global_factor": ratio_med,
        "expected_global_factor": 6.0,
        "max_ratio_deviation": ratio_span,
        "max_generated_on_reference_zero_component": zero_ref_max,
        "reference_tensor_norm": ref_norm,
        "generated_tensor_norm_after_dividing_global_factor": gen_norm_div6,
        "expected_norm": "95/768",
        "inherited_P_E_6d_C3_response": inherited["normalized_projector_responses"]["C3"],
        "pass": cubic_pass,
    }

    vertex_controls = {}
    for n in (3, 4, 5):
        ps = generic_momenta(n, 100 + n)
        hs = generic_tts(ps, 200 + n)
        base = vertex(ps, hs, 1.0)
        twice = vertex(ps, hs, 2.0)
        zero = vertex(ps, hs, 0.0)
        perms = list(itertools.permutations(range(n)))
        vals = [vertex([ps[i] for i in q], [hs[i] for i in q], 1.0) for q in perms]
        max_diff = max(abs(v - base) for v in vals)
        scale = max(1.0, abs(base))
        coupling_ratio = twice / base if abs(base) > 1e-14 else None
        passed = (
            abs(zero) < TOL
            and coupling_ratio is not None
            and abs(coupling_ratio - 2.0) < TOL
            and max_diff / scale < TOL
        )
        vertex_controls[str(n)] = {
            "value_at_unit_coupling": base,
            "value_at_double_coupling": twice,
            "value_at_zero_coupling": zero,
            "double_to_unit_ratio": coupling_ratio,
            "permutations_tested": math.factorial(n),
            "max_permutation_abs_difference": max_diff,
            "max_permutation_scaled_difference": max_diff / scale,
            "tt_quality": tt_quality(ps, hs),
            "pass": passed,
        }
    result["Gamma3_4_5_common_origin_controls"] = vertex_controls

    result["lane_B_pass"] = (
        result["Gamma2_control"]["pass"]
        and result["Gamma3_SF052_match"]["pass"]
        and all(v["pass"] for v in vertex_controls.values())
    )
    result["classification"] = (
        "PASS_C3_COMMON_ORIGIN_VERTEX_GENERATOR_SCOPED"
        if result["lane_B_pass"]
        else "BLOCKED_C3_VERTEX_GENERATOR_NOT_CLOSED"
    )
    result["SF055_terminal_pass"] = False
    result["remaining_lanes"] = {
        "A": "OPEN_BASELINE_EH_GHOST_FLOW_REPRODUCTION",
        "C": "ABSTRACT_MANIFEST_PASS_IMPLEMENTED_DIAGRAM_MANIFEST_OPEN",
        "projected_C3_beta": "UNAUTHORIZED_UNTIL_ALL_CALIBRATION_LANES_TERMINAL",
    }

    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if not result["lane_B_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
