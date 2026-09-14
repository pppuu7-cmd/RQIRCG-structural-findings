# SF012 — selector-fiber / information-deficit theorem — TERMINAL

Date: 2026-09-14
Status: **TERMINAL STRUCTURAL THEOREM / no `chi_ABC` evaluation**

Preregistration: `b35a43e9abd0bd36cbb5b222d8952300dd7d7bc6`.

## Definitions

Let `M` be a scoped class of microscopic realizations and let `~phys` identify only realizations proven physically equivalent in the domain under study.

`P = M / ~phys`.

Let

`J : P -> Y`

collect the frozen inherited data and already-declared judge/consistency values. For the inherited datum `y0`, define

`F(y0) = J^{-1}(y0)`.

This is the **selector fiber**.

- `F = empty` means the scoped model class is incompatible with the judge datum.
- `F = {p}` means complete selection within the scoped class.
- `|F| > 1` means physical underdetermination remains.

The definition is representation-independent because `P` is already a physical quotient.

## T1 — faithful representation invariance

Let

`R : U subset P -> X`

be injective on `F(y0) subset U`.

Take two distinct physical classes `p1 != p2` in `F(y0)`. Injectivity gives

`R(p1) != R(p2)`.

Therefore the image

`R(F(y0))`

contains at least as many distinct elements as the original fiber; in fact `R` gives a bijection between `F(y0)` and its image.

Hence a faithful change of representation cannot turn a non-singleton physical selector fiber into a singleton.

`QED T1`.

## T2 — nonfaithful compression is not physical selection

Suppose instead that

`R(p1) = R(p2)`

for two physically inequivalent classes `p1 != p2` in `F(y0)`.

Then `R` is noninjective on physical theory space. It has erased the distinction between two different physical realizations.

A singleton image under such a compression cannot imply that Nature/theory has selected one of the original classes. It shows only that the representation is insensitive to their difference.

To promote the identification to a physical quotient, one must separately prove

`p1 ~phys p2`.

Without that proof, compression is loss of information, not selection.

`QED T2`.

## T3 — local information-deficit rank

Assume a differentiable physical theory-space chart near `p0` and define

`K_p0 = ker D J|p0`.

Let `R` be a local diffeomorphic reparameterization with inverse in the neighborhood. In the new coordinates,

`J' = J o R^{-1}`.

Therefore

`D J'|R(p0) = D J|p0 o D R^{-1}|R(p0)`.

Because `D R` is an isomorphism,

`v in ker D J|p0`

iff

`D R(v) in ker D J'|R(p0)`.

Thus `D R` maps the kernels isomorphically and

`dim ker D J|p0 = dim ker D J'|R(p0)`.

The local unresolved physical tangent dimension is invariant under faithful smooth reparameterization.

`QED T3`.

## Programme witness

The theorem would be vacuous for RQIRCG if no scoped physical non-singleton fiber had been exhibited. Earlier frozen results provide such witnesses without needing `chi_ABC`.

SF003/SF004 identify separately invariant higher-order carrier functionals whose coefficients are not fixed by the inherited quadratic weak-field normalization or by nonlinear gauge closure/universal source composition. The physically relevant witness was strengthened using non-evanescent curvature-cubed on-shell directions rather than relying only on Ricci-type off-shell redundancies.

Thus, in the scoped higher-order gravitational sector, there exists at least one inherited-data-preserving physical direction before a genuinely new microscopic selector is imposed.

Subsequent gates then show the same information deficit in different representations:

- SF005/SF006: Wilson/spectral matching data;
- SF008: relevant RG trajectory coordinates;
- SF010: primitive/contact/recursion-boundary amplitude data;
- SF011: reference-measure/state-counting data.

SF012 does not claim a global bijection among all of these formalisms for every conceivable quantum-gravity theory. It claims the narrower theorem: **where two descriptions faithfully encode the same physical completion space, a representation change cannot remove a non-singleton selector fiber.**

## Terminal classification

All three preregistered theorem targets pass:

`SELECTOR_FIBER_INFORMATION_DEFICIT_IS_REPRESENTATION_INVARIANT_SCOPED`.

## New scientific result

The recurring nonlinear underdetermination is now formally separable from the choice of formalism.

A faithful translation

`action coefficients <-> amplitude seeds <-> RG coordinates <-> spectral/matching data <-> state/measure data`

may move the unresolved information into a different coordinate system, but it cannot by itself reduce the number of physically admissible completions.

This explains why SF003-SF011 repeatedly recovered a free datum under different names.

## Genuine selector criterion

A proposed new physical principle must contribute an additional physical condition

`S : P -> Z`

with selected value/property `z0`, producing

`F_new = {p in F(y0) : S(p)=z0}`.

It has genuine selector power only if

`F_new` is strictly smaller than `F(y0)`

in the **physical quotient**, not merely in a chosen parameterization.

Complete selection requires `F_new` to be a singleton within the scoped model class.

This supplies a reusable adversarial test for all future principles.

## Consequence for RQIRCG structural findings

The project should stop treating the following as possible selectors by themselves:

- a new notation or field redefinition;
- switching from action to amplitude language;
- switching from amplitudes to dispersion relations;
- switching from Wilson coefficients to UV spectral data;
- switching from UV data to entropy/reference-measure language.

Each can be useful computationally, but none adds physical information unless an additional condition actually reduces the selector fiber.

## Next research target

The next high-value task is a **selector-principle class triage using the fiber criterion**.

Every candidate new principle should be asked, before any nonlinear observable is calculated:

1. What physical function `S` does it add?
2. Is `S` independently motivated or merely a coordinate choice/minimality convention?
3. Can two physically inequivalent points in the old fiber satisfy the same `S`?
4. If yes, what is the residual fiber dimension/cardinality?
5. If no, what independent theorem establishes uniqueness?

Only a class that survives this test should be allowed to open the `chi_ABC` embargo.
