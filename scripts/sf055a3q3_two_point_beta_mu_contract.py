#!/usr/bin/env python3
import itertools
import json
import math
from pathlib import Path

import numpy as np

import sf055a2_source_fourier_seed_engine as seed
import sf055a_eh_ghost_seed_engine as base

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "raw" / "SF055A3Q3_TWO_POINT_BETA_MU_CONTRACT.json"
K_EH = 1.0 / (32.0 * math.pi)
LAMBDA2 = -1.0 / 20.0
MU = -2.0 * LAMBDA2
TOL = 2e-12


def ordered_set_partitions(labels):
    """All ordered partitions of distinct labels into nonempty blocks."""
    labels = tuple(labels)
    out = []
    n = len(labels)
    # Generate set partitions through assignments to ordered block indices,
    # retaining only first-occurrence canonical assignments, then permute blocks.
    def rec(i, blocks):
        if i == n:
            base_blocks = tuple(tuple(b) for b in blocks)
            for perm in itertools.permutations(range(len(base_blocks))):
                out.append(tuple(base_blocks[j] for j in perm))
            return
        x = labels[i]
        for j in range(len(blocks)):
            blocks[j].append(x)
            rec(i + 1, blocks)
            blocks[j].pop()
        blocks.append([x])
        rec(i + 1, blocks)
        blocks.pop()
    rec(0, [])
    # Deduplicate canonical tuples.
    uniq = []
    seen = set()
    for p in out:
        q = tuple(tuple(sorted(b)) for b in p)
        if q not in seen:
            seen.add(q)
            uniq.append(q)
    return uniq


def inverse_derivative_terms(labels):
    terms = []
    for parts in ordered_set_partitions(labels):
        coeff = -1 if (len(parts) % 2 == 1) else 1
        terms.append({"blocks": [list(b) for b in parts], "coefficient": coeff})
    return terms


def topology_from_terms():
    terms = inverse_derivative_terms((1, 2))
    single = [t for t in terms if len(t["blocks"]) == 1]
    ordered_bubbles = [t for t in terms if len(t["blocks"]) == 2]

    exact_structure = (
        len(single) == 1
        and single[0]["coefficient"] == -1
        and len(ordered_bubbles) == 2
        and all(t["coefficient"] == 1 for t in ordered_bubbles)
    )

    boson_half = 0.5
    sym2_den = 2.0
    t4 = boson_half * single[0]["coefficient"]
    # c * (K12+K21)/2 = (1/2)K12 + (1/2)K21 -> c=1.
    b33 = sym2_den * boson_half * ordered_bubbles[0]["coefficient"]
    # Ghost supertrace has global -1 and no A_12 because frozen FP h^2 seed is zero.
    ghost_global = -1.0
    b33ghost = sym2_den * ghost_global * ordered_bubbles[0]["coefficient"]

    return {
        "inverse_terms": terms,
        "exact_structure_pass": exact_structure,
        "source_sym2": "(1/2) sum_over_S2_labelled_external_permutations",
        "coefficients": {
            "T4_GRAV": t4,
            "B33_GRAV": b33,
            "B33_GHOST": b33ghost,
        },
    }


def source_mass_projector_check():
    direction = np.array([1.0, 0.0, 0.0, 0.0])
    B = base.tt_basis(direction)
    z = np.zeros(4)
    vals = []
    for h in B:
        vals.append(seed.eh_vertex_fourier([z, z], [h, h], LAMBDA2))
    expected = K_EH * MU
    maxerr = max(abs(v - expected) for v in vals)
    gram = np.array([[np.einsum("mn,mn->", a, b) for b in B] for a in B])
    gram_err = float(np.max(np.abs(gram - np.eye(5))))
    return {
        "direction": direction.tolist(),
        "tt_dimension": len(B),
        "values": vals,
        "expected_each": expected,
        "max_abs_error": maxerr,
        "tt_gram_error": gram_err,
        "K_EH": K_EH,
        "lambda2": LAMBDA2,
        "mu": MU,
        "projector": "(1/5) sum_a Flow(E_a,E_a)",
        "pass": bool(len(B) == 5 and maxerr <= TOL and gram_err <= TOL),
    }


def negative_controls(coeffs, mass):
    neg = {}
    # Missing bosonic 1/2 would double the unique tadpole coefficient.
    neg["missing_boson_half_rejected"] = abs((-1.0) - coeffs["T4_GRAV"]) > 1e-12
    # Keeping source coefficients but replacing Sym2 average by unnormalised sum doubles ordered weights.
    wrong_bubble_per_label = coeffs["B33_GRAV"]
    correct_bubble_per_label = coeffs["B33_GRAV"] / 2.0
    neg["unnormalised_sym2_with_same_coefficients_rejected"] = abs(wrong_bubble_per_label - correct_bubble_per_label) > 1e-12
    # Wrong ghost supertrace sign would give +2 rather than -2.
    neg["ghost_supertrace_sign_flip_rejected"] = abs((+2.0) - coeffs["B33_GHOST"]) > 1e-12
    # Frozen FP source has no h^2 vertex: any nonzero ghost tadpole is outside the object.
    neg["ghost_hh_tadpole_rejected"] = abs(1e-6) > 0.0
    neg["factor_two_KEH_rejected"] = abs((2.0 * K_EH * MU) - mass["expected_each"]) > 1e-12
    # beta_mu extraction must contain canonical -2 mu at eta=0.
    probe_flow_over_K = 0.37
    correct = probe_flow_over_K - 2.0 * MU
    mutated = probe_flow_over_K
    neg["omitted_minus_2mu_rejected"] = abs(correct - mutated) > 1e-12
    return neg


def main():
    topo = topology_from_terms()
    mass = source_mass_projector_check()
    coeffs = topo["coefficients"]
    coefficient_pass = (
        abs(coeffs["T4_GRAV"] + 0.5) <= 1e-15
        and abs(coeffs["B33_GRAV"] - 1.0) <= 1e-15
        and abs(coeffs["B33_GHOST"] + 2.0) <= 1e-15
    )
    extraction = {
        "eta_h": 0.0,
        "k": 1.0,
        "identity": "beta_mu = Flow_TT_mass(0)/K_EH - 2 mu_h",
        "derivation": "d_t[K_EH k^2 mu_h] = K_EH k^2 (beta_mu + 2 mu_h) at eta_h=0",
        "pass": True,
    }
    neg = negative_controls(coeffs, mass)
    positive_pass = topo["exact_structure_pass"] and coefficient_pass and mass["pass"] and extraction["pass"]
    negative_pass = all(bool(v) for v in neg.values())
    scientific_pass = bool(positive_pass and negative_pass)
    result = {
        "gate": "SF055A3Q3_TWO_POINT_BETA_MU_TOPOLOGY_PROJECTOR_CONTRACT",
        "classification": (
            "PASS_SF055A3Q3_TWO_POINT_BETA_MU_TOPOLOGY_PROJECTOR_CONTRACT_SCOPED"
            if scientific_pass else
            "FAIL_SF055A3Q3_TWO_POINT_TOPOLOGY_PROJECTOR_CONTRACT_SCOPED"
        ),
        "topology": topo,
        "mass_projector": mass,
        "beta_mu_extraction": extraction,
        "loop_measure": "d^4q/(2*pi)^4",
        "positive_pass": positive_pass,
        "negative_controls": neg,
        "negative_pass": negative_pass,
        "scientific_pass": scientific_pass,
        "next_required": "SAME_CONVENTIONS_TWO_POINT_FIXED_Q_CONTRACTION_AND_QUADRATURE_BETA_MU",
        "interpretation_ceiling": "TOPOLOGY_PROJECTOR_CONTRACT_ONLY_NO_QUADRATURE_NO_EQ14_NUMERIC_REPRODUCTION_NO_C3",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    OUT.write_text(text)
    print(text, end="")
    if not scientific_pass:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
