# SF055A3 — source-Fourier full EH/ghost baseline loop reproduction — PREOUTCOME

Date: 2026-09-15
Parent SF055 preregistration: `9d998d984566aa5bf290312a6a062fd632c85561`.
Inherited authority: SF055A2 seed-object PASS; SF055 Lane B PASS; SF055 Lane C topology/insertion-bookkeeping PASS; internal propagator/regulator source-authority audit PASS.

## PURPOSE

Close the last remaining SF055 calibration dependency before any substantive C3 projected flow is inspected:

`LANE_A_BASELINE_EH_GHOST_THREE_POINT_FLOW_REPRODUCTION`.

This gate must reconstruct the published baseline from source-defined EH/FP objects through the same numerical code path that will later carry the C3 insertions. Hard-coding or fitting Eq. (14) is forbidden.

## HYPOTHESIS

The frozen Local Quantum Gravity source objects are sufficient to numerically reconstruct the eta_h=eta_c=0 baseline three-graviton flow at the frozen benchmark point within prospectively fixed numerical tolerances.

## SOURCE AUTHORITY

Primary target:

N. Christiansen, B. Knorr, J. Meibohm, J. M. Pawlowski, M. Reichert, *Local Quantum Gravity*, arXiv:1506.07016v2.

Required source objects:

- Wetterich flow Eq. (1);
- classical gauge-fixed EH/FP vertex ansatz Eqs. (3)–(5);
- external TT projection Eq. (6);
- three-point flow/topologies Eq. (7) and Fig. 2;
- symmetric kinematics and extraction Eqs. (9)–(11);
- regulator prescription following Eq. (11);
- eta_h=eta_c=0 analytic baseline Eq. (14).

Propagator/gauge clarification authority:

- arXiv:1403.1232v2, especially gauge-fixed action, harmonic/Landau gauge and regulator definitions;
- arXiv:1612.07315, used only to clarify the closed transverse fluctuation implementation and non-TT internal transverse mode, not to replace the 2015 target.

## FROZEN REALIZATION

- D=4 flat Euclidean background;
- linear split;
- source-Fourier convention `partial_mu -> i p_mu` everywhere;
- harmonic/de-Donder linear gauge with beta=1 and Landau alpha->0;
- external TT legs;
- internal graviton sector is the full Landau-transverse kernel `K(q)=ker F(q)`, not TT-only;
- uniform graviton wave-function normalization inherited from the TT mode;
- source FP ghost sector;
- source optimized regulator `R_phi(x)=Gamma^(2)_{phi phi}|_{mu=0}(x) r(x)`, `x r(x)=(1-x) theta(1-x)`;
- eta_h=eta_c=0 for the frozen analytic baseline comparison;
- no C3 insertions enabled anywhere in this gate.

## FROZEN BENCHMARK COORDINATE

At k=1 use the already-frozen Eq. (14) diagnostic point

`g=1`, `mu_h=1/10`, `lambda_3=-7/10`.

Use the vertex-expansion mass relation

`mu_h=-2 lambda_2`, hence `lambda_2=-1/20` for the internal two-point object at the benchmark.

The prospectively frozen analytic Eq. (14) targets remain

`beta_g = 2 - (274830865/9179907)/pi`,

`beta_lambda3 = 7/5 - (3364922887/183598140)/pi`,

`beta_mu = -1/5 + (6554/3993)/pi`.

No coefficient may be inferred by fitting these targets.

## PHASE A3.1 — INTERNAL PROPAGATOR / REGULATOR CALIBRATION

For every nonzero internal q construct the 10-dimensional real symmetric-tensor basis and the source gauge map

`F_mu[h;q] = i q^nu h_mu nu - (i/2) q_mu tr(h)`.

Construct an orthonormal numerical basis of

`K(q)=ker F(q)`.

Frozen controls:

1. `dim K(q)=6` for generic nonzero q.
2. All five independently constructed TT polarizations lie in K(q).
3. The sixth transverse non-TT direction is retained; a TT-only 5-dimensional replacement must fail the negative control.
4. Restrict the source-Fourier EH two-point Hessian to K(q) using the validated SF055A2 action generator.
5. On the TT subspace, the Hessian must reproduce `K_EH (q^2-2 lambda_2)` with `K_EH=1/(32 pi)` to absolute tolerance `1e-10`.
6. Construct `H_0(q)` at lambda_2=0 and `R_h(q)=H_0(q) r(q^2)` as a full 6x6 tensor on K(q).
7. For `0<q^2<1`, the regulated TT inverse-propagator eigenvalue must equal `K_EH (1+mu_h)` at the benchmark to absolute tolerance `2e-10`.
8. Numerical inverse residual `||P_h P_h^{-1}-I||_max <= 1e-10` at frozen q controls.
9. Ghost two-point/regulator must reproduce source-Fourier `-q^2 I`, optimized regulated `-I` for `0<q^2<1`, and inverse residual <= `1e-12`.
10. Full-matrix regulator identity `R_h-H_0 r=0` is checked directly; a scalar/projector substitute is not accepted.

Frozen q controls:

- `(sqrt(0.2),0,0,0)`;
- `(0.3,0.4,0,0)` with q^2=0.25;
- `(0.2,-0.3,0.4,0.1)`;
- `(1.2,0,0,0)` as an above-cutoff regulator control.

## PHASE A3.2 — FIGURE-2 BASELINE LOOP ASSEMBLY

After A3.1 passes, assemble exactly the Lane-C/source topologies with no C3 insertions:

- graviton 5-vertex tadpole coefficient `-1/2`;
- graviton 4/3 bubble coefficient `+3`;
- graviton 3/3/3 triangle coefficient `-3`;
- ghost triangle coefficient `+6`;
- full external-momentum symmetrisation.

All internal graviton contractions must use the A3.1 full 6-dimensional Landau-transverse propagator. All n=3,4,5 EH and ghost-h tensors come from the validated source-Fourier seed generator.

## LOOP MOMENTUM ROUTING

Use a single loop momentum `q` and source-consistent shifted momenta generated mechanically from graph incidence. Every vertex must receive momenta whose sum is zero. Routing-equivalent shifts are a mandatory consistency control before integration.

No topology may use a manually tuned momentum assignment to improve agreement.

## QUADRATURE / CONVERGENCE FREEZE

Exploit rotational symmetry only after the tensor contractions are constructed source-faithfully.

For the optimized regulator, integrate the compact support induced by `dot R` using deterministic Gauss-Legendre quadrature in radial and angular variables.

Required convergence sequence for every published-baseline scalar extraction:

`N = 8, 12, 16, 24` per active quadrature dimension where tensor-reduced integration permits this directly; if a lower-dimensional analytic angular reduction is derived before output, record the derivation and apply the same increasing-order principle.

Numerical convergence PASS requires the N=16 to N=24 change to be <= `2e-3` relative (or <=`2e-6` absolute for values below `1e-3`).

## BASELINE REPRODUCTION PASS THRESHOLDS

After convergence passes, the same code path must reproduce each frozen Eq. (14) beta target at the benchmark with

- relative error <= `1e-2` for `beta_g`,
- relative error <= `1e-2` for `beta_lambda3`,
- relative error <= `1e-2` for `beta_mu`.

All three must pass. Agreement of only one or two equations is FAIL, not partial PASS.

The implementation must additionally reproduce the source finite-difference/extraction architecture of Eqs. (10)–(11); direct insertion of Eq. (14) is forbidden.

## NEGATIVE CONTROLS

The checker must reject at least:

- TT-only internal graviton propagation;
- deletion of the transverse non-TT mode;
- scalar regulator substituted for `H_0 r`;
- wrong optimized-regulator support;
- omission of any Figure-2 topology;
- sign flip of the ghost trace;
- omission of external symmetrisation;
- wrong loop routing at one vertex;
- return to the invalid real-exponential derivative convention;
- fitting a kernel coefficient to Eq. (14).

## PASS

`PASS_LANE_A_BASELINE_EH_GHOST_THREE_POINT_FLOW_REPRODUCTION_SCOPED`

only if A3.1, A3.2, quadrature convergence and all three baseline targets pass under the frozen criteria.

## FAIL

`FAIL_LANE_A_BASELINE_REPRODUCTION_SCOPED`

if the source-closed implementation is numerically converged but misses the frozen source baseline beyond tolerance.

## BLOCKED

`BLOCKED_LANE_A_IMPLEMENTATION_OBJECT` only if a required source-defined object cannot be constructed without an additional unsupported convention.

## INVALID

Any post-output change to gauge, momentum convention, propagator subspace, regulator tensor prescription, benchmark point, topology coefficients, extraction rule, or PASS tolerance requires a new prospectively frozen gate.

## INTERPRETATION CEILING

Even a PASS only validates the frozen EH/ghost baseline implementation path. It does not itself compute or validate a C3 beta function, fixed point, regulator independence, background/fluctuation equality, Lorentzian matching, SF025 b, or a successor selector.
