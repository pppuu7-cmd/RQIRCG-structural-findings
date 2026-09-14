# RQIRCGSF current authoritative front

Updated: 2026-09-15, after SF032.

## Repository role

`pppuu7-cmd/RQIRCG-structural-findings` remains an independent `PROSPECTIVE NEW-PRINCIPLE / SUCCESSOR SEARCH`.

It is not an in-place repair of historical RCG-002 and does not inherit programme-disposition authority from parent RQIRCG.

Parent `pppuu7-cmd/RQIR-Candidate-Gravity` remains blocked on `EXPLICIT_PROGRAMME_DISPOSITION_AUTHORITY_REQUIRED`.

RQIRCGSF results remain successor authority until separately imported/promoted.

## Retained theory authorities

SF021: `RHPI_SELECTED_AS_CLASSICAL_GRAVITATIONAL_LAW_PRINCIPLE_SCOPED`.

SF025: `POST_RHPI_QUANTUM_COMPOSITION_DOES_NOT_FIX_FINITE_ON_SHELL_MATCHING_SCOPED`.

Retain `QUANTUM_STATE_MEASURE_SELECTION != QUANTUM_LAW_ON_SHELL_MATCHING_SELECTION`.

SF027: `QCA_PERTURBATIVE_RANK_ZERO_EXACT_MAP_BLOCKED_SCOPED` and `ANOMALY_FREEDOM_IS_CONSISTENCY_NOT_PHYSICAL_MATCHING_SELECTION_SCOPED`.

Theory-track blocker remains:

`GENUINELY_NEW_MICROSCOPIC_MATCHING_PRINCIPLE_WITH_EXPLICIT_PHYSICAL_MAP_REQUIRED`.

## Operational object authority

SF028 remains terminal-invalid:

`INVALID_FROZEN_PROTOCOL_1D_POINT_GAUSSIAN_GRAVITATIONAL_OBJECT_SCOPED`.

SF028B remains the boundary-complete physical-object authority:

`PASS_BOUNDARY_COMPLETE_KNOWN_PHYSICS_COHERENCE_BASELINE_SCOPED`.

Physical chain:

`NORMALIZED 3-QUBIT + 4-BODY 3D MOTIONAL STATE -> COM-CLOSED U_PREP -> FULL FREE ALL-BODY EVOLUTION -> U_PREP^dagger RECOMBINATION -> TRACE MOTION -> QUBIT TOMOGRAPHY`.

Connected readout:

`C3=Log K_111-Log K_110-Log K_101-Log K_011+Log K_100+Log K_010+Log K_001`,

`Theta3=Im C3`, `Gamma3=-Re C3`.

Retain:

`OPEN_ACTION != MEASURED_REDUCED_COHERENCE`.

`NONZERO_CONNECTED_SIGNAL != NEW_THREE_BODY_GRAVITATIONAL_VERTEX`.

## SF029 robustness authority

Terminal `33660feffa3cf9c3ad1dc6d3cd75c73fea7f5887`.

`ROBUST_KNOWN_PHYSICS_COHERENCE_BASELINE_HIERARCHY_SCOPED`.

Distinct finite-R/time/packet-width scalings and crossover surfaces are now explicit. Large-R diagnostics agree with inherited analytic hierarchy: Newtonian apparatus and feedback apparatus corrections approximately `R^-4`; 1PN apparatus correction approximately `R^-2`. Full frozen `tau<=0.2` family remains inside preregistered short-time controls.

## SF030 identifiability authority

Terminal `6a7d5e9455441a1182c260913da79ed5c4f3abd9`.

`KNOWN_PHYSICS_COHERENCE_COMPONENTS_STRUCTURALLY_IDENTIFIABLE_SCOPED`.

Full normalized 9-row joint `R,T` design has rank 3 and `kappa=5.5659`.

Each fixed-R design has rank 2: time alone cannot separate Newtonian apparatus and 1PN because both are linear in `tau`.

Each fixed-tau R-only design is rank 3 but poorly conditioned (`kappa~867.74`). Joint R+T leverage is essential.

Retain `IDENTIFIABILITY != ESTIMABILITY` and `IDENTIFIABILITY != DYNAMICS`.

## SF031 noise-aware estimability authority

Preregistration `f825f57e4a57b47effed68e34d2ab747a4881d15`.
Terminal `ac0ec512a109c51ae7fbee2f9006548d05fac5bc`.

`PN_CALIBRATION_REMAINS_ESTIMABLE_UNDER_FROZEN_COMMON_MODE_NUISANCES_SCOPED`.

`COMMON_MODE_NUISANCE_STRONGLY_INFLATES_PN_PRECISION_SCOPED`.

`TAU_LINEAR_COMMON_MODE_NEAR_DEGENERACY_DOMINATES_PN_PRECISION_SCOPED`.

All frozen nuisance models remain full mathematical rank after the pre-terminal numerical-rank firewall correction. The generic R-independent `tau`-linear nuisance raises normalized condition number to `~1008` and PN variance by `~2.1341e4`; with both offset and tau-linear nuisance `kappa~1113` and the same variance penalty.

Required dimensionless SNR1 phase-noise ceiling under both nuisances is

`sigma_y <= 2.11469516e-6 epsilon_PN`,

relative to an unspecified common phase scale `Phi0`.

Retain:

`STRUCTURAL_IDENTIFIABILITY != ESTIMABILITY != FEASIBILITY`.

## Latest gate — SF032 matched null-control calibration

Prospective preregistration:

`66e7b301200ca7b450f0bba38b4edce872166762`.

Script:

`bc6b7c4c723c1fb3334679180d0793b55c56763b`.

Canonical raw:

`bf0b266f54a1f19153d1b19a5dcbba09e8278e66`.

Terminal:

`e8dc5ca051e5f5c8669d6a0a1fe99e6c93b1ff4e`.

Ledger:

`3eadfdbedfa257b280e21c205db98ae1d8d7dc1b`.

Primary classification:

`MATCHED_NULL_CONTROL_BREAKS_COMMON_MODE_PN_NEAR_DEGENERACY_SCOPED`.

Mandatory qualification:

`NULL_CONTROL_CALIBRATION_BLOCKED_BY_UNVALIDATED_SHARED_NUISANCE_MAP`.

Secondary:

`SHARED_TAU_LINEAR_CONTROL_CHANNEL_PROVIDES_DOMINANT_CALIBRATION_INFORMATION_SCOPED`.

### Frozen control

One matched delete-A connected-null row is added for every science `(R,tau)` row. The inherited exact connected finite-difference theorem makes the known gravity columns exactly zero in these controls.

### Calibration result

Science-only SF031 common-mode model:

`PN VIF ~ 2.1341e4`, `kappa~1113`.

Matched null control with shared offset and shared tau-linear nuisance:

`PN VIF=1.658`, `kappa=9.948`.

PN variance improves by `~1.2870e4` relative to the science-only common-mode model.

Sharing only the offset gives essentially no improvement.

Sharing only the tau-linear nuisance gives PN VIF `12.31` and variance improvement `~1.7339e3`.

No-sharing negative control gives no improvement to numerical precision.

Thus the SF031 bottleneck is not irreducible white noise: it is calibratable if the dominant tau-linear nuisance is genuinely shared between science and null-control configurations.

### Physical promotion blocker

Current protocol authority does **not** yet derive that a laboratory/control nuisance coefficient is unchanged when the A branch displacement is disabled.

Retain:

`CONTROL_CALIBRATION != PHYSICAL_TRANSFERABILITY`.

The algebraic calibration PASS is conditional on the shared-nuisance map.

## Highest-information next operational gate

**`SF033_SCIENCE_NULL_CONTROL_NUISANCE_TRANSFERABILITY_PREOUTCOME_GATE`.**

Prospectively audit the minimal science/control implementation map. The gate must identify whether any nuisance sharing is guaranteed by the current abstract protocol versus requiring new pulse/readout/hardware physics.

If no explicit transfer map is already supplied by current authority, terminalize as

`BLOCKED_MISSING_CONTROL_TRANSFER_MODEL`

rather than assuming common mode.

Do not invent a pulse sequence, detector, electronics model or material response merely to rescue SF032.

## Theory track remains separate

`GENUINELY_NEW_MICROSCOPIC_MATCHING_PRINCIPLE_WITH_EXPLICIT_PHYSICAL_MAP_REQUIRED`.

Operational calibration cannot select SF025/SF027 quantum-law matching data.

## Claim locks

- no open action equals measured `Theta3`;
- no raw connected signal equals new three-body vertex;
- no apparatus/feedback baseline called new physics;
- no full rank or finite CRLB promoted to detector feasibility;
- no null-control calibration promoted to physical transferability without a map;
- no identifiability/estimability promoted to dynamics;
- no state/preparation freedom relabelled as quantum-law matching freedom;
- no new quantum principle selected;
- no matching coefficient selected;
- no quantum `chi_ABC` computed;
- no exact all-time, exact extended-body, or laboratory-feasibility claim;
- no historical RCG-002 authority changed;
- no parent programme disposition selected;
- no `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, or theory-establishment claim.
