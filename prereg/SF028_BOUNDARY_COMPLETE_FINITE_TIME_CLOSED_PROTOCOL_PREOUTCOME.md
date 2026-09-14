# SF028 — boundary-complete finite-time closed protocol — PREOUTCOME

Date: 2026-09-15
Status: PROSPECTIVE / outcome unseen for this frozen protocol
Inherited authority: `recovery/CURRENT_FRONT.md` at post-SF027 head `24fb52c7cba15f89629661e02eae7ae9d902a27a`.

## Gate

`SF028_BOUNDARY_COMPLETE_FINITE_TIME_CLOSED_PROTOCOL_PREOUTCOME_GATE`

## Scientific question

Can one define and evaluate a finite-time **physical reduced-coherence observable** for one closed single-recoil apparatus protocol, using exactly the same preparation, free-evolution interval, recombination and readout under:

1. the self-consistent Newtonian all-body baseline; and
2. the selected conservative 1PN/EIH all-body baseline,

without replacing the physical readout by an open propagation action or coordinate potential?

The gate is about a known-physics operational baseline. It does not introduce a successor quantum-gravity matching contribution and does not compute a quantum-gravity `chi_ABC`.

## Frozen system

Work in one spatial dimension with three equal source masses

`m_A=m_B=m_C=m`

and one common recoil/reference body

`M_D=5m`.

The source branch geometry is inherited from the prospectively frozen SF026 counterexample:

`x_A(a)=a ell`,

`x_B(b)=(4+2b) ell`,

`x_C(c)=(10+3c) ell`,

with `a,b,c in {0,1}`.

Freeze the finite apparatus reference distance to the already-used SF026 control value

`R=100 ell`.

Exact center-of-mass closure fixes

`x_D(a,b,c)=R-(m/M_D)(a+2b+3c) ell`

so the total mass-weighted branch displacement is exactly zero.

The ordering `A<B<C<D` is fixed for all eight branches.

## Frozen normalized initial state

Introduce three internal branch qubits with computational basis `|a b c>`.

The internal state before preparation is

`|+++> = 2^(-3/2) sum_{a,b,c}|abc>`.

The motional reference state is a normalized product of real minimum-uncertainty Gaussian packets centered on

`(0,4 ell,10 ell,R)`

with zero mean momenta and common position standard deviation

`sigma=ell/100`.

The Gaussian width is a fixed analytic benchmark, not a fitted experimental parameter. Any finite-width correction that is not controlled at the target order must remain an explicit error term rather than being tuned away.

## Frozen preparation map

Define branch-conditioned translations

`T_abc = exp[-(i/hbar) sum_I delta x_I(abc) p_I]`,

with

`delta x_A=a ell`,
`delta x_B=2b ell`,
`delta x_C=3c ell`,
`delta x_D=-(m/M_D)(a+2b+3c)ell`.

Then

`U_prep = sum_abc |abc><abc| tensor T_abc`.

This unitary leaves every branch mean momentum zero, commutes with total momentum, and preserves the same total center-of-mass mean. The three branch qubits are retained as part of the closed readout record; no branch record is discarded during the free interval.

No holding potential is active during the free interval.

## Frozen dynamics

### Newtonian baseline N

`H_N = sum_I p_I^2/(2m_I) - G sum_{I<J} m_I m_J/r_IJ`.

All four bodies evolve self-consistently.

### 1PN baseline EIH

Use the standard conservative Einstein-Infeld-Hoffmann N-body dynamics through `O(c^-2)` for the same four masses, same initial state and same branch translations.

The zero-velocity static `O(G^2/c^2)` sector is frozen with the convention already used by SF022:

`V_static^(1PN) = +(G^2/(2c^2)) sum_A sum_{B!=A} sum_{C!=A} m_A m_B m_C/(r_AB r_AC)`.

All required velocity-dependent EIH terms must be included if they enter the retained power-counting order. They may not be deleted after seeing the result.

## Frozen recombination and readout

After free evolution for time `T`, apply

`U_read = U_prep^dagger`.

Then trace out all four motional degrees of freedom and retain the three-qubit reduced density matrix `rho_q^X(T)` for baseline `X in {N,EIH}`.

No endpoint projection onto a chosen classical trajectory is performed.

The readout is an informationally complete qubit tomography POVM. Therefore the off-diagonal qubit coherences are physical readout objects rather than open-action surrogates.

For each nonzero branch label `s=abc`, define the normalized reference coherence

`K_s^X(T) = rho_q^X(T)[s,000] / sqrt(rho_q^X(T)[s,s] rho_q^X(T)[000,000])`.

In the short-time domain require all seven `K_s` to remain nonzero.

Define the connected complex coherence cumulant by the continuous logarithm from `T=0`:

`C3^X(T) = Log K_111^X - Log K_110^X - Log K_101^X - Log K_011^X + Log K_100^X + Log K_010^X + Log K_001^X`.

Primary physical outputs:

`Theta3^X(T) = Im C3^X(T)`

and

`Gamma3^X(T) = -Re C3^X(T)`.

The same-protocol 1PN comparator is

`Delta_1PN Theta3(T) = Theta3^EIH(T)-Theta3^N(T)`

and likewise for `Gamma3`.

This definition is fixed before evaluating any connected coefficient.

## Frozen short-time / weak-field target order

Let

`t_G=sqrt(ell^3/(Gm))`, `tau=T/t_G`.

The analytic gate targets the collision-free short-time expansion around `tau=0` and will use inherited control times

`tau = 0.05, 0.10, 0.20`

only as numerical convergence checks if a numerical trajectory control is needed.

Retain:

- Newtonian connected coherence through the first nonzero self-consistent force/trajectory term, expected at or below `O(G^2 T^3)`;
- the EIH-minus-Newtonian connected phase through `O(G^2 T/c^2)`;
- finite-R apparatus contributions at `R=100 ell` rather than replacing them by `R=infinity`;
- finite Gaussian-width terms if they contribute at the same retained order.

Terms proven to be higher order must be displayed in the error budget, not silently omitted.

## Frozen finite-size treatment

The dynamical baseline is the nonspinning monopole/point-particle EIH model. For physical extended-body interpretation, freeze spherical nonoverlapping sources and apparatus with calibrated total masses and radius ceiling

`r_body <= 10^-3 ell`.

A PASS may promote the point-particle/monopole protocol only through 1PN if primary-source authority supports effacement of spinless finite-size structure through the retained order. Otherwise the finite-size extension is `BLOCKED_FINITE_SIZE_MAP` and the terminal claim must remain point-particle only.

No radius or Love-number-like parameter may be tuned after the connected result is known.

## Positive / negative controls

C1. `T=0`: `U_read U_prep=I`, so all `K_s=1` and `C3=0`.

C2. `G=0`: the gravitational contribution to the connected cumulant vanishes.

C3. Delete any one source branch displacement: the third Boolean connected cumulant must vanish.

C4. Same-protocol identity: state, `U_prep`, free time, `U_read`, tomography basis, masses, `R`, `sigma`, and branch geometry are identical in N and EIH.

C5. Apparatus decoupling control: repeating only the analytic coefficient check in the formal `R/ell -> infinity` limit must recover the source-only coefficient appropriate to the **same SF026 geometry**. This is a control, not the primary finite-R prediction.

C6. Independent prescribed-history control: an externally prescribed factorized pairwise history must retain the exact pairwise third-difference null. Any Newtonian connected term in the present protocol must be attributable to the all-body preparation/apparatus or self-consistent dynamics/coherence pullback, not to a new three-body Newtonian vertex.

C7. Boundary/canonical control: no conclusion may be drawn from an isolated open action. Only the reduced qubit coherence after `U_read` may be promoted.

## PASS / FAIL / BLOCKED / INVALID

### PASS_WITH_SCOPE

Requires all of:

1. the normalized closed protocol above is mathematically well defined in a collision-free short-time domain;
2. `K_s` remain nonzero in that domain;
3. an explicit short-time expression for the physical `C3^N` is derived including finite-R apparatus terms at the frozen `R`;
4. the same observable is evaluated under EIH through the frozen target order;
5. all retained velocity/trajectory terms are included according to prospectively fixed power counting;
6. controls C1-C7 pass;
7. the result is reported as a known-physics baseline, not new physics.

### NULL_WITH_SCOPE

If the physical connected cumulant or EIH-minus-N comparator is zero through the retained order after all terms and controls are included, record the null. Do not modify the readout or geometry to obtain a nonzero value.

### BLOCKED

Use `BLOCKED` if a required physical map is missing, including inability to map the full retained EIH dynamics to the reduced coherence at the target order, inability to control the endpoint/readout map, or inability to justify the finite-size extension.

A finite-size blocker may coexist with a point-particle scoped result.

### FAIL

Use scientific FAIL only if the frozen protocol is internally inconsistent (e.g. nonunitary preparation/readout, unavoidable collision in the declared short-time domain, or contradiction among its required physical definitions).

### INVALID

Any post-outcome change to geometry, `R`, apparatus mass, Gaussian width, qubit observable, branch combination, baseline order, or control definition invalidates this gate and requires SF028b/new preregistration.

## Interpretation ceiling

SF028 may establish a finite-time, boundary-complete **known-physics reduced-coherence baseline** in the declared point-particle/semiclassical short-time scope.

It may not establish:

- quantum-gravity matching;
- a successor quantum law;
- a new three-body gravitational vertex;
- `NEW_PHYSICS_FOUND`;
- a full laboratory feasibility claim;
- full finite-size realism beyond the frozen authority;
- exact all-time dynamics;
- a historical RCG-002 prediction;
- quantum `chi_ABC`.

Retain:

`NONZERO_CONNECTED_SIGNAL != NEW_THREE_BODY_GRAVITATIONAL_VERTEX`.

The object `Theta3` may coincide with a phase cumulant in the coherent diagonal limit, but it is defined operationally here from measured reduced coherences rather than assumed to equal an open action.