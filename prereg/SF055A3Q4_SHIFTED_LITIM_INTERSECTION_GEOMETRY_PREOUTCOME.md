# SF055A3Q4 — shifted Litim intersection geometry and piecewise-equivalence gate — PREOUTCOME

Date: 2026-09-16
Parent authority: `recovery/CURRENT_FRONT.md` after terminal baseline classification `BLOCKED_LANE_A_BASELINE_QUADRATURE_NOT_CONVERGED_SCOPED` and the derivative/regulator-shell diagnostic.

Status: prospectively frozen before Q4 geometry/equivalence output is inspected.

## PURPOSE

Test the implementation-only hypothesis that the frozen derivative-sensitive three-point integrals can be evaluated without missing thin optimized-regulator shells by making every shifted propagator support surface an explicit quadrature boundary, while preserving the exact same integrals and all original science criteria.

This gate does NOT rerun the full tensor baseline and does NOT change the historical BLOCKED result.

## FROZEN PARENT OBJECT

Retain without modification:

- D=4 flat Euclidean source-Fourier realization;
- full 6D Landau-transverse internal graviton sector plus FP ghosts;
- source optimized regulator and single-scale line `G dotR G`;
- Figure-2 source coefficients and source symmetrisation;
- loop measure `d^4q/(2 pi)^4`;
- external momentum points `p=0,1/8,1/16,1/32` for the derivative target and `p=1` for the separate finite-difference control;
- Richardson stencil already frozen by SF055A3;
- deterministic Gauss-Legendre science sequence `N={8,12,16,24}`;
- original 0.2% inter-order convergence threshold and 1% target threshold;
- C3 disabled.

No target-dependent rescaling, smoothing of the regulator, alternative stencil, changed h ladder or changed convergence criterion is allowed.

## EXACT SHIFTED LINES

For canonical three-point routing with `ps_i=p UNIT_PS_i`, the non-differentiated shifted internal propagator momenta are exactly

- bubble: `ell=q+ps_0+ps_1`;
- triangle/ghost: `e23=q-ps_1`;
- triangle/ghost: `e31=q+ps_0`.

Thus define planar shifts

`a_B=p(UNIT_PS_0+UNIT_PS_1)`,

`a_23=-p UNIT_PS_1`,

`a_31=+p UNIT_PS_0`.

All have magnitude `|a|=p` for the symmetric 120-degree external configuration.

The differentiated line remains q with `q^2<1`; Q4 concerns only the non-smooth `max(|q+a|^2,1)` transitions of shifted non-differentiated propagators.

## REDUCED COORDINATES

Retain the parent reduced coordinates

`q=(sqrt(x(1-y)) cos(phi), sqrt(x(1-y)) sin(phi), sqrt(x y), 0)`,

`x in [0,1]`, `y in [0,1]`, `phi in [0,2 pi]`,

with measure

`d^4q/(2 pi)^4 = [x/(32 pi^3)] dx dy dphi`.

Set `r=sqrt(x)` and for a planar shift of angle alpha define

`c(y,phi;alpha)=sqrt(1-y) cos(phi-alpha)`.

The shifted regulator boundary hypothesis is

`|q+a|^2=1`

iff

`r^2 + 2 p c r + p^2 = 1`.

For `0<p<=1` its nonnegative radial root is frozen as

`r_b=-p c + sqrt(1-p^2+p^2 c^2)`.

A root lies inside the q-ball precisely when

`c > -p/2`,

with equality corresponding to `r_b=1`; for `p=1,c>=0`, `r_b=0` is permitted as an integration-boundary root.

The corresponding exact x-boundary is `x_b=r_b^2`.

## ANGULAR BIRTH/DEATH SURFACES

Let `s=sqrt(1-y)`.

For `s>=p/2`, root activation changes at

`cos(phi-alpha)=-p/(2s)`.

The exact phi breakpoints are therefore

`phi=alpha +/- arccos[-p/(2 sqrt(1-y))] (mod 2 pi)`.

The angular topology changes at

`y_*=1-p^2/4`.

For `y>y_*`, `sqrt(1-y)<p/2` and every shift has an interior/boundary radial transition for all phi.

## PIECEWISE PARTITION ALGORITHM

For each frozen p:

1. split the y domain at `y_*` when it lies strictly inside `(0,1)`;
2. at each y quadrature node, construct the union of exact phi birth/death breakpoints for all three shifts plus `0,2pi`;
3. at each `(y,phi)` quadrature node, construct all active exact `x_b=r_b^2` roots for `a_B,a_23,a_31`, add `0,1`, sort/deduplicate, and integrate separately on every radial interval;
4. within each open radial interval the support bit-vector `(|q+a_i|^2>1)` must be constant.

This is a domain partition of the same integral, not a new regulator prescription.

## POSITIVE CONTROLS

Q4 PASS requires all of the following before any new full tensor baseline is attempted:

1. **Boundary residual:** for deterministic dense controls at `p in {1/8,1/16,1/32,1}`, every computed interior/boundary root satisfies `||q+a|^2-1| <= 2e-13`.
2. **Activation equivalence:** `c>-p/2` agrees with direct endpoint test `|n+a|^2>1` at `r=1` away from a `2e-13` boundary band.
3. **Phi-break equivalence:** prospectively generated phi intervals have constant active-shift sets at deterministic interior samples; no unrecorded activation crossing is allowed.
4. **Partition completeness:** sorted radial intervals cover `[0,1]` with no gap/overlap larger than `2e-14`; support bit-vectors are constant at three deterministic interior samples per interval.
5. **Shift census:** the generated canonical shifts match exactly the PR16 routing objects `ell`, `e23`, `e31`, including their magnitudes and directions.
6. **Smooth-integrand equivalence:** piecewise and unsplit integration of at least two smooth polynomial controls under the parent reduced measure agree to absolute `2e-12` at N=24.
7. **Scalar Litim-shell control:** for the one-shift scalar control already used in the derivative audit, the new reduced-coordinate piecewise integration must agree with an independent polar split implementation to relative `2e-3` at N=24 for `p=1/8` and `p=1/32`.
8. **Continuum coefficient control:** at a prospectively fixed small momentum `p=1/256`, the split scalar `Delta J/p^2` at N=24 must agree with the independently derived coefficient `-1/[64 pi^2 (1+mu)^2]` to relative `5e-3` for `mu=1/10`.
9. **Counterexample to unsplit finite grid:** at the prospectively generated safe momentum `p_safe=(1-sqrt(x_max(N)))/4`, the unsplit N-point scalar grid must return zero shell contribution while the piecewise implementation returns a nonzero contribution with the correct sign. This confirms that Q4 addresses the diagnosed finite-grid shell-loss mechanism rather than merely reparameterising identical nodes.

## NEGATIVE CONTROLS

The checker must reject:

- omission of one of the three canonical shifted lines;
- sign reversal of one canonical shift;
- using `r_b=-pc-sqrt(...)`;
- omitting the angular birth/death breakpoints while claiming complete partition equivalence;
- freezing shifted-propagator support while moving q;
- changing the optimized regulator to a smoothed regulator;
- target-dependent radial clipping/rescaling.

## PASS

`PASS_SHIFTED_REGULATOR_INTERSECTION_GEOMETRY_AND_PIECEWISE_EQUIVALENCE_SCOPED`

only if every frozen positive and negative control passes.

## FAIL

`FAIL_SHIFTED_REGULATOR_INTERSECTION_GEOMETRY_SCOPED`

if the exact boundary/partition construction is well-defined but fails the frozen equivalence or scalar controls.

## BLOCKED

`BLOCKED_SHIFTED_REGULATOR_PARTITION_OBJECT`

if the exact same parent integral cannot be partitioned without introducing an unsupported convention.

## INTERPRETATION CEILING

Even a PASS validates only the exact geometry/equivalence machinery for a later implementation-only baseline retry. It is not a repaired baseline PASS, does not alter the historical `BLOCKED_LANE_A_BASELINE_QUADRATURE_NOT_CONVERGED_SCOPED`, does not establish the full tensor error mechanism, does not validate Richardson truncation error, does not terminalize SF055, and does not authorize any substantive C3 projected-flow output.