# SF055A3Q6P merge-only recovery — prospective control-only freeze

Date: 2026-09-16

## Authority

Authoritative frozen shard run: `35044525051`, head `521812df9f1084bcae0aef816f460dad2041c455`.

All eight preregistered Q6P shard jobs completed successfully. The three merge jobs failed only after artifact download because the merge environment did not install NumPy; the log terminates at `ModuleNotFoundError: No module named 'numpy'` before the merge script can read the shard JSON files.

This gate is infrastructure/provenance recovery only. It does not alter Q6 science.

## Frozen object

Recover exactly the three complete merged records from the already-existing shard artifacts of run `35044525051`:

- `p16N24`: shards 0,1,2;
- `p32N16`: shards 0,1;
- `p32N24`: shards 0,1,2.

Use the already-authoritative merge function in `scripts/sf055a3q6p_yshard.py` without scientific modification.

## Allowed repair

Create a merge-only workflow that:

1. checks out the repository;
2. installs Python plus the same import dependencies used by the successful shard jobs (`numpy`, `numba`);
3. downloads only the named artifacts from source run `35044525051`;
4. invokes `sf055a3q6p_yshard.py --mode merge` for each frozen point;
5. verifies exact shard-ID coverage, exact y-index coverage, exact node budget, and `C3_enabled=false` through the unchanged merge function;
6. uploads the three merged JSON records plus a manifest containing source run/head and file SHA256 digests.

## Forbidden changes

No shard recomputation. No change to Q6/Q6P integrands, Q4 geometry, allocator, node counts, p/N values, y assignments, merge arithmetic, source objects, regulator, projectors, normalisations, Richardson extraction, 0.2% convergence criterion, 1% target criterion, or C3 state. No partial-shard scientific interpretation.

## PASS

`PASS_Q6P_MERGE_ONLY_RECOVERY_SCOPED` iff all three complete merged records are produced from the original run artifacts and each satisfies exact metadata/coverage/node-budget/C3 controls.

## BLOCKED / INVALID

- infrastructure failure before complete merge: `BLOCKED_Q6P_MERGE_RECOVERY_INFRASTRUCTURE_SCOPED`;
- missing/inconsistent shard metadata or failed coverage: `INVALID_Q6P_MERGED_PROVENANCE`.

## Interpretation ceiling

A merge recovery PASS is not Q6 baseline PASS. Only after complete merged records exist may the unchanged Q6 aggregate/convergence/target contract be applied. Historical baseline BLOCKED remains historical authority until a prospectively authorized successor verdict is completed.
