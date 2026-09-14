# RQIRCGSF current authoritative front

Updated: 2026-09-15, after SF031.

## Repository role

`pppuu7-cmd/RQIRCG-structural-findings` remains an independent `PROSPECTIVE NEW-PRINCIPLE / SUCCESSOR SEARCH`.

It is not an in-place repair of historical RCG-002 and does not inherit programme-disposition authority from parent RQIRCG.

Parent `pppuu7-cmd/RQIR-Candidate-Gravity` remains blocked on `EXPLICIT_PROGRAMME_DISPOSITION_AUTHORITY_REQUIRED`.

RQIRCGSF science may continue independently; its results remain successor authority until separately imported/promoted.

## Retained theory authorities

SF021: `RHPI_SELECTED_AS_CLASSICAL_GRAVITATIONAL_LAW_PRINCIPLE_SCOPED`.

SF025: `POST_RHPI_QUANTUM_COMPOSITION_DOES_NOT_FIX_FINITE_ON_SHELL_MATCHING_SCOPED`.

Retain `QUANTUM_STATE_MEASURE_SELECTION != QUANTUM_LAW_ON_SHELL_MATCHING_SELECTION`.

SF027: `QCA_PERTURBATIVE_RANK_ZERO_EXACT_MAP_BLOCKED_SCOPED` and `ANOMALY_FREEDOM_IS_CONSISTENCY_NOT_PHYSICAL_MATCHING_SELECTION_SCOPED`.

Theory-track blocker remains:

`GENUINELY_NEW_MICROSCOPIC_MATCHING_PRINCIPLE_WITH_EXPLICIT_PHYSICAL_MAP_REQUIRED`.

## Retained operational object

SF028 is terminal-invalid:

`INVALID_FROZEN_PROTOCOL_1D_POINT_GAUSSIAN_GRAVITATIONAL_OBJECT_SCOPED`.

No SF028 coefficient is authoritative.

SF028B remains the boundary-complete physical-object authority:

`PASS_BOUNDARY_COMPLETE_KNOWN_PHYSICS_COHERENCE_BASELINE_SCOPED`.

Physical chain:

`NORMALIZED 3-QUBIT + 4-BODY 3D MOTIONAL STATE`
`-> COM-CLOSED U_PREP`
`-> FULL FREE ALL-BODY EVOLUTION`
`-> U_PREP^dagger RECOMBINATION`
`-> TRACE MOTION`
`-> QUBIT TOMOGRAPHY`.

Connected readout:

`C3=Log K_111-Log K_110-Log K_101-Log K_011+Log K_100+Log K_010+Log K_001`,

`Theta3=Im C3`, `Gamma3=-Re C3`.

Retain `OPEN_ACTION != MEASURED_REDUCED_COHERENCE`.

Known-physics decomposition remains:

`RAW CONNECTED COHERENCE = FINITE-R NEWTONIAN APPARATUS/COM + SELF-CONSISTENT NEWTONIAN FORCE/COHERENCE PULLBACK + ORDINARY EIH 1PN NONLINEAR GRAVITY + HIGHER ORDERS/NUISANCES`.

Retain `NONZERO_CONNECTED_SIGNAL != NEW_THREE_BODY_GRAVITATIONAL_VERTEX`.

## SF029 robustness terminal

Preregistration `ee392560debda35c0fbe51ca65112d1939fb3cfb`.
Terminal `33660feffa3cf9c3ad1dc6d3cd75c73fea7f5887`.

Classification:

`ROBUST_KNOWN_PHYSICS_COHERENCE_BASELINE_HIERARCHY_SCOPED`.

Distinct nuisance scalings and crossover surfaces were established on the frozen grid. Large-R diagnostics agree with inherited analytic scaling: Newtonian apparatus and Newtonian-feedback apparatus corrections approximately `R^-4`; 1PN apparatus correction approximately `R^-2`. All frozen `tau<=0.2` cells pass the prospectively fixed short-time controls.

## SF030 identifiability terminal

Preregistration `0fa7251021afc5c230578c5c933b1e11d78c3a3d`.
Terminal `6a7d5e9455441a1182c260913da79ed5c4f3abd9`.

Classification:

`KNOWN_PHYSICS_COHERENCE_COMPONENTS_STRUCTURALLY_IDENTIFIABLE_SCOPED`.

Full normalized 9-row design `R={60,160,400} x tau={0.05,0.1,0.2}` has rank 3, singular values `(1.53862,0.74581,0.27644)`, and `kappa_shape=5.5659`.

Every single-R multi-tau control has rank 2, proving time variation alone cannot split the two `tau`-linear apparatus and 1PN terms. Single-tau R-only designs are rank 3 but ill-conditioned (`kappa~867.74`). Joint R+T variation is the productive calibration lever.

Retain `IDENTIFIABILITY != ESTIMABILITY` and `IDENTIFIABILITY != DYNAMICS`.

## Latest gate — SF031 noise-aware estimability

Prospective preregistration:

`f825f57e4a57b47effed68e34d2ab747a4881d15`.

Stable script:

`aa8313baf931b4b390ac81c4853647d5cca95c5a`.

Canonical raw:

`18342c91acfbc89e235c3994e0b19859cbc6a2da`.

Terminal:

`ac0ec512a109c51ae7fbee2f9006548d05fac5bc`.

Ledger:

`43a0e567f24a06d624100a0989cef388fc29f6f2`.

Primary classification:

`PN_CALIBRATION_REMAINS_ESTIMABLE_UNDER_FROZEN_COMMON_MODE_NUISANCES_SCOPED`.

Secondary:

`COMMON_MODE_NUISANCE_STRONGLY_INFLATES_PN_PRECISION_SCOPED`.

Localization:

`TAU_LINEAR_COMMON_MODE_NEAR_DEGENERACY_DOMINATES_PN_PRECISION_SCOPED`.

### Numerical-rank firewall

A preliminary unnormalized-SVD rank check was rejected before terminalization because making a nonzero PN column small via nonzero `epsilon_PN` cannot change mathematical rank. Stable authority uses column-normalized SVD for rank and normalized-Gram rescaling for CRLB.

No scientific contract changed.

### Frozen nuisance models

A: iid homoscedastic phase noise.

B: A + additive constant offset.

C: A + global R-independent `tau`-linear common phase.

D: A + both nuisances.

All remain full column rank at `epsilon_PN={1e-2,1e-4,1e-6,1e-8}`.

Normalized condition numbers:

- A: `5.5659`;
- B: `20.2578`;
- C: `1007.6502`;
- D: `1113.4625`.

PN variance-inflation factors relative to A:

- B: `11.695`;
- C: `~2.1341e4`;
- D: `~2.1341e4`.

Thus the generic R-independent `tau`-linear nuisance is the dominant calibration bottleneck. The PN amplitude remains mathematically estimable because finite-R R-dependence breaks exact degeneracy, but only weakly.

### Precision scaling

Required dimensionless per-row phase-noise ceilings for nominal PN SNR 1 scale exactly linearly with `epsilon_PN`:

- A: `sigma_y <= 3.08928556e-4 epsilon_PN`;
- B: `sigma_y <= 9.03345143e-5 epsilon_PN`;
- C/D: `sigma_y <= 2.11469516e-6 epsilon_PN`.

For SNR 5 divide by five.

These are requirements relative to an unspecified common phase scale `Phi0`, not achieved laboratory sensitivities.

Retain:

`STRUCTURAL_IDENTIFIABILITY != ESTIMABILITY != FEASIBILITY`.

## Highest-information next operational gate

**`SF032_NULL_CONTROL_COMMON_MODE_CALIBRATION_PREOUTCOME_GATE`.**

Prospectively freeze matched delete-one-label connected-null controls using the same `tau` schedule/readout. Under an explicit shared-nuisance hypothesis, test whether the exactly zero known-physics connected control rows can directly calibrate the additive and `tau`-linear nuisance terms and reduce PN variance inflation.

Required safeguards:

- control science columns are exactly zero by the already-validated connected finite-difference deletion theorem;
- nuisance sharing between science and control rows must be a prospectively stated hypothesis and separately ablated;
- no gravity component may be subtracted from science rows by assumption;
- report full rank, condition number, PN VIF and phase-noise requirement;
- include a negative control where nuisance is not shared, which should provide no calibration benefit.

No successor residual column is authorized.

## Theory track remains separate

`GENUINELY_NEW_MICROSCOPIC_MATCHING_PRINCIPLE_WITH_EXPLICIT_PHYSICAL_MAP_REQUIRED`.

Operational calibration information may not choose SF025/SF027 quantum-law matching data.

## Claim locks

- no open action equals measured `Theta3`;
- no raw connected signal equals new three-body vertex;
- no apparatus/feedback baseline called new physics;
- no full rank or finite CRLB promoted to detector feasibility;
- no identifiability/estimability promoted to dynamics;
- no state/preparation freedom relabelled as quantum-law matching freedom;
- no new quantum principle selected;
- no matching coefficient selected;
- no quantum `chi_ABC` computed;
- no exact all-time, exact extended-body, or laboratory-feasibility claim;
- no historical RCG-002 authority changed;
- no parent programme disposition selected;
- no `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, or theory-establishment claim.
