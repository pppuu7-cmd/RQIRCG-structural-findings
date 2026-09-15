# SF037 — noise-aware Q2 control calibration estimability — PREOUTCOME

Date: 2026-09-15
Parent recovery: `9f31f98d767e71461012d3590828b1eda460dad0`.

## PURPOSE

Quantify the phase-precision cost of jointly estimating the ordinary known-gravity `C3` basis and the SF036 quadratic connected control-phase nuisance on the exact frozen five-point amplitude design.

This gate tests estimability only. It does not introduce a detector model or successor residual.

## FROZEN DESIGN

Use exactly the SF036 rows:

`lambda_A in {0,1/4,1/2,3/4,1}`,

`R/ell in {60,160,400}`,

`tau in {0.05,0.1,0.2}`,

45 rows total.

Use the exact SF036 known-gravity coefficient table and no new geometry.

## FROZEN STATISTICAL MODEL

Independent homoscedastic phase noise:

`y = X beta + epsilon`,

`Cov(epsilon)=sigma_y^2 I`.

No correlated noise, no offset beyond the explicit Q2 control nuisance, no detector floor and no shot-count model.

## PARAMETER MODELS

### K3 — ideal known-only reference

Columns:

`[x_app,x_fb,epsilon_PN*x_1PN]`.

### M0 — amplitude-independent connected control phase

Columns:

`[x_app,x_fb,epsilon_PN*x_1PN,x_z0]`.

### L1 — linear amplitude dependence

Columns:

`[x_app,x_fb,epsilon_PN*x_1PN,x_z0,x_z1]`.

### Q2 — quadratic amplitude dependence

Columns:

`[x_app,x_fb,epsilon_PN*x_1PN,x_z0,x_z1,x_z2]`.

with

`x_z0=tau`,

`x_z1=lambda_A tau`,

`x_z2=lambda_A^2 tau`.

The control nuisance coefficients are not multiplied by `epsilon_PN`.

## FROZEN EPSILON DIAGNOSTICS

`epsilon_PN in {1e-4,1e-6,1e-8}`.

The exact Fisher-rank structure cannot change for nonzero epsilon; these values test the expected small-signal scaling.

## NUMERICAL PROCEDURE

Use stable column scaling before Gram inversion. Rank is evaluated on the column-normalized shape matrix with tolerance `1e-10*s_max`.

For each model compute:

- rank;
- normalized condition number;
- PN CRLB variance coefficient;
- PN variance-inflation factor relative to K3 on the same 45 rows;
- largest `sigma_y` giving nominal PN SNR 1 for `alpha_1PN=1`;
- `sigma_y,SNR1 / epsilon_PN` scaling constant.

## THREE-POINT Q2 COMPARATOR

Recompute the Q2 Fisher result on the inherited SF035 amplitude subset

`lambda_A in {0,1/2,1}`

with the same R/T grid and noise model.

Record the ratio of PN variance between three-point and five-point Q2 designs.

## FROZEN PENALTY BANDS

Relative to K3 on the same five-point rows:

- `LOW`: VIF <= 10;
- `MODERATE`: 10 < VIF <= 100;
- `HIGH`: 100 < VIF <= 1e4;
- `EXTREME`: VIF > 1e4.

These labels describe statistical geometry only, not feasibility.

## DECISION RULE

### PASS

`Q2_CONTROL_PHASE_AND_1PN_JOINTLY_ESTIMABLE_SCOPED`

if Q2 is full rank for all nonzero epsilon diagnostics and has finite PN CRLB.

### QUALIFICATION

Append the frozen penalty band and the five-point versus three-point variance-improvement factor.

### DEGENERATE

`Q2_CONTROL_PHASE_MAKES_1PN_UNIDENTIFIABLE_SCOPED`

only if the full Q2 Fisher/design matrix is rank deficient.

### INVALID

Any post-result addition/removal of nuisance columns, amplitude points, R/tau rows, epsilon values or noise correlations requires a new preregistration.

## INTERPRETATION CEILING

A finite CRLB establishes a required dimensionless phase precision relative to the unspecified SF031 phase scale `Phi0`; it does not establish that a laboratory can achieve it.

No successor quantum residual, detector technology, repetition count, matching coefficient, quantum `chi_ABC`, new physics or parent promotion is authorized.

Retain:

`ESTIMABILITY != FEASIBILITY`.
