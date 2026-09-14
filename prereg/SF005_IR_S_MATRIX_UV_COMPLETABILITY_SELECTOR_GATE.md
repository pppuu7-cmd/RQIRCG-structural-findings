# SF005 — IR S-matrix consistency + UV-completability selector gate — PREREGISTRATION

Date: 2026-09-14
Status: **FROZEN DECISION RULE / dedicated evaluation not yet performed**

## Provenance note

SF005 is prospective with respect to its **specific selector decision**, but not literature-blind: SF004 already consulted standard causality and higher-curvature literature. No `chi_ABC` calculation has occurred.

## Scientific question

After SF004 decomposed the nonlinear generator schematically as

`Gamma = Gamma_forced + Gamma_homogeneous`, 

can on-shell consistency principles uniquely fix the homogeneous nonlinear coefficients?

Candidate principle **SUC** (`S-matrix/UV Consistency`) requires, in the applicable weak-field scattering domain:

1. universal leading soft-graviton factorization;
2. Lorentz invariance;
3. unitarity / factorization on physical poles;
4. crossing symmetry;
5. causal analyticity / admissible dispersion behavior;
6. existence of some UV completion or Regge/high-energy completion compatible with the low-energy amplitude;
7. inherited weak-field carrier and universal coupling normalization.

No derivative-order truncation is postulated as fundamental physics.

## Outcome embargo

`chi_ABC` remains embargoed. No connected observable is evaluated or used to select coefficients.

## Selector criterion

SUC succeeds only if the above conditions fix every surviving homogeneous coefficient uniquely, up to already-calibrated normalization and physical equivalence.

Positive verdict:

`SUC_SELECTS_HOMOGENEOUS_NONLINEAR_SECTOR_SCOPED`.

## Counterexample-first falsifier

SUC fails if there exists an interval, ray, finite-dimensional region, or discrete multiplicity of inequivalent low-energy amplitudes such that:

1. all share the inherited massless spin-2 pole and leading universal soft behavior;
2. all satisfy local factorization/unitarity at the order tested;
3. they differ by a genuine higher-order contact/three-point structure or Wilson coefficient;
4. causal/analytic consistency constrains but does not uniquely determine that coefficient;
5. at least two values can be associated with admissible UV-completion data/scales, or the consistency conditions themselves leave matching data free.

Failure verdict:

`SUC_INSUFFICIENT_WILSON_MATCHING_FREEDOM_SURVIVES`.

## Mandatory lanes

### Lane A — soft/factorization audit
Determine whether higher-order pure-carrier operators are visible to, or left free by, leading soft-graviton universality and pole factorization.

### Lane B — amplitude/contact freedom audit
Identify at least one physically inequivalent on-shell higher-curvature amplitude direction that is not fixed by the inherited two-derivative amplitude normalization.

### Lane C — analyticity/positivity audit
Determine whether dispersion/causality/positivity conditions produce an equality fixing the coefficient, or only inequalities/suppression/scale relations.

### Lane D — UV matching audit
Determine whether the remaining coefficient is fixed by IR consistency alone or requires microscopic spectrum/coupling/boundary data.

## Strict interpretation rule

A bound such as `|alpha| < f(M_gap)` is **not** selection of `alpha` unless `M_gap` and all other matching data are themselves fixed by the inherited architecture.

Likewise, proving `alpha=0` only under an extra assumption such as “no new states at any scale” does not count unless that assumption was independently derived rather than inserted as a new minimality axiom.

## Claim ceiling

SF005 is not an experimental test, not a proof about all possible UV completions, and not a quantum-gravity construction. It tests whether standard on-shell consistency can supply the missing coefficient-selection information.

## Next-step rule

If SUC fails, the next search must move from **consistency principles** to **microscopic state/spectrum/boundary principles** or show that the RQIR requirements themselves contain an unexploited rule of that type. The project must not continue stacking generic consistency conditions if they only bound a Wilson-coefficient space.
