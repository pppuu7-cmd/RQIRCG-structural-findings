# SF054 — minimal covariant C3 vertex closure of the three-point FRG flow — TERMINAL

Date: 2026-09-15
Preregistration: `34777656841abd66b221614bef8c0fafe06f8292`.
Audit: `research_log/SF054_MINIMAL_COVARIANT_C3_VERTEX_CLOSURE_AUDIT.md`, commit `a9f1bff60d14e8843563ad085e121813329aa87c`.

## RESULT / CLASSIFICATION

`MINIMAL_C3_FLOW_REQUIRES_CORRELATED_3_4_5_VERTEX_INSERTIONS_SCOPED`.

Secondary:

`THREE_POINT_ONLY_C3_TRUNCATION_NOT_COVARIANTLY_CLOSED_SCOPED`.

## Structural result

The covariant operator

`int sqrt(g) C^3`

has no flat-background two-point vertex but generates nonzero correlated graviton vertices beginning at n=3 and continuing through n=4,5,... .

The exact three-graviton Wetterich flow depends on dressed vertices of orders n=3,4,5.

Therefore at first order in a single fluctuation coupling `g_C3^fluc`, a source-faithful RHS contains one-C3-insertion contributions through each of

`Gamma_C3^(3)`,

`Gamma_C3^(4)`,

`Gamma_C3^(5)`.

Adding a C3 tensor only to the three-point vertex while keeping baseline-only 4-/5-point vertices drops terms required by the same covariant deformation.

## Minimum future flow architecture

A future projected fluctuation beta calculation must use one common C3 coupling and a correlated vertex family derived from the same covariant operator:

`{Gamma_C3^(3), Gamma_C3^(4), Gamma_C3^(5)}`.

The SF052 projector is then applied to the full three-point RHS after loop contraction.

At schematic linear order:

`beta_C3^fluc ~ P_E_6d[F3_baseline] + g_C3^fluc P_E_6d[F3_one-C3-insertion(3,4,5)] + ...`.

This equation is an implementation architecture, not a numerical beta function.

## Controls

- `Gamma_C3^(2)=0` around flat space: PASS.
- `Gamma_C3^(3)` matches the already-authorized C3 physical/off-shell direction: PASS.
- nontrivial higher-point C3 content: supported independently by known R3/C3 four- and five-graviton amplitude sectors.
- 3-/4-/5-point dependence of the three-point FRG flow: explicit in the audited vertex-flow construction.

## New exact frontier

`CORRELATED_C3_3_4_5_VERTEX_GENERATOR_AND_PROJECTED_LOOP_EVALUATION_REQUIRED`.

This is now the smallest source-faithful missing calculation on the fluctuation side.

## Claim ceiling

SF054 does not compute the C3 fluctuation beta function, establish a fixed point, identify background and fluctuation C3 couplings, remove regulator dependence, perform Lorentzian matching, select physical SF025 `b`, compute quantum `chi_ABC`, change historical RCG-002 authority, establish full quantum gravity, or discover new physics.
