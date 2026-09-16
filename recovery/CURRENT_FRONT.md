# RQIRCGSF current authoritative front

Updated: 2026-09-16 after completed Q6 radial-min2 piecewise baseline, Q6P merge-only recovery, and Q7A full-tensor regularity application.

## Current programme verdict

`MISSING_OBJECT_OR_CONTROL_BLOCKER_SCOPED`.

`SF055_TERMINAL_PASS=FALSE`.

The programme remains stopped before substantive C3 flow.

The active numerical blocker is now localized to derivative resolution/regularity at the smallest frozen momentum `p=1/32`; it is no longer missing shifted-support geometry, Q5 one-node radial allocation, y-shard execution, or merge provenance.

## Parent separation

Successor repository `pppuu7-cmd/RQIRCG-structural-findings` remains independent from historical `pppuu7-cmd/RQIR-Candidate-Gravity`.

Parent remains parked on

`WAIT_FOR_EXPLICIT_PROGRAMME_DISPOSITION_DECLARATION`.

No D1/D2/D3 disposition is selected. `chi_ABC` remains unauthorized/not computed. No successor result automatically becomes historical RCG-002 authority.

## Retained theory authority

Retain all terminal SF001-SF054 results, especially:

- SF021 `RHPI_SELECTED_AS_CLASSICAL_GRAVITATIONAL_LAW_PRINCIPLE_SCOPED`;
- SF025 `POST_RHPI_QUANTUM_COMPOSITION_DOES_NOT_FIX_FINITE_ON_SHELL_MATCHING_SCOPED`;
- SF043 `ASYMPTOTIC_SAFETY_PROVIDES_NONZERO_TRUNCATION_LEVEL_MATCHING_SELECTION_SCOPED`;
- `R_ASGS_TRUNCATION=1`;
- `R_ASGS_PHYSICAL=UNDEFINED_MAP_NOT_CLOSED`;
- SF046 `b=s G_C3/(32 pi G_N)` only as coordinate conversion, no physical b selected;
- SF049 physical on-shell C3 helicity projector scoped;
- SF052 complete six-derivative TT quotient only at the frozen D=4 Euclidean TT symmetric point;
- SF053 published executed fluctuation truncations do not reconstruct the target C3/p6 flow object;
- SF054 minimal C3 flow requires correlated 3/4/5-point insertions.

Retain:

`PHYSICAL_HELICITY_PROJECTOR != PROJECTED_FRG_FLOW`.

`BACKGROUND_COUPLING != PHYSICAL_FLUCTUATION_COUPLING`.

`TRUNCATION_SELECTOR != PHYSICAL_SELECTOR`.

## SF055 fixed implementation authority

Parent preregistration: `9d998d984566aa5bf290312a6a062fd632c85561`.

Lane B remains `PASS_C3_COMMON_ORIGIN_VERTEX_GENERATOR_SCOPED`.

Lane C remains `PASS_IMPLEMENTED_THREE_POINT_FLOW_C3_INSERTION_MANIFEST_SCOPED`.

Three-point source topology coefficients remain

`T5=-1/2`, `B43=+3`, `T333grav=-3`, `T333ghost=+6`.

Retain validated source-Fourier EH/ghost seed engine, six-dimensional Landau-transverse graviton internal space, FP ghosts, canonical routing, fixed-q contraction assembly, TT projector normalisation, Q1 exact TT-projector regrouping and Q2 source symmetrisation.

Frozen normalisations:

`N_g^(-1)=0.00052874519051635`,

`N_lambda^(-1)=0.0026385724906858796`.

Loop measure `d^4q/(2pi)^4`; source symmetrisation `Sym_3=(1/6)sum_S3`; single-scale line `G dotR G`; no fitted rescaling.

## Historical original baseline retained

Original terminal classification remains

`BLOCKED_LANE_A_BASELINE_QUADRATURE_NOT_CONVERGED_SCOPED`.

Its N24 values were target-close but N16->N24 convergence failed. Q6 is a prospectively authorized numerical successor and does not rewrite this history.

## Q4 and Q5 retained

Q4:

`PASS_SHIFTED_REGULATOR_INTERSECTION_GEOMETRY_AND_PIECEWISE_EQUIVALENCE_SCOPED`.

Canonical shifted support boundaries:

`r^2+2 p c r+p^2=1`,

`r_b=-p c+sqrt(1-p^2+p^2 c^2)`,

crossing iff `c>-p/2`, topology-change surface `y_*=1-p^2/4`.

Q5:

`BLOCKED_LANE_A_PIECEWISE_IMPLEMENTATION_CONTROL_SCOPED`.

Its one-node radial allocation failed the target-blind quadratic smooth control. Q6 prospectively repaired only that implementation defect by requiring minimum two GL nodes per nonempty radial piece.

## Q6 radial-min2 piecewise baseline — TERMINAL BLOCKED

Preregistration:

`54fe1870177ce8d9155bd0731203197761bed5dc`.

Terminal result:

`results/SF055A3Q6_RADIAL_MIN2_PIECEWISE_BASELINE_TERMINAL.md`, commit `7fb39877f2415c6367c83af6c9ec0b183509178e`.

Workflow run `35040058701`, head `4b6c6902376e88f49c291813ecc4250edc8f32ee`.

Aggregate artifact `10429809775`, digest

`sha256:cfbd1546ec1b0fdc08be2dfce15d6d7660bf3e83ae38f51ea769fe303c9e1485`.

Preflight artifact `10424957402`, digest

`sha256:89fba3d99d76dd86e7919abdf72439da67027bac209aa731333ff424e9e634fc`.

Classification:

`BLOCKED_LANE_A_Q6_PIECEWISE_BASELINE_NOT_CONVERGED_SCOPED`.

All required implementation controls pass, including source/JIT equivalence, fixed-q topology equivalence, p=0 historical-rule equivalence, node budgets, smooth reduced-measure controls, Q4 thin-shell control and frozen negative controls.

`C3_enabled=false`.

At N=16:

- `beta_g=-3.4763144983440384`;
- `beta_lambda3=-3.015202432913556`;
- `beta_mu=0.3224650623712873`.

At N=24:

- `beta_g=-7.590697586295343`;
- `beta_lambda3=-4.455236523767682`;
- `beta_mu=0.3224650623712883`.

Frozen N16->N24 relative changes:

- beta_g `0.5420296410411126` = 54.2029641%;
- beta_lambda3 `0.3232228150339199` = 32.3222815%;
- beta_mu `3.098632499331524e-15`.

Frozen allowed relative change is 0.2%.

All separate N24 1% target checks pass:

- beta_g target error 0.810645%;
- beta_lambda3 target error 0.481827%;
- beta_mu target error negligible.

Therefore `target_pass=true` cannot override `convergence_pass=false`.

Retain:

`PIECEWISE_SUPPORT_CLOSURE != DERIVATIVE_CONVERGENCE`.

`TARGET_PROXIMITY != CONVERGENCE`.

## Q6P execution and merge provenance — TERMINAL PASS

Q6P deterministic y-shard equivalence remains

`PASS_Q6P_Y_SHARD_EXECUTION_EQUIVALENCE_SCOPED`.

The first fatal-point workflow graph failure was infrastructure only. All eight repaired shard jobs later completed successfully.

Their original merge jobs failed only because NumPy was not installed in the merge environment; no shard value was read before that failure.

Merge-only recovery was prospectively frozen at

`8dab2f6561d4bae1e3b91eba9cd31152a6795082`.

Recovery workflow run `35132698327` completed successfully.

Artifact `10461044772`, digest

`sha256:bc2a95fc125e3d0b86c85139c4224c2ceb45aac2034a14b66d30654585477416`.

Terminal classification:

`PASS_Q6P_MERGE_ONLY_RECOVERY_SCOPED`.

Recovered fatal points:

- p=1/16,N=24: `Flow_G=0.0005465706425780866`;
- p=1/32,N=16: `Flow_G=0.0005545825645617645`;
- p=1/32,N=24: `Flow_G=0.0005537769479482955`.

All have exact shard/y coverage, exact node budget, and `C3_enabled=false`.

They agree with independent monolithic Q6 values at about `1.5e-18` to `2.3e-18` absolute.

Thus monolithic-vs-sharded execution is not the source of the Q6 derivative nonconvergence.

## Q7 frozen Richardson regularity authority retained

Q7 terminal classification:

`PASS_Q7_RICHARDSON_REGULARITY_DIAGNOSTIC_CONSTRUCTED_SCOPED`.

For `h=1/32`, with `D_r=[F(rh)-F(0)]/(rh)^2`, r={1,2,4}:

`C2_234=(8D_1-6D_2+D_4)/3`,

`C3_234=[-2D_1+(5/2)D_2-(1/2)D_4]/h`,

and exact identity

`R_h-C2_234=(2h/3)C3_234`,

where `R_h=(4D_1-D_2)/3`.

Q7 is a diagnostic, not an authorized replacement estimator.

## Q7A application to complete Q6 ladder — TERMINAL INCONCLUSIVE

Terminal result:

`results/SF055A3Q7A_FULL_TENSOR_REGULARITY_APPLICATION_TERMINAL.md`, commit `2abcc0740061951c71b08cf8a772e97527b44ea9`.

Classification:

`INCONCLUSIVE_Q7_FULL_TENSOR_CUBIC_DIRECTION_SCOPED`.

`C3_234` sequence:

- N8 `+0.11047520333196903`;
- N12 `-0.15822591014134924`;
- N16 `-0.04860017786014337`;
- N24 `+0.0015123122084195195`.

The sequence changes sign and magnitude strongly. No stable nonzero continuum cubic/nonanalytic direction is established.

The cubic-sensitive discrepancy `|R_h-C2_234|/|R_h|` falls from about 69.9% at N16 to about 1.24% at N24.

### Exact derivative-instability localization

For N16->N24:

- `Delta D_1` at p=1/32: `-0.0008249207987136575`;
- `Delta D_2` at p=1/16: `-0.000036492790310538314`;
- `Delta D_4` at p=1/8: `-0.000014811385983241887`.

Historical Richardson uses only D1,D2:

`Delta R_h=(4 Delta D_1-Delta D_2)/3`.

Contributions:

- p=1/32: `-0.0010998943982848768`;
- p=1/16: `+0.000012164263436846104`;
- total: `-0.0010877301348480308`.

Thus p=1/32 accounts for about 101.118% of the signed change, with p=1/16 canceling about 1.118%. In absolute-contribution terms p=1/32 carries about **98.9061%** of the N16->N24 Richardson instability.

Retain:

`UNSTABLE_C3_DIAGNOSTIC != NONZERO_CONTINUUM_ABS_P3`.

`P32_ERROR_LOCALIZATION != PERMISSION_TO_DROP_P32`.

## Exact next admissible gate

The highest-information next successor should target only the derivative-sensitive p=1/32 object with stronger prospectively frozen resolution/error control.

Do not blindly recompute the entire Q6 matrix: p=0, p=1/16, p=1/8 and beta_mu are not the dominant source of the current Richardson instability.

A new gate must be frozen before any new higher-resolution p=1/32 values are inspected. It may vary numerical resolution prospectively, but it must not rewrite Q6, change the historical Richardson definition post hoc, relax the 0.2% convergence threshold, fit a normalization, or inspect C3 physics.

Useful target of the next gate:

`P32_HIGH_RESOLUTION_DERIVATIVE_CONVERGENCE_AND_ERROR_BUDGET`.

Even if p=1/32 numerical convergence is achieved, derivative-truncation/regularity remains a separate question unless independently bounded.

## Operational front retained

SF028B remains boundary-complete coherence authority; SF029-SF042 retain the known-physics/control chain.

Operational blocker remains

`DEVICE_LEVEL_NONLINEAR_CROSSTALK_MAGNITUDE_AND_STABILITY_DATA_REQUIRED`.

Retain:

`OPEN_ACTION != MEASURED_REDUCED_COHERENCE`.

`NONZERO_CONNECTED_SIGNAL != NEW_THREE_BODY_GRAVITATIONAL_VERTEX`.

`STRUCTURAL_CONTROL_CLOSURE != DEVICE_VALIDATION`.

## Claim locks

Without separate authority:

- no physical SF025 b selected;
- no truncation parameter promoted to physical matching;
- no background/fluctuation equality assumed;
- no frozen-point quotient promoted to arbitrary kinematics;
- no projected dynamical C3 beta claimed;
- no Q4/Q5/Q6/Q6P/Q7/Q7A sub-result promoted to SF055 PASS;
- no Euclidean off-shell coefficient declared physical without continuation;
- no quantum chi_ABC;
- no historical RCG-002 authority change;
- no asymptotic-safety correctness or failure claim;
- no `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, `THEORY_ESTABLISHED`, or unique quantum-gravity selector claim.
