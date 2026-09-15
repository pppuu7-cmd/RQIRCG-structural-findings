# SF037 — noise-aware Q2 control calibration estimability — TERMINAL

Date: 2026-09-15
Preregistration: `2e5107a94fa0588e9ec190a1245f5056dcef0c2a`.
Script: `scripts/sf037_checks.py`, commit `76d97a2d5275315b09e6f55a266dac1f04257149`.
Canonical raw: `results/raw/SF037_CHECKS.json`, commit `e5928128f27a87fb75b61c0e14e9660d2dc3781d`.
Script SHA-256: `91fc234eb3cbccc7fce40d62daa31477aebb8031846135f6b86b648b93677c29`.

## RESULT / CLASSIFICATION

`Q2_CONTROL_PHASE_AND_1PN_JOINTLY_ESTIMABLE_SCOPED`.

Frozen precision penalty band:

`HIGH`.

Secondary design result:

`FIVE_POINT_AMPLITUDE_LADDER_IMPROVES_Q2_PN_VARIANCE_BY_22_9X_SCOPED`.

No successor quantum residual was introduced or fitted.

## Frozen statistical object

45 rows:

`lambda_A={0,1/4,1/2,3/4,1}`

x

`R/ell={60,160,400}`

x

`tau={0.05,0.1,0.2}`.

Noise model:

`Cov(epsilon)=sigma_y^2 I`.

The physical PN column is multiplied by nonzero `epsilon_PN`; the control nuisance columns are not.

## Rank and normalized conditioning

All four frozen parameter models remain full rank for all nonzero epsilon diagnostics.

Known-only K3:

`rank=3`, `kappa=5.544`.

M0 amplitude-independent cubic control phase:

`rank=4`, `kappa=6.510`.

L1 linear amplitude dependence:

`rank=5`, `kappa=24.847`.

Q2 quadratic amplitude dependence:

`rank=6`, `kappa=219.148`.

Thus Q2 does not make the 1PN coefficient algebraically unidentifiable.

## PN variance inflation

Relative to the known-only K3 model on the same 45 rows:

M0:

`VIF_PN = 1.2069`.

L1:

`VIF_PN = 10.4205`.

Q2:

`VIF_PN = 909.166`.

Under the preregistered bands, Q2 is `HIGH` penalty rather than `EXTREME`.

This is a large statistical cost, but it is finite and far below the uncalibrated generic tau-linear science-only penalty found in SF031 (`~2.13e4`).

## Required dimensionless phase precision

For nominal `alpha_1PN=1`, the maximum iid phase-noise scale for PN SNR 1 is

Known-only K3:

`sigma_y,SNR1 = 3.81027e-4 epsilon_PN`.

M0:

`3.46826e-4 epsilon_PN`.

L1:

`1.18035e-4 epsilon_PN`.

Q2:

`1.26367e-5 epsilon_PN`.

The ratio `sigma_y,SNR1/epsilon_PN` is constant across `epsilon_PN={1e-4,1e-6,1e-8}` to numerical precision, confirming the expected small-signal scaling.

For example, at diagnostic `epsilon_PN=1e-6`, Q2 requires

`sigma_y <= 1.26367e-11`

for nominal SNR 1 relative to the still-unspecified phase scale `Phi0`.

This is a requirement, not an achieved detector sensitivity.

## Five-point versus three-point Q2

The inherited three-point Q2 design gives

`sigma_y,SNR1/epsilon_PN = 2.63970e-6`.

The five-point design gives

`1.26367e-5`.

Equivalently, PN variance improves by

`22.917x`

when the prospectively fixed `1/4` and `3/4` amplitude rows are added.

Thus the SF036 structural information gain converts into a substantial statistical precision gain.

## Relation to earlier calibration limits

SF031 generic science-only time-linear nuisance:

required SNR1 coefficient `~2.1147e-6 epsilon_PN`.

SF032 ideal perfectly shared matched-null control:

`~2.39905e-4 epsilon_PN`.

SF037 Q2 five-point self-calibration:

`~1.26367e-5 epsilon_PN`.

Therefore the explicit amplitude-ladder strategy performs much better than leaving the time-linear nuisance unconstrained, but remains substantially worse than the ideal perfectly shared null-control model.

This is the expected cost of allowing nonzero `zeta1` and `zeta2` rather than assuming exact M0 sharing.

## Scientific interpretation

The operational calibration hierarchy is now quantitative:

`M0 exact sharing` -> near-ideal PN precision;

`L1 amplitude dependence` -> modest-to-moderate precision cost;

`Q2 amplitude curvature` -> high but finite precision cost;

`generic uncalibrated tau-linear science nuisance` -> much larger cost.

The quadratic nuisance is therefore a **precision problem**, not an exact identifiability obstruction, on the frozen five-point/R/T design.

Retain:

`ESTIMABILITY != FEASIBILITY`.

## Highest-information next operational direction

The remaining Q2 penalty is driven by the same 1PN-versus-amplitude-curvature near-null direction identified in SF035/SF036.

A high-information next gate may test a prospectively symmetric signed-displacement control family, where reversal of the A transport direction provides an odd/even amplitude lever on `zeta1` versus `zeta2` while the exact known-gravity basis is recomputed for the signed geometry.

No signed-amplitude result is authorized until separately preregistered.

## Claim ceiling

SF037 establishes no achieved laboratory sensitivity, repetition requirement, detector technology, device stability, higher-than-quadratic nuisance bound, successor quantum residual, quantum matching coefficient, GR-vs-QG discriminator, quantum `chi_ABC` or new physics.
