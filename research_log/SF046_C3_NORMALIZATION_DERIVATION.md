# SF046 — C3 normalization derivation

Date: 2026-09-15
Preregistration: `0b84c461737d5d308e19d9382fc5a262acfa4f1e`.

## Input conventions

Baldazzi et al. (arXiv:2312.03831), eq. (6):

`Gamma_k superset G_C3 int sqrt(g) C^rho sigma_mu nu C^mu nu_alpha beta C^alpha beta_rho sigma`.

Dimensionless coupling, eq. (30):

`g_C3 = k^2 G_C3`.

SF025 convention:

`delta Gamma = epsilon^2 delta b(mu) kappa^2 I3`,

`I3=int sqrt(-g) R_ab^cd R_cd^ef R_ef^ab`,

`kappa^2=32 pi G_N`.

SF025 also records the nonzero physical four-graviton insertion proportional to the coefficient multiplying this `R^3` operator.

## On-shell operator identity

For flat-space vacuum external gravitons, the linear external equations give Ricci-flat external legs. On this physical sector the Weyl tensor equals the Riemann tensor.

The tensor contraction in the Baldazzi `C^3` operator has the same cyclic index contraction as SF025 `I3`.

Therefore both action coordinates multiply the same on-shell local operator, modulo global action/sign conventions.

## Dimension check

In four dimensions:

`[C^3]=6`, `[d^4x]=-4`, so `[int C^3]=2`.

Hence `[G_C3]=-2`.

SF025 has `[kappa^2]=-2` and dimensionless `b`.

Thus the only dimensionally consistent direct coefficient map is

`G_C3 = s * epsilon^2 * kappa^2 * b`

at the formal order where SF025's bookkeeping `epsilon^2` is retained, with `s=+1 or -1` representing the unresolved global Euclidean/Lorentzian/Riemann-sign convention.

Equivalently, after stripping the formal loop-counting symbol and comparing the physical coefficient at that order,

`b = s * G_C3/kappa^2`.

Using `kappa^2=32 pi G_N`:

`b = s * G_C3/(32 pi G_N)`.

## Mapping the SF043 truncation trajectory

Baldazzi et al. give in the IR

`g_C3 = [G_N k^2][A - q ln(G_N k^2)]`,

`q=43/(645120 pi^3)`.

Since `g_C3=k^2 G_C3`, one obtains within that truncation

`G_C3 = G_N [A - q ln(G_N k^2)]`.

Therefore the corresponding SF025-coordinate representation is

`b_trunc(k) = s/(32 pi) [A - q ln(G_N k^2)]`.

For the representative technical value `A=-3.988e-6`, the constant part maps to

`b_trunc,const = s * (-3.988e-6)/(32 pi)`

`               approximately s * (-3.966e-8)`.

This number is a coordinate conversion of the finite-truncation value only. It is not a physical prediction.

## Beta-function cross-check

The finite-derivative FRG result is

`partial_t g_C3 = 2 g_C3 - [43/(322560 pi^3)] g_N + ...`.

The perturbative physical comparison quoted by the same source is

`partial_t g_C3 = 2 g_C3 + [1/(7680 pi^3)] g_N + ...`.

Using `g_C3=k^2 kappa^2 b` with `kappa^2=32 pi G_N` in the IR convention, the corresponding `b` beta coefficients differ by the same dimensionless ratio

`(-43/(322560 pi^3)) / (1/(7680 pi^3)) = -43/42`.

Thus the known mismatch is not removed by translating from `G_C3` to the SF025 `b` coordinate.

This is a strong sanity check: normalization conversion closes a coordinate ambiguity but leaves the approximation/physical-map problem intact.

## Convention-sign ceiling

Baldazzi et al. formulate the EAA in Euclidean signature and SF025's amplitude convention is Lorentzian. In addition, Riemann-tensor sign conventions can reverse a cubic invariant. The present gate does not independently reconcile every sign convention in the two source chains.

Therefore the magnitude and scale normalization are derived, while one global sign `s` remains convention-dependent.

## Result

`C3_NORMALIZATION_MAP_DERIVED_UP_TO_SIGNATURE_CONVENTION_SCOPED`.

The remaining physical blocker is not operator normalization. It is the regulator/truncation-independent Lorentzian computation of the cubic-curvature observable from the UV-safe trajectory.
