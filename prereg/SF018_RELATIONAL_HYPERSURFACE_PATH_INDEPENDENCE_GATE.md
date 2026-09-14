# SF018 — Relational Hypersurface Path Independence selector gate — PREREGISTRATION

Date: 2026-09-14
Status: **FROZEN PRE-LITERATURE-OUTCOME NEW-PRINCIPLE GATE**

## Context

SF012 established a representation-independent selector-fiber criterion. SF013 showed that exact global preservation of the inherited two graviton DOF has genuine selector power in a broad metric-only class. SF014/SF017 then showed that DOF counting plus a preferred variable name is insufficient: auxiliary geometry can relocate the same physical freedom into the source/matter sector.

SF018 therefore tests a stronger principle formulated on physical phase space and evolution rather than on Lagrangian variables.

`chi_ABC` remains embargoed.

## Candidate principle — RHPI

**Relational Hypersurface Path Independence (RHPI):**

> The complete local gravitational state on any spacelike relational hypersurface is exhausted, up to gauge, by its intrinsic spatial metric `h_ij` and conjugate momentum `pi^ij`. Infinitesimal normal and tangential deformations of such hypersurfaces represent changes of embedding into one physical spacetime, and composing those deformations is path/foliation independent. The canonical generators therefore realize the standard hypersurface-deformation algebra with structure functions determined by `h_ij`.

This is a new physical principle beyond frozen RQIR. It combines:

1. **phase-space completeness** — no independent auxiliary gravitational canonical datum beyond `(h_ij, pi^ij)`;
2. **relational embeddability** — evolution is deformation of physical spatial geometry rather than evolution relative to a preferred external time;
3. **path independence** — different infinitesimal foliations connecting the same physical hypersurfaces agree modulo the canonical constraints.

The principle does **not** pre-insert the ADM Hamiltonian, Einstein equations, a derivative order, or a curvature scalar potential.

## Frozen algebraic target

Let `H_i(x)` generate tangential deformations and `H_perp(x)` normal deformations. RHPI requires a representation of the hypersurface-deformation algebra (schematically, up to sign/convention):

`{H_i(x), H_j(y)} ~ H_i(y) partial_j delta + H_j(x) partial_i delta`,

`{H_perp(x), H_i(y)} ~ H_perp(y) partial_i delta`,

`{H_perp(x), H_perp(y)} ~ h^{ij}(x) H_i(x) partial_j delta - (x <-> y)`.

The precise density/sign convention is not frozen as physics; the geometric algebraic content is.

## Scientific question

Within the declared complete metric phase space, does RHPI uniquely determine the nonlinear gravitational Hamiltonian/constraint class from the inherited weak-field normalization, or do inequivalent local two-DOF dynamics realize the same geometric deformation algebra?

## Positive criterion

Return

`RHPI_SELECTS_ADM_EINSTEIN_GEOMETRODYNAMICS_SCOPED`

only if an audited reconstruction theorem establishes, within explicitly stated assumptions independently compatible with the RQIRCG architecture, that the constraint representation is unique up to:

- the already calibrated Newton normalization/sign convention;
- a cosmological constant/background datum not fixed by RHPI;
- canonical transformations / physical equivalence;
- boundary or topological terms that do not change local dynamics.

The theorem must derive the Hamiltonian form rather than assume it through an ansatz equivalent to two-derivative Einstein dynamics.

## Counterexample-first failure criterion

Return

`RHPI_INSUFFICIENT_ALTERNATIVE_GEOMETRODYNAMICS_SURVIVE`

if there exist physically inequivalent local Hamiltonian constraints on the same complete `(h_ij,pi^ij)` phase space that:

1. realize the same undeformed hypersurface-deformation algebra;
2. preserve exactly two local gravitational DOF on generic backgrounds;
3. recover the inherited weak-field massless-spin-2/Newton branch;
4. differ in nonlinear dynamics by a genuine physical coupling/function.

## Assumption quarantine

The following may **not** be silently treated as consequences of RHPI unless the theorem audit proves or independently motivates them:

- polynomial or quadratic dependence on `pi^ij`;
- ultralocality in momenta;
- at most second spatial derivatives of `h_ij`;
- time-reversal invariance;
- a particular DeWitt supermetric;
- the scalar-curvature potential `sqrt(h) R`;
- Einstein-Hilbert action;
- absence of canonical transformations or equivalent constraint rescalings.

If uniqueness depends essentially on one of these assumptions, SF018 must state that the selector is the **compound package**, not RHPI alone.

## Mandatory lanes

### Lane A — HKT/reconstruction theorem audit
Read Hojman-Kuchar-Teitelboim-type reconstruction results and identify the exact theorem assumptions, derived objects, residual constants and uniqueness scope.

### Lane B — assumption necessity audit
For every non-geometric technical assumption used in the reconstruction, determine whether it follows from phase-space completeness/path independence/locality already frozen here or whether it is extra microscopic information.

### Lane C — counterexample/deformed-algebra audit
Search for alternative canonical gravities, deformed hypersurface algebras, strong-gravity/ultralocal branches, higher-curvature theories and canonical reformulations. Distinguish:

- exact same standard algebra on the same physical phase space;
- deformed algebra / preferred foliation;
- enlarged phase space;
- canonical-equivalent rewritings.

Only the first category is a decisive RHPI counterexample.

### Lane D — source-interface consequence
Determine what RHPI fixes for the pure gravitational generator and what remains unfixed about coupling to the closed matter/apparatus system. Do not infer universal source coupling unless it is actually entailed by total hypersurface path independence.

## Selector-fiber interpretation

SF012 applies directly. RHPI has genuine selector power only if adding the hypersurface-deformation representation condition strictly shrinks the physical completion fiber rather than merely choosing ADM coordinates for an already free theory.

## Claim ceiling

A positive result is a scoped reconstruction of classical local geometrodynamics, not proof of quantum gravity, not experimental confirmation, and not by itself a unique quantum measure/state. `chi_ABC` remains closed until all theory-law blockers needed for its parent map are prospectively resolved.

## Next-step rule

- If RHPI uniquely selects pure geometrodynamics but leaves matter/source coupling free, the next gate must impose path independence on the **total closed gravity+matter phase space** with independently fixed flat-space matter physics.
- If RHPI itself is insufficient, record the surviving same-algebra counterexample or the exact extra theorem assumptions needed.
