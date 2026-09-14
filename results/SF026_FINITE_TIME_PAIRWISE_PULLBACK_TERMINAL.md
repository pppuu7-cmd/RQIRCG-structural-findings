# SF026 - finite-time pairwise-null pullback and endpoint audit - TERMINAL

Date: 2026-09-14
Preregistration: `3a495200aa2e9afaf1c3f56f887a0b40fa810cb9`.
Inherited frontier: SF024, `b588d8e47c24c6bc12976d54f0a976dc9df099d3`.

## RESULT / CLASSIFICATION

`PAIRWISE_NULL_NOT_STABLE_UNDER_SELF_CONSISTENT_HISTORY_PULLBACK_SCOPED`.

`FINITE_TIME_OBSERVABLE_BLOCKED_PENDING_BOUNDARY_COMPLETE_PROTOCOL`.

An exactly pairwise Newtonian potential produces a connected three-label contribution to the classical action evaluated on mutually interacting released trajectories. This is a source-motion effect, not a new three-body gravitational vertex. The derived action is NOT, by itself, a measured chi_ABC. The original pairwise-null theorem remains correct for independently prescribed factorized histories.

## STATE_READ / TARGET / PROVENANCE

SF024 left a finite-time closed-history gate. SF022's fixed-position static pair null and exact rational kernel were read and independently regressed. The law is not being selected in SF026: it is the controlled Newtonian limit of the class selected in SF021. Geometry and classification criteria were committed before the branch calculation. The possibility of feedback was the motivation, not an outcome-blind physical-principle contest.

## PHYSICAL_OBJECTS / STATE_AND_BOUNDARY_DATA

Consider N classical bodies in a collision-free region, with positive constant mass matrix M and

`L(q,qdot)=qdot^T M qdot/2 - V(q)`.

For gravity, `V=-G sum_{i<j}m_i m_j/|q_i-q_j|`. The released problem fixes `q(0)=q0` and `qdot(0)=0`. It does not prescribe the final point. The distinct return-endpoint control fixes `q(0)=q(T)=q0`, and its initial velocity is generally nonzero. Confusing these boundary problems is explicitly invalid.

Let `g=grad V(q0)` and

`A(q0)=g^T M^{-1}g=sum_i |F_i(q0)|^2/m_i`.

A is nonnegative as a full force norm, although an isolated three-label cross term within it need not be positive.

## DERIVED RESULT 1 - RELEASED ACTION

Newton's equation is `M qddot=-grad V(q)`. Time reversal of the initial-rest solution gives an even trajectory, locally:

`q(t)=q0-(1/2)M^{-1}g t^2+O(t^4)`.

Consequently

`K(t)=(1/2)A t^2+O(t^4)`,

`V(q(t))=V(q0)-(1/2)A t^2+O(t^4)`.

Integrating the full Lagrangian, rather than only a frozen potential, yields

`S_release(q0,T)=-V(q0) T+(1/3)A(q0) T^3+O(T^5)`.

This coefficient is fixed by the original pairwise dynamics. There is no adjustable connected coupling.

For a smooth potential the remainders are uniform on a compact collision-free neighborhood and for sufficiently small T. A useful control condition is `T^2 ||M^{-1} Hess V|| << 1`, together with displacement much smaller than the minimum separation. This is a short-time statement, not a bound valid through a close encounter.

## DERIVED RESULT 2 - WHY A THIRD LABEL APPEARS

With independent prescribed paths `q_i=q_i(s_i,t)`, every kinetic term depends on one bit and every pair interaction on at most two. Integrating over t preserves this degree, so `Delta3 S=0` exactly.

But the self-consistent solution is `q_i=q_i(s_A,s_B,s_C,t)`. Composition with this solution map does not preserve the subspace of functions involving at most two bits. In A, the cross product `F_ij dot F_ik` already involves three bodies. For three sources the distinct-label contribution is

`A_ABC = 2 G^2 m_A m_B m_C sum_cyclic_i [(q_i-q_j) dot (q_i-q_k)]/(r_ij^3 r_ik^3)`.

The squared single-pair force terms still have zero third difference for independent initial source positions. Therefore `Delta3 A=Delta3 A_ABC` in the source-only limit.

For ordered collinear positions, let `u=q_B-q_A>0`, `v=q_C-q_B>0`. Direct reduction gives

`A_ABC = -4 G^2 m_A m_B m_C/[u v (u+v)^2]`.

The minus sign does not violate positivity of A; it is a cross term in a sum of squares.

## EXACT FROZEN COUNTEREXAMPLE

Use the preregistered equal-mass branches

`q_A=a ell`, `q_B=(4+2b)ell`, `q_C=(10+3c)ell`, with a,b,c in {0,1}.

Use `Delta3 f=f111-f110-f101-f011+f100+f010+f001-f000`.

Exact rational arithmetic yields

`Delta3 V_N = 0`,

`Delta3 A = -(82/616005) G^2 m^3/ell^4`,

hence

`Delta3 S_release = -(82/1848015) (G^2 m^3/ell^4) T^3+O(T^5)`.

This is a counterexample to preserving the pairwise null AFTER trajectory elimination. It is not a counterexample to the original factorized-history theorem, and it is not a claim about the observed phase of an unspecified instrument.

## DERIVED RESULT 3 - DIFFERENT ENDPOINT DATA GIVE A DIFFERENT COEFFICIENT

For the short return path with q(0)=q(T)=q0, the leading trajectory is

`q(t)=q0+(1/2)M^{-1}g t(T-t)+O(T^4)`.

The kinetic correction integrates to `A T^3/24`; the potential-displacement correction integrates to `-A T^3/12`. Thus

`S_return(q0,q0;T)=-V(q0)T-(1/24)A(q0)T^3+O(T^5)`.

For the same initial-position cube, the connected coefficient is now

`Delta3 S_return = +(41/7392060)(G^2 m^3/ell^4)T^3+O(T^5)`.

These opposite signs are NOT two predictions for one experiment. The boundary conditions differ. The return problem requires initial velocity `(1/2)M^{-1}g T+O(T^3)`, not zero. Both coefficients are reproduced by an exact constant-force calculation.

A further analytical check uses Hamilton-Jacobi evolution from constant initial phase: `S_HJ(q,T)=-V(q)T-A(q)T^3/6+O(T^5)` at fixed final q. Evaluating it at the released final position adds `+A T^3/2` from the leading potential and recovers `+A T^3/3`. Fixed-coordinate phase and action along a moving endpoint must not be conflated.

## CLOSED APPARATUS CONTROL / CONSERVATION

For equal source masses include one finite M apparatus at

`q_D=R-(m/M)(a+2b+3c)ell`.

All initial velocities vanish. The total mass-weighted initial position is `14 m ell+M R`, independent of bits, and total momentum is zero. This verifies Newtonian COM bookkeeping exactly. It does NOT independently certify a relativistic preparation, a 1PN center-of-energy constraint, or an experimentally preparable quantum state.

At fixed finite M and bounded source geometry, apparatus forces on sources are O(R^-2), while the source forces remain bounded. Therefore the all-body A approaches the source A, with a sufficient bound `A_total-A_source=O(R^-2)`; the apparatus own force-square contribution is O(R^-4). The finite eight-branch difference commutes with this limit. The nonzero source feedback term consequently survives the same formal distant-apparatus limit rather than being removed by it.

For the fixed illustrative mass M=5m and R/ell=50,100,200, exact rational evaluations approach the source value. Their absolute errors in units G^2 m^3/ell^4 are approximately `5.93e-7, 3.05e-8, 1.74e-9`. These samples are controls, not a fitted proof of an asymptotic exponent. The theorem uses the force bound. No M=0 or infinite-M limit is taken.

Translation invariance gives sum_i F_i=0, and time independence gives conserved total Newtonian energy. Rotational invariance gives angular-momentum conservation in the general vector case. Local existence and uniqueness follow from the smooth collision-free force field. Nonlinear Bianchi/quantum Ward closure is not re-proven by a Newtonian ODE; this is a limit audit only. Nor is the Newtonian instantaneous force used as proof of microscopic relativistic causality.

## BOUNDARY / GAUGE ADVERSARY

For `L'=L+dF(q,t)/dt`,

`S'=S+F(q_f,T)-F(q_i,0)`.

The propagator transforms as

`K'=exp(iF_f/hbar) K exp(-iF_i/hbar)`.

Transforming endpoint states consistently, `psi_i'=exp(iF_i/hbar)psi_i` and `psi_f'=exp(iF_f/hbar)psi_f`, leaves the amplitude `<psi_f|K|psi_i>` unchanged. The same cancellation holds for transformed density matrices and POVMs. A change of an OPEN action without its endpoint states is not a change of physical theory.

This prevents two errors: treating a boundary-dependent open phase as already observable, and treating arbitrary boundary conventions as a fundamental matching parameter. Interferometer treatments explicitly combine propagation, interaction and separation/readout contributions [1]. The atom-interferometer formula is a sanity check, not an imported RQIRCG apparatus design.

## MINIMAL FINITE-TIME OBSERVABLE CONTRACT

The next experiment-level calculation must specify a normalized total initial state; internal, momentum-conserving preparation maps including recoil and control records; the selected all-body evolution to the stated order; final recombination/readout operations; the final POVM; and which apparatus/environment variables are retained or traced out.

For example, the fundamental prediction is a probability

`P(o)=Tr[E_o U_read U(T) U_prep rho_0 U_prep^dag U(T)^dag U_read^dag]`,

with every operation and its source content declared. Extracting eight branch phases is legitimate only if the resulting channel admits the requisite approximately diagonal coherent-phase description. If which-branch records remain or visibility changes, a single phase table is not an adequate parent object.

This contract is theory-independent measurement bookkeeping. It does not fix missing quantum gravitational dynamics, nor does it authorize arbitrary controls chosen to erase an inconvenient connected result.

## INFORMATION_RANK / ABLATION / NEW_STRUCTURAL_FACT

No new law coordinate was introduced or selected in SF026. Once V and the boundary-value problem are fixed, the displayed Taylor coefficients are unique. The unresolved freedom is the operational history/readout map, generally functional control data, not a free gravitational cubic coefficient. It cannot be assigned a finite rank before a protocol family is specified.

Ablation controls isolate the cause: freezing independently prescribed paths restores the null; deleting one bit restores it; G=0 removes it; a purely quadratic pair potential has linear forces and a quadratic A, so its third difference also vanishes for affine branch positions. Therefore the statement is loss of a GENERAL preservation theorem, not a claim that every pair model or every geometry has a nonzero connected action.

The key structural fact is that 'microscopic pairwise interaction' and 'pairwise on-shell branch functional' are not interchangeable. Solving source dynamics can create connected dependence without adding a nonlinear mediator vertex. This must be part of the comparator baseline before assigning a finite-time connected signal to a new law.

As dimensional guidance only, the motion-induced action is of order `G^2 m^3 T^3/d^4`, whereas the static 1PN vertex action is of order `G^2 m^3 T/(c^2 d^2)`. Their ratio scales as `(cT/d)^2`, times geometry factors. This is NOT a measured-phase ratio until all endpoint/control contributions are included.

## COMPUTATIONAL EVIDENCE

Script: `scripts/sf025_sf026_checks.py`, commit `36d3f61f35792177333ada9615983c595b3c9863`, SHA-256 `c9bea62cdb327cf7841959204b9f656163fd71a284f00176361f0a24da3399f8`.
Raw: `results/raw/SF026_CHECKS.json`, commit `91b9aca1bf7477375d3de6dda42a3fda03e15fc0`.

All 14 SF026 checks passed locally; failures=[]. These include exact rational, symbolic and numerical controls; they are not all exact proofs. There were 32 three-body trajectory/action integrations: eight branches at four times. With m=G=ell=1, T=0.4,0.2,0.1,0.05, the computed connected released action divided by its derived leading T^3 term was `1.0274276,1.0067811,1.0016906,1.0004224`. The convergence supports, but does not replace, the analytical expansion. Time is measured in `sqrt(ell^3/(G m))`.

SF022's original finite difference `13/2520` was independently reproduced. No old terminal was overwritten. No GitHub Actions run is claimed.

## WHAT_IS_STILL_NOT_ESTABLISHED / CLAIM_CEILING

No full finite-time 1PN action/readout prediction; no physically measured chi_ABC; no exact quantum channel positivity; no finite-size matching or source-preparation feasibility; no radiation/reaction closure; no GR-versus-semiclassical quantum discrimination; no new physics. The full relativistic gauge interpretation of the older instantaneous claim was not independently re-proven in this Newtonian gate.

Classical diagnostic differences are allowed by the post-SF021 scope; quantum chi_ABC remains uncomputed. A global experimental prediction is blocked until the boundary-complete contract is supplied.

## EXACT_NEXT_ADMISSIBLE_GATE

Preregister one fully specified finite-time closed preparation/recombination/readout model, then propagate the SAME full model under (a) the evolving Newtonian pairwise baseline and (b) the selected 1PN law. Include all velocities, trajectory response, endpoints/control phases, finite-R recoil, source sizes and the common error budget. Subtract observables/probabilities, not a coordinate potential or an open propagation phase. Keep the SF025 quantum-law question separate.

## Primary external sanity check

[1] S. Dimopoulos, P. W. Graham, J. M. Hogan, M. A. Kasevich, General Relativistic Effects in Atom Interferometry, arXiv:0802.4098, especially section II and eq. (70), Phys. Rev. D 78, 042003 (2008). https://arxiv.org/abs/0802.4098

The Taylor/pullback derivations and frozen rational counterexample above were derived in this gate. They are not attributed to [1].
