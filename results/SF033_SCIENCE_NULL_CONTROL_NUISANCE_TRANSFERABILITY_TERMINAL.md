# SF033 — science/null-control nuisance transferability — TERMINAL

Date: 2026-09-15
Preregistration: `518409ca497882baa3bad546a01836d4c075139d`.
Authority audit: `research_log/SF033_NUISANCE_TRANSFERABILITY_AUTHORITY_AUDIT.md`, commit `297168c2d7a8a411f582110ea4ba5d8c7dfa88eb`.

## RESULT / CLASSIFICATION

`BLOCKED_MISSING_CONTROL_TRANSFER_MODEL`

Secondary structural result:

`NULL_CONTROL_HAS_CALIBRATION_POWER_BUT_SHARED_NUISANCE_IS_NEW_OPERATIONAL_MODEL_CONTENT_SCOPED`.

No control-error model was imported or invented after the SF032 result.

## Exact audited question

SF032 proved that a matched delete-A connected-null control can remove the dominant PN calibration near-degeneracy **if** the relevant additive / `tau`-linear nuisance parameters are shared between science and control configurations.

SF033 asked whether that sharing equality is already a consequence of the current RQIRCGSF protocol.

The target was specifically

`n_tau^science = n_tau^deleteA`.

## Current protocol content

SF028B specifies an ideal unitary preparation/readout chain:

`U_prep = branch-conditioned translation`,

`U_read = U_prep^dagger`,

followed by trace over motion and qubit tomography.

It defines the ideal Newtonian/EIH evolution and the physical reduced coherence.

It does **not** define a pulse/readout/control-error generator, clock/electronics model, actuator dynamics, switching error, material response or stochastic parameter whose coefficient could be tracked between science and delete-A configurations.

The SF028B derivation notes explicitly exclude material branch-generation stresses, pulse hardware and finite-time control implementation from their authority.

## Delete-A null versus nuisance sharing

The exact delete-A result is strong but narrower:

`x_app=x_fb=x_1PN=0`

for the retained connected known-gravity basis.

This proves that delete-A is a valid gravity-null calibration channel at the modeled order.

It does not prove that an unmodeled control/readout phase is unchanged when the A displacement operation is disabled.

Thus

`GRAVITATIONAL NULL != SHARED CONTROL NUISANCE`.

## Six-element transfer-map audit

The preregistration required six physical elements for PASS:

1. explicit nuisance-generating operation;
2. its action on science protocol;
3. its action on delete-A protocol;
4. equality/symmetry reason for identical coefficient;
5. explicit fixed-versus-changed implementation variables;
6. physical falsification test of sharing.

Present at current authority level:

`0/6`.

The nominal phrase 'same readout' does not supply these missing elements because the current readout is an ideal mathematical operation, not an implementation-error model.

## Terminal decision

The PASS condition

`SCIENCE_NULL_NUISANCE_TRANSFER_MAP_DERIVED_SCOPED`

is not satisfied.

No existing model predicts unequal nuisance either, so the FAIL condition is also not satisfied.

The correct preregistered classification is

`BLOCKED_MISSING_CONTROL_TRANSFER_MODEL`.

This is a model-definition blocker, not evidence against null-control calibration.

## Relation to SF032

SF032 remains scientifically valid:

`MATCHED_NULL_CONTROL_BREAKS_COMMON_MODE_PN_NEAR_DEGENERACY_SCOPED`.

But its physical promotion remains conditional.

The new exact logical structure is

`VALID GRAVITY NULL`
`+ SHARED NUISANCE HYPOTHESIS`
`=> STRONG CALIBRATION POWER`,

while current authority only establishes the first term and the conditional implication.

It does not establish the shared-nuisance premise.

Therefore retain:

`CONTROL_CALIBRATION != PHYSICAL_TRANSFERABILITY`.

## New operational boundary

The next missing object is no longer a gravitational coefficient, another R/T scan, another Fisher matrix or another generic noise parameter.

It is an explicit **control/readout implementation map** connecting the science and null-control configurations.

Any future repair must be prospectively specified and must include, at minimum:

- physical displacement/control operations;
- the operation changed or disabled in delete-A;
- the phase/time reference;
- nuisance/error generator;
- shared versus configuration-specific error parameters;
- a falsifiable transfer test.

Those are new operational model data.

## Claim ceiling

SF033 does not establish:

- that a matched null control cannot work;
- that common-mode rejection is impossible;
- a detector or pulse architecture;
- laboratory feasibility;
- a control-error coefficient;
- a successor quantum residual;
- quantum-gravity dynamics;
- a quantum matching coefficient;
- GR-vs-QG discrimination;
- quantum `chi_ABC`;
- new physics.

Retain strictly:

`BLOCKED != FAIL`.

Theory track remains independently blocked on

`GENUINELY_NEW_MICROSCOPIC_MATCHING_PRINCIPLE_WITH_EXPLICIT_PHYSICAL_MAP_REQUIRED`.

## Exact next admissible operational action

`EXPLICIT_CONTROL_READOUT_IMPLEMENTATION_MODEL_REQUIRED`.

Do not continue neighboring abstract R/T/noise scans until such a model is prospectively supplied. Further operational progress without it would only reparameterize the same missing transfer datum.