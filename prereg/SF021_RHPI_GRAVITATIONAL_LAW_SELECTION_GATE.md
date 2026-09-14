# SF021 — RHPI gravitational-law prospective selection gate — PREREGISTRATION

Date: 2026-09-14
Status: **FROZEN PRE-SELECTION / `chi_ABC` STILL EMBARGOED**

## Purpose

SF001-SF020 searched for a new principle capable of reducing the nonlinear selector fiber without choosing a preferred connected outcome. SF021 is the first formal **selection** gate: it asks whether the accumulated evidence is now sufficient to adopt Relational Hypersurface Path Independence (RHPI) as the principle that fixes the classical local gravitational law for the next phase of the project.

No connected three-source phase may be calculated until SF021 is terminalized.

## Candidate principle to be selected

The candidate is **Strong Relational Hypersurface Path Independence (RHPI-S)**:

> The local physical gravitational canonical state on a relational spacelike hypersurface is exhausted, up to gauge, by its intrinsic spatial metric `h_ij` and conjugate momentum `pi^ij`. These variables represent embeddable spatial geometry. Normal and tangential deformations of hypersurfaces must compose as one spacetime geometry, with path/foliation independence represented by the standard strong hypersurface-deformation structure and the correct geometric action on `h_ij`.

RHPI-S is selected as a **gravitational-law principle**, not as a complete microscopic quantum theory and not as a claim that all source constitutive parameters are determined by gravity.

## Candidate law class if selected

Within the audited HKT/geometrodynamical scope, RHPI-S implies the ADM/Einstein pure gravitational constraint class, modulo:

- Newton normalization `G`, already inherited/calibrated;
- cosmological/background datum `Lambda`, to be frozen independently for the laboratory protocol;
- canonical/field equivalence;
- boundary/topological terms that do not alter local equations.

No arbitrary cubic/higher connected gravitational coefficient is permitted.

## Frozen source/data separation

Following SF016 and SF020, source properties are separated from gravitational-law parameters.

### Allowed independently frozen protocol/source data

- masses and branch configurations;
- finite-size density profiles / apparatus geometry;
- internal material/tidal response parameters if relevant at the retained order;
- prepared incoming gravitational state/boundary condition when required;
- nuisance data independently measured or bounded.

### Forbidden as post-selection gravitational fit parameters

- a free connected `lambda` or `gamma`;
- an arbitrary higher-curvature gravitational Wilson coefficient not implied by RHPI-S;
- an auxiliary source/geometry coupling introduced solely to tune `chi_ABC`;
- a branch-dependent gravitational rule chosen after seeing the connected result.

Any source constitutive coefficient retained in the calculation must be fixed before `chi_ABC` and have independent operational provenance.

## Selection criteria

RHPI-S may be selected only if all criteria S1-S8 pass.

### S1 — prospective independence
The principle was motivated and tested while `chi_ABC` remained embargoed; its selection must not depend on sign, magnitude or nonzero value of the connected observable.

### S2 — genuine selector-fiber reduction
Using SF012, RHPI-S must reduce the physical pure-gravity completion fiber, not merely reparameterize it.

### S3 — physical DOF
The selected law must retain the inherited massless spin-2 gravitational phase-space content and not require extra local gravitational DOF in the selected domain.

### S4 — nonlinear dynamics
The principle must determine an actual nonlinear gravitational evolution/constraint law rather than another consistency bound.

### S5 — conservation / constraint closure
The selected law must possess the nonlinear constraint/Bianchi structure needed for closed total source evolution.

### S6 — causal solution prescription
A retarded/causal classical branch-history prescription must be admissible as a protocol boundary condition without changing the local selected law.

### S7 — inherited weak-field recovery
The selected law must recover the already validated Newtonian/pairwise weak-field branch after fixing `G` and the source protocol.

### S8 — no connected gravitational coefficient by hand
Once RHPI-S and source protocol data are frozen, any higher connected classical gravitational contribution must be derived from the selected nonlinear law. It may turn out to be zero or nonzero; either outcome is acceptable. No independent connected gravitational coefficient may be introduced.

## Failure conditions

Return

`RHPI_NOT_READY_FOR_SELECTION`

if any of the following holds:

- the HKT/RHPI uniqueness evidence still depends on an unacknowledged arbitrary gravitational coefficient;
- a decisive same-phase-space, same-strong-HDA inequivalent gravitational counterexample survives;
- the source/model separation is ill-defined so that a free gravity coefficient can be relabeled as a source input;
- no causal branch-history prescription can be defined;
- weak-field recovery requires changing the selected principle.

## Positive decision

If S1-S8 pass, return

`RHPI_SELECTED_AS_CLASSICAL_GRAVITATIONAL_LAW_PRINCIPLE_SCOPED`.

This authorizes **only the next classical/semiclassical coherent-phase derivation**. It does not authorize claims of new physics, unique quantum gravity, unique noise, or quantum-state selection.

## Post-selection lock

If selected, freeze before opening the connected observable:

1. the exact ADM/RHPI normalization and sign conventions;
2. laboratory `Lambda` treatment;
3. the G97-compatible three-source + apparatus preparation model;
4. source profiles/finite-size approximation order;
5. retarded/no-incoming boundary prescription;
6. branch phase convention inherited from the validated pairwise bridge;
7. perturbative expansion order needed for the first genuinely connected classical contribution.

Only after these objects are committed may the first `chi_ABC` calculation be performed.
