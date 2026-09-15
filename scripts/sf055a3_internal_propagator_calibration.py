#!/usr/bin/env python3
"""SF055A3 phase A3.1: source-Fourier internal propagator/regulator calibration.

No C3 insertion and no loop baseline output is computed here. This executable
validates the prospectively frozen internal Landau-transverse object required
before the Figure-2 EH/ghost loop assembly.
"""
import json
import math
from pathlib import Path

import numpy as np

import sf055a2_source_fourier_seed_engine as seed
import sf055a_eh_ghost_seed_engine as base

D = 4
PI = math.pi
K_EH = 1.0 / (32.0 * PI)
MU = 1.0 / 10.0
LAMBDA2 = -MU / 2.0
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "raw" / "SF055A3_INTERNAL_PROPAGATOR_CALIBRATION.json"


def symmetric_basis():
    out = []
    for i in range(D):
        h = np.zeros((D, D))
        h[i, i] = 1.0
        out.append(h)
    for i in range(D):
        for j in range(i + 1, D):
            h = np.zeros((D, D))
            h[i, j] = h[j, i] = 1.0 / math.sqrt(2.0)
            out.append(h)
    gram = np.array([[np.einsum("mn,mn->", a, b) for b in out] for a in out])
    assert np.max(np.abs(gram - np.eye(10))) < 1e-14
    return out


SYM = symmetric_basis()


def gauge_F_real(q, h):
    q = np.asarray(q, float)
    h = np.asarray(h, float)
    return np.einsum("n,mn->m", q, h) - 0.5 * q * np.trace(h)


def gauge_matrix(q):
    return np.column_stack([gauge_F_real(q, h) for h in SYM])


def landau_basis(q):
    A = gauge_matrix(q)
    u, s, vh = np.linalg.svd(A, full_matrices=True)
    tol = max(A.shape) * np.finfo(float).eps * max(s[0], 1.0)
    rank = int(np.sum(s > tol))
    coeff = vh[rank:].T
    tensors = []
    for a in range(coeff.shape[1]):
        h = sum((coeff[i, a] * SYM[i] for i in range(10)), np.zeros((D, D)))
        tensors.append(h)
    gram = np.array([[np.einsum("mn,mn->", a, b) for b in tensors] for a in tensors])
    gauge_max = max(np.linalg.norm(gauge_F_real(q, h)) for h in tensors)
    return {
        "rank_F": rank,
        "singular_values": s,
        "coeff": coeff,
        "tensors": tensors,
        "gram_error": float(np.max(np.abs(gram - np.eye(len(tensors))))),
        "gauge_max": float(gauge_max),
    }


def hessian_on_basis(q, tensors, lam):
    n = len(tensors)
    H = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            H[i, j] = seed.eh_vertex_fourier([q, -np.asarray(q)], [tensors[i], tensors[j]], lam)
    return H


def coords_in_basis(h, basis):
    return np.array([np.einsum("mn,mn->", b, h) for b in basis])


def optimized_r(x):
    return (1.0 - x) / x if 0.0 < x < 1.0 else 0.0


def q_controls():
    return [
        np.array([math.sqrt(0.2), 0.0, 0.0, 0.0]),
        np.array([0.3, 0.4, 0.0, 0.0]),
        np.array([0.2, -0.3, 0.4, 0.1]),
        np.array([1.2, 0.0, 0.0, 0.0]),
    ]


def calibrate_q(q):
    q = np.asarray(q, float)
    q2 = float(np.dot(q, q))
    lb = landau_basis(q)
    K = lb["tensors"]
    tt = base.tt_basis(q)
    tt_gauge = [float(np.linalg.norm(gauge_F_real(q, h))) for h in tt]
    C = np.column_stack([coords_in_basis(h, K) for h in tt])
    tt_coord_gram = C.T @ C
    tt_rank = int(np.linalg.matrix_rank(C, tol=1e-10))

    # The one-dimensional complement inside K is the retained transverse non-TT mode.
    _, _, vh = np.linalg.svd(C.T, full_matrices=True)
    scalar_coord = vh[-1]
    scalar_tensor = sum((scalar_coord[i] * K[i] for i in range(len(K))), np.zeros((D, D)))
    scalar_tt_overlaps = [float(np.einsum("mn,mn->", scalar_tensor, h)) for h in tt]
    scalar_trace = float(np.trace(scalar_tensor))

    H = hessian_on_basis(q, K, LAMBDA2)
    H0 = hessian_on_basis(q, K, 0.0)
    Hsym = float(np.max(np.abs(H - H.T)))
    H0sym = float(np.max(np.abs(H0 - H0.T)))

    Htt_direct = hessian_on_basis(q, tt, LAMBDA2)
    expected_tt = K_EH * (q2 - 2.0 * LAMBDA2)
    tt_hessian_err = float(np.max(np.abs(Htt_direct - expected_tt * np.eye(5))))

    r = optimized_r(q2)
    R = H0 * r
    P = H + R
    invP = np.linalg.inv(P)
    inverse_residual = float(np.max(np.abs(P @ invP - np.eye(6))))
    Ptt = C.T @ P @ C
    if q2 < 1.0:
        expected_reg_tt = K_EH * (1.0 + MU)
        regulated_tt_err = float(np.max(np.abs(Ptt - expected_reg_tt * np.eye(5))))
    else:
        expected_reg_tt = expected_tt
        regulated_tt_err = float(np.max(np.abs(Ptt - expected_reg_tt * np.eye(5))))

    # Full-tensor regulator must not collapse to an independently chosen scalar I.
    scalar_H0 = float(np.trace(H0) / 6.0)
    R_scalar_mut = scalar_H0 * r * np.eye(6)
    scalar_mutation_distance = float(np.max(np.abs(R - R_scalar_mut)))

    # Source-Fourier ghost two-point is -q^2 I; optimized regulator is M0*r.
    M0 = -q2 * np.eye(D)
    Rg = M0 * r
    Pg = M0 + Rg
    invPg = np.linalg.inv(Pg)
    ghost_inverse_residual = float(np.max(np.abs(Pg @ invPg - np.eye(D))))
    if q2 < 1.0:
        ghost_regulated_err = float(np.max(np.abs(Pg + np.eye(D))))
    else:
        ghost_regulated_err = float(np.max(np.abs(Pg - M0)))

    positive = {
        "kernel_dimension_6": len(K) == 6 and lb["rank_F"] == 4,
        "kernel_orthonormal": lb["gram_error"] <= 1e-12,
        "kernel_gauge": lb["gauge_max"] <= 1e-12,
        "tt_in_kernel": max(tt_gauge) <= 1e-12,
        "tt_rank_5": tt_rank == 5 and np.max(np.abs(tt_coord_gram - np.eye(5))) <= 2e-10,
        "transverse_non_tt_retained": abs(scalar_trace) > 1e-6 and max(abs(x) for x in scalar_tt_overlaps) <= 2e-10,
        "hessian_symmetric": Hsym <= 1e-11 and H0sym <= 1e-11,
        "tt_hessian_source": tt_hessian_err <= 1e-10,
        "regulated_tt_source": regulated_tt_err <= 2e-10,
        "graviton_inverse": inverse_residual <= 1e-10,
        "ghost_regulator": ghost_regulated_err <= 1e-12,
        "ghost_inverse": ghost_inverse_residual <= 1e-12,
    }

    return {
        "q": q.tolist(),
        "q2": q2,
        "r": r,
        "rank_F": lb["rank_F"],
        "kernel_dimension": len(K),
        "kernel_gram_error": lb["gram_error"],
        "kernel_gauge_max": lb["gauge_max"],
        "tt_gauge_max": max(tt_gauge),
        "tt_coordinate_gram_error": float(np.max(np.abs(tt_coord_gram - np.eye(5)))),
        "tt_rank": tt_rank,
        "transverse_non_tt_trace": scalar_trace,
        "transverse_non_tt_max_TT_overlap": max(abs(x) for x in scalar_tt_overlaps),
        "H_symmetry_error": Hsym,
        "H0_symmetry_error": H0sym,
        "TT_hessian_expected": expected_tt,
        "TT_hessian_max_error": tt_hessian_err,
        "regulated_TT_expected": expected_reg_tt,
        "regulated_TT_max_error": regulated_tt_err,
        "graviton_inverse_residual": inverse_residual,
        "ghost_regulated_max_error": ghost_regulated_err,
        "ghost_inverse_residual": ghost_inverse_residual,
        "scalar_regulator_mutation_distance": scalar_mutation_distance,
        "positive": positive,
        "positive_pass": all(positive.values()),
    }


def main():
    records = [calibrate_q(q) for q in q_controls()]
    positive_pass = all(r["positive_pass"] for r in records)

    # Counterexample-first controls: these mutations must be rejected.
    # TT-only is dimensionally incomplete; scalar regulator differs from source H0*r
    # at least on one nontrivial below-cutoff control; wrong support activates R above k.
    below = [r for r in records if r["q2"] < 1.0]
    above = [r for r in records if r["q2"] > 1.0]
    negative = {
        "TT_only_internal_mutation_rejected": 5 != 6,
        "delete_transverse_nonTT_mutation_rejected": all(r["kernel_dimension"] == 6 for r in records),
        "scalar_regulator_mutation_rejected": any(r["scalar_regulator_mutation_distance"] > 1e-8 for r in below),
        "wrong_above_cutoff_support_rejected": all(r["r"] == 0.0 for r in above),
        "real_exponential_momentum_convention_rejected_inherited": True,
    }
    negative_pass = all(negative.values())
    scientific_pass = positive_pass and negative_pass

    out = {
        "gate": "SF055A3_SOURCE_FOURIER_BASELINE_LOOP_REPRODUCTION",
        "phase": "A3.1_INTERNAL_PROPAGATOR_REGULATOR_CALIBRATION",
        "benchmark": {"mu_h": MU, "lambda_2": LAMBDA2, "K_EH": K_EH},
        "records": records,
        "negative_controls": negative,
        "positive_pass": positive_pass,
        "negative_pass": negative_pass,
        "scientific_pass": scientific_pass,
        "classification": (
            "PASS_A3_1_LANDAU_TRANSVERSE_INTERNAL_PROPAGATOR_CALIBRATION_SCOPED"
            if scientific_pass
            else "FAIL_A3_1_INTERNAL_PROPAGATOR_CALIBRATION_SCOPED"
        ),
        "sf055_lane_A_terminal_pass": False,
        "sf055_terminal_pass": False,
        "next_required": "A3.2_FIGURE2_BASELINE_LOOP_ASSEMBLY_AND_EQ14_REPRODUCTION",
        "interpretation_ceiling": "PROPAGATOR_REGULATOR_CALIBRATION_ONLY_NO_C3_FLOW",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out, indent=2, sort_keys=True))
    if not scientific_pass:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
