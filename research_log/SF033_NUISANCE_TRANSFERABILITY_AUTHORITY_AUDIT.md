# SF033 — nuisance-transferability authority audit

Date: 2026-09-15
Preregistration: `518409ca497882baa3bad546a01836d4c075139d`.

## Audited authority

The audit was restricted prospectively to the protocol chain named in the preregistration.

### SF028B protocol definition

`U_prep` is an ideal branch-conditioned translation. `U_read=U_prep^dagger` is an ideal inverse translation. The final object is a reduced three-qubit density matrix reconstructed by tomography.

The preregistration defines no stochastic or systematic pulse/readout error generator, no electronics/clock model, and no parameter describing a `tau`-linear nuisance.

### SF028B derivation/source notes

The notes derive the gravitational coherence under the ideal controlled translation/free-evolution/inverse-translation protocol.

They explicitly state that the finite-size authority is **not** an engineering model of material deformation, branch-generation stresses, pulse hardware or finite-time control implementation.

The atom-interferometer literature is used only as an external sanity check that propagation, interaction/control and readout contributions jointly define an observable; no external apparatus is imported into RQIRCGSF.

### Delete-one-label authority

The SF028B/SF029 exact controls establish that deleting any one source displacement makes the retained connected known-gravity coefficients vanish.

This gives a valid gravitational null channel.

It does **not** specify how a real control/readout error changes when one displacement operation is removed.

### SF032 calibration authority

SF032 explicitly introduced the sharing equality only as a prospectively frozen statistical hypothesis and retained

`NULL_CONTROL_CALIBRATION_BLOCKED_BY_UNVALIDATED_SHARED_NUISANCE_MAP`.

Thus SF032 did not itself create physical transfer authority.

## Six required transfer-map elements

The SF033 preregistration required all six elements for PASS.

### 1. Explicit nuisance-generating control/readout operation

Status: **ABSENT**.

Current authority contains ideal unitary preparation/readout but no physical error generator producing the abstract `tau`-linear nuisance.

### 2. Action on science protocol

Status: **ABSENT** as an error model.

The ideal science protocol is explicit, but no nuisance operation is composed with it.

### 3. Action on delete-A protocol

Status: **ABSENT** as an error model.

The delete-A known-gravity null is explicit, but the changed control implementation is not modeled.

### 4. Equality/symmetry reason for identical nuisance coefficient

Status: **ABSENT**.

No existing symmetry theorem says that disabling one branch displacement leaves a pulse/readout/clock error coefficient invariant.

The fact that the nominal readout concept is the same does not prove equality of implementation errors.

### 5. Fixed versus changed hardware/control variables

Status: **ABSENT**.

The abstract protocol does not define the pulse sequence, actuator, timing electronics, switching operation, control field, material response or detector degrees needed to state this comparison.

### 6. Falsification condition for nuisance sharing

Status: **ABSENT** physically.

SF032 contains a statistical no-sharing ablation, but no hardware-level observable or calibration test whose failure would falsify transferability in an implementation.

## Decision

Required PASS elements present: `0/6` at the physical transfer-map level.

The current protocol supplies the **logical benefit** of a shared nuisance and a valid gravitational null channel, but not the physical map that makes the nuisance shared.

Therefore the preregistered result is

`BLOCKED_MISSING_CONTROL_TRANSFER_MODEL`.

This is not evidence that matched controls fail. It is a model-definition boundary.

## What a future repair must add prospectively

A new control/readout implementation gate must specify at minimum:

- the physical operation implementing each source displacement;
- what changes in the delete-A configuration;
- the timing/readout phase reference;
- the nuisance/error generator and its parameterization;
- which parameters are common by construction and why;
- at least one independent measurement or symmetry test of the transfer relation.

That content would be new operational model information, not an inference from the SF032 Fisher improvement.

## Claim ceiling

No detector failure, no impossibility of common-mode rejection, no hardware recommendation, no feasibility claim, no new-gravity residual and no quantum-law statement follows from this audit.