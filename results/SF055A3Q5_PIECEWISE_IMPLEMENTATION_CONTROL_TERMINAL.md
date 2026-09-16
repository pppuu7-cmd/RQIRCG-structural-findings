# SF055A3Q5 — piecewise baseline implementation-control terminal

Date: 2026-09-16
Preregistration: `f00901e9a429ee5bfafc45c6734f1286ed435578`.

## Classification

`BLOCKED_LANE_A_PIECEWISE_IMPLEMENTATION_CONTROL_SCOPED`.

## What was executed

The Q5 implementation was frozen before output with exact Q4 shell boundaries and a total-N composite Gauss budget. The frozen allocator assigned at least one node to every nonempty subinterval and distributed the remaining nodes by interval length using the Hamilton/largest-remainder rule.

Before any full tensor baseline matrix was allowed, the Q5 preregistration required target-blind smooth reduced-measure controls to reproduce their analytic integrals to absolute `2e-10` for every `N in {8,12,16,24}`.

A clean local runtime using the committed Q5 algorithm and the historical source-basis/JIT conventions gave maximum smooth-control absolute errors

- N=8: `1.1541821024916785e-07`;
- N=12: `2.2976919557965436e-08`;
- N=16: `5.879272069186925e-09`;
- N=24: `8.177778909775058e-10`.

All exceed the frozen `2e-10` requirement.

Therefore Q5 is blocked **before** any new full-tensor beta values are inspected.

## Counterexample interpretation

The Q4 geometry is not falsified. The same Q5 implementation still captures the prospectively fixed thin-shell control:

- `p_safe=0.00030097992802030626`;
- piecewise N24 contribution `-1.1850604402647715e-10`;
- unsplit N24 contribution `0.0`.

The blocker is instead the frozen Q5 composite budget: allowing only one Gauss node on a radial piece is not sufficient to preserve the preregistered smooth polynomial equivalence at low N.

This is an implementation/control blocker, not a scientific failure of the EH/ghost baseline or of asymptotic safety.

## Why the matrix was not run

PASS required **all** implementation controls before classification. Once the smooth-equivalence control failed under the frozen rule, running the expensive tensor matrix would be outcome-invalid and lower information value.

No threshold, source object, regulator, momentum point, Richardson stencil, target or physics coefficient was changed.

## Authorized successor logic

A new allocator is a changed implementation contract and therefore requires a new prospective gate rather than a repair of Q5.

The analytically motivated next option is to require at least two Gauss nodes on every nonempty **radial** piece while preserving the total N radial budget. Two-point Gauss-Legendre is exact for polynomials through degree 3; the frozen smooth reduced-measure controls contain radial degree at most 2 after the measure, so this is an outcome-independent mathematical motivation rather than target tuning.

Any successor must preserve the original baseline physics, `N={8,12,16,24}`, historical convergence/target thresholds, Q4 shell geometry, and C3-disabled hard stop.

## Claim ceiling

`Q5_IMPLEMENTATION_BLOCKED != BASELINE_FAIL`.

`Q4_GEOMETRY_PASS` remains intact.

Historical `BLOCKED_LANE_A_BASELINE_QUADRATURE_NOT_CONVERGED_SCOPED` remains intact.

`SF055_TERMINAL_PASS=FALSE`.

No substantive C3 beta output is authorized.
