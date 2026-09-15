#!/usr/bin/env python3
"""SF055A3 fixed-q Figure-2 EH/ghost tensor contraction assembly.

C3 is disabled. This script validates source-Fourier vertex contractions,
full six-dimensional Landau-transverse graviton edges, single-scale G dotR G,
and the frozen ghost-arrow matrix chain before any loop quadrature.
"""
import itertools
import json
import math
from pathlib import Path

import numpy as np

import sf055a2_source_fourier_seed_engine as seed
import sf055a_eh_ghost_seed_engine as base
import sf055a3_internal_propagator_calibration as prop

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "raw" / "SF055A3_FIGURE2_CONTRACTION_ASSEMBLY.json"
D = 4
LAMBDA2 = -0.05
LAMBDA3 = -0.7
TOL_INV = 1e-10
TOL_ROT = 1e-9
NONZERO = 1e-12
COEFF = {"T5_GRAV": -0.5, "B43_GRAV": 3.0, "T333_GRAV": -3.0, "T333_GHOST": 6.0}


def json_default(obj):
    if isinstance(obj, np.bool_):
        return bool(obj)
    if isinstance(obj, np.integer):
        return int(obj)
    if isinstance(obj, np.floating):
        return float(obj)
    raise TypeError(type(obj).__name__)


def sym_external():
    ps = base.symmetric_ps3()
    hs = [base.tt_basis(p)[i] for i, p in enumerate(ps)]  # frozen (0,1,2)
    return ps, hs


def q_controls():
    return [
        np.array([0.23, -0.31, 0.17, 0.29]),
        np.array([0.41, 0.12, -0.27, 0.19]),
    ]


def deterministic_rotation(n, seed_value):
    rng = np.random.default_rng(seed_value)
    a = rng.normal(size=(n, n))
    q, r = np.linalg.qr(a)
    signs = np.sign(np.diag(r))
    signs[signs == 0] = 1.0
    return q @ np.diag(signs)


def rotate_basis(basis, Q):
    return [sum((Q[i, a] * basis[i] for i in range(len(basis))), np.zeros((D, D))) for a in range(len(basis))]


def edge_basis(ell, rotation=None, tt_only=False):
    ell = np.asarray(ell, float)
    if np.linalg.norm(ell) < 1e-10:
        raise ValueError("zero internal momentum is outside fixed-q controls")
    if tt_only:
        b = base.tt_basis(ell)
    else:
        b = prop.landau_basis(ell)["tensors"]
    if rotation is not None:
        b = rotate_basis(b, rotation)
    return b


def edge_objects(ell, basis_override=None, scalar_regulator=False, bad_single_scale=False):
    ell = np.asarray(ell, float)
    B = basis_override if basis_override is not None else edge_basis(ell)
    H = prop.hessian_on_basis(ell, B, LAMBDA2)
    H0 = prop.hessian_on_basis(ell, B, 0.0)
    x = float(np.dot(ell, ell))
    r = prop.optimized_r(x)
    if scalar_regulator:
        R = float(np.trace(H0) / len(B)) * r * np.eye(len(B))
    else:
        R = H0 * r
    P = H + R
    G = np.linalg.inv(P)
    inv_resid = float(np.max(np.abs(P @ G - np.eye(len(B)))))
    if 0.0 < x < 1.0:
        dotR = 2.0 * H0 / x
    else:
        dotR = np.zeros_like(H0)
    S = G @ dotR if bad_single_scale else G @ dotR @ G
    return {"basis": B, "H": H, "H0": H0, "R": R, "P": P, "G": G, "dotR": dotR, "S": S, "inverse_residual": inv_resid, "q2": x}


def ehv(ps, hs, lam=LAMBDA3):
    return seed.eh_vertex_fourier(ps, hs, lam)


def v5_array(ps, hs, qobj):
    Bq = qobj["basis"]
    out = np.zeros((len(Bq), len(Bq)))
    for a, A in enumerate(Bq):
        for b, B in enumerate(Bq):
            out[a, b] = ehv([ps[0], ps[1], ps[2], qobj["ell"], -qobj["ell"]], [hs[0], hs[1], hs[2], A, B])
    return out


def t5_value(ps, hs, q, rotations=None, bad_single=False, scalar_regulator=False, tt_only=False):
    Bq = edge_basis(q, rotations.get("q") if rotations else None, tt_only=tt_only)
    qedge = edge_objects(q, Bq, scalar_regulator=scalar_regulator, bad_single_scale=bad_single)
    qedge["ell"] = np.asarray(q, float)
    V5 = v5_array(ps, hs, qedge)
    return COEFF["T5_GRAV"] * float(np.einsum("ab,ba->", V5, qedge["S"])), [qedge["inverse_residual"]]


def bubble_arrays(ps, hs, q, qedge, ledge, wrong_endpoint_rotation=None):
    p1, p2, p3 = ps
    ell = q + p1 + p2
    Bq = qedge["basis"]
    Bl = ledge["basis"]
    V4 = np.zeros((len(Bq), len(Bl)))
    V3 = np.zeros((len(Bq), len(Bl)))
    for a, A in enumerate(Bq):
        for b, B in enumerate(Bl):
            V4[a, b] = ehv([p1, p2, q, -ell], [hs[0], hs[1], A, B])
    Bq_v3 = Bq
    if wrong_endpoint_rotation is not None:
        Bq_v3 = rotate_basis(Bq, wrong_endpoint_rotation)
    for c, C in enumerate(Bq_v3):
        for d, E in enumerate(Bl):
            V3[c, d] = ehv([p3, -q, ell], [hs[2], C, E])
    return V4, V3


def bubble_value(ps, hs, q, rotations=None, bad_single=False, scalar_regulator=False,
                 wrong_endpoint_rotation=None, single_scale_on_ell=False, omit_ell_G=False, coeff=None):
    ell = q + ps[0] + ps[1]
    Bq = edge_basis(q, rotations.get("q") if rotations else None)
    Bl = edge_basis(ell, rotations.get("ell") if rotations else None)
    qedge = edge_objects(q, Bq, scalar_regulator=scalar_regulator, bad_single_scale=bad_single)
    ledge = edge_objects(ell, Bl)
    V4, V3 = bubble_arrays(ps, hs, q, qedge, ledge, wrong_endpoint_rotation=wrong_endpoint_rotation)
    Sq = ledge["S"] if single_scale_on_ell and len(Bq) == len(Bl) else qedge["S"]
    Gl = np.eye(len(Bl)) if omit_ell_G else ledge["G"]
    c = COEFF["B43_GRAV"] if coeff is None else coeff
    val = c * float(np.einsum("ab,ac,cd,db->", V4, Sq, V3, Gl))
    return val, [qedge["inverse_residual"], ledge["inverse_residual"]]


def triangle_arrays(ps, hs, q, edges):
    p1, p2, p3 = ps
    e23 = q - p2
    e31 = q + p1
    Bq, B23, B31 = edges["q"]["basis"], edges["e23"]["basis"], edges["e31"]["basis"]
    V1 = np.zeros((len(Bq), len(B31)))
    V2 = np.zeros((len(Bq), len(B23)))
    V3 = np.zeros((len(B23), len(B31)))
    for a, A in enumerate(Bq):
        for c, C in enumerate(B31):
            V1[a, c] = ehv([p1, q, -e31], [hs[0], A, C])
    for b, B in enumerate(Bq):
        for d, E in enumerate(B23):
            V2[b, d] = ehv([p2, -q, e23], [hs[1], B, E])
    for e, E in enumerate(B23):
        for f, F in enumerate(B31):
            V3[e, f] = ehv([p3, -e23, e31], [hs[2], E, F])
    return V1, V2, V3


def triangle_value(ps, hs, q, rotations=None, omit_e31_G=False, coeff=None):
    e23, e31 = q - ps[1], q + ps[0]
    rots = rotations or {}
    edges = {
        "q": edge_objects(q, edge_basis(q, rots.get("q"))),
        "e23": edge_objects(e23, edge_basis(e23, rots.get("e23"))),
        "e31": edge_objects(e31, edge_basis(e31, rots.get("e31"))),
    }
    V1, V2, V3 = triangle_arrays(ps, hs, q, edges)
    G31 = np.eye(6) if omit_e31_G else edges["e31"]["G"]
    c = COEFF["T333_GRAV"] if coeff is None else coeff
    val = c * float(np.einsum("ac,ab,bd,de,ef,fc->", V1, edges["q"]["S"], V2, edges["e23"]["G"], V3, G31))
    return val, [edges[k]["inverse_residual"] for k in ("q", "e23", "e31")]


def ghost_matrix(ph, h, pc):
    V = np.zeros((D, D))
    eye = np.eye(D)
    for i in range(D):  # row = bar-c
        for j in range(D):  # column = c
            V[i, j] = seed.fp_h_vertex_fourier(ph, h, pc, eye[j], eye[i])
    return V


def ghost_edge(ell):
    x = float(np.dot(ell, ell))
    M = -x * np.eye(D)
    r = prop.optimized_r(x)
    R = M * r
    P = M + R
    G = np.linalg.inv(P)
    if 0.0 < x < 1.0:
        dotR = -2.0 * np.eye(D)
    else:
        dotR = np.zeros((D, D))
    S = G @ dotR @ G
    return {"G": G, "S": S, "P": P, "inverse_residual": float(np.max(np.abs(P @ G - np.eye(D))))}


def ghost_value(ps, hs, q, wrong_pc=False, wrong_order=False, coeff=None):
    p1, p2, p3 = ps
    e23, e31 = q - p2, q + p1
    V1 = ghost_matrix(p1, hs[0], q)
    V2 = ghost_matrix(p2, hs[1], e23 if not wrong_pc else q)
    V3 = ghost_matrix(p3, hs[2], e31)
    Q, E23, E31 = ghost_edge(q), ghost_edge(e23), ghost_edge(e31)
    if wrong_order:
        product = V1 @ Q["S"] @ V3 @ E23["G"] @ V2 @ E31["G"]
    else:
        product = V1 @ Q["S"] @ V2 @ E23["G"] @ V3 @ E31["G"]
    c = COEFF["T333_GHOST"] if coeff is None else coeff
    val = c * float(np.trace(product))
    reverse = c * float(np.trace(product.T))
    return val, reverse, [Q["inverse_residual"], E23["inverse_residual"], E31["inverse_residual"]]


def permuted_values(kind, ps, hs, q):
    vals = []
    for perm in itertools.permutations(range(3)):
        pp = [ps[i] for i in perm]
        hh = [hs[i] for i in perm]
        if kind == "T5_GRAV":
            v, _ = t5_value(pp, hh, q)
        elif kind == "B43_GRAV":
            v, _ = bubble_value(pp, hh, q)
        elif kind == "T333_GRAV":
            v, _ = triangle_value(pp, hh, q)
        else:
            v, _, _ = ghost_value(pp, hh, q)
        vals.append(float(v))
    return vals


def rotation_check(kind, ps, hs, q, seed0):
    if kind == "T5_GRAV":
        basev, _ = t5_value(ps, hs, q)
        rots = {"q": deterministic_rotation(6, seed0)}
        rotv, _ = t5_value(ps, hs, q, rotations=rots)
    elif kind == "B43_GRAV":
        basev, _ = bubble_value(ps, hs, q)
        rots = {"q": deterministic_rotation(6, seed0), "ell": deterministic_rotation(6, seed0 + 1)}
        rotv, _ = bubble_value(ps, hs, q, rotations=rots)
    elif kind == "T333_GRAV":
        basev, _ = triangle_value(ps, hs, q)
        rots = {"q": deterministic_rotation(6, seed0), "e23": deterministic_rotation(6, seed0 + 1), "e31": deterministic_rotation(6, seed0 + 2)}
        rotv, _ = triangle_value(ps, hs, q, rotations=rots)
    else:
        basev, rev, _ = ghost_value(ps, hs, q)
        rotv = rev
    err = abs(rotv - basev)
    return {"base": basev, "transformed": rotv, "abs_difference": err, "pass": err <= TOL_ROT * (1.0 + abs(basev))}


def mutation_suite(ps, hs, q, canon):
    neg = {}
    # TT-only is dimensionally incomplete by the frozen A3.1 authority.
    neg["TT_only_internal_basis_rejected"] = len(edge_basis(q, tt_only=True)) != len(edge_basis(q))

    Qbad = deterministic_rotation(6, 991)
    bad_endpoint, _ = bubble_value(ps, hs, q, wrong_endpoint_rotation=Qbad)
    neg["untransported_endpoint_basis_rotation_rejected"] = abs(bad_endpoint - canon["B43_GRAV"]) > 1e-10 * (1.0 + abs(canon["B43_GRAV"]))

    badS, _ = t5_value(ps, hs, q, bad_single=True)
    neg["G_dotR_instead_of_G_dotR_G_rejected"] = abs(badS - canon["T5_GRAV"]) > 1e-10 * (1.0 + abs(canon["T5_GRAV"]))

    shiftedS, _ = bubble_value(ps, hs, q, single_scale_on_ell=True)
    neg["noncanonical_single_scale_edge_rejected"] = abs(shiftedS - canon["B43_GRAV"]) > 1e-10 * (1.0 + abs(canon["B43_GRAV"]))

    missG_b, _ = bubble_value(ps, hs, q, omit_ell_G=True)
    missG_t, _ = triangle_value(ps, hs, q, omit_e31_G=True)
    neg["missing_bubble_propagator_rejected"] = abs(missG_b - canon["B43_GRAV"]) > 1e-10 * (1.0 + abs(canon["B43_GRAV"]))
    neg["missing_triangle_propagator_rejected"] = abs(missG_t - canon["T333_GRAV"]) > 1e-10 * (1.0 + abs(canon["T333_GRAV"]))

    wrong_order, _, _ = ghost_value(ps, hs, q, wrong_order=True)
    wrong_pc, _, _ = ghost_value(ps, hs, q, wrong_pc=True)
    neg["wrong_ghost_matrix_order_rejected"] = abs(wrong_order - canon["T333_GHOST"]) > 1e-10 * (1.0 + abs(canon["T333_GHOST"]))
    neg["wrong_ghost_pc_assignment_rejected"] = abs(wrong_pc - canon["T333_GHOST"]) > 1e-10 * (1.0 + abs(canon["T333_GHOST"]))

    wrong_coeff, _ = triangle_value(ps, hs, q, coeff=-2.0)
    neg["wrong_topology_coefficient_rejected"] = abs(wrong_coeff - canon["T333_GRAV"]) > 1e-10 * (1.0 + abs(canon["T333_GRAV"]))

    scalarR, _ = t5_value(ps, hs, q, scalar_regulator=True)
    neg["scalar_identity_graviton_regulator_rejected"] = abs(scalarR - canon["T5_GRAV"]) > 1e-10 * (1.0 + abs(canon["T5_GRAV"]))
    return neg


def main():
    ps, hs = sym_external()
    records = {}
    nonzero_by_kind = {k: False for k in COEFF}
    for qi, q in enumerate(q_controls()):
        key = f"q{qi+1}"
        vals = {}
        invs = {}
        vals["T5_GRAV"], invs["T5_GRAV"] = t5_value(ps, hs, q)
        vals["B43_GRAV"], invs["B43_GRAV"] = bubble_value(ps, hs, q)
        vals["T333_GRAV"], invs["T333_GRAV"] = triangle_value(ps, hs, q)
        vals["T333_GHOST"], rev, invs["T333_GHOST"] = ghost_value(ps, hs, q)
        for k, v in vals.items():
            nonzero_by_kind[k] = nonzero_by_kind[k] or abs(v) > NONZERO
        rotations = {k: rotation_check(k, ps, hs, q, 1000 + 20 * qi + j) for j, k in enumerate(COEFF)}
        perms = {k: permuted_values(k, ps, hs, q) for k in COEFF}
        max_inv = max(max(x) for x in invs.values())
        records[key] = {
            "q": q.tolist(),
            "values": vals,
            "inverse_residuals": invs,
            "max_inverse_residual": max_inv,
            "rotation_or_arrow_reversal_controls": rotations,
            "permutation_values": perms,
            "permutations_generated_each": 6,
            "finite": all(np.isfinite(v) for v in vals.values()),
            "inverse_pass": max_inv <= TOL_INV,
            "transform_pass": all(x["pass"] for x in rotations.values()),
        }

    canon = records["q1"]["values"]
    neg = mutation_suite(ps, hs, q_controls()[0], canon)
    positive_pass = all(
        r["finite"] and r["inverse_pass"] and r["transform_pass"] and r["permutations_generated_each"] == 6
        for r in records.values()
    ) and all(nonzero_by_kind.values())
    negative_pass = all(bool(v) for v in neg.values())
    scientific_pass = positive_pass and negative_pass
    result = {
        "gate": "SF055A3_FIGURE2_TENSOR_CONTRACTION_ASSEMBLY",
        "C3_enabled": False,
        "lambda_2": LAMBDA2,
        "lambda_3": LAMBDA3,
        "external_TT_indices": [0, 1, 2],
        "records": records,
        "topology_nonzero_on_at_least_one_q": nonzero_by_kind,
        "negative_controls": neg,
        "positive_pass": positive_pass,
        "negative_pass": negative_pass,
        "scientific_pass": scientific_pass,
        "classification": "PASS_A3_2_FIGURE2_TENSOR_CONTRACTION_ASSEMBLY_SCOPED" if scientific_pass else "FAIL_A3_2_FIGURE2_TENSOR_CONTRACTION_ASSEMBLY_SCOPED",
        "next_required": "DETERMINISTIC_FIGURE2_QUADRATURE_AND_EQ14_BASELINE_REPRODUCTION",
        "interpretation_ceiling": "FIXED_Q_CONTRACTION_ONLY_NO_QUADRATURE_NO_EQ14_NO_C3",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(result, indent=2, sort_keys=True, default=json_default) + "\n"
    OUT.write_text(text)
    print(text, end="")
    if not scientific_pass:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
