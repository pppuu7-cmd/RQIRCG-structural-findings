# SF028B — 3D boundary-complete finite-time closed coherence protocol — PREOUTCOME

Date: 2026-09-15
Status: PROSPECTIVE / no SF028 connected coefficient reused
Parent gate: SF028 terminal `INVALID_FROZEN_PROTOCOL_1D_POINT_GAUSSIAN_GRAVITATIONAL_OBJECT_SCOPED`, commit `a654b2590df5fb79b5e499402208c9786d2386ad`.

## Repair boundary

SF028B changes exactly the defective motional object: the normalized motional Hilbert space is now three-dimensional for every body. Branch centers remain collinear and all other protocol choices are inherited unless explicitly restated below.

No connected coefficient obtained during exploratory work on the invalid SF028 object is admissible evidence for SF028B. All substantive coefficients must be recomputed after this preregistration.

## Gate

`SF028B_3D_BOUNDARY_COMPLETE_COHERENCE_PROTOCOL_PREOUTCOME_GATE`

## Frozen bodies and branch centers

Three source masses:

`m_A=m_B=m_C=m`.

Single common recoil/reference body:

`M_D=5m`.

Reference distance:

`R=100 ell`.

All branch centers lie on the x axis:

`q_A(a)=(a ell,0,0)`,

`q_B(b)=((4+2b)ell,0,0)`,

`q_C(c)=((10+3c)ell,0,0)`,

`q_D(a,b,c)=((R/ell-(a+2b+3c)/5)ell,0,0)`.

Thus the branch-dependent total center-of-mass displacement is exactly zero.

## Frozen normalized initial state

Internal branch register:

`|+++>=2^(-3/2) sum_abc |abc>`.

Motional reference state: product of four normalized isotropic real 3D minimum-uncertainty Gaussians with centers

`(0,0,0)`, `(4ell,0,0)`, `(10ell,0,0)`, `(R,0,0)`,

zero mean momenta, and per-Cartesian-coordinate standard deviation

`sigma=ell/100`.

The Gaussian width is fixed before all connected evaluation.

The 3D Newtonian pair singularity is locally integrable on these packets; this domain fact must be verified explicitly before PASS.

## Frozen preparation / recombination

For branch `s=abc`, define the 3D translation

`T_s=exp[-(i/hbar) sum_I delta q_I(s).p_I]`

with branch displacements along x exactly as above.

`U_prep=sum_s |s><s| tensor T_s`.

No holding force acts during free evolution.

After time T:

`U_read=U_prep^dagger`.

Then trace out all four motional systems and perform informationally complete tomography on the three-qubit register.

## Frozen physical readout

For `X in {N,EIH}` define

`K_s^X(T)=rho_q^X(T)[s,000]/sqrt(rho_q^X(T)[s,s]rho_q^X(T)[000,000])`.

Use the continuous logarithm from T=0 while all seven coherences remain nonzero.

Define

`C3^X=Log K_111^X-Log K_110^X-Log K_101^X-Log K_011^X+Log K_100^X+Log K_010^X+Log K_001^X`.

Primary physical outputs:

`Theta3^X=Im C3^X`,

`Gamma3^X=-Re C3^X`.

Same-protocol comparator:

`Delta_1PN Theta3=Theta3^EIH-Theta3^N`.

No open action is the promoted observable.

## Frozen dynamics

### N

Three-dimensional point-particle Newtonian Hamiltonian:

`H_N=sum_I p_I^2/(2m_I)-G sum_{I<J}m_I m_J/|q_I-q_J|`.

### EIH

Use the standard conservative GR 1PN N-body Einstein-Infeld-Hoffmann dynamics for the same four bodies.

At zero initial velocities, the static target sector uses the inherited convention

`V_static^(1PN)=+(G^2/(2c^2)) sum_A sum_{B!=A} sum_{C!=A} m_A m_B m_C/(r_AB r_AC)`.

Velocity-dependent EIH terms must be retained whenever prospective power counting places them at the requested order.

For the quantum readout calculation, only the leading semiclassical/coherent-state expansion is claimed. Any operator-ordering dependence beyond that classical order is an explicit remainder, not candidate physics.

## Frozen expansion parameters and target orders

Define

`tau=T/sqrt(ell^3/(Gm))`,

`eta=sigma/ell=10^-2`,

`epsilon_PN=Gm/(c^2 ell)`.

Target the collision-free local expansion around `tau=0`, `eta<<1`, `epsilon_PN<<1`.

Authoritative terms to retain if present:

1. finite-R Newtonian connected center-potential phase `O(GT)`;
2. Newtonian self-consistent/force-pullback coherence phase through `O(G^2 T^3)`;
3. leading force-distinguishability contribution to `Gamma3` through `O(G^2 sigma^2 T^2/hbar^2)`;
4. EIH-minus-Newtonian connected phase through `O(G^2 T/(hbar c^2))`;
5. any finite-width correction that scales at one of these retained orders.

Higher-order terms must be classified by explicit power counting.

Inherited trajectory-check times `tau=0.05,0.10,0.20` may be used only as convergence controls, never to tune the analytic coefficient.

## Frozen finite-size applicability audit

The dynamical calculation is a point-particle/monopole baseline.

For physical extended-body interpretation freeze nonspinning spherical, nonoverlapping bodies with calibrated total masses and

`r_body <= 10^-3 ell`.

Use primary PN/EFT authority to decide whether internal structure is effaced through the retained 1PN order. If that authority is insufficient for this laboratory-style source class, record

`BLOCKED_FINITE_SIZE_EXTENSION`

while retaining any valid point-particle result.

No finite-size coefficient may be chosen after seeing `Theta3`.

## Controls

C1. Domain: `1/r` and the retained 1PN singular factors have finite expectation on the frozen 3D Gaussian state in the collision-free separated-center regime.

C2. T=0: `K_s=1`, `C3=0`.

C3. G=0: gravitational connected cumulants vanish.

C4. Delete any one source displacement: `C3=0` through every retained gravitational order.

C5. Same-protocol identity: N and EIH use identical state, geometry, apparatus, preparation, T, recombination and tomography.

C6. Formal `R/ell -> infinity` control recovers the source-only coefficients for the same SF026 geometry.

C7. Factorized prescribed pair histories retain the exact pairwise third-difference null; Newtonian connected terms in SF028B must be attributable to finite-R COM apparatus dependence and/or self-consistent force/coherence pullback.

C8. Any canonical/total-derivative representation change receives no credit from an open action; only the reduced qubit coherence is authoritative.

C9. EIH power counting: starting from zero branch momenta, prove whether the velocity-dependent 1PN terms enter or do not enter at `O(G^2 T/c^2)` before omitting them.

## Decision rule

### PASS_WITH_SCOPE

Requires a well-defined 3D normalized protocol, an explicit short-time physical `C3^N`, an explicit same-protocol EIH correction through the frozen order, controls C1-C9, and a declared error/claim ceiling.

### NULL_WITH_SCOPE

If a connected component vanishes after all frozen terms are included, preserve the null.

### BLOCKED

Use BLOCKED for missing EIH-to-coherence map, unresolved finite-size extension, uncontrolled operator ordering at the claimed order, or inability to keep the physical readout separate from an open-action surrogate.

### FAIL

Use FAIL only for a real inconsistency of this frozen 3D protocol or a failed prospective control.

### INVALID

Any post-result change to dimension, state width, geometry, R, M_D, readout, branch combination, order counting or baseline requires a new preregistration.

## Claim ceiling

A successful SF028B can establish only a boundary-complete **known-physics, point-particle, leading-semiclassical, short-time coherence baseline**.

It cannot establish a quantum-gravity law, new three-body vertex, new physics, all-time prediction, laboratory feasibility, historical RCG-002 prediction, or quantum `chi_ABC`.

Retain:

`NONZERO_CONNECTED_SIGNAL != NEW_THREE_BODY_GRAVITATIONAL_VERTEX`.