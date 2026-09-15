# SF054 — minimal covariant C3 vertex closure of the three-point FRG flow — AUDIT

Date: 2026-09-15
Preregistration: `34777656841abd66b221614bef8c0fafe06f8292`.

## Frozen covariant deformation

`Delta Gamma_C3 = g_C3^fluc(k) int sqrt(g) C_rho_sigma^mu_nu C_mu_nu^alpha_beta C_alpha_beta^rho_sigma`.

On a flat background, `C[delta]=0`, so the expansion begins at cubic order:

`Gamma_C3^(2)=0`,

`Gamma_C3^(3) != 0`.

Nonlinear curvature, inverse metrics and `sqrt(g)` then generate correlated higher vertices `Gamma_C3^(4)`, `Gamma_C3^(5)`, ... from the same single covariant coupling.

The nonzero four-point R3/C3 amplitude used as an SF049 control independently confirms that the deformation does not stop at three points. Independent five-graviton amplitude calculations also detect the same R3 counterterm in the physical five-point sector.

## Three-point flow topology authority

Christiansen et al., *Local Quantum Gravity*, arXiv:1506.07016, derive the three-graviton flow from three field derivatives of the Wetterich equation. Their eq. (7) states explicitly that the flow functions depend on dressed vertices with `n in {3,4,5}`.

The source also displays the diagrammatic three-point flow and notes that all diagrams are symmetrized in the external momenta.

Therefore the exact structural three-point RHS contains positions for 3-, 4-, and 5-point dressed vertices.

## Linear order in the fluctuation C3 coupling

Write schematically

`Gamma^(n) = Gamma_EH^(n) + g_C3^fluc Gamma_C3^(n) + O((g_C3^fluc)^2)`.

At first order in `g_C3^fluc`, the graviton part of `partial_t Gamma^(3)` contains contributions with exactly one C3 insertion:

- triangle-type terms: one `Gamma_C3^(3)` and remaining three-point vertices from the baseline truncation;
- mixed bubble-type terms: `Gamma_C3^(4)` with baseline `Gamma^(3)`, or baseline `Gamma^(4)` with `Gamma_C3^(3)`;
- tadpole-type term: `Gamma_C3^(5)`.

Since `Gamma_C3^(2)=0`, there is no tree-level C3 propagator/two-point insertion around flat space. This satisfies the frozen negative control.

The baseline EH/ghost diagrams still contribute to the projected p6 flow and can generate a C3 direction even when `g_C3^fluc=0`; SF054 does not assume otherwise.

## Closure conclusion

A truncation that adds only an independent p6/C3 tensor to `Gamma^(3)` while retaining baseline-only `Gamma^(4)` and `Gamma^(5)` omits source-authorized terms in the exact three-point RHS at linear order in the same covariant coupling.

Therefore it is not a source-faithful covariant C3 truncation.

The minimum covariant fluctuation extension must contain the correlated set

`{Gamma_C3^(3), Gamma_C3^(4), Gamma_C3^(5)}`

derived from one `int C3` operator and one common `g_C3^fluc(k)`.

It may not fit the three higher vertices independently if the gate claims a one-operator covariant deformation.

## Minimal projected beta architecture

The target can be organized as

`beta_C3^fluc ~ P_E_6d[F3_EH+ghost] + g_C3^fluc P_E_6d[F3_one-C3-insertion(3,4,5)] + O((g_C3^fluc)^2)`

with separately tracked wave-function/canonical-normalization terms.

This is an architecture, not a computed beta function.

## Classification

`MINIMAL_C3_FLOW_REQUIRES_CORRELATED_3_4_5_VERTEX_INSERTIONS_SCOPED`.

Secondary:

`THREE_POINT_ONLY_C3_TRUNCATION_NOT_COVARIANTLY_CLOSED_SCOPED`.

## Next object

`CORRELATED_C3_3_4_5_VERTEX_GENERATOR_AND_PROJECTED_LOOP_EVALUATION_REQUIRED`.

A future calculation must generate the mixed-momentum 3/4/5-point tensors from the same covariant C3 operator and insert them in the three-point flow before applying the SF052 projector.
