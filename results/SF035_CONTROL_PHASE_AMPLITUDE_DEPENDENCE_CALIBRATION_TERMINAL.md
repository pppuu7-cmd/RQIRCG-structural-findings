# SF035 — control-phase amplitude-dependence calibration — TERMINAL

Date: 2026-09-15
Preregistration: `854c33c5fde4092b76c506d39f6eea056784a182`.
Executed script: `scripts/sf035_checks.py`, commit `fa90297afc7040b7cf23d8b06cb89c97fe789c6b`.
Canonical raw: `results/raw/SF035_CHECKS.json`, commit `8a411f87e126b5e5186afb8e2bb850eb1cbc95be`.
Near-null diagnostic script: `ccd96870843939cf4840487cfe0206f53b0b365e`.
Near-null raw: `532e0be167054184c80aa7228dbe271f8f5a3362`.
Main script SHA-256: `3db5663118b3ee20ad7691633489c257591e24891ab9eddac536d4c32ee3995d`.

## RESULT / CLASSIFICATION

Primary:

`LINEAR_CONTROL_PHASE_AMPLITUDE_DEPENDENCE_IDENTIFIABLE_SCOPED`.

Qualified secondary:

`QUADRATIC_CONTROL_PHASE_AMPLITUDE_DEPENDENCE_IDENTIFIABLE_BUT_ILL_CONDITIONED_SCOPED`.

New structural localization:

`QUADRATIC_CONTROL_PHASE_CURVATURE_IS_NEAR_DEGENERATE_WITH_1PN_AMPLITUDE_SHAPE_SCOPED`.

No successor quantum residual was added or fitted.

## Frozen design

`lambda_A in {0,1/2,1}`,

`R/ell in {60,160,400}`,

`tau in {0.05,0.1,0.2}`,

for 27 rows.

At every amplitude the A motional displacement and compensating D recoil displacement were changed together, preserving exact COM closure.

The known-gravity basis was recomputed directly for every `(lambda_A,R)` cell rather than interpolating endpoint coefficients.

## Exact endpoint and delete-label controls

At `lambda_A=0`:

`Delta3 V_N = Delta3 A_N = Delta3 V_static^1PN = 0`

exactly at every frozen R.

At `lambda_A=1` the inherited SF029/SF030 coefficients are recovered.

Delete-A, delete-B and delete-C finite-difference controls are exact zero across all frozen cells.

## L1 — linear nuisance result

For

`zeta(lambda_A)=zeta0+zeta1 lambda_A`,

the five-column normalized design

`[x_app,x_fb,x_1PN,x_z0,x_z1]`

has

`rank=5`,

`kappa=23.8972`,

with singular values

`(1.97621,0.78136,0.61629,0.31211,0.08270)`.

Therefore the linear amplitude dependence is structurally identifiable with moderate normalized conditioning in the full frozen design.

Classification:

`LINEAR_CONTROL_PHASE_AMPLITUDE_DEPENDENCE_IDENTIFIABLE_SCOPED`.

### Endpoint-only `{0,1}` comparison

Using only delete-A and full-science amplitudes remains formally rank 5, but

`kappa=1088.93`.

Thus endpoint-only calibration is almost degenerate.

The intermediate `lambda_A=1/2` row is not redundant: it improves the normalized condition number by about a factor 45.6.

### Required no-amplitude-lever negative control

At `lambda_A=1` only,

`rank=4` rather than 5,

because `x_z0=tau` and `x_z1=lambda_A tau=tau` are exactly collinear.

This negative control passes and confirms that amplitude variation, not SVD tolerance, carries the new information.

## Q2 — quadratic nuisance result

For

`zeta(lambda_A)=zeta0+zeta1 lambda_A+zeta2 lambda_A^2`,

the six-column full design has

`rank=6`,

`kappa=899.709`,

with smallest normalized singular value

`2.4456e-3`.

Thus quadratic amplitude dependence is structurally identifiable but strongly ill-conditioned.

Classification:

`QUADRATIC_CONTROL_PHASE_AMPLITUDE_DEPENDENCE_IDENTIFIABLE_BUT_ILL_CONDITIONED_SCOPED`.

### Why the middle amplitude is essential

With only `lambda_A in {0,1}` the Q2 design has rank 5, because `lambda_A` and `lambda_A^2` are identical on the two-point set.

The intermediate amplitude restores the sixth direction.

### Single-R and single-tau ablations

For every fixed R, both L1 and Q2 designs collapse to rank 4. Therefore R variation remains essential.

For one fixed tau, L1 is formally rank 5 but `kappa~883.6`; Q2 is formally rank 6 but `kappa~6.90e4`.

Thus time variation remains essential for useful conditioning even after the amplitude lever is added.

## Near-null diagnostic

The smallest-singular-vector diagnostic localizes the Q2 weakness.

For Q2 the near-null normalized combination is dominated by

`-0.802 * 1PN -0.317 * zeta1 -0.506 * zeta2`,

with negligible feedback component.

Therefore the residual poor conditioning is specifically a near-degeneracy between the **1PN amplitude shape** and the linear/quadratic connected control-phase amplitude dependence.

This is a sharper blocker than generic noise.

## Scientific interpretation

SF034 showed that perfect M0 transferability is one explicit model class.

SF035 now shows that perfect transferability need not be assumed even at first order in control amplitude: a prospectively varied amplitude ladder can structurally fit `zeta1` alongside the known Newtonian and 1PN basis.

Quadratic control curvature can also be separated in principle, but the three-amplitude design gives poor leverage against the 1PN column.

Therefore:

`AMPLITUDE_CALIBRATION != PERFECT_CONTROL_SEPARABILITY`.

But also:

`STRUCTURAL_IDENTIFIABILITY != PRECISION`.

## Exact next admissible operational gate

`SF036_FIVE_POINT_AMPLITUDE_LADDER_INFORMATION_GAIN_PREOUTCOME_GATE`.

Prospectively freeze a denser A-displacement ladder while keeping the same R/T design, gravitational model and Q2 nuisance family. Test whether added amplitude curvature information materially improves the Q2 smallest singular value / normalized conditioning and whether the improvement survives leave-one-amplitude-out controls.

Do not add higher nuisance degree or successor residual in that gate.

## Claim ceiling

SF035 establishes no device amplitude stability, achieved phase precision, detector feasibility, unique control-error law, successor quantum component, quantum matching coefficient, GR-vs-QG discriminator, quantum `chi_ABC` or new physics.

Retain:

`KNOWN_PHYSICS_SUBTRACTION != QUANTUM_RESIDUAL_AUTHORITY`.

Retain:

`AMPLITUDE_CALIBRATION != DEVICE_FEASIBILITY`.
