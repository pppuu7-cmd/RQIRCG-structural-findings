# SF055A3Q8 p=1/32 high-resolution derivative convergence and error budget — PROSPECTIVE PREREGISTRATION

Date: 2026-09-16
Status: `PROSPECTIVELY_FROZEN_BEFORE_ANY_Q8_HIGH_RESOLUTION_OUTPUT`.

## Scope and parent separation

This successor is numerical only. It does not alter the terminal Q6 classification, does not choose a programme disposition D1/D2/D3, does not authorize `chi_ABC`, and does not enter substantive C3 physics.

Authoritative retained inputs:

- Q6 preregistration `54fe1870177ce8d9155bd0731203197761bed5dc`;
- terminal Q6 `7fb39877f2415c6367c83af6c9ec0b183509178e` with classification `BLOCKED_LANE_A_Q6_PIECEWISE_BASELINE_NOT_CONVERGED_SCOPED`;
- canonical Q6 derivative ladder `results/raw/SF055A3Q6_DERIVATIVE_LADDER_CANONICAL.json`;
- Q7A terminal localization `results/SF055A3Q7A_FULL_TENSOR_REGULARITY_APPLICATION_TERMINAL.md`, which attributes about 98.9061% of the absolute N16->N24 historical Richardson instability to the smallest frozen momentum `p=1/32`.

Retain:

`P32_ERROR_LOCALIZATION != PERMISSION_TO_DROP_P32`.

`Q8_NUMERICAL_PASS != Q6_PASS`.

## Frozen question

Does the unchanged Q6 p=1/32 primitive flow become numerically stable under stronger quadrature resolution, when all non-p=1/32 ingredients of the historical Richardson construction are held at their already-authoritative Q6 N24 values?

This is deliberately narrower and higher-information-per-cost than rerunning the entire Q6 matrix.

## Frozen executor and physics content

Use the unchanged deterministic Q6 y-shard executor:

- `scripts/sf055a3q6p_yshard.py`, blob `26475668608e897645d8954f98890c7d50b3cdbf`;
- underlying `scripts/sf055a3q6_piecewise_baseline.py`, blob `b2748807d73ada4ac4693d3bf3729bf18a96a539`.

The integrand, shifted-support geometry, radial-min2 allocation rule, source objects, projectors, routing, loop measure, normalisations and `C3_enabled=false` remain unchanged.

No fitted rescaling and no target-based tuning are permitted.

## Frozen high-resolution sequence

Only `p=1/32 = 0.03125` is newly evaluated.

Orders and deterministic y-shards:

- N=32 with 4 shards;
- N=40 with 5 shards;
- N=48 with 8 shards.

Each merged record must have exact y-index coverage, exact `N^3` node budget, complete shard-ID coverage and `C3_enabled=false`.

No N>24 Q8 value may be inspected before this preregistration exists.

## Frozen inherited anchors

Let `h=1/32`.

Hold fixed at authoritative Q6 N24 values:

- `F0 = Flow_G(p=0) = 0.0005562382414400815`;
- `F16 = Flow_G(p=1/16) = 0.0005465706425780851`;
- `N_g^(-1)=0.00052874519051635`, hence `N_g=1/N_g^(-1)`.

For each new N define

`D32(N) = [F32(N)-F0]/h^2`,

`D16_anchor = [F16-F0]/(1/16)^2`,

`R_anchor(N) = [4 D32(N)-D16_anchor]/3`,

`beta_g_anchor(N) = 2 + 2 N_g R_anchor(N)`.

`beta_g_anchor` is a Q8 numerical diagnostic of the dominant primitive-resolution contribution only. It is not a replacement Q6 estimator and cannot rewrite Q6.

The inherited p=0 primitive N16->N24 drift is frozen as an error-floor witness:

`|Delta F0_16_24| = 2.9895975343745274e-11`.

Its propagated absolute contribution to `beta_g_anchor` must be reported, not silently discarded.

## Frozen classification contract

First require provenance/control validity:

- exact expected N in {32,40,48};
- exact p=1/32;
- exact y coverage and exact node budget;
- finite merged `Flow_G`;
- `C3_enabled=false` for every merged record.

Failure of any of these yields

`INVALID_Q8_P32_HIGH_RESOLUTION_PROVENANCE_OR_CONTROL_SCOPED`.

Otherwise define

`rel_40_48 = |beta_g_anchor(48)-beta_g_anchor(40)| / |beta_g_anchor(48)|`

and absolute successive increments

`inc_32_40 = |beta_g_anchor(40)-beta_g_anchor(32)|`,

`inc_40_48 = |beta_g_anchor(48)-beta_g_anchor(40)|`.

The numerical p=1/32 resolution subgate passes iff BOTH:

1. `rel_40_48 <= 0.002`, reusing the historical frozen 0.2% convergence criterion rather than inventing a looser one;
2. `inc_40_48 <= inc_32_40`, requiring the last increment not to grow.

PASS classification:

`PASS_Q8_P32_HIGH_RESOLUTION_NUMERICAL_CONVERGENCE_SCOPED`.

Otherwise:

`BLOCKED_Q8_P32_HIGH_RESOLUTION_NUMERICAL_CONVERGENCE_SCOPED`.

No post-output threshold substitution is permitted.

## Frozen error budget outputs

Report at minimum:

- merged `Flow_G(p=1/32)` for N=32,40,48;
- `D32`, `R_anchor`, and `beta_g_anchor` for each N;
- both successive `beta_g_anchor` increments;
- `rel_40_48` and the two preregistered pass booleans;
- propagated `beta_g_anchor` uncertainty floor from the inherited p=0 N16->N24 primitive drift;
- exact provenance/control flags.

No geometric-tail, Richardson-order, or continuum extrapolation may be promoted without a separate prospective gate.

## Interpretation ceiling and next-gate rule

Even a Q8 PASS establishes only that the dominant p=1/32 primitive is numerically stabilized under this stronger resolution sequence. It does NOT establish:

- Q6 baseline PASS;
- derivative-truncation or regularity closure;
- zero or nonzero continuum `|p|^3` coefficient;
- projected physical C3 flow or physical matching;
- asymptotic-safety correctness or failure;
- any programme disposition or `chi_ABC`.

A Q8 PASS would authorize only a separately preregistered derivative-truncation/regularity gate using the now-resolved primitive. A Q8 BLOCKED would keep resolution of the p=1/32 primitive as the active numerical blocker.
