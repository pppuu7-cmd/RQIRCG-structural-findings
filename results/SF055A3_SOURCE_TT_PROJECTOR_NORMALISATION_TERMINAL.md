# SF055A3 — source TT projector normalisation — TERMINAL

Date: 2026-09-15
Prospective freeze: `9bf75bbe2c1ff7ae7fdad03475e2e07793ac42a0`.
Executed implementation head: `8afc79b78313e11369f386684e19859c9f312acd`.

## CLASSIFICATION

`PASS_SF055A3_SOURCE_TT_PROJECTOR_NORMALISATION_SCOPED`.

This validates the source normalisation objects only.

`SF055_LANE_A_TERMINAL_PASS = FALSE`.

`SF055_TERMINAL_PASS = FALSE`.

No C3 flow was computed or inspected.

## EXACT IMPLEMENTED SOURCE DEFINITIONS

Using the complete 125-component orthonormal external TT basis sums,

`N_g^(-1) = T^(3)(k;0) o Pi_TT^3 o T^(3)(k;0)`

and

`N_lambda^(-1) = T^(3)(0;1) o Pi_TT^3 o T^(3)(0;1)`

were generated directly from the SF055A2 source-Fourier Einstein-Hilbert three-point tensor.

Executed values:

`N_g^(-1) = 0.00052874519051635`,

`N_g = 1891.2701579818486`,

`N_lambda^(-1) = 0.0026385724906858796`,

`N_lambda = 378.99280900183135`.

Deterministic tensor hashes:

`T_G sha256 = 66638b7f47175bfbe0b1fb7234f0c0f5260764da17942b9eedc9af0c35cf8e80`,

`T_Lambda sha256 = d4bce18818b05fcaf3e36c78683da0c0ca43db995221462c71131c90ecdf84e5`.

## SOURCE EQ. (6) CONTROL

For `lambda = -7/10, -1/5, 2/5`, the component-wise decomposition

`T3(p;lambda)=T_G+lambda T_Lambda`

held over all 125 external TT components with maximum absolute residual

`1.734723475976807e-18`.

## ZERO-MOMENTUM TT ROBUSTNESS

The `T^(3)(0;1)` TT norm was evaluated by the symmetric-direction `p->0` prescription frozen before output.

No material ambiguity was found:

- plane `(0,1)`: `N_lambda^(-1)=0.0026385724906858796`;
- plane `(0,2)`: same displayed value;
- plane `(1,3)`: same displayed value.

Global O(4) rotation changed the inverse Lambda norm by only `8.673617379884035e-19` relative under the frozen diagnostic definition. Independent TT-basis rotations produced the same scale of residual.

Therefore the preregistered blocker

`BLOCKED_ZERO_MOMENTUM_TT_PROJECTOR_CONVENTION`

is **not active** for this implementation object.

## COUNTEREXAMPLE-FIRST CONTROLS

All frozen mutations were rejected:

- one polarization triple substituted for the full TT norm;
- arbitrary fitted rescaling of `T_G`;
- arbitrary fitted rescaling of `T_Lambda`.

Bose-labelled permutations, global rotations, independent TT-basis rotations and alternative symmetric embeddings preserved the complete norms within the prospectively frozen tolerance.

## REPRODUCIBILITY / PROVENANCE

Successful GitHub Actions run:

- run: `35001632950`;
- job: `104491160831`;
- executed head: `8afc79b78313e11369f386684e19859c9f312acd`;
- artifact id: `10409971299`;
- artifact name: `sf055a3-tt-projector-normalization`;
- artifact digest: `sha256:e92c770acb56722729d307ee7740b01cf4d521b42c8dda65bd64d1e178b6a40d`.

## NEW IMPLEMENTATION FACT

The source-defined TT projector normalisations required by Eqs. (10)–(11) are numerically closed in the same source-Fourier EH tensor basis, without fitting to Eq. (14), and the zero-momentum Lambda norm is robust under the frozen embedding/rotation controls.

## INTERPRETATION CEILING

No loop quadrature, finite-difference coupling flow, derivative-at-p=0 Eq. (14) reproduction, beta_mu reproduction, Lane-A terminal PASS, SF055 terminal PASS, or C3 result is authorized by this normalisation PASS.

## NEXT REQUIRED DEPENDENCY

`FULL_TT_PROJECTED_FIGURE2_QUADRATURE_DERIVATIVE_AND_FINITE_DIFFERENCE_EXTRACTION`,

plus the separately required same-conventions two-point integration/extraction for the frozen `beta_mu` target.
