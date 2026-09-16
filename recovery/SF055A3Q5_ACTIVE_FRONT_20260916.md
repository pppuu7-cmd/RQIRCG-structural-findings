# SF055A3Q5 active frontier addendum

Date: 2026-09-16
Main before addendum: `12cdc03f5e35b8040cb8ec36ef2aa4f09748969e`.
This addendum supplements, not rewrites, `recovery/CURRENT_FRONT.md` while Q5 is non-terminal.

## Auto-research read
The authoritative Q4 terminal result is retained:
`PASS_SHIFTED_REGULATOR_INTERSECTION_GEOMETRY_AND_PIECEWISE_EQUIVALENCE_SCOPED`.
The historical original baseline remains:
`BLOCKED_LANE_A_BASELINE_QUADRATURE_NOT_CONVERGED_SCOPED`.
`SF055_TERMINAL_PASS=FALSE`; C3 remains disabled.

Q4 established exact shifted-Litim intersection geometry and authorized exactly one next science calculation: `FULL_TENSOR_PIECEWISE_BASELINE_IMPLEMENTATION_RETRY_UNDER_ORIGINAL_FREEZE`.

## Q5 prospective science branch
Branch: `sf055a3-piecewise-baseline-20260916`, created from original baseline implementation head `1828aeb994265cb78691493a21bdd4f120a30d58` so the executed source code path is preserved.
Draft PR: #17.

Q5 preregistration: `prereg/SF055A3Q5_FULL_TENSOR_PIECEWISE_BASELINE_RETRY_PREOUTCOME.md`, freeze commit `6a031dc34f67705ba355b40596513a91bfecd967`.

Only authorized implementation change: make the exact Q4 shifted-sphere surfaces nested boundaries of the same three-point reduced integral. Same source vertices, propagators, optimized regulator, topology coefficients, complete projectors, Sym_3, measure, p ladder, Richardson stencil, N={8,12,16,24}, 0.2% convergence rule and 1% target thresholds. Two-point beta_mu path is unchanged. No C3.

Implementation: `scripts/sf055a3q5_piecewise_baseline.py`, commit `2953c1a2ce20516f70eeb36361326f4f8d72ea63`.
Workflow: `.github/workflows/sf055a3q5-piecewise-baseline.yml`, commit `8f5811e6b959e93265c9693c16e3322d23cd6048`.
Actions run `35039027783`; at this addendum its equivalence job `104614507478` is QUEUED. Queue state is infrastructure only and is not scientific authority.

No Q5 full-tensor baseline verdict exists yet. Do not infer PASS/FAIL from target proximity, queue state, or code review.

## Completed Q5 derivative-regularity control
Before full output, a separate implementation/numerical-analysis control was prospectively frozen at `2a95bbfd78c651ff89435f71090ce42cb9ed8efd`.

Classification:
`BOSE_ROTATIONAL_SYMMETRY_DOES_NOT_IMPLY_P2_ANALYTICITY_SCOPED`.

Result branch terminal: `results/SF055A3Q5_RICHARDSON_REGULARITY_CONTROL_TERMINAL.md`, commit `c8cd89195dbc11a63321a330dda6dc702ea531ec`.
Raw: `results/raw/SF055A3Q5_RICHARDSON_REGULARITY_CONTROL_LOCAL.json`, commit `9311133edbc072afc0069645c1d0beb4c3ac98f7`.
Repository checker latest implementation: `0eddbd0e724f68d73ae3f5b286db8c4445f6c73d`.

For the sharp-regulator scalar counterexample class,
`J=J0+c2 p^2+c3 |p|^3+O(p^4)`, with
`c2=-1/[64 pi^2(1+mu)^2]` and
`c3=[8-5(1+mu)]/[180 pi^3(1+mu)^3]`.
At mu=0.1, c3 is nonzero. O(4) invariance makes the three canonical rotated copies identical, so an equal-weight three-shift sum has coefficient 3c3 rather than canceling it.

For a generic `F=F0+A p^2+B |p|^3+C p^4+...`, the frozen estimator satisfies
`R_h=A+(2/3)B h` through that order. Thus symmetry alone does not justify an O(h^4) Richardson truncation assumption. In the scalar witness at h=1/32 the relative bias magnitude is about 0.535875%; this is NOT an estimate of the full tensor gravitational bias.

A zero-sum signed combination can cancel the rotated scalar copies, demonstrating that cancellation requires an extra coefficient relation/dynamical identity. Whether the actual tensor/topology sum provides such a cancellation remains open and must be checked, not assumed.

## Current exact scientific status
Programme classification remains `MISSING_OBJECT_OR_CONTROL_BLOCKER_SCOPED` until the full Q5 matrix terminalizes under the original classifier.

Retain locks:
- no physical SF025 b;
- no projected dynamical C3 beta;
- no background/fluctuation equality;
- no Lorentzian matching;
- no quantum chi_ABC;
- no new physics/theory-established claim.

## Exact next admissible action
Consume the Q5 equivalence result when terminal. If it fails, preserve `INVALID_OR_BLOCKED_Q5_PIECEWISE_IMPLEMENTATION` and do not inspect a science matrix. If it passes, complete the frozen full matrix and apply the original aggregator unchanged. Separately report derivative truncation uncertainty/cancellation; do not promote N-convergence alone to an h->0 theorem.
