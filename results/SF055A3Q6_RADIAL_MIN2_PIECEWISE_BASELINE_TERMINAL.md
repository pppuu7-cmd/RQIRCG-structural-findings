# SF055A3Q6 radial-min2 piecewise baseline — TERMINAL

Date: 2026-09-16

Preregistration: `54fe1870177ce8d9155bd0731203197761bed5dc`.

Workflow run: `35040058701`, head `4b6c6902376e88f49c291813ecc4250edc8f32ee`.

Aggregate artifact: `10429809775`, digest `sha256:cfbd1546ec1b0fdc08be2dfce15d6d7660bf3e83ae38f51ea769fe303c9e1485`.

Preflight artifact: `10424957402`, digest `sha256:89fba3d99d76dd86e7919abdf72439da67027bac209aa731333ff424e9e634fc`.

Canonical compact summary: `results/raw/SF055A3Q6_TERMINAL_SUMMARY_RUN35040058701.json`.

## Classification

`BLOCKED_LANE_A_Q6_PIECEWISE_BASELINE_NOT_CONVERGED_SCOPED`.

This is exactly the preregistered BLOCKED branch: implementation controls pass, but the frozen historical convergence criterion fails.

## Implementation controls

All required pre-beta implementation controls passed:

- source/JIT n=2..5 equivalence;
- fixed-q topology equivalence;
- p=0 composite-rule identity with the historical unsplit rule;
- exact node budgets;
- Q4 piecewise support geometry;
- smooth reduced-measure controls at about `1e-17` absolute error;
- nonzero piecewise thin-shell control where the historical unsplit finite grid gives zero;
- negative controls reject dropped radial pieces, support mutation, target rescaling and post-output allocator substitution.

`C3_enabled=false` throughout.

## Complete Q6 result

At N=16:

- `beta_g=-3.4763144983440384`;
- `beta_lambda3=-3.015202432913556`;
- `beta_mu=0.3224650623712873`.

At N=24:

- `beta_g=-7.590697586295343`;
- `beta_lambda3=-4.455236523767682`;
- `beta_mu=0.3224650623712883`.

Frozen N16->N24 relative changes:

- `beta_g=0.5420296410411126` = 54.2029641%;
- `beta_lambda3=0.3232228150339199` = 32.3222815%;
- `beta_mu=3.098632499331524e-15`.

Frozen allowed relative change is `0.002` = 0.2%.

Therefore convergence fails decisively for beta_g and beta_lambda3.

## Target proximity does not rescue convergence

At N=24, all separate 1% Eq.(14) target checks pass:

- beta_g relative target error `0.008106450284486958` = 0.810645%;
- beta_lambda3 relative target error `0.004818266531148309` = 0.481827%;
- beta_mu relative target error `7.57443499836589e-15`.

The preregistered logic requires convergence before target reproduction can support PASS. Hence `target_pass=true` and `convergence_pass=false` correctly yield BLOCKED, not PASS.

The separate p=1 finite-difference control also passes and remains distinct from the Eq.(14) derivative-at-zero target.

## Independent Q6P cross-execution verification

The three fatal derivative-sensitive points were independently recomputed through prospectively validated deterministic y-sharding and recovered by merge-only run `35132698327`.

Agreement with the monolithic Q6 aggregate:

- p=1/16,N=24: absolute difference about `1.52e-18`;
- p=1/32,N=16: about `2.28e-18`;
- p=1/32,N=24: about `2.06e-18`.

Thus the failure of beta convergence is not explained by monolithic-vs-sharded execution or merge arithmetic.

## New scientific/numerical fact

Exact shifted-Litim shell partition plus minimum-two-node radial quadrature closes the Q5 implementation defect and reproduces the frozen targets at N24, but **does not produce a converged derivative extraction** on the frozen N16->N24 sequence.

Therefore the active blocker is no longer missing support geometry or the Q5 one-node radial allocation. It is localized downstream to derivative regularity/truncation and/or residual finite-N resolution of the momentum derivative.

Retain:

`PIECEWISE_SUPPORT_CLOSURE != DERIVATIVE_CONVERGENCE`.

`TARGET_PROXIMITY != CONVERGENCE`.

## Interpretation ceiling

`Q6_BLOCKED != ASYMPTOTIC_SAFETY_FAIL`.

`Q6_BLOCKED != PHYSICAL_C3_RESULT`.

`Q6_BLOCKED != DERIVATIVE_TRUNCATION_CLOSURE`.

No physical SF025 b is selected. No projected C3 beta is computed. SF055 remains non-terminal.
