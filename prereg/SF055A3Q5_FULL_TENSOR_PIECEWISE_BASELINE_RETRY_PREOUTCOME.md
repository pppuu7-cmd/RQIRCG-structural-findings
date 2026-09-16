# SF055A3Q5 — full-tensor piecewise baseline retry preoutcome

Date: 2026-09-16
Parent authority: `recovery/CURRENT_FRONT.md` after terminal SF055A3Q4.

## HYPOTHESIS

The historical SF055A3 baseline convergence blocker may be caused, wholly or partly, by unsplit Gauss nodes missing thin shifted optimized-regulator shells. Re-evaluating the **same** frozen EH/ghost baseline with exact Q4 shell surfaces as quadrature boundaries may satisfy the already-frozen convergence and target controls without changing the physical or numerical target object.

This is an implementation-only successor. The historical blocked result is never rewritten.

## OBJECT

Exactly the historical C3-disabled SF055A3 baseline:

- D=4 flat Euclidean, linear split, source-Fourier `partial -> i p`;
- source EH/FP vertices and source Figure-2 coefficients;
- full six-dimensional Landau-transverse internal graviton space plus FP ghosts;
- optimized regulator and canonical `G dotR G` single-scale line;
- source `Sym_3=(1/6)sum_S3` and loop measure `d^4q/(2pi)^4`;
- complete source TT projectors and frozen normalisations;
- benchmark `g=1`, `mu=1/10`, `lambda_2=-1/20`, `lambda_3=lambda_4=lambda_5=-7/10`, `eta_h=eta_c=0`, `k=1`;
- C3 disabled.

No coupling, coefficient, sign, regulator, routing, projector, normalization, target or threshold may be fitted or changed.

## FROZEN MOMENTA / EXTRACTION

Three-point flow at

`p = 0, 1/8, 1/16, 1/32`

plus separate finite-difference control at

`p=1` for N=16,24.

Retain the historical Richardson extraction:

`D(h)=[Flow_G(h^2)-Flow_G(0)]/h^2`,

`Flow_G_prime(0)=[4 D(1/32)-D(1/16)]/3`.

Retain

`beta_g = 2 + 2 N_g Flow_G_prime(0)`,

`beta_lambda3 = (-1-beta_g/2) lambda_3 + N_lambda Flow_Lambda(0)`,

`beta_mu = -2 mu + (32 pi/5) Flow_TT^(2)(0)`.

## Q4 PIECEWISE GEOMETRY

For each shifted non-differentiated internal line `q+a` with `|a|=p`, use the exact Q4 surface

`r^2 + 2 p c r + p^2 = 1`,

`c=sqrt(1-y) cos(phi-alpha)`,

`r_b=-p c+sqrt(1-p^2+p^2 c^2)`.

Angular birth/death points and `y_*=1-p^2/4` are quadrature boundaries. For each `(y,phi)` cell, all valid radial roots `x_b=r_b^2` from the canonical shifted lines are radial quadrature boundaries.

## COMPOSITE GAUSS BUDGET — FROZEN BEFORE OUTPUT

To preserve `N` as the historical resolution parameter and avoid an order-of-magnitude cost change, use exactly **N total Gauss-Legendre nodes per nested coordinate**, distributed over the current exact smooth subintervals.

For a partition with positive interval lengths `L_i` and total node budget `N`:

1. assign one node to every nonempty interval;
2. distribute the remaining `N-m` nodes proportionally to `L_i/sum L` by the Hamilton/largest-remainder method;
3. ties are broken by lower interval index;
4. use ordinary Gauss-Legendre of the assigned order on each interval;
5. the union of weighted nodes is the composite rule.

For the y partition use the Q4 topology-change boundary if it lies strictly inside `(0,1)`. For each resulting y-node construct its exact phi partition; for each phi-node construct its exact radial-x partition.

This budget rule is target-blind and may not be changed after any baseline output is inspected.

## FROZEN SCIENCE SEQUENCE

`N={8,12,16,24}`.

Historical convergence rule retained exactly:

- N16 -> N24 relative change <= `2e-3`, or
- absolute change <= `2e-6` when `|N24|<1e-3`.

Historical target tolerance retained exactly: all three Eq.(14) beta targets within 1% relative **after** convergence passes.

Finite-difference p=1 remains a separate control and is not compared to Eq.(14).

## REQUIRED POSITIVE CONTROLS

Before classification:

1. inherited source/JIT n=2..5 vertex equivalence must pass;
2. inherited six-dimensional Hessian/propagator controls must pass;
3. inherited fixed-q topology comparison must pass;
4. Q4 boundary residual and partition coverage controls must pass in the implementation;
5. at p=0, where no shifted shell partition exists, piecewise and historical unsplit integration at each N must agree within `2e-9*(1+|value|)` for the three-point p=0 flow and within the inherited two-point tolerance;
6. a smooth reduced-measure polynomial control integrated through the composite partition must reproduce its analytic integral to <= `2e-10` absolute for every N;
7. a scalar thin-shell control must be nonzero at a prospectively fixed safe small p where the unsplit N=24 rule can return zero, with the sign agreeing with the Q4 analytic coefficient.

## REQUIRED NEGATIVE CONTROLS

The implementation must reject at least:

- an intentionally dropped nonempty radial subinterval;
- a frozen-support mutation that evaluates both sides of a known shell with the same support bit;
- a target-dependent normalization rescale;
- an alternative node allocator chosen after output.

## PASS

`PASS_LANE_A_PIECEWISE_BASELINE_REPRODUCTION_SCOPED` iff:

- all required implementation controls pass;
- the historical N16->N24 convergence criterion passes for every required aggregate key;
- the p=1 finite-difference control is finite and converged under its historical criterion;
- all three N24 Eq.(14) beta values satisfy the historical 1% target tolerance.

## BLOCKED

`BLOCKED_LANE_A_PIECEWISE_BASELINE_QUADRATURE_NOT_CONVERGED_SCOPED` if the implementation controls pass but the historical convergence criterion still fails.

`BLOCKED_LANE_A_PIECEWISE_IMPLEMENTATION_CONTROL_SCOPED` if any required equivalence/partition/control fails before scientific classification.

Infrastructure failure before complete outputs is infrastructure-only.

## FAIL

`FAIL_LANE_A_PIECEWISE_BASELINE_REPRODUCTION_SCOPED` if all required convergence and implementation controls pass but at least one historical target fails the 1% threshold.

## INTERPRETATION CEILING

A PASS validates only the frozen EH/ghost baseline implementation at the specified regulator/gauge/truncation and momentum extraction. It does not establish a physical C3 coefficient, asymptotic-safety correctness, regulator independence, background/fluctuation equality, Lorentzian matching, new physics or quantum gravity.

Even on PASS, derivative truncation error remains a separate required control before substantive C3 output can be interpreted unless existing authority already closes it.

Retain:

`PIECEWISE_BASELINE_PASS != C3_PHYSICAL_MATCHING`.

`INTER_ORDER_CONVERGENCE != DERIVATIVE_TRUNCATION_ERROR_CONTROL`.
