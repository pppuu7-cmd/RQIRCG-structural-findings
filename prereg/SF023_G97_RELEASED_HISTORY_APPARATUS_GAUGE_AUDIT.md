# SF023 — G97 released-history apparatus and gauge audit — PREREGISTRATION

Date: 2026-09-14
Status: **FROZEN BEFORE CLOSED-PROTOCOL EVALUATION**

## Context

SF022 derived a parameter-free nonzero 1PN connected point-source phase-rate kernel from the prospectively selected RHPI/ADM law. SF022 explicitly did not prove that the isolated point-source EIH representative is already the full closed laboratory observable.

SF023 tests the two highest-risk issues:

1. G97 apparatus/support closure;
2. coordinate/canonical/gauge dependence of the isolated EIH potential representative.

No new gravitational coefficient may be introduced.

## Frozen operational target

The target is the **instantaneous connected phase rate immediately after release** from a closed preparation:

`dot(chi_ABC)(0+)`.

This choice avoids postulating a finite static holding interval with hidden external support forces.

The finite-duration integrated phase is deferred until the released-history kernel is closed.

## Closed preparation architecture

Use three source bodies `A,B,C` plus three local preparation/recoil devices `D_A,D_B,D_C` and any branch-independent common reference body `R0` needed to define the relational frame.

For each source `X`:

1. device `D_X` prepares the binary source position branch `x_X(0)` / `x_X(1)` through an internal impulse/translation process;
2. the source+device impulse map conserves the total momentum of that local module exactly, following the G97 logic;
3. the device may carry a branch-dependent recoil state, but that dependence is local to the corresponding bit before gravitational interactions are evaluated;
4. at the release event `t=0`, all preparation couplings/holding forces are switched off as internal interactions, and the complete source+device system evolves freely under the selected gravitational law plus its frozen nongravitational internal Hamiltonians.

The total preparation is closed. No infinite-mass external holder is permitted.

## Frozen release kinematics

At `t=0+` in the relational interaction frame:

- source velocities are zero to the retained point-source kernel order;
- source positions are the binary branch positions frozen in SF022;
- each recoil device is at finite distance `R_X` from the source interaction region, with finite mass `M_X` and finite branch displacement/recoil data;
- define `d = max(r_AB,r_AC,r_BC)` for source separations;
- the apparatus-decoupling limit is `R_X/d -> infinity` at fixed finite masses and fixed local branch displacements.

No apparatus mass may be set to zero merely to force decoupling.

## Total 1PN phase-rate rule

Evaluate the same selected EIH/ADM 1PN conservative Hamiltonian/Lagrangian reduction for **all branch-dependent bodies**, not just A,B,C.

The connected finite difference is taken only over the source branch labels `(a,b,c)`, with apparatus branch states determined by the frozen local preparation map.

Split the exact all-body result into:

1. pure-source triples `ABC`;
2. two-source + one-device triples;
3. one-source + two-device triples;
4. three-device triples;
5. repeated-label/pairwise sectors.

The pure-source contribution must reproduce SF022 in the point-source limit.

## Apparatus-decoupling criterion

For every connected term containing at least one recoil/preparation device, audit its scaling in the limit `R_X/d -> infinity`.

The SF022 kernel is physically isolated in this limit only if

`dot(chi_total) = dot(chi_source) + O(d/R_min)`

or faster suppression, with the precise mass-dependent coefficient finite for fixed device masses.

If a branch-dependent apparatus contribution remains finite as all devices are taken far away, the source-only promotion fails.

## Gauge/canonical audit

The standard 1PN N-body dynamics admits different coordinate/canonical representatives related by contact/canonical transformations and total time derivatives.

SF023 freezes two complementary tests.

### G1 — boundary/total-derivative control

For a time-independent total derivative `dF(q)/dt`, evaluate its contribution to the instantaneous phase rate at the frozen source rest instant. If all relevant source velocities vanish, the source-coordinate contribution must vanish at that instant.

This is only a scoped control; it does not prove invariance under every possible momentum-dependent canonical transformation.

### G2 — relational observable statement

The promoted object is not “the harmonic-coordinate potential term” by itself. It is the phase-rate difference conditioned on the same **relational source separations** and transformed consistently with states/observables.

Any canonical transformation that merely changes theory coordinates must leave the physical selector-fiber prediction invariant after relational data are mapped consistently. If an apparent change survives for the same relational configuration, the gauge audit remains blocked.

## Point-source / finite-size lock

SF023 retains the point-source limit only under

`source size / d << 1`.

Finite-size/tidal coefficients are not set to arbitrary values. They are omitted only as a controlled leading-order approximation and must enter a later uncertainty/matching audit if their power-counting order competes with the 1PN connected term.

## Exact controls

C1. Remove all apparatus branch dependence while keeping devices finite and distant. Then apparatus-only contributions to `Delta_A Delta_B Delta_C` must vanish unless mediated through source-dependent gravitational dynamics beyond the instantaneous kernel.

C2. Take `R_X/d -> infinity` with finite `M_X`. Every explicit apparatus-containing instantaneous EIH triple contribution must vanish relative to the pure-source finite term.

C3. Set one source branch displacement to zero. Total connected phase rate must vanish in the apparatus-decoupled limit.

C4. `G -> 0` gives zero.

## Pass classification

If the closed all-body instantaneous kernel has the asymptotic form

`dot(chi_total)(0+) = dot(chi_SF022)(0+) + apparatus corrections -> dot(chi_SF022)`

and the frozen gauge controls reveal no surviving representation artifact, return

`G97_CLOSED_RELEASE_LIMIT_RECOVERS_RHPI_1PN_CONNECTED_KERNEL_SCOPED`.

## Block/fail classifications

If apparatus terms do not decouple:

`APPARATUS_CONNECTED_CONTRIBUTION_REMAINS_AT_LEADING_ORDER`.

If canonical/gauge equivalence cannot be established:

`CONNECTED_KERNEL_GAUGE_PROMOTION_BLOCKED`.

Both labels may coexist; no criterion may be weakened after evaluation.

## Claim ceiling

Even a PASS establishes a closed **instantaneous release-limit phase-rate** prediction, not yet a full finite-time experimental interferometer. Finite-time trajectories, radiation/reaction, quantum noise, finite-size matching and practical measurability remain downstream.
