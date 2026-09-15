# SF040 — triple-null cubic crosstalk localization — PREOUTCOME

Date: 2026-09-15
Parent terminal: SF039 `92b84b7e65c3fac26796b7b7fe04d529f3104bf5`.

## PURPOSE

Use the already-established delete-A, delete-B and delete-C exact connected-gravity nulls to test whether genuine degree-three control crosstalk can be localized and calibrated without fitting any successor quantum-gravity residual.

This gate addresses

`BOUND_OR_CALIBRATE_GENUINE_MULTILABEL_NONLINEAR_CONTROL_CONTENT`.

## RETAINED PHYSICAL OBJECT

Keep the SF028B/SF038 `C3` reduced-coherence readout and the SF039 quadratic reversible transport implementation as the ideal control baseline.

No change is made to Newtonian/EIH gravity or to the parent/theory frontiers.

## FROZEN CUBIC CROSSTALK MODEL

The connected register/control phase during the free/readout interval is

`Theta3_ctrl = - zeta(lambda_A,lambda_B,lambda_C) T`.

Freeze the minimal first-order actuator-dependence model

`zeta = zeta0 + zeta_A lambda_A + zeta_B lambda_B + zeta_C lambda_C`.

Here `lambda_I` are physical transport-amplitude settings, not branch bits.

Nominal science amplitudes:

`lambda_B=lambda_C=1`,

`lambda_A in {-1,-1/2,0,1/2,1}`.

No quadratic cross-amplitude terms such as `lambda_A lambda_B` are allowed in SF040; they require a new independently motivated gate.

## FROZEN NULL CONFIGURATIONS

For every signed `lambda_A` and every retained `(R,tau)` row, define four configurations:

S — science:

`(lambda_A,1,1)`.

NA — delete-A gravity null:

`(0,1,1)` while the A qubit remains in the register.

NB — delete-B gravity null:

`(lambda_A,0,1)` while the B qubit remains in the register.

NC — delete-C gravity null:

`(lambda_A,1,0)` while the C qubit remains in the register.

All controls retain exact COM closure by updating the D transport accordingly.

By inherited authority, every NA/NB/NC known-gravity connected term is exactly zero at the retained order.

## EXACT CROSSTALK IDENTITIES TO TEST

Under the frozen linear actuator-dependence model:

`zeta_S = zeta0 + zeta_A lambda_A + zeta_B + zeta_C`,

`zeta_NA = zeta0 + zeta_B + zeta_C`,

`zeta_NB = zeta0 + zeta_A lambda_A + zeta_C`,

`zeta_NC = zeta0 + zeta_A lambda_A + zeta_B`.

Therefore prospectively expected algebraic differences are

`zeta_S-zeta_NA = zeta_A lambda_A`,

`zeta_S-zeta_NB = zeta_B`,

`zeta_S-zeta_NC = zeta_C`.

After `zeta_A,zeta_B,zeta_C` are determined, `zeta0` is overdetermined by the three null families.

## FROZEN DESIGN

Use the SF038 signed amplitudes

`lambda_A={-1,-1/2,0,1/2,1}`.

Retain the SF038 geometry/time grid

`R/ell={60,160,400}`,

`tau={0.05,0.1,0.2}`.

The algebraic localization result must not depend on choosing a favorable R or tau.

## REQUIRED CHECKS

C1. Exact inherited gravity null for NA/NB/NC across all signed lambda_A cells.

C2. Build the control-only design matrix for `[zeta0,zeta_A,zeta_B,zeta_C]` from S/NA/NB/NC and verify full rank.

C3. Compute normalized conditioning of the control-only localization matrix.

C4. Verify that omitting all three null families and using science rows alone cannot separately identify `zeta0,zeta_B,zeta_C`.

C5. Verify that using only NA plus science identifies the A-dependent difference but leaves B/C decomposition underdetermined.

C6. Verify the exact difference identities above.

C7. Construct one mandatory countermodel containing `zeta_AB lambda_A lambda_B`; show which triple-null consistency relation it violates or leaves ambiguous. Do not fit its coefficient.

C8. Do not include any quantum-gravity residual column.

## DECISION RULE

### PASS

`TRIPLE_NULL_CONTROLS_LOCALIZE_LINEAR_CUBIC_CROSSTALK_SCOPED`

if the full S+NA+NB+NC control model is full rank, the expected exact identities hold, and the science-only / partial-null negative controls fail in the preregistered way.

### QUALIFIED

If full rank exists but conditioning is poor (`kappa>50`), use

`TRIPLE_NULL_CROSSTALK_LOCALIZATION_FULL_RANK_BUT_ILL_CONDITIONED_SCOPED`.

### BLOCKED

Use `BLOCKED` for failure of inherited gravity nulls or inability to maintain exact COM-closed control definitions.

### INVALID

Any post-result addition of higher actuator-dependence degree, residual gravity column, changed null definition or selected R/tau subset requires a new preregistration.

## INTERPRETATION CEILING

A PASS establishes a self-calibrating **control protocol architecture** for the frozen linear actuator-dependence model. It does not establish actual crosstalk magnitudes or real-device precision.

No quantum matching coefficient, quantum `chi_ABC`, successor residual, new physics or parent promotion is authorized.
