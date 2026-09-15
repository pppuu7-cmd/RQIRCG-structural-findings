#!/usr/bin/env python3
"""SF055 pre-science checks.

This script checks only frozen source transcription, topology completeness logic,
and the inherited SF052 projector-interface certificate.  It does NOT generate
C3 vertices and therefore cannot terminalize SF055 Lane B or Lane A.
"""
from fractions import Fraction as F
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "raw" / "SF055_PREFLIGHT_CHECKS.json"


def eq14_exact():
    g, mu, lam = F(1), F(1, 10), F(-7, 10)
    bg_bracket = (
        (584*lam**3 - 910*lam**2 + 445*lam - F(299,4)) / (15*(mu+1)**5)
        - F(47,8)/(mu+1)**2
        - F(5,8)
        + (864*lam**3 + 133*lam**2 - 112*lam + F(49,4))/(6*(mu+1)**4)
        - (60*lam**2 - 58*lam - 15)/(6*(mu+1)**3)
    )
    a = F(8,19) * bg_bracket
    d = (
        (2*lam**3 - 4*lam**2 + 3*lam - F(11,20))/(mu+1)**4
        - 4*(4*lam**2-lam)/(mu+1)**3
        + (1-3*lam)/(mu+1)**2
        + F(6,5)
    )
    c_lam = -lam*a/F(2) + d
    e_mu = 2*g*((16*lam**2 - 8*lam + F(7,4))/(3*(mu+1)**3)
                + (2*lam-1)/(mu+1)**2 - 1)
    return {
        "B_g": str(bg_bracket),
        "beta_g_const": "2",
        "beta_g_invpi_coeff": str(a),
        "beta_lambda3_const": str(-2*lam),
        "beta_lambda3_invpi_coeff": str(c_lam),
        "beta_mu_const": str(-2*mu),
        "beta_mu_invpi_coeff": str(e_mu),
        "decimals": {
            "beta_g": 2 + float(a)/math.pi,
            "beta_lambda3": float(-2*lam) + float(c_lam)/math.pi,
            "beta_mu": float(-2*mu) + float(e_mu)/math.pi,
        },
    }


def topology_manifest():
    # Abstract insertion slots implied by the differentiated Wetterich flow.
    # Symmetry factors are deliberately NOT inferred here.
    baseline = {
        "triangle": ["G3a", "G3b", "G3c"],
        "bubble_34": ["G3", "G4"],
        "tadpole_5": ["G5"],
        "ghost": ["ghost_baseline"],
    }
    expected_linear_c3 = {
        "triangle": {"C3@G3a", "C3@G3b", "C3@G3c"},
        "bubble_34": {"C3@G3", "C3@G4"},
        "tadpole_5": {"C3@G5"},
        "ghost": set(),
    }
    forbidden = {"C3@G2", "C3@ghost", "C3x2"}
    return baseline, expected_linear_c3, forbidden


def validate_manifest(candidate, expected, forbidden):
    seen = set()
    problems = []
    for topo, exp in expected.items():
        got = set(candidate.get(topo, []))
        if got != exp:
            problems.append({"topology": topo,
                             "missing": sorted(exp-got),
                             "extra": sorted(got-exp)})
        seen |= got
    bad = sorted(seen & forbidden)
    if bad:
        problems.append({"forbidden_seen": bad})
    return problems


def negative_controls(expected, forbidden):
    tests = {}
    good = {k: sorted(v) for k,v in expected.items()}
    tests["good_manifest_passes"] = validate_manifest(good, expected, forbidden) == []

    missing = json.loads(json.dumps(good))
    missing["triangle"].remove("C3@G3b")
    tests["omitted_triangle_slot_fails"] = validate_manifest(missing, expected, forbidden) != []

    extra_g2 = json.loads(json.dumps(good))
    extra_g2["triangle"].append("C3@G2")
    tests["C3_Gamma2_insertion_fails"] = validate_manifest(extra_g2, expected, forbidden) != []

    ghost = json.loads(json.dumps(good))
    ghost["ghost"].append("C3@ghost")
    tests["ghost_C3_insertion_fails"] = validate_manifest(ghost, expected, forbidden) != []

    double = json.loads(json.dumps(good))
    double["bubble_34"].append("C3x2")
    tests["double_C3_linear_order_fails"] = validate_manifest(double, expected, forbidden) != []
    return tests


def inherited_projector_certificate():
    src = ROOT / "results" / "raw" / "SF052_DERIVATIVE_REDUNDANT_QUOTIENT.json"
    data = json.loads(src.read_text())
    wanted = {
        "C3": 1, "S3": 0, "SSC": 0, "RDeltaR": 0, "SDeltaS": 0
    }
    return {
        "source_file": str(src.relative_to(ROOT)),
        "responses_match": data["normalized_projector_responses"] == wanted,
        "residual_norm_match": data["residual_norm"] == "243/9920",
        "classification_match": data["classification"] == "PASS_COMPLETE_SIX_DERIVATIVE_TT_QUOTIENT_SCOPED",
    }


def main():
    exact = eq14_exact()
    expected_exact = {
        "B_g": "-274830865/3865224",
        "beta_g_invpi_coeff": "-274830865/9179907",
        "beta_lambda3_invpi_coeff": "-3364922887/183598140",
        "beta_mu_invpi_coeff": "6554/3993",
    }
    eq14_ok = all(exact[k] == v for k,v in expected_exact.items())
    baseline, expected, forbidden = topology_manifest()
    neg = negative_controls(expected, forbidden)
    proj = inherited_projector_certificate()

    result = {
        "gate": "SF055_C3_PROJECTED_FRG_IMPLEMENTATION_CONTRACT",
        "scope": "PREFLIGHT_ONLY_NOT_TERMINAL",
        "eq14_spotcheck": {"pass": eq14_ok, "computed": exact},
        "topology": {
            "baseline_abstract_classes": baseline,
            "expected_linear_C3_slots": {k: sorted(v) for k,v in expected.items()},
            "forbidden": sorted(forbidden),
            "negative_controls": neg,
            "pass": all(neg.values()),
        },
        "projector_interface_inherited_certificate": proj,
        "lane_status": {
            "A": "PARTIAL_SOURCE_TRANSCRIPTION_ONLY_EH_GHOST_DIAGRAM_REPRODUCTION_STILL_REQUIRED",
            "B": "OPEN_COMMON_C3_VERTEX_GENERATOR_3_4_5_REQUIRED",
            "C": "ABSTRACT_SLOT_COMPLETENESS_CHECKED_IMPLEMENTED_DIAGRAM_MANIFEST_STILL_REQUIRED",
        },
        "terminal_SF055_pass": False,
    }
    result["preflight_pass"] = (
        result["eq14_spotcheck"]["pass"]
        and result["topology"]["pass"]
        and all(v for k,v in proj.items() if k.endswith("_match"))
    )
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if not result["preflight_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
