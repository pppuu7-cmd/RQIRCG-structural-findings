# SF055 — common covariant C3 vertex generator implementation freeze

Date: 2026-09-15
Parent gate: `SF055_C3_PROJECTED_FRG_IMPLEMENTATION_CONTRACT`.
Branch: `sf055-c3-generator-20260915`.
Status: **prospective freeze before generator output is inspected**.

This is not a new competing gate. It freezes the implementation method for SF055 Lane B and the Lane-C insertion object interface.

## TARGET OBJECT

Generate contracted flat-background pure-graviton vertices

`Gamma_C3^(n)[(p1,h1),...,(pn,hn)]`, `n=2,3,4,5`,

from one and the same covariant local deformation

`Delta Gamma_C3 = G_C3^fluc int d^4x sqrt(g) C_ab^cd C_cd^ef C_ef^ab`.

No independent n=3/4/5 coefficients or templates are permitted.

## FIELD / SIGNATURE / DERIVATIVE CONVENTION

- D=4 Euclidean flat background `bar g = delta`;
- linear split `g = delta + h`;
- each external leg is represented as a plane-wave perturbation `epsilon_i h_i exp(p_i.x)`;
- local derivative convention is `partial_mu exp(p.x) = p_mu exp(p.x)` with no explicit Fourier `i` factor;
- momentum conservation `sum_i p_i = 0` is required before interpreting the extracted coefficient as an integrated local vertex;
- any eventual Fourier-phase convention change is one single global convention and may not be changed independently by vertex order.

## EXACT MULTILINEAR EXTRACTION ALGORITHM

Use a square-free nilpotent polynomial algebra in `epsilon_i`:

`epsilon_i^2 = 0`, `epsilon_i epsilon_j = epsilon_j epsilon_i`.

A coefficient is indexed by a bitmask. Products whose masks overlap are identically discarded. Therefore the coefficient of the full mask extracts the fully multilinear n-leg functional derivative without finite-difference step-size contamination.

For every mask `M`, spatial derivatives act exactly by the total momentum carried by that monomial:

`partial_mu X[M] = (sum_{i in M} p_i)_mu X[M]`.

The generator must construct, in this algebra and without order-specific templates:

1. `g^{-1}` from the finite nilpotent geometric series;
2. `sqrt(det g)` from the determinant and truncated binomial series;
3. Christoffel symbols;
4. Riemann, Ricci and scalar curvature;
5. the D=4 Weyl tensor;
6. the mixed two-form operator `C_ab^cd`;
7. `sqrt(g) Tr(C^3)`;
8. the coefficient of the full external-leg mask.

Because the algebra is nilpotent of order n, all expansions truncate exactly at finite order.

## PROSPECTIVELY FROZEN CONTROLS

### B0 — two-point negative control

For any conserved two-leg configuration, `Gamma_C3^(2)=0` within floating roundoff. Frozen threshold:

`abs(Gamma_C3^(2)) <= 1e-11`.

### B1 — SF052 three-point cross-check

Use exactly the SF052 D=4 unit symmetric point and its five TT polarizations per leg, all 125 triples.

The common-action coefficient must agree with the existing SF052 cubic `C3` tensor up to **one constant global factor common to all 125 components**. The expected combinatorial factor for an action coefficient versus the SF052 symmetrized template is prospectively `6` under the derivative convention above.

PASS_B1 requires:

- for every component with `|T_SF052| > 1e-10`, ratio `T_generator/T_SF052 = 6` within `1e-9` relative error;
- for components with `|T_SF052| <= 1e-10`, `|T_generator| <= 1e-9`;
- global maximum absolute mismatch against `6*T_SF052` <= `1e-9`.

A different constant factor is not silently accepted; it requires an audit of conventions before proceeding.

### B2 — deterministic generic four-point control

Momenta are frozen as

`p1=(1,0,0,0)`,
`p2=(0,1,0,0)`,
`p3=(0,0,1,0)`,
`p4=(-1,-1,-1,0)`.

For each leg construct a deterministic orthonormal transverse 3-frame by QR completion and use TT basis element index `(leg_index mod 5)` from the same normalized 3x3 traceless basis convention as SF052.

PASS_B2 requires:

- the contracted four-point coefficient is finite;
- `abs(Gamma_C3^(4)) > 1e-10`;
- invariance under all adjacent external-leg transpositions within `1e-9` relative/absolute mixed tolerance.

### B3 — deterministic generic five-point control

Momenta are frozen as

`p1=(1,0,0,0)`,
`p2=(0,1,0,0)`,
`p3=(0,0,1,0)`,
`p4=(0,0,0,1)`,
`p5=(-1,-1,-1,-1)`.

Use the same deterministic TT-basis construction and basis index `(leg_index mod 5)`.

PASS_B3 requires:

- the contracted five-point coefficient is finite;
- `abs(Gamma_C3^(5)) > 1e-10`;
- invariance under all adjacent external-leg transpositions within `1e-9` relative/absolute mixed tolerance.

### B4 — common-origin API control

The generator API must have no per-order C3 coupling parameter. It returns the bare coefficient of the one common action. The single running `g_C3^fluc(k)` multiplies every generated n-point insertion externally and identically.

## COUNTEREXAMPLE-FIRST NEGATIVE TESTS

The test suite must deliberately fail if:

- one leg is removed from the full-mask extraction but the result is presented as an n-point vertex;
- an independent n=4 or n=5 rescaling is injected;
- a leg momentum is changed without restoring momentum conservation and the output is interpreted as an integrated local vertex;
- the Weyl-cubic contraction is replaced by the SF052 three-point template for n=4 or n=5.

## PASS / BLOCKED

`PASS_COMMON_COVARIANT_C3_VERTEX_GENERATOR_2_TO_5_SCOPED` only if B0–B4 and negative controls pass in CI.

`BLOCKED_C3_VERTEX_GENERATOR_NOT_CLOSED` if a single common covariant implementation cannot simultaneously satisfy the frozen n=2/3/4/5 controls.

## INTERPRETATION CEILING

A PASS closes only the SF055 common C3 vertex-generator control. It does not establish the EH/ghost baseline loop reproduction, diagram symmetry factors, a projected C3 beta function, regulator independence, background/fluctuation equality, or Lorentzian physical matching.
