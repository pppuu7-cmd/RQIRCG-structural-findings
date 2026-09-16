# SF055A3Q6P — y-shard execution equivalence terminal

Date: 2026-09-16
Preregistration: `1a9266881aa13ac8ae1a51e16466f00c2426a050`.

## Classification

`PASS_Q6P_Y_SHARD_EXECUTION_EQUIVALENCE_SCOPED`.

## Frozen control

At `p=1/8, N=8`, compare the ordinary serial Q6 quadrature to two deterministic y-shards with assignment `i mod 2` and merge them without changing any global Q6 node, weight, support boundary or integrand.

Frozen tolerance for Flow_G and each G topology component:

`abs(sharded-serial) <= 5e-12*(1+abs(serial))`.

## Result

Serial Flow_G:

`0.0005202256280417457`.

Merged two-shard Flow_G:

`0.0005202256280417462`.

Absolute difference:

`5.421010862427522e-19`.

Topology absolute differences:

- T5_GRAV: `1.8973538018496328e-19`;
- B43_GRAV: `5.421010862427522e-19`;
- T333_GRAV: `8.131516293641283e-20`;
- T333_GHOST: `4.0657581468206416e-20`.

All are many orders of magnitude below the frozen tolerance.

Point count is exactly `8^3=512`; all y indices are covered exactly once. Dropped-shard and duplicated-index mutations are rejected by coverage logic.

## Authority

Q6P may now be used only to distribute the unchanged Q6 quadrature across workers for speed. It does not change the Q6 node allocator, quadrature rule, science thresholds or classification rules.

Queued hosted reproduction workflow `35042418376` is additional provenance only; queue/completion status is not a scientific premise for this terminal algebraic execution-equivalence result.

## Claim ceiling

`PARALLEL_EXECUTION_EQUIVALENCE != SCIENTIFIC_CONVERGENCE`.

`Q6P_PASS != Q6_BASELINE_PASS`.

No C3 flow output is authorized by Q6P itself.
