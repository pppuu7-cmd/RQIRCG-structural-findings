# RQIRCGSF research ledger — SF039 through SF042 addendum

Date: 2026-09-15

## SF039 — reversible harmonic transport

Preregistration: `de31d7e3c6c6bbd97045709ff032e7f6a951f98d`.

Derivation/source notes: `6bbc2cf28ee6d65bea52ab4bdab5d2a71caf06aa`.

Terminal: `92b84b7e65c3fac26796b7b7fe04d529f3104bf5`.

Classification:

`QUADRATIC_REVERSIBLE_TRANSPORT_GENERATES_NO_CONNECTED_CONTROL_PHASE_SCOPED`.

Key theorem: forced-harmonic control phases are at most quadratic in branch-programmed displacements; with linear Boolean drives and the common recoil body, the complete ideal transport phase contains no `abc` monomial, hence exact `Delta3=0`.

## SF040 — triple-null single-actuator cubic-crosstalk localization

Preregistration: `bcbe70def315877ba5148f725d86444513f64cf1`.

Script: `9dff4fbd9e2de8bc14044e600a764a90d6cb1c82`.

Raw: `763f1bea76494400018d5ed26cb60f67f20c6998`.

Terminal: `daeedf7e765eb9ae767492ea6f8df2ae6f8e513f`.

Classification:

`TRIPLE_NULL_CONTROLS_LOCALIZE_LINEAR_CUBIC_CROSSTALK_SCOPED`.

Full S+NA+NB+NC rank 4, `kappa=6.375`.

Stronger: null-only NA+NB+NC rank 4, `kappa=5.956`.

Thus the four linear actuator-dependence coefficients can be calibrated without using gravity-bearing science rows.

## SF041 — pair-cross stress test

Preregistration: `1127a7a774aeab6e33c27f3a0532f32068f35fd2`.

Terminal: `0502125168c6ba09c4d4f5f70ec68df058ded2bb`.

Classification:

`TRIPLE_NULL_PAIR_CROSS_CROSSTALK_HAS_ONE_UNRESOLVED_DIRECTION_SCOPED`.

Seven-parameter model rank 6. Exact null vector:

`(1,0,-1,-1,0,0,1)`

in parameter order `[zeta0,zeta_A,zeta_B,zeta_C,zeta_AB,zeta_AC,zeta_BC]`.

This prospectively identified the missing double-null lever `B=C=0`.

## SF042 — minimum double-null repair

Preregistration: `de70e9ca001611ce6f3ab63bc460b045ee187d3d`.

Terminal: `27a249ce8c4741ce0b4e5768a5b091b2301620b0`.

Classifications:

`DOUBLE_NULL_CLOSES_PAIR_CROSS_CROSSTALK_MODEL_SCOPED`.

`GRAVITY_NULL_CONTROLS_ALONE_CLOSE_PAIR_CROSS_CROSSTALK_MODEL_SCOPED`.

Adding only `NBC=(lambda_A,0,0)` gives full seven-parameter rank 7, `kappa=7.636`.

Null-only NA+NB+NC+NBC is also rank 7 with `kappa=5.828`.

Removing NBC reproduces SF041 rank 6 exactly.

## Frontier effect

Within the explicit quadratic reversible transport plus linear/pair-cross connected cubic-crosstalk model, structural calibration can be completed entirely on gravity-null channels.

The remaining operational object is empirical/device-level:

`DEVICE_LEVEL_NONLINEAR_CROSSTALK_MAGNITUDE_AND_STABILITY_DATA_REQUIRED`.

Do not continue arbitrary higher actuator polynomial degree without independent physical motivation.

Theory track remains separately blocked on

`GENUINELY_NEW_MICROSCOPIC_MATCHING_PRINCIPLE_WITH_EXPLICIT_PHYSICAL_MAP_REQUIRED`.
