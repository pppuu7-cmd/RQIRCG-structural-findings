# SF038 — signed-amplitude parity calibration — TERMINAL

Date: 2026-09-15
Preregistration: `08d16e0c75192345f196cb82f0aaf0bb5c6eb04b`.
Script: `scripts/sf038_checks.py`, commit `735257e70413746db9e05fcfdb166585e162cb75`.
Canonical raw: `results/raw/SF038_CHECKS.json`, commit `6c942861ead30a6f8bbdfa947a8104d0173dbab5`.
Script SHA-256: `cb1a78cc1d3ab829c4b5b6ff49aa30fd4958a1ae7e892964872258a1c3a4bf43`.

## RESULT / CLASSIFICATION

`SIGNED_AMPLITUDE_PARITY_STRONGLY_IMPROVES_Q2_CALIBRATION_SCOPED`.

All three preregistered strong-information-gain criteria pass.

No successor residual was added or fitted.

## Frozen signed design

`lambda_A in {-1,-1/2,0,1/2,1}`,

`R/ell in {60,160,400}`,

`tau in {0.05,0.1,0.2}`,

for 45 rows, exactly matching the row count of the positive five-point SF036/SF037 comparator.

At every signed amplitude the exact Newtonian, force-feedback and static EIH coefficients were recomputed with the compensating D displacement; no parity assumption was imposed on gravity.

## Geometry/domain controls

All signed branch configurations remain collision-free and maintain the index ordering used by the exact rational model.

Minimum pair-center separation across the full signed grid:

`3 ell`.

This equals the minimum separation of the positive comparator.

`lambda_A=0` remains an exact connected known-gravity null.

`lambda_A=+1` exactly recovers the positive endpoint coefficients.

Delete-A, delete-B and delete-C controls remain exact zero across the signed grid.

## Pure nuisance parity control

On the symmetric signed design, the pure nuisance columns

`x_z1=lambda tau`

and

`x_z2=lambda^2 tau`

have numerical inner product

`3.61e-18`,

consistent with the exact odd/even cancellation expected from the symmetric amplitude set.

This parity leverage was the preregistered independent motivation for the gate.

## Structural Q2 result

Signed design:

`rank=6`,

`kappa=41.8259`,

`smin=0.0439834`.

Positive five-point comparator recomputed by the same implementation:

`rank=6`,

`kappa=219.1476`,

`smin=0.0100762`.

Therefore signed reversal improves

`kappa` by factor `~5.24`,

and

`smin` by factor `~4.36`.

The preregistered factor-three structural criteria are both passed.

## Noise-aware Q2 result

At diagnostic `epsilon_PN=1e-6`:

positive five-point Q2:

`VIF_PN = 909.166`;

signed Q2:

`VIF_PN = 37.5094`.

Thus the relative VIF improves by factor

`24.238x`.

The direct PN variance improvement between positive-Q2 and signed-Q2 designs is

`19.273x`.

The same values are reproduced at `epsilon_PN=1e-8` to numerical precision after the expected scale factor is removed.

Signed-design SNR1 phase-noise coefficient:

`sigma_y,SNR1/epsilon_PN = 5.54767e-5`.

Positive five-point value:

`1.26367e-5`.

Hence the signed design tolerates about `4.39x` larger iid phase noise for the same nominal PN SNR1 within the frozen Q2 model.

## Strong-rule audit

Preregistered strong criteria:

1. `kappa_signed <= kappa_pos/3`: PASS;
2. `smin_signed >= 3*smin_pos`: PASS;
3. `VIF_signed <= VIF_pos/3`: PASS.

Observed strong-criteria vector:

`[PASS,PASS,PASS]`.

## Near-null interpretation

The remaining smallest-singular direction is still dominated by the 1PN and amplitude-dependent control sector, approximately

`-0.704 * 1PN -0.603 * zeta1 -0.375 * zeta2`,

with small Newtonian contributions.

Thus signed parity does not remove the calibration problem completely, but it converts the Q2 penalty from severe/high (`VIF~909`) to a much more moderate statistical geometry (`VIF~37.5`).

## Scientific interpretation

The result is a fair same-row-count comparison. The improvement does not come from adding more observations; it comes from reversing the physical A-transport direction and thereby exposing odd/even amplitude structure.

This gives a concrete operational design principle:

`SIGNED TRANSPORT REVERSAL PROVIDES PARITY CALIBRATION POWER AGAINST CONNECTED CONTROL-PHASE CURVATURE`.

The principle is scoped to the explicit Q2 effective control model and the recomputed known-gravity protocol family.

## New operational frontier

The abstract calibration geometry is no longer the dominant blocker.

The next missing object is **device-level reversible transport authority**: a prospectively specified control implementation in which `lambda_A -> -lambda_A` is a physically meaningful reversal with controlled pulse/readout errors and a defined transfer test.

Recommended next action:

`EXPLICIT_REVERSIBLE_TRANSPORT_IMPLEMENTATION_MODEL_REQUIRED`.

Do not continue arbitrary higher-polynomial nuisance scans merely because Q2 was tractable; a higher nuisance degree requires independent physical motivation.

## Claim ceiling

SF038 establishes no laboratory implementation of signed transport, achieved phase sensitivity, detector technology, control hardware, higher-than-quadratic nuisance bound, successor quantum residual, quantum matching coefficient, GR-vs-QG discriminator, quantum `chi_ABC` or new physics.

Retain:

`DESIGN_CALIBRATION_POWER != DEVICE_VALIDATION`.

Retain:

`KNOWN_PHYSICS_SUBTRACTION != QUANTUM_RESIDUAL_AUTHORITY`.
