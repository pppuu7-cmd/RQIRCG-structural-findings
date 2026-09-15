# RQIRCGSF current authoritative front

Updated: 2026-09-15, after SF055 Lane B/C terminal PASS and SF055A3 A3.1/A3.2 fixed-q baseline-calibration PASSes. SF055 overall remains non-terminal.

## Repository role / parent separation

`pppuu7-cmd/RQIRCG-structural-findings` remains an independent `PROSPECTIVE NEW-PRINCIPLE / SUCCESSOR SEARCH`.

Parent `pppuu7-cmd/RQIR-Candidate-Gravity` remains separately parked on `WAIT_FOR_EXPLICIT_PROGRAMME_DISPOSITION_DECLARATION`.

Successor results do not become historical RCG-002 authority without a separate prospective import/promotion gate.

## Retained established theory status

SF021: `RHPI_SELECTED_AS_CLASSICAL_GRAVITATIONAL_LAW_PRINCIPLE_SCOPED`.

SF025: `POST_RHPI_QUANTUM_COMPOSITION_DOES_NOT_FIX_FINITE_ON_SHELL_MATCHING_SCOPED`.

Retain:

`QUANTUM_STATE_MEASURE_SELECTION != QUANTUM_LAW_ON_SHELL_MATCHING_SELECTION`.

SF043: `ASYMPTOTIC_SAFETY_PROVIDES_NONZERO_TRUNCATION_LEVEL_MATCHING_SELECTION_SCOPED`, but

`R_ASGS_TRUNCATION=1`,

`R_ASGS_PHYSICAL=UNDEFINED_MAP_NOT_CLOSED`.

SF046 on-shell coordinate bridge remains

`b = s G_C3/(32 pi G_N)`

with one unresolved global sign convention; no physical `b` has been selected.

SF049: `PHYSICAL_ON_SHELL_C3_HELICITY_PROJECTOR_CONSTRUCTED_SCOPED`.

SF052: `PASS_COMPLETE_SIX_DERIVATIVE_TT_QUOTIENT_SCOPED` in the frozen D=4 Euclidean TT symmetric-point domain.

Complete nonzero basis:

`[C3,S3,SSC,SDeltaS]`.

Frozen essentialized tensor:

`T_C3_perp_6d = T_C3 + (84/155)T_S3 + (364/155)T_SSC + (49/155)T_SDeltaS`,

residual norm `243/9920 > 0`, with

`P_E_6d[C3]=1`,

`P_E_6d[S3]=P_E_6d[SSC]=P_E_6d[RDeltaR]=P_E_6d[SDeltaS]=0`.

Do not promote this frozen Euclidean quotient to arbitrary kinematics or Lorentzian physical matching.

SF053: `BLOCKED_TARGET_FLOW_OBJECT_NOT_RECONSTRUCTIBLE_SCOPED`; published executed fluctuation calculations did not retain the projector-ready orthogonal p6/C3 tensor information.

SF054: `MINIMAL_C3_FLOW_REQUIRES_CORRELATED_3_4_5_VERTEX_INSERTIONS_SCOPED`; a three-point-only C3 deformation is not covariantly closed.

## Active gate — SF055 projected fluctuation-FRG implementation contract

Preregistration:

`9d998d984566aa5bf290312a6a062fd632c85561`.

Status:

`ACTIVE / NON-TERMINAL`.

Frozen realization remains:

- D=4 flat Euclidean background;
- linear split;
- source-Fourier convention `partial_mu -> i p_mu` in the validated seed path;
- De-Donder/harmonic linear gauge in the Landau limit;
- full Landau-transverse internal graviton sector plus Faddeev-Popov ghosts;
- source optimized regulator `R_phi=Gamma^(2)|_{mu=0} r`, `x r(x)=(1-x) theta(1-x)`;
- symmetric external three-point kinematics;
- one common `g_C3^fluc=k^2 G_C3^fluc` generating correlated `Gamma_C3^(3,4,5)`;
- final target `B_C3=P_E_6d[[partial_t Gamma^(3)]_TT]` only after all calibration lanes terminalize.

No substantive C3 flow output has been inspected or authorized.

## SF055 Lane B — terminal PASS scoped

Classification:

`PASS_C3_COMMON_ORIGIN_VERTEX_GENERATOR_SCOPED`.

Result note:

`results/SF055_LANE_B_C3_COMMON_ORIGIN_VERTEX_GENERATOR_TERMINAL.md`.

Controls include:

- `Gamma_C3^(2)=0`;
- all 125 SF052 cubic TT components reproduce with the common `3! = 6` functional-derivative factor;
- complete Bose permutations n=3,4,5;
- one common C3 coupling with no independent n=3/4/5 coefficients.

Independent reproducibility retry: run `34995827603`, job `104471676663`, artifact `10407234167`, digest `sha256:7db9004088f78bb8513c84373a5c4688790e28749727af866ab56a7518048e9c`.

Retain:

`LANE_B_PASS != SF055_TERMINAL_PASS`.

## SF055 Lane C — terminal PASS scoped

Classification:

`PASS_IMPLEMENTED_THREE_POINT_FLOW_C3_INSERTION_MANIFEST_SCOPED`.

Result note:

`results/SF055_LANE_C_C3_INSERTION_MANIFEST_TERMINAL.md`.

Implemented source topology classes are frozen as:

- `T5_GRAV`: coefficient `-1/2`, n=5;
- `B43_GRAV`: coefficient `+3`, n=4/3;
- `T333_GRAV`: coefficient `-3`, n=3/3/3;
- `T333_GHOST`: coefficient `+6`, baseline ghost only.

First-order common-C3 insertion histogram is `{3:4,4:1,5:1}`, with no C3 ghost or two-point insertion.

Run `34995935520`, job `104472035930`, artifact `10407288690`, digest `sha256:879f6860559205acf526eb1cf65386b17eeb3914a7a278b05e9e7fe9beb28502`.

## SF055 Lane A — active source-Fourier baseline reproduction

### Seed authority

SF055A2 classification:

`PASS_SOURCE_FOURIER_EH_GHOST_BASELINE_SEED_ENGINE_SCOPED`.

The validated source path uses `partial_mu -> i p_mu`, reproduces the TT two-point source normalization `K_EH=1/(32 pi)`, supplies common EH n=3/4/5 vertices, FP two-point/ghost-h vertices, and source regulator/threshold controls.

Run `34997423208`, job `104477069061`, artifact `10407843711`, digest `sha256:21abcd4b7cbeffdbd8d7d6d71c697c7aebe883e0a3afc439dd554902ccb1085b`.

### SF055A3 prospective baseline-loop gate

Preregistration:

`prereg/SF055A3_SOURCE_FOURIER_BASELINE_LOOP_REPRODUCTION_PREOUTCOME.md`, freeze commit `e38e2fcc1a2da0c39be1d2cb28a7c8d5a3db276a`.

Frozen benchmark at k=1:

`g=1`, `mu_h=1/10`, `lambda_2=-1/20`, `lambda_3=-7/10`, `eta_h=eta_c=0`.

Frozen analytic Eq. (14) targets:

`beta_g = 2 - (274830865/9179907)/pi`,

`beta_lambda3 = 7/5 - (3364922887/183598140)/pi`,

`beta_mu = -1/5 + (6554/3993)/pi`.

Hard-coding/fitting these targets is forbidden.

### A3.1 internal propagator/regulator — PASS

Classification:

`PASS_A3_1_LANDAU_TRANSVERSE_INTERNAL_PROPAGATOR_CALIBRATION_SCOPED`.

Merged authority:

`5ec13709774f91d4073363e79e805862a1840c6d`.

For generic nonzero q, the source Landau-transverse internal space has `dim K(q)=6`: five TT directions plus one independent transverse non-TT direction. Source EH Hessian, full tensor regulator `R_h=H0 r`, graviton inverse, FP regulator and ghost inverse pass frozen controls.

Successful run `35000156977`, job `104486265741`, artifact `10409790029`, digest `sha256:09a4604d5eee8c1af801b958d58191a309e1a50f31555d0208efabc42461cb65`.

Retain:

`EXTERNAL_TT_PROJECTION != TT_ONLY_INTERNAL_PROPAGATION`.

### A3.2 Figure-2 routing — PASS

Classification:

`PASS_A3_2_FIGURE2_ROUTING_PREFLIGHT_SCOPED`.

Merged authority:

`c68eeccb734c1f77c411ad5f531efafb082c1526`.

Canonical tadpole/bubble/triangle/ghost-triangle routings conserve momentum, pair every internal edge with opposite endpoint momentum, preserve all six external permutations and inherited topology coefficients under the frozen diagnostic affine q shifts.

Successful run `35000570266`, job `104487655005`, artifact `10409661837`, digest `sha256:4f20ca865dfc1987937a3689de7106bd38923331d9b6c666b01eace0e8ba7d5f`.

Retain:

`LOOP_ROUTING_EQUIVALENCE != HOLD_REGULATOR_ARGUMENT_FIXED_WHILE_SHIFTING_OTHER_LINES`.

### A3.2 fixed-q tensor contraction assembly — PASS

Classification:

`PASS_A3_2_FIGURE2_TENSOR_CONTRACTION_ASSEMBLY_SCOPED`.

Merged authority:

`2beb6bc6fb9d0544410512c7443b273b45487ecb`.

At two frozen dense q controls the full Figure-2 baseline contractions were assembled with C3 disabled using:

- full six-dimensional internal Landau-transverse graviton spaces;
- source-Fourier EH n=3/4/5 vertices;
- `G=(H+R)^-1`;
- canonical single-scale line `S=G dotR G`;
- frozen ghost-arrow matrix chain;
- inherited topology coefficients `(-1/2,+3,-3,+6)`.

All four topology classes were finite/nonzero on the controls. Consistent internal basis rotations changed contracted scalars by at most `1.65e-14`; maximum propagator inverse residual was `3.18e-16`. Ten contraction-level counterexample mutations were rejected.

Successful run `35000997597`, job `104489066892`, artifact `10409825944`, digest `sha256:bc558d2fa44d1cde0103b6f4ca1bc059b1740161927c63fb847cb008f51fe4bb`.

Retain:

`SINGLE_SCALE_PROPAGATOR = G dotR G`, not `G dotR`.

## Current exact frontier

SF055 Lane B: terminal PASS scoped.

SF055 Lane C: terminal PASS scoped.

SF055 Lane A: **still open**.

Immediate active dependency:

`DETERMINISTIC_FIGURE2_QUADRATURE_AND_EQ14_BASELINE_REPRODUCTION`.

The exact fixed-q contraction object must now be integrated under the already-frozen SF055A3 convergence sequence and then reproduce all three Eq. (14) baseline targets through the same implementation path.

Only after Lane A terminal PASS may SF055 itself be considered for terminal implementation validation and only then may a substantive C3 projected-flow output be inspected.

`SF055_TERMINAL_PASS = FALSE`.

## Operational front retained

SF028B remains the boundary-complete coherence authority; SF029-SF042 retain the known-physics calibration/control chain.

Operational blocker remains:

`DEVICE_LEVEL_NONLINEAR_CROSSTALK_MAGNITUDE_AND_STABILITY_DATA_REQUIRED`.

Retain:

`OPEN_ACTION != MEASURED_REDUCED_COHERENCE`,

`NONZERO_CONNECTED_SIGNAL != NEW_THREE_BODY_GRAVITATIONAL_VERTEX`,

`STRUCTURAL_CONTROL_CLOSURE != DEVICE_VALIDATION`.

## Claim locks

Without separate authority:

- no physical SF025 `b` selected;
- no truncation constant promoted to physical matching;
- no background/fluctuation equality assumed;
- no frozen-point quotient PASS promoted to arbitrary kinematics;
- no projected dynamical C3 beta function claimed;
- no Lane-B/C/A3 sub-PASS promoted to SF055 terminal PASS;
- no three-point-only C3 truncation called covariantly complete;
- no Euclidean off-shell coefficient called a physical observable without continuation;
- no operational result selects quantum-law matching;
- no quantum `chi_ABC` computed;
- no historical RCG-002 authority changed;
- no asymptotic-safety correctness claim;
- no `NEW_PHYSICS_FOUND`, `FULL_QUANTUM_GRAVITY`, `THEORY_ESTABLISHED`, or unique quantum-gravity selector claim.
