# SF016 — theory-vs-preparation selector quotient gate — TERMINAL

Date: 2026-09-14
Status: **TERMINAL / selector accounting corrected / no `chi_ABC` evaluation**

Preregistration: `f28d13e8351e8f602758dd05c1c4c904b91595e1`.

## Lane A — standard quantum-control sanity check

A Hamiltonian or quantum field theory does not become a different theory for every allowed state in its state space.

If one fixed law `theta` maps each admissible initial state `rho(s)` to a unique later state and outcome distribution, then

`rho_1 != rho_2`

under the same dynamics represents different physical preparations, not theory-law underdetermination.

Therefore SF015's state-dependent Hadamard/noise kernel proves nonuniqueness of the **unconditional parent influence object**, but it does not by itself prove nonuniqueness of the underlying theory.

Lane classification:

`MULTIPLE_STATES_OF_ONE_FIXED_LAW_ARE_NOT_MULTIPLE_THEORIES`.

## Lane B — compatibility with frozen RQIR methodology

This distinction is already built into RQIR.

`docs/FOUNDATIONS.md` states that the observable index includes experimental settings and **state preparation**, along with smearing/coarse-graining, detector response and renormalization data required for the operational observable.

The abstract interface map explicitly takes `rho_matter` and other setting/model data as inputs rather than demanding a single universal state.

The Candidate Gravity contract separately requires a model to declare state preparation and boundary conditions, then derive the source hierarchy and operational maps from the same declared dynamics.

Therefore conditioning predictions on a frozen preparation is methodologically legitimate and is not a post-hoc escape from theory selection.

Lane classification:

`RQIR_EXPLICITLY_PERMITS_STATE_PREPARATION_AS_PROTOCOL_INPUT`.

## Lane C — gravitational state classification

The SF015 residual data separate into distinct categories.

### Legitimate protocol input `s`

Examples, when operationally specified in the target domain:

- incoming weak gravitational coherent/wavepacket state;
- a declared Gaussian covariance state that can in principle be prepared or independently certified;
- a no-incoming-radiation/asymptotic-vacuum boundary condition used as part of a scattering/laboratory preparation protocol;
- source/apparatus branch state and timing protocol.

These do not need to be predicted by the gravitational law if the experiment declares them as inputs.

### Nuisance `nu`

Examples:

- uncontrolled ambient gravitational-wave/background covariance;
- thermal/environmental occupation that is not intentionally prepared but can be measured/bounded/marginalized;
- calibration uncertainty in the effective incoming state.

These require an identifiability/calibration model, not a new fundamental gravity law merely because they are uncertain.

### Theory-law data `theta`

The following cannot be demoted to preparation labels:

- the physical Hilbert/state-space structure itself;
- commutation/algebra rules;
- fundamental path-integral/CTP measure;
- contour/unitarity prescription insofar as it defines the theory rather than a chosen experiment;
- renormalization law and fundamental couplings;
- source/geometry ontology;
- rules determining which states are admissible and how they evolve.

These remain selector-level content.

Lane classification:

`GRAVITATIONAL_STATE_FIBER_SPLITS_INTO_PREPARATION_NUISANCE_AND_THEORY_COMPONENTS`.

## Lane D — consequence for the connected-observable embargo

State multiplicity alone is **not** a sufficient reason to keep `chi_ABC` forever undefined.

Once a theory law `theta` is selected, one may legitimately predict a conditional observable

`chi_ABC | s,nu`

for a prospectively frozen preparation and nuisance model.

However SF016 does not yet authorize that calculation because the more fundamental theory-level source/geometry ambiguity from SF014 remains unresolved, and the quantum measure/quantization-law component of `theta` has not been selected.

Thus the correct blocker is narrower than SF015 initially suggested:

`not unique state` — **not by itself a theory blocker**;

`not unique law/source ontology/quantization rule` — **still a blocker**.

Lane classification:

`CONDITIONAL_CONNECTED_PREDICTION_IS_METHODologically_VALID_ONCE_THEORY_LAW_IS_SELECTED`.

## Terminal decision

Record both scoped outcomes:

`QUANTUM_STATE_MULTIPLICITY_IS_NOT_BY_ITSELF_THEORY_UNDERDETERMINATION_SCOPED`

and

`THEORY_LEVEL_MEASURE_SOURCE_ONTOLOGY_REMAIN_SELECTOR_BLOCKERS_SCOPED`.

## New structural finding

The selector fiber should henceforth be defined **conditional on protocol inputs**:

`F_theta(y0 | s,nu)`

rather than over all possible physical states indiscriminately.

This prevents the programme from demanding an impossible and unnecessary “unique state of Nature” before making a laboratory prediction.

The genuinely missing information has now narrowed to theory-law content:

1. source/geometry ontology beyond GDP's propagating-DOF rule;
2. fundamental quantum measure/algebra/evolution prescription;
3. any true couplings not fixed by inherited calibration.

## Exact next admissible gate

The next high-value test is **Source-Metric Sufficiency** in a representation-invariant operational form.

The gate must ask whether auxiliary metric-affine completions are genuinely distinct gravity-interface theories after independently frozen matter physics is held fixed, or whether their effects can always be reclassified as matter-sector operators under an invertible field redefinition.

This is critical because SF012 forbids calling a change of variables a selector. The next gate must compare physical predictions with the *same frozen matter calibration*, not merely compare Lagrangian labels.

`chi_ABC` remains embargoed pending that audit.
