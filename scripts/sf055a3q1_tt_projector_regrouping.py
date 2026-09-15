#!/usr/bin/env python3
"""SF055A3Q1 exact complete-TT projector regrouping controls.

No physics object is changed.  The identity tested is
  sum_abc T_abc F(E1_a,E2_b,E3_c)
= sum_ab F(E1_a,E2_b,sum_c T_abc E3_c)
for the already frozen source projectors T_G and T_Lambda.
"""
import itertools
import json
from pathlib import Path

import numpy as np

import sf055a3_figure2_contraction_assembly as fig
import sf055a3_tt_projector_normalization as norm

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "raw" / "SF055A3Q1_TT_PROJECTOR_REGROUPING.json"
TOL = 1e-10
ZERO = 1e-15


def jdefault(x):
    if isinstance(x, np.bool_): return bool(x)
    if isinstance(x, np.integer): return int(x)
    if isinstance(x, np.floating): return float(x)
    raise TypeError(type(x).__name__)


def topo_value(kind, ps, hs, q):
    if kind == "T5_GRAV":
        return fig.t5_value(ps, hs, q)[0]
    if kind == "B43_GRAV":
        return fig.bubble_value(ps, hs, q)[0]
    if kind == "T333_GRAV":
        return fig.triangle_value(ps, hs, q)[0]
    if kind == "T333_GHOST":
        return fig.ghost_value(ps, hs, q)[0]
    raise KeyError(kind)


def labelled_sym_sum(kind, ps, hs, q):
    # Deliberately unnormalised.  This gate proves projector regrouping only;
    # it does not choose the source convention for a possible overall sym factor.
    return sum(
        topo_value(kind, [ps[i] for i in perm], [hs[i] for i in perm], q)
        for perm in itertools.permutations(range(3))
    )


def eval_kernel(kind, ps, hs, q, sym=False):
    return labelled_sym_sum(kind, ps, hs, q) if sym else topo_value(kind, ps, hs, q)


def brute_contract(kind, T, ps, Bs, q, sym=False):
    total = 0.0
    calls = 0
    skipped_norm2 = 0.0
    for a, b, c in itertools.product(range(5), repeat=3):
        w = float(T[a, b, c])
        if abs(w) <= ZERO:
            skipped_norm2 += w*w
            continue
        total += w * eval_kernel(kind, ps, [Bs[0][a], Bs[1][b], Bs[2][c]], q, sym=sym)
        calls += 1
    return total, calls, skipped_norm2


def grouped_contract(kind, T, ps, Bs, q, sym=False, drop_pair=None, scale=1.0):
    total = 0.0
    calls = 0
    used_pairs = []
    for a, b in itertools.product(range(5), repeat=2):
        if drop_pair is not None and (a, b) == tuple(drop_pair):
            continue
        coeff = np.asarray(T[a, b, :], float) * scale
        if np.linalg.norm(coeff) <= ZERO:
            continue
        H3 = sum((coeff[c] * Bs[2][c] for c in range(5)), np.zeros((4, 4)))
        total += eval_kernel(kind, ps, [Bs[0][a], Bs[1][b], H3], q, sym=sym)
        calls += 1
        used_pairs.append([a, b])
    return total, calls, used_pairs


def closeness(a, b):
    err = abs(a-b)
    lim = TOL * (1.0 + abs(a))
    return {"brute": a, "grouped": b, "abs_error": err, "limit": lim, "pass": err <= lim}


def trilinearity(kind, ps, Bs, q, slot):
    # Fixed deterministic source-TT vectors.  Only the external tensor is varied.
    i0 = [0, 1, 2]
    i1 = [3, 4, 0]
    alpha, beta = 0.37, -0.61
    h0 = [Bs[j][i0[j]] for j in range(3)]
    h1 = [Bs[j][i1[j]] for j in range(3)]
    mix = list(h0)
    mix[slot] = alpha*h0[slot] + beta*h1[slot]
    a = topo_value(kind, ps, mix, q)
    left0 = list(h0)
    left1 = list(h0)
    left1[slot] = h1[slot]
    b = alpha*topo_value(kind, ps, left0, q) + beta*topo_value(kind, ps, left1, q)
    err = abs(a-b)
    lim = TOL*(1.0+abs(b))
    return {"lhs": a, "rhs": b, "abs_error": err, "limit": lim, "pass": err <= lim}


def main():
    ps = norm.symmetric_ps_in_plane(0, 1)
    Bs = norm.bases_for(ps)
    zps = [np.zeros(4) for _ in range(3)]
    TG = norm.tensor3(ps, Bs, 0.0)
    TL = norm.tensor3(zps, Bs, 1.0)
    projectors = {"G": TG, "Lambda": TL}
    qvals = fig.q_controls()
    kinds = list(fig.COEFF)

    projector_meta = {}
    for name, T in projectors.items():
        pair_count = sum(np.linalg.norm(T[a,b,:]) > ZERO for a,b in itertools.product(range(5), repeat=2))
        nz = int(np.sum(np.abs(T) > ZERO))
        skipped = float(np.sum(T[np.abs(T) <= ZERO]**2))
        projector_meta[name] = {
            "nonzero_components": nz,
            "nonzero_grouped_pairs": int(pair_count),
            "grouped_evaluations_max": int(pair_count),
            "skipped_norm2": skipped,
            "total_norm2": float(np.sum(T*T)),
            "skipped_norm_fraction": skipped/max(float(np.sum(T*T)), 1e-300),
        }

    tri = {}
    for qi, q in enumerate(qvals):
        for kind in kinds:
            key = f"q{qi+1}:{kind}"
            tri[key] = [trilinearity(kind, ps, Bs, q, s) for s in range(3)]

    comparisons = {}
    for pname, T in projectors.items():
        for qi, q in enumerate(qvals):
            for kind in kinds:
                bval, bcalls, skipped = brute_contract(kind, T, ps, Bs, q, sym=False)
                gval, gcalls, pairs = grouped_contract(kind, T, ps, Bs, q, sym=False)
                rec = closeness(bval, gval)
                rec.update({"brute_calls": bcalls, "grouped_calls": gcalls, "grouped_pairs": pairs, "skipped_norm2": skipped})
                comparisons[f"{pname}:q{qi+1}:{kind}"] = rec

    # One complete six-labelled-permutation control, as frozen.  Keep the raw
    # symmetrisation unnormalised so this gate cannot decide an overall source factor.
    sym_b, sym_bc, _ = brute_contract("B43_GRAV", TG, ps, Bs, qvals[0], sym=True)
    sym_g, sym_gc, sym_pairs = grouped_contract("B43_GRAV", TG, ps, Bs, qvals[0], sym=True)
    sym_control = closeness(sym_b, sym_g)
    sym_control.update({"brute_calls": sym_bc*6, "grouped_calls": sym_gc*6,
                        "grouped_pairs": sym_pairs, "symmetrisation": "unnormalised_sum_over_6_labelled_permutations"})

    # Counterexample-first controls. Pick the largest grouped row in T_G so
    # dropping it cannot be hidden by an exactly-zero row.
    row_norms = {(a,b): float(np.linalg.norm(TG[a,b,:])) for a,b in itertools.product(range(5), repeat=2)}
    drop_pair = max(row_norms, key=row_norms.get)
    ref_g, _, _ = grouped_contract("T333_GRAV", TG, ps, Bs, qvals[0])
    drop_g, _, _ = grouped_contract("T333_GRAV", TG, ps, Bs, qvals[0], drop_pair=drop_pair)
    scale_g, _, _ = grouped_contract("T333_GRAV", TG, ps, Bs, qvals[0], scale=1.137)
    lam_ref, _, _ = grouped_contract("T333_GRAV", TL, ps, Bs, qvals[0])
    wrong_lam, _, _ = grouped_contract("T333_GRAV", TG, ps, Bs, qvals[0])
    single = float(TG[0,1,2]) * topo_value("T333_GRAV", ps, [Bs[0][0],Bs[1][1],Bs[2][2]], qvals[0])
    negative = {
        "dropped_nonzero_group_rejected": abs(drop_g-ref_g) > TOL*(1+abs(ref_g)),
        "fitted_rescale_rejected": abs(scale_g-ref_g) > TOL*(1+abs(ref_g)),
        "G_weights_substituted_for_Lambda_rejected": abs(wrong_lam-lam_ref) > TOL*(1+abs(lam_ref)),
        "single_polarization_not_complete_projection": abs(single-ref_g) > TOL*(1+abs(ref_g)),
        "dropped_pair": list(drop_pair),
    }

    tri_pass = all(x["pass"] for vv in tri.values() for x in vv)
    cmp_pass = all(x["pass"] for x in comparisons.values())
    meta_pass = all(x["skipped_norm_fraction"] <= 1e-24 and x["grouped_evaluations_max"] <= 25 for x in projector_meta.values())
    neg_pass = all(v for k,v in negative.items() if k != "dropped_pair")
    scientific_pass = tri_pass and cmp_pass and sym_control["pass"] and meta_pass and neg_pass

    result = {
        "gate": "SF055A3Q1_TT_PROJECTOR_RANK1_ACCELERATION",
        "classification": "PASS_SF055A3_EXACT_TT_PROJECTOR_REGROUPING_ACCELERATION_SCOPED" if scientific_pass else "FAIL_SF055A3_TT_PROJECTOR_REGROUPING_EQUIVALENCE_SCOPED",
        "projector_meta": projector_meta,
        "trilinearity": tri,
        "canonical_comparisons": comparisons,
        "symmetrized_control": sym_control,
        "negative_controls": negative,
        "trilinearity_pass": tri_pass,
        "comparison_pass": cmp_pass,
        "metadata_pass": meta_pass,
        "negative_pass": neg_pass,
        "scientific_pass": scientific_pass,
        "next_if_pass": "USE_EXACT_GROUPED_PROJECTORS_IN_FROZEN_N_8_12_16_24_QUADRATURE",
        "interpretation_ceiling": "IMPLEMENTATION_EQUIVALENCE_ONLY_NO_QUADRATURE_NO_EQ14_NO_LANE_A_NO_C3",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(result, indent=2, sort_keys=True, default=jdefault) + "\n"
    OUT.write_text(text)
    print(json.dumps({
        "classification": result["classification"],
        "projector_meta": projector_meta,
        "trilinearity_pass": tri_pass,
        "comparison_pass": cmp_pass,
        "symmetrized_control": sym_control,
        "negative_controls": negative,
        "scientific_pass": scientific_pass,
    }, indent=2, sort_keys=True, default=jdefault))
    if not scientific_pass:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
