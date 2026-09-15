# RQIRCGSF research ledger — SF038 addendum

Date: 2026-09-15

Gate: `SF038_SIGNED_AMPLITUDE_PARITY_CALIBRATION_PREOUTCOME_GATE`.

Preregistration: `08d16e0c75192345f196cb82f0aaf0bb5c6eb04b`.

Script: `735257e70413746db9e05fcfdb166585e162cb75`.

Raw: `6c942861ead30a6f8bbdfa947a8104d0173dbab5`.

Terminal: `6a8afd7bde8a4d9d7783e9ec01dfb5f444250ff9`.

Classification:

`SIGNED_AMPLITUDE_PARITY_STRONGLY_IMPROVES_Q2_CALIBRATION_SCOPED`.

Signed five-point design `{-1,-1/2,0,1/2,1}` at the same 45-row count as the positive five-point comparator gives:

- Q2 `kappa=41.8259` versus `219.1476`;
- `smin=0.0439834` versus `0.0100762`;
- PN VIF `37.5094` versus `909.166`;
- direct Q2 PN variance improvement `19.273x`.

All three preregistered strong-information criteria pass.

Geometry remains collision-free with minimum separation `3 ell`; delete-one-label controls remain exact zero; `lambda=0` remains exact gravity null.

The pure `lambda tau` and `lambda^2 tau` nuisance columns are odd/even orthogonal on the symmetric design to numerical precision.

## FRONTIER EFFECT

Abstract calibration geometry is no longer the dominant operational blocker.

The next missing object is a device-level reversible transport implementation and error-transfer model validating that `lambda_A -> -lambda_A` is a physically controlled operation.

Recommended next action:

`EXPLICIT_REVERSIBLE_TRANSPORT_IMPLEMENTATION_MODEL_REQUIRED`.

Do not stack higher nuisance-polynomial degree without independent physical motivation.

No successor quantum residual, matching coefficient, quantum `chi_ABC`, new physics or parent promotion is authorized.
