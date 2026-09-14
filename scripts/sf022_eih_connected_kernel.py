#!/usr/bin/env python3
"""Exact algebraic checks for SF022.

This script evaluates the prospectively frozen one-dimensional control geometry
using rational arithmetic.  It does not model apparatus/support closure.
"""

from fractions import Fraction
import json

A = {0: Fraction(0), 1: Fraction(1)}
B = {0: Fraction(3), 1: Fraction(4)}
C = {0: Fraction(8), 1: Fraction(10)}


def f_geom(a: int, b: int, c: int) -> Fraction:
    r_ab = abs(A[a] - B[b])
    r_ac = abs(A[a] - C[c])
    r_bc = abs(B[b] - C[c])
    return (
        Fraction(1, r_ab * r_ac)
        + Fraction(1, r_ab * r_bc)
        + Fraction(1, r_ac * r_bc)
    )


def delta3(values):
    return (
        values[(1, 1, 1)]
        - values[(1, 1, 0)]
        - values[(1, 0, 1)]
        - values[(0, 1, 1)]
        + values[(1, 0, 0)]
        + values[(0, 1, 0)]
        + values[(0, 0, 1)]
        - values[(0, 0, 0)]
    )


def q(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


values = {(a, b, c): f_geom(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)}
connected = delta3(values)

# Generic <=2-body control on the Boolean cube.
k, A1, B1, C1, AB, AC, BC = map(Fraction, range(1, 8))
pair_values = {
    (a, b, c): k + A1*a + B1*b + C1*c + AB*a*b + AC*a*c + BC*b*c
    for a in (0, 1) for b in (0, 1) for c in (0, 1)
}

# Negative control: A has no branch displacement.
A_saved = dict(A)
A[1] = A[0]
neg_values = {(a, b, c): f_geom(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)}
A.update(A_saved)

result = {
    "classification": "RHPI_ADM_DERIVES_PARAMETER_FREE_1PN_CONNECTED_THREE_SOURCE_KERNEL_SCOPED",
    "control_geometry_values_F_times_ell2": {
        f"{a}{b}{c}": q(values[(a, b, c)])
        for a in (0, 1) for b in (0, 1) for c in (0, 1)
    },
    "delta3_F_times_ell2": q(connected),
    "expected_delta3": "13/2520",
    "positive_control_pass": connected == Fraction(13, 2520),
    "pairwise_polynomial_delta3": q(delta3(pair_values)),
    "pairwise_null_pass": delta3(pair_values) == 0,
    "no_A_displacement_delta3": q(delta3(neg_values)),
    "no_A_displacement_null_pass": delta3(neg_values) == 0,
    "derived_energy_kernel": "V_ABC^(1PN)=+(G^2 m_A m_B m_C/c^2) F_ABC",
    "derived_phase_rate_kernel": "dot_chi_ABC=-(G^2 m_A m_B m_C/(hbar c^2)) Delta3[F_ABC]",
    "positive_control_phase_rate": "-13 G^2 m_A m_B m_C/(2520 hbar c^2 ell^2)",
    "claim_ceiling": "point-source instantaneous conservative EIH representative only; apparatus/support closure and gauge/boundary audit deferred",
}

print(json.dumps(result, indent=2, sort_keys=True))
