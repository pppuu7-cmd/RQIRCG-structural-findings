#!/usr/bin/env python3
"""SF055 Lane-B reproducibility repair (V2).

Scientific vertex evaluation is imported unchanged from
scripts/sf055_c3_vertex_generator.py. This wrapper changes only the fixed
SF052 TT frame and durable serialization, as frozen in
research_log/SF055_LANE_B_REPRODUCIBILITY_REPAIR.md.
"""
import itertools
import json
import math
from pathlib import Path

import numpy as np
import sf055_c3_vertex_generator as core

TOL = core.TOL
D = core.D
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "raw" / "SF055_C3_VERTEX_GENERATOR_V2.json"


def q10(x):
    return round(float(x), 10)


def lt(x, bound):
    return bool(float(x) < bound)


def sf050_analytic_tt_bases():
    s3 = math.sqrt(3.0)
    frames = [
        np.column_stack(([0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1])).astype(float),
        np.column_stack(([-s3 / 2, -0.5, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1])).astype(float),
        np.column_stack(([s3 / 2, -0.5, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1])).astype(float),
    ]
    mats = [
        np.diag([1.0, -1.0, 0.0]) / math.sqrt(2),
        np.diag([1.0, 1.0, -2.0]) / math.sqrt(6),
    ]
    for i, j in [(0, 1), (0, 2), (1, 2)]:
        M = np.zeros((3, 3))
        M[i, j] = M[j, i] = 1 / math.sqrt(2)
        mats.append(M)
    return [[E @ M @ E.T for M in mats] for E in frames]


def tt_quality_tuple(ps, hs):
    return (
        max(abs(np.trace(h)) for h in hs),
        max(np.linalg.norm(p @ h) for p, h in zip(ps, hs)),
        np.linalg.norm(sum(ps, np.zeros(D))),
    )


def main():
    inherited = json.loads(
        (ROOT / "results" / "raw" / "SF052_DERIVATIVE_REDUNDANT_QUOTIENT.json").read_text()
    )
    result = {
        "gate": "SF055_C3_PROJECTED_FRG_IMPLEMENTATION_CONTRACT",
        "lane": "B_COMMON_ORIGIN_C3_VERTEX_GENERATOR",
        "repair_version": "V2_REPRODUCIBILITY_ONLY",
        "scope": "FLAT_EUCLIDEAN_PURE_GRAVITON_VERTEX_CALIBRATION_NO_FRG_LOOPS",
        "scientific_core": "scripts/sf055_c3_vertex_generator.py",
        "repair_contract": "research_log/SF055_LANE_B_REPRODUCIBILITY_REPAIR.md",
        "method": {
            "operator": "int sqrt(g) C_rhosigma^munu C_munu^alphabeta C_alphabeta^rhosigma",
            "single_common_coupling_parameter": True,
            "pass_tolerance": "1e-10_on_unrounded_runtime_values",
            "SF052_symmetric_TT_basis": "explicit_SF050_analytic_frames_no_SVD",
            "durable_serialization": "rounded_nonzero_diagnostics_and_threshold_certificates",
        },
    }

    ps2 = [np.array([1.0, 0, 0, 0]), np.array([-1.0, 0, 0, 0])]
    hs2 = core.generic_tts(ps2, 12)
    gamma2 = core.vertex(ps2, hs2)
    tq2 = tt_quality_tuple(ps2, hs2)
    result["Gamma2_control"] = {
        "value_rounded": q10(gamma2),
        "value_abs_lt_1e-10": lt(abs(gamma2), TOL),
        "trace_lt_1e-12": lt(tq2[0], 1e-12),
        "transversality_lt_1e-12": lt(tq2[1], 1e-12),
        "momentum_conservation_lt_1e-12": lt(tq2[2], 1e-12),
    }
    result["Gamma2_control"]["pass"] = all(
        result["Gamma2_control"][k]
        for k in ("value_abs_lt_1e-10", "trace_lt_1e-12", "transversality_lt_1e-12", "momentum_conservation_lt_1e-12")
    )

    ps3 = core.symmetric_ps3()
    bases = sf050_analytic_tt_bases()
    ratios = []
    zero_ref_max = 0.0
    gen_norm_div6 = 0.0
    ref_norm = 0.0
    nonzero = 0
    for i, j, k in itertools.product(range(5), repeat=3):
        hs = [bases[0][i], bases[1][j], bases[2][k]]
        ref = core.sf052_c3_component(ps3, hs)
        got = core.vertex(ps3, hs)
        ref_norm += ref * ref
        gen_norm_div6 += (got / 6.0) ** 2
        if abs(ref) > TOL:
            ratios.append(got / ref)
            nonzero += 1
        else:
            zero_ref_max = max(zero_ref_max, abs(got))
    ratio_med = float(np.median(ratios))
    ratio_span = max(abs(r - ratio_med) for r in ratios)
    cubic_checks = {
        "factor_deviation_lt_1e-10": lt(abs(ratio_med - 6.0), TOL),
        "max_component_ratio_deviation_lt_1e-10": lt(ratio_span, TOL),
        "reference_zero_leakage_lt_1e-10": lt(zero_ref_max, TOL),
        "reference_norm_error_lt_1e-10": lt(abs(ref_norm - 95 / 768), TOL),
        "generated_norm_after_dividing_6_error_lt_1e-10": lt(abs(gen_norm_div6 - 95 / 768), TOL),
        "inherited_projector_response_is_one": inherited["normalized_projector_responses"]["C3"] == 1,
    }
    result["Gamma3_SF052_match"] = {
        "tt_components": 125,
        "nonzero_reference_components": nonzero,
        "functional_derivative_global_factor_rounded": q10(ratio_med),
        "expected_global_factor": "3! = 6",
        "reference_tensor_norm_target": "95/768",
        **cubic_checks,
        "pass": all(cubic_checks.values()),
    }

    controls = {}
    for n in (3, 4, 5):
        ps = core.generic_momenta(n, 100 + n)
        hs = core.generic_tts(ps, 200 + n)
        base = core.vertex(ps, hs, 1.0)
        twice = core.vertex(ps, hs, 2.0)
        zero = core.vertex(ps, hs, 0.0)
        vals = [
            core.vertex([ps[i] for i in perm], [hs[i] for i in perm], 1.0)
            for perm in itertools.permutations(range(n))
        ]
        max_diff = max(abs(v - base) for v in vals)
        scale = max(1.0, abs(base))
        ratio = twice / base if abs(base) > 1e-14 else float("nan")
        tq = tt_quality_tuple(ps, hs)
        checks = {
            "zero_coupling_abs_lt_1e-10": lt(abs(zero), TOL),
            "coupling_scaling_error_lt_1e-10": lt(abs(ratio - 2.0), TOL),
            "bose_scaled_residual_lt_1e-10": lt(max_diff / scale, TOL),
            "trace_lt_1e-12": lt(tq[0], 1e-12),
            "transversality_lt_1e-12": lt(tq[1], 1e-12),
            "momentum_conservation_lt_1e-12": lt(tq[2], 1e-12),
        }
        controls[str(n)] = {
            "unit_coupling_value_rounded": q10(base),
            "double_coupling_value_rounded": q10(twice),
            "double_to_unit_ratio_rounded": q10(ratio),
            "permutations_tested": math.factorial(n),
            **checks,
            "pass": all(checks.values()),
        }
    result["Gamma3_4_5_common_origin_controls"] = controls

    result["lane_B_pass"] = (
        result["Gamma2_control"]["pass"]
        and result["Gamma3_SF052_match"]["pass"]
        and all(v["pass"] for v in controls.values())
    )
    result["classification"] = (
        "PASS_C3_COMMON_ORIGIN_VERTEX_GENERATOR_SCOPED"
        if result["lane_B_pass"]
        else "BLOCKED_C3_VERTEX_GENERATOR_NOT_CLOSED"
    )
    result["SF055_terminal_pass"] = False
    result["remaining_lanes"] = {
        "A": "OPEN_BASELINE_EH_GHOST_FLOW_REPRODUCTION",
        "C": "ABSTRACT_MANIFEST_PASS_IMPLEMENTED_DIAGRAM_MANIFEST_OPEN",
        "projected_C3_beta": "UNAUTHORIZED_UNTIL_ALL_CALIBRATION_LANES_TERMINAL",
    }
    OUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))
    if not result["lane_B_pass"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
