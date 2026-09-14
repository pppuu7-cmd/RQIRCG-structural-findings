# SF032 — matched null-control common-mode calibration — PREOUTCOME PREREGISTRATION

Date: 2026-09-15
Inherited authoritative recovery head: `46069eef9c8526c090c945b5d3a8e76dd67602c9`.

## PURPOSE

Test whether an already-validated connected-null control can calibrate the dominant SF031 additive / `tau`-linear common-mode nuisances without assuming away any physical gravity contribution in the science rows.

This is a calibration-design gate. It does not add a successor quantum residual or choose any new dynamics.

## SCIENCE ROWS LOCK

Keep the exact SF030/SF031 9 science rows:

`R/ell in {60,160,400}` x `tau in {0.05,0.1,0.2}`.

Known science columns remain

`x_app=-Delta3 V_N(R) tau`,

`x_fb=[Delta3 A_N(R)/12] tau^3`,

`x_1PN=-epsilon_PN Delta3 V_static^1PN(R) tau`.

Keep the SF031 diagnostic grid

`epsilon_PN in {1e-2,1e-4,1e-6,1e-8}`.

## MATCHED NULL-CONTROL ROWS

Add one delete-A control row for every science `(R,tau)` row, for 9 additional rows.

The control uses the same apparatus topology, mass ratio, R value, tau value, recombination/readout bookkeeping and connected finite-difference convention, but the A branch displacement amplitude is prospectively set to zero.

By the exact delete-one-label controls already validated in SF028B/SF029,

`x_app=x_fb=x_1PN=0`

for these control rows at the retained known-physics order.

This zero is inherited physical/algebraic authority, not a fitted subtraction.

## NOISE MODEL

All 18 rows have independent Gaussian readout noise with the same frozen variance

`Cov(n)=sigma_y^2 I_18`.

As in SF031, `sigma_y` is dimensionless relative to the unspecified common phase scale `Phi0`.

No achieved detector noise is claimed.

## NUISANCE-SHARING HYPOTHESES

The gate tests four prospectively frozen models.

### S0 — science-only baseline

Use only the 9 science rows with science nuisance columns

`n0=1`, `n1=tau`.

This must reproduce SF031 model D.

### S1 — shared offset and shared tau-linear nuisance

Use all 18 rows. One common offset coefficient and one common `tau`-linear coefficient act identically on science and matched delete-A control rows.

This is the intended positive-control sharing hypothesis.

### S2 — shared offset only

Use all 18 rows. The offset coefficient is shared, but science and control have independent `tau`-linear nuisance coefficients.

### S3 — shared tau-linear only

Use all 18 rows. The `tau`-linear coefficient is shared, but science and control have independent offsets.

### S4 — no nuisance sharing negative control

Use all 18 rows, but give science and control independent offset and `tau`-linear nuisance coefficients.

The control rows must provide no material PN precision improvement beyond numerical roundoff in this model because their nuisance parameters are disconnected from science nuisance parameters.

## DESIGN-MATRIX CONVENTION

Science gravity columns are nonzero only on science rows.

All gravity columns are exactly zero on control rows.

Nuisance columns are populated according to S0-S4 above.

Rank is evaluated from a column-normalized SVD with threshold

`s_i/s_max > 1e-10`.

CRLB is evaluated through the normalized Gram matrix and then rescaled by physical column norms, exactly as in terminal SF031.

This avoids confusing small `epsilon_PN` with rank loss.

## OUTPUTS

For every `epsilon_PN` and model S0-S4 report:

- total rank versus number of columns;
- normalized condition number;
- PN `g_PN`;
- PN variance-inflation factor relative to SF031 iid science-only model A;
- `sigma_y,SNR1` and `sigma_y,SNR5`;
- improvement factor relative to S0:
  `I = Var_PN(S0)/Var_PN(Sx)`.

## PREDECLARED DECISION RULE

### CALIBRATION PASS

`MATCHED_NULL_CONTROL_BREAKS_COMMON_MODE_PN_NEAR_DEGENERACY_SCOPED`

if:

1. S1 remains full rank for every frozen epsilon;
2. `VIF_PN(S1) < 100` relative to SF031 iid model A;
3. S1 improves PN variance by at least a factor 100 relative to S0;
4. S4 gives no more than 1% variance improvement relative to S0.

### PARTIAL PASS

`NULL_CONTROL_PARTIALLY_CALIBRATES_COMMON_MODE_SCOPED`

if S1 is full rank and improves variance by >10 but fails either threshold 2 or 3.

### BLOCKED SHARING

`NULL_CONTROL_CALIBRATION_BLOCKED_BY_UNVALIDATED_SHARED_NUISANCE_MAP`

is an interpretation qualification that must be retained even after algebraic PASS: the mathematical benefit applies only when the nuisance coefficient is physically shared between the science and control configurations. This gate tests the consequence of that explicit hypothesis; it does not prove laboratory transferability.

### FAIL

`MATCHED_NULL_CONTROL_DOES_NOT_RESOLVE_PN_PRECISION_BOTTLENECK_SCOPED`

if S1 is rank deficient or improves PN variance by <=10.

### INVALID

`INVALID_NULL_CONTROL_OR_NUISANCE_OBJECT`

if science rows, control null identity, R/tau grid, epsilon grid, noise covariance, sharing definitions or thresholds change after evaluation.

## SHARING ABLATION INTERPRETATION

S2 and S3 determine which common-mode channel is responsible for any improvement.

Based on SF031, the `tau`-linear nuisance is expected to dominate, but this is a motivation, not a result.

## CLAIM CEILING

Even a calibration PASS establishes only a mathematical control-design mechanism under a shared-nuisance hypothesis.

It does not establish:

- that the nuisance is physically identical in the two laboratory configurations;
- achievable switching/calibration fidelity;
- detector feasibility;
- pulse/control equivalence;
- a successor residual;
- a quantum matching coefficient;
- GR-vs-QG discrimination;
- quantum `chi_ABC`;
- new physics.

Retain:

`CONTROL_CALIBRATION != PHYSICAL_TRANSFERABILITY`.

Retain:

`STRUCTURAL_IDENTIFIABILITY != ESTIMABILITY != FEASIBILITY`.

Theory track remains separately blocked on

`GENUINELY_NEW_MICROSCOPIC_MATCHING_PRINCIPLE_WITH_EXPLICIT_PHYSICAL_MAP_REQUIRED`.