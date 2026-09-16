# SF055A3Q6 — radial-min2 piecewise baseline successor preoutcome

Date: 2026-09-16
Predecessor: terminal Q5 `BLOCKED_LANE_A_PIECEWISE_IMPLEMENTATION_CONTROL_SCOPED`.

## Motivation frozen before Q6 output

Q5 failed its target-blind smooth polynomial equivalence because its frozen allocator permitted a single Gauss-Legendre node on a radial shell piece. One-point GL is exact only through polynomial degree 1. Under the reduced measure, the Q5 smooth controls require exact radial integration of `x` and `x^2` on each shell piece.

Two-point Gauss-Legendre is exact through degree 3. Therefore require a minimum of **two** nodes on every nonempty radial piece. This is mathematically motivated by the preregistered smooth control itself, not by any beta target.

No Q6 substantive baseline output has been inspected at freeze time.

## OBJECT

Exactly the same C3-disabled SF055A3 EH/ghost baseline, source objects, gauge/regulator, topology coefficients, projectors, normalisations, momentum points, Richardson extraction and targets as Q5 and the historical baseline.

## Q4 GEOMETRY

Retain exactly the Q4 support surfaces and nested y/phi/radial partition.

## Q6 NODE BUDGET

The total node budget per nested coordinate remains exactly `N`.

- y intervals: minimum 1 node per nonempty segment; distribute remainder by length with Hamilton/largest-remainder, lower-index tie break.
- phi intervals: same minimum-1 rule.
- radial x intervals: **minimum 2 nodes per nonempty segment**; distribute the remainder `N-2m` by interval length with Hamilton/largest-remainder, lower-index tie break.

If `N < 2m` for any radial partition, classification is implementation BLOCKED. Under Q4 there are at most four radial segments and the frozen sequence begins at N=8, so the rule is prospectively feasible.

No allocator change is permitted after output.

## FROZEN SEQUENCE / TARGETS

Retain exactly:

- `N={8,12,16,24}`;
- p=`0,1/8,1/16,1/32`; separate p=1 finite-difference control for N=16,24;
- historical Richardson stencil;
- N16->N24 convergence <=0.2% relative (or <=2e-6 absolute when |N24|<1e-3);
- all three N24 Eq.(14) beta targets <=1% relative after convergence passes;
- C3 disabled.

## REQUIRED PRE-BETA CONTROLS

1. source/JIT n=2..5 equivalence;
2. fixed-q topology equivalence;
3. p=0 composite rule identity with historical unsplit rule;
4. exact total node budget N in every nested coordinate;
5. Q4 partition coverage/support controls;
6. smooth reduced-measure controls `1` and `x` agree with analytic integrals to <=2e-10 absolute for every N;
7. Q4 safe thin-shell control is nonzero with correct sign while the historical unsplit N24 control is zero;
8. negative controls reject a dropped radial piece, frozen-support mutation, target rescale and post-output allocator substitution.

If any required pre-beta control fails, STOP before the full matrix and classify

`BLOCKED_LANE_A_Q6_IMPLEMENTATION_CONTROL_SCOPED`.

## PASS / BLOCKED / FAIL

PASS:

`PASS_LANE_A_Q6_PIECEWISE_BASELINE_REPRODUCTION_SCOPED`

iff all implementation controls, historical convergence controls, p=1 finite-difference control and all historical 1% targets pass.

BLOCKED:

`BLOCKED_LANE_A_Q6_PIECEWISE_BASELINE_NOT_CONVERGED_SCOPED`

if implementation controls pass but historical convergence fails.

FAIL:

`FAIL_LANE_A_Q6_PIECEWISE_BASELINE_REPRODUCTION_SCOPED`

if implementation and convergence controls pass but any historical beta target fails.

Infrastructure failure is not a science verdict.

## Interpretation ceiling

A Q6 PASS would validate only the frozen EH/ghost baseline numerical implementation. It would not authorize physical C3 matching by itself. Derivative truncation error remains a separate control even after inter-order convergence.

Retain:

`Q6_BASELINE_PASS != DERIVATIVE_TRUNCATION_CONTROL`.

`Q6_BASELINE_PASS != PHYSICAL_C3_MATCHING`.
