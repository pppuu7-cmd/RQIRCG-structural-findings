# SF015 — quantum state/influence closure after local-dynamics selection — TERMINAL

Date: 2026-09-14
Status: **TERMINAL / parent quantum object remains nonunique / no `chi_ABC` evaluation**

Preregistration: `ef784ba5b8868b26433c82a00781390906a04f8a`.

## Outcome lock

No connected three-source phase was evaluated. SF015 asks whether selecting a local classical generator is enough to select the quantum parent influence object.

## Lane A — state versus dynamics

Fix a linear bosonic field generator, including the linearized graviton as the relevant control case.

The canonical commutator/Pauli-Jordan function and retarded Green function are fixed by the field equations, canonical algebra and causal boundary prescription. For a free linear field, this commutator is a c-number and does not depend on whether the field is in vacuum, thermal, squeezed or another admissible Gaussian state.

By contrast, the symmetrized/Hadamard covariance

`G_H(x,y) = < {h(x),h(y)} >/2`

is state dependent.

Therefore two quantum states can share the same local classical equations and the same retarded response while possessing different fluctuation/noise kernels.

This distinction is already native to frozen RQIR Foundations: RQIR separately tracks symmetrized noise `N`, commutator/antisymmetric kernel `D`, retarded response `chi^R`, and a parent CTP generating functional

`Z_T[J_+,J_-] = Tr(U[J_+] rho_T U[J_-]^dagger)`.

The explicit appearance of `rho_T` is exactly the state datum GDP does not determine.

Lane classification:

`FIXED_LOCAL_GENERATOR_AND_RETARDED_RESPONSE_DO_NOT_FIX_SYMMETRIZED_QUANTUM_COVARIANCE`.

## Lane B — closed-system constraint

“Closed total source + gravity” removes an uncontrolled external environment from the dynamical bookkeeping. It does not mathematically choose one initial global quantum state from the Hilbert/state space of the closed system.

A closed Hamiltonian system admits many pure states and density operators. Unitary evolution preserves closure for all of them.

Likewise, G97 source closure ensures the apparatus/support is included in the conserved preparation system; it supplies no theorem selecting a unique gravitational vacuum, squeezed state, incoming-radiation condition, or global branch wavefunctional.

Thus

`closed dynamics`

is not equivalent to

`unique closed-system state`.

Lane classification:

`CLOSED_TOTAL_SYSTEM_DOES_NOT_SELECT_GLOBAL_QUANTUM_STATE`.

## Lane C — influence-functional consequence

For a Gaussian mediator/field, integrating out the field produces an influence functional whose causal/retarded part is controlled by the commutator/retarded kernel and whose fluctuation/decoherence part is controlled by the Hadamard/symmetrized covariance.

Hence different admissible field states can produce the same classical retarded force law while changing the noise/dephasing influence kernel.

At higher order, interacting states and contour/boundary prescriptions can also change higher CTP cumulants even when the local action is held fixed.

Therefore selecting an Einstein-Hilbert-like `Gamma_cl` does not by itself select the parent operational channel.

This result is deliberately made at the parent-object level. It does not assert that every state dependence survives every particular connected finite difference; that would require opening the `chi_ABC` calculation, which remains forbidden.

Lane classification:

`QUANTUM_INFLUENCE_OBJECT_REQUIRES_STATE_MEASURE_CONTOUR_DATA_BEYOND_CLASSICAL_ACTION`.

## Lane D — selector-fiber interpretation

Using SF012 notation, GDP can strongly reduce the **action-coordinate fiber** in the metric-only classical sector.

But the full microscopic point is more like

`p = (Gamma_cl, Q)`

with

`Q = {rho_g, measure, contour, boundary prescription, renormalized state data, ...}`.

A judge map that fixes `Gamma_cl` while remaining insensitive to `Q` leaves a residual quantum fiber

`F_Q(Gamma_cl) = {Q admissible for the same local dynamics}`.

SF015 exhibits this fiber already in the linear Gaussian control case through states with identical retarded response and different Hadamard covariance.

Thus GDP reduces one physical fiber direction but does not collapse the full microscopic fiber to a singleton.

Lane classification:

`GDP_SHRINKS_DYNAMICAL_ACTION_FIBER_BUT_LEAVES_QUANTUM_STATE_MEASURE_FIBER`.

## Terminal decision

The preregistered failure criterion is satisfied:

`CLASSICAL_GENERATOR_SELECTION_DOES_NOT_FIX_QUANTUM_STATE_INFLUENCE_DATA`.

## New structural finding

A complete nonlinear operational prediction requires **two distinct selections**:

1. a law for the local gravitational generator/source ontology;
2. a law for the quantum state/measure/boundary data used to construct the influence functional.

The first plausible selector found so far is GDP within a metric-only scope. The second is still missing.

This explains why a classical uniqueness result cannot automatically resolve the NP1 phase/noise hierarchy: even a uniquely selected local action can admit multiple quantum parent states/influence kernels.

## Exact next admissible work

Before `chi_ABC` can be opened, at least two principle questions remain:

### P1 — Source-Metric Sufficiency
Does a principled requirement force matter/apparatus to couple only through the same physical metric carrier, excluding auxiliary geometric source maps such as the SF014 escape without merely banning variables by convention?

### P2 — Quantum State Selection
Is there an independently motivated rule selecting the relevant closed gravitational state/measure/contour in the laboratory weak-field domain (for example an asymptotic/no-incoming condition, ground-state condition, relational preparation rule, or other state principle)?

Neither principle is currently derived.

`chi_ABC` remains embargoed.
