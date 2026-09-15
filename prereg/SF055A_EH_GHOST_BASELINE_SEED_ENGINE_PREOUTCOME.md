# SF055A — EH/ghost baseline seed engine — PREOUTCOME

Date: 2026-09-15
Parent authority: SF055 preregistration `9d998d984566aa5bf290312a6a062fd632c85561`.
Inherited current-main status: Lane B common C3 vertex generator PASS; Lane C topology/insertion bookkeeping PASS; Lane A remains open.

This is a calibration subgate inside SF055. It prospectively freezes the baseline vertex/propagator/regulator seed objects **before** their implementation output is inspected. It does not yet execute the three-point loop integral and cannot terminalize Lane A by itself.

## PURPOSE

Before assembling the source three-graviton Wetterich diagrams, construct and validate from the primary-source actions the exact baseline objects that every Lane-A diagram uses:

1. Einstein-Hilbert pure-graviton seed vertices through n=5;
2. Faddeev-Popov ghost two-point and ghost-ghost-graviton seed vertex;
3. flat-background TT two-point normalization and mass coordinate;
4. Landau-gauge/TT compatibility controls;
5. optimized regulator denominator and threshold-function controls.

A PASS authorizes use of these baseline seeds in the later three-point loop implementation. It is not a baseline-flow PASS.

## PRIMARY SOURCE AUTHORITY

### Local Quantum Gravity

N. Christiansen, B. Knorr, J. Meibohm, J. M. Pawlowski, M. Reichert, *Local Quantum Gravity*, arXiv:1506.07016v2 / Phys. Rev. D 92, 121501.

Frozen source objects:

- Eq. (1): graviton/ghost Wetterich traces;
- Eqs. (3)–(5): vertex ansatz and classical gauge-fixed Einstein-Hilbert seed action;
- Eqs. (6)–(11): TT projection, symmetric three-point kinematics and extraction;
- regulator statement: `R_phi(x)=Gamma_k^(phi phi)|_{mu=0}(x) r(x)`, `x r(x)=(1-x) theta(1-x)`;
- Eq. (14): later Lane-A numerical target at `eta_h=eta_c=0`.

### Global Flows in Quantum Gravity

N. Christiansen, B. Knorr, J. M. Pawlowski, A. Rodigast, *Global Flows in Quantum Gravity*, arXiv:1403.1232v2 / Phys. Rev. D 93, 044036.

This is explicitly cited by the Local Quantum Gravity paper for the underlying fully momentum-dependent vertex/propagator setup.

Frozen source objects:

- Eqs. (5)–(7):

`S_grav = (16 pi G_N)^(-1) int sqrt(g) (-R + 2 Lambda)`,

`S_gh = int sqrt(bar g) bar c^mu M_mu nu c^nu`,

`M_mu nu = bar nabla^alpha (g_mu nu nabla_alpha + g_alpha nu nabla_mu) - bar nabla_mu nabla_nu`,

`F_mu = bar nabla^nu h_mu nu - (1/2) bar nabla_mu h^nu_nu`,

`S_gf=(2 xi)^(-1) int sqrt(bar g) bar g^mu nu F_mu F_nu`, with `xi -> 0`;

- Eqs. (11)–(16): TT inverse-propagator/mass convention and EH-derived tensor structures;
- regulator construction around Eq. (18)–(19);
- Appendix A Eq. (56): modified threshold functions.

## FROZEN BACKGROUND / VARIABLES / SIGNATURE

- D=4 Euclidean;
- `bar g_mu nu = delta_mu nu`;
- linear split `g=bar g+h`;
- local plane-wave derivative convention for the implementation: `partial_mu exp(p.x)=p_mu exp(p.x)`;
- all integrated vertex tests obey momentum conservation;
- Fourier `i` factors are not inserted per vertex order. A later global Fourier convention change would require a separately audited bridge and is not permitted inside this subgate.

## EXACT PURE-GRAVITON GENERATOR

Use the same square-free commuting nilpotent multilinear extraction principle already validated for the common C3 generator:

`epsilon_i^2=0`.

For each external graviton leg `(p_i,h_i)`, build

`g=delta + sum_i epsilon_i h_i exp(p_i.x)`.

For each mask, derivatives act with the total mask momentum. Construct `g^{-1}`, `sqrt(det g)`, Christoffels, Ricci scalar and the density

`L_EH = (16 pi)^(-1) sqrt(g) (-R + 2 Lambda)`

with `G_N=1` in the raw seed. The full-mask coefficient is the raw functional vertex contracted with the chosen legs.

No n-specific EH tensor template may be hard-coded.

## SOURCE TT TWO-POINT NORMALIZATION CONTROL

For any unit-normalized TT polarization `h` transverse to nonzero momentum `p`, the raw seed must satisfy

`Gamma_EH,TT^(2)[p,h;-p,h] = K_EH (p^2 - 2 Lambda)`

with the prospectively frozen source normalization

`K_EH = 1/(32 pi)`.

This follows from the source action and its TT inverse-propagator convention.

Frozen tests use:

- `p=(1,0,0,0)`;
- all five normalized TT basis polarizations;
- `Lambda=0`, `Lambda=+3/20`, and `Lambda=-1/5`.

PASS requires maximum absolute error <= `1e-11` against `K_EH (p^2-2 Lambda)`.

The canonical baseline graviton field normalization used by later loop code is then fixed once as

`h_can = sqrt(K_EH) h_raw`,

so an n-graviton raw seed vertex is converted by the corresponding `K_EH^(-n/2)` field factor. This convention is frozen before any loop result.

## LANDAU GAUGE CONTROL

For every TT external polarization in the two-point normalization test,

`F_mu[h_TT]=0`

must hold to <= `1e-13`. Therefore the linear gauge-fixing action contributes exactly zero on the TT normalization controls.

This subgate does not approximate the internal full Landau propagator by a TT-only propagator. The complete internal propagator is a later Lane-A loop object.

## PURE EH n=3,4,5 BOSE / NONZERO CONTROLS

Frozen momenta:

### n=3

`p1=(1,0,0,0)`,
`p2=(-1/2,sqrt(3)/2,0,0)`,
`p3=-(p1+p2)`.

### n=4

`p1=(1,0,0,0)`,
`p2=(0,1,0,0)`,
`p3=(0,0,1,0)`,
`p4=(-1,-1,-1,0)`.

### n=5

`p1=(1,0,0,0)`,
`p2=(0,1,0,0)`,
`p3=(0,0,1,0)`,
`p4=(0,0,0,1)`,
`p5=(-1,-1,-1,-1)`.

For each leg, construct the deterministic normalized TT polarization obtained from the local five-element TT basis with dense weights

`w=(1,2,3,5,7)`

cyclically shifted by the zero-based leg index, followed by unit Frobenius normalization.

Use `Lambda=-7/10`, matching the already-frozen Local Quantum Gravity benchmark coordinate for the higher vertices.

For each n=3,4,5:

- vertex value must be finite;
- `abs(vertex)>1e-10`;
- all permutations of external `(p_i,h_i)` pairs must agree within mixed tolerance `1e-10*(1+|V|)`.

If a prospectively chosen dense control unexpectedly vanishes, classify that positive control INVALID; do not replace it post-outcome and claim PASS.

## FADDEEV-POPOV SEED GENERATOR

Implement the source FP operator equivalently by varying the source linear gauge condition under the quantum diffeomorphism of the linear split:

`delta_c g_mu nu = L_c g_mu nu`.

On the flat background,

`delta_c h_mu nu = partial_mu c_nu + partial_nu c_mu + c^rho partial_rho h_mu nu + h_mu rho partial_nu c^rho + h_nu rho partial_mu c^rho`.

Then

`(M c)_mu = delta_c F_mu`.

This representation is frozen because it is algebraically the FP operator generated by the source gauge condition and makes its h-degree explicit.

### Ghost two-point control

At `h=0`, for conserved ghost/antighost momenta `p_bar=-p_c`, the contracted operator must equal

`bar c^mu (M c)_mu = p_c^2 (bar c . c)`

under the frozen real-exponential derivative convention, to absolute error <= `1e-12`.

Use three deterministic non-collinear momenta and three deterministic ghost polarization pairs.

### Ghost h-degree control

Because the quantum diffeomorphism of `g=bar g+h` is at most linear in h and `F_mu` is linear, the FP seed is at most linear in h.

Required:

- ghost-ghost-h vertex: finite and nonzero on the frozen generic control below;
- ghost-ghost-h^2 coefficient: exactly zero within `1e-12`;
- ghost-ghost-h^3 coefficient: exactly zero within `1e-12`.

Frozen generic ghost-h control:

- graviton momentum `p_h=(1,0,0,0)` with dense TT polarization defined above;
- ghost momentum `p_c=(0,1,1,0)`;
- antighost momentum `p_bar=-(p_h+p_c)`;
- `c=(1,2,-1,1)/sqrt(7)`;
- `bar c=(2,-1,1,0)/sqrt(6)`.

## OPTIMIZED REGULATOR CONTROL

At `k=1`, freeze

`r(x)=(1-x)/x` for `0<x<1`, and `r(x)=0` for `x>1`.

Then source inverse-propagator denominators must satisfy:

- ghost: `q^2(1+r(q^2)) = 1` for `0<q^2<1` and `=q^2` for `q^2>1`;
- graviton TT: the same plus dimensionless mass `mu`, i.e. `1+mu` inside the cutoff and `q^2+mu` outside.

Test points: `q^2 in {1/16,1/4,3/4,5/4,2}` and `mu in {-1/2,0,1/10}`.

PASS tolerance: `1e-13`.

## THRESHOLD-FUNCTION CONTROL

For `eta=0`, the source Appendix-A threshold function is

`Phi_n^p[0](omega) = Gamma(n)^(-1) int_0^infty dx x^n dot r(x) / (x(1+r(x))+omega)^p`.

For the frozen optimized regulator, `dot r(x)=2/x` on `0<x<1`, hence analytically

`Phi_n^p[0](omega)=2/(n! (1+omega)^p)`.

Numerically integrate, without substituting the analytic answer into the integrand, the frozen cases

`(n,p,omega) in {(1,1,0),(1,1,1/10),(2,2,0),(2,2,1/10),(1,2,-1/2),(2,3,-1/2)}`.

PASS relative/absolute mixed tolerance: `2e-10*(1+|target|)`.

This validates the regulator scale derivative, radial measure convention and massive denominator before the three-point loop is attempted.

## COUNTEREXAMPLE-FIRST NEGATIVE CONTROLS

The executable test suite must reject at least:

1. wrong EH kinetic normalization `1/(16 pi)` substituted for `1/(32 pi)`;
2. wrong cosmological TT sign `p^2+2 Lambda`;
3. one independent rescaling of the n=4 EH seed after canonical normalization;
4. a non-Bose-symmetric n=3 seed mutation;
5. a nonzero ghost-ghost-h^2 mutation;
6. omission of the ghost-h interaction;
7. regulator `r(x)=1-x` instead of `(1-x)/x`;
8. `dot r=2` instead of `2/x` in the threshold integral.

Green execution without these negative controls is not a scientific PASS.

## PASS

`PASS_EH_GHOST_BASELINE_SEED_ENGINE_SCOPED`

only if all frozen positive and negative controls pass.

## BLOCKED / INVALID

`BLOCKED_EH_GHOST_SEED_OBJECT_NOT_RECONSTRUCTIBLE` if the primary-source action cannot be implemented consistently with the frozen TT/ghost/regulator controls.

`INVALID_SEED_POSITIVE_CONTROL` if a prospectively frozen positive control is degenerate or ill-posed while the underlying source object remains otherwise reconstructible.

`INVALID_SEED_CRITERIA_CHANGED_POSTOUTCOME` if any threshold, normalization, kinematics or source convention is changed after output inspection.

## INTERPRETATION CEILING

A PASS establishes only source-faithful baseline seed objects and regulator conventions. It does not establish:

- the full internal Landau graviton propagator;
- three-point loop integrands or momentum routing;
- source Figure-2 diagram symmetry factors beyond the already-closed Lane-C manifest;
- numerical loop integration;
- `Flow_G^(3)` or `Flow_Lambda^(3)`;
- reproduction of Eq. (14);
- Lane-A terminal PASS;
- any C3 projected beta function.

## NEXT IF PASS

Prospectively freeze the full internal propagator + EH/ghost Figure-2 loop contraction and require same-code-path reproduction of the already-frozen Local Quantum Gravity Eq. (14) benchmark before any C3 loop output is inspected.
