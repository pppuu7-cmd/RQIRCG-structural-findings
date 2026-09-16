# SF055A3Q5 - full-tensor piecewise baseline retry - PREOUTCOME

Date: 2026-09-16
Branch: `sf055a3-piecewise-baseline-20260916`, created from original failed-baseline implementation head `1828aeb994265cb78691493a21bdd4f120a30d58`.
External implementation-geometry authority: SF055A3Q4 terminal `9b3933fe70b0042374b10c9d25f5fb05fb01048f` on main.
Status: implementation-only retry under the ORIGINAL SF055A3 science freeze. No new physical gate and no C3.

## Motivation / maximum information gain
The original source-faithful full tensor baseline reached all three N24 Eq.(14) targets within 1% but failed the frozen N16->N24 convergence test for beta_g and beta_lambda3. Q4 independently proved exact shifted optimized-regulator intersection surfaces and a scalar finite-grid shell-loss mechanism. The highest-information next test is therefore to change ONLY the quadrature partition so those exact surfaces are integration boundaries, and ask whether the original full tensor baseline converges under unchanged science criteria.

## Frozen physical and numerical object
Retain without alteration:
- D=4 flat Euclidean, linear split, source-Fourier `partial -> i p`;
- source EH/FP vertices and full six-dimensional Landau-transverse internal graviton space;
- optimized source regulator and canonical `G dotR G` single-scale line;
- source Figure-2 topology coefficients `(-1/2,+3,-3,+6)`;
- source external normalization `Sym_3=(1/6)sum_S3` and `d^4q/(2pi)^4`;
- complete source TT projectors and frozen norms `N_g^-1=0.00052874519051635`, `N_lambda^-1=0.0026385724906858796`;
- benchmark `g=1`, `mu_h=1/10`, `lambda_2=-1/20`, `lambda_3=-7/10`, `eta_h=eta_c=0`, k=1;
- momentum points `p={0,1/8,1/16,1/32}` for Eq.(14) derivative extraction and separate `p=1` finite-difference control;
- Richardson estimator `D(h)=[F(h)-F(0)]/h^2`, `F'(0)=[4D(1/32)-D(1/16)]/3`;
- science quadrature sequence `N={8,12,16,24}`;
- frozen convergence criterion: N16->N24 <=0.2% relative, or <=2e-6 absolute when magnitude <1e-3;
- frozen target criterion: <=1% relative for each of beta_g, beta_lambda3, beta_mu;
- two-point beta_mu path unchanged;
- C3 disabled everywhere.

No target-dependent rescaling, altered projector, changed gauge, changed routing, changed source symmetrisation, changed measure, changed momentum ladder, new coefficient, fitted kernel or tolerance relaxation is permitted.

## Only authorized implementation change
Replace the unsplit reduced Gauss rule for the THREE-POINT integral by the exact Q4 nested partition. The integrand function `three_point_projected` and all physics objects are unchanged.

For each p>0 and y, split phi at all canonical shifted-sphere birth/death curves. For each resulting phi node, split x=r^2 at every active exact boundary root for the three canonical shifted lines:

- `ell=q+p0+p1`, direction angle +pi/3;
- `e23=q-p1`, direction angle -pi/3;
- `e31=q+p0`, direction angle 0.

With `c=sqrt(1-y) cos(phi-alpha)`, a shifted boundary is active iff `c>-p/2` and

`r_b=-p c+sqrt(1-p^2+p^2 c^2)`, `x_b=r_b^2`.

Use exactly the original reduced measure `x/(32*pi^3) dx dy dphi`. For p=0 the partition has no shifted breaks and is the same domain integral.

## Implementation equivalence controls before accepting science output
1. Run the original baseline self-test unchanged.
2. Check exact Q4 root residual/partition coverage functions in the retry code path.
3. For p=0 at frozen low orders, compare piecewise integration with the original unsplit implementation. Difference must be compatible with deterministic re-ordering only; required absolute difference <=2e-10 for Flow_G and Flow_Lambda at N=8 and N=12.
4. Repeat analytic smooth-measure controls from Q4 using the actual retry partition.
5. For a frozen scalar shifted-Litim control, reproduce the Q4 piecewise shell result to <=2e-6 relative at p=1/8 and p=1/32.
6. Record quadrature point counts and reject empty/overlapping intervals.
7. The two-point code path must be byte-identical/import-identical to the original implementation; no piecewise modification is authorized there.

If any implementation equivalence control fails, classification is `INVALID_OR_BLOCKED_Q5_PIECEWISE_IMPLEMENTATION` and no science verdict is issued.

## Science decision rule
After implementation controls pass, evaluate the COMPLETE original matrix and aggregate with the original reducer logic.

PASS only if the original convergence AND target rules all pass:
`PASS_LANE_A_BASELINE_EH_GHOST_THREE_POINT_FLOW_REPRODUCTION_SCOPED`.
This would authorize a separate terminalization of Lane A/SF055; it does not itself compute C3.

If values are numerically converged under the frozen criterion but miss one or more targets >1%:
`FAIL_LANE_A_BASELINE_REPRODUCTION_SCOPED`.

If the original N16->N24 convergence criterion still fails:
`BLOCKED_LANE_A_BASELINE_PIECEWISE_QUADRATURE_NOT_CONVERGED_SCOPED`.

Missing matrix data or resource failure is not a physics FAIL and must be labeled separately.

## Derivative truncation lock
N-convergence and target agreement do not certify h->0 truncation error. The post-run derivative audit and Q4 scalar result showed the sharp regulator permits a regularity class in which |p|^3 can occur. Therefore record the preceding Richardson estimate and the frozen final estimator, but do not claim an O(h^4) truncation theorem unless separately proven for the full tensor projected flow. This Q5 retry does not change the stencil.

## Claim ceiling
Q5 is calibration of one frozen Euclidean FRG implementation. Even a PASS is not asymptotic-safety correctness, regulator independence, a physical SF025 matching coefficient, background/fluctuation equality, Lorentzian matching, unique quantum gravity, or new physics. No quantum chi_ABC. Historical original baseline BLOCKED result remains preserved as provenance even if this implementation retry passes.
