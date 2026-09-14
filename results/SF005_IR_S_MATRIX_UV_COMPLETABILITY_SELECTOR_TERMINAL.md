# SF005 — IR S-matrix consistency + UV-completability selector gate — TERMINAL

Date: 2026-09-14
Status: **TERMINAL / no `chi_ABC` evaluation**

Preregistration: `ec70ca91c48bbbeb8fa949e65a0a8aea8c469da3`.

## Outcome lock

The connected three-source observable remained embargoed throughout SF005.

## Lane A — soft/factorization audit

Leading soft-graviton universality fixes the long-distance pole residue/universal coupling structure, but it does not encode all higher-derivative microscopic information.

A useful sharp statement comes from generic soft-theorem analyses: through sub-subleading order, the soft-graviton amplitude separates into a universal part and theory-dependent pieces controlled by lower-point/1PI data. Thus soft universality is not a theorem that all nonlinear graviton couplings are fixed by the leading two-derivative normalization.

Representative reference:

- A. Laddha, A. Sen, *Sub-subleading Soft Graviton Theorem in Generic Theories of Quantum Gravity*, JHEP 10 (2017) 065, arXiv:`1706.00759`.

For curvature-cubic interactions specifically, their extra derivatives make them invisible to sufficiently low orders in a soft expansion in configurations where each curvature contributes soft momentum powers. Therefore the inherited leading soft factor cannot determine their coefficient.

Lane classification:

`LEADING_SOFT_UNIVERSALITY_DOES_NOT_FIX_HIGHER_DERIVATIVE_HOMOGENEOUS_DATA`.

## Lane B — explicit on-shell amplitude freedom

A curvature-cubed interaction provides an independent graviton three-point amplitude structure. Extended-gravity amplitude analyses explicitly construct an S-matrix obtained by adding the minimal higher-derivative three-point amplitude corresponding to an `R^3` term and then use unitarity to generate/diagnose higher-point amplitudes and counterterms.

Representative reference:

- D. C. Dunbar, J. H. Godwin, G. R. Jehu, W. B. Perkins, *Loop amplitudes in an extended gravity theory*, Phys. Lett. B 780 (2018) 41–47, DOI `10.1016/j.physletb.2018.02.046`.

This supplies exactly the SF005 falsifier: the same massless graviton pole and ordinary Einstein-like low-order sector can coexist with an independently normalized higher-derivative on-shell interaction.

The programme-internal G90 covariant cubic family is consistent with this conclusion at the off-shell/covariant level.

Lane classification:

`INEQUIVALENT_ON_SHELL_HIGHER_ORDER_AMPLITUDE_DIRECTION_EXISTS_SCOPED`.

## Lane C — analyticity / crossing / positivity audit

Perturbative unitarity, crossing and dispersive consistency strongly constrain gravitational EFT Wilson coefficients, but the resulting statements are bounds rather than unique coefficient equalities.

A direct example is the four-graviton dispersive analysis of Bern, Kosmopoulos and Zhiboedov. They derive a bound of the schematic form

`|beta_R3|^2 <= beta_R4^+ / m_gap^2`

(up to their conventions), relating the curvature-cubic coefficient to a curvature-quartic coefficient and the massive spectral gap. The same work exhibits nontrivial EFT data from different heavy spectra and string amplitudes occupying constrained regions rather than a single universal point.

Representative reference:

- Z. Bern, D. Kosmopoulos, A. Zhiboedov, *Gravitational Effective Field Theory Islands, Low-Spin Dominance, and the Four-Graviton Amplitude*, J. Phys. A 54 (2021), arXiv:`2103.12728`.

This directly triggers the preregistered interpretation rule: a bound containing `m_gap` and another Wilson coefficient is not selection when those matching data are not fixed by RQIRCG.

Lane classification:

`ANALYTICITY_UNITARITY_CROSSING_BOUND_WILSON_SPACE_BUT_DO_NOT_SELECT_POINT`.

## Lane D — UV matching / causality audit

Causality strengthens the constraints but again moves the missing information into UV data rather than fixing the IR coefficient numerically.

Camanho-Edelstein-Maldacena-Zhiboedov show that additional higher-derivative graviton three-point structures lead to causality problems when treated in isolation at sufficiently high energy, and that the problem can be repaired by an infinite tower of massive higher-spin states. Thus a nonzero higher-derivative coefficient implies information about the UV spectrum/Regge scale.

Representative reference:

- X. O. Camanho, J. D. Edelstein, J. Maldacena, A. Zhiboedov, *Causality constraints on corrections to the graviton three-point coupling*, JHEP 02 (2016) 020, arXiv:`1407.5597`.

The physical message for the present gate is precise:

`higher-order coefficient -> constraint on / matching to UV spectral data`,

not

`IR consistency -> unique coefficient`.

The coefficient therefore remains microscopic matching information unless the spectrum/couplings are themselves fixed by a deeper principle.

Lane classification:

`UV_COMPLETABILITY_TRANSFERS_FREEDOM_TO_SPECTRUM_AND_MATCHING_DATA`.

## Terminal decision

All preregistered failure conditions are satisfied.

`SUC_INSUFFICIENT_WILSON_MATCHING_FREEDOM_SURVIVES`.

## New structural finding

The programme has now crossed a conceptual boundary.

Earlier gates localized the missing object from

`arbitrary connected channel`

to

`nonlinear generator`

to

`homogeneous invariant sector`.

SF005 further localizes it to

`microscopic spectral / UV matching data`.

In other words, standard IR consistency principles can constrain the allowed Wilson-coefficient region, sometimes sharply, but they do not in general supply the microscopic spectral measure that determines a point in that region.

This suggests the decomposition

`IR consistency + spectral data -> Wilson coefficients -> nonlinear observables`.

RQIRCG currently possesses the leftmost consistency architecture but not the independently selected spectral data.

## Implication for the search strategy

It is no longer efficient to stack another generic IR consistency condition unless it is known to generate an equality rather than another bound.

The next scientific task should instead make the spectral statement explicit:

1. write the homogeneous coefficients as spectral/matching functionals wherever possible;
2. identify exactly which microscopic data remain free;
3. audit the frozen RQIR requirements for any principle that actually fixes those data;
4. if no such rule exists, record a terminal theorem that the structural-finding branch cannot select nonlinear dynamics from RQIR + consistency alone.

This next step remains prior to `chi_ABC`.
