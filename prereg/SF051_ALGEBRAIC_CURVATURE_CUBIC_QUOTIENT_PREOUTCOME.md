# SF051 — algebraic curvature-cubic redundant quotient — PREOUTCOME

Date: 2026-09-15
Status: PROSPECTIVE
Inherited SF050 recovery head: `3d41ea7456cb2a83d1c68f4d5c7ad5d8ba8faf3a`.

## Gate

`SF051_ALGEBRAIC_CURVATURE_CUBIC_QUOTIENT_PREOUTCOME_GATE`.

## Question

Within the six-derivative **algebraic curvature-cubic** sector around flat space, can the Euclidean TT C3 tensor be explicitly quotiented against the Ricci/EOM-redundant cubic tensors using an exact finite Gram construction at the frozen real symmetric point?

This gate does not include derivative-redundant operators such as curvature-Laplacian structures and therefore cannot close the full SF050 essential quotient by itself.

## Frozen kinematics

Use exactly the SF050 real Euclidean symmetric point:

`p_i^2=1`,

`p_i.p_j=-1/2` for `i != j`,

`p1+p2+p3=0`.

Use the same orthonormal five-dimensional transverse-traceless symmetric tensor basis on each external leg.

## Frozen operator basis

Essential target:

`O_E = C_{rho sigma}^{mu nu} C_{mu nu}^{alpha beta} C_{alpha beta}^{rho sigma}`.

Redundant algebraic curvature-cubic controls, using the traceless Ricci tensor `S_mu nu`:

`O_R1 = S_mu^nu S_nu^rho S_rho^mu`.

`O_R2 = S^{mu nu} S^{rho sigma} C_{mu rho nu sigma}`.

Scalar-containing algebraic controls:

`R^3`, `R S_mu nu S^{mu nu}`, `R C_mu nu rho sigma C^{mu nu rho sigma}`.

For linearized TT external legs around flat space, the scalar controls are prospectively expected to vanish at the pure `curvature^(1)^3` cubic level because `R^(1)=0`. This is a frozen zero-control, not a post-result interpretation.

## Frozen calculations

1. Construct the exact symmetrized cubic TT tensors `T_E`, `T_R1`, `T_R2` from three linearized curvature factors.
2. Verify scalar-R controls vanish in the declared linearized-curvature cubic sector.
3. Compute the exact Gram matrix of `[T_E,T_R1,T_R2]` over all `5^3` TT basis triples.
4. Determine the rank of the redundant sub-Gram matrix `[T_R1,T_R2]`.
5. If full rank, construct

`T_E_perp = T_E - T_a (G_R^-1)^{ab}<T_b,T_E>`.

6. Compute exact `||T_E_perp||^2`, its overlap with each redundant tensor, and the response of the normalized projector

`P_E_alg[Gamma]=<T_E_perp,Gamma>/<T_E_perp,T_E>`

to unit `T_E`, `T_R1`, `T_R2`.

## Frozen controls

C1. Unit target response must be exactly 1 if the quotient is well-defined.

C2. Responses to `T_R1` and `T_R2` must be exactly 0.

C3. Redundant subspace rank must be reported; rank deficiency is not repaired post hoc by deleting an operator.

C4. Scalar-R cubic controls must be reported as zero/nonzero exactly in the declared linearized-curvature sector.

C5. No derivative-redundant operator is claimed covered.

C6. No background/fluctuation equality or physical matching coefficient may be inferred.

## Decision rule

### PASS_ALGEBRAIC_QUOTIENT_SCOPED

Requires a nonzero `T_E_perp`, exact null response to the full frozen redundant algebraic subspace, and exact unit response to `T_E`.

### DEGENERATE_ALGEBRAIC_SUBSPACE

Use if the frozen redundant tensors are linearly dependent in the frozen TT/kinematic domain in a way that prevents a unique quotient there.

### BLOCKED_IMPLEMENTATION

Use if the frozen tensors cannot be constructed unambiguously.

### FAIL

Use only if the essential target lies entirely inside the frozen redundant algebraic subspace.

## Interpretation ceiling

A PASS establishes only an exact projector in the frozen algebraic curvature-cubic TT subspace. It does not cover derivative redundancies, does not compute an FRG flow, does not establish split/Nielsen closure, does not select physical SF025 `b`, and does not establish regulator independence or quantum gravity.
