# SF042 — double-null pair-cross crosstalk closure — TERMINAL

Date: 2026-09-15
Preregistration: `de70e9ca001611ce6f3ab63bc460b045ee187d3d`.

## RESULT / CLASSIFICATION

`DOUBLE_NULL_CLOSES_PAIR_CROSS_CROSSTALK_MODEL_SCOPED`.

Secondary stronger result:

`GRAVITY_NULL_CONTROLS_ALONE_CLOSE_PAIR_CROSS_CROSSTALK_MODEL_SCOPED`.

No successor residual was introduced.

## Frozen seven-parameter model

`zeta = zeta0 + zeta_A lambda_A + zeta_B lambda_B + zeta_C lambda_C`
`       + zeta_AB lambda_A lambda_B + zeta_AC lambda_A lambda_C + zeta_BC lambda_B lambda_C`.

The only new configuration relative to SF041 was

`NBC=(lambda_A,0,0)`.

No further null family or nuisance term was added.

## Full S+NA+NB+NC+NBC result

Exact algebraic rank:

`7/7`.

Column-normalized singular values:

`(1.80029,1.51022,0.707107,0.608294,0.577350,0.468213,0.235775)`.

Normalized condition number:

`kappa=7.63564`.

The exact nullspace is empty.

Thus the single prospectively identified double-null lever removes the complete SF041 one-dimensional degeneracy with moderate conditioning.

## Null-only stronger result

Using no science rows and only

`NA+NB+NC+NBC`

gives

`rank=7/7`,

`kappa=5.82843`.

Therefore all seven single- and pair-actuator cubic crosstalk coefficients can be structurally calibrated using **only connected-gravity-null channels** in the frozen model.

This establishes the strong firewall:

`PAIR-CROSS CROSSTALK CALIBRATION DOES NOT REQUIRE A GRAVITY-BEARING SCIENCE FIT`.

## Required SF041 reproduction

Removing NBC and restoring exactly S+NA+NB+NC reproduces

`rank=6`

and the SF041 unresolved direction

`(1,0,-1,-1,0,0,1)`.

Thus the rank closure is genuinely caused by the new double-null lever rather than a changed tolerance or implementation.

## Leave-one-configuration audit

From the five-family full design:

- drop S: rank 7, `kappa=5.82843`;
- drop NA: rank 7, `kappa=5.82843`;
- drop NB: rank 6;
- drop NC: rank 6;
- drop NBC: rank 6.

Therefore NB, NC and NBC are essential to the frozen pair-cross closure.

S and NA are algebraically redundant with respect to rank when the other four families are present, but NA is required if one wants a calibration set composed entirely of gravity-null channels.

## Scientific interpretation

SF040 showed that one-body nulls completely calibrate a linear single-actuator dependence.

SF041 found the exact one-dimensional ambiguity introduced by pair-cross actuator terms.

SF042 now closes that ambiguity with the minimum preregistered double-null lever.

The resulting operational architecture is overdetermined and does not use a fitted gravity residual to define nuisance coefficients.

This is a substantially stronger calibration structure than the generic common-mode assumption that motivated SF031–SF033.

## Operational frontier

Within the now-explicit quadratic reversible transport + linear/pair-cross cubic-crosstalk class, structural nuisance identifiability is closed.

Further polynomial expansion without independent physical motivation would have low information value.

The next missing empirical object is

`DEVICE_LEVEL_NONLINEAR_CROSSTALK_MAGNITUDE_AND_STABILITY_DATA_REQUIRED`.

A future experiment/device model must provide actual bounds or measurements for the connected nonlinear control coefficients and verify stability across the null/science schedule.

This is not obtainable from the current abstract protocol alone.

## Claim ceiling

SF042 establishes no actual device crosstalk value, detector sensitivity, achievable calibration precision, higher-order actuator completeness, successor quantum residual, quantum matching coefficient, GR-vs-QG discriminator, quantum `chi_ABC` or new physics.

Retain:

`STRUCTURAL_CONTROL_CLOSURE != DEVICE_VALIDATION`.

Retain:

`KNOWN_PHYSICS_SUBTRACTION != QUANTUM_RESIDUAL_AUTHORITY`.
