# SF031 — noise-aware known-baseline estimability — TERMINAL

Date: 2026-09-15
Preregistration: `f825f57e4a57b47effed68e34d2ab747a4881d15`.
Stable execution script: `scripts/sf031_checks.py`, commit `aa8313baf931b4b390ac81c4853647d5cca95c5a`.
Canonical raw: `results/raw/SF031_CHECKS.json`, commit `18342c91acfbc89e235c3994e0b19859cbc6a2da`.

## RESULT / CLASSIFICATION

`PN_CALIBRATION_REMAINS_ESTIMABLE_UNDER_FROZEN_COMMON_MODE_NUISANCES_SCOPED`

Secondary:

`COMMON_MODE_NUISANCE_STRONGLY_INFLATES_PN_PRECISION_SCOPED`

Additional structural localization:

`TAU_LINEAR_COMMON_MODE_NEAR_DEGENERACY_DOMINATES_PN_PRECISION_SCOPED`.

No successor quantum component was introduced or fitted.

## Frozen statistical object

The exact SF030 9-row design is retained:

`R/ell={60,160,400}` x `tau={0.05,0.1,0.2}`.

The known-physics columns are

`x_app=-Delta3 V_N(R) tau`,

`x_fb=[Delta3 A_N(R)/12] tau^3`,

`x_1PN=-epsilon_PN Delta3 V_static^1PN(R) tau`.

The frozen diagnostic weak-field values are

`epsilon_PN in {1e-2,1e-4,1e-6,1e-8}`.

Four statistical models were prospectively frozen:

A. iid homoscedastic phase noise;
B. A plus unknown additive common offset `1`;
C. A plus unknown R-independent `tau`-linear common mode;
D. A plus both nuisances.

Noise is expressed as a dimensionless per-row standard deviation `sigma_y` relative to a common phase scale `Phi0`. No laboratory value of `Phi0` is selected.

## Pre-terminal numerical-rank correction

A preliminary implementation attempted to infer rank from an **unnormalized** SVD of the physical matrix. For very small `epsilon_PN`, numerical tolerance then incorrectly mimicked rank loss because the PN column is small in norm.

This was rejected before any terminal scientific classification.

Multiplying a nonzero column by nonzero `epsilon_PN` cannot change exact mathematical rank. The stable implementation therefore uses the preregistered column-normalized SVD for rank/shape conditioning and computes the CRLB through the normalized Gram matrix with exact column rescaling.

No scientific design point, nuisance column, PASS rule or physical coefficient was changed.

This is an implementation/numerical-conditioning correction, not a changed scientific hypothesis.

## Rank result

All four nuisance models remain full column rank for every frozen `epsilon_PN`.

Normalized ranks are:

- A: `rank=3`;
- B: `rank=4`;
- C: `rank=4`;
- D: `rank=5`.

Therefore the preregistered degeneracy verdict is **not** triggered.

The PN amplitude remains algebraically estimable in the exact frozen design even after the two common-mode nuisance columns are included.

## Normalized conditioning

Because the normalized shape matrices do not depend on the nonzero scale `epsilon_PN`, the normalized condition numbers are constant across the diagnostic epsilon grid:

- A iid: `kappa=5.565925`;
- B + offset: `kappa=20.257799`;
- C + global `tau`-linear mode: `kappa=1007.650209`;
- D + offset + `tau`-linear mode: `kappa=1113.462549`.

Thus the additive offset is a moderate nuisance, whereas the R-independent `tau`-linear mode produces an extremely near-degenerate geometry.

The degeneracy is not exact because the physical 1PN column has nontrivial R dependence inherited from the finite apparatus. But the remaining R lever arm is weak enough that precision requirements increase sharply.

## PN variance inflation

Relative to iid model A, the PN variance-inflation factors are

- A: `VIF=1`;
- B: `VIF=11.6952`;
- C: `VIF=2.13413e4`;
- D: `VIF=2.13413e4`.

Therefore the predeclared strong-penalty threshold `VIF>10` is exceeded decisively.

The `tau`-linear nuisance alone accounts for essentially all of the large penalty. Adding the constant offset on top of it changes the PN variance only at a negligible relative level in this design.

This yields the scoped structural result:

`TAU_LINEAR_COMMON_MODE_NEAR_DEGENERACY_DOMINATES_PN_PRECISION_SCOPED`.

## Precision requirement

Let nominal `alpha_1PN=1`. The CRLB gives the largest dimensionless per-row noise compatible with unit nominal PN signal-to-noise as

`sigma_y,SNR1 = epsilon_PN * q_model`,

where the prospectively derived constants are

- A: `q_A = 3.08928556e-4`;
- B: `q_B = 9.03345143e-5`;
- C: `q_C = 2.11469516e-6`;
- D: `q_D = 2.11469516e-6`.

For nominal SNR 5, divide these values by five.

For example, at diagnostic `epsilon_PN=1e-6`:

- A requires `sigma_y <= 3.0893e-10` for SNR 1;
- B requires `sigma_y <= 9.0335e-11`;
- C/D require `sigma_y <= 2.1147e-12`.

At `epsilon_PN=1e-8`, model D requires

`sigma_y <= 2.1147e-14` for SNR 1

and

`sigma_y <= 4.2294e-15` for SNR 5.

These are **requirements in units of the unspecified common phase scale `Phi0`**, not statements that any laboratory can achieve them.

## Scaling audit

The quantity

`sigma_y,SNR1 / epsilon_PN`

is constant across all four frozen epsilon values for each nuisance model to numerical precision.

Therefore the expected linear small-signal scaling is explicitly verified:

`required phase noise ~ epsilon_PN`.

This is a precision-target scaling, not a detector model.

## Scientific meaning

SF030 established

`STRUCTURAL IDENTIFIABILITY`.

SF031 now shows that this does **not** imply easy estimation.

The finite-R geometry technically breaks the PN versus common-`tau` exact degeneracy, but only weakly. An uncalibrated R-independent time-linear phase therefore creates an approximately four-orders-of-magnitude variance penalty.

This identifies the next information bottleneck more sharply than generic 'noise':

`COMMON_TAU_LINEAR_PHASE_CALIBRATION`.

Simply reducing iid readout noise while leaving this nuisance unconstrained is an inefficient strategy.

The higher-information next step is to ask whether an independently measurable null/control channel can calibrate the common `tau`-linear nuisance without also subtracting the physical connected gravity components.

## Interpretation firewalls

Retain:

`STRUCTURAL_IDENTIFIABILITY != ESTIMABILITY != FEASIBILITY`.

Retain:

`IDENTIFIABILITY != DYNAMICS`.

A finite Fisher matrix does not establish an achievable detector precision.

No residual after fitting/calibration is authorized as quantum gravity.

## Claim ceiling

SF031 establishes no:

- laboratory phase sensitivity;
- shot-noise/repetition-time requirement;
- detector technology;
- experimental feasibility;
- exact all-time dynamics;
- successor quantum law;
- quantum matching coefficient;
- GR-vs-QG discriminator;
- quantum `chi_ABC`;
- new physics.

Theory track remains independently blocked on

`GENUINELY_NEW_MICROSCOPIC_MATCHING_PRINCIPLE_WITH_EXPLICIT_PHYSICAL_MAP_REQUIRED`.

## Exact next admissible operational gate

`SF032_NULL_CONTROL_COMMON_MODE_CALIBRATION_PREOUTCOME_GATE`.

Freeze matched delete-one-label null-control rows using the same `tau` schedule and readout bookkeeping. Under an explicitly frozen shared-nuisance hypothesis, test whether those exact-zero known-physics connected controls can calibrate the additive and `tau`-linear nuisance columns and reduce the PN variance inflation.

The gate must explicitly test the shared-nuisance assumption and must not subtract any physical gravity column from the science rows by construction.