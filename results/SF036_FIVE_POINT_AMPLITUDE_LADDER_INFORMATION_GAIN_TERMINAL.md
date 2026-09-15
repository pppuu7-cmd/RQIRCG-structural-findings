# SF036 — five-point amplitude ladder information gain — TERMINAL

Date: 2026-09-15
Preregistration: `b75f25c587ba32c55750ab40ce77a11edf4a6c34`.
Script: `scripts/sf036_checks.py`, commit `164e432ce903dc1b7ca4b10e2d3e1663992dc644`.
Canonical raw: `results/raw/SF036_CHECKS.json`, commit `4d7046d6c6907cafa50211374664c67e30e92062`.
Script SHA-256: `0a007907883f6c34abad78233d742aec7ef18a59de328362e5b71ca7ad46f440`.

## RESULT / CLASSIFICATION

`FIVE_POINT_AMPLITUDE_LADDER_STRONGLY_IMPROVES_Q2_CONDITIONING_SCOPED`.

No successor residual was introduced.

## Frozen design

`lambda_A in {0,1/4,1/2,3/4,1}`,

`R/ell in {60,160,400}`,

`tau in {0.05,0.1,0.2}`,

for 45 rows.

The Q2 nuisance family remained exactly

`zeta(lambda_A)=zeta0+zeta1 lambda_A+zeta2 lambda_A^2`.

The known Newtonian/feedback/1PN coefficients were recomputed for every new amplitude with exact COM closure; no endpoint interpolation was used.

## Full five-point result

Normalized six-column design:

`rank=6`,

`kappa=219.1476`,

`smin=0.0100762`.

The SF035 three-point comparator was

`kappa=899.7091`,

`smin=0.00244557`.

Thus

`kappa improvement factor = 4.1055`,

`smin improvement factor = 4.1202`.

Both exceed the preregistered factor-three strong-PASS thresholds.

## Robustness to one missing interior amplitude

All leave-one-interior-amplitude designs remain rank 6:

- drop `lambda=1/4`: `kappa=325.12`;
- drop `lambda=1/2`: `kappa=212.26`;
- drop `lambda=3/4`: `kappa=324.92`.

Therefore the gain is not carried by a single unique interior point.

The symmetric interior coverage matters, but no one amplitude is indispensable for rank.

## R and T remain essential

With only one fixed R, the five-point amplitude ladder is formally rank 6, but normalized condition numbers are enormous:

- `R=60`: `kappa~3.88e6`;
- `R=160`: `kappa~2.12e7`;
- `R=400`: `kappa~1.22e8`.

Thus amplitude variation cannot replace the geometry lever.

With one fixed tau, rank remains 6 but

`kappa~892.3`.

Thus amplitude variation also cannot replace time leverage.

The information is genuinely complementary:

`R + T + lambda_A`.

## Near-null structure after five-point repair

The smallest-singular direction remains dominated by the same sector:

`1PN ~ -0.804`,

`zeta1 ~ -0.323`,

`zeta2 ~ -0.498`,

with negligible feedback contribution.

Thus the added amplitudes weaken but do not remove the physical calibration tension between the 1PN amplitude shape and smooth connected control-phase curvature.

This is why the result is a strong structural information-gain PASS rather than a precision/feasibility PASS.

## Exact controls

`lambda_A=0` remains an exact gravitational connected null.

Delete-A, delete-B and delete-C controls remain exact zero.

No sign/coefficient selection was made from the output.

## Structural interpretation

SF035 established that Q2 is full rank but badly conditioned on the minimal amplitude ladder.

SF036 shows that adding prospectively fixed intermediate amplitudes provides **real independent information**, improving the critical singular direction by more than a factor four.

Therefore the quadratic control-phase problem is not an exact known-gravity degeneracy.

But:

`STRUCTURAL INFORMATION GAIN != PHASE PRECISION`.

The remaining high-value question is statistical: how much PN precision is lost when `zeta0,zeta1,zeta2` are estimated simultaneously in the improved five-point design?

## Exact next admissible operational gate

`SF037_NOISE_AWARE_Q2_CONTROL_CALIBRATION_ESTIMABILITY_PREOUTCOME_GATE`.

Use the five-point/R/T design exactly as frozen here, add only homoscedastic phase noise, and compute Fisher/CRLB requirements for the 1PN amplitude while jointly fitting the known Newtonian basis and `zeta0,zeta1,zeta2`.

Compare prospectively against SF031 science-only common-mode and SF032 ideal shared-control reference numbers, but do not claim detector feasibility.

## Claim ceiling

SF036 establishes no achieved phase sensitivity, device transfer stability, detector feasibility, higher-than-quadratic nuisance bound, successor quantum residual, quantum matching coefficient, quantum `chi_ABC` or new physics.

Retain:

`DESIGN_INFORMATION_GAIN != DEVICE_FEASIBILITY`.
