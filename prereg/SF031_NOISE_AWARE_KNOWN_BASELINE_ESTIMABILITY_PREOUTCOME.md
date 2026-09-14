# SF031 — noise-aware known-baseline estimability — PREOUTCOME PREREGISTRATION

Date: 2026-09-15
Inherited authoritative recovery head: `2c01c39dcf0bd133b6030aa1b3868aa54f810d22`.

## PURPOSE

Quantify the phase-precision requirement for estimating the already-known 1PN calibration amplitude in the frozen SF030 multi-R/multi-T design, and adversarially test whether simple common-mode calibration nuisances destroy that estimability.

This gate does not claim a detector can achieve the required precision. It derives the requirement under explicitly frozen statistical models.

No successor quantum residual or matching coefficient is allowed.

## INHERITED PHYSICAL / DESIGN OBJECT

Keep the same 9 SF030 phase rows:

`R/ell in {60,160,400}` x `tau in {0.05,0.1,0.2}`.

Keep the physical known basis:

`x_app = -Delta3 V_N(R) tau`,

`x_fb = [Delta3 A_N(R)/12] tau^3`,

`x_1PN = -epsilon_PN Delta3 V_static^1PN(R) tau`.

Unknown calibration coordinates are

`alpha=(alpha_app,alpha_fb,alpha_1PN)`

with nominal known-physics value `(1,1,1)`.

## DIMENSIONLESS NOISE CONVENTION

Write the physical phase as

`Theta3 = Phi0 * y_tilde`,

where `Phi0` is the common Newtonian phase scale inherited from the dimensional normalization of the SF028B/SF029 formulas.

The statistical model is written for `y_tilde`.

`noise sigma_y` therefore means a per-row phase standard deviation in units of `Phi0`.

The corresponding dimensional phase requirement is simply

`sigma_Theta = Phi0 sigma_y`.

No value of `Phi0`, source mass, separation or laboratory noise is selected in this gate.

## FROZEN EPSILON_PN DIAGNOSTICS

Evaluate

`epsilon_PN in {1e-2,1e-4,1e-6,1e-8}`.

These are dynamic-range controls, not asserted laboratory parameters.

## FROZEN STATISTICAL MODEL A — iid control

Assume independent zero-mean Gaussian phase noise with common variance

`Cov(n)=sigma_y^2 I_9`.

For design matrix `A`, Fisher information is

`F=A^T A/sigma_y^2`.

If full rank, the Cramer-Rao covariance is

`Cov(theta_hat) >= sigma_y^2 (A^T A)^-1`.

For `alpha_1PN`, define

`g_PN = sqrt([(A^T A)^-1]_(PN,PN))`.

Then

`std(alpha_1PN) >= sigma_y g_PN`.

Report the maximum per-row noise scale compatible with nominal `alpha_1PN=1` at

- `SNR=1`: `sigma_y,1 = 1/g_PN`;
- `SNR=5`: `sigma_y,5 = 1/(5 g_PN)`.

These are required precisions under the frozen idealized model, not achieved precisions.

## FROZEN NUISANCE ADVERSARIES

Repeat the Fisher/rank calculation with the following additional unpenalized nuisance columns.

### B — additive common offset

Add one column

`n0(R,tau)=1`.

This represents an unknown additive phase calibration offset common to all nine rows.

### C — global tau-linear common mode

Add one column

`n1(R,tau)=tau`.

This represents an R-independent phase term linear in interaction time, e.g. a generic residual common clock/control phase at the level of this abstract calibration audit.

It is an adversarial nuisance template, not a claim that such a systematic exists.

### D — both nuisances

Add both `1` and `tau` columns.

For every model A-D, report:

- total design rank;
- condition number after independently normalizing every included column;
- `g_PN` if full rank;
- `sigma_y,1` and `sigma_y,5`;
- variance-inflation factor relative to model A:
  `VIF_PN = g_PN^2 / g_PN,A^2`.

## PREDECLARED DECISION RULE

### PASS

`PN_CALIBRATION_REMAINS_ESTIMABLE_UNDER_FROZEN_COMMON_MODE_NUISANCES_SCOPED`

if models A-D are all full column rank for every frozen `epsilon_PN`.

### CALIBRATION DEGENERACY

`PN_CALIBRATION_DEGENERATE_WITH_FROZEN_COMMON_MODE_SCOPED`

if any nuisance model makes the PN amplitude nonidentifiable / matrix rank deficient.

### STRONG NUISANCE PENALTY

Independently record

`COMMON_MODE_NUISANCE_STRONGLY_INFLATES_PN_PRECISION_SCOPED`

if the full-rank model D has

`VIF_PN > 10`

for any frozen `epsilon_PN`.

The threshold 10 is frozen before evaluation.

A strong penalty does not change PASS into scientific failure if rank remains full; it is a precision warning.

### INVALID

`INVALID_STATISTICAL_OBJECT_OR_DESIGN`

if the R/tau rows, known-physics columns, epsilon grid, nuisance templates, noise covariance or decision rule change after evaluation.

## REQUIRED SCALING AUDIT

Check whether `sigma_y,1` and `sigma_y,5` scale linearly with `epsilon_PN` once the PN column is the limiting small-amplitude direction.

Do not fit an experimental noise floor.

## REQUIRED INTERPRETATION FIREWALL

A finite CRLB does not imply practical measurability.

`STRUCTURAL IDENTIFIABILITY != ESTIMABILITY != FEASIBILITY`.

This gate supplies only a precision target under the frozen abstract noise/correlation models.

No residual after known-baseline calibration may be called quantum gravity without a separately selected successor law and a new prospectively frozen residual model.

## CLAIM CEILING

No detector technology, shot-noise model, integration time, repetition count, metrology platform, laboratory mass/length scale, successor quantum coefficient, GR-vs-QG discriminator, quantum `chi_ABC`, or new physics is selected or established.

Theory track remains separately blocked on

`GENUINELY_NEW_MICROSCOPIC_MATCHING_PRINCIPLE_WITH_EXPLICIT_PHYSICAL_MAP_REQUIRED`.