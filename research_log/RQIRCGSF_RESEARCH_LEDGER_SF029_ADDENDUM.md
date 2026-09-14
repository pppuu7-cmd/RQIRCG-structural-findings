# RQIRCGSF research ledger — SF029 addendum

Date: 2026-09-15

## STATE_READ

Inherited source head: `4e9d1d243d666d7d0db44f31f1b0851b720cccc0`.

Inherited operational authority: SF028B `PASS_BOUNDARY_COMPLETE_KNOWN_PHYSICS_COHERENCE_BASELINE_SCOPED`.

Inherited theory blocker: `GENUINELY_NEW_MICROSCOPIC_MATCHING_PRINCIPLE_WITH_EXPLICIT_PHYSICAL_MAP_REQUIRED`.

## TARGET_GATE

`SF029_FINITE_TIME_COHERENCE_BASELINE_ROBUSTNESS_PREOUTCOME_GATE`.

## PREREG

`ee392560debda35c0fbe51ca65112d1939fb3cfb`.

Frozen independent nuisance lanes:

- finite apparatus distance `R`;
- packet width `sigma`;
- dimensionless short time `tau`;
- spherical finite-size applicability `rho`.

No branch geometry, apparatus topology, mass ratio, readout definition, baseline identity, sign convention or PASS threshold was changed after computation.

## EXECUTION

Reproducible exact-rational / numerical-control script:

`scripts/sf029_checks.py`

commit `2373f6baca6a77d169553b09fd6ed89f1d7e1170`.

Executed script SHA-256:

`6dd62123bc8c523fa8731a596ce2e59447d67a6f13936851bf46e48c75bc7b94`.

Canonical decision-relevant raw projection:

`results/raw/SF029_CHECKS.json`

commit `fc11740ea476253b6755d2af90a0cd763ee6ee36`.

Derivation / source authority:

`research_log/SF029_ROBUSTNESS_DERIVATION_AND_AUTHORITY_NOTES.md`

commit `0f2a6ff88c885bbe80adcf28759a5cbaa1436234`.

## RESULT

Terminal:

`results/SF029_FINITE_TIME_COHERENCE_BASELINE_ROBUSTNESS_TERMINAL.md`

commit `33660feffa3cf9c3ad1dc6d3cd75c73fea7f5887`.

Primary classification:

`ROBUST_KNOWN_PHYSICS_COHERENCE_BASELINE_HIERARCHY_SCOPED`.

Secondary structural results:

`DISTINCT_NUISANCE_SCALINGS_CREATE_BASELINE_CROSSOVER_SURFACES_SCOPED`.

`FINITE_R_1PN_APPARATUS_CORRECTION_DECAYS_MORE_SLOWLY_THAN_NEWTONIAN_APPARATUS_CONNECTED_TERM_SCOPED`.

`SHORT_TIME_COHERENCE_EXPANSION_CONTROLLED_ON_FULL_FROZEN_TAU_GRID_SCOPED`.

## KEY FINDINGS

1. Delete-A/B/C controls are exact zero over the entire new R grid.
2. `Delta3 A_N` and `Delta3 Q` remain negative; `Delta3 V_1PN` remains positive.
3. The full frozen `tau<=0.2` family passes prospectively fixed displacement/Hessian validity bounds.
4. `Gamma3` obeys the frozen `sigma^2` scaling at retained order.
5. Large-R diagnostics reproduce the analytic hierarchy: Newtonian apparatus and feedback correction approximately `R^-4`; 1PN apparatus correction approximately `R^-2`.
6. Raw connected coherence has explicit `epsilon_PN` crossover surfaces: ordinary Newtonian apparatus and motion feedback can exceed the 1PN term without any new gravitational vertex.
7. Spherical finite-size values through `rho=ell/20` remain within the declared center-level nonoverlap / inherited 1PN monopole scope; no material/control coefficient was invented.

## CLAIM_CEILING

No exact all-time channel, laboratory feasibility, exact extended-body quantum model, quantum-law selector, matching coefficient, GR-vs-QG discriminator, quantum `chi_ABC`, or new physics.

## NEXT

Operational:

`SF030_KNOWN_PHYSICS_COHERENCE_COMPONENT_IDENTIFIABILITY_PREOUTCOME_GATE`.

Theory:

`GENUINELY_NEW_MICROSCOPIC_MATCHING_PRINCIPLE_WITH_EXPLICIT_PHYSICAL_MAP_REQUIRED`.

Do not mix the two tracks.