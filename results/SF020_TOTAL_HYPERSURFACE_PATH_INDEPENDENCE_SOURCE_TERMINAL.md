# SF020 — total closed gravity+matter hypersurface path-independence source gate — TERMINAL

Date: 2026-09-14
Status: **TERMINAL / source coupling nonunique / no `chi_ABC` evaluation**

Preregistration: `f0563c0acfda029ef844a42305ba1f553bb21f72`.

## Outcome lock

`chi_ABC` remained embargoed. SF020 tests whether total hypersurface path independence uniquely fixes the matter/source coupling once flat-space matter dynamics is held fixed.

## Executive classification

`TOTAL_RHPI_INSUFFICIENT_COVARIANT_SOURCE_COUPLING_FREEDOM_SURVIVES`.

This does **not** invalidate the SF018/SF019 pure-geometrodynamical reconstruction. It localizes the remaining freedom to source/matter constitutive data.

## Lane A — Kuchar source-field theorem audit

Kuchar's 1974 Lagrangian reconstruction gives the key historical result directly:

- when the intrinsic spatial geometry is the sole gravitational configuration variable, the ADM super-Lagrangian is uniquely recovered as the representation of hypersurface deformations;
- **no analogous uniqueness exists for source-field super-Lagrangians**.

As an explicit illustration, Kuchar reconstructs the most general scalar-field super-Lagrangian with nonderivative gravitational coupling compatible with the closing relation.

Reference:

- K. V. Kuchar, *Geometrodynamics regained: A Lagrangian approach*, J. Math. Phys. 15 (1974) 708, DOI `10.1063/1.1666715`.

Therefore total path independence is known to constrain source-field coupling without collapsing the whole source sector to one unique constitutive law.

Lane classification:

`HYPERSURFACE_CLOSURE_SELECTS_PURE_GEOMETRODYNAMICS_MORE_STRONGLY_THAN_SOURCE_FIELD_LAGRANGIANS`.

## Lane B — explicit covariant source-coupling witness

A simple modern counterexample is a scalar field with curvature coupling

`S_phi = -1/2 Integral sqrt(-g) [ (nabla phi)^2 + m^2 phi^2 + xi R phi^2 ]`.

For any fixed `xi`, this is a local generally covariant theory. In flat spacetime, `R=0`, so all values of `xi` share the same ordinary flat-space Klein-Gordon dynamics and can satisfy the same frozen nongravitational calibration.

In curved/dynamical geometry, however, `xi` changes both the scalar equation and the metric source tensor. It is therefore a genuine curved-source constitutive parameter.

The freedom is not an exotic loophole. Curved-space QFT treats `xi R phi^2` as a standard local covariant operator; in four dimensions `xi` is dimensionless, and interacting renormalization generally mixes/induces the curvature coupling rather than protecting `xi=0` as a universal principle.

Representative references:

- standard curved-space scalar action with nonminimal coupling `xi R phi^2`;
- A. Codello et al., *Renormalization of multicritical scalar models in curved space*, Eur. Phys. J. C 79 (2019) 331.

Scalar-tensor canonical analyses provide the canonical side of the same witness. Brans-Dicke/scalar-tensor theories possess closed first-class Hamiltonian/diffeomorphism constraint algebras expressing their general covariance, while their nonlinear scalar-curvature coupling differs from minimally coupled Einstein-scalar theory.

Representative reference:

- G. Gionti, *Canonical analysis of Brans-Dicke theory addresses Hamiltonian inequivalence between the Jordan and Einstein frames*, Phys. Rev. D 103, 024022 (2021).

This satisfies the preregistered falsifier at the level of principle information content:

- same flat/gravity-off matter theory;
- generally covariant total dynamics / closed constraint algebra;
- same pure metric gravitational branch when the source field is absent;
- independent nonlinear source coupling `xi`;
- different curved-space source response.

Lane classification:

`STANDARD_TOTAL_HDA_IS_COMPATIBLE_WITH_INEQUIVALENT_NONMINIMAL_SOURCE_COUPLINGS`.

## Lane C — G97 / conservation audit

G97 closes mechanical source preparation by including apparatus/support in one total source bookkeeping system. It does not specify the curved-space constitutive form of every source contribution.

For a diffeomorphism-invariant total action, the gravitational and matter Euler-Lagrange equations satisfy the corresponding Noether/Bianchi consistency identities. Thus a covariant nonminimal coupling is not generically rejected merely because it changes the split between 'matter stress' and curvature-dependent terms.

The relevant conservation statement is the **total** covariant identity, not preservation of a particular minimal-coupling stress tensor under a changed theory.

Therefore G97 plus Bianchi compatibility does not fix `xi`.

Lane classification:

`CLOSED_TOTAL_SOURCE_CONSERVATION_IS_COMPATIBLE_WITH_COVARIANT_NONMINIMAL_CONSTITUTIVE_DATA`.

## Lane D — relevance to laboratory massive sources

The same structural issue occurs even when the laboratory source is modeled as a massive extended body rather than a fundamental scalar field.

Worldline EFT for extended gravitating objects contains generally covariant higher-order worldline operators encoding finite-size/tidal response. Goldberger and Rothstein show that:

- some lower Ricci-linear worldline operators are field-redefinition redundant;
- genuinely physical curvature-quadratic tidal operators appear at higher order;
- their Wilson coefficients encode internal source structure and are fixed by matching, not by general covariance/hypersurface algebra alone.

Reference:

- W. D. Goldberger, I. Z. Rothstein, *An Effective Field Theory of Gravity for Extended Objects*, Phys. Rev. D 73, 104029 (2006), arXiv:`hep-th/0409156`.

This is crucial for interpretation. Not every surviving coefficient is a free **gravitational-law** coefficient. Some are physical properties of the prepared source and may be independently calibrated/matched.

SF016 therefore applies: a prediction may be conditional on prospectively frozen source constitutive data without treating every source property as a failure of gravitational theory selection.

Lane classification:

`TOTAL_RHPI_LEAVES_SOURCE_CONSTITUTIVE_MATCHING_DATA_WHICH_MAY_BE_PROTOCOL_OR_MATTER_INPUTS`.

## Terminal decision

The positive uniqueness criterion fails and the counterexample criterion passes:

`TOTAL_RHPI_INSUFFICIENT_COVARIANT_SOURCE_COUPLING_FREEDOM_SURVIVES`.

## What RHPI nevertheless fixes

The result should not be read as 'RHPI fails'. The combined SF018-SF020 picture is sharper:

1. strong embeddable metric geometrodynamics has genuine power to select the pure ADM/Einstein gravitational constraint structure in its scoped class;
2. applying covariance/path independence to the total system guarantees a consistent way for matter/source variables to participate in spacetime evolution;
3. it does **not** select every generally covariant source constitutive coefficient;
4. those coefficients must be separated into independently calibrated matter/source data versus genuinely new gravitational-law data.

## New structural finding

The original desired chain should be refined from

`new gravity principle -> unique total source law`

into

`gravity-law selector + independently frozen source constitutive model -> nonlinear branch dynamics -> operational prediction`.

This is not a relaxation that permits fitting `chi_ABC`. Source parameters are admissible only if fixed independently of the connected outcome, exactly as masses, shapes, polarizabilities and apparatus parameters are fixed in ordinary predictive physics.

## Exact next admissible gate

The next gate should decide whether RHPI can now be **prospectively selected as the gravitational-law principle** despite leaving independently calibratable matter/source coefficients.

That gate must freeze:

1. the exact RHPI/HKT pure-gravity scope accepted as the selected law class;
2. which source parameters belong to the protocol/matter model and must be independently measured or set before any connected calculation;
3. which residual data would still count as forbidden free gravitational coefficients;
4. the branchwise causal/retarded classical solution prescription;
5. the inherited phase map to be used only after the selection decision is committed.

Only after that selection gate may the project reconsider opening `chi_ABC`.
