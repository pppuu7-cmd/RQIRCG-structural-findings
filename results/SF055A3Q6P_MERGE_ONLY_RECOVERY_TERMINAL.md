# SF055A3Q6P merge-only recovery — TERMINAL

Date: 2026-09-16

Preregistration: `8dab2f6561d4bae1e3b91eba9cd31152a6795082`.

Workflow: `.github/workflows/sf055a3q6p-merge-recovery.yml`, launch commit `1a0e0f53a466ed23178d641f574ee5ff1c1fbaf6`.

Source shard run: `35044525051`, head `521812df9f1084bcae0aef816f460dad2041c455`.

Recovery run: `35132698327`.

Recovery artifact: `10461044772`.

Artifact digest: `sha256:bc2a95fc125e3d0b86c85139c4224c2ceb45aac2034a14b66d30654585477416`.

## Classification

`PASS_Q6P_MERGE_ONLY_RECOVERY_SCOPED`.

Secondary:

`ORIGINAL_Q6P_FATAL_SHARDS_RECOVERED_WITHOUT_RECOMPUTATION_SCOPED`.

## Failure diagnosis retained

The first merge attempt in run `35044525051` downloaded the correct shard artifacts but failed before reading them because the merge job omitted the NumPy dependency. The log terminates at

`ModuleNotFoundError: No module named 'numpy'`.

All eight shard jobs had completed successfully. Therefore the failed merge jobs were infrastructure/packaging failures only, not scientific failures.

## Frozen recovery result

The recovery workflow checked out the original source head, installed only the same Python import dependencies already used by the successful shard jobs, downloaded the original artifacts and called the unchanged `sf055a3q6p_yshard.py --mode merge` function.

Recovered complete records:

- `p=1/16, N=24`: `Flow_G=0.0005465706425780866`, 13824 points;
- `p=1/32, N=16`: `Flow_G=0.0005545825645617645`, 4096 points;
- `p=1/32, N=24`: `Flow_G=0.0005537769479482955`, 13824 points.

For all three records:

- shard-ID coverage is complete;
- y-index coverage is exact;
- total node budget equals `N^3`;
- `C3_enabled=false`;
- no shard was recomputed.

Canonical manifest is archived at

`results/raw/SF055A3Q6P_MERGE_RECOVERY_RUN35132698327_MANIFEST.json`.

## Independent agreement with monolithic Q6

The recovered values agree with the independently completed monolithic Q6 aggregate from run `35040058701` at approximately `1.5e-18` to `2.3e-18` absolute on the three fatal points.

This cross-execution agreement validates the Q6P sharding/merge route for these points; it does not alter the Q6 PASS/BLOCKED/FAIL contract.

## Interpretation ceiling

`MERGE_RECOVERY_PASS != Q6_BASELINE_PASS`.

`GREEN_CI != SCIENCE`.

The scientific Q6 verdict must be taken from the prospectively frozen Q6 contract applied to complete Q6 data.
