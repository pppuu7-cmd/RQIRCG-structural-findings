# SF022 — RHPI/ADM 1PN connected three-source phase-rate kernel — PREREGISTRATION

Date: 2026-09-14
Status: **FROZEN BEFORE BRANCH FINITE-DIFFERENCE EVALUATION**

## Provenance note

SF021 prospectively selected RHPI-S as the scoped classical gravitational-law principle before any `chi_ABC` computation.

After selection, standard 1PN N-body dynamics was inspected to identify the first conservative order containing a genuine three-body term. SF022 is therefore **not literature-blind with respect to the existence of the EIH 1PN term**, but the branch finite-difference outcome, its exact coefficient for the frozen control geometry, and all connected classifications below are frozen before evaluation.

This is scientifically admissible because the theory/principle selection was already terminalized independently of the connected outcome.

## Scope

SF022 computes only a **point-source conservative connected phase-rate kernel** of the selected classical law.

It is not yet the complete G97 closed-apparatus laboratory prediction. Holding/preparation/support stresses and finite-size source matching are deferred to SF023+ and may add prospectively calculable terms.

## Frozen theory reduction

Use the standard Einstein-Infeld-Hoffmann 1PN N-body Lagrangian representative

`L = L_N + c^-2 L_1PN + O(c^-4)`

with

`L_N = (1/2) Sum_A m_A v_A^2 + (G/2) Sum_A Sum_{B!=A} m_A m_B / r_AB`,

and

`L_1PN = (1/8) Sum_A m_A v_A^4`
` - (G/4) Sum_A Sum_{B!=A} (m_A m_B/r_AB)[7 v_A.v_B + (n_AB.v_A)(n_AB.v_B)]`
` + (3G/2) Sum_A Sum_{B!=A} (m_A m_B/r_AB) v_A^2`
` - (G^2/2) Sum_A Sum_{B!=A} Sum_{C!=A} m_A m_B m_C/(r_AB r_AC)`.

The point-source self divergences are understood as already removed/renormalized in the standard EIH reduction. Terms with `B=C` are retained as ordinary two-body 1PN terms; terms with all three labels distinct contain the genuine three-body conservative interaction.

Representative external authority: the standard EIH N-body formula as reproduced in modern 1PN N-body literature.

## Frozen branch configuration

Use exactly three point sources `A,B,C`, with fixed masses `m_A,m_B,m_C` independent of branch.

Each source has a binary relational position:

`x_A(a)`, `x_B(b)`, `x_C(c)`, with `a,b,c in {0,1}`.

At the instant where the conservative phase-rate kernel is evaluated, freeze

`v_A = v_B = v_C = 0`.

This is an instantaneous Hamiltonian/Lagrangian kernel diagnostic. It does not assert that three isolated masses can remain static for a finite interval without support.

## Frozen phase-rate convention

For a branch with conservative interaction energy `V_abc`, use the inherited weak-field phase convention

`dot(phi_abc) = - V_abc / hbar`.

Define

`dot(chi_ABC) = Delta_A Delta_B Delta_C dot(phi)`

with explicit sign convention

`Delta_A Delta_B Delta_C f = f_111 - f_110 - f_101 - f_011 + f_100 + f_010 + f_001 - f_000`.

No phase normalization may be introduced after evaluation.

## Frozen order bookkeeping

Evaluate separately:

1. Newtonian `O(G)` pair potential;
2. static 1PN `O(G^2/c^2)` terms with repeated source labels (`B=C` etc.);
3. static 1PN `O(G^2/c^2)` terms with three distinct source labels.

Promotion to a genuine connected kernel requires:

- sectors 1 and 2 have exact third finite difference zero;
- sector 3 yields a branch function not reducible to constant/one-body/two-body terms and can be nonzero for the frozen positive-control geometry.

## Frozen general three-body candidate function

For three distinct sources, after collecting ordered EIH terms but **before evaluating the branch finite difference**, define the candidate geometric function

`F_ABC(a,b,c) =`
` 1/[r_AB(a,b) r_AC(a,c)]`
`+1/[r_AB(a,b) r_BC(b,c)]`
`+1/[r_AC(a,c) r_BC(b,c)]`.

The corresponding candidate 1PN triple interaction energy is to be derived from the frozen EIH ordered sums; its overall coefficient/sign must be checked rather than assumed from this notation.

## Exact positive-control geometry

To calibrate the finite-difference algebra independently of physical units, freeze a one-dimensional ordered geometry in arbitrary length unit `ell`:

- `x_A(0)=0 ell`, `x_A(1)=1 ell`;
- `x_B(0)=3 ell`, `x_B(1)=4 ell`;
- `x_C(0)=8 ell`, `x_C(1)=10 ell`.

All masses are nonzero and held symbolically. The exact rational value of

`Delta_A Delta_B Delta_C F_ABC`

for this geometry is **not evaluated in the preregistration**.

## Negative controls

N1. Set `x_A(1)=x_A(0)` while leaving B,C unchanged. Then a genuine third finite difference must vanish.

N2. Replace the 1PN branch energy by an arbitrary constant + one-body + pairwise function. The third finite difference must vanish identically.

N3. Set `G=0`. The connected gravitational phase rate must vanish.

## Gauge / representation ceiling

The EIH potential is a standard coordinate/canonical representative of the 1PN conservative dynamics. SF022 may establish a **derived connected kernel in that prospectively frozen representative**.

It may not yet claim full gauge-invariant laboratory observability. SF023 must embed the kernel into a closed relational branch history and audit canonical/total-derivative boundary effects plus apparatus/support contributions.

## Pass labels

If the EIH distinct-three-body term yields a fixed nonzero generic connected kernel with no free coefficient:

`RHPI_ADM_DERIVES_PARAMETER_FREE_1PN_CONNECTED_THREE_SOURCE_KERNEL_SCOPED`.

If the third finite difference vanishes identically after exact collection:

`RHPI_ADM_1PN_CONNECTED_THREE_SOURCE_KERNEL_ZERO_SCOPED`.

Either outcome is accepted; no criterion may be changed after evaluation.
