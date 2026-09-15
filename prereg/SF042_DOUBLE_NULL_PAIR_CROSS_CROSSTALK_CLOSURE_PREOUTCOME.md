# SF042 — double-null pair-cross crosstalk closure — PREOUTCOME

Date: 2026-09-15
Parent terminal: SF041 `0502125168c6ba09c4d4f5f70ec68df058ded2bb`.

## PURPOSE

Test the minimum prospective repair identified by the exact SF041 null direction: add one `B=C=0` double-null control family and determine whether the frozen seven-parameter linear+pair-cross crosstalk model becomes fully identifiable.

## RETAINED MODEL

Keep exactly

`zeta = zeta0 + zeta_A lambda_A + zeta_B lambda_B + zeta_C lambda_C`
`       + zeta_AB lambda_A lambda_B + zeta_AC lambda_A lambda_C + zeta_BC lambda_B lambda_C`.

No square/cubic amplitude powers, higher cross terms or successor residual are allowed.

## RETAINED CONFIGURATIONS

S `(lambda_A,1,1)`,

NA `(0,1,1)`,

NB `(lambda_A,0,1)`,

NC `(lambda_A,1,0)`.

## NEW PROSPECTIVE DOUBLE-NULL FAMILY

Add exactly

`NBC = (lambda_A,0,0)`.

B and C qubits remain in the register but their motional displacement operations are disabled. A uses the same signed ladder.

Exact COM closure is maintained by the recoil-body transport.

Because both B and C displacements are disabled, every retained connected known-gravity coefficient is exactly zero in NBC by the same delete-label theorem used in earlier gates.

## FROZEN DESIGN

`lambda_A={-1,-1/2,0,1/2,1}`.

Retain the inherited tau schedule. R repetition may be included but cannot create algebraic control rank by itself.

## REQUIRED CHECKS

C1. Exact rational rank of full S+NA+NB+NC+NBC seven-column matrix.

C2. Column-normalized condition number and singular spectrum.

C3. Exact nullspace must be empty for PASS.

C4. Null-only NA+NB+NC+NBC rank/conditioning; determine whether science rows are required for control calibration.

C5. Remove NBC again and reproduce the SF041 exact null vector `(1,0,-1,-1,0,0,1)`.

C6. Remove one other null family in turn and record rank loss/conditioning to identify minimum control completeness.

C7. No gravity-bearing science residual may be introduced as an eighth parameter.

## DECISION RULE

### PASS

`DOUBLE_NULL_CLOSES_PAIR_CROSS_CROSSTALK_MODEL_SCOPED`

if the full seven-parameter matrix has rank 7 and `kappa<=50`.

Secondary PASS if null-only controls also reach rank 7:

`GRAVITY_NULL_CONTROLS_ALONE_CLOSE_PAIR_CROSS_CROSSTALK_MODEL_SCOPED`.

### QUALIFIED

If full rank 7 but `kappa>50`:

`DOUBLE_NULL_PAIR_CROSS_MODEL_FULL_RANK_BUT_ILL_CONDITIONED_SCOPED`.

### FAIL / NO INFORMATION GAIN

If the exact SF041 null direction survives after NBC, record the scoped design failure without changing the model.

### INVALID

Any post-result extra double-null family or new nuisance term requires a new gate.

## INTERPRETATION CEILING

A PASS establishes control-model identifiability only. It does not establish actual crosstalk magnitude, phase precision or device feasibility.

No quantum residual, matching coefficient, quantum `chi_ABC`, new physics or parent promotion is authorized.
