# SF041 — pairwise actuator-cross crosstalk localization — PREOUTCOME

Date: 2026-09-15
Parent terminal: SF040 `daeedf7e765eb9ae767492ea6f8df2ae6f8e513f`.

## PURPOSE

Stress-test the SF040 triple-null calibration architecture against the exact pair-cross actuator countermodel frozen by SF040.

## FROZEN CROSSTALK MODEL

`zeta = zeta0 + zeta_A lambda_A + zeta_B lambda_B + zeta_C lambda_C`
`       + zeta_AB lambda_A lambda_B + zeta_AC lambda_A lambda_C + zeta_BC lambda_B lambda_C`.

Parameter order:

`[zeta0,zeta_A,zeta_B,zeta_C,zeta_AB,zeta_AC,zeta_BC]`.

No square/cubic amplitude powers and no successor residual are allowed.

## FROZEN CONFIGURATIONS

Keep exactly SF040:

S `(lambda_A,1,1)`,

NA `(0,1,1)`,

NB `(lambda_A,0,1)`,

NC `(lambda_A,1,0)`.

Signed A ladder:

`lambda_A={-1,-1/2,0,1/2,1}`.

Use the inherited tau schedule; R repetition may be retained but cannot change the control-only algebraic rank because the crosstalk model is R-independent.

All NA/NB/NC known-gravity connected terms remain exact zero by inherited authority.

## REQUIRED TESTS

C1. Build the exact seven-column control matrix from S/NA/NB/NC.

C2. Determine rank and normalized singular spectrum.

C3. If rank deficient, report an explicit null-space parameter combination rather than choosing a pseudoinverse solution.

C4. Repeat on null-only NA/NB/NC.

C5. Preserve science-only rank failure as negative control.

C6. Identify the **minimum additional null configuration class** that would target the null direction, without adding it to SF041.

## DECISION RULE

### PASS

`TRIPLE_NULL_CONTROLS_LOCALIZE_PAIR_CROSS_CUBIC_CROSSTALK_SCOPED`

only if rank is 7.

### BLOCKED / STRUCTURAL DEGENERACY

`TRIPLE_NULL_PAIR_CROSS_CROSSTALK_HAS_ONE_UNRESOLVED_DIRECTION_SCOPED`

if rank is exactly 6 with an explicit one-dimensional null direction.

Use a broader degeneracy label if rank <6.

### INVALID

Do not add a double-null configuration after seeing the rank. Any repair is a separate preregistered successor gate.

## INTERPRETATION CEILING

A degeneracy is a design-information result, not evidence that crosstalk exists physically and not a gravity failure.

No quantum residual, matching coefficient, quantum `chi_ABC`, new physics or parent promotion is authorized.
