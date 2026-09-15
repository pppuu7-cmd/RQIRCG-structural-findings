#!/usr/bin/env python3
import copy
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "results" / "raw" / "SF055C_THREE_POINT_FLOW_TOPOLOGY_MANIFEST.json"
OUT = ROOT / "results" / "raw" / "SF055C_THREE_POINT_FLOW_TOPOLOGY_CHECK.json"

EXPECTED_IDS = ["T5_GRAV", "B43_GRAV", "T333_GRAV", "T333_GHOST"]
EXPECTED_COEFF = {
    "T5_GRAV": Fraction(-1, 2),
    "B43_GRAV": Fraction(3, 1),
    "T333_GRAV": Fraction(-3, 1),
    "T333_GHOST": Fraction(6, 1),
}
EXPECTED_VERTEX_ORDERS = {
    "T5_GRAV": [5],
    "B43_GRAV": [4, 3],
    "T333_GRAV": [3, 3, 3],
    "T333_GHOST": [3, 3, 3],
}
EXPECTED_SLOTS = {
    "T5_GRAV": [("v5", 5)],
    "B43_GRAV": [("v4", 4), ("v3", 3)],
    "T333_GRAV": [("v3a", 3), ("v3b", 3), ("v3c", 3)],
    "T333_GHOST": [],
}
COMMON = "g_C3_fluc"


def derived_source_coefficients():
    # Three fluctuation derivatives of the frozen Wetterich traces.
    return {
        "T5_GRAV": Fraction(1, 2) * Fraction(-1, 1),
        "B43_GRAV": Fraction(1, 2) * Fraction(6, 1),
        "T333_GRAV": Fraction(1, 2) * Fraction(-6, 1),
        "T333_GHOST": Fraction(-1, 1) * Fraction(-6, 1),
    }


def validate(m):
    errors = []
    if m.get("parent_gate") != "SF055_C3_PROJECTED_FRG_IMPLEMENTATION_CONTRACT":
        errors.append("parent_gate")
    if m.get("common_c3_coupling") != COMMON:
        errors.append("common_c3_coupling")
    if m.get("linear_c3_order") != 1:
        errors.append("linear_c3_order")
    if m.get("projection_stage") != "AFTER_UNPROJECTED_TT_FLOW_ASSEMBLED":
        errors.append("projection_stage")

    tops = m.get("topologies", [])
    ids = [t.get("id") for t in tops]
    if ids != EXPECTED_IDS:
        errors.append("topology_ids_or_order")
    if len(tops) != 4 or not all(t.get("baseline") is True for t in tops):
        errors.append("baseline_topology_count")
    if not all(t.get("external_symmetrized") is True for t in tops):
        errors.append("external_symmetrization")

    byid = {t.get("id"): t for t in tops}
    if len(byid) != len(tops):
        errors.append("duplicate_topology_id")

    for tid in EXPECTED_IDS:
        t = byid.get(tid)
        if t is None:
            continue
        try:
            coeff = Fraction(str(t.get("source_coefficient")))
        except Exception:
            errors.append(f"coefficient_parse:{tid}")
            continue
        if coeff != EXPECTED_COEFF[tid]:
            errors.append(f"source_coefficient:{tid}")
        if t.get("vertex_orders") != EXPECTED_VERTEX_ORDERS[tid]:
            errors.append(f"vertex_orders:{tid}")
        got_slots = [(x.get("slot"), x.get("vertex_order")) for x in t.get("c3_insertions", [])]
        if got_slots != EXPECTED_SLOTS[tid]:
            errors.append(f"c3_slots:{tid}")

    derived = derived_source_coefficients()
    if derived != EXPECTED_COEFF:
        errors.append("functional_derivative_coefficient_derivation")

    insertions = [(t.get("id"), x) for t in tops for x in t.get("c3_insertions", [])]
    if len(insertions) != 6:
        errors.append("c3_insertion_count")
    hist = Counter(x.get("vertex_order") for _, x in insertions)
    if hist != Counter({3: 4, 4: 1, 5: 1}):
        errors.append("c3_vertex_order_histogram")
    grav_orders = set()
    for t in tops:
        if t.get("species") == "graviton":
            grav_orders.update(t.get("vertex_orders", []))
    if grav_orders != {3, 4, 5}:
        errors.append("graviton_vertex_order_union")
    if any(x for t, x in insertions if byid.get(t, {}).get("species") == "ghost"):
        errors.append("c3_ghost_insertion")
    if any(x.get("vertex_order") == 2 for _, x in insertions):
        errors.append("c3_two_point_insertion")
    if any(x.get("c3_power") != 1 for _, x in insertions):
        errors.append("nonlinear_c3_power")
    if any(x.get("coupling") != COMMON for _, x in insertions):
        errors.append("noncommon_c3_coupling")

    return sorted(set(errors))


def mutate_delete_slot(m, tid, slot):
    x = copy.deepcopy(m)
    for t in x["topologies"]:
        if t["id"] == tid:
            t["c3_insertions"] = [z for z in t["c3_insertions"] if z["slot"] != slot]
    return x


def mutation_suite(m):
    muts = {}
    muts["delete_T5_C3_slot"] = mutate_delete_slot(m, "T5_GRAV", "v5")
    muts["delete_B43_C3_slot"] = mutate_delete_slot(m, "B43_GRAV", "v4")
    muts["delete_T333_C3_slot"] = mutate_delete_slot(m, "T333_GRAV", "v3c")

    x = copy.deepcopy(m)
    x["topologies"][0]["c3_insertions"].append(
        {"slot": "prop2", "vertex_order": 2, "c3_power": 1, "coupling": COMMON}
    )
    muts["add_C3_two_point_insertion"] = x

    x = copy.deepcopy(m)
    x["topologies"][3]["c3_insertions"].append(
        {"slot": "ghost_c3", "vertex_order": 3, "c3_power": 1, "coupling": COMMON}
    )
    muts["add_C3_ghost_insertion"] = x

    x = copy.deepcopy(m)
    x["topologies"][2]["c3_insertions"][0]["c3_power"] = 2
    muts["set_C3_power_two"] = x

    x = copy.deepcopy(m)
    x["topologies"][1]["source_coefficient"] = "4"
    muts["alter_source_coefficient"] = x

    x = copy.deepcopy(m)
    x["topologies"].append(
        {
            "id": "EXTRA_GRAV",
            "species": "graviton",
            "source_coefficient": "1",
            "vertex_orders": [3],
            "baseline": True,
            "external_symmetrized": True,
            "c3_insertions": [],
        }
    )
    muts["add_extra_source_topology"] = x

    x = copy.deepcopy(m)
    x["topologies"][1]["c3_insertions"][0]["coupling"] = "g_C3_fluc_independent_n4"
    muts["independent_n4_coupling"] = x
    return muts


def main():
    manifest = json.loads(MANIFEST.read_text())
    errors = validate(manifest)
    negatives = {}
    negative_errors = {}
    for name, mutant in mutation_suite(manifest).items():
        errs = validate(mutant)
        negatives[name] = bool(errs)
        negative_errors[name] = errs

    coeffs = derived_source_coefficients()
    insertions = [x for t in manifest["topologies"] for x in t["c3_insertions"]]
    hist = Counter(x["vertex_order"] for x in insertions)
    positive_pass = not errors
    negative_pass = all(negatives.values())
    scientific_pass = positive_pass and negative_pass

    result = {
        "gate": manifest["gate"],
        "source_coefficient_sequence": [str(coeffs[k]) for k in EXPECTED_IDS],
        "source_coefficient_derivation_pass": coeffs == EXPECTED_COEFF,
        "baseline_topology_ids": [t["id"] for t in manifest["topologies"]],
        "baseline_topology_count": len(manifest["topologies"]),
        "graviton_vertex_order_union": sorted(
            {o for t in manifest["topologies"] if t["species"] == "graviton" for o in t["vertex_orders"]}
        ),
        "c3_insertion_count": len(insertions),
        "c3_insertion_order_histogram": {str(k): hist[k] for k in sorted(hist)},
        "positive_errors": errors,
        "positive_pass": positive_pass,
        "negative_controls": negatives,
        "negative_control_errors": negative_errors,
        "negative_pass": negative_pass,
        "scientific_pass": scientific_pass,
        "classification": (
            "PASS_IMPLEMENTED_THREE_POINT_FLOW_C3_INSERTION_MANIFEST_SCOPED"
            if scientific_pass
            else "FAIL_C3_INSERTION_MANIFEST_INCOMPLETE_SCOPED"
        ),
        "interpretation_ceiling": "TOPOLOGY_AND_INSERTION_BOOKKEEPING_ONLY_NO_LOOP_INTEGRAND_OR_C3_BETA",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if not scientific_pass:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
