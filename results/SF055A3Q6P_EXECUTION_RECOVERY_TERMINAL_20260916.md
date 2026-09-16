# SF055A3Q6P — execution recovery terminal

Date: 2026-09-16

## Object

Recover the already-preregistered Q6P fatal-convergence execution after the first GitHub Actions workflow failed before any job instantiated, without changing any Q6 scientific or numerical contract.

## Prior exact-execution authority

Q6P y-shard equivalence is already terminal:

`PASS_Q6P_Y_SHARD_EXECUTION_EQUIVALENCE_SCOPED`.

At frozen `p=1/16`, `N=8`:

- serial Q6 `Flow_G = -0.0008541599769643584`;
- deterministic two-shard merge `Flow_G = -0.0008541599769643585`;
- absolute error `1.0842021724855044e-19`;
- exact one-time coverage of every y index;
- dropped and duplicate shard controls rejected.

Therefore deterministic y sharding is an exact additive execution transformation of Q6, not a changed quadrature or physical approximation.

## Failed workflow attempt

Launch commit:

`42517365ed6f5a09babc8d9eaa8542c81e1819b3`.

Run:

`35043244628`.

Observed result:

- workflow conclusion `failure`;
- zero instantiated jobs;
- therefore zero Q6 shard executions and zero substantive Q6 values.

Classification:

`INFRASTRUCTURE_WORKFLOW_GRAPH_FAILURE_ONLY`.

This cannot support a scientific Q6 verdict.

## Prospective control-only repair

Before retry, freeze commit:

`d5631d160e567c84daf493fda437c78614556e7f`.

The freeze explicitly preserves:

- Q6 preregistration and code;
- Q6P executor;
- p/N values;
- y-index modulo shard assignment;
- shard counts;
- merge arithmetic;
- source objects, regulator, topology coefficients, projectors and normalisations;
- convergence and target criteria.

Only workflow orchestration was allowed to change.

Repair commit:

`521812df9f1084bcae0aef816f460dad2041c455`.

The repaired workflow uses explicit lowercase matrix keys and separate merge jobs for the same three frozen fatal points.

## Reproducible execution result

Retry run:

`35044525051`.

The repaired workflow graph successfully instantiated exactly the required eight shard jobs:

- `p=1/16, N=24`: shard 0/3, 1/3, 2/3;
- `p=1/32, N=16`: shard 0/2, 1/2;
- `p=1/32, N=24`: shard 0/3, 1/3, 2/3.

At terminalization of this recovery gate these jobs were queued, so no partial scientific value was read or used.

## Classification

`PASS_Q6P_WORKFLOW_GRAPH_RECOVERY_SCOPED`.

Secondary:

`Q6P_FATAL_POINT_EXECUTION_OBJECT_RESTORED_WITHOUT_SCIENCE_CONTRACT_CHANGE_SCOPED`.

## What this PASS means

It establishes only that:

1. the original failure occurred before Q6 execution;
2. the repair was prospectively frozen and workflow-only;
3. the repaired Actions graph now represents the same already-validated Q6P sharding and the same frozen fatal-point set;
4. all eight required shard jobs are instantiated.

## What this PASS does not mean

It does **not** establish Q6 numerical convergence, baseline PASS, C3 beta, physical C3 matching, asymptotic-safety correctness, or a quantum-gravity result.

`GREEN_OR_INSTANTIATED_CI != SCIENCE`.

`Q6P_EXECUTION_RECOVERY_PASS != Q6_BASELINE_PASS`.

`Q6_BASELINE_PASS != DERIVATIVE_TRUNCATION_CONTROL`.

## Exact next authority

Run `35044525051` is the sole authoritative fatal-point execution until terminal.

Do not use partial shards. Once all required shard and merge jobs are terminal:

1. verify complete shard IDs and exact y-index coverage;
2. verify exact node budget and `C3_enabled=false`;
3. use only the three complete merged records;
4. apply the unchanged Q6 extraction, convergence and target rules;
5. terminalize Q6 according to its prospective PASS/BLOCKED/FAIL criteria.
