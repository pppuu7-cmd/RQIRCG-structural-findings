# SF022 — RHPI/ADM 1PN connected three-source phase-rate kernel — TERMINAL

Date: 2026-09-14
Status: **TERMINAL / FIRST POST-SELECTION CONNECTED KERNEL / NOT YET FULL G97 LAB PREDICTION**

Preregistration: `bfc0f14a261cc30bfeb7a107b9244a604cf5eef0`.
Exact script: `scripts/sf022_eih_connected_kernel.py`.
Exact archived output: `results/raw/SF022_EIH_CONNECTED_KERNEL_EXACT.json`.

## Frozen theory input

Use the standard Einstein-Infeld-Hoffmann N-body Lagrangian through 1PN,

`L = L_N + c^-2 L_1PN + O(c^-4)`,

whose static `O(G^2/c^2)` sector contains

`L_static^(1PN) = -(G^2/(2c^2)) Sum_A Sum_{B!=A} Sum_{C!=A} m_A m_B m_C/(r_AB r_AC)`.

No nonlinear coefficient is introduced beyond the RHPI-selected ADM/Einstein law and the inherited Newton constant `G`.

## Ordered-sum derivation

For exactly three distinct source labels `A,B,C`, keep only the terms with all three labels distinct.

For fixed center label `A`, the ordered pairs `(B,C)` and `(C,B)` contribute equally. Therefore the factor of two cancels the explicit `1/2`:

`L_ABC,center=A = -(G^2 m_A m_B m_C/c^2) / (r_AB r_AC)`.

Summing the three choices of center gives

`L_ABC^(1PN) = -(G^2 m_A m_B m_C/c^2) F_ABC`,

where

`F_ABC = 1/(r_AB r_AC) + 1/(r_AB r_BC) + 1/(r_AC r_BC)`.

For a static conservative kernel `L=-V`, hence

`V_ABC^(1PN) = +(G^2 m_A m_B m_C/c^2) F_ABC`.

The inherited branch-phase convention is

`dot(phi) = -V/hbar`,

so the candidate connected phase rate is not fitted but derived:

`dot(chi_ABC) = -(G^2 m_A m_B m_C/(hbar c^2)) Delta_A Delta_B Delta_C F_ABC`.

## Lower-order nulls

### Newtonian sector

The Newtonian interaction is a sum of pair functions

`V_N = -G[m_A m_B/r_AB + m_A m_C/r_AC + m_B m_C/r_BC]`.

Every term depends on at most two branch labels. Therefore

`Delta_A Delta_B Delta_C V_N = 0`

exactly.

### Repeated-label 1PN sector

Terms with `B=C` in the EIH triple sum have the form

`m_A m_B^2/r_AB^2`

or permutations. They depend on at most the two labels carried by the distinct bodies, so their third finite difference is also exactly zero.

Thus the first static point-source connected contribution in this representative comes from the all-distinct EIH term.

## Exact positive-control result

For the prospectively frozen one-dimensional geometry (in unit `ell`)

- `A0=0`, `A1=1`;
- `B0=3`, `B1=4`;
- `C0=8`, `C1=10`,

the exact values of `F_ABC * ell^2` are

- `000: 2/15`,
- `001: 2/21`,
- `010: 1/8`,
- `011: 1/12`,
- `100: 1/5`,
- `101: 1/7`,
- `110: 1/6`,
- `111: 1/9`.

Using the frozen sign convention,

`Delta_A Delta_B Delta_C F_ABC = 13/(2520 ell^2)`.

Therefore

`dot(chi_ABC) = -13 G^2 m_A m_B m_C/(2520 hbar c^2 ell^2)`

for this exact algebraic control geometry.

The value is nonzero and contains no free connected coefficient.

## Negative controls

### N1 — no A branch displacement

Setting `A1=A0` makes the exact third finite difference zero.

### N2 — arbitrary <=2-body branch polynomial

For

`k + A a + B b + C c + AB ab + AC ac + BC bc`,

the exact third finite difference is zero.

### N3 — gravity off

The derived connected rate is proportional to `G^2`, so `G -> 0` gives zero.

All preregistered controls pass.

## Terminal classification

`RHPI_ADM_DERIVES_PARAMETER_FREE_1PN_CONNECTED_THREE_SOURCE_KERNEL_SCOPED`.

This is the first post-selection nonzero connected object in the new branch.

## What has been established

Within the standard point-source EIH representative of the prospectively selected RHPI/ADM law:

1. all static Newtonian pair interactions are annihilated by the connected third finite difference;
2. repeated-label `O(G^2/c^2)` terms are also annihilated;
3. the genuine all-distinct 1PN interaction produces a generically nonzero connected phase-rate kernel;
4. its coefficient is fixed by `G`, `c`, `hbar`, source masses and geometry;
5. no `lambda`, cubic kernel normalization, mediator phase, or post-hoc connected parameter is present.

## Scientific interpretation

This closes the exact obstruction that defeated the old G93/G94 line at the **point-source conservative-kernel level**: there is now a candidate-owned nonlinear source-to-phase map derived from a principle selected before the connected outcome.

The old project could only show algebraic connected sensitivity with an arbitrary normalization. SF022 instead derives the normalization from the selected nonlinear law.

## Claim ceiling

SF022 is **not yet** the final physical laboratory prediction.

It does not yet establish:

- a finite-duration static closed preparation;
- support/apparatus stress-energy closure at 1PN;
- gauge/canonical-invariance of the isolated EIH potential term by itself;
- finite-size/tidal corrections for realistic sources;
- quantum noise/dephasing;
- discrimination from GR (the selected classical law has converged to GR in this scope);
- new physics.

The EIH potential is a coordinate/canonical representative. The physical connected observable must be embedded into a closed relational history before promotion beyond a kernel result.

## Exact next gate

**SF023 — closed G97 branch-history and gauge/boundary audit.**

Required before a laboratory `chi_ABC` prediction:

1. construct a closed branch-history protocol including apparatus/support or a free-evolution protocol that does not require hidden holding forces;
2. apply the same 1PN law to all branch-dependent source/apparatus bodies;
3. define relational endpoints / phase comparison;
4. audit total-derivative/canonical-transformation boundary terms;
5. show the connected phase is not an artifact of the chosen EIH coordinate representative;
6. freeze all source finite-size/constitutive parameters before evaluation.
