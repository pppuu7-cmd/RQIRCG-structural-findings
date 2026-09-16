# SF055A3Q6P — y-shard execution equivalence preoutcome

Date: 2026-09-16
Parent science gate: SF055A3Q6, prereg `54fe1870177ce8d9155bd0731203197761bed5dc`.

## Purpose

Accelerate the already-frozen Q6 deterministic quadrature by distributing independent outer-y nodes across workers. This is an execution-equivalence gate only. It may not change any Q6 node, weight, shell boundary, source object, topology coefficient, projector, momentum, N, threshold or beta extraction.

No Q6 N24 substantive output has been inspected at freeze time.

## Exact object

For fixed `(p,N)`, first construct the exact same global Q6 y-node/weight arrays using the prospectively frozen Q6 radial-min2 allocator. A shard receives a prospectively specified subset of integer y indices and evaluates the unchanged nested phi/radial Q6 integrand for only those y nodes.

Every y index must appear exactly once in the complete shard set. No worker-specific quadrature or adaptive refinement is allowed.

## Frozen sharding rule

For `S` shards, shard `s` receives y indices

`i such that i mod S = s`, for `i=0,...,N-1`.

This balances work while remaining deterministic and target-blind.

Each shard records topology sums and count of Q6 points over its assigned y indices. The merger checks exact index coverage and adds shard totals in ascending shard id. Small floating summation-order differences are allowed only within the frozen equivalence tolerance below.

## Required equivalence control

Before any N24 science use, compare at `p=1/8, N=8`:

1. ordinary serial Q6 output;
2. Q6P with `S=2` shards merged under this rule.

For `Flow_G` and every G topology component, require

`abs(sharded-serial) <= 5e-12 * (1+abs(serial))`.

Also require:

- total point count exactly `N^3`;
- all y indices covered once;
- no duplicate y indices;
- same max phi/radial segment ceilings as serial metadata.

A dropped-shard mutation must fail coverage. A duplicated-index mutation must fail coverage. A worker-local alternative node allocator must be rejected by code identity; workers import the Q6 node builder directly.

## PASS

`PASS_Q6P_Y_SHARD_EXECUTION_EQUIVALENCE_SCOPED` iff all equivalence and negative controls pass.

## BLOCKED

`BLOCKED_Q6P_EXECUTION_EQUIVALENCE_SCOPED` if any equivalence/coverage control fails. In that case only serial Q6 remains authoritative.

## Interpretation ceiling

Q6P PASS authorizes only parallel execution of the same Q6 quadrature. It cannot alter the Q6 scientific classification and cannot rescue a convergence or target failure.

Retain:

`PARALLEL_EXECUTION_EQUIVALENCE != SCIENTIFIC_CONVERGENCE`.
