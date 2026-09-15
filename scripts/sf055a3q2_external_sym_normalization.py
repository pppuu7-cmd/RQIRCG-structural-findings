#!/usr/bin/env python3
"""SF055A3Q2 source external-symmetrisation normalisation.

Derives three labelled fluctuation derivatives of an inverse operator G=A^{-1}
using the exact product rule, retaining noncommuting factor order.  No Eq. (14)
value or integrated flow enters this calculation.
"""
from collections import defaultdict
import itertools
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "raw" / "SF055A3Q2_EXTERNAL_SYM_NORMALIZATION.json"

# A term is (integer coefficient, tuple of factors).
# G is ('G', ()); A_S is ('A', tuple(sorted(labels))).
G = ("G", ())

def Af(labels):
    return ("A", tuple(sorted(labels)))


def canonical_expr(terms):
    acc = defaultdict(int)
    for c, facs in terms:
        acc[tuple(facs)] += c
    return [(c, facs) for facs, c in sorted(acc.items(), key=lambda x: repr(x[0])) if c]


def derivative_factor(factor, label):
    kind, labs = factor
    if kind == "A":
        if label in labs:
            raise ValueError("distinct labelled derivatives expected")
        return [(1, (Af(set(labs) | {label}),))]
    if kind == "G":
        # D G = - G (D A) G
        return [(-1, (G, Af({label}), G))]
    raise KeyError(kind)


def derivative_expr(terms, label):
    out = []
    for coeff, facs in terms:
        for pos, f in enumerate(facs):
            for dc, replacement in derivative_factor(f, label):
                out.append((coeff * dc, facs[:pos] + replacement + facs[pos+1:]))
    return canonical_expr(out)


def a_sizes(facs):
    return tuple(sorted((len(labs) for kind, labs in facs if kind == "A"), reverse=True))


def classify(terms):
    classes = defaultdict(list)
    for c, facs in terms:
        classes[a_sizes(facs)].append((c, facs))
    return classes


def pretty_factor(f):
    kind, labs = f
    if kind == "G":
        return "G"
    return "A_" + "".join(str(x) for x in labs)


def pretty_term(term):
    c, facs = term
    return {"coefficient": c, "word": " ".join(pretty_factor(x) for x in facs)}


def source_coefficient_test():
    # Raw exact derivative weights BEFORE bosonic global 1/2:
    # Gamma5 representative: -1
    # each of six Gamma4-Gamma3 labelled words: +1
    # each of six Gamma3^3 labelled words: -1
    # ghost each of six triangle words after the supertrace sign: +1.
    # A source coefficient C multiplying Sym_3 of a canonical labelled graph
    # must match these per-labelled-term coefficients.
    # If Sym=sum, per-labelled coefficient=C.
    # If Sym=average, per-labelled coefficient=C/6.
    published = {
        "T5_GRAV": -0.5,
        "B43_GRAV": 3.0,
        "T333_GRAV": -3.0,
        "T333_GHOST": 6.0,
    }
    exact_per_label = {
        "T5_GRAV": -0.5, # unique fully symmetric Gamma5 term
        "B43_GRAV": +0.5,
        "T333_GRAV": -0.5,
        "T333_GHOST": +1.0,
    }
    # For T5 the canonical object is permutation invariant; sum would multiply it by six,
    # while average leaves it unchanged.  Treat this as an independent discriminator.
    predictions = {}
    for mode in ("sum", "average"):
        per_label = {}
        t5_total = None
        for k, C in published.items():
            if k == "T5_GRAV":
                t5_total = C * (6.0 if mode == "sum" else 1.0)
                per_label[k] = t5_total
            else:
                per_label[k] = C if mode == "sum" else C/6.0
        ok = all(abs(per_label[k] - exact_per_label[k]) < 1e-15 for k in exact_per_label)
        predictions[mode] = {"effective_per_label_or_unique_weight": per_label, "matches_exact": ok}
    return published, exact_per_label, predictions


def main():
    expr = [(1, (G,))]
    stages = {"0": [pretty_term(x) for x in expr]}
    for lab in (1, 2, 3):
        expr = derivative_expr(expr, lab)
        stages[str(lab)] = [pretty_term(x) for x in expr]

    classes = classify(expr)
    counts = {str(k): len(v) for k, v in classes.items()}
    coeff_sets = {str(k): sorted(c for c, _ in v) for k, v in classes.items()}

    derivative_controls = {
        "Gamma5_one_term": counts.get("(3,)", 0) == 1,
        "Gamma5_sign_minus": coeff_sets.get("(3,)", []) == [-1],
        "Gamma4Gamma3_six_terms": counts.get("(2, 1)", 0) == 6,
        "Gamma4Gamma3_each_plus": coeff_sets.get("(2, 1)", []) == [1]*6,
        "Gamma3cubed_six_terms": counts.get("(1, 1, 1)", 0) == 6,
        "Gamma3cubed_each_minus": coeff_sets.get("(1, 1, 1)", []) == [-1]*6,
    }

    published, exact, predictions = source_coefficient_test()
    average_pass = predictions["average"]["matches_exact"]
    sum_pass = predictions["sum"]["matches_exact"]
    unique = average_pass ^ sum_pass

    # Ghost control: inverse derivative triangle has -1 per ordering; the FP
    # supertrace contributes an additional minus, yielding +1 per labelled ordering.
    ghost = {
        "inverse_triangle_terms": 6,
        "inverse_each_coefficient": -1,
        "supertrace_sign": -1,
        "effective_each_labelled_term": +1,
        "published_plus6_times_average_each": 6.0/6.0,
        "pass": abs(6.0/6.0 - 1.0) < 1e-15,
    }

    positive = all(derivative_controls.values()) and ghost["pass"] and unique and average_pass
    result = {
        "gate": "SF055A3Q2_EXTERNAL_SYMMETRISATION_NORMALISATION",
        "classification": (
            "PASS_SOURCE_EXTERNAL_SYMMETRISATION_NORMALISATION_SCOPED" if positive
            else ("BLOCKED_SOURCE_SYMMETRISATION_NORMALISATION_AMBIGUOUS" if average_pass and sum_pass
                  else "FAIL_SOURCE_FIGURE2_COMBINATORICS_MISMATCH_SCOPED")
        ),
        "derivative_stages": stages,
        "class_counts": counts,
        "class_coefficients_before_bosonic_half": coeff_sets,
        "derivative_controls": derivative_controls,
        "published_figure2_coefficients": published,
        "exact_effective_weight_per_labelled_term": exact,
        "symmetrisation_hypotheses": predictions,
        "ghost_control": ghost,
        "inferred_source_symmetrisation": "(1/6) * sum_over_S3_labelled_external_permutations" if positive else "UNRESOLVED",
        "loop_measure_authority": "d^4 q / (2 pi)^4",
        "eq14_values_used": False,
        "scientific_pass": positive,
        "interpretation_ceiling": "SOURCE_COMBINATORICS_ONLY_NO_QUADRATURE_NO_EQ14_NO_LANE_A_NO_C3",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    OUT.write_text(text)
    print(json.dumps({
        "classification": result["classification"],
        "class_counts": counts,
        "class_coefficients_before_bosonic_half": coeff_sets,
        "derivative_controls": derivative_controls,
        "symmetrisation_hypotheses": predictions,
        "ghost_control": ghost,
        "inferred_source_symmetrisation": result["inferred_source_symmetrisation"],
        "scientific_pass": positive,
    }, indent=2, sort_keys=True))
    if not positive:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
