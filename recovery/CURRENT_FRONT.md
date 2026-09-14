# RQIRCGSF current authoritative front

Updated: 2026-09-15, after SF030.

## Repository role

`pppuu7-cmd/RQIRCG-structural-findings` remains an independent

`PROSPECTIVE NEW-PRINCIPLE / SUCCESSOR SEARCH`.

It is not an in-place repair of historical RCG-002 and does not inherit programme-disposition authority from parent RQIRCG.

Parent `pppuu7-cmd/RQIR-Candidate-Gravity` remains blocked on

`EXPLICIT_PROGRAMME_DISPOSITION_AUTHORITY_REQUIRED`.

RQIRCGSF science may continue independently; its results remain successor authority until separately imported/promoted.

## Retained scientific authorities

### SF021 classical law

`RHPI_SELECTED_AS_CLASSICAL_GRAVITATIONAL_LAW_PRINCIPLE_SCOPED`.

Scoped sufficient classical reconstruction only; not complete quantum theory and not historical RCG-002 authority.

### SF025 quantum matching

`POST_RHPI_QUANTUM_COMPOSITION_DOES_NOT_FIX_FINITE_ON_SHELL_MATCHING_SCOPED`.

Retain:

`QUANTUM_STATE_MEASURE_SELECTION != QUANTUM_LAW_ON_SHELL_MATCHING_SELECTION`.

### SF026 self-consistent baseline

`PAIRWISE_NULL_NOT_STABLE_UNDER_SELF_CONSISTENT_HISTORY_PULLBACK_SCOPED`.

Factorized-history pairwise-null remains exact in its scope. SF026 open-action coefficients remain diagnostics only.

### SF027 quantum-constraint selector

`QCA_PERTURBATIVE_RANK_ZERO_EXACT_MAP_BLOCKED_SCOPED`.

`ANOMALY_FREEDOM_IS_CONSISTENCY_NOT_PHYSICAL_MATCHING_SELECTION_SCOPED`.

Theory-track blocker remains:

`GENUINELY_NEW_MICROSCOPIC_MATCHING_PRINCIPLE_WITH_EXPLICIT_PHYSICAL_MAP_REQUIRED`.

## SF028 / SF028B object history

SF028 remains terminal-invalid:

`INVALID_FROZEN_PROTOCOL_1D_POINT_GAUSSIAN_GRAVITATIONAL_OBJECT_SCOPED`.

No SF028 coefficient is authoritative.

SF028B remains the boundary-complete operational authority:

`PASS_BOUNDARY_COMPLETE_KNOWN_PHYSICS_COHERENCE_BASELINE_SCOPED`.

Physical object:

`NORMALIZED 3-QUBIT + 4-BODY 3D MOTIONAL STATE`
`-> COM-CLOSED U_PREP`
`-> FULL FREE ALL-BODY EVOLUTION`
`-> U_PREP^dagger RECOMBINATION`
`-> TRACE MOTION`
`-> QUBIT TOMOGRAPHY`.

Connected readout:

`C3=Log K_111-Log K_110-Log K_101-Log K_011+Log K_100+Log K_010+Log K_001`,

`Theta3=Im C3`, `Gamma3=-Re C3`.

Retain:

`OPEN_ACTION != MEASURED_REDUCED_COHERENCE`.

Known-physics decomposition:

`RAW CONNECTED COHERENCE`
`= FINITE-R NEWTONIAN APPARATUS/COM`
`+ SELF-CONSISTENT NEWTONIAN FORCE/COHERENCE PULLBACK`
`+ ORDINARY EIH 1PN NONLINEAR GRAVITY`
`+ HIGHER ORDERS / NUISANCES`.

Retain:

`NONZERO_CONNECTED_SIGNAL != NEW_THREE_BODY_GRAVITATIONAL_VERTEX`.

## SF029 robustness terminal

Preregistration: `ee392560debda35c0fbe51ca65112d1939fb3cfb`.

Terminal: `33660feffa3cf9c3ad1dc6d3cd75c73fea7f5887`.

Classification:

`ROBUST_KNOWN_PHYSICS_COHERENCE_BASELINE_HIERARCHY_SCOPED`.

Key structural result:

`DISTINCT_NUISANCE_SCALINGS_CREATE_BASELINE_CROSSOVER_SURFACES_SCOPED`.

On the frozen R grid, no sign crossings occur. Delete-one-label controls are exact zero. The complete frozen `tau<=0.2` range remains within preregistered short-time control bounds.

Large-R hierarchy is numerically consistent with the inherited analytic multipole structure:

`Newtonian apparatus O(T) ~ R^-4`,

`Newtonian feedback apparatus correction ~ R^-4`,

`1PN apparatus correction ~ R^-2`,

while Newtonian feedback and 1PN source terms each approach nonzero source-only limits.

The finite-R/raw-baseline crossover surfaces are now explicit functions of `epsilon_PN`, R and tau.

## Latest gate — SF030 known-physics component identifiability

Prospective preregistration:

`0fa7251021afc5c230578c5c933b1e11d78c3a3d`.

Corrected pre-terminal script authority:

`d197fbbbe6560fb3cf919ce04ad8533afaae786e`.

Canonical raw:

`f60946d712192313a2fccd18d7642b57ed9e0cee`.

Terminal:

`6a7d5e9455441a1182c260913da79ed5c4f3abd9`.

Ledger:

`96d488adc6ba7f92d775b0315dc6041e5d922b8a`.

Primary classification:

`KNOWN_PHYSICS_COHERENCE_COMPONENTS_STRUCTURALLY_IDENTIFIABLE_SCOPED`.

Secondary:

`R_VARIATION_REQUIRED_TO_BREAK_T_LINEAR_APPARATUS_VS_1PN_DEGENERACY_SCOPED`.

`JOINT_R_AND_T_DESIGN_STRONGLY_IMPROVES_CONDITIONING_SCOPED`.

`STRUCTURAL_IDENTIFIABILITY_DOES_NOT_REMOVE_SMALL_EPSILON_PN_DYNAMIC_RANGE_SCOPED`.

### Frozen design

9 rows:

`R/ell={60,160,400}` x `tau={0.05,0.1,0.2}`.

Known basis only:

`x_app=-Delta3 V_N(R) tau`,

`x_fb=[Delta3 A_N(R)/12] tau^3`,

`x_1PN=-Delta3 V_static^1PN(R) tau`.

No successor/quantum basis column was allowed.

### Structural result

Column-normalized full design:

`rank=3`,

singular values `(1.53862,0.74581,0.27644)`,

`kappa_shape=5.5659`.

All leave-one-R subsets remain rank 3 with `kappa<5.91`.

All leave-one-tau subsets remain rank 3 with `kappa<9.56`.

### Decisive ablations

Each fixed-R, multi-tau design has `rank=2` exactly/numerically: the Newtonian apparatus and 1PN columns are both proportional to `tau`, so time variation alone cannot separate them.

Each fixed-tau, multi-R design has formal rank 3 but poor `kappa~867.74`.

Thus R variation is required to break the exact two-linear-T degeneracy, while T variation is required for useful conditioning of the feedback/1PN separation.

### Identifiability versus estimability

The unnormalized physical matrix remains rank 3 but becomes badly conditioned when the 1PN scale is very small. Frozen diagnostics give

`kappa_phys~27.8` at `epsilon_PN=1e-4`,

`~2.50e3` at `1e-6`,

`~2.50e5` at `1e-8`.

Therefore retain strictly:

`IDENTIFIABILITY != ESTIMABILITY`.

And:

`IDENTIFIABILITY != DYNAMICS`.

No detector/noise precision claim is yet authorized.

## Highest-information next operational gate

**`SF031_NOISE_AWARE_KNOWN_BASELINE_ESTIMABILITY_PREOUTCOME_GATE`.**

Prospectively freeze one minimal statistical model before computing precision requirements.

Recommended structure:

1. same 9 SF030 `Theta3` rows;
2. independent homoscedastic phase-noise control;
3. one additive common-offset nuisance;
4. one global `tau`-linear common-mode nuisance adversary;
5. Fisher/Cramer-Rao precision requirement for the known 1PN calibration amplitude as a function of `epsilon_PN` and phase-noise scale;
6. explicit nuisance-rank and variance-inflation audit.

The gate may quantify required precision but may not call that precision experimentally achievable without a separate detector/noise model.

No successor residual column is authorized.

## Theory track remains separate

`GENUINELY_NEW_MICROSCOPIC_MATCHING_PRINCIPLE_WITH_EXPLICIT_PHYSICAL_MAP_REQUIRED`.

Do not use operational rank/conditioning to choose the SF025/SF027 quantum-law matching datum.

## Claim locks

- no open action equals measured `Theta3`;
- no raw connected signal equals new three-body vertex;
- no apparatus/feedback baseline called new physics;
- no full rank promoted to detector feasibility;
- no identifiability promoted to dynamics;
- no state/preparation freedom relabelled as quantum-law matching freedom;
- no new quantum principle selected;
- no matching coefficient selected;
- no quantum `chi_ABC` computed;
- no exact all-time, exact extended-body, or laboratory-feasibility claim;
- no historical RCG-002 authority changed;
- no parent programme disposition selected;
- no `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, or theory-establishment claim.
