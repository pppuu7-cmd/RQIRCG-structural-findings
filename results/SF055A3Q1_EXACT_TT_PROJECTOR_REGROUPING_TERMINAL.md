# SF055A3Q1 — exact TT projector regrouping acceleration — TERMINAL

Date: 2026-09-16
Prospective freeze: `ebfced4bc837c3042eb58bd1f536b136d90c2ef4`.
Implementation head: `d8647c16f18f043d15dde5aa7264dc3073cca569`.
Workflow head: `5661af6bdbd57463612fcb562ccf75b34128ef04`.

## CLASSIFICATION

`PASS_SF055A3_EXACT_TT_PROJECTOR_REGROUPING_ACCELERATION_SCOPED`.

This is an exact algebraic implementation-equivalence PASS only. It does not terminalize Lane A or SF055 and contains no substantive C3-flow result.

## EXACT IDENTITY VALIDATED

For a trilinear external-flow functional `F` and frozen source projector tensor `T_abc`, the implementation validates

`sum_abc T_abc F(E1_a,E2_b,E3_c)`

`= sum_ab F(E1_a,E2_b, sum_c T_abc E3_c)`.

No SVD/CP truncation, stochastic estimator, fitted rescaling, target-dependent approximation, or changed tensor basis is used.

## EXECUTED RESULT

GitHub Actions run `35016211111`, job `104540163228`, completed successfully.

Artifact:

- id: `10416306023`;
- name: `sf055a3q1-tt-projector-regrouping`;
- digest: `sha256:132244f69243c67e5c0d2c6c3af0842ea9bc202dcbb8bc5fb56e04367b3e41b7`.

The complete source projectors have:

- G channel: 26 nonzero tensor components, 19 nonzero grouped `(a,b)` pairs, grouped evaluation maximum 19;
- Lambda channel: 32 nonzero tensor components, 25 nonzero grouped `(a,b)` pairs, grouped evaluation maximum 25.

The inherited projector norms are reproduced:

- `||T_G||^2 = 0.0005287451905163499`;
- `||T_Lambda||^2 = 0.0026385724906858796`.

A full six-permutation symmetrized control gave

- brute result `0.42234129174039`;
- grouped result `0.4223412917403892`;
- absolute difference `7.771561172376096e-16`;
- frozen tolerance bound `1.42234129174039e-10`.

The implementation also passed its trilinearity control.

## COUNTEREXAMPLE-FIRST CONTROLS

All frozen mutations were rejected:

- dropping a nonzero grouped pair;
- substituting G-channel weights into the Lambda projector;
- fitted multiplicative rescaling;
- replacing the complete projector by a single polarization.

## Q2 NORMALISATION COMPATIBILITY

The Q1 symmetrized control was evaluated as an unnormalised sum over six labelled external permutations solely to test algebraic equivalence.

SF055A3Q2 subsequently fixed the physical/source convention as

`SOURCE_SYM_3 = (1/6) SUM_OVER_S3_LABELLED_EXTERNAL_PERMUTATIONS`.

There is no conflict: regrouping is a linear identity, so multiplying both brute and grouped sides by the same factor `1/6` preserves the validated equality exactly. Q1 does **not** select the source symmetrisation normalisation; Q2 remains the authority for that factor.

## IMPLEMENTATION CONSEQUENCE

The exact grouped source projector is now authorized for SF055A3 quadrature in the frozen D=4 Euclidean TT baseline implementation:

- use at most 19 grouped evaluations for the G projector;
- use at most 25 grouped evaluations for the Lambda projector;
- retain the Q2 source average `1/6` over labelled external permutations;
- retain all frozen Lane-A quadrature/extraction tolerances unchanged.

## INTERPRETATION CEILING

`EXACT_PROJECTOR_REGROUPING != LOOP_QUADRATURE_PASS`.

`EXACT_PROJECTOR_REGROUPING != EQ14_REPRODUCTION`.

`EXACT_PROJECTOR_REGROUPING != SF055_TERMINAL_PASS`.

No projected C3 beta function, fixed point, regulator-independent prediction, Lorentzian matching coefficient, or physical SF025 `b` is obtained here.

## NEXT REQUIRED DEPENDENCY

`SOURCE_NORMALIZED_FIGURE2_QUADRATURE_AND_EQ14_BASELINE_REPRODUCTION`

with the already-frozen convergence sequence `N={8,12,16,24}`, Q2 source symmetrisation, source loop measure, and independent same-conventions two-point reconstruction for `beta_mu`.