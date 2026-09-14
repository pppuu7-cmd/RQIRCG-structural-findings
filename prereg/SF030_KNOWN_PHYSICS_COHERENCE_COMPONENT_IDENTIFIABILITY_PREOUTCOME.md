# SF030 — known-physics coherence component identifiability — PREOUTCOME PREREGISTRATION

Date: 2026-09-15
Inherited authoritative recovery head: `bb147285d13d8548bcbe09a5d273b2fba2e15b0a`.

## PURPOSE

Test whether the three already-authorized known-physics contributions to the SF028B/SF029 connected phase readout are structurally separable from the **same physical protocol family**, before introducing any successor quantum coefficient.

This is an identifiability/calibration gate, not a new-law search.

## PHYSICAL READOUT LOCK

Keep the same boundary-complete `C3`/`Theta3` readout and all SF028B object definitions.

At retained order use the decomposition

`Theta3(R,tau) = alpha_app f_app(R) tau + alpha_fb f_fb(R) tau^3 + alpha_1PN epsilon_PN f_1PN(R) tau + higher orders`,

where the shape functions are fixed by known physics:

`f_app(R) = -Delta3 V_N(R)`,

`f_fb(R) = Delta3 A_N(R)/12`,

`f_1PN(R) = -Delta3 V_static^1PN(R)`.

`epsilon_PN=Gm/(c^2 ell)` is a calibrated weak-field scale, not a fitted new coefficient.

The dimensionless amplitudes `alpha_app`, `alpha_fb`, `alpha_1PN` are **calibration coordinates only**. Under the nominal known-physics model each equals one. They are introduced only to ask whether these three known basis components can be distinguished by the protocol family.

No successor/quantum column is allowed.

## FROZEN CALIBRATION DESIGN

Use the Cartesian product

`R/ell in {60,160,400}`

and

`tau in {1/20,1/10,1/5}`.

This gives 9 phase-readout rows.

No design point may be moved after singular values are observed.

The chosen R values span the prospectively completed SF029 hierarchy from finite apparatus correction to near-source-limit behavior; the chosen tau values all passed the SF029 short-time validity controls.

## DESIGN MATRICES

### Structural shape matrix

For row `(R,tau)` define

`X_shape = [ f_app(R) tau, f_fb(R) tau^3, f_1PN(R) tau ]`.

Before computing singular values, independently normalize each column to Euclidean norm one.

This normalized matrix tests **shape identifiability / collinearity**, not signal amplitude.

Report:

- numerical rank using tolerance `s_i/s_max > 1e-10`;
- all singular values;
- condition number `kappa_shape=s_max/s_min`;
- pairwise normalized-column correlations.

### Physical-dynamic-range matrix

Also evaluate the unnormalized matrix

`X_phys(epsilon) = [ f_app tau, f_fb tau^3, epsilon f_1PN tau ]`

for the frozen diagnostic values

`epsilon in {1e-2,1e-4,1e-6,1e-8}`.

These values are not asserted laboratory parameters. They only expose how structural identifiability differs from practical dynamic range as the PN scale becomes small.

No detector-noise claim may be derived without an explicit noise model.

## PROSPECTIVE PASS / QUALIFICATION RULES

### PASS

`KNOWN_PHYSICS_COHERENCE_COMPONENTS_STRUCTURALLY_IDENTIFIABLE_SCOPED`

requires:

1. full 9-row normalized matrix has rank 3;
2. `kappa_shape <= 10`;
3. every leave-one-R-out subset remains rank 3 with `kappa_shape <= 25`;
4. every leave-one-tau-out subset remains rank 3 with `kappa_shape <= 25`;
5. the single-R ablation has rank at most 2, as an exact negative control showing why R variation is required.

### QUALIFIED

`IDENTIFIABLE_BUT_ILL_CONDITIONED_SCOPED`

if rank is 3 but any preregistered condition-number bound fails.

### FAIL / NONIDENTIFIABLE

`KNOWN_PHYSICS_COMPONENT_DEGENERACY_SURVIVES_SCOPED`

if the full frozen design has rank <3.

### INVALID

`INVALID_DESIGN_OR_OBJECT_IDENTITY`

if any coefficient function, readout, R/tau point, normalization rule, or baseline identity changes after evaluation.

## REQUIRED ABLATIONS

A. **Single-R negative control**: choose each of the three frozen R values separately with all three tau values. Because apparatus and 1PN columns are both proportional to `tau` at fixed R, structural rank must be <=2. This is a required logical control.

B. **Single-tau R-only control**: choose each frozen tau separately across the three R values. Report rank/conditioning without a predeclared PASS requirement. This diagnoses how much separation comes from distinct R-scaling alone.

C. **Leave-one-R-out**: all 6-row subsets.

D. **Leave-one-tau-out**: all 6-row subsets.

E. **Column-deletion controls**: removing any one known component must reduce the fitted component count accordingly; no missing column may be interpreted as zero physical contribution.

## NUISANCE-EQUIVALENCE AUDIT

The gate must distinguish:

- mathematical basis rank;
- coefficient dynamic range;
- experimental estimability.

A full-rank normalized matrix does not prove a tiny 1PN coefficient is measurable in the presence of detector noise or calibration error.

A large unnormalized condition number at small `epsilon_PN` is not a scientific degeneracy theorem; it is a scale/precision requirement.

No residual after fitting these three known components may be called quantum gravity without a separately selected successor law and a prospectively frozen residual model.

## EXPECTED STRUCTURAL LOGIC — NOT A RESULT

At fixed R, the apparatus and 1PN columns share the same `tau` dependence, so time scans alone cannot separate them.

Across R, their known shapes differ strongly (`R^-4`-like apparatus suppression versus nonzero-source-limit 1PN with `R^-2` correction), so multi-R data may lift that degeneracy.

The Newtonian feedback column carries `tau^3`, so multi-tau data may isolate it.

These are motivations for the gate, not precomputed verdicts.

## INTERPRETATION CEILING

Even PASS establishes only noiseless local algebraic identifiability of the three **known-physics** basis components in the frozen leading-order protocol family.

It does not establish:

- detector feasibility;
- statistical precision;
- robust estimation under arbitrary calibration systematics;
- exact all-time dynamics;
- a successor quantum contribution;
- a quantum matching coefficient;
- GR-vs-QG discrimination;
- quantum `chi_ABC`;
- new physics.

Retain:

`IDENTIFIABILITY != DYNAMICS`.

Retain:

`NONZERO_CONNECTED_SIGNAL != NEW_THREE_BODY_GRAVITATIONAL_VERTEX`.

Theory track remains independently blocked on

`GENUINELY_NEW_MICROSCOPIC_MATCHING_PRINCIPLE_WITH_EXPLICIT_PHYSICAL_MAP_REQUIRED`.