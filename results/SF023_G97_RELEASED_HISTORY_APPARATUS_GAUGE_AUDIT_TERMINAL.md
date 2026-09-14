# SF023 — G97 released-history apparatus and gauge audit — TERMINAL / BLOCKED

Date: 2026-09-14
Status: **TERMINAL ADVERSARIAL BLOCK / protocol refined rather than patched**

Preregistration: `7c996667bab2aacf05b9299df064ddd02b229ec3`.

## Target

SF023 attempted to promote the SF022 source-only EIH phase-rate kernel into a closed G97-compatible instantaneous release protocol using three separate local recoil/preparation devices `D_A,D_B,D_C`.

## Pure source sector

The all-body EIH law contains the same pure-source `ABC` triple as SF022, so the source contribution itself is unchanged:

`dot(chi_source) = -(G^2 m_A m_B m_C/(hbar c^2)) Delta3 F_ABC`.

The issue is whether all branch-dependent apparatus terms vanish in the preregistered large-separation limit.

## Apparatus-containing source/device triples

A distinct triple containing two sources and one distant device has geometric factor of the form

`F_ABD = 1/(r_AB r_AD) + 1/(r_AB r_BD) + 1/(r_AD r_BD)`.

For source separation `r_AB = O(d)` and device distances `r_AD,r_BD = O(R)`,

`F_ABD = O(1/(d R)) + O(1/R^2)`.

Thus such terms do decouple for fixed finite device mass as `R/d -> infinity`.

Triples with one source and two mutually distant devices likewise contain large-distance factors and can decouple when all relevant device separations scale with the decoupling parameter.

## Decisive preregistered-protocol defect: three-device triple

The frozen SF023 architecture contains **three branch-dependent devices**.

The all-body 1PN law therefore also contains a genuine `D_A D_B D_C` three-body term. Its branch labels are inherited locally from the three source preparation bits, so it can contribute to `Delta_A Delta_B Delta_C` even if all source-device distances are taken large.

Crucially, the preregistration required only that each device be far from the source interaction region. It did **not** require the mutual distances

`r_DA,DB`, `r_DA,DC`, `r_DB,DC`

to scale to infinity.

If the three devices are transported far away as a finite-size apparatus cluster, their mutual EIH triple interaction remains finite and can carry a connected three-bit phase rate unrelated to the desired source `ABC` kernel.

Therefore the frozen statement

`every apparatus-containing connected term -> 0 as R_X/d -> infinity`

is not proven and is false for the allowed clustered-device geometry.

Classification:

`APPARATUS_CONNECTED_CONTRIBUTION_REMAINS_POSSIBLE_AT_LEADING_ORDER_IN_FROZEN_SF023_PROTOCOL`.

## Gauge/boundary control defect

SF023 also froze a simple total-derivative control based on vanishing source velocities. But the three recoil devices are allowed to carry branch-dependent recoil velocities at release.

For a total time derivative of a configuration-space generating function,

`dF/dt = Sum_I (partial F/partial q_I) dot(q_I)`,

apparatus velocities can therefore produce branch-dependent boundary-phase rates even when the sources themselves are instantaneously at rest.

This does not show that the physical connected observable is gauge dependent. It shows that the **frozen SF023 control is too weak** to prove representation independence for the complete branch-dependent system.

Classification:

`CONNECTED_KERNEL_GAUGE_PROMOTION_BLOCKED_BY_NONZERO_APPARATUS_RELEASE_VELOCITIES_IN_FROZEN_PROTOCOL`.

## Controls

C1 (branch-independent apparatus) would remove apparatus finite differences, but it is not the actual G97 recoil preparation and cannot rescue the frozen protocol.

C2 (large source-device distance) suppresses mixed source-device triples but does not suppress a finite-size three-device cluster.

C3/C4 remain valid only after an adequate apparatus-decoupling construction is supplied.

## Terminal decision

SF023 does **not** promote SF022 to a closed laboratory result.

Record both frozen blockers:

`APPARATUS_CONNECTED_CONTRIBUTION_REMAINS_AT_LEADING_ORDER_POSSIBLE`

and

`CONNECTED_KERNEL_GAUGE_PROMOTION_BLOCKED`.

This is `BLOCKED`, not a failure of the RHPI/ADM connected kernel.

## New scientific finding

G97 closure must be enforced not only in momentum bookkeeping but also in the **connected gravitational interaction graph**. Multiple branch-record apparatus bodies can themselves form a connected three-source proxy and contaminate exactly the Möbius/finite-difference channel intended to isolate gravitational source nonlinearity.

This is a useful general design constraint:

> a three-source connected observable requires apparatus topology whose own branch-dependent gravitational interactions cannot form an unsuppressed three-bit connected cluster.

## Prospectively admissible repair

The cleanest next protocol uses **one common finite-mass recoil/reference apparatus** `D` rather than three mutually interacting branch-record devices.

At the release instant:

- all sources and `D` are at rest;
- `D` has branch-dependent position fixed by exact total center-of-mass closure;
- `D` is a distance `R >> d` from the source interaction region;
- there is no pure three-device triple sector;
- all source-device interactions contain at least one large distance;
- zero velocities strengthen the total-derivative boundary control.

This repair must be preregistered as a new gate; it is not applied retroactively to SF023.
