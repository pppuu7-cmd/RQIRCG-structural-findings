# SF055 — preflight source baseline and completeness freeze

Date: 2026-09-15
Parent preregistration: `9d998d984566aa5bf290312a6a062fd632c85561`.
Branch: `sf055-preflight-20260915`.
Status at this commit: **prospective calibration specification; no SF055 implementation output inspected yet**.

This note does not open a competing gate and does not alter the frozen SF055 gauge, regulator, split, kinematics, C3 closure, or projector. It supplies the numerical/structural benchmark that SF055 Lane A explicitly required to be specified prospectively before implementation output is used.

## SOURCE AUTHORITY

Primary source for the baseline realization:

N. Christiansen, B. Knorr, J. Meibohm, J. M. Pawlowski, M. Reichert, *Local Quantum Gravity*, arXiv:1506.07016v2 (20 May 2016), Phys. Rev. D 92, 121501 (2015).

Exact source objects used here:

- eq. (1): Wetterich flow with graviton and Faddeev–Popov ghost traces;
- eqs. (3)–(5): vertex ansatz and gauge-fixed Einstein–Hilbert tensor origin;
- eq. (6): TT projected three-point decomposition;
- eq. (7) and Fig. 2: projected three-point flow and dependence on dressed vertices `n in {3,4,5}`, with external-momentum symmetrization;
- eqs. (9)–(11): symmetric three-point kinematics and finite-difference extraction of `g_3` and `lambda_3`;
- regulator paragraph following eq. (11): `R_phi(x)=Gamma_k^(phi phi)|_{mu=0}(x) r(x)`, `x r(x)=(1-x) theta(1-x)`;
- eq. (14): analytic `eta_h=eta_c=0`, `partial_{p^2} Flow_G|_{p=0}` benchmark equations.

Frozen baseline point for the analytic spot-check is the source Fig. 1 point

`(g, mu_h, lambda_3) = (1, 1/10, -7/10)`.

The analytic spot-check is deliberately only a transcription/combinatoric/regulator-convention control. It is **not** sufficient to pass Lane A, because SF055 requires reproduction from the implemented EH/ghost flow machinery rather than substitution of the published beta function.

## LANE A — PROSPECTIVELY FROZEN BENCHMARK

### A1. Structural topology benchmark

The implementation must represent the source three-graviton Wetterich RHS before target projection, with the source-required dressed graviton vertex orders 3, 4 and 5 and baseline ghost contributions. External legs must be symmetrized.

PASS_A1 requires the generated topology manifest to contain the triangle, mixed 3/4 bubble, and 5-vertex tadpole classes, plus baseline ghost classes, without inserting a C3 ghost vertex.

### A2. Published extraction benchmark

At symmetric external momenta, the baseline implementation must expose enough unprojected/TT information to form the source projection and finite-difference extraction used in eqs. (10)–(11), including the evaluations corresponding to `p=k` and `p=0` where required by the published extraction.

PASS_A2 is not awarded by hard-coding source scalar `Flow_G` or `Flow_Lambda` values.

### A3. Independent analytic Eq. (14) spot-check

For `(g,mu,lambda)=(1,1/10,-7/10)`, define the source Eq. (14) `beta_g` bracket `B_g`. Exact rational reduction gives

`B_g = -274830865/3865224`,

hence

`beta_g = 2 - (274830865/9179907)/pi`.

For the same point the remaining two analytic source equations reduce to

`beta_lambda3 = 7/5 - (3364922887/183598140)/pi`,

`beta_mu = -1/5 + (6554/3993)/pi`.

Reference decimals (diagnostic only, exact forms above are authoritative):

- `beta_g ~= -7.529658781722162`;
- `beta_lambda3 ~= -4.433872942167074`;
- `beta_mu ~= 0.32246506237129074`.

PASS_A3 requires an implementation with exact-rational intermediate arithmetic for the coefficients of `1` and `1/pi` to reproduce these forms before floating evaluation. This guards against an accidental numerical near-match.

**Lane A cannot terminal-PASS on A1–A3 alone.** It remains open until the same code path that generates the EH/ghost diagrams reproduces the prospectively specified published three-point baseline projection/extraction under the frozen conventions.

## LANE B — C3 TENSOR / GENERATOR CONTROLS

Frozen object: a single covariant deformation

`Delta Gamma_C3 = G_C3^fluc int d^4x sqrt(g) C_rho_sigma^mu_nu C_mu_nu^alpha_beta C_alpha_beta^rho_sigma`.

All pure-graviton C3 vertices used by SF055 must be functional derivatives of this same object. No independently fitted 3/4/5 coefficients are allowed.

Pre-science controls:

1. `Gamma_C3^(2)=0` on a flat background.
2. At the exact SF052 D=4 Euclidean unit symmetric point with TT external legs, the generated cubic C3 tensor must agree with the existing SF052 `C3` tensor up to one prospectively tracked global functional-derivative normalization convention only; the normalization must then be fixed once and used unchanged at n=4,5.
3. The generated n=3,4,5 multilinear tensors must be invariant under simultaneous permutation of external `(p_i,h_i)` legs (Bose symmetry), within deterministic numerical tolerance when floating arithmetic is used.
4. A change of the one common C3 coupling must rescale all n=3,4,5 C3 vertices together. No separate vertex-order rescaling is allowed.

Lane-B blocker remains the preregistered `BLOCKED_C3_VERTEX_GENERATOR_NOT_CLOSED` if these objects cannot be generated source-faithfully.

## LANE C — LINEAR-ORDER FLOW COMPLETENESS

At first order in the one common `g_C3^fluc`, the frozen insertion classes are:

- triangle: exactly one of the three graviton 3-vertices replaced by `Gamma_C3^(3)`;
- mixed 3/4 bubble: either the 4-vertex is `Gamma_C3^(4)` with baseline 3-vertex, or the 3-vertex is `Gamma_C3^(3)` with baseline 4-vertex, with the source-required external symmetrization;
- tadpole: the 5-vertex is `Gamma_C3^(5)`;
- propagator/two-point C3 insertion: **forbidden/zero** because `Gamma_C3^(2)=0` in the frozen flat-background expansion;
- ghost diagrams: **baseline only**, because the covariant C3 action contains no ghost fields.

PASS_C requires a machine-readable manifest that enumerates every permitted one-C3 insertion slot for every retained graviton topology and rejects both missing and double-C3 insertions at linear order. Exact symmetry factors remain sourced from the baseline diagram realization and are not inferred from slot counts alone.

## PROJECTOR-FLOW INTERFACE PREFLIGHT

Before any loop output is interpreted, reconstruct the SF052 frozen tensor basis and normalized linear projector in the 125-component TT triple space. Required controls are exactly

`P_E_6d[C3]=1`,

`P_E_6d[S3]=P_E_6d[SSC]=P_E_6d[RDeltaR]=P_E_6d[SDeltaS]=0`,

with residual norm `243/9920` and the inherited Gram matrix unchanged.

This preflight validates the tensor interface only. It does not demonstrate that a future loop RHS has been generated correctly.

## COUNTEREXAMPLE-FIRST CHECKS FROZEN FOR THIS PREFLIGHT

The implementation must deliberately fail tests when any of the following mutations are injected:

- omit one C3 insertion class;
- add a C3 two-point insertion;
- add a ghost-C3 insertion;
- permit independent n=3/4/5 C3 rescalings;
- break one external-leg permutation;
- feed only an Einstein–Hilbert scalar dressing into `P_E_6d` and claim it reconstructs the orthogonal p6 tensor.

A green test suite without these negative controls is not a scientific PASS.

## INTERPRETATION CEILING

This preflight can validate source transcription, tensor/projector plumbing, C3 vertex common-origin controls, and flow-topology completeness. It cannot establish a C3 beta function, fixed point, scheme/regulator independence, background/fluctuation equality, Lorentzian on-shell matching, SF025 `b`, or a successor selector.

No substantive C3 flow value is authorized for inspection until all SF055 calibration lanes terminalize under the original preregistration.
