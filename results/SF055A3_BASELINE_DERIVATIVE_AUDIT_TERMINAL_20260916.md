# SF055A3 baseline derivative conditioning and regulator-shell audit - TERMINAL

Date: 2026-09-16
Diagnostic preregistration: `052eb59b2155adbfbc2e52b6dbf0137525578e68`.

## Status separation

Historical baseline result, retained without alteration:

`BLOCKED_LANE_A_BASELINE_QUADRATURE_NOT_CONVERGED_SCOPED`.

New diagnostic result:

`PASS_SCOPED_DERIVATIVE_CONDITIONING_AND_REGULATOR_SHELL_DIAGNOSTIC`.

Programme-level verdict under the frozen execution plan:

`MISSING_OBJECT_OR_CONTROL_BLOCKER_SCOPED`.

A diagnostic PASS does not promote Lane A or SF055. C3 remains disabled; no physical matching b, quantum chi_ABC or new principle is selected. The present result is a computational/mathematical localization of a calibration obstacle, not a no-go theorem for the physical research programme.

## State and automation inspected

The read-only starting main was `7898ae6aea08feaf2488f2b3c742f7a46d386fd4`. The recovery file was stale concerning Q1: its terminal result and summary were already committed in that main. Q1 is therefore closed as an exact-projector-regrouping PASS, not still in progress. Its result does not close the integrated baseline.

The latest baseline run was inspected through its jobs, full aggregate log, actual downloaded aggregate ZIP, code and frozen contracts:

- PR 16, branch `sf055a3-baseline-quadrature-20260915`, remains unmerged at this audit;
- executed head `1828aeb994265cb78691493a21bdd4f120a30d58`;
- run `35019599951`, aggregate job `104590644553`;
- checkout merge `3c1ce57310bc465805dea98cbee8c9cc08c0f8cb`;
- aggregate artifact `10421617496`;
- ZIP SHA256 `85f0a9dd92d067ada9bbcccba8fbb3059d7545e4e039865cd26ff7b30ad10952`;
- extracted JSON SHA256 `5d934d4bfe721ab28c36c179f9817f19087bd04dee550ccea3bed511f88fb955`.

The ZIP digest was checked locally. The source JSON is archived unchanged at `results/raw/SF055A3_BASELINE_AGGREGATE_RUN35019599951.json` (commit `0f59cae8736a1161e81d14b75a071838b35b8803`). No missing input is reported. Preflight, 18 three-point jobs and four two-point jobs completed successfully; the aggregate failed its scientific convergence check. This is not an infrastructure crash and not a missing-artifact failure.

This audit read the current recovery, Q1 terminal diff/raw summary, the active source contract, the programme execution plan, the quadrature implementation freeze, the reducer and relevant integrand code. It did not independently re-prove all historical SF001-SF054 results or rerun the expensive full tensor matrix.

## Selected iteration question and prospective boundary

The efficient next question is not another unconstrained principle search or a blind repeat of the matrix. It is: do the two unstable beta values reflect independent defects, or the propagation of one insufficiently resolved momentum derivative? What mathematically justified numerical correction could address that derivative while leaving the physics and tolerances unchanged?

The original aggregate was known before the diagnostic freeze. Therefore the freeze is prospective only for the new quantitative diagnostic and scalar controls. It is not described as a blinded preregistration of the old outcome. No derivative stencil or momentum point was selected for improved agreement after seeing the target.

## Retained physics and calibration contract

D=4 flat Euclidean source-Fourier realization; full six-dimensional Landau-transverse graviton internal space; source EH/FP vertices; optimized regulator; canonical G dotR G line; topology coefficients (-1/2,+3,-3,+6); source Sym_3=(1/6)sum_S3; measure d4q/(2pi)^4. Retain g=1, mu=1/10, lambda_2=-1/20, lambda_3=-7/10, eta_h=eta_c=0 and the source-derived projector norms.

`N_g = 1/0.00052874519051635`, `N_lambda = 1/0.0026385724906858796`.

The convergence sequence N=8,12,16,24 and the original thresholds remain unchanged. The p=1 finite-difference extraction is not the derivative-at-p=0 Eq. (14) target. The primary source [1] explicitly distinguishes these projection prescriptions. No published formula is inserted into the integrand as its answer.

## Baseline replay

At N=24:

| Quantity | Computed | Frozen target | Relative target discrepancy | Relative N16-to-N24 change |
|---|---:|---:|---:|---:|
| beta_g | -7.461665474536886 | -7.529658781722162 | 0.903006486% | 2.852652658% |
| beta_lambda3 | -4.4100752846522155 | -4.433872942167074 | 0.536723939% | 1.689299492% |
| beta_mu | 0.3224650623712883 | 0.32246506237129074 | 7.57e-13% | 2.07e-13% |

All three satisfy the separate 1% agreement test, but the first two fail the 0.2% inter-order convergence requirement. Hence `target_pass=true` and `convergence_pass=false` coexist consistently. The frozen aggregate correctly refuses a physics PASS. Replaying all four N rows from their archived primitive flow values reproduced the printed beta values with zero floating-point difference in this environment.

## Result A: exact conditioning of the frozen derivative

For clarity write `F(p)=Flow_G(p^2)`, with p the momentum magnitude. With h=1/32, the frozen reducer is

`D(h)=[F(h)-F(0)]/h^2`,

`R_h=[4 D(h)-D(2h)]/3`

`=4 F(h)/(3 h^2)-F(2h)/(12 h^2)-5 F(0)/(4 h^2)`.

The exact weights for (F(0),F(h),F(2h)) are

`(-1280, 4096/3, -256/3)`.

Their absolute sum is `8/(3 h^2)=2730.6666666666665`. Thus if the three input errors have absolute bounds epsilon, then

`|delta R_h| <= [8/(3 h^2)] epsilon`,

`|delta beta_g| <= [16 N_g/(3 h^2)] epsilon`

`=10328856.756124869 epsilon`.

The bound is sharp for independent worst-case errors: choose their signs to agree with the stencil weights. Correlated numerical errors can cancel; the bound is sufficient, not necessary.

The old primitive-flow absolute threshold 2e-6 alone would allow a worst-case beta_g change as large as 20.6577. This does NOT say the observed error has that size. It shows why convergence of each small primitive flow under that threshold does not imply convergence of its derived beta. The original aggregate's additional beta checks are essential and already caught the problem.

Using the actual N24 magnitude as a scale, a common bound of approximately `1.4448192381237589e-9` on the three input perturbations would suffice to guarantee a 0.2% beta_g change under this worst-case model. This is a diagnostic budgeting number, not a retrospectively changed pass threshold. Adjacent quadrature differences are not certified absolute error bounds.

The stencil annihilates constants and p^4, returns the p^2 coefficient, and has p^6 moment `-4 h^4`. However its |p|^3 moment is `2 h/3`. Therefore fourth-order Richardson bias cancellation requires the appropriate smooth expansion in p^2; evenness in signed p alone does not establish that expansion.

## Result B: the two unstable outputs share one dominant error direction

The same source equations give

`beta_g=2+2 N_g R_h`,

`beta_lambda3=(-1-beta_g/2)lambda_3+N_lambda F_lambda(0)`.

Consequently

`delta beta_lambda3=-(lambda_3/2)delta beta_g+N_lambda delta F_lambda(0)`.

For the archived N16-to-N24 changes:

- delta R_h = 5.6273134106739515e-5;
- delta beta_g = 0.21285539846437374;
- delta beta_lambda3 = 0.07449937939135598;
- derivative-mediated contribution to delta beta_lambda3 = 0.0744993894625309;
- F_lambda(0) contribution = -1.0071174744890123e-8.

Thus the second instability is almost entirely the expected propagation of the first derivative instability, not evidence for a second independent large error.

The derivative-insensitive combination is

`C=beta_lambda3+(lambda_3/2)beta_g=-lambda_3+N_lambda F_lambda(0)`.

At the frozen point it is `beta_lambda3-0.35 beta_g`. Its N24 value is -1.7984923685643057; the corresponding target combination is -1.7984923685643177. Their relative difference is about 6.67e-15. This is an algebraic diagnostic, not a new independent baseline target or an additional physical result.

The full Jacobian with respect to (R_h,F_lambda(0)) has determinant `2 N_g N_lambda` and rank two. Only the dominant propagated uncertainty direction is one-dimensional. No theory-space information rank, matching-selector rank or global uniqueness is inferred from this numerical coordinate transformation.

## Result C: an explicit regulator-shell counterexample

The actual code includes shifted denominators of the form `max(1,|q+p_i|^2)+mu` while integrating a compact single-scale support. To test a real numerical hazard without claiming to reproduce the full tensor calculation, define the scalar control

`J_mu(p)=integral_{|q|<1} d4q/(2pi)^4 [max(1,|q+p e_1|^2)+mu]^-1`,

with `mu=1/10` and `a=1+mu`.

This is a denominator-regularity witness only. It has no physical graviton projector, vertex numerator or topology cancellation.

### Leading shell coefficient

At p=0, `J_mu(0)=1/(32 pi^2 a)`. For p>0, the change resides in a thin outward shell. Put `q=(1-p t)n`, `u=n.e_1`. To leading order, the shell is `u>0`, `0<t<u` and

`|q+p e_1|^2-1=2p(u-t)+O(p^2)`.

The measure supplies one power of p and the reciprocal-denominator change another. Integration over t gives u^2; on S^3, the outward-hemisphere integral of u^2 is pi^2/4. Therefore

`J_mu(p)=J_mu(0)-p^2/[64 pi^2 a^2]+O(|p|^3)`.

The integrated derivative with respect to p^2 at zero is nonzero:

`c2=-1/[64 pi^2 a^2]=-0.0013083830532326674`.

### Finite-node differentiation misses it

For every fixed finite interior quadrature grid define `delta_N=1-max_i |q_i|>0`. If `|p|<delta_N`, every shifted quadrature node remains inside the regulator sphere. The evaluated denominator is a at every node and `J_N(p)=J_N(0)` exactly. Hence its nodewise derivative at p=0 vanishes exactly for every N, whereas the derivative of the integrated continuum expression is c2, not zero.

This proves that these two operations cannot be interchanged for this control: taking the continuum quadrature limit and taking the derivative at p=0. Arbitrarily decreasing the difference step at fixed nodes, or automatic differentiation of the fixed-node integrand, is not by itself a valid repair. It may remove the entire leading boundary contribution rather than improve it.

### Independent split-domain integration

For angular u=cos(theta), the exact cutoff intersection is

`r_b=-p u+sqrt(1-p^2(1-u^2))`.

The shell exists for `u>-p/2`; integrate `theta in [0,acos(-p/2)]`, `r in [r_b,1]`, with weight `sin^2(theta) r^3/(4 pi^3)`. The implementation computes J(p)-J(0) directly and uses a stable expression for shell width,

`1-r_b=(2pu+p^2)/(1+pu+sqrt(1-p^2(1-u^2)))`.

No coefficient or boundary is chosen from a gravity target. Independent split Gauss-Legendre and adaptive integration agree to approximately 4.1e-15 to 4.5e-15 relative at three frozen check momenta. These are numerical consistency checks, not rigorous interval bounds.

At p=1/4096, the numerical p^2 coefficient divided by c2 is 0.999937197196481. The split-domain evaluation resolves the shell even at this small p. The original unsplit rule was also applied to this scalar control at N=8,12,16,24 and exhibits non-monotone derivative estimates; at sufficiently small p each finite grid returns an exactly zero shell contribution, as proved above.

### Exploratory higher-order refinement

After the preregistered leading-shell analysis, an additional analytic refinement was derived and tested:

`J_mu(p)=J_mu(0)+c2 p^2+c3 |p|^3+O(p^4)`,

`c3=(8-5a)/(180 pi^3 a^3)`.

For transparency, this cubic coefficient is an exploratory result, not an originally specified target. It is derived by expanding with depth x=1-r. The radial integrals of the first and second powers of the excess denominator are

`p^2 u^2+p^3(u-5u^3/3)+O(p^4)` and `4 p^3 u^3/3+O(p^4)`.

Using `integral_0^1 u sqrt(1-u^2)du=1/3` and `integral_0^1 u^3 sqrt(1-u^2)du=2/15` gives the stated coefficient. Reflection invariance extends the p>0 result to |p|^3. At mu=0.1, c3=0.0003365424329368007; the small-p numerical estimate approaches it.

This demonstrates explicitly that a piecewise-regulated even function can contain |p|^3. The frozen Richardson stencil then has an O(h) bias from that term rather than the O(h^4) bias valid for an even analytic series. The existence or cancellation of the corresponding term in the full graviton flow is NOT established by this scalar example.

## What is established, and what is not

Established here: exact propagation of the archived baseline errors; one dominant derivative direction connecting the two failing beta values; a quantitative sufficient input-error budget; a mathematical boundary-layer witness where finite-grid differentiation fails; and validated split-domain scalar controls.

Not established: that the regulator shell is the sole or quantitatively dominant source of the full graviton discrepancy; that the full flow contains a noncancelled |p|^3 term; a corrected full tensor integration; a certified derivative truncation-error bound; baseline PASS; C3 flow; Nielsen/split closure; Lorentzian matching; physical b; a new quantum theory or chi_ABC. No covariance, conservation, physical state space or regulator law was changed in this audit. A scalar numerical control is not a positivity or causality proof for quantum gravity.

## Reproducible evidence

Script: `scripts/sf055a3_derivative_audit.py`, commit `ef2202a43772410e6b713b3ccfcbdfddd1dfea6f`.
Script SHA256: `d4ccad6c83c60e1dec7cde1f405b6f77ed7c05e61f0d93a8f4c7ad8ecda4183d`.
New raw output: `results/raw/SF055A3_DERIVATIVE_AUDIT_20260916.json`, commit `5d8d84f8cf981d700b10f22c9451e3ba9b3d8fb6`.
Raw SHA256: `f30f8745e5044edd4c01a4919e53083f4d996b520130cd2bd81655665eb6e725`.

All 19 diagnostic checks passed locally; failures=[]. They include exact symbolic identities, replay tests and numerical controls, not 19 independent physical proofs. No new GitHub Actions run was launched. The archived baseline was replayed, not recomputed.

Reproduce from repository root:

```bash
python scripts/sf055a3_derivative_audit.py --input results/raw/SF055A3_BASELINE_AGGREGATE_RUN35019599951.json --out results/raw/SF055A3_DERIVATIVE_AUDIT_REPLAY.json
```

Python 3.13.5, NumPy 2.3.5, SciPy 1.17.0 and SymPy 1.14.0 were used. Environment metadata or last floating digits can differ elsewhere.

## Exact next admissible work and hard stop

Do not repeat the same matrix without a justified implementation change and do not enable C3. The current frozen programme is blocked at baseline calibration, not failed as a physical principle.

A defensible implementation correction would first derive all shifted regulator-intersection surfaces for the actual topologies and evaluate the same integrals piecewise, preserving the source objects, momenta, frozen Richardson stencil, N sequence and scientific thresholds. It must pass fixed-integrand equivalence and independent controls before a new full baseline result. The finite-h derivative bias must also be quantified rather than inferred from target proximity.

Changing to an analytic/distributional derivative or another stencil would require its own prospective specification and equivalence/error proof; the historical result is never overwritten by that change. Merely increasing N, shrinking h, taking pointwise derivatives, choosing the apparently best estimate or relaxing 0.2% to the observed error does not close the present gate.

Only a baseline that passes the unchanged applicable criteria can reopen the already-frozen downstream sequence. No new open-ended chain of selector micro-gates is introduced by this diagnostic.

## Sources and ownership

[1] N. Christiansen, B. Knorr, J. Meibohm, J. M. Pawlowski, M. Reichert, Local Quantum Gravity, arXiv:1506.07016v2, equations (10)-(14), https://arxiv.org/abs/1506.07016. The parsed v2 text was consulted for the distinction between the finite-difference and derivative projections; PDF screenshot retrieval was unavailable in this audit. The exact implemented numerical targets are grounded in the frozen repository contract, not reconstructed from an unread equation image.

[2] `prereg/SF055A3_SOURCE_FOURIER_BASELINE_LOOP_REPRODUCTION_PREOUTCOME.md`, `research_log/SF055A3_BASELINE_QUADRATURE_IMPLEMENTATION_FREEZE.md`, `prereg/SF055_TO_PROGRAMME_VERDICT_EXECUTION_PLAN_20260915.md`, and `scripts/sf055a3_baseline_aggregate.py` at executed head `1828aeb994265cb78691493a21bdd4f120a30d58`.

[3] Original Actions aggregate archived above. All conditioning identities and scalar-shell derivations are the present diagnostic analysis, not claims of new results attributed to [1].
