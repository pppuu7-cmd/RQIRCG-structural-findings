# RQIRCGSF research ledger — SF030 addendum

Date: 2026-09-15

## STATE_READ

Inherited recovery head: `bb147285d13d8548bcbe09a5d273b2fba2e15b0a`.

Inherited operational result: SF029 `ROBUST_KNOWN_PHYSICS_COHERENCE_BASELINE_HIERARCHY_SCOPED`.

## TARGET_GATE

`SF030_KNOWN_PHYSICS_COHERENCE_COMPONENT_IDENTIFIABILITY_PREOUTCOME_GATE`.

## PREREG

`0fa7251021afc5c230578c5c933b1e11d78c3a3d`.

Frozen 9-row design:

`R/ell={60,160,400}` x `tau={0.05,0.1,0.2}`.

Known basis only:

- finite-R Newtonian apparatus;
- Newtonian self-consistent feedback;
- ordinary 1PN EIH.

No successor/quantum column.

## IMPLEMENTATION

Initial script commit `4eaaea7904ddaf3acebf4f509478e792ffc25040` had only a repository-path issue before terminalization. It was corrected without changing any scientific object, design point, matrix definition or threshold.

Corrected script authority:

`d197fbbbe6560fb3cf919ce04ad8533afaae786e`.

Executed corrected script SHA-256:

`062b1b540bc42b40968ff55ad2cbf7079390da5e5463ac2cd9cc25f65726d00a`.

Canonical raw:

`f60946d712192313a2fccd18d7642b57ed9e0cee`.

Raw SHA-256:

`cc6514e4b45ac1a45e545220178a51bb26468aa030ca794e206d5a6b8d498944`.

## RESULT

Terminal commit:

`6a7d5e9455441a1182c260913da79ed5c4f3abd9`.

Classification:

`KNOWN_PHYSICS_COHERENCE_COMPONENTS_STRUCTURALLY_IDENTIFIABLE_SCOPED`.

Secondary:

`R_VARIATION_REQUIRED_TO_BREAK_T_LINEAR_APPARATUS_VS_1PN_DEGENERACY_SCOPED`.

`JOINT_R_AND_T_DESIGN_STRONGLY_IMPROVES_CONDITIONING_SCOPED`.

`STRUCTURAL_IDENTIFIABILITY_DOES_NOT_REMOVE_SMALL_EPSILON_PN_DYNAMIC_RANGE_SCOPED`.

## KEY NUMBERS

Full normalized design:

- rank `3`;
- singular values `(1.53862,0.74581,0.27644)`;
- condition number `5.5659`.

All leave-one-R subsets remain rank 3 with `kappa<5.91`.

All leave-one-tau subsets remain rank 3 with `kappa<9.56`.

Each single-R negative control has exact/numerical rank `2`, confirming the predicted two-linear-T degeneracy.

Each single-tau R-only control has formal rank 3 but poor `kappa~867.74`.

Thus joint R+T variation is the productive calibration lever.

Physical unnormalized conditioning becomes severe when the PN column is very small; at the frozen diagnostic `epsilon_PN=1e-8`, `kappa_phys~2.50e5`. This is an estimability/precision issue, not loss of algebraic rank.

## CLAIM_CEILING

`IDENTIFIABILITY != ESTIMABILITY`.

`IDENTIFIABILITY != DYNAMICS`.

No detector precision, feasibility, successor residual, quantum matching coefficient, quantum `chi_ABC`, or new physics.

## NEXT

Operational:

`SF031_NOISE_AWARE_KNOWN_BASELINE_ESTIMABILITY_PREOUTCOME_GATE`.

Theory remains independently blocked on:

`GENUINELY_NEW_MICROSCOPIC_MATCHING_PRINCIPLE_WITH_EXPLICIT_PHYSICAL_MAP_REQUIRED`.