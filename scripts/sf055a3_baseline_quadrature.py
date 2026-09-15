#!/usr/bin/env python3
"""SF055A3 frozen EH/ghost baseline quadrature.

C3 is disabled.  This is the integrated continuation of the already-validated
Figure-2 contraction path.  It uses the exact source-normalized TT projectors,
full 6D Landau-transverse internal graviton sector, optimized regulator,
source Sym_3 normalization, and deterministic Gauss-Legendre quadrature.
"""
import argparse
import itertools
import json
import math
from pathlib import Path

import numpy as np

import sf055a3_numba_source as fast
import sf055a2_source_fourier_seed_engine as seed
import sf055a_eh_ghost_seed_engine as base
import sf055a3_figure2_contraction_assembly as fig

D = 4
PI = math.pi
K_EH = 1.0 / (32.0 * PI)
MU = 1.0 / 10.0
LAMBDA2 = -MU / 2.0
LAMBDA3 = -7.0 / 10.0
ZERO = 1e-15
SELF_TOL = 2e-9
ROOT = Path(__file__).resolve().parents[1]

UNIT_PS = [
    np.array([1.0, 0.0, 0.0, 0.0]),
    np.array([-0.5, math.sqrt(3.0) / 2.0, 0.0, 0.0]),
    np.array([-0.5, -math.sqrt(3.0) / 2.0, 0.0, 0.0]),
]
EXT_BASES = [np.asarray(base.tt_basis(p), float) for p in UNIT_PS]
INDEX_CACHE = {}


def jdefault(x):
    if isinstance(x, np.bool_):
        return bool(x)
    if isinstance(x, np.integer):
        return int(x)
    if isinstance(x, np.floating):
        return float(x)
    if isinstance(x, np.ndarray):
        return x.tolist()
    raise TypeError(type(x).__name__)


def cartesian_indices(sizes):
    key = tuple(int(s) for s in sizes)
    if key not in INDEX_CACHE:
        INDEX_CACHE[key] = np.asarray(list(itertools.product(*[range(s) for s in key])), dtype=np.int64)
    return INDEX_CACHE[key]


def make_vertex_batch(ps, bases):
    ps = [np.asarray(p, float) for p in ps]
    bases = [np.asarray(B, float) for B in bases]
    sizes = tuple(len(B) for B in bases)
    inds = cartesian_indices(sizes)
    count = len(inds)
    n = len(ps)
    P = np.empty((count, n, D), float)
    H = np.empty((count, n, D, D), float)
    for leg in range(n):
        P[:, leg, :] = ps[leg]
        H[:, leg, :, :] = bases[leg][inds[:, leg]]
    return P, H, sizes


def eval_requests(requests, lam):
    """Evaluate several same-n cartesian vertex batches in one JIT call."""
    built = [make_vertex_batch(ps, bases) for ps, bases in requests]
    if not built:
        return []
    n = built[0][0].shape[1]
    if any(x[0].shape[1] != n for x in built):
        raise ValueError("eval_requests requires equal vertex order")
    lengths = [x[0].shape[0] for x in built]
    P = np.concatenate([x[0] for x in built], axis=0)
    H = np.concatenate([x[1] for x in built], axis=0)
    vals = fast.eval_many(P, H, float(lam))
    out = []
    off = 0
    for (Pb, Hb, shape), length in zip(built, lengths):
        out.append(vals[off:off + length].reshape(shape))
        off += length
    return out


def vertex_tensor(ps, bases, lam):
    return eval_requests([(ps, bases)], lam)[0]


def analytic_landau_basis(p):
    p = np.asarray(p, float)
    nrm = float(np.linalg.norm(p))
    if nrm <= 1e-13:
        raise ValueError("zero internal momentum has measure zero and is not a quadrature node")
    u = p / nrm
    tt = np.asarray(base.tt_basis(p), float)
    hs = (np.eye(D) + 2.0 * np.outer(u, u)) / math.sqrt(12.0)
    B = np.concatenate([tt, hs[None, :, :]], axis=0)
    return B


def grav_G_diag(p):
    x = float(np.dot(p, p))
    d = max(x, 1.0) + MU
    return np.array([1.0 / (K_EH * d)] * 5 + [-2.0 / (K_EH * d)])


def grav_S_q_diag():
    d = 1.0 + MU
    return np.array([2.0 / (K_EH * d * d)] * 5 + [-4.0 / (K_EH * d * d)])


def ghost_G_scalar(p):
    return -1.0 / max(float(np.dot(p, p)), 1.0)


def ghost_S_q_scalar():
    return -2.0


def ghost_matrix(ph, h, pc):
    """Source-Fourier FP h vertex matrix: rows bar-c, columns c."""
    ph = np.asarray(ph, float)
    h = np.asarray(h, float)
    pc = np.asarray(pc, float)
    q = ph + pc
    V = np.zeros((D, D), float)
    for j in range(D):
        hj = h[:, j]
        dh = ph[j] * h + np.outer(hj, pc) + np.outer(pc, hj)
        dF = dh @ q - 0.5 * q * np.trace(dh)
        V[:, j] = -dF
    return V


def build_projectors():
    TG = vertex_tensor(UNIT_PS, EXT_BASES, 0.0)
    zeros = [np.zeros(D) for _ in range(3)]
    TL = vertex_tensor(zeros, EXT_BASES, 1.0)
    return TG, TL


def grouped_pairs(T):
    return [(a, b) for a in range(5) for b in range(5) if np.linalg.norm(T[a, b, :]) > ZERO]


def t5_projected_batch(Ts, ps, q, Bq, Sq):
    """Exact Q1 regrouping for one or more complete TT projectors."""
    P_all = []
    H_all = []
    specs = []
    for T in Ts:
        pairs = grouped_pairs(T)
        count = len(pairs) * 6
        P = np.empty((count, 5, D), float)
        H = np.empty((count, 5, D, D), float)
        k = 0
        for a, b in pairs:
            h3 = np.tensordot(T[a, b, :], EXT_BASES[2], axes=(0, 0))
            for i in range(6):
                P[k] = np.asarray([ps[0], ps[1], ps[2], q, -q])
                H[k] = np.asarray([EXT_BASES[0][a], EXT_BASES[1][b], h3, Bq[i], Bq[i]])
                k += 1
        P_all.append(P)
        H_all.append(H)
        specs.append((len(pairs), count))
    values = fast.eval_many(np.concatenate(P_all), np.concatenate(H_all), LAMBDA3)
    out = []
    off = 0
    for npairs, count in specs:
        arr = values[off:off + count].reshape(npairs, 6)
        out.append(-0.5 * float(np.sum(arr * Sq[None, :])))
        off += count
    return out


def three_point_projected(pmag, q, TG, TL=None):
    ps = [float(pmag) * p for p in UNIT_PS]
    q = np.asarray(q, float)
    Bq = analytic_landau_basis(q)
    Sq = grav_S_q_diag()
    want_lambda = TL is not None

    t5s = t5_projected_batch([TG] + ([TL] if want_lambda else []), ps, q, Bq, Sq)
    topo_g = {"T5_GRAV": t5s[0]}
    topo_l = {"T5_GRAV": t5s[1]} if want_lambda else {}

    # 4/3 bubble.
    ell = q + ps[0] + ps[1]
    Bl = analytic_landau_basis(ell)
    Gl = grav_G_diag(ell)
    V4 = vertex_tensor([ps[0], ps[1], q, -ell], [EXT_BASES[0], EXT_BASES[1], Bq, Bl], LAMBDA3)

    # One combined n=3 JIT call supplies the bubble and all three triangle vertices.
    e23 = q - ps[1]
    e31 = q + ps[0]
    B23 = analytic_landau_basis(e23)
    B31 = analytic_landau_basis(e31)
    req3 = [
        ([ps[2], -q, ell], [EXT_BASES[2], Bq, Bl]),
        ([ps[0], q, -e31], [EXT_BASES[0], Bq, B31]),
        ([ps[1], -q, e23], [EXT_BASES[1], Bq, B23]),
        ([ps[2], -e23, e31], [EXT_BASES[2], B23, B31]),
    ]
    V3b, V1, V2, V3 = eval_requests(req3, LAMBDA3)
    Fb = 3.0 * np.einsum("abij,i,cij,j->abc", V4, Sq, V3b, Gl, optimize=True)
    topo_g["B43_GRAV"] = float(np.sum(TG * Fb))
    if want_lambda:
        topo_l["B43_GRAV"] = float(np.sum(TL * Fb))

    G23 = grav_G_diag(e23)
    G31 = grav_G_diag(e31)
    Ft = -3.0 * np.einsum("aij,i,bik,k,ckj,j->abc", V1, Sq, V2, G23, V3, G31, optimize=True)
    topo_g["T333_GRAV"] = float(np.sum(TG * Ft))
    if want_lambda:
        topo_l["T333_GRAV"] = float(np.sum(TL * Ft))

    A = np.asarray([ghost_matrix(ps[0], h, q) for h in EXT_BASES[0]])
    B = np.asarray([ghost_matrix(ps[1], h, e23) for h in EXT_BASES[1]])
    C = np.asarray([ghost_matrix(ps[2], h, e31) for h in EXT_BASES[2]])
    Fgh = (6.0 * ghost_S_q_scalar() * ghost_G_scalar(e23) * ghost_G_scalar(e31)
           * np.einsum("aij,bjk,cki->abc", A, B, C, optimize=True))
    topo_g["T333_GHOST"] = float(np.sum(TG * Fgh))
    if want_lambda:
        topo_l["T333_GHOST"] = float(np.sum(TL * Fgh))

    return topo_g, topo_l


def two_point_projected(q):
    """Complete external-TT trace at p=0 for the source mass flow."""
    q = np.asarray(q, float)
    Bq = analytic_landau_basis(q)
    Bext = np.asarray(base.tt_basis(np.array([1.0, 0.0, 0.0, 0.0])), float)
    Sq = grav_S_q_diag()
    Gq = grav_G_diag(q)
    z = np.zeros(D)

    P4 = np.empty((5 * 6, 4, D), float)
    H4 = np.empty((5 * 6, 4, D, D), float)
    k = 0
    for a in range(5):
        for i in range(6):
            P4[k] = np.asarray([z, z, q, -q])
            H4[k] = np.asarray([Bext[a], Bext[a], Bq[i], Bq[i]])
            k += 1
    V4diag = fast.eval_many(P4, H4, LAMBDA3).reshape(5, 6)
    tad = -0.5 * float(np.sum(V4diag * Sq[None, :]))

    Vplus, Vminus = eval_requests([
        ([z, q, -q], [Bext, Bq, Bq]),
        ([z, -q, q], [Bext, Bq, Bq]),
    ], LAMBDA3)
    bubble = float(np.einsum("aij,i,aij,j->", Vplus, Sq, Vminus, Gq, optimize=True))

    Vg = np.asarray([ghost_matrix(z, h, q) for h in Bext])
    ghost = (-2.0 * ghost_S_q_scalar() * ghost_G_scalar(q)
             * float(np.einsum("aij,aji->", Vg, Vg, optimize=True)))
    return {"T4_GRAV": tad, "T33_GRAV": bubble, "T33_GHOST": ghost}


def gauss_interval(N, a, b):
    z, w = np.polynomial.legendre.leggauss(int(N))
    x = 0.5 * (b - a) * z + 0.5 * (a + b)
    ww = 0.5 * (b - a) * w
    return x, ww


def integrate_three(pmag, N):
    TG, TL = build_projectors()
    want_lambda = abs(float(pmag)) < 1e-16
    xs, wx = gauss_interval(N, 0.0, 1.0)
    ys, wy = gauss_interval(N, 0.0, 1.0)
    phis, wp = gauss_interval(N, 0.0, 2.0 * PI)
    keys = ["T5_GRAV", "B43_GRAV", "T333_GRAV", "T333_GHOST"]
    total_g = {k: 0.0 for k in keys}
    total_l = {k: 0.0 for k in keys}
    points = 0
    for x, ax in zip(xs, wx):
        for y, ay in zip(ys, wy):
            qplane = math.sqrt(float(x) * (1.0 - float(y)))
            qorth = math.sqrt(float(x) * float(y))
            for phi, ap in zip(phis, wp):
                q = np.array([qplane * math.cos(phi), qplane * math.sin(phi), qorth, 0.0])
                g, l = three_point_projected(float(pmag), q, TG, TL if want_lambda else None)
                weight = float(ax * ay * ap) * float(x) / (32.0 * PI ** 3)
                for k in keys:
                    total_g[k] += weight * g[k]
                    if want_lambda:
                        total_l[k] += weight * l[k]
                points += 1
    flow_g = float(sum(total_g.values()))
    flow_l = float(sum(total_l.values())) if want_lambda else None
    return {
        "mode": "three",
        "p": float(pmag),
        "p2": float(pmag) ** 2,
        "N": int(N),
        "quadrature_points": points,
        "measure": "x/(32*pi^3) dx dy dphi",
        "source_symmetrisation": "Sym3=(1/6)sum_S3; exact integrated reduction to one canonical labelled routing",
        "topology_G": total_g,
        "Flow_G": flow_g,
        "topology_Lambda": total_l if want_lambda else None,
        "Flow_Lambda": flow_l,
        "projector_norm2": {"G": float(np.sum(TG * TG)), "Lambda": float(np.sum(TL * TL))},
        "C3_enabled": False,
    }


def integrate_two(N):
    xs, wx = gauss_interval(N, 0.0, 1.0)
    ths, wt = gauss_interval(N, 0.0, PI)
    total = {"T4_GRAV": 0.0, "T33_GRAV": 0.0, "T33_GHOST": 0.0}
    points = 0
    for x, ax in zip(xs, wx):
        r = math.sqrt(float(x))
        for th, at in zip(ths, wt):
            q = np.array([r * math.cos(th), r * math.sin(th), 0.0, 0.0])
            vals = two_point_projected(q)
            weight = float(ax * at) * float(x) * (math.sin(th) ** 2) / (8.0 * PI ** 3)
            for k in total:
                total[k] += weight * vals[k]
            points += 1
    flow = float(sum(total.values()))
    beta_mu = -2.0 * MU + (32.0 * PI / 5.0) * flow
    return {
        "mode": "two",
        "N": int(N),
        "quadrature_points": points,
        "measure": "x*sin(theta)^2/(8*pi^3) dx dtheta",
        "topology_TT": total,
        "Flow_TT2_0": flow,
        "beta_mu": beta_mu,
        "C3_enabled": False,
    }


def single_fast_topologies(ps, hs, q):
    q = np.asarray(q, float)
    Bq = analytic_landau_basis(q)
    Sq = grav_S_q_diag()
    V5 = vertex_tensor([ps[0], ps[1], ps[2], q, -q],
                       [[hs[0]], [hs[1]], [hs[2]], Bq, Bq], LAMBDA3)[0, 0, 0]
    t5 = -0.5 * float(np.sum(np.diag(V5) * Sq))

    ell = q + ps[0] + ps[1]
    Bl = analytic_landau_basis(ell)
    Gl = grav_G_diag(ell)
    V4 = vertex_tensor([ps[0], ps[1], q, -ell], [[hs[0]], [hs[1]], Bq, Bl], LAMBDA3)[0, 0]
    V3b = vertex_tensor([ps[2], -q, ell], [[hs[2]], Bq, Bl], LAMBDA3)[0]
    bub = 3.0 * float(np.einsum("ij,i,ij,j->", V4, Sq, V3b, Gl, optimize=True))

    e23, e31 = q - ps[1], q + ps[0]
    B23, B31 = analytic_landau_basis(e23), analytic_landau_basis(e31)
    V1 = vertex_tensor([ps[0], q, -e31], [[hs[0]], Bq, B31], LAMBDA3)[0]
    V2 = vertex_tensor([ps[1], -q, e23], [[hs[1]], Bq, B23], LAMBDA3)[0]
    V3 = vertex_tensor([ps[2], -e23, e31], [[hs[2]], B23, B31], LAMBDA3)[0]
    tri = -3.0 * float(np.einsum("ij,i,ik,k,kj,j->", V1, Sq, V2, grav_G_diag(e23), V3, grav_G_diag(e31), optimize=True))

    A = ghost_matrix(ps[0], hs[0], q)
    B = ghost_matrix(ps[1], hs[1], e23)
    C = ghost_matrix(ps[2], hs[2], e31)
    gh = (6.0 * ghost_S_q_scalar() * ghost_G_scalar(e23) * ghost_G_scalar(e31)
          * float(np.trace(A @ B @ C)))
    return {"T5_GRAV": t5, "B43_GRAV": bub, "T333_GRAV": tri, "T333_GHOST": gh}


def selftest():
    # Exact JIT/source scalar vertex equivalence at n=2..5.
    tests = []
    p2 = [np.array([0.37, -0.22, 0.19, 0.41]), np.array([-0.37, 0.22, -0.19, -0.41])]
    tests.append((p2, [base.dense_tt(p2[0], 0), base.dense_tt(p2[1], 1)], -0.05))
    tests.append((UNIT_PS, [base.dense_tt(p, i) for i, p in enumerate(UNIT_PS)], -0.7))
    p4 = [np.array([1., 0., 0., 0.]), np.array([0., 1., 0., 0.]), np.array([0., 0., 1., 0.]), np.array([-1., -1., -1., 0.])]
    tests.append((p4, [base.dense_tt(p, i) for i, p in enumerate(p4)], -0.7))
    p5 = [np.array([1., 0., 0., 0.]), np.array([0., 1., 0., 0.]), np.array([0., 0., 1., 0.]), np.array([0., 0., 0., 1.]), np.array([-1., -1., -1., -1.])]
    tests.append((p5, [base.dense_tt(p, i) for i, p in enumerate(p5)], -0.7))
    vertex_records = []
    for ps, hs, lam in tests:
        ref = seed.eh_vertex_fourier(ps, hs, lam)
        got = float(fast.eh_vertex_fourier(np.asarray(ps), np.asarray(hs), lam))
        err = abs(got - ref)
        vertex_records.append({"n": len(ps), "reference": ref, "jit": got, "abs_error": err, "pass": err <= 2e-11 * (1 + abs(ref))})

    # Analytic six-dimensional basis and diagonal Hessian against source engine.
    hess_records = []
    for q in [np.array([0.23, -0.31, 0.17, 0.29]), np.array([0.41, 0.12, -0.27, 0.19])]:
        B = analytic_landau_basis(q)
        H = np.empty((6, 6))
        for i in range(6):
            for j in range(6):
                H[i, j] = seed.eh_vertex_fourier([q, -q], [B[i], B[j]], LAMBDA2)
        q2 = float(np.dot(q, q))
        target = K_EH * (q2 + MU) * np.diag([1., 1., 1., 1., 1., -0.5])
        err = float(np.max(np.abs(H - target)))
        gram = np.einsum("amn,bmn->ab", B, B)
        hess_records.append({"q": q.tolist(), "max_hessian_error": err, "gram_error": float(np.max(np.abs(gram - np.eye(6)))), "pass": err <= 2e-10})

    # Fast formulas against the already-terminal fixed-q contraction engine.
    ps, hs = fig.sym_external()
    fixed = []
    for q in fig.q_controls():
        f = single_fast_topologies(ps, hs, q)
        refs = {
            "T5_GRAV": fig.t5_value(ps, hs, q)[0],
            "B43_GRAV": fig.bubble_value(ps, hs, q)[0],
            "T333_GRAV": fig.triangle_value(ps, hs, q)[0],
            "T333_GHOST": fig.ghost_value(ps, hs, q)[0],
        }
        rec = {}
        for k in refs:
            err = abs(f[k] - refs[k])
            rec[k] = {"reference": refs[k], "fast": f[k], "abs_error": err,
                      "pass": err <= SELF_TOL * (1.0 + abs(refs[k]))}
        fixed.append({"q": q.tolist(), "topologies": rec, "pass": all(x["pass"] for x in rec.values())})

    TG, TL = build_projectors()
    projector = {
        "Ng_inv": float(np.sum(TG * TG)),
        "Nlambda_inv": float(np.sum(TL * TL)),
        "Ng_match": abs(float(np.sum(TG * TG)) - 0.00052874519051635) <= 2e-14,
        "Nlambda_match": abs(float(np.sum(TL * TL)) - 0.0026385724906858796) <= 2e-14,
    }
    passed = (all(x["pass"] for x in vertex_records)
              and all(x["pass"] for x in hess_records)
              and all(x["pass"] for x in fixed)
              and projector["Ng_match"] and projector["Nlambda_match"])
    return {
        "classification": "PASS_SF055A3_BASELINE_QUADRATURE_IMPLEMENTATION_SELFTEST_SCOPED" if passed else "FAIL_SF055A3_BASELINE_QUADRATURE_IMPLEMENTATION_SELFTEST_SCOPED",
        "vertex_equivalence": vertex_records,
        "landau_hessian": hess_records,
        "fixed_q_topologies": fixed,
        "projector": projector,
        "scientific_object_unchanged": True,
        "pass": passed,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["selftest", "three", "two"], required=True)
    ap.add_argument("--N", type=int)
    ap.add_argument("--p", type=float, default=0.0)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    if args.mode == "selftest":
        result = selftest()
    elif args.mode == "three":
        if args.N is None:
            raise SystemExit("--N required")
        result = integrate_three(args.p, args.N)
    else:
        if args.N is None:
            raise SystemExit("--N required")
        result = integrate_two(args.N)
    path = ROOT / args.out
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(result, indent=2, sort_keys=True, default=jdefault) + "\n"
    path.write_text(text)
    print(text, end="")
    if args.mode == "selftest" and not result["pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
