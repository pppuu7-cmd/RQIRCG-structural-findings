# SF055A3 — baseline quadrature implementation freeze

Date: 2026-09-15
Parent science contract: `prereg/SF055A3_SOURCE_FOURIER_BASELINE_LOOP_REPRODUCTION_PREOUTCOME.md`
Programme plan: `prereg/SF055_TO_PROGRAMME_VERDICT_EXECUTION_PLAN_20260915.md`

This file freezes numerical implementation details inside Major Step 1B only. It does not add a new scientific gate and changes no previously frozen physics object, target or PASS threshold.

## Exact source objects retained

- D=4 flat Euclidean, linear split, source-Fourier `partial -> i p`;
- full six-dimensional Landau-transverse internal graviton sector;
- source EH/FP n-point vertices;
- `mu=1/10`, `lambda_2=-1/20`, `lambda_3=lambda_4=lambda_5=-7/10`, `g_n=1` at k=1;
- optimized regulator, canonical `G dotR G` single-scale line;
- Figure-2 coefficients `(-1/2,+3,-3,+6)`;
- source external symmetrisation `Sym_3=(1/6)sum_{S3}`;
- loop measure `d^4q/(2 pi)^4`;
- complete source TT projectors `T_G,T_Lambda` and previously measured normalisations;
- C3 disabled.

## Exact analytic Landau basis used only as a speed implementation

For nonzero q let `u=q/|q|`, `P=I-u u^T`. Use the same five orthonormal transverse-traceless tensors as the validated TT constructor plus

`H_s=(P+3 u u^T)/sqrt(12)=(I+2 u u^T)/sqrt(12)`.

Then `F[H_s;q]=0`, `tr H_s=sqrt(3)`, and `H_s` is orthogonal to all five TT tensors. Thus these six tensors span exactly the already-authorized `ker F(q)`.

A pre-quadrature direct evaluation with the validated source-Fourier two-point engine fixes the diagonal Hessian in this normalized basis: five TT modes have inverse two-point coefficient `K_EH(q^2+mu)` and the sixth scalar transverse mode has `-(K_EH/2)(q^2+mu)`, with `K_EH=1/(32 pi)`. This replaces an initial implementation note that incorrectly wrote `-2 K_EH`; the correction was made before any quadrature output and changes no frozen science object. The optimized regulator replaces `q^2` by 1 below cutoff. The executable MUST independently repeat this source-Hessian self-check before any integrated result is accepted.

## Exact batched EH vertex evaluation

The existing square-free source-Fourier polynomial algebra is lifted only by adding leading batch axes. Every batch element is exactly the same multilinear coefficient calculation as `seed.eh_vertex_fourier`; no interpolation, SVD/CP truncation, stochastic estimator or fitted coefficient is introduced.

Before quadrature the batched engine MUST reproduce scalar source vertices at frozen n=2..5 controls and reproduce the existing fixed-q Figure-2 topology values.

## Rotational reduction of the 4D loop integral

External symmetric momenta lie in the 1-2 plane. After the complete TT tensor contraction and source S3 symmetrisation, the scalar integrand is invariant under rotations in the orthogonal 3-4 plane. Parameterise

`q=(sqrt(x(1-y)) cos(phi), sqrt(x(1-y)) sin(phi), sqrt(x y), 0)`

with `x=q^2 in [0,1]`, `y in [0,1]`, `phi in [0,2pi]`.

Integrating the orthogonal azimuth exactly gives

`d^4q/(2pi)^4 = [x/(32 pi^3)] dx dy dphi`.

This is an exact coordinate reduction of the same compact-support integral, not a change of regulator or angular averaging approximation.

For the p=0 two-point mass projection, retain the reference TT direction and use the residual O(3) symmetry around it. With q polar angle theta relative to that reference direction,

`d^4q/(2pi)^4 = [1/(4 pi^3)] r^3 sin^2(theta) dr dtheta`.

## Frozen quadrature and derivative implementation

Use deterministic Gauss-Legendre nodes independently in every active reduced dimension with the already-frozen science sequence

`N = 8,12,16,24`.

The science convergence criterion remains exactly the parent criterion: N=16 to N=24 change <=2e-3 relative, or <=2e-6 absolute when the value is below 1e-3.

For the analytic Eq.(14) gravitational projection evaluate the integrated `Flow_G(p^2)` at

`p = 0, 1/8, 1/16, 1/32`.

For `D(h)=[Flow_G(h^2)-Flow_G(0)]/h^2`, use the prospectively frozen Richardson derivative

`Flow_G_prime(0) = [4 D(1/32)-D(1/16)]/3`.

Record the preceding estimate `[4 D(1/16)-D(1/8)]/3` as a derivative-stability diagnostic. No target-dependent choice of h is permitted after output.

At eta=0, g=1, k=1 use the source equations

`beta_g = 2 + 2 N_g Flow_G_prime(0)`,

`beta_lambda3 = (-1-beta_g/2) lambda_3 + N_lambda Flow_Lambda(0)`.

For the source-architecture finite-difference control also evaluate `Flow_G(1)` after the analytic-target run and report

`beta_g_FD = 2 + 2 N_g [Flow_G(1)-Flow_G(0)]`

and the corresponding Eq.(11) lambda3 output. These finite-difference values are NOT forced to Eq.(14).

## Separate two-point beta_mu path

Differentiate the same Wetterich trace twice, giving the source two-point topology coefficients

- graviton four-vertex tadpole `-1/2`;
- graviton two-three-vertex bubble `+1`;
- ghost two-vertex bubble `-2`.

Project the p=0 graviton two-point flow on the complete five-dimensional TT trace. At eta_h=0,

`beta_mu = -2 mu + (32 pi/5) Flow_TT^(2)(0)`.

This is generated by the diagram code path; the printed Eq.(14) beta_mu is used only as the frozen comparison target.

## Hard outcome rule

All three Eq.(14) targets must satisfy the already-frozen 1% relative tolerance after the frozen convergence criterion passes. Failure of any target after implementation-only bugs are corrected terminalizes Lane A as FAIL/BLOCKED and stops the programme before any substantive C3 flow.
