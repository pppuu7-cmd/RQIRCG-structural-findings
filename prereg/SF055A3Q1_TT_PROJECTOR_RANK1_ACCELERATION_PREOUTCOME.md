# SF055A3Q1 — complete-TT projector rank-one acceleration — PREOUTCOME

Date: 2026-09-15
Parent gate: `SF055A3_SOURCE_FOURIER_BASELINE_LOOP_REPRODUCTION_PREOUTCOME`.
Inherited terminal authority: `PASS_SF055A3_SOURCE_TT_PROJECTOR_NORMALISATION_SCOPED`, merge `6c6a324ba94c25fa40dc30565b05407109a92ece`.

## PURPOSE

Reduce the computational cost of the already-frozen complete external-TT projection before the N=8,12,16,24 loop quadrature, without changing the physical flow object, source tensor, topology, kinematics, regulator, or any Lane-A PASS threshold.

This is an implementation-equivalence gate only. It cannot change any source normalization or fit Eq. (14).

## FROZEN IDENTITY

For either already-source-generated projector tensor `T[a,b,c]` in the orthonormal external TT bases, and any trilinear external flow component `F(h1,h2,h3)`, use the exact regrouping

`sum_{a,b,c} T[a,b,c] F(E1[a],E2[b],E3[c])`

`= sum_{a,b} F(E1[a],E2[b], H3[a,b])`,

where

`H3[a,b] = sum_c T[a,b,c] E3[c]`.

Thus a complete 125-component contraction can be evaluated using at most 25 flow evaluations per projector, with no SVD, fitted factor, stochastic trace estimator, or truncated tensor decomposition.

Apply separately to the already-frozen `T_G` and `T_Lambda`; no mixing or redefinition of the two source channels is permitted.

## FROZEN OBJECTS

- projector tensors: direct source-generated `T_G` and `T_Lambda` from `scripts/sf055a3_tt_projector_normalization.py`;
- external basis: the same 5x5x5 orthonormal TT bases used by the normalization PASS;
- flow kernels: the existing C3-disabled Figure-2 canonical topology functions in `scripts/sf055a3_figure2_contraction_assembly.py`;
- topology coefficients remain `(-1/2,+3,-3,+6)`;
- fixed-q controls are the two already-frozen dense q controls from the contraction-assembly PASS;
- tolerance for equality: absolute <= `1e-10*(1+|brute|)`.

## REQUIRED POSITIVE CONTROLS

1. Regrouping reconstructs the raw projector tensor coefficient contraction algebraically to machine precision.
2. Each canonical topology is verified trilinear in each external polarization slot on both frozen q controls.
3. For both `T_G` and `T_Lambda`, accelerated and explicit nonzero-weight brute-force contractions agree for all four canonical topology classes on both frozen q controls.
4. At least one full external six-permutation symmetrized projected control agrees between accelerated and explicit implementations.
5. Zero-weight tensor entries are skipped only as exact/numerical zeros below `1e-15`; the skipped total projector norm fraction must be <= `1e-24`.
6. Evaluation count is reported; acceleration is authorized only if the grouped path uses <=25 topology evaluations per projector before external-permutation multiplication.

## NEGATIVE CONTROLS

The checker must reject:

- deleting one nonzero `(a,b)` grouped term;
- substituting `T_G` weights for `T_Lambda` in a Lambda-channel contraction;
- applying an arbitrary fitted rescaling to grouped weights;
- replacing the complete source tensor by a single polarization triple.

## PASS

`PASS_SF055A3_EXACT_TT_PROJECTOR_REGROUPING_ACCELERATION_SCOPED`

only if all positive and negative controls pass.

## FAIL

`FAIL_SF055A3_TT_PROJECTOR_REGROUPING_EQUIVALENCE_SCOPED`

if the already-source-defined complete TT contraction and the regrouped implementation disagree beyond tolerance.

## INVALID

Any use of truncated SVD/CP rank, stochastic estimation, target-dependent rescaling, changed external basis, changed source tensor, or altered topology/propagator/regulator is outside this gate and requires new prospective authority.

## INTERPRETATION CEILING

PASS would authorize only a computationally cheaper exact implementation of the same frozen external-TT projector during quadrature. It is not loop quadrature, Eq. (14) reproduction, Lane-A PASS, SF055 PASS, a C3 flow, or a physical matching result.
