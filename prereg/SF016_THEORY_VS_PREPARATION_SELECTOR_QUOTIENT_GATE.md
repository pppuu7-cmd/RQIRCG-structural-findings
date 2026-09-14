# SF016 — theory-vs-preparation selector quotient gate — PREREGISTRATION

Date: 2026-09-14
Status: **FROZEN PRE-OUTCOME CONCEPTUAL/OPERATIONAL GATE**

## Motivation

SF015 showed that a fixed local gravitational generator admits many quantum states/influence kernels. But a physical theory is not normally required to select one unique state of the universe for every experiment. States can be controlled inputs or measured nuisance variables.

SF016 prevents a category error: counting legitimate protocol inputs as theory underdetermination.

`chi_ABC` remains embargoed.

## Frozen decomposition

Write a prediction abstractly as

`P(o | s, theta, nu)`

where:

- `theta` = theory-law data (dynamical generator, fundamental couplings, source ontology, quantization rule);
- `s` = declared controllable preparation/settings, including matter/source branch preparation and any operationally specifiable gravitational input state;
- `nu` = nuisance/uncontrolled environmental or calibration data with a declared measurement/prior model.

A theory is predictive for a protocol if `theta` is selected/fixed and `s,nu` are either experimentally specified or statistically identifiable/calibrated to the required accuracy.

## Scientific question

Which part of the SF015 quantum-state fiber is genuine theory-law underdetermination, and which part is ordinary preparation/nuisance freedom that may be conditioned on without adding a new physical principle?

## Theory-selector criterion

A family does **not** count as a residual theory fiber merely because different declared preparations `s` produce different outcomes under the same law.

A residual theory fiber remains only if two physically inequivalent `theta_1 != theta_2` give different predictions for the same fully specified admissible `(s,nu)` while all inherited theory-level constraints are identical.

## Preparation admissibility criterion

A gravitational state datum may be treated as `s` only if:

1. its operational meaning is specified (e.g. asymptotic incoming state, finite-region Gaussian covariance, no-incoming-radiation condition);
2. the theory supplies its evolution once prepared;
3. the protocol can in principle prepare, certify, bound, or condition on it to the claimed accuracy;
4. it is not secretly a theory coupling/measure rewritten as a state label.

If these fail, the datum remains part of `theta` or `nu`, not a free preparation excuse.

## Mandatory lanes

### Lane A — standard quantum-control sanity check
Confirm that multiple states under one Hamiltonian do not constitute multiple theories.

### Lane B — RQIR compatibility
Use RQIR's explicit inclusion of state preparation/settings in the observable index and Candidate Gravity contract to determine whether conditioning on state/preparation is methodologically allowed.

### Lane C — gravitational state audit
Classify vacuum/incoming radiation/Gaussian covariance choices into theory, preparation, or nuisance categories in the weak-field laboratory domain.

### Lane D — consequence for the `chi_ABC` embargo
Determine whether state nonuniqueness alone remains a blocker to eventually computing a **conditional** connected prediction after a dynamical principle is selected.

## Pass/terminal labels

If the state fiber is largely protocol-level rather than theory-level, return

`QUANTUM_STATE_MULTIPLICITY_IS_NOT_BY_ITSELF_THEORY_UNDERDETERMINATION_SCOPED`.

If the relevant gravitational state cannot be operationally specified/calibrated and its law is not fixed, return

`GRAVITATIONAL_STATE_REMAINS_UNCONTROLLED_THEORY_OR_NUISANCE_BLOCKER_SCOPED`.

Both can coexist for different state components; classification must be explicit.

## Claim ceiling

SF016 does not choose a vacuum or compute `chi_ABC`. It only repairs the selector accounting so that the programme demands uniqueness of laws, not uniqueness of all physical states.
