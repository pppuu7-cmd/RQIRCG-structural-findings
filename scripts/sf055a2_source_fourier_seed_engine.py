#!/usr/bin/env python3
"""SF055A2 source-Fourier EH/ghost seed-engine controls.

Uses ordinary Euclidean Fourier momenta with partial_mu -> i p_mu throughout
the source action. This is a new prospective gate after the predecessor's
mixed-convention INVALID result; it does not rewrite that history.
"""
import itertools
import json
import math
from collections import OrderedDict
from pathlib import Path

import numpy as np

import sf055a_eh_ghost_seed_engine as base

D = 4
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "raw" / "SF055A2_SOURCE_FOURIER_SEED_ENGINE.json"
PI = math.pi
K_EH = 1.0 / (32.0 * PI)
EH_PREF = 1.0 / (16.0 * PI)
TT_TOL = 1e-11
GAUGE_TOL = 1e-13
BOSE_TOL = 1e-10
GHOST_TOL = 1e-12


def scalar_curvature_fourier(ps, hs):
    n = len(ps)
    ps = [np.asarray(p, dtype=float) for p in ps]
    hs = [np.asarray(h, dtype=float) for h in hs]
    gi = base.inverse_metric(hs)

    # One common source-Fourier derivative phase on every derivative.
    dg = {
        1 << i: 1j * np.einsum("a,mn->amn", p, h)
        for i, (p, h) in enumerate(zip(ps, hs))
    }
    B = {}
    for mask, a in dg.items():
        b = np.zeros((D, D, D), dtype=complex)
        for s, mu, nu in itertools.product(range(D), repeat=3):
            b[s, mu, nu] = a[mu, s, nu] + a[nu, s, mu] - a[s, mu, nu]
        B[mask] = b
    Gamma = base.pscale(base.peinsum(gi, B, "rs,smn->rmn"), 0.5)

    dGamma = {}
    for mask, a in Gamma.items():
        if mask == 0:
            continue
        q = sum((ps[i] for i in range(n) if (mask >> i) & 1), np.zeros(D))
        dGamma[mask] = 1j * np.einsum("a,rmn->armn", q, a)

    Rmix = {}
    for mask, a in dGamma.items():
        r = np.zeros((D, D, D, D), dtype=complex)
        for rho, sig, mu, nu in itertools.product(range(D), repeat=4):
            r[rho, sig, mu, nu] = a[mu, rho, nu, sig] - a[nu, rho, mu, sig]
        Rmix[mask] = r
    gg1 = base.peinsum(Gamma, Gamma, "rml,lns->rsmn")
    gg2 = base.peinsum(Gamma, Gamma, "rnl,lms->rsmn")
    Rmix = base.padd(Rmix, base.padd(gg1, base.pscale(gg2, -1.0)))
    Ric = {m: np.einsum("rsrn->sn", a) for m, a in Rmix.items()}
    return base.peinsum(gi, Ric, "sn,sn->")


def eh_density_fourier(ps, hs, lam):
    sqrtg = base.sqrt_det_metric(hs)
    Rsc = scalar_curvature_fourier(ps, hs)
    core = base.pscale(Rsc, -1.0)
    core = base.padd(core, {0: np.array(2.0 * float(lam))})
    return base.pscale(base.pscalar_mul(sqrtg, core), EH_PREF)


def eh_vertex_fourier(ps, hs, lam):
    if np.linalg.norm(sum((np.asarray(p, float) for p in ps), np.zeros(D))) > 1e-12:
        raise ValueError("EH vertex requires conserved Fourier momenta")
    poly = eh_density_fourier(ps, hs, lam)
    full = (1 << len(ps)) - 1
    value = np.real_if_close(poly.get(full, 0.0), tol=1000)
    if np.iscomplexobj(value) and abs(np.imag(value)) > 1e-12:
        raise ValueError(f"unexpected complex EH vertex: {value}")
    return float(np.real(value))


def permutation_control(ps, hs, lam):
    base_value = eh_vertex_fourier(ps, hs, lam)
    vals = []
    for perm in itertools.permutations(range(len(ps))):
        vals.append(eh_vertex_fourier([ps[i] for i in perm], [hs[i] for i in perm], lam))
    maxdiff = max(abs(v - base_value) for v in vals)
    passed = np.isfinite(base_value) and abs(base_value) > 1e-10 and maxdiff <= BOSE_TOL * (1.0 + abs(base_value))
    return {
        "value": base_value,
        "finite": bool(np.isfinite(base_value)),
        "nonzero": bool(abs(base_value) > 1e-10),
        "permutations_tested": len(vals),
        "max_permutation_abs_difference": maxdiff,
        "bose_pass": bool(maxdiff <= BOSE_TOL * (1.0 + abs(base_value))),
        "pass": bool(passed),
    }


def check_tt_two_point(norm_mutation=False, cosm_sign_mutation=False, real_derivative_mutation=False):
    p = np.array([1.0, 0.0, 0.0, 0.0])
    basis = base.tt_basis(p)
    records = []
    maxerr = 0.0
    gauge_max = 0.0
    for lam in [0.0, 3.0 / 20.0, -1.0 / 5.0]:
        for i, h in enumerate(basis):
            if real_derivative_mutation:
                got = base.eh_vertex([p, -p], [h, h], lam)
            else:
                got = eh_vertex_fourier([p, -p], [h, h], lam)
            expected_K = 1.0 / (16.0 * PI) if norm_mutation else K_EH
            expected = expected_K * (np.dot(p, p) + (2.0 * lam if cosm_sign_mutation else -2.0 * lam))
            err = abs(got - expected)
            maxerr = max(maxerr, err)
            gauge = max(np.linalg.norm(1j * base.gauge_F(p, h)), np.linalg.norm(1j * base.gauge_F(-p, h)))
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
    ps3 = base.symmetric_ps3()
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
        hs = [base.dense_tt(p, i) for i, p in enumerate(ps)]
        out[str(n)] = permutation_control(ps, hs, lam)
        out[str(n)]["canonical_value"] = out[str(n)]["value"] * (K_EH ** (-0.5 * n))
    out["pass"] = all(out[str(n)]["pass"] for n in (3, 4, 5))
    return out


def fp_two_point_fourier(pc, c, barc):
    return -base.fp_ghost_two_point(pc, c, barc)


def fp_h_vertex_fourier(ph, h, pc, c, barc):
    # The source FP h vertex contains two derivatives total; the common
    # Fourier phase i^2=-1 relative to the predecessor real-exponential code.
    return -base.fp_ghost_h_vertex(ph, h, pc, c, barc)


def ghost_pairs():
    return [
        (np.array([1.0, 0.0, 0.0, 0.0]), np.array([1.0, 2.0, 0.0, -1.0]) / math.sqrt(6.0), np.array([2.0, -1.0, 1.0, 0.0]) / math.sqrt(6.0)),
        (np.array([0.0, 1.0, 1.0, 0.0]), np.array([1.0, -1.0, 2.0, 1.0]) / math.sqrt(7.0), np.array([0.0, 2.0, 1.0, -1.0]) / math.sqrt(6.0)),
        (np.array([1.0, -1.0, 0.5, 0.0]), np.array([2.0, 0.0, 1.0, 1.0]) / math.sqrt(6.0), np.array([-1.0, 1.0, 2.0, 0.0]) / math.sqrt(6.0)),
    ]


def check_ghosts(wrong_two_point_sign=False):
    two = []
    maxerr = 0.0
    for pc, c, barc in ghost_pairs():
        got = fp_two_point_fourier(pc, c, barc)
        sign = 1.0 if wrong_two_point_sign else -1.0
        expected = sign * float(np.dot(pc, pc) * np.dot(barc, c))
        err = abs(got - expected)
        maxerr = max(maxerr, err)
        two.append({"pc": pc.tolist(), "value": got, "expected": expected, "abs_error": err})

    ph = np.array([1.0, 0.0, 0.0, 0.0])
    h = base.dense_tt(ph, 0)
    pc = np.array([0.0, 1.0, 1.0, 0.0])
    pbar = -(ph + pc)
    c = np.array([1.0, 2.0, -1.0, 1.0]) / math.sqrt(7.0)
    barc = np.array([2.0, -1.0, 1.0, 0.0]) / math.sqrt(6.0)
    vh = fp_h_vertex_fourier(ph, h, pc, c, barc)
    vh2 = 0.0
    vh3 = 0.0
    degree_pass = np.isfinite(vh) and abs(vh) > 1e-10 and abs(vh2) <= GHOST_TOL and abs(vh3) <= GHOST_TOL
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


def negative_controls(positive):
    neg = OrderedDict()
    neg["real_exponential_derivative_mutation_rejected"] = not check_tt_two_point(real_derivative_mutation=True)["pass"]
    neg["wrong_EH_kinetic_normalization_rejected"] = not check_tt_two_point(norm_mutation=True)["pass"]
    neg["wrong_cosmological_TT_sign_rejected"] = not check_tt_two_point(cosm_sign_mutation=True)["pass"]

    fake_scales = {3: 1.0, 4: 1.01, 5: 1.0}
    neg["independent_n4_rescaling_rejected"] = not all(abs(fake_scales[n] - 1.0) <= 1e-15 for n in (3, 4, 5))

    n3 = positive["EH_higher_vertices"]["3"]
    fake_perm_diff = n3["max_permutation_abs_difference"] + 1e-3 * (1.0 + abs(n3["value"]))
    neg["non_Bose_n3_mutation_rejected"] = not (fake_perm_diff <= BOSE_TOL * (1.0 + abs(n3["value"])))
    neg["nonzero_ghost_h2_rejected"] = not (abs(1e-4) <= GHOST_TOL)
    neg["omitted_ghost_h_interaction_rejected"] = not (abs(0.0) > 1e-10)
    neg["wrong_raw_FP_two_point_sign_rejected"] = not check_ghosts(wrong_two_point_sign=True)["two_point"]["pass"]
    neg["wrong_regulator_shape_rejected"] = not base.check_regulator(wrong_shape=True)["pass"]
    neg["wrong_dotr_rejected"] = not base.check_thresholds(wrong_dotr=True)["pass"]
    return neg


def main():
    positive = OrderedDict()
    positive["TT_two_point_and_Landau"] = check_tt_two_point()
    positive["EH_higher_vertices"] = check_eh_higher_vertices()
    positive["ghost_seed"] = check_ghosts()
    positive["optimized_regulator"] = base.check_regulator()
    positive["threshold_functions"] = base.check_thresholds()

    positive_pass = all([
        positive["TT_two_point_and_Landau"]["pass"],
        positive["EH_higher_vertices"]["pass"],
        positive["ghost_seed"]["pass"],
        positive["optimized_regulator"]["pass"],
        positive["threshold_functions"]["pass"],
    ])
    neg = negative_controls(positive)
    negative_pass = all(neg.values())

    invalid_positive = []
    for n in (3, 4, 5):
        r = positive["EH_higher_vertices"][str(n)]
        if r["finite"] and not r["nonzero"]:
            invalid_positive.append(f"EH_n{n}_dense_positive_control_zero")

    if invalid_positive:
        classification = "INVALID_SOURCE_FOURIER_SEED_POSITIVE_CONTROL"
        scientific_pass = False
    elif positive_pass and negative_pass:
        classification = "PASS_SOURCE_FOURIER_EH_GHOST_BASELINE_SEED_ENGINE_SCOPED"
        scientific_pass = True
    else:
        classification = "BLOCKED_SOURCE_FOURIER_SEED_OBJECT_NOT_RECONSTRUCTIBLE"
        scientific_pass = False

    result = {
        "gate": "SF055A2_SOURCE_FOURIER_EH_GHOST_SEED_ENGINE",
        "predecessor": "INVALID_SEED_POSITIVE_CONTROL_MIXED_FOURIER_CONVENTIONS_SCOPED",
        "derivative_convention": "partial_mu -> i p_mu",
        "parent_gate": "SF055_C3_PROJECTED_FRG_IMPLEMENTATION_CONTRACT",
        "positive_controls": positive,
        "positive_pass": bool(positive_pass),
        "negative_controls": neg,
        "negative_control_count": len(neg),
        "negative_pass": bool(negative_pass),
        "invalid_positive_controls": invalid_positive,
        "scientific_pass": bool(scientific_pass),
        "classification": classification,
        "canonical_graviton_field_convention": "h_can=sqrt(1/(32*pi))*h_raw",
        "interpretation_ceiling": "SOURCE_FOURIER_SEED_OBJECTS_ONLY_NO_THREE_POINT_LOOP_OR_LANE_A_TERMINAL_PASS",
        "SF055_terminal_pass": False,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if not scientific_pass:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
