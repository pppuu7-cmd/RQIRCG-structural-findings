# SF012 — selector-fiber / information-deficit theorem — PREREGISTRATION

Date: 2026-09-14
Status: **FROZEN PRE-PROOF STRUCTURAL THEOREM GATE**

## Motivation

SF003-SF011 repeatedly found the same apparent freedom in different languages:

- homogeneous invariant action coefficients;
- Wilson/spectral matching data;
- relevant RG trajectory coordinates;
- primitive/contact/recursion-boundary amplitude data;
- reference-measure/state-counting weights.

SF012 asks whether this can be stated as one representation-independent selection problem.

`chi_ABC` remains embargoed.

## Frozen abstract setup

Let `M` denote a class of candidate microscopic realizations and let `~phys` identify only realizations that are physically equivalent in the domain under consideration (e.g. invertible local field redefinitions, gauge redundancy, boundary terms that change no physical observables).

Define the physical model quotient

`P = M / ~phys`.

Let

`J : P -> Y`

be the **frozen judge map** collecting all inherited lower-order/calibration data and all already accepted consistency predicates that have definite values at the present stage. Let `y0` be the inherited RQIRCG datum.

Define the **selector fiber**

`F(y0) = { p in P : J(p) = y0 }`.

A complete microscopic selector exists on the scoped class iff `F(y0)` is a singleton (assuming nonempty admissibility).

## Representation charts

A formalism/representation is modeled as a faithful chart or encoding

`R : U subset P -> X`

that is injective on physical equivalence classes in its domain. Examples include action coordinates, on-shell amplitude data, RG trajectory coordinates, spectral data, or state/measure coordinates when the translation is faithful in the common domain.

## Theorem target T1 — faithful representation invariance

Prove:

> If `R` is injective on `F(y0)`, then changing from `P` to representation coordinates `X` cannot turn a non-singleton selector fiber into a singleton.

Equivalently, representation change can relabel or reorganize missing information but cannot remove it.

## Theorem target T2 — nonfaithful compression is not selection

Prove:

> If a map `R` sends distinct physically inequivalent elements of `F(y0)` to the same representation datum, then `R` has discarded physical information. The resulting singleton image is not a physical selection theorem unless the identified elements are first proven physically equivalent.

## Theorem target T3 — local deficit rank

Where `P` and `Y` admit a differentiable local chart near a candidate `p0`, define the local unresolved tangent space

`K_p0 = ker D J|p0`

after the physical redundancy quotient.

If `dim K_p0 > 0`, then infinitesimal lower-order/judge-preserving physical directions survive. Under a local diffeomorphic reparameterization of theory space, `dim K_p0` is invariant.

This provides a local **information-deficit rank** without asserting a global manifold structure for all gravity theories.

## Empirical/structural witness requirement

The theorem itself is mathematical. To connect it to RQIRCG, SF012 must also identify at least one already-frozen scoped non-singleton fiber witness or unresolved physical direction from SF003-SF011, without strengthening old claims beyond their scope.

## Pass criterion

Return

`SELECTOR_FIBER_INFORMATION_DEFICIT_IS_REPRESENTATION_INVARIANT_SCOPED`

if T1-T3 are established and the programme mapping is clean.

## Failure criterion

Return

`SELECTOR_FIBER_THEOREM_NOT_ESTABLISHED`

if the supposed representations require noninvertible maps that cannot distinguish physical equivalence from information loss, or if the quotient/judge definitions are internally inconsistent.

## Interpretation rule

A new physical principle is genuinely selective only if it adds a new map/predicate `S` such that

`F_new = {p in F(y0) : S(p)=s0}`

is strictly smaller in the physical quotient. A mere change of variables/representation is not a selector.

## Claim ceiling

SF012 is not a classification theorem for all quantum-gravity theories. It formalizes the information geometry of the scoped reconstruction problem and supplies a criterion for recognizing genuine new selection information.
