# SF026 - finite-time pairwise-null pullback and boundary audit - PREREGISTRATION

Date: 2026-09-14
Inherited frontier: SF024 at b588d8e47c24c6bc12976d54f0a976dc9df099d3.
Status: PROSPECTIVE; an independent classical continuation gate, not new principle selection.

## Question
SF024 leaves finite-time histories open. The inherited pairwise-null theorem applies to functions depending on at most two independently assigned source bits/histories. Does this null survive pulling the action back along self-consistent, mutually interacting source trajectories? Can an open propagation action be promoted to an observed phase without endpoint/readout data?

This is a theorem-level baseline/protocol audit, not an attempt to fit the selected law or to calculate an unspecified experimental chi_ABC.

## Frozen physical model and scope
Use the Newtonian controlled limit of the selected classical law, with L=dot(q)^T M dot(q)/2 - V(q), a positive constant mass matrix and smooth pairwise potential on a collision-free region. Specialize the physical witness to V=-G sum_{i<j}m_i m_j/r_ij. All velocities vanish at release. Consider small positive T with trajectories remaining collision-free; derive rather than guess the first feedback correction to the propagation action. No static holding support is present.

Compare with prescribed factorized paths as a negative control. As a separate boundary-value control, consider the principal action with q(0)=q(T)=q0. This control need not have zero initial velocity and MUST NOT be represented as the same release experiment.

## Frozen exact geometry
For a,b,c in {0,1}, set q_A=a ell, q_B=(4+2b)ell, q_C=(10+3c)ell. The exact third difference of the trajectory-feedback term is not evaluated at registration. Source masses are equal to m for the rational control; the general derivation retains arbitrary positive masses.

For closed Newtonian COM bookkeeping include one finite-mass apparatus D at q_D=R-(m/M)(a+2b+3c)ell with zero initial velocity. This makes total COM branch-independent. Analyze R->infinity at fixed finite M before invoking a source-only result. M=5m may be used as an exact control, not an assumption needed by the theorem. No finite-R or 1PN preparation claim is inferred from Newtonian COM alone.

## Targets
1. Derive short-time released-trajectory action, including motion feedback, rather than integrating V at fixed positions.
2. Determine whether products of pair forces sharing a body generate a three-label function without a three-body term in the original Hamiltonian.
3. Test the frozen geometry exactly using rational arithmetic; no geometry scan or post-outcome replacement.
4. Derive the same-order coincident-endpoint principal-action coefficient and distinguish its boundary data.
5. Audit L -> L+dF/dt together with endpoint states/readouts. Boundary terms in an open action do not establish a gauge-dependent physical observable; dropping the accompanying state/readout transformation is invalid.
6. State a minimal complete amplitude/readout contract for a finite-time experiment, including all prepared branch-conditioned apparatus states and final measurement/recombination.

## Controls
- Independently prescribed pairwise paths: exact third difference zero.
- Remove one branch displacement, including its COM compensation: exact zero.
- G=0: zero gravitational feedback.
- Pure quadratic/harmonic pair action: verify the special low-degree null rather than claiming every pair model violates it.
- Constant-force and/or Hamilton-Jacobi short-time control for action signs and coefficients.
- Exact initial total momentum and branch-independent Newtonian COM.
- Optional numerical trajectory/action convergence tests validate asymptotics only; no precision claim from a single fitted point.
- SF022 frozen algebra may be rerun as regression, without changing its interpretation.

## Classifications
PAIRWISE_NULL_STABLE_UNDER_FROZEN_HISTORY_PULLBACK_SCOPED only with a proof.
PAIRWISE_NULL_NOT_STABLE_UNDER_SELF_CONSISTENT_HISTORY_PULLBACK_SCOPED if an exact counterexample is derived.
FINITE_TIME_OBSERVABLE_BLOCKED_PENDING_BOUNDARY_COMPLETE_PROTOCOL if the record lacks the preparation/recombination/readout map needed for an observable.
INVALID if an open action is called measured chi_ABC, if the fixed-endpoint control is confused with zero-velocity release, or if a new coefficient/geometry is chosen after the outcome.

## Claim ceiling and embargo
SF026 may evaluate connected finite differences of a preregistered classical baseline/action diagnostic after SF021's classical selection. It may not predict a quantum chi_ABC, claim a closed measured finite-time phase, infer new gravity from a nonzero connected baseline, or reinterpret instantaneous SF024 as a finite-time certificate. The original pairwise theorem is retained with its actual factorized-history premise. No new fundamental principle or quantum construction is adopted.
