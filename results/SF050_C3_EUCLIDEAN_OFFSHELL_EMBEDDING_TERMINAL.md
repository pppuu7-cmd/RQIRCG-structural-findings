# SF050 — C3 Euclidean/off-shell embedding — TERMINAL

Date: 2026-09-15
Preregistration: `ae2d3414e87dd1b364a97b69349330267e88faff`.
Exact symbolic control script: `scripts/sf050_tt_gram_check.py`, commit `ba1bac6a1490e75aafce0e16faef9b6272eb2a8d`.
Raw exact result: `results/raw/SF050_TT_GRAM_CHECK.json`, commit `1b8cba99d1f33f596485e5a50d0ad80d6e52b30b`.
Authority/derivation audit: `research_log/SF050_C3_EUCLIDEAN_OFFSHELL_EMBEDDING_AUDIT.md`, commit `e70a049c7f6d14b48ec47ec2a44449c789a7cb75`.

## RESULT / CLASSIFICATION

Primary decision-rule classification:

`PARTIAL_TEMPLATE_ONLY_C3_TEMPLATE_CLOSED_ESSENTIAL_QUOTIENT_OPEN_SCOPED`.

Secondary structural result:

`OFFSHELL_REDUNDANT_DIRECTIONS_MUST_BE_QUOTIENTED_BEFORE_PHYSICAL_C3_FRG_MATCHING_SCOPED`.

Counterexample result:

`NAIVE_SINGLE_TEMPLATE_EUCLIDEAN_C3_PROJECTOR_CONTAMINATED_SCOPED`.

Retain:

`R_ASGS_TRUNCATION=1`.

`R_ASGS_PHYSICAL=UNDEFINED_MAP_NOT_CLOSED`.

No physical SF025 coefficient is selected.

## D1/D2 — explicit cubic C3 template

For

`S_C3 = integral sqrt(g) C_{rho sigma}^{mu nu} C_{mu nu}^{alpha beta} C_{alpha beta}^{rho sigma}`

and

`g = delta + h`,

flat space has `C[delta]=0`. Hence

`C = C^(1)[h] + C^(2)[h,h] + ...`.

At cubic order in h,

`S_C3^(3) = integral C^(1)[h] C^(1)[h] C^(1)[h]`.

The measure correction begins only at `O(h^4)` because `(sqrt(g)-1) C^3 = O(h^4)`. Terms containing `C^(2)` also begin at `O(h^4)`.

Therefore the cubic momentum-space tensor

`T_C3^(3)(p1,p2,p3) = delta^3 S_C3 / [delta h(p1) delta h(p2) delta h(p3)] |_{h=0}`

is fully determined by three linearized Weyl tensors.

It is local, Bose symmetric, linearized-gauge invariant, and homogeneous of momentum degree six.

Verdict:

`C3_EUCLIDEAN_CUBIC_TEMPLATE = CLOSED`.

## D3 — relation to SF049 physical projector

Under Lorentzian/complex on-shell continuation, physical helicity contractions of `T_C3^(3)` reduce to the SF049 structures

`B_+++=[12]^2[23]^2[31]^2`,

`B_---=<12>^2<23>^2<31>^2`.

The SF049 all-plus/all-minus projector therefore remains the physical on-shell quotient target.

Verdict:

`EUCLIDEAN_C3_TEMPLATE_TO_SF049_PHYSICAL_DIRECTION = CLOSED_ALGEBRAIC_SCOPED`.

This is not yet a projected FRG flow.

## D4 — exact off-shell redundancy counterexample

Use the prospectively frozen redundant control

`O_Ric3 = integral sqrt(g) R_mu^nu R_nu^rho R_rho^mu`.

For flat-background transverse-traceless external legs,

`R_mu nu^(1) = -1/2 p^2 h_mu nu`

up to the overall curvature-sign convention.

Thus the Ricci-cubic vertex is nonzero for generic Euclidean off-shell `p_i^2 != 0`, has the same total momentum degree six as C3, but vanishes for physical on-shell Ricci-flat external gravitons.

At the frozen real Euclidean symmetric point

`p_i^2=1`,

`p_i.p_j=-1/2`,

with a five-dimensional orthonormal TT basis on each leg, the exact symbolic Gram values are

`||T_C3||^2 = 95/768`,

`||T_Ric3||^2 = 5/192`,

`<T_C3,T_Ric3> = -35/768`.

Therefore the naive normalized one-template contraction gives

`<T_C3,T_Ric3>/<T_C3,T_C3> = -7/19`.

The overall sign can change with the Riemann convention. The nonzero contamination cannot.

Hence

`KNOWN PHYSICAL C3 DIRECTION + KNOWN EUCLIDEAN C3 TEMPLATE`

does not imply

`SINGLE EUCLIDEAN TEMPLATE CONTRACTION = PHYSICAL C3 PROJECTOR`.

The frozen naive-projector claim is falsified.

## D5 — current dynamical-vertex realization

Current dynamical FRG graviton calculations provide momentum-dependent three- and four-point functions, but the executed tensor ansaetze used in the audited effective-action reconstructions retain primarily Einstein-Hilbert/classical tensor structures and encode omitted higher-curvature effects in momentum-dependent dressings.

This is adequate for their declared lower-curvature reconstruction but does not identify an essential six-derivative C3 coefficient.

Therefore retain:

`MOMENTUM_DEPENDENCE != OPERATOR_IDENTIFICATION`.

`EH_TENSOR_VERTEX_DRESSING != ESSENTIAL_C3_COEFFICIENT`.

## D6 — minimum correct embedding

Let `T_E=T_C3^(3)` and let `{T_a}` span all redundant six-derivative fluctuation tensors relevant to the chosen momentum/vertex domain.

With Gram matrix

`G_AB=<T_A,T_B>`,

a tensor-space quotient can be represented schematically by

`T_E_perp = T_E - T_a (G_R^-1)^{ab} <T_b,T_E>`

provided the redundant sub-Gram matrix is full rank on the declared kinematic family.

Then

`g_E = <T_E_perp,Gamma^(3)>/<T_E_perp,T_E>`

is an essentialized tensor coefficient in that declared space.

This construction is only a kinematic realization of the quotient. A physical FRG flow must additionally implement the scale-dependent field redefinitions / split-Nielsen identities that define the essential scheme and must establish Lorentzian/on-shell matching.

A single symmetric point is insufficient unless rank completeness is proven; a multi-kinematic family may be required.

## Decision rule

The preregistered strong PASS is not satisfied because the complete redundant quotient and its dynamical-flow implementation are not closed.

BLOCKED is too strong because the explicit C3 tensor template and its physical continuation are now constructed.

FAIL is not triggered because there is no inconsistency between the local C3 operator and the SF049 physical amplitude direction.

Therefore the preregistered correct verdict is:

`PARTIAL_TEMPLATE_ONLY_C3_TEMPLATE_CLOSED_ESSENTIAL_QUOTIENT_OPEN_SCOPED`.

## New exact theory frontier

`ESSENTIAL_SIX_DERIVATIVE_C3_FLUCTUATION_QUOTIENT_PROJECTOR_REQUIRED`.

More operationally:

`C3 TEMPLATE`
`-> COMPLETE SIX-DERIVATIVE REDUNDANT TENSOR / FIELD-REDEFINITION QUOTIENT`
`-> PROJECTED DYNAMICAL C3 FLOW`
`-> BACKGROUND/FLUCTUATION SPLIT-NIELSEN CONTROL`
`-> LORENTZIAN ON-SHELL MATCHING`.

The next high-information gate should use the existing essential sixth-derivative redundant-kernel basis rather than inventing arbitrary polynomial tensor contaminations.

## Claim ceiling

SF050 establishes no:

- physical SF025 `b`;
- background/fluctuation equality;
- regulator-independent C3 prediction;
- complete projected FRG C3 flow;
- asymptotic-safety correctness claim;
- historical RCG-002 authority;
- quantum `chi_ABC`;
- full quantum gravity;
- new physics.
