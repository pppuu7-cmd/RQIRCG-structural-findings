# SF041 — pairwise actuator-cross crosstalk localization — TERMINAL

Date: 2026-09-15
Preregistration: `1127a7a774aeab6e33c27f3a0532f32068f35fd2`.

## RESULT / CLASSIFICATION

`TRIPLE_NULL_PAIR_CROSS_CROSSTALK_HAS_ONE_UNRESOLVED_DIRECTION_SCOPED`.

This is a structural calibration-design degeneracy, not a gravity failure and not evidence that pair-cross crosstalk is physically present.

## Frozen seven-parameter model

`zeta = zeta0 + zeta_A lambda_A + zeta_B lambda_B + zeta_C lambda_C`
`       + zeta_AB lambda_A lambda_B + zeta_AC lambda_A lambda_C + zeta_BC lambda_B lambda_C`.

Configurations remained exactly

S `(lambda_A,1,1)`,

NA `(0,1,1)`,

NB `(lambda_A,0,1)`,

NC `(lambda_A,1,0)`.

No double-null row was added after observing the result.

## Exact rank result

Using the full signed A ladder and inherited tau schedule, the exact rational control matrix has

`rank=6`

for 7 parameters.

Nullity:

`1`.

The exact null-space vector in parameter order

`[zeta0,zeta_A,zeta_B,zeta_C,zeta_AB,zeta_AC,zeta_BC]`

is

`(1,0,-1,-1,0,0,1)`.

Thus the unresolved reparameterization is

`delta zeta0 = +delta`,

`delta zeta_B = -delta`,

`delta zeta_C = -delta`,

`delta zeta_BC = +delta`.

All S/NA/NB/NC predicted control phases are invariant under this transformation.

Equivalently, the current configurations cannot separately identify the combination

`zeta0 - zeta_B - zeta_C + zeta_BC`.

No pseudoinverse coefficient is promoted.

## Null-only result

Using only NA+NB+NC gives

`rank=5`

with two exact null directions.

One is the same B/C pair-cross ambiguity above.

The second mixes `zeta_A` with `zeta_AB,zeta_AC`, because without science rows there is insufficient information to distinguish all A-linear cross contributions in this enlarged model.

Thus the strong null-only completeness of SF040 is specific to its prospectively frozen first-order single-actuator model and does not survive automatic model enlargement.

## Science-only negative control

Science rows alone have

`rank=2`

for the seven-parameter model.

This confirms that the rank-6 result is genuinely provided by complementary null controls rather than by signed-lambda repetition alone.

## Why the degeneracy occurs

B and C amplitudes appear only in the binary patterns represented by S/NA/NB/NC.

There is no configuration in SF041 with

`lambda_B=lambda_C=0`

while retaining the A register/control structure.

Therefore the data never directly expose the pure baseline plus A sector independently of B, C and BC contributions.

## Minimum prospective repair

The exact null vector identifies the minimum missing lever:

one double-null family

`NBC = (lambda_A,0,0)`.

Such rows would be an exact connected-gravity null because both B and C displacements are disabled while all qubits remain present.

SF041 does **not** add this repair.

A separate prospective gate is required.

## New structural fact

The appropriate design principle is now explicit:

`ONE-BODY NULLS CALIBRATE SINGLE-ACTUATOR CROSSTALK; PAIR-CROSS CROSSTALK REQUIRES AT LEAST ONE DOUBLE-NULL LEVER`.

This is scoped to the frozen linear+pair-cross actuator model.

## Exact next admissible gate

`SF042_DOUBLE_NULL_PAIR_CROSS_CROSSTALK_CLOSURE_PREOUTCOME_GATE`.

Add only `NBC=(lambda_A,0,0)` to the existing S/NA/NB/NC family and test whether the seven-parameter model becomes full rank with moderate conditioning.

Do not add higher actuator polynomial degree in that gate.

## Claim ceiling

No actual crosstalk magnitude, device feasibility, successor quantum residual, quantum matching coefficient, quantum `chi_ABC`, new physics or parent promotion is established.
