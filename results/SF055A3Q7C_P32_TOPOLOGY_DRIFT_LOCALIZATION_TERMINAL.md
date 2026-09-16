# SF055A3Q7C p=1/32 topology drift localization — TERMINAL

Date: 2026-09-16

Classification:

`DESCRIPTIVE_Q7C_P32_TOPOLOGY_DRIFT_LOCALIZED_SCOPED`.

This is a retrospective exact decomposition of already-existing Q6 data. It is intentionally **not** presented as prospectively thresholded evidence. No Q8 N>24 value is used.

## Source provenance

Monolithic Q6 run `35040058701`, head `4b6c6902376e88f49c291813ecc4250edc8f32ee`:

- p=1/32,N16 artifact `10427431773`, digest `sha256:77eb1328d16fd839f0d4cf7d1a49f2c0ef33f7b0f64a365c42589c35f481d379`;
- p=1/32,N24 artifact `10426124437`, digest `sha256:3cd0c5def1050cc55a67fc1198e61331e0c6b7b981b22049993a6bcce66dbbc1`.

Independent deterministic y-sharded Q6P merge-recovery:

- run `35132698327`;
- artifact `10461044772`;
- digest `sha256:bc2a95fc125e3d0b86c85139c4224c2ceb45aac2034a14b66d30654585477416`.

Q7C independent execution:

- run `35149044304`;
- head `ccc99eb964311284f96410e0c496a1d061e392f5`;
- conclusion `success`;
- artifact `10467778500`;
- digest `sha256:3dee255da80dfe3bb353582b4ab964a6a73263be184d4c2a261a4f1ca06023e5`.

Raw committed record:

`results/raw/SF055A3Q7C_P32_TOPOLOGY_DRIFT.json`.

## Exact decomposition

Total p=1/32 primitive drift from N16 to N24:

`Delta Flow_G = -8.056166134691499e-07`.

Topology changes:

- `T333_GRAV`: `-5.511214710161362e-07`;
- `B43_GRAV`: `-2.5465286334941557e-07`;
- `T333_GHOST`: `+1.57720897336921e-10`;
- `T5_GRAV`: `-8.944667923005412e-19`.

The topology sum reproduces the full drift with absolute identity residual

`4.0657581468206416e-20`.

## Absolute drift localization

Fractions of the sum of absolute topology changes:

- `T333_GRAV`: `0.6838311833070755` = **68.3831%**;
- `B43_GRAV`: `0.3159731166991083` = **31.5973%**;
- `T333_GHOST`: `0.00019569999270633136` = **0.01957%**;
- `T5_GRAV`: `1.1098538474285905e-12`, numerically negligible at this scale.

Combined `T333_GRAV + B43_GRAV` absolute fraction:

`0.9998043000061838` = **99.98043%**.

Thus the p=1/32 N16->N24 finite-resolution drift is not a generic four-topology instability. It is localized almost completely to the two gravitational topologies `T333_GRAV` and `B43_GRAV`, with `T333_GRAV` the larger contributor.

The small positive ghost change slightly cancels the gravitational drift. `T5_GRAV` is effectively resolution-stable across this pair.

## Independent execution check

Monolithic-vs-y-sharded absolute differences remain at floating-point-level scale.

At N16, the largest topology difference is about `3.25e-18`; at N24 it is about `1.57e-18`. Flow_G differences are about `2.28e-18` and `2.17e-18` respectively.

Therefore the topology localization is not an artifact of monolithic execution or shard merge arithmetic.

## New retained numerical fact

`P32_DRIFT_DOMINATED_BY_T333_GRAV_AND_B43_GRAV_SCOPED`.

More specifically:

`ABSOLUTE_P32_N16_N24_DRIFT_T333_GRAV_PLUS_B43_GRAV_FRACTION ~= 0.9998043`.

This narrows the numerical target for any successor after Q8: if p=1/32 convergence remains blocked, the next topology-resolved resolution control should prioritize `T333_GRAV` and `B43_GRAV` rather than spending equal computational effort on `T5_GRAV` or the ghost topology.

## Interpretation ceiling

Not established:

- Q8 convergence;
- continuum derivative regularity;
- Q6 baseline PASS;
- a physical or continuum meaning for the finite-N topology drift;
- continuum `|p|^3` coefficient zero or nonzero;
- projected physical C3 flow;
- physical matching;
- asymptotic-safety correctness or failure;
- programme disposition or `chi_ABC`.

Retain:

`TOPOLOGY_DRIFT_LOCALIZATION != PHYSICAL_TOPOLOGY_DOMINANCE`.

`Q7C_DESCRIPTIVE_RESULT != Q8_CONVERGENCE_PASS`.

`FINITE_N_NUMERICAL_DRIFT != CONTINUUM_PHYSICS`.
