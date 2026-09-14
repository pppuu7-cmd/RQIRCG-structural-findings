# SF024 — single-recoil-apparatus closed release-limit gate — TERMINAL

Date: 2026-09-14
Status: **TERMINAL / ASYMPTOTIC CLOSED RELEASE-LIMIT PASS / no finite-time claim**

Preregistration: `657bb30be18ea6bf92e1198df69714b3eb3c1951`.

## Outcome

`SINGLE_RECOIL_G97_RELEASE_LIMIT_RECOVERS_SF022_CONNECTED_KERNEL_SCOPED`.

The result is asymptotic in apparatus distance and applies to the instantaneous post-release phase rate.

## Closed COM preparation

With one finite-mass apparatus `D`, exact total center-of-mass closure makes its branch displacement an affine function of the source branch displacements:

`delta x_D(a,b,c) = -(m_A delta x_A(a)+m_B delta x_B(b)+m_C delta x_C(c))/M`

up to a branch-independent reference translation.

At release all four bodies are at rest, so the total momentum is exactly zero in every branch and no holding force remains active at `t=0+`.

The apparatus may be placed at relational distance `R` from the source triangle while its branch displacement remains finite, `O(d)` times finite mass ratios, independent of `R`.

## General large-R lemma

For a source-device separation

`r_XD = |R e + y_X(a,b,c)|`

with `y_X=O(d)` and bounded branch offsets, the inverse distance has an analytic multipole expansion for sufficiently large `R`:

`1/r_XD = R^-1 + R^-2 P_1(y_X) + R^-3 P_2(y_X) + R^-4 P_3(y_X)+...`,

where `P_n` is degree `n` in the bounded displacement components.

Because `y_X(a,b,c)` is affine in the three binary branch variables, the third Boolean finite difference annihilates every term of branch degree <=2.

Therefore

`Delta_A Delta_B Delta_C (1/r_XD) = O(d^3/R^4)`.

Likewise

`Delta_A Delta_B Delta_C (1/r_XD^2) = O(d^3/R^5)`.

This immediately controls Newtonian apparatus pairs and repeated-label 1PN apparatus sectors.

## Newtonian apparatus contamination

A source-apparatus Newtonian term is

`V_XD^N = -G m_X M/r_XD`.

Although `x_D(a,b,c)` contains all three source bits through COM closure, its connected third finite difference is suppressed as

`Delta3 V_XD^N = O(G m_X M d^3/R^4)`

with additional finite mass-ratio factors from the COM displacement.

Thus the apparatus can generate a finite-R connected Newtonian contamination, but it vanishes as `R -> infinity` without taking `M` to zero or infinity.

This is an important practical warning: at finite `R`, an `O(G)` apparatus contaminant can dominate the much smaller `O(G^2/c^2)` source kernel unless the geometry is designed/calibrated accordingly.

## Mixed 1PN source-source-apparatus triples

Consider the distinct triple `A,B,D`. Its EIH geometric factor is

`F_ABD = 1/(r_AB r_AD) + 1/(r_AB r_BD) + 1/(r_AD r_BD)`.

The leading `R^-1/r_AB` terms contain at most the `A,B` branch bits if the apparatus inverse distance is replaced by its branch-independent leading `R^-1`; their third finite difference is zero.

The first `C` dependence enters through the COM-induced displacement of `D`:

`Delta_C x_D = -(m_C/M) Delta_C x_C`.

Hence

`Delta_C(1/r_AD) = O((m_C/M)d/R^2)`.

Multiplying by the EIH mass coefficient `m_A m_B M` cancels the apparatus mass in the leading connected scaling. Therefore the mixed triple contribution has the generic behavior

`Delta3 V_ABD^(1PN) = O(G^2 m_A m_B m_C/(c^2 R^2))`

up to dimensionless geometry/mass-ratio factors.

The same result holds for `ACD` and `BCD`.

The pure-source term remains

`Delta3 V_ABC^(1PN) = O(G^2 m_A m_B m_C/(c^2 d^2))`.

Thus the leading mixed-triple ratio is

`Delta3 V_mixed / Delta3 V_source = O((d/R)^2)`.

This is the dominant apparatus decoupling law in the frozen single-recoil topology.

## No pure apparatus connected triple

Unlike SF023, the frozen apparatus sector contains only one body `D`.

There is therefore no distinct `D_A D_B D_C` EIH triple capable of retaining a finite connected apparatus phase when the apparatus is moved far away.

This topological change is the essential repair.

## Kinetic sector

All source and apparatus velocities vanish at the release instant. The explicit velocity-dependent 1PN terms therefore vanish exactly at `t=0+`.

No recoil-velocity boundary term is present in this instantaneous gate.

## Gauge / canonical audit

### G1 — total configuration derivative

For any time-independent configuration-space total derivative,

`dF(q)/dt = Sum_I grad_I F . v_I`.

All four velocities vanish at release, so its instantaneous contribution is exactly zero.

### G2 — contact/canonical representation

Post-Newtonian harmonic-coordinate Lagrangians and ADM Hamiltonians are known to be related, order by order, by contact/canonical transformations when the dynamical variables are transformed consistently. The literature establishes physical equivalence between such PN representations.

The SF024 physical object is therefore defined as the **conserved all-body energy / phase rate at corresponding relational initial data**, not as one named coordinate term in a particular potential decomposition.

Under a time-independent canonical transformation `T`,

`H'(Q,P) = H(T^-1(Q,P))`,

so the numerical energy assigned to the same physical phase-space point is unchanged after the relational data are mapped consistently.

This does not mean that individual pair/triple terms are separately gauge invariant. The promoted object is their full all-body energy finite difference.

Classification:

`PASS_CANONICAL_REPRESENTATIVE_EQUIVALENCE_FOR_FULL_RELEASE_ENERGY_SCOPED`.

### G3 — relational far reference

Only source-apparatus separations enter the calculation. Taking `R -> infinity` removes apparatus interactions while leaving fixed source-source relational separations `r_AB,r_AC,r_BC`. No absolute-coordinate observable is introduced.

Classification:

`PASS_RELATIONAL_APPARATUS_DECOUPLING_LIMIT`.

## Frozen controls

C1. Decoupling uses finite arbitrary `M`; no `M=0` or `M=infinity` assumption is required.

C2. If one source branch displacement is removed, the pure-source SF022 finite difference vanishes and all remaining apparatus contributions vanish in the decoupling limit.

C3. Every gravitational contribution vanishes for `G->0`.

C4. A branch-independent apparatus position gives exact zero Newtonian apparatus third difference, as expected; the physical COM-closed branch dependence merely converts this exact null into the asymptotically suppressed terms above.

## Terminal formula

In the single-recoil closed-release limit,

`dot(chi_total)(0+) = dot(chi_SF022)(0+)`
` + O(G * apparatus_branch_multipoles/R^4)`
` + O(G^2 m_A m_B m_C/(hbar c^2 R^2))`
` + higher orders`,

where the precise finite-R coefficients depend on the prospectively specified apparatus geometry.

Therefore

`lim_(R/d -> infinity) dot(chi_total)(0+)`
` = -(G^2 m_A m_B m_C/(hbar c^2)) Delta3 F_ABC`.

For the frozen SF022 rational control geometry,

`lim dot(chi_total)(0+) = -13 G^2 m_A m_B m_C/(2520 hbar c^2 ell^2)`.

No connected gravitational coefficient is fitted.

## Scientific classification

`G97_CLOSED_RELEASE_LIMIT_RECOVERS_RHPI_1PN_CONNECTED_KERNEL_SCOPED`.

This is the first closed-preparation-compatible asymptotic connected phase-rate result in the structural-findings branch.

## Claim ceiling

The result remains deliberately narrow:

- instantaneous post-release phase rate, not finite interaction time;
- asymptotic apparatus decoupling, not an engineering design at finite `R`;
- point-source leading order;
- conservative 1PN sector;
- no radiation reaction;
- no quantum gravitational noise prediction;
- no experimental feasibility claim;
- no new-physics claim, because the selected classical law converged to the ADM/Einstein class.

## Exact next research direction

The next gate should convert the instantaneous result into a **finite-time closed-history observable** without hidden support:

1. choose a prospectively frozen released/free or pulse-controlled branch trajectory;
2. include all EIH velocity and trajectory-response terms consistently to `O(G^2/c^2)`;
3. integrate the full action/phase over the closed protocol;
4. retain apparatus terms at finite `R` or define an experimentally meaningful subtraction/calibration;
5. verify that source finite-size/tidal corrections enter at a controlled higher order for the chosen scale hierarchy;
6. only then compare the derived connected signal against classical GR, semiclassical gravity and EFT comparators.
