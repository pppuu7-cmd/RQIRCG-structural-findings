# SF030 — known-physics coherence component identifiability — TERMINAL

Date: 2026-09-15
Preregistration: `0fa7251021afc5c230578c5c933b1e11d78c3a3d`.
Executed script: `scripts/sf030_checks.py`, corrected pre-terminal implementation commit `d197fbbbe6560fb3cf919ce04ad8533afaae786e`.
Canonical raw: `results/raw/SF030_CHECKS.json`, commit `f60946d712192313a2fccd18d7642b57ed9e0cee`.
Executed corrected script SHA-256: `062b1b540bc42b40968ff55ad2cbf7079390da5e5463ac2cd9cc25f65726d00a`.
Canonical raw SHA-256: `cc6514e4b45ac1a45e545220178a51bb26468aa030ca794e206d5a6b8d498944`.

## RESULT / CLASSIFICATION

`KNOWN_PHYSICS_COHERENCE_COMPONENTS_STRUCTURALLY_IDENTIFIABLE_SCOPED`

Secondary structural results:

`R_VARIATION_REQUIRED_TO_BREAK_T_LINEAR_APPARATUS_VS_1PN_DEGENERACY_SCOPED`

`JOINT_R_AND_T_DESIGN_STRONGLY_IMPROVES_CONDITIONING_SCOPED`

`STRUCTURAL_IDENTIFIABILITY_DOES_NOT_REMOVE_SMALL_EPSILON_PN_DYNAMIC_RANGE_SCOPED`

No successor quantum component was added or fitted.

## Frozen design

The preregistered calibration design was the 9-row Cartesian product

`R/ell in {60,160,400}`

and

`tau in {0.05,0.1,0.2}`.

The known basis was

`x_app = -Delta3 V_N(R) tau`,

`x_fb = [Delta3 A_N(R)/12] tau^3`,

`x_1PN = -Delta3 V_static^1PN(R) tau`.

For structural shape rank, each column was independently normalized to unit Euclidean norm before singular-value analysis.

For physical dynamic-range diagnostics, the 1PN column was multiplied by the frozen diagnostic `epsilon_PN` values without column normalization.

## Full design — structural shape result

The normalized full design has singular values

`s = (1.5386204771, 0.7458085029, 0.2764357147)`.

Therefore

`rank = 3`,

`kappa_shape = 5.5659250798`.

The preregistered PASS threshold was `kappa_shape <= 10`.

Thus all three known-physics component shapes are linearly independent with moderate normalized conditioning in the frozen joint `R,T` design.

## Leave-one-R robustness

Every 6-row leave-one-R-out design remains rank 3:

- omit `R=60`: `kappa=5.906`;
- omit `R=160`: `kappa=5.758`;
- omit `R=400`: `kappa=5.790`.

All are comfortably below the frozen `kappa<=25` robustness limit.

Thus the rank-3 result is not carried by one special apparatus distance.

## Leave-one-tau robustness

Every 6-row leave-one-tau-out design remains rank 3:

- omit `tau=0.05`: `kappa=6.458`;
- omit `tau=0.10`: `kappa=9.558`;
- omit `tau=0.20`: `kappa=6.458`.

All pass the frozen `kappa<=25` limit.

Thus the rank-3 result is not carried by one special interaction time.

## Required single-R negative control

For each fixed R separately, the three-column design has

`rank = 2`.

The smallest normalized singular value is numerical zero (`~1e-16`).

This is the exact expected degeneracy: at one R,

`x_app ~ tau`,

`x_1PN ~ tau`,

so time variation alone cannot distinguish the finite-R Newtonian apparatus term from the 1PN term.

This negative control passes and proves that the successful full-rank result is not an artifact of the SVD tolerance.

## Single-tau R-only diagnostic

For each fixed tau, variation across the three R values gives formal rank 3, but the normalized condition number is

`kappa ~ 867.74`.

The normalized columns are nearly collinear in this restricted design.

Therefore R variation alone technically lifts the rank defect but does so very poorly.

The large improvement

`kappa: ~868 -> 5.57`

when the multi-tau lever arm is restored is the most useful design result of SF030.

The component decomposition is therefore not just a consequence of having many rows; it relies on the complementary physics scalings:

- apparatus Newtonian: `tau` with strong R suppression;
- self-consistent feedback: `tau^3` with nonzero source limit;
- 1PN: `tau` with nonzero source limit and slower finite-R correction.

## Correlation interpretation

In the full normalized design, the feedback and 1PN columns remain strongly correlated (`~0.9715`), but the independent time power is enough to retain a smallest singular value `0.2764` and moderate overall conditioning.

This is a useful warning: eliminating too much time leverage would rapidly degrade separation even though formal rank could remain three.

## Physical dynamic-range audit

Structural column normalization deliberately removes amplitude scale. It must not be confused with experimental estimability.

The preregistered unnormalized diagnostic matrices remain rank 3 for all tested

`epsilon_PN in {1e-2,1e-4,1e-6,1e-8}`,

but their condition numbers are:

- `epsilon_PN=1e-2`: `kappa_phys ~ 138.3`;
- `epsilon_PN=1e-4`: `kappa_phys ~ 27.8`;
- `epsilon_PN=1e-6`: `kappa_phys ~ 2.50e3`;
- `epsilon_PN=1e-8`: `kappa_phys ~ 2.50e5`.

The nonmonotonic moderate minimum around the intermediate diagnostic scale comes from balancing the absolute column norms; for sufficiently small `epsilon_PN`, the 1PN column becomes the tiny singular direction and conditioning degrades approximately in inverse proportion to its scale.

This does not destroy structural identifiability. It means practical estimation requires phase precision/calibration information that SF030 deliberately did not assume.

## Nuisance-equivalence conclusion

The frozen protocol family supplies nonzero algebraic information rank for the three known components.

But:

`IDENTIFIABILITY != ESTIMABILITY`.

A full-rank known-physics design does not prove that the 1PN coefficient is measurable at a laboratory-relevant `epsilon_PN`, because no detector/noise/correlated-calibration model has yet been specified.

Likewise:

`IDENTIFIABILITY != DYNAMICS`.

SF030 does not select or constrain the missing SF025/SF027 quantum-law matching datum.

## New structural fact

The SF028B/SF029 baseline is not only theoretically decomposable; it is **locally algebraically calibratable** using orthogonal control levers:

`R` breaks the two `T`-linear components,

`T` strongly improves separation of the `T^3` feedback component from the `T`-linear sector.

This supplies a principled route to known-physics subtraction that does not rely on observing one raw connected phase at one geometry/time.

## Claim ceiling

SF030 establishes no detector feasibility, statistical significance, calibration precision, exact all-time dynamics, successor quantum law, quantum matching coefficient, GR-vs-QG discriminator, quantum `chi_ABC`, or new physics.

No residual is authorized as quantum gravity.

Retain strictly:

`NONZERO_CONNECTED_SIGNAL != NEW_THREE_BODY_GRAVITATIONAL_VERTEX`.

Theory track remains:

`GENUINELY_NEW_MICROSCOPIC_MATCHING_PRINCIPLE_WITH_EXPLICIT_PHYSICAL_MAP_REQUIRED`.

## Exact next admissible operational gate

`SF031_NOISE_AWARE_KNOWN_BASELINE_ESTIMABILITY_PREOUTCOME_GATE`.

Freeze one minimal statistical model **before** computing precision requirements. The recommended first control is independent homoscedastic phase noise on the same 9 `Theta3` rows, followed by one correlated/common-mode nuisance ablation.

The gate should derive Fisher/Cramer-Rao precision requirements as functions of `epsilon_PN` and noise scale. It must distinguish required precision from claimed laboratory feasibility and may not add a successor quantum residual column.