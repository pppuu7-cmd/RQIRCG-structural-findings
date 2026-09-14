# SF003 — nonlinear gauge-closure selector gate — PREREGISTRATION

Date: 2026-09-14
Status: **PROSPECTIVE / PRE-OUTCOME**

## Motivation

SF001 showed that one closed generator can unify source and operational interfaces but does not select the generator class. SF002 showed that generic minimality cannot be promoted into a physical law without independent justification.

The strongest remaining inherited structure is gauge/relational redundancy: the weak-field carrier has linear spin-2 gauge symmetry and conserved-source compatibility, while the RQIR construction contract requires gauge/relational observable discipline.

## Candidate principle NGC

**Nonlinear Gauge Closure (NGC):**

> The nonlinear completion must arise as a consistent closure/deformation of the inherited carrier gauge redundancy and source constraint structure, preserving the physical gauge-orbit interpretation of the carrier and the closed-system conservation identities.

NGC does **not** preregister a derivative-order bound, Einstein-Hilbert action, GR equations, or a connected observable value.

## Frozen tests

### A — algebra closure
Determine whether nonlinear consistency forces deformation of the linear gauge transformations/constraint algebra and whether that deformation is unique up to field redefinitions and normalization already fixed by the weak-field coupling.

### B — invariant-vertex escape
Counterexample-first search: determine whether a local interaction functional can

1. begin above quadratic order around the inherited flat/weak-field background;
2. be exactly invariant under the relevant nonlinear gauge redundancy (or leave its algebra unchanged);
3. preserve the frozen quadratic carrier and pairwise weak-field limit;
4. modify genuine nonlinear response;
5. carry an independent coefficient not fixed by lower-order calibration.

If such a direction exists, NGC fails selector power even if the nonlinear gauge algebra itself is unique.

### C — physical-equivalence quotient
Quotient boundary/topological terms, invertible local field redefinitions, and terms proportional to lower-order equations when they do not change the physical response in the frozen domain. Only genuinely inequivalent vertices count against NGC.

### D — causal/constraint audit
Any surviving nonlinear direction must still face hyperbolicity/causality, constraint propagation, source closure, and positive operational reduction. Failure of a specific direction does not prove NGC uniqueness unless all inequivalent escapes are excluded by already-frozen principles.

## Decision rule

- `NGC_SELECTED_FOR_DERIVATION` only if the gauge/constraint closure uniquely fixes the nonlinear generator class relevant to the closed system, modulo the physical-equivalence quotient, without importing a derivative-order or no-new-scale axiom.
- `NGC_INSUFFICIENT_INVARIANT_VERTEX_FREEDOM_SURVIVES` if an inequivalent gauge-invariant nonlinear direction survives with the same frozen lower-order structure.
- `NGC_BLOCKED` if the necessary nonlinear gauge/source algebra cannot be defined from inherited structure.

No `chi_ABC` calculation is authorized by this gate.
