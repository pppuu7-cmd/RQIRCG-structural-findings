# SF032 — matched null-control common-mode calibration — TERMINAL

Date: 2026-09-15
Preregistration: `66e7b301200ca7b450f0bba38b4edce872166762`.
Script: `scripts/sf032_checks.py`, commit `bc6b7c4c723c1fb3334679180d0793b55c56763b`.
Canonical raw: `results/raw/SF032_CHECKS.json`, commit `bf0b266f54a1f19153d1b19a5dcbba09e8278e66`.

## RESULT / CLASSIFICATION

`MATCHED_NULL_CONTROL_BREAKS_COMMON_MODE_PN_NEAR_DEGENERACY_SCOPED`

Mandatory interpretation qualification:

`NULL_CONTROL_CALIBRATION_BLOCKED_BY_UNVALIDATED_SHARED_NUISANCE_MAP`

Secondary structural result:

`SHARED_TAU_LINEAR_CONTROL_CHANNEL_PROVIDES_DOMINANT_CALIBRATION_INFORMATION_SCOPED`.

No successor quantum component was added or fitted.

## Frozen control construction

SF032 retains the exact 9 SF030/SF031 science rows

`R/ell={60,160,400}` x `tau={0.05,0.1,0.2}`

and adds one matched delete-A control for each row.

The delete-A controls use the same nominal R, tau, apparatus topology, mass ratio and readout bookkeeping while prospectively setting the A branch displacement amplitude to zero.

By the exact connected finite-difference controls already established in SF028B/SF029, all three retained gravity columns vanish on these control rows:

`x_app=x_fb=x_1PN=0`.

The control zeros are therefore inherited known-physics structure, not fitted subtractions.

## Frozen sharing models

S0: science-only SF031 baseline with offset and `tau`-linear nuisance.

S1: matched controls with both offset and `tau`-linear nuisance shared between science and control rows.

S2: shared offset only; independent science/control `tau`-linear nuisances.

S3: shared `tau`-linear nuisance only; independent science/control offsets.

S4: no nuisance sharing; independent offset and `tau`-linear nuisance in science and control rows.

Every row has the same frozen iid noise variance `sigma_y^2`.

## Rank result

All models are full rank for every frozen nonzero `epsilon_PN`:

- S0: `5/5`;
- S1: `5/5`;
- S2: `6/6`;
- S3: `6/6`;
- S4: `7/7`.

Thus the matched controls do not create an artificial algebraic rank defect.

## Conditioning result

Normalized condition numbers are

- S0: `1113.46`;
- S1 shared both: `9.948`;
- S2 shared offset only: `1070.81`;
- S3 shared tau-linear only: `22.362`;
- S4 no sharing: `1113.46`.

The enormous SF031 near-degeneracy is therefore specifically broken when the `tau`-linear common mode is independently constrained by the null-control rows.

Sharing only the constant offset barely changes the bad geometry.

## PN variance inflation

Relative to the ideal iid SF031 model A, the PN variance-inflation factors are

- S0: `~2.13413e4`;
- S1: `1.65820`;
- S2: `~2.13413e4`;
- S3: `12.3086`;
- S4: `~2.13413e4`.

Thus the fully shared matched control restores PN variance to within a factor `1.66` of the ideal iid calibration case.

The preregistered PASS condition `VIF(S1)<100` is satisfied by a wide margin.

## Improvement relative to SF031 common-mode baseline

PN variance improvement relative to S0 is

- S1: `~1.28702e4`;
- S2: `~1.00000000007`;
- S3: `~1.73385e3`;
- S4: `1` to numerical precision.

The preregistered required S1 improvement factor was `>=100`; the observed factor is over twelve thousand.

The no-sharing negative control S4 changes the PN variance by less than `1e-14` fractionally and therefore passes the preregistered requirement that an unshared control provide no material benefit.

This negative control is important: the precision gain does not come merely from appending more zero-valued rows. It comes from a specific cross-configuration nuisance-identification assumption.

## Required phase precision

The required dimensionless phase-noise ceiling for nominal PN SNR 1 remains linear in `epsilon_PN`.

The coefficients are

- S0: `sigma_y,SNR1 = 2.11470e-6 epsilon_PN`;
- S1: `sigma_y,SNR1 = 2.39905e-4 epsilon_PN`;
- S2: `2.11470e-6 epsilon_PN`;
- S3: `8.80549e-5 epsilon_PN`;
- S4: `2.11470e-6 epsilon_PN`.

At diagnostic `epsilon_PN=1e-6`, for example:

- S0 requires `sigma_y <= 2.1147e-12`;
- S1 permits `sigma_y <= 2.3991e-10`;
- S3 permits `sigma_y <= 8.8055e-11`.

Again these are requirements relative to the unspecified phase scale `Phi0`, not achieved detector sensitivities.

## What the ablations prove

The calibration value is carried overwhelmingly by the shared `tau`-linear nuisance channel.

`shared offset only -> essentially no benefit`.

`shared tau-linear only -> ~1.73e3 variance improvement`.

`shared both -> ~1.29e4 improvement`.

`no sharing -> no benefit`.

Therefore the next experimental/model-definition question is highly localized:

**Is the dominant `tau`-linear phase nuisance physically transferable between the science configuration and the delete-A null-control configuration?**

SF032 does not assume that this transferability is automatically true in a real apparatus.

## Interpretation qualification

The algebraic PASS is conditional on the prospectively explicit shared-nuisance hypothesis.

The current RQIRCGSF protocol does not yet contain a microscopic pulse/readout/control-error model proving that a real `tau`-linear nuisance coefficient is invariant when one source branch displacement is disabled.

Therefore retain:

`NULL_CONTROL_CALIBRATION_BLOCKED_BY_UNVALIDATED_SHARED_NUISANCE_MAP`.

This does not revoke the algebraic calibration PASS. It limits its physical promotion.

## New structural fact

The SF031 precision bottleneck is not irreducible white noise. It is a **calibratable nuisance direction** if a matched connected-null control shares the relevant phase nuisance.

This changes the operational frontier from

`need fantastically small raw phase noise`

to

`need a physically justified science-to-null-control nuisance transfer map`.

That is a much sharper and more falsifiable requirement.

## Firewalls

Retain:

`CONTROL_CALIBRATION != PHYSICAL_TRANSFERABILITY`.

Retain:

`STRUCTURAL_IDENTIFIABILITY != ESTIMABILITY != FEASIBILITY`.

No null-control residual is authorized as quantum gravity.

## Claim ceiling

SF032 establishes no:

- physically demonstrated common-mode transferability;
- pulse/control fidelity;
- detector feasibility;
- laboratory phase sensitivity;
- exact all-time dynamics;
- successor quantum law;
- quantum matching coefficient;
- GR-vs-QG discriminator;
- quantum `chi_ABC`;
- new physics.

Theory track remains independently blocked on

`GENUINELY_NEW_MICROSCOPIC_MATCHING_PRINCIPLE_WITH_EXPLICIT_PHYSICAL_MAP_REQUIRED`.

## Exact next admissible operational gate

`SF033_SCIENCE_NULL_CONTROL_NUISANCE_TRANSFERABILITY_PREOUTCOME_GATE`.

Before using the S1 precision improvement as a physical design claim, prospectively define the minimal science/control implementation map and identify which nuisance terms are guaranteed common by construction, which can change when A displacement is disabled, and which require independent calibration.

If the current abstract protocol does not contain enough control/readout physics to derive sharing, terminalize the gate as `BLOCKED_MISSING_CONTROL_TRANSFER_MODEL` rather than assuming perfect common mode.