# SF054 — minimal covariant C3 vertex closure of the three-point FRG flow — PREOUTCOME

Date: 2026-09-15
Inherited authority: SF052 completed the frozen six-derivative essential projector; SF053 found the target projected dynamical C3 flow object absent from executed/published truncations.

## HYPOTHESIS

A source-faithful dynamical fluctuation flow for one covariant C3 coupling cannot in general be implemented by adding only a C3 tensor dressing to the three-graviton vertex. Because the three-point Wetterich flow depends on dressed n-point vertices through n=5, the covariant operator may require correlated C3-induced 3-, 4-, and 5-graviton vertices tied to one common coupling.

## EXACT OBJECT

Frozen covariant deformation:

`Delta Gamma_C3 = g_C3^fluc(k) * integral d4x sqrt(g) C_rho_sigma^mu_nu C_mu_nu^alpha_beta C_alpha_beta^rho_sigma`.

Expand about flat Euclidean background:

`Delta Gamma_C3 = sum_{n>=3} (1/n!) Gamma_C3^(n) h^n`.

The gate audits only which `Gamma_C3^(n)` are structurally required for the RHS of `partial_t Gamma^(3)` at first order in the fluctuation C3 coupling.

## FROZEN SOURCE AUTHORITY

Christiansen et al., *Local Quantum Gravity*, arXiv:1506.07016, especially the three-point flow discussion and eq. (7): the flow functions for `Gamma^(3)` depend on dressed vertices with `n in {3,4,5}`.

## REQUIRED CHECKS

1. Does the covariant C3 operator have nonzero flat-background vertices `Gamma_C3^(3)`, `Gamma_C3^(4)`, `Gamma_C3^(5)` generically?
2. Does the exact structural form of the three-point FRG RHS contain places where 3-, 4-, and 5-point graviton vertices enter?
3. At linear order in `g_C3^fluc`, can a C3 insertion occur in each of those vertex orders?
4. Does C3 generate a two-point vertex around flat space? This is a frozen negative control.
5. Is a three-point-only C3 truncation source-faithful for the projected beta function?

## PASS OPTIONS

`MINIMAL_C3_FLOW_REQUIRES_CORRELATED_3_4_5_VERTEX_INSERTIONS_SCOPED` if 3-, 4-, and 5-point C3 vertices are generically nonzero and all can enter the three-point flow at linear order.

`THREE_POINT_ONLY_C3_TRUNCATION_STRUCTURALLY_CLOSED_SCOPED` only if higher C3 vertices are absent or provably irrelevant to the frozen three-point flow at linear order.

## BLOCKED

`BLOCKED_C3_HIGHER_VERTEX_OBJECT_NOT_DEFINED` if the covariant expansion or flow topology is insufficiently specified to decide the closure requirement.

## INVALID

No post-result replacement of the covariant C3 operator by independent unrelated 3/4/5 tensor couplings. A later approximation may split them only in a new prospectively frozen gate.

## CONTROLS

- `Gamma_C3^(2)=0` around flat background must hold because C3 begins at cubic order in the curvature perturbation.
- `Gamma_C3^(3)` must reproduce the SF049/SF052 C3 direction.
- Higher vertices must be derived from the same covariant operator, not separately fitted.

## INTERPRETATION CEILING

A closure result specifies the minimum consistent tensor content of a future flow calculation. It does not compute the loop integral, beta function, fixed point, background/fluctuation map, regulator independence, Lorentzian matching, physical SF025 `b`, quantum `chi_ABC`, historical RCG-002 authority, full quantum gravity, or new physics.
