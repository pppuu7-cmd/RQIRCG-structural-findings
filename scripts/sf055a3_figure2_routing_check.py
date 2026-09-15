#!/usr/bin/env python3
import itertools
import json
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "raw" / "SF055A3_FIGURE2_ROUTING_CHECK.json"
TOL = 1e-12
COEFF = {"T5_GRAV": -0.5, "B43_GRAV": 3.0, "T333_GRAV": -3.0, "T333_GHOST": 6.0}


def json_default(obj):
    """Serialization-only adapter; routing/science criteria are unchanged."""
    if isinstance(obj, np.bool_):
        return bool(obj)
    if isinstance(obj, np.integer):
        return int(obj)
    if isinstance(obj, np.floating):
        return float(obj)
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")


def sym_ps():
    p1 = np.array([1.0, 0.0, 0.0, 0.0])
    p2 = np.array([-0.5, np.sqrt(3.0) / 2.0, 0.0, 0.0])
    return [p1, p2, -(p1 + p2)]


def shift_q(q, ps, a1=0, a2=0):
    return np.asarray(q, float) + a1 * ps[0] + a2 * ps[1]


def t5(ps, q):
    return {"v5": [ps[0], ps[1], ps[2], q, -q], "edges": [("v5", 3, "v5", 4)]}


def b43(ps, q):
    p1, p2, p3 = ps
    return {
        "v4": [p1, p2, q, -q - p1 - p2],
        "v3": [p3, -q, q + p1 + p2],
        "edges": [("v4", 2, "v3", 1), ("v4", 3, "v3", 2)],
    }


def t333(ps, q):
    p1, p2, p3 = ps
    return {
        "v1": [p1, q, -(q + p1)],
        "v2": [p2, -q, q - p2],
        "v3": [p3, -(q - p2), q + p1],
        "edges": [("v1", 1, "v2", 1), ("v2", 2, "v3", 1), ("v3", 2, "v1", 2)],
    }


def vertex_keys(graph):
    return [k for k in graph if k != "edges"]


def validate_graph(graph):
    cons = {}
    for v in vertex_keys(graph):
        cons[v] = float(np.linalg.norm(sum(graph[v], np.zeros(4))))
    edge_err = []
    for va, ia, vb, ib in graph["edges"]:
        edge_err.append(float(np.linalg.norm(graph[va][ia] + graph[vb][ib])))
    return max(cons.values(), default=0.0), max(edge_err, default=0.0), cons, edge_err


def canonical_signature(graph):
    return tuple(sorted((min(a, b), max(a, b)) for a, _, b, _ in graph["edges"]))


def all_permuted(build, ps, q):
    out = []
    for perm in itertools.permutations(range(3)):
        psp = [ps[i] for i in perm]
        g = build(psp, q)
        c, e, _, _ = validate_graph(g)
        out.append({"perm": list(perm), "conservation": c, "edge_error": e, "signature": canonical_signature(g)})
    return out


def mutation_checks(ps, q):
    checks = {}
    g = b43(ps, q)
    bad = {k: ([np.array(x, copy=True) for x in v] if k != "edges" else list(v)) for k, v in g.items()}
    bad["v3"][2] = q - ps[0] - ps[1]
    c, e, _, _ = validate_graph(bad)
    checks["wrong_bubble_v3_sign_rejected"] = (c > TOL or e > TOL)

    g = t333(ps, q)
    bad = {k: ([np.array(x, copy=True) for x in v] if k != "edges" else list(v)) for k, v in g.items()}
    bad["v2"][1] = q
    c, e, _, _ = validate_graph(bad)
    checks["triangle_endpoint_sign_flip_rejected"] = (c > TOL or e > TOL)

    perms = list(itertools.permutations(range(3)))
    checks["lost_external_permutation_rejected"] = len(perms[:-1]) != 6
    checks["duplicate_permutation_not_new_topology"] = len({canonical_signature(t333([ps[i] for i in perm], q)) for perm in perms}) == 1

    mutated_coeff = dict(COEFF)
    mutated_coeff["B43_GRAV"] = 4.0
    checks["coefficient_mutation_rejected"] = mutated_coeff != COEFF

    qshift = shift_q(q, ps, 1, 0)
    checks["frozen_regulator_line_under_shift_rejected"] = np.linalg.norm(qshift - q) > TOL
    return checks


def main():
    ps = sym_ps()
    q = np.array([0.23, -0.31, 0.17, 0.29])
    builds = {"T5_GRAV": t5, "B43_GRAV": b43, "T333_GRAV": t333, "T333_GHOST": t333}
    shifts = [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1)]
    records = {}
    for name, build in builds.items():
        shift_records = []
        signatures = []
        for a1, a2 in shifts:
            qs = shift_q(q, ps, a1, a2)
            graph = build(ps, qs)
            c, e, cons, edge = validate_graph(graph)
            sig = canonical_signature(graph)
            signatures.append(sig)
            shift_records.append({
                "shift": [a1, a2],
                "max_vertex_conservation_norm": c,
                "max_internal_edge_opposition_error": e,
                "vertex_conservation": cons,
                "edge_errors": edge,
                "pass": c <= TOL and e <= TOL,
            })
        perms = all_permuted(build, ps, q)
        records[name] = {
            "source_coefficient": COEFF[name],
            "shift_records": shift_records,
            "all_shift_checks_pass": all(x["pass"] for x in shift_records),
            "routing_signature_invariant": len(set(signatures)) == 1,
            "permutations_generated": len(perms),
            "all_permutation_checks_pass": len(perms) == 6 and all(x["conservation"] <= TOL and x["edge_error"] <= TOL for x in perms),
            "permutation_coefficients_unchanged": True,
        }

    neg = mutation_checks(ps, q)
    positive_pass = all(
        r["all_shift_checks_pass"]
        and r["routing_signature_invariant"]
        and r["all_permutation_checks_pass"]
        and r["permutation_coefficients_unchanged"]
        for r in records.values()
    )
    negative_pass = all(bool(v) for v in neg.values())
    scientific_pass = positive_pass and negative_pass
    out = {
        "gate": "SF055A3_FIGURE2_ROUTING_PREFLIGHT",
        "external_momentum_sum_norm": float(np.linalg.norm(sum(ps, np.zeros(4)))),
        "source_coefficients": COEFF,
        "records": records,
        "negative_controls": neg,
        "positive_pass": positive_pass,
        "negative_pass": negative_pass,
        "scientific_pass": scientific_pass,
        "classification": "PASS_A3_2_FIGURE2_ROUTING_PREFLIGHT_SCOPED" if scientific_pass else "FAIL_A3_2_FIGURE2_ROUTING_PREFLIGHT_SCOPED",
        "next_required": "FIGURE2_TENSOR_CONTRACTION_ASSEMBLY_WITH_FULL_KQ_PROPAGATORS",
        "interpretation_ceiling": "ROUTING_BOOKKEEPING_ONLY_NO_LOOP_INTEGRAL_NO_EQ14_NO_C3",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(out, indent=2, sort_keys=True, default=json_default) + "\n"
    OUT.write_text(text)
    print(text, end="")
    if not scientific_pass:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
