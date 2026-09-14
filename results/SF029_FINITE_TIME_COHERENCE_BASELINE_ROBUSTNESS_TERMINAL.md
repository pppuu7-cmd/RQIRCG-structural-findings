# SF029 — finite-time coherence baseline robustness — TERMINAL

Date: 2026-09-15
Preregistration: `ee392560debda35c0fbe51ca65112d1939fb3cfb`.
Script: `scripts/sf029_checks.py`, commit `2373f6baca6a77d169553b09fd6ed89f1d7e1170`.
Canonical raw output: `results/raw/SF029_CHECKS.json`, commit `fc11740ea476253b6755d2af90a0cd763ee6ee36`.
Derivation/source notes: `research_log/SF029_ROBUSTNESS_DERIVATION_AND_AUTHORITY_NOTES.md`, commit `0f2a6ff88c885bbe80adcf28759a5cbaa1436234`.
Executed script SHA-256: `6dd62123bc8c523fa8731a596ce2e59447d67a6f13936851bf46e48c75bc7b94`.

## RESULT / CLASSIFICATION

`ROBUST_KNOWN_PHYSICS_COHERENCE_BASELINE_HIERARCHY_SCOPED`

Secondary structural classifications:

`DISTINCT_NUISANCE_SCALINGS_CREATE_BASELINE_CROSSOVER_SURFACES_SCOPED`

`FINITE_R_1PN_APPARATUS_CORRECTION_DECAYS_MORE_SLOWLY_THAN_NEWTONIAN_APPARATUS_CONNECTED_TERM_SCOPED`

`SHORT_TIME_COHERENCE_EXPANSION_CONTROLLED_ON_FULL_FROZEN_TAU_GRID_SCOPED`

No quantum-law matching coefficient is selected. No quantum `chi_ABC` is computed.

## Frozen physical object retained

SF029 kept exactly the SF028B boundary-complete reduced-qubit-coherence object:

`NORMALIZED 3-QUBIT + 4-BODY 3D MOTIONAL STATE`
`-> COM-CLOSED U_PREP`
`-> FULL FREE ALL-BODY EVOLUTION`
`-> U_PREP^dagger RECOMBINATION`
`-> TRACE MOTION`
`-> QUBIT TOMOGRAPHY`.

The connected observable remains

`C3=Log K_111-Log K_110-Log K_101-Log K_011+Log K_100+Log K_010+Log K_001`,

`Theta3=Im C3`,

`Gamma3=-Re C3`.

The leading known-physics structure remains

`Theta3^N = -(T/hbar) Delta3[V_N] + (T^3/(12hbar)) Delta3[A_N] + ...`,

`Gamma3^N = (sigma^2 T^2/(2hbar^2)) Delta3[Q] + ...`,

`Delta_1PN Theta3 = -(T/hbar) Delta3[V_static^1PN] + ...`.

No open action is promoted.

## Frozen robustness families

The prospectively fixed nuisance families were:

- `R/ell = {30,40,60,80,120,160,250,400,800}`;
- `sigma/ell = {1/200,1/100,1/50,1/25,1/20}`;
- `tau = {1/100,1/50,1/20,1/10,1/5}`;
- `rho/ell = {0,1/200,1/100,1/50,1/20}`.

The branch geometry, apparatus mass `M_D=5m`, COM closure, state/readout identity, finite-difference convention and Newtonian/EIH baselines were not changed.

## Exact controls

For every new R cell, delete-A, delete-B and delete-C controls give exact zero for

`Delta3 V_N`, `Delta3 A_N`, `Delta3 V_static^1PN`, and `Delta3 Q`.

All exact controls pass.

Across the full new R grid:

`Delta3 A_N < 0`,

`Delta3 Q < 0`,

`Delta3 V_static^1PN > 0`.

No nuisance-induced sign crossing appears.

## Finite-R robustness result

The exact source-only limits are

`Delta3 A_N(infinity) = -82/616005`,

`Delta3 V_static^1PN(infinity) = 2/945`.

The observed fractional 1PN apparatus correction relative to the source-only 1PN coefficient is:

- `R=30 ell`: `23.98%`;
- `R=40 ell`: `14.93%`;
- `R=60 ell`: `6.41%`;
- `R=80 ell`: `3.49%`;
- `R=120 ell`: `1.50%`;
- `R=160 ell`: `0.826%`;
- `R=250 ell`: `0.331%`;
- `R=400 ell`: `0.128%`;
- `R=800 ell`: `0.0315%`.

These values are specific to the frozen geometry and are calibration landmarks, not universal design requirements.

By contrast, the Newtonian feedback coefficient approaches its source-only limit much faster: its fractional apparatus correction is already about `0.201%` at `R=60 ell`, `0.0587%` at `R=80 ell`, and `0.0107%` at `R=120 ell`.

## Asymptotic scaling diagnostic

The finite grid is used only as a diagnostic because SF024 already supplied the analytic multipole scaling.

Large-R effective powers approach:

`|Delta3 V_N| ~ R^-4`,

`|Delta3 A_N(R)-Delta3 A_N(infinity)| ~ R^-4`,

`|Delta3 V_1PN(R)-Delta3 V_1PN(infinity)| ~ R^-2`.

For the final tested interval `R=400 -> 800`, the effective powers are approximately

`4.047`, `4.034`, and `2.017`, respectively.

This explains why a finite apparatus can be essentially decoupled from the Newtonian force-feedback coefficient while still giving a percent-level 1PN correction.

## Crossover surface 1 — Newtonian apparatus versus 1PN

Define

`epsilon_PN = Gm/(c^2 ell)`

and

`epsilon_app(R)=|Delta3 V_N(R)|/|Delta3 V_static^1PN(R)|`.

Then the finite-R Newtonian apparatus `O(T)` term exceeds the 1PN `O(T)` term whenever

`epsilon_PN < epsilon_app(R)`.

The frozen values are:

- `R=30`: `7.71e-2`;
- `R=40`: `1.36e-2`;
- `R=60`: `1.69e-3`;
- `R=80`: `4.47e-4`;
- `R=120`: `7.55e-5`;
- `R=160`: `2.23e-5`;
- `R=250`: `3.49e-6`;
- `R=400`: `5.11e-7`;
- `R=800`: `3.09e-8`.

Thus raw connected coherence can remain Newtonian-apparatus dominated deep into a weak-field regime even when the desired 1PN coefficient is perfectly well defined.

This does not obstruct a same-protocol theory comparator; it does forbid interpreting raw nonzero connected coherence as the nonlinear gravity term without baseline subtraction/calibration.

## Crossover surface 2 — Newtonian feedback versus 1PN

Define

`epsilon_fb(R,tau)=|Delta3 A_N(R)| tau^2/[12 |Delta3 V_static^1PN(R)|]`.

Newtonian self-consistent feedback exceeds the 1PN comparator whenever

`epsilon_PN < epsilon_fb(R,tau)`.

At `tau=0.1`, the frozen values range from approximately

`6.51e-5` at `R=30`

to

`5.24e-5` at `R=800`.

Unlike the finite-R apparatus term, this contribution approaches a nonzero source-only limit as `R -> infinity`. Increasing apparatus distance alone therefore cannot remove it.

Time dependence is essential: this term is `O(T^3)`, while the leading 1PN comparator is `O(T)`.

## Short-time validity result

The preregistered control metrics were

`eta_disp <= 0.02`,

`eta_H <= 0.05`.

Every `tau <= 0.1` cell passes for every R, satisfying the preregistered PASS condition.

Stronger result: the entire frozen `tau=0.2` row also passes.

The worst observed `tau=0.2` values are only approximately

`eta_disp = 8.63e-4`,

`eta_H = 6.20e-3`.

Therefore no short-time validity boundary occurs inside the frozen tau family.

This does not prove exact all-time packet evolution.

## Packet-width result

For the frozen `sigma` family the geometric narrow-packet ratio is

`eta_sigma=sigma/d_min <= 1.67e-2`.

At the retained order the quantity

`Gamma3/(sigma^2 T^2/hbar^2)`

is constant over the entire width grid and equals

`-6.654245028696249e-5`

for the inherited `R=100 ell` primary cell.

Thus the prospectively frozen `sigma^2` scaling is exactly reproduced at this order.

No packet width is selected by outcome.

## Finite-size applicability

For the frozen spherical-radius family, the minimum branch-center separation is `3 ell` and the worst center-level nonoverlap margin at `rho=ell/20` is `2.9 ell`.

No finite-size parameter is fitted.

Goldberger-Rothstein EFT power counting places leading conservative tidal finite-size operators well beyond 1PN for spinless compact objects, and standard PN reviews treat tidal structure as a separate higher-order sector. This supports the inherited nonspinning spherical/monopole 1PN applicability ceiling.

The claim remains leading-semiclassical and center-level. It does not construct exact extended-body Gaussian packet dynamics, material control stresses or branch-generation hardware.

## Structural result

The known-physics connected baseline is robust but **not one nuisance amplitude**.

It contains distinct scalings:

`finite-R Newtonian apparatus: O(T) with asymptotic R^-4 suppression`,

`self-consistent Newtonian feedback: O(T^3), nonzero R->infinity limit`,

`ordinary 1PN gravity: O(T), nonzero R->infinity limit with R^-2 apparatus correction`,

`connected visibility cumulant: O(sigma^2 T^2)`.

Therefore the correct next scientific problem is not to search for another connected coefficient. It is to test whether these known-physics components are **operationally identifiable/calibratable from the same protocol family without post-hoc nuisance fitting**.

## Claim ceiling

SF029 does not establish:

- laboratory feasibility;
- exact all-time coherence;
- complete quantum wave-packet dynamics;
- exact extended-body apparatus physics;
- a new quantum-gravity law;
- a quantum matching coefficient;
- a GR-vs-QG discriminator;
- quantum `chi_ABC`;
- new physics.

Retain strictly:

`NONZERO_CONNECTED_SIGNAL != NEW_THREE_BODY_GRAVITATIONAL_VERTEX`.

Theory-track blocker remains:

`GENUINELY_NEW_MICROSCOPIC_MATCHING_PRINCIPLE_WITH_EXPLICIT_PHYSICAL_MAP_REQUIRED`.

## Exact next admissible operational gate

`SF030_KNOWN_PHYSICS_COHERENCE_COMPONENT_IDENTIFIABILITY_PREOUTCOME_GATE`.

Before evaluating any new outcome, prospectively freeze a multi-R / multi-T calibration design and test whether the finite-R Newtonian apparatus term, Newtonian `T^3` feedback, and 1PN `T` term can be separated at nonzero information rank using the same physical `C3` readout.

The gate must use design-matrix rank/conditioning and negative controls. It may not fit or introduce any successor quantum coefficient.