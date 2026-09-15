# SF055A2 — source-Fourier EH/ghost baseline seed engine — TERMINAL

Date: 2026-09-15
Parent SF055 preregistration: `9d998d984566aa5bf290312a6a062fd632c85561`.
SF055A2 prospective freeze: `1dafca60d599195e1dec2d2cd0f2f352ea5c387b`.
Predecessor retained: `INVALID_SEED_POSITIVE_CONTROL_MIXED_FOURIER_CONVENTIONS_SCOPED`.

## RESULT / CLASSIFICATION

`PASS_SOURCE_FOURIER_EH_GHOST_BASELINE_SEED_ENGINE_SCOPED`.

This closes only the source-Fourier baseline **seed-object** calibration.

SF055 overall remains non-terminal:

`SF055_TERMINAL_PASS = FALSE`.

Lane A still requires the full internal propagator + Figure-2 EH/ghost three-point loop realization and same-code-path published baseline reproduction before any substantive C3 projected flow may be inspected.

## WHY THIS DOES NOT REWRITE SF055A

The predecessor SF055A remains INVALID because its frozen TT control mixed real-exponential and source-Fourier momentum coordinates.

SF055A2 was separately preregistered after that diagnosis and before any new output. It uses one convention throughout:

`partial_mu -> i p_mu`.

The first gate's raw failure and terminal INVALID result remain durable and unchanged.

## PRIMARY SOURCE OBJECTS VALIDATED

Within D=4 flat Euclidean linear-split source conventions:

- one covariant Einstein-Hilbert action `sqrt(g)(-R+2 Lambda)` generates the tested n=2,3,4,5 graviton seeds;
- the raw Faddeev-Popov operator is generated from the same source linear gauge condition;
- the Landau TT test sector satisfies the frozen gauge constraint;
- the optimized regulator denominator and Appendix-A threshold-function convention are reproduced.

## EXECUTED POSITIVE CONTROLS

### TT two-point / Landau

For all five normalized TT polarizations and

`Lambda in {0, +3/20, -1/5}`,

the source-Fourier action generator reproduced

`K_EH (p^2 - 2 Lambda)`, `K_EH=1/(32 pi)`,

with maximum absolute error

`1.734723475976807e-18`.

The maximum Landau gauge-function norm was exactly zero in the executed controls.

### Common EH n=3,4,5 seeds

At the frozen dense TT controls with `Lambda=-7/10`:

- n=3 raw value: `0.008584658331267788`; all 6 permutations agree, max difference `1.73e-18`;
- n=4 raw value: `0.003238758821367775`; all 24 permutations agree, max difference `6.51e-18`;
- n=5 raw value: `0.0010631582906211552`; all 120 permutations agree, max difference `1.45e-17`.

All were finite and nonzero.

### Faddeev-Popov seed

The three frozen raw Fourier ghost two-point controls matched

`bar c M c = -p_c^2 (bar c.c)`

with maximum absolute error

`2.546621511893469e-18`.

The frozen generic ghost-ghost-h control is nonzero:

`0.3168020092097069`.

The source linear split/gauge h-degree controls give ghost-ghost-h^2 = ghost-ghost-h^3 = 0.

### Regulator / threshold functions

All optimized-regulator denominator controls passed exactly at the frozen q^2/mu points.

All six numerical threshold-function controls passed. Maximum scaled error:

`3.9474596431116675e-16`.

## COUNTEREXAMPLE-FIRST NEGATIVE CONTROLS

All ten prospectively frozen mutations were rejected:

1. predecessor real-exponential derivative convention;
2. wrong EH kinetic normalization;
3. wrong cosmological TT sign;
4. independent n=4 rescaling;
5. non-Bose n=3 mutation;
6. nonzero ghost-h^2 mutation;
7. omitted ghost-h interaction;
8. wrong raw Fourier FP two-point sign;
9. wrong optimized-regulator shape;
10. wrong `dot r` threshold derivative.

Thus the PASS is not merely a positive-template match.

## REPRODUCIBILITY / PROVENANCE

GitHub Actions:

- run: `34997423208`;
- job: `104477069061` (`source-fourier-seed`);
- conclusion: `success`;
- executed branch head: `81c637370be876bccf7806a52071b66841391cbd`;
- artifact id: `10407843711`;
- artifact name: `sf055a2-source-fourier-seed-engine`;
- artifact digest: `sha256:21abcd4b7cbeffdbd8d7d6d71c697c7aebe883e0a3afc439dd554902ccb1085b`.

Durable raw output:

`results/raw/SF055A2_SOURCE_FOURIER_SEED_ENGINE.json`.

## NEW IMPLEMENTATION FACT

A single source-Fourier implementation now simultaneously closes:

`EH n=2,3,4,5 seed generation + raw FP 2pt/ghost-h seed + Landau TT control + optimized regulator + threshold convention`

under one internally consistent momentum convention.

This removes the seed-object ambiguity exposed by the invalid predecessor.

## INTERPRETATION CEILING

This PASS does not establish:

- the full internal Landau graviton propagator;
- Figure-2 loop tensor contractions;
- loop momentum integration;
- the published `Flow_G^(3)` / `Flow_Lambda^(3)` baseline;
- Eq. (14) reproduction;
- Lane-A terminal PASS;
- an unprojected C3 loop RHS;
- a C3 beta function, fixed point, regulator independence, background/fluctuation equality or Lorentzian matching.

## NEXT RECOMMENDED GATE

Highest-information next dependency:

`SOURCE_FOURIER_INTERNAL_PROPAGATOR_PLUS_FIGURE2_BASELINE_LOOP_REPRODUCTION`.

Before execution, prospectively freeze the full Landau internal graviton/ghost propagator conventions, regulator insertions, loop momentum routing, Figure-2 tensor contractions, radial/angular integration strategy, and exact published baseline comparison thresholds. Then require same-code-path reproduction of the frozen Local Quantum Gravity baseline before any C3 insertion is enabled.
