# SF018 — Relational Hypersurface Path Independence selector gate — TERMINAL / PARTIAL POSITIVE

Date: 2026-09-14
Status: **TERMINAL FOR FROZEN RHPI / PARTIAL POSITIVE PURE-GRAVITY SELECTOR / no `chi_ABC` evaluation**

Preregistration: `9af7a56db5e581185dbb2fb26747c9b27c22ad5a`.

## Outcome lock

The RHPI decision rule was frozen before the dedicated HKT/theorem audit. `chi_ABC` remained embargoed throughout.

## Executive classification

SF018 yields two simultaneous results:

`POSITIVE_SCOPED: STRONG_GEOMETRODYNAMICAL_EMBEDDABILITY_PLUS_REVERSIBILITY_SELECTS_ADM_GRAVITY`

and

`BLOCKED_AS_FROZEN: RHPI_ALONE_DOES_NOT_YET_JUSTIFY_ALL_HKT_SELECTION_POSTULATES_OR_SOURCE_DYNAMICS`.

This is stronger than SF013 in one important respect: the positive mechanism is formulated directly on physical canonical geometry and hypersurface evolution rather than by banning higher-curvature Lagrangians. But the pure-gravity reconstruction and the matter/source problem must not be conflated.

## Lane A — HKT / reconstruction theorem audit

The original Hojman-Kuchar-Teitelboim result is explicitly a uniqueness statement for pure geometrodynamics: Einsteinian geometrodynamics is the unique **time-reversible** canonical representation of hypersurface deformations when the intrinsic metric of the hypersurface and its conjugate momentum are the sole canonical variables.

Primary reference:

- S. A. Hojman, K. Kuchar, C. Teitelboim, *Geometrodynamics Regained*, Annals of Physics 96 (1976) 88–135, DOI `10.1016/0003-4916(76)90112-3`.

The earlier Lagrangian reconstruction by Kuchar gives the same structural message: the ADM super-Lagrangian is the unique representation of hypersurface deformations when the intrinsic spatial geometry is the sole gravitational configuration variable.

- K. Kuchar, *Geometrodynamics regained: A Lagrangian approach*, J. Math. Phys. 15 (1974) 708.

A modern geometric analysis strengthens the interpretation of the constraint algebra. Głowacki derives the ADM hypersurface-deformation Poisson-bracket structure from consistency of geometrodynamical evolution and then states the resulting HKT consequence as:

`the only consistent time-reversal pure geometrodynamics is the ADM gravity.`

- J. Głowacki, *Inevitability of the Poisson Bracket Structure of the Relativistic Constraints*, Found. Phys. 51, 111 (2021).

Thus the standard Dirac/HDA bracket structure need not be viewed as an arbitrary ADM-inspired ansatz once the geometric interpretation of hypersurface evolution is imposed.

Lane classification:

`STRONG_EMBEDDABLE_METRIC_GEOMETRODYNAMICS_HAS_THEOREM_LEVEL_ADM_SELECTION_POWER_WITH_REVERSIBILITY`.

## Lane B — assumption-necessity audit

The detailed HKT tradition contains more structure than the slogan “the constraints close.” Kouletsis summarizes the original postulates as:

1. lapse-shift form of evolution;
2. strong representation of the Dirac/hypersurface-deformation algebra;
3. correct tangential reshuffling of intrinsic metric data;
4. ultralocal normal update of the intrinsic metric in the canonical momenta;
5. reversibility;
6. path independence.

- I. Kouletsis, *A classical history theory: Geometrodynamics and general field dynamics regained*, arXiv:`gr-qc/9801019`.

This audit produces two important refinements.

### B1 — reshuffling / ultralocality are not arbitrary coefficient choices

Kouletsis shows in the history formalism that once the configuration variable is literally the pullback of the spacetime metric, the tangential reshuffling rule and ultralocality of its normal deformation follow from that geometric meaning. This supports treating them as part of **embeddable metric phase-space completeness**, rather than as a hidden Einstein potential.

### B2 — reversibility is additional information

Time-reversibility remains explicit in the HKT uniqueness statement. The frozen RHPI preregistration did not separately postulate microscopic time-reversal invariance. Therefore SF018 cannot silently promote the HKT theorem to `RHPI alone => ADM`.

A recent modified-gravity review also phrases the HKT theorem with an explicit regularity restriction that the deformation generators involve no more than second derivatives of the induced metric. Whether this is a presentation of the locality class used in the theorem or an independently indispensable axiom does not need to be resolved by overclaim here: the correct scientific classification is that the strongest clean uniqueness statement belongs to a **scoped geometrodynamical regularity class**, not to every conceivable functional on `(h,pi)`.

Representative comparator:

- J. Ben Achour, *DHOST theories as disformal gravity: from black holes to radiative spacetimes*, Eur. Phys. J. C 85, 424 (2025), HKT review section.

Lane classification:

`RHPI_GEOMETRY_MOTIVATES_MOST_HKT_KINEMATIC_POSTULATES_BUT_REVERSIBILITY_AND_REGULARITY_SCOPE_REMAIN_EXPLICIT_SELECTION_INPUTS`.

## Lane C — counterexample / algebra audit

A crucial adversarial result comes from the weak-algebra analysis.

Kouletsis exhibits, when only the weak Dirac/path-independence condition is imposed, an infinite family of normal generators of the form

`H = sqrt(g) W[h,f]`,

where `W` solves a first-order equation and the solution family is parametrized by an arbitrary function of one variable. The GR super-Hamiltonian is the special `W=h` member and is singled out by the geometric ultralocality condition in the momenta.

Therefore:

`weak path independence / on-constraint closure != unique dynamics`.

This is a direct counterexample to any weaker reading of RHPI.

Conversely, the common modified-gravity escape routes do not provide a decisive counterexample to the **strong** RHPI package:

- spatially covariant/minimally modified two-DOF theories relax the full spacetime HDA;
- deformed-HDA quantum-gravity models change the algebra;
- higher-derivative fundamental metric theories require enlarged canonical data or violate the frozen phase-space completeness if their extra exact modes are retained;
- Shape Dynamics trades refoliation symmetry for a different gauge symmetry and is not a second inequivalent realization of the same strong HDA on exactly the same physical phase space.

A 2016 rigidity result also supports the strength of the canonical restriction: broad spatially covariant scalar-constraint deformations quadratic in the momenta become second class rather than producing new first-class GR-like geometrodynamics.

- H. Gomes, V. Shyam, *Extending the rigidity of general relativity*, J. Math. Phys. 57, 112503 (2016), arXiv:`1608.08236`.

Lane classification:

`WEAK_HDA_NONUNIQUE_BUT_NO_DECISIVE_INEQUIVALENT_STRONG_RHPI_SAME_PHASE_SPACE_COUNTEREXAMPLE_FOUND_IN_SCOPED_CLASS`.

## Lane D — source-interface consequence

The pure-gravity result does **not** automatically solve the RQIRCG source problem.

Kuchar's Lagrangian reconstruction explicitly notes that the pure geometrodynamical uniqueness does not extend to arbitrary source-field super-Lagrangians. Path independence constrains matter couplings, but many covariant matter theories can satisfy the same geometric deformation algebra.

Głowacki likewise finds that the bracket structure is insensitive to matter content for standard non-derivative metric coupling. In other words, the HDA determines the geometric covariance structure but does not uniquely specify the matter Hamiltonian/source constitutive law.

This is exactly where the SF014/SF017 auxiliary-geometry/source-map issue reappears in canonical language.

Lane classification:

`RHPI_CAN_SELECT_PURE_GRAVITATIONAL_GEOMETRODYNAMICS_WITHOUT_SELECTING_COMPLETE_MATTER_SOURCE_HAMILTONIAN`.

## Selector-fiber interpretation

SF012 makes the result precise.

The old pure-gravity fiber contained inequivalent nonlinear action/constraint directions. Adding strong metric embeddability/HDA plus the HKT regularity/reversibility package collapses that **pure geometrodynamical** fiber to the ADM/Einstein class, modulo Newton normalization, cosmological constant, canonical equivalence and boundaries.

This is genuine selection information, not a field redefinition.

However the total closed gravity+matter fiber remains non-singleton because the source Hamiltonian/coupling sector is not fixed by the pure-gravity theorem.

## Relation to GDP

GDP and RHPI are not independent accidents.

- GDP says the nonlinear theory must not enlarge the physical gravitational initial-data content.
- RHPI says those metric canonical data must compose as embeddable, foliation-independent hypersurface geometry.

Within their common local metric domain, both point toward the ADM/Einstein class from different directions. This independent convergence is scientifically stronger than either argument alone.

RHPI is conceptually cleaner with respect to SF014/SF017 because it formulates the selector on canonical physical geometry rather than merely naming a preferred Lagrangian variable.

## Terminal decision

Record:

`PARTIAL_PASS: STRONG_RHPI_PLUS_REVERSIBILITY_SELECTS_ADM_EINSTEIN_PURE_GEOMETRODYNAMICS_SCOPED`

`BLOCKED: REVERSIBILITY/REGULARITY_SCOPE_NOT_YET_DERIVED_FROM_FROZEN_RHPI_ALONE`

`BLOCKED: TOTAL_CLOSED_MATTER_SOURCE_DYNAMICS_NOT_SELECTED_BY_PURE_HKT_RESULT`.

## New scientific finding

The most promising selector found so far is no longer “minimality” or “two DOF” in isolation. It is the compound physical idea:

`complete intrinsic metric phase space`
`+ embeddable/path-independent hypersurface evolution`
`+ microscopic reversibility`
`=> ADM/Einstein pure geometrodynamics`  (scoped HKT class).

This is a genuine reconstruction principle because the nonlinear Hamiltonian is recovered from spacetime-composition structure rather than inserted as an action ansatz.

## Exact next admissible work

Two questions now dominate and should be tested separately before opening `chi_ABC`:

1. **SF019 — closed-system microscopic reversibility audit:** determine whether the additional reversibility assumption is independently justified by the fundamental closed gravity+matter architecture, rather than adopted because it completes HKT uniqueness.
2. **SF020 — total hypersurface path-independence source gate:** with independently calibrated flat-space matter dynamics, test how much of the gravitational matter/source coupling is fixed by requiring the *total* closed Hamiltonian constraints to realize the same hypersurface-deformation algebra.

Only after these gates can the project decide whether a genuinely prospectively selected nonlinear law exists.
