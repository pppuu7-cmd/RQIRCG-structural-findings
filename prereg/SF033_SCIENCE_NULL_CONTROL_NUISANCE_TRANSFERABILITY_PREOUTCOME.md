# SF033 — science/null-control nuisance transferability — PREOUTCOME PREREGISTRATION

Date: 2026-09-15
Inherited authoritative recovery head: `232b137fbc7c5fad4cbb6c19a7644faf0676e8e3`.

## PURPOSE

Determine whether the **current already-authorized RQIRCGSF protocol**, without inventing new apparatus/control physics, supplies a physical map that guarantees the dominant SF032 `tau`-linear nuisance is shared between the science configuration and the matched delete-A null-control configuration.

This is an object/authority audit. No connected coefficient, Fisher scan or successor law is evaluated.

## TARGET STATEMENT

The target physical statement is:

`n_tau^science = n_tau^deleteA`

for the nuisance coefficient multiplying the same abstract `tau`-linear phase template in the two configurations.

SF032 established the consequence of this equality if it holds. SF033 asks whether the equality itself is already derived by current protocol authority.

## AUTHORITATIVE OBJECTS TO AUDIT

Read only the current protocol-defining chain relevant to transferability:

1. SF028B prospective preregistration;
2. SF028B terminal result;
3. SF028B derivation/source notes;
4. SF029 robustness terminal only for delete-one-label control scope;
5. SF032 preregistration/terminal only for the exact sharing hypothesis and claim ceiling.

Do not search unrelated detector technologies or choose a hardware implementation post hoc.

## REQUIRED TRANSFER MAP FOR PASS

A physical PASS requires current authority to specify all of:

1. an explicit control/readout operation or error generator that produces the `tau`-linear nuisance;
2. its action on the full science protocol;
3. its action on the delete-A protocol;
4. an explicit reason or symmetry showing the nuisance coefficient is identical when the A displacement operation is disabled;
5. a statement of which variables/hardware degrees are held fixed versus changed;
6. a falsification condition for nuisance sharing.

An abstract statement that the same nominal readout is used is insufficient if no error/control generator is defined.

Likewise, 'common mode' is not self-authorizing terminology.

## PREDECLARED TERMINAL RULE

### PASS

`SCIENCE_NULL_NUISANCE_TRANSFER_MAP_DERIVED_SCOPED`

only if all six required map elements are already present in current authoritative protocol content.

### BLOCKED

`BLOCKED_MISSING_CONTROL_TRANSFER_MODEL`

if current authority defines ideal `U_prep/U_read` and known-gravity evolution but does not specify the physical pulse/readout/control-error model needed to derive the sharing equality.

### FAIL

`CURRENT_PROTOCOL_PREDICTS_NONTRANSFERABLE_NUISANCE_SCOPED`

only if an existing explicit control/error model affirmatively predicts different nuisance coefficients between science and delete-A configurations.

### INVALID

`INVALID_RETROACTIVE_CONTROL_MODEL_IMPORT`

if the audit attempts to introduce new hardware, pulse-error, electronics, detector or material dynamics after seeing the SF032 calibration benefit and then treats it as inherited authority.

## INTERPRETATION CEILING

A BLOCKED result is not evidence that matched controls cannot work. It means only that transferability is not yet part of the defined physical model.

A future repair must be a new prospective control/readout model or experimental calibration contract.

No quantum residual or new-gravity coefficient is authorized.

## CLAIM LOCKS

Retain:

`CONTROL_CALIBRATION != PHYSICAL_TRANSFERABILITY`.

Retain:

`BLOCKED != FAIL`.

Retain:

`STRUCTURAL_IDENTIFIABILITY != ESTIMABILITY != FEASIBILITY`.

Theory track remains independently blocked on

`GENUINELY_NEW_MICROSCOPIC_MATCHING_PRINCIPLE_WITH_EXPLICIT_PHYSICAL_MAP_REQUIRED`.