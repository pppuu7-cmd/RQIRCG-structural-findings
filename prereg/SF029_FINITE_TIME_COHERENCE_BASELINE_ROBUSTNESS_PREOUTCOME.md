# SF029 — finite-time coherence baseline robustness — PREOUTCOME PREREGISTRATION

Date: 2026-09-15
Inherited authoritative head: `4e9d1d243d666d7d0db44f31f1b0851b720cccc0`.

## PURPOSE

Test whether the **same physical boundary-complete connected readout** constructed in SF028B remains structurally stable across prospectively frozen nuisance families, without searching nuisance space for a preferred sign, coefficient, cancellation, or apparent beyond-known-physics residual.

This gate is a robustness / validity-domain gate. It is not a new connected-coefficient search and does not select quantum-law matching data.

## INHERITED PHYSICAL OBJECT

Keep the SF028B normalized chain unchanged:

`NORMALIZED 3-QUBIT + 4-BODY 3D MOTIONAL STATE`
`-> COM-CLOSED U_PREP`
`-> FULL FREE ALL-BODY EVOLUTION`
`-> U_PREP^dagger RECOMBINATION`
`-> TRACE MOTION`
`-> QUBIT TOMOGRAPHY`.

For branch-reference coherences `K_s`, retain

`C3 = Log K_111-Log K_110-Log K_101-Log K_011+Log K_100+Log K_010+Log K_001`,

`Theta3 = Im C3`,

`Gamma3 = -Re C3`,

with continuous `Log` from `T=0`.

At the retained leading-semiclassical short-time order:

`Theta3^N = -(T/hbar) Delta3[V_N] + (T^3/(12 hbar)) Delta3[A_N] + ...`,

`Gamma3^N = (sigma^2 T^2/(2 hbar^2)) Delta3[Q] + ...`,

`Delta_1PN Theta3 = -(T/hbar) Delta3[V_static^1PN] + higher orders`.

No open action may replace this readout.

## FIXED SOURCE / APPARATUS TOPOLOGY

- equal source masses `m_A=m_B=m_C=m`;
- one common recoil/reference apparatus with `M_D=5m`;
- source branch centers on one axis:
  - `A=a ell`,
  - `B=(4+2b)ell`,
  - `C=(10+3c)ell`;
- exact total-COM closure for apparatus branch center:
  `x_D = R - (a+2b+3c)ell/5`;
- zero branch mean velocities at release;
- same inverse preparation/recombination and same tomography convention in every nuisance cell.

Changing branch geometry, apparatus topology, mass ratio, readout, coefficient definitions, or baseline model after seeing results is forbidden.

## PROSPECTIVELY FROZEN NUISANCE FAMILIES

### Lane R — finite apparatus distance

Evaluate exact rational center-level coefficients at previously unreported values

`R/ell in {30, 40, 60, 80, 120, 160, 250, 400, 800}`.

The earlier SF028B values `{50,100,200,1000}` are retained only as inherited controls and must not be used to retune criteria.

For every R cell compute:

- `Delta3 V_N(R)`;
- `Delta3 A_N(R)`;
- `Delta3 Q(R)`;
- `Delta3 V_static^1PN(R)`;
- fractional departure of `Delta3 A_N` from its source-only limit;
- fractional departure of `Delta3 V_static^1PN` from its source-only limit;
- geometry-only crossover
  `epsilon_app(R)=|Delta3 V_N|/|Delta3 V_static^1PN|`;
- feedback crossover coefficient
  `epsilon_fb(R,tau)=|Delta3 A_N| tau^2/(12 |Delta3 V_static^1PN|)`.

No fit exponent is authoritative. A log-slope may be reported only as a diagnostic.

### Lane sigma — packet width

Freeze

`sigma/ell in {1/200, 1/100, 1/50, 1/25, 1/20}`.

The center-level `Theta3` coefficients are not allowed to be redefined as sigma-dependent at the retained leading order. The test is:

- `Gamma3` must scale exactly as `sigma^2` within the frozen leading formula;
- narrow-packet geometry parameter `eta_sigma = sigma/d_min` must be reported for every cell;
- no packet-width value may be selected because it makes `Gamma3` small or changes a preferred interpretation.

### Lane tau — short-time validity

Define

`tau = T/sqrt(ell^3/(Gm))`.

Freeze

`tau in {1/100, 1/50, 1/20, 1/10, 1/5}`.

For every branch and R cell evaluate dimensionless initial accelerations and the leading displacement estimate

`delta_i/ell = (1/2)|a_i| tau^2`,

and define

`eta_disp = max_i(delta_i)/d_min`.

Also compute the largest dimensionless mass-normalized Newtonian Hessian frequency magnitude `lambda_H` over the branch cube and

`eta_H = tau^2 lambda_H`.

The leading short-time formula is considered internally controlled on a cell when both

`eta_disp <= 0.02`

and

`eta_H <= 0.05`.

These thresholds are frozen before computation. If a tau cell violates them, record a validity boundary; do not delete or replace the cell.

### Lane size — spherical finite-size applicability ceiling

Freeze nonspinning spherical body/support radii

`rho/ell in {0, 1/200, 1/100, 1/50, 1/20}`.

This lane is an applicability/domain audit, not an invented finite-size coefficient model.

Required checks:

- `2 rho < d_min` for every source-source branch separation;
- source-apparatus nonoverlap for every R cell;
- Newtonian exterior monopole equivalence for nonoverlapping spherical bodies is used only in its exact spherical scope;
- inherited standard 1PN monopole/effacement authority is retained only within the already declared nonspinning weak-field scope;
- no material-control stress, tidal deformation, quadrupole, equation-of-state, or branch-generation hardware effect is assigned a value without a new prospective model.

Failure of this applicability lane is `FINITE_SIZE_MODEL_REQUIRED`, not a failure of Newtonian/EIH gravity.

## INDEPENDENT NEGATIVE CONTROLS

For every R cell, separately set each branch displacement amplitude to zero:

- delete A;
- delete B;
- delete C.

The corresponding connected finite differences must vanish exactly for all center-level coefficients.

Gravity-off (`G -> 0`) remains an exact null by scaling.

## SOURCE-ONLY LIMIT CONTROLS

The exact inherited source-only values are frozen:

`Delta3 V_N(infinity)=0`,

`Delta3 A_N(infinity)=-(82/616005) G^2 m^3/ell^4`,

`Delta3 V_static^1PN(infinity)=(2/945) G^2 m^3/(c^2 ell^2)`.

The new R grid must be compared to these limits without changing them.

## PRIMARY ROBUSTNESS QUESTIONS

Q1. Does `Delta3 V_static^1PN(R)` retain its source-limit sign throughout the frozen R family?

Q2. Does `Delta3 A_N(R)` retain its source-limit sign throughout the frozen R family?

Q3. Does `Delta3 Q(R)` retain one sign throughout the frozen R family, with sigma affecting only its prescribed `sigma^2` prefactor at this order?

Q4. Which frozen R cells make apparatus/COM contamination parametrically larger than the 1PN comparator for a given weak-field `epsilon_PN=Gm/(c^2 ell)`? Report the crossover `epsilon_app(R)`; do not choose an `epsilon_PN` to manufacture hierarchy.

Q5. Which `(R,tau)` cells make Newtonian feedback larger than the 1PN comparator? Report `epsilon_fb(R,tau)` and the short-time validity metrics.

Q6. Does the declared spherical finite-size family remain within the monopole applicability domain, or is an explicit finite-size/control-stress model required?

## PREDECLARED TERMINAL CLASSIFICATIONS

### PASS

`ROBUST_KNOWN_PHYSICS_COHERENCE_BASELINE_HIERARCHY_SCOPED`

if all exact controls pass, the same-protocol coefficients remain well-defined on the full frozen grid, no sign reversal occurs in the 1PN comparator or Newtonian feedback coefficient, and the short-time validity window contains at least the frozen `tau <= 1/10` cells for all R cells.

PASS does **not** require raw Newtonian apparatus contamination to be numerically smaller than the 1PN term; dominance boundaries are themselves scientific baseline information.

### QUALIFIED

`ROBUSTNESS_BOUNDARY_IDENTIFIED_SCOPED`

if the object remains valid but one or more frozen nuisance cells exhibit a sign crossing, a short-time-control violation, or loss of the inherited monopole applicability domain. Preserve the boundary; do not tune it away.

### BLOCKED

`BLOCKED_MISSING_FINITE_SIZE_OR_CONTROL_MODEL`

if the requested finite-size applicability cannot be assessed without introducing new material/control physics not authorized by this gate.

### INVALID

`INVALID_IMPLEMENTATION_OR_OBJECT_IDENTITY`

if the executed code changes the SF028B physical object, branch geometry, baseline identity, finite-difference convention, apparatus topology, or frozen nuisance grid.

## INTERPRETATION CEILING

Even a PASS establishes only robustness of a known-physics point-particle/monopole leading-semiclassical short-time baseline.

It does not establish:

- laboratory feasibility;
- exact all-time coherence;
- complete wave-packet dynamics;
- realistic pulse/control noise;
- a quantum-gravity law;
- a quantum matching coefficient;
- GR-vs-QG discrimination;
- new physics;
- quantum `chi_ABC`.

Retain:

`NONZERO_CONNECTED_SIGNAL != NEW_THREE_BODY_GRAVITATIONAL_VERTEX`.

Retain separately:

`GENUINELY_NEW_MICROSCOPIC_MATCHING_PRINCIPLE_WITH_EXPLICIT_PHYSICAL_MAP_REQUIRED`.

## CLAIM LOCK

No nuisance value, sign, threshold, or geometry may be changed after substantive results are observed. Any changed physical object requires a new preregistered gate.