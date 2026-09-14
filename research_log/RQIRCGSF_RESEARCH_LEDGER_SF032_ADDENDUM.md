# RQIRCGSF research ledger — SF032 addendum

Date: 2026-09-15

## STATE_READ

Inherited recovery head: `46069eef9c8526c090c945b5d3a8e76dd67602c9`.

Inherited bottleneck: SF031 `TAU_LINEAR_COMMON_MODE_NEAR_DEGENERACY_DOMINATES_PN_PRECISION_SCOPED`.

## TARGET_GATE

`SF032_NULL_CONTROL_COMMON_MODE_CALIBRATION_PREOUTCOME_GATE`.

## PREREG

`66e7b301200ca7b450f0bba38b4edce872166762`.

Matched delete-A null-control rows were frozen before evaluation.

## EXECUTION

Script: `bc6b7c4c723c1fb3334679180d0793b55c56763b`.

Canonical raw: `bf0b266f54a1f19153d1b19a5dcbba09e8278e66`.

## RESULT

Terminal: `e8dc5ca051e5f5c8669d6a0a1fe99e6c93b1ff4e`.

Primary:

`MATCHED_NULL_CONTROL_BREAKS_COMMON_MODE_PN_NEAR_DEGENERACY_SCOPED`.

Mandatory qualification:

`NULL_CONTROL_CALIBRATION_BLOCKED_BY_UNVALIDATED_SHARED_NUISANCE_MAP`.

Key result:

- SF031 science-only offset+tau nuisance: PN VIF `~2.1341e4`;
- shared matched null control: VIF `1.658`;
- variance improvement `~1.2870e4`;
- shared offset only: essentially no improvement;
- shared tau-linear only: improvement `~1.7339e3`;
- no-sharing negative control: no improvement to numerical precision.

The algebraic calibration mechanism is therefore real and specifically targets the tau-linear nuisance direction, but physical science/control nuisance transferability is not yet derived.

## CLAIM_CEILING

`CONTROL_CALIBRATION != PHYSICAL_TRANSFERABILITY`.

No detector feasibility, pulse fidelity, successor residual, quantum matching coefficient, quantum `chi_ABC`, or new physics.

## NEXT

Operational:

`SF033_SCIENCE_NULL_CONTROL_NUISANCE_TRANSFERABILITY_PREOUTCOME_GATE`.

Theory remains independently blocked on:

`GENUINELY_NEW_MICROSCOPIC_MATCHING_PRINCIPLE_WITH_EXPLICIT_PHYSICAL_MAP_REQUIRED`.