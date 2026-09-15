# SF040 — triple-null cubic crosstalk localization — TERMINAL

Date: 2026-09-15
Preregistration: `bcbe70def315877ba5148f725d86444513f64cf1`.
Script: `scripts/sf040_checks.py`, commit `9dff4fbd9e2de8bc14044e600a764a90d6cb1c82`.
Canonical raw: `results/raw/SF040_CHECKS.json`, commit `763f1bea76494400018d5ed26cb60f67f20c6998`.

## RESULT / CLASSIFICATION

`TRIPLE_NULL_CONTROLS_LOCALIZE_LINEAR_CUBIC_CROSSTALK_SCOPED`.

Secondary:

`GRAVITY_NULL_CONTROLS_ALONE_IDENTIFY_LINEAR_ACTUATOR_DEPENDENT_CUBIC_CROSSTALK_SCOPED`.

No successor residual was fitted.

## Frozen crosstalk model

`zeta=zeta0+zeta_A lambda_A+zeta_B lambda_B+zeta_C lambda_C`.

Science:

`(lambda_A,1,1)`.

Null controls:

NA `(0,1,1)`,

NB `(lambda_A,0,1)`,

NC `(lambda_A,1,0)`.

The qubit register remains intact in every null configuration; only motional transport amplitudes are disabled.

## Exact inherited gravity null

SF038 already established exact delete-A/B/C connected known-gravity nulls over the signed amplitude grid with exact COM closure.

Therefore the NA/NB/NC rows are control-calibration channels with no retained connected Newtonian/feedback/1PN signal.

No gravity coefficient is estimated from those null rows.

## Full localization matrix

Using S+NA+NB+NC over the signed lambda/time grid, the normalized four-parameter control matrix has

`rank=4`,

`kappa=6.3751`,

with singular values

`(1.61327,1.00000,0.57735,0.25306)`.

Thus `zeta0,zeta_A,zeta_B,zeta_C` are structurally identifiable with moderate conditioning.

## Stronger null-only result

Using **only** NA+NB+NC rows and no science rows at all:

`rank=4`,

`kappa=5.9558`.

Therefore the frozen linear actuator-dependent cubic crosstalk can be calibrated entirely on gravitational-null channels before inspecting or fitting the science connected signal.

This is the most important operational result of SF040.

It yields the firewall:

`CROSSTALK CALIBRATION NEED NOT USE THE GRAVITY RESIDUAL`.

## Required negative controls

Science rows alone:

`rank=2`.

Science + NA only:

`rank=2`.

Science + NB only:

`rank=3`.

Science + NC only:

`rank=3`.

Thus the full-rank result genuinely requires the complementary null families; it is not an artifact of row count or time repetition.

## Exact difference identities

The frozen model gives

`zeta_S-zeta_NA=zeta_A lambda_A`,

`zeta_S-zeta_NB=zeta_B`,

`zeta_S-zeta_NC=zeta_C`.

After these are determined, `zeta0` is recovered redundantly from the null families.

No outcome-tuned coefficient is required.

## Mandatory pair-cross countermodel

For an extra term

`zeta_AB lambda_A lambda_B`,

its contribution to the three science-minus-null differences is

`S-NA: zeta_AB lambda_A`,

`S-NB: zeta_AB lambda_A`,

`S-NC: 0`.

Therefore it contaminates the simple `zeta_A` and `zeta_B` identities but leaves a characteristic signed-amplitude dependence in `S-NB` that is forbidden by the frozen linear model.

This countermodel is not absorbed into the SF040 fit. It is an explicit falsifier and motivates the next gate if pursued.

## Scientific interpretation

SF039 showed that ideal quadratic reversible transport itself produces no connected control phase.

SF040 now shows that if genuine cubic multilabel control crosstalk exists and depends linearly on actuator amplitudes, three exact gravitational-null configurations can identify it **without using the gravity-bearing science channel**.

This sharply reduces the risk of circular known-physics subtraction.

Retain:

`CONTROL_NUISANCE_CALIBRATION != GRAVITY_SIGNAL_FIT`.

## Exact next admissible direction

The only preregistered countermodel exposed by SF040 is minimal pairwise actuator cross-dependence such as

`zeta_AB lambda_A lambda_B`, `zeta_AC lambda_A lambda_C`, `zeta_BC lambda_B lambda_C`.

A high-information successor may test whether the same triple-null/signed-amplitude architecture identifies these pair-cross terms. Do not jump to arbitrary higher polynomial degree.

Recommended gate:

`SF041_PAIRWISE_ACTUATOR_CROSS_CROSSTALK_LOCALIZATION_PREOUTCOME_GATE`.

## Claim ceiling

SF040 establishes no actual device crosstalk magnitude, achieved control precision, detector feasibility, higher-order actuator model, successor quantum residual, quantum matching coefficient, GR-vs-QG discriminator, quantum `chi_ABC` or new physics.
