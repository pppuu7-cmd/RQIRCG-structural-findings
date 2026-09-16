# SF055A3Q6P — workflow control-only repair freeze

Date: 2026-09-16

## Trigger

Authoritative execution attempt `35043244628` at head `42517365ed6f5a09babc8d9eaa8542c81e1819b3` ended `conclusion=failure` with **zero instantiated jobs**. Therefore no Q6 shard executed and no substantive Q6 value was produced.

Classification of that attempt: `INFRASTRUCTURE_WORKFLOW_GRAPH_FAILURE_ONLY`.

## Frozen repair scope

This repair changes only GitHub Actions orchestration. It MUST NOT change:

- Q6 preregistered physics/numerics;
- `scripts/sf055a3q6p_yshard.py`;
- Q6 node allocator;
- p values;
- N values;
- shard assignment `y_index mod nshards`;
- shard counts;
- merge arithmetic;
- source objects, topology coefficients, regulator, projectors or normalisations;
- convergence/target criteria.

The exact requested fatal points remain:

- `p=1/16, N=24, nshards=3`;
- `p=1/32, N=16, nshards=2`;
- `p=1/32, N=24, nshards=3`.

## Allowed workflow-only changes

1. Replace ambiguous short/uppercase matrix keys by explicit lowercase keys `nshards` and `shard_id`.
2. Avoid a matrix-dependent merge job; use three explicit merge jobs, one for each frozen `(p,N)` point.
3. Keep `fail-fast:false` for the shard matrix.
4. Keep the same Python/runtime dependencies.
5. Upload each shard and each merged JSON as before.

No substantive output from a retry may be used unless all shards required for that point complete and the exact coverage/merge checks in the unchanged Q6P script pass.

## Interpretation ceiling

A green repaired workflow is only execution/provenance. Scientific convergence still depends on the frozen Q6 aggregate comparison. `GREEN_CI != SCIENCE`.
