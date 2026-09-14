# SF024 — single-recoil-apparatus closed release-limit gate — PREREGISTRATION

Date: 2026-09-14
Status: **FROZEN BEFORE APPARATUS DECOPLING EVALUATION**

## Context

SF023 found that three independent branch-record devices can themselves form an unsuppressed connected three-device gravitational cluster. SF024 changes the apparatus topology prospectively rather than patching SF023.

The RHPI/ADM gravitational law and SF022 source kernel remain unchanged.

## Frozen apparatus architecture

Use exactly one finite-mass common recoil/reference apparatus body `D` of mass `M` in addition to the three source bodies `A,B,C`.

Let source branch positions at the release event be the same generic binary configurations used in SF022.

Freeze a common total center of mass `X_CM=0` in every branch by defining the apparatus position

`x_D(a,b,c) = -[m_A x_A(a) + m_B x_B(b) + m_C x_C(c)]/M + R e_R`,

followed, if needed, by a branch-independent translation of all coordinates so that the chosen far-reference vector `R e_R` and total COM convention are mutually consistent. Operationally the required condition is exact branch-independent total COM and an apparatus-source separation scale `R >> d`; absolute origin is gauge/reference bookkeeping.

Equivalent implementation is allowed if it gives the same relational distances and exact COM closure.

At `t=0+`:

- all four bodies have zero velocity in the frozen interaction frame;
- all nongravitational preparation/holding interactions are off;
- the four-body system subsequently evolves freely;
- preparation history is not used to define the instantaneous post-release phase rate.

## G97 closure

The preparation map must be realizable by internal impulses/forces with exact total momentum conservation and invertibility, as in G97. The common apparatus is permitted to move branch-dependently during preparation and end at the branch-dependent COM-compensating position above, but with zero final velocity.

No infinite-mass or externally fixed support is permitted.

## Frozen hierarchy

Let

`d = max(r_AB,r_AC,r_BC)`

at release and let all source branch displacements be `O(d)`.

Take the apparatus decoupling limit

`epsilon = d/R -> 0`

with `m_A,m_B,m_C,M` fixed and finite.

The apparatus branch displacement induced by COM closure is `O((m_source/M)d)` and does not scale with `R`.

## Exact all-body sectors to audit

Use the same 1PN EIH law for four bodies.

The third finite difference over `(a,b,c)` can receive contributions from:

1. pure source triple `ABC` — must reproduce SF022;
2. distinct triples `ABD`, `ACD`, `BCD`;
3. repeated-label/pair sectors involving `D`, including Newtonian pair energies `A-D`, `B-D`, `C-D` whose distance to `D(a,b,c)` can inherit all three bits through COM closure;
4. kinetic sectors — zero at the release instant because all velocities vanish.

There is no three-device sector.

## Decoupling criterion

For every apparatus-containing branch energy, expand at fixed finite masses in `epsilon=d/R`.

Promotion requires

`Delta3 V_apparatus = o(1)`

as `R -> infinity`, while

`Delta3 V_ABC^(1PN)`

remains finite at fixed source geometry.

A sufficient result is any positive power suppression

`Delta3 V_apparatus / Delta3 V_source = O(epsilon^p)`

for `p>0`, modulo finite mass ratios.

## Frozen gauge/boundary controls

### G1 — zero-velocity total derivative
For any time-independent configuration-space total derivative `dF(q)/dt`, all four velocities vanish at `t=0+`, so its instantaneous contribution is exactly zero.

### G2 — conserved-energy representative
The promoted physical object is the full four-body conservative energy/phase rate at the same relational initial data, not a named coordinate potential term. Canonical/contact transformations must be accompanied by the corresponding transformation of positions/states. A disagreement at fixed physical relational data is a blocker.

### G3 — asymptotic relational reference
The far apparatus defines an operational reference frame only through relational distances. The `R -> infinity` limit must leave the finite source triangle observables unchanged rather than introduce an external absolute frame.

## Controls

C1. `M` finite but arbitrary: decoupling must not require `M=0` or `M=infinity`.

C2. Set `x_A(1)=x_A(0)`: source connected term and apparatus-decoupled total connected term must vanish.

C3. `G->0`: all gravitational connected terms vanish.

C4. If apparatus branch displacement is artificially set to zero, all Newtonian/pair apparatus terms depend on at most one source bit per source-device pair and the exact third finite difference vanishes; this is a calibration control only, not the physical COM-closed preparation.

## Pass classification

If apparatus contamination decouples and the frozen gauge controls pass:

`SINGLE_RECOIL_G97_RELEASE_LIMIT_RECOVERS_SF022_CONNECTED_KERNEL_SCOPED`.

## Failure/block classifications

If a finite apparatus-connected term survives as `R->infinity`:

`SINGLE_RECOIL_APPARATUS_DOES_NOT_DECOUPLE`.

If representation invariance of the full energy at fixed relational data cannot be established:

`RELEASE_PHASE_RATE_GAUGE_PROMOTION_REMAINS_BLOCKED`.

## Claim ceiling

A PASS establishes an asymptotically closed instantaneous release-limit phase-rate observable. It does not yet establish a finite-time interferometer, experimental feasibility, or quantum-noise prediction.
