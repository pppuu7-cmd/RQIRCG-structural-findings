# RQIRCGSF research ledger — SF031 addendum

Date: 2026-09-15

## STATE_READ

Inherited recovery head: `2c01c39dcf0bd133b6030aa1b3868aa54f810d22`.

Inherited operational authority: SF030 `KNOWN_PHYSICS_COHERENCE_COMPONENTS_STRUCTURALLY_IDENTIFIABLE_SCOPED`.

## TARGET_GATE

`SF031_NOISE_AWARE_KNOWN_BASELINE_ESTIMABILITY_PREOUTCOME_GATE`.

## PREREG

`f825f57e4a57b47effed68e34d2ab747a4881d15`.

Frozen statistical models:

A. iid homoscedastic phase noise;
B. A + common additive offset;
C. A + global R-independent `tau`-linear phase nuisance;
D. A + both nuisances.

Frozen diagnostic `epsilon_PN` values:

`{1e-2,1e-4,1e-6,1e-8}`.

## IMPLEMENTATION AUDIT

A preliminary unnormalized-SVD rank check was identified as numerically invalid before terminalization because shrinking a nonzero PN column by nonzero `epsilon_PN` cannot change exact mathematical rank.

Stable execution instead uses column-normalized SVD for rank/shape conditioning and rescaled normalized-Gram CRLB evaluation. This changed no scientific object, design point, nuisance model or decision threshold.

Stable script:

`aa8313baf931b4b390ac81c4853647d5cca95c5a`.

Canonical raw:

`18342c91acfbc89e235c3994e0b19859cbc6a2da`.

## RESULT

Terminal:

`ac0ec512a109c51ae7fbee2f9006548d05fac5bc`.

Primary:

`PN_CALIBRATION_REMAINS_ESTIMABLE_UNDER_FROZEN_COMMON_MODE_NUISANCES_SCOPED`.

Secondary:

`COMMON_MODE_NUISANCE_STRONGLY_INFLATES_PN_PRECISION_SCOPED`.

Localization:

`TAU_LINEAR_COMMON_MODE_NEAR_DEGENERACY_DOMINATES_PN_PRECISION_SCOPED`.

All A-D models remain full normalized rank for every frozen `epsilon_PN`.

Normalized condition numbers:

A `5.566`, B `20.258`, C `1007.65`, D `1113.46`.

PN variance-inflation factors:

A `1`, B `11.695`, C `~2.1341e4`, D `~2.1341e4`.

Required dimensionless per-row SNR1 phase-noise ceilings scale exactly linearly with `epsilon_PN`:

A `3.0893e-4 epsilon_PN`,

B `9.0335e-5 epsilon_PN`,

C/D `2.1147e-6 epsilon_PN`.

These are precision targets in units of an unspecified common phase scale, not achieved laboratory sensitivities.

## CLAIM_CEILING

`STRUCTURAL_IDENTIFIABILITY != ESTIMABILITY != FEASIBILITY`.

No detector technology, laboratory feasibility, successor residual, quantum matching coefficient, quantum `chi_ABC`, or new physics.

## NEXT

Operational:

`SF032_NULL_CONTROL_COMMON_MODE_CALIBRATION_PREOUTCOME_GATE`.

Theory remains independently blocked on:

`GENUINELY_NEW_MICROSCOPIC_MATCHING_PRINCIPLE_WITH_EXPLICIT_PHYSICAL_MAP_REQUIRED`.