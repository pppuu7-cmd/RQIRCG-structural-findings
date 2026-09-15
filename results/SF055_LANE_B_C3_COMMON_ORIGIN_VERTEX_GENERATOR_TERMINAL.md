# SF055 Lane B — common-origin C3 vertex generator — TERMINAL

Date: 2026-09-15
Parent preregistration: `9d998d984566aa5bf290312a6a062fd632c85561`.
Prospective reproducibility-only repair record: `research_log/SF055_LANE_B_REPRODUCIBILITY_REPAIR.md`.

## RESULT / CLASSIFICATION

`PASS_C3_COMMON_ORIGIN_VERTEX_GENERATOR_SCOPED`.

SF055 overall status remains **NON-TERMINAL**.

`SF055_TERMINAL_PASS = FALSE`.

Lane A baseline EH/ghost flow reproduction and implemented Lane C diagram manifest remain separately required. No substantive projected C3 beta value is authorized for inspection or interpretation.

## Frozen object

One covariant deformation only:

`Delta Gamma_C3 = G_C3^fluc int d^4x sqrt(g) C_rho_sigma^mu_nu C_mu_nu^alpha_beta C_alpha_beta^rho_sigma`.

All tested pure-graviton vertices are multilinear functional derivatives of this one object. No independent n=3,4,5 C3 coefficients are introduced.

The generator uses a square-free multivariate formal expansion. This is exact for the coefficient containing one power of every external-leg bookkeeping variable: a monomial containing `epsilon_i^2` cannot contribute to `d/d epsilon_1 ... d/d epsilon_n` at the origin.

Momentum derivatives use the same stripped Euclidean `d -> p` convention as SF050/SF052. The omitted Fourier `i^6` is one common global convention factor.

## B1 — two-point negative control

For the flat-background expansion:

`Gamma_C3^(2)=0`.

The executed generator returns zero within the unchanged frozen tolerance `1e-10`.

This also excludes a C3 propagator/two-point insertion at linear order in the later SF055 three-point flow.

## B2 — full SF052 cubic-tensor match

The fixed SF052 unit symmetric point was evaluated with the explicit analytic TT frames already used by SF050, avoiding any basis ambiguity from numerical SVD.

All `5^3 = 125` TT components were compared.

- nonzero SF052 reference components: `32`;
- common functional-derivative normalization factor: exactly `3! = 6` within the frozen tolerance;
- every reference-zero component remains zero within tolerance;
- after dividing by the common factor 6, the generated tensor norm reproduces the SF050/SF052 C3 norm `95/768` within tolerance;
- inherited `P_E_6d[C3]=1` is retained.

Thus the common covariant generator reproduces the frozen SF052 cubic C3 tensor up to the single prospectively allowed global functional-derivative normalization.

## B3 — Bose symmetry

Independent generic off-shell TT configurations were frozen by deterministic seeds and all permutations were tested:

- n=3: all `3! = 6` permutations;
- n=4: all `4! = 24` permutations;
- n=5: all `5! = 120` permutations.

Every scaled permutation residual is below the unchanged `1e-10` tolerance.

## B4 — one-common-coupling control

For each n=3,4,5 generated vertex:

- zero common coupling gives zero vertex;
- doubling the one common coupling doubles the vertex;
- the double/unit ratio is 2 within the frozen tolerance.

No vertex-order-specific rescaling is present.

Representative rounded diagnostic amplitudes are:

- n=3: unit `8.4261423547`, double `16.8522847093`;
- n=4: unit `24.9491036083`, double `49.8982072167`;
- n=5: unit `2.2626622791`, double `4.5253245582`.

These rounded amplitudes are diagnostics only. PASS decisions use the unrounded runtime values.

## Reproducibility incident and repair

Initial validation run `34995303477` recomputed the scientific controls successfully but failed byte-for-byte JSON comparison because platform-dependent floating diagnostics differed at approximately `1e-14` to `1e-13`, far below the fixed `1e-10` science tolerance.

That run is infrastructure/provenance evidence, not a Lane-B scientific FAIL.

A prospective control-only repair was frozen before the retry. It changed only:

1. the fixed SF052 TT frame from SVD construction to the explicit SF050 analytic frame;
2. durable serialization of machine-noise diagnostics to threshold certificates and fixed decimal diagnostic amplitudes.

It did **not** change the operator, kinematics, common coupling, required vertex orders, threshold, PASS criteria or interpretation ceiling.

Independent retry GitHub Actions run `34995827603`, job `104471676663`, completed successfully:

- generator recomputation: PASS;
- canonical raw byte comparison: PASS;
- artifact upload: PASS.

Artifact:

- id `10407234167`;
- name `sf055-c3-vertex-generator-v2`;
- digest `sha256:7db9004088f78bb8513c84373a5c4688790e28749727af866ab56a7518048e9c`.

## NEW SCIENTIFIC FACT

Within the frozen flat-Euclidean SF055 realization, a single covariant `C^3` deformation can be expanded source-faithfully into correlated pure-graviton vertices through orders n=3,4,5 while satisfying:

`Gamma_C3^(2)=0`,

`Gamma_C3^(3) -> SF052 C3 tensor x one global 3! convention factor`,

Bose symmetry at n=3,4,5,

and one-common-coupling scaling across all three vertex orders.

Therefore the SF054 structural requirement for correlated C3 3/4/5 vertices is computationally realizable in this scoped implementation.

## REMAINING SF055 LANES

Lane A:

`OPEN_BASELINE_EH_GHOST_FLOW_REPRODUCTION`.

Lane C:

`ABSTRACT_MANIFEST_PASS_IMPLEMENTED_DIAGRAM_MANIFEST_OPEN`.

Projector-flow interface remains preflight-certified only until an actual unprojected loop RHS is produced.

No projected C3 beta value is authorized until all SF055 calibration lanes terminalize.

## CLAIM CEILING

This result does not establish:

- a C3 beta function;
- a C3 fixed point;
- background/fluctuation equality;
- regulator independence;
- Lorentzian physical matching;
- physical SF025 `b`;
- quantum `chi_ABC`;
- historical RCG-002 authority;
- asymptotic safety as the correct theory;
- full quantum gravity or new physics.
