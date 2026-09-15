# SF055A3Q1 — exact complete-TT projector regrouping — TERMINAL

Date: 2026-09-15
Parent: SF055A3 source-Fourier baseline loop reproduction.

## Classification

`PASS_SF055A3_EXACT_TT_PROJECTOR_REGROUPING_ACCELERATION_SCOPED`.

This closes SF055A3Q1. It authorizes the exact grouped external-TT projector in the already-frozen Figure-2 quadrature. It does not by itself terminalize Lane A or SF055.

## Exact identity tested

For each already-source-generated projector `T in {T_G,T_Lambda}` the executed checker compared

`sum_abc T[a,b,c] F(E1[a],E2[b],E3[c])`

against

`sum_ab F(E1[a],E2[b],sum_c T[a,b,c]E3[c])`.

No SVD/CP truncation, stochastic trace estimate, interpolation, fitted factor, changed basis, changed topology, propagator or regulator was used.

## Result

All prospectively frozen controls passed:

- trilinearity of every canonical Figure-2 topology in every external polarization slot at both frozen q controls;
- exact grouped-versus-brute comparison for both source projectors and all four topology classes at both q controls;
- the full six-labelled-external-permutation control;
- skipped-zero projector norm requirement;
- grouped evaluation-count requirement;
- all declared counterexamples.

The complete symmetrized B43 control was

- brute: `0.42234129174039`;
- grouped: `0.4223412917403892`;
- absolute difference: `7.771561172376096e-16`.

Projector sparsity/evaluation facts:

- `T_G`: 26 nonzero components, 19 nonzero grouped `(a,b)` rows, maximum 19 grouped topology evaluations, skipped norm fraction `1.4243321899823828e-31`;
- `T_Lambda`: 32 nonzero components, 25 nonzero grouped rows, maximum 25 grouped topology evaluations, skipped norm fraction exactly zero.

The corresponding complete norms remain the already-authoritative values

- `||T_G||^2 = 0.0005287451905163499`;
- `||T_Lambda||^2 = 0.0026385724906858796`.

## Negative controls

All were rejected as required:

- replacing `T_Lambda` weights with `T_G` weights;
- deleting a nonzero grouped term;
- applying a fitted multiplicative rescaling;
- replacing the complete projector by a single polarization triple.

## Reproducibility / provenance

GitHub Actions:

- run `35016211111`;
- job `104540163228`;
- conclusion `success`;
- head `5661af6bdbd57463612fcb562ccf75b34128ef04`;
- artifact id `10416306023`;
- artifact digest `sha256:132244f69243c67e5c0d2c6c3af0842ea9bc202dcbb8bc5fb56e04367b3e41b7`.

## Interpretation ceiling / next dependency

`Q1_PASS != LANE_A_PASS` and `Q1_PASS != SF055_PASS`.

The next and only remaining mandatory Lane-A science step is the already-frozen deterministic Figure-2 baseline quadrature, derivative/finite-difference extraction, and separate same-conventions two-point `beta_mu` reproduction. The programme hard-stops before any substantive C3 flow if that baseline does not reproduce all frozen targets.
