# SF049 — on-shell C3 helicity projector derivation

Date: 2026-09-15
Preregistration: `f04367fa06d44ccb62f236f2ea7c011587ad702f`.

## Source normalization

Primary source: Dunbar, Godwin, Jehu, Perkins, arXiv:1711.05526, especially eqs. (39)-(42).

They strip a common gravitational amplitude factor and write the three-point structures

`M3(--+) = <12>^6/(<23>^2<31>^2)`,

`M3(++-) = [12]^6/([23]^2[31]^2)`,

and the R3 deformation

`delta M3(+++) = alpha [12]^2[23]^2[31]^2`,

`delta M3(---) = alpha <12>^2<23>^2<31>^2`.

Their Lagrangian normalization is written as

`L = integral sqrt(-g) [R + (alpha/60) R_abcd R^cdef R_ef^ab]`

in that stripped convention.

The four-point leading-deformation coefficient is

`delta M4(++++) = -10 alpha K_++++^2 s t u`

when the explicit deformation parameter is restored.

SF049 uses this source normalization only to construct a projector. It does not identify `alpha` with the SF043 background coupling or the exact SF025 physical matching coefficient.

## H1 — uniqueness from little-group weights

Consider complex three-point massless kinematics on the anti-holomorphic branch

`<ij>=0`, `[ij] != 0`.

A local all-plus graviton amplitude can be written as a spinor monomial

`M3(+++) = c [12]^a [23]^b [31]^c_exp`.

Use `c_exp` for the exponent to avoid confusing it with the overall coefficient.

Under little-group scaling

`lambda_i -> t_i lambda_i`,

`tilde_lambda_i -> t_i^-1 tilde_lambda_i`,

an amplitude for helicity `h_i=+2` must scale as

`t_i^-4`.

Since `[ij] -> t_i^-1 t_j^-1 [ij]`, the three legs require

`a + c_exp = 4`,

`a + b = 4`,

`b + c_exp = 4`.

Subtracting these equations gives

`a=b=c_exp`,

hence

`a=b=c_exp=2`.

Therefore the unique local all-plus three-graviton structure is

`B_+++ = [12]^2[23]^2[31]^2`

up to an overall coefficient.

Its momentum mass dimension is six. Thus a four-derivative local operator cannot mimic this all-plus local three-point amplitude.

Parity gives the unique all-minus structure

`B_--- = <12>^2<23>^2<31>^2`.

This proves H1 in the frozen local six-derivative scope.

## H2 — normalized three-point projectors

For a physically normalized local three-graviton amplitude define

`P3+[M] = coeff_local_p6( M3(+++) / B_+++ )`

on any non-exceptional complex three-point configuration with `B_+++ != 0`.

Equivalently, when the amplitude contains a homogeneous local degree-six term, `coeff_local_p6` means take that homogeneous local term before division.

Likewise

`P3-[M] = coeff_local_p6( M3(---) / B_--- )`.

For the frozen R3/C3 deformation,

`P3+[delta M_C3] = alpha`,

`P3-[delta M_C3] = alpha`.

These are linear coefficient-extraction functionals on the declared local amplitude sector.

## H3 — Einstein/lower-derivative null

The Einstein-Hilbert three-point amplitudes have only the mixed helicity structures

`--+`

and

`++-`

in the source convention.

Therefore their all-plus and all-minus helicity components vanish:

`M3_EH(+++) = M3_EH(---) = 0`.

Hence

`P3+[M_EH]=P3-[M_EH]=0`.

The little-group derivation gives an additional derivative-order control: a local `+++` graviton amplitude requires the six-bracket-dimension structure above. Lower-derivative local sectors cannot produce a competing all-plus three-point polynomial with the same physical helicity weights.

After the inherited 4D local field-redefinition/EOM quotient, SF048 authority identifies the Goroff-Sagnotti C3 direction as the relevant essential local third-curvature pure-gravity scattering direction.

Thus the frozen lower-sector null is not obtained by choosing a convenient tensor basis.

## H4 — independent four-point projector

Dunbar et al. give the leading R3 deformation in the four-point all-plus channel as

`delta M4(++++) = -10 alpha K_++++^2 s t u`.

At a generic non-exceptional physical four-point configuration with

`s t u != 0`

and nonzero `K_++++`, define

`P4+[delta M] = - delta M4(++++) / (10 K_++++^2 s t u)`

at first order in the local six-derivative deformation.

Then

`P4+[delta M_C3] = alpha`.

Thus the independent four-point channel returns the same deformation coordinate as the three-point projector.

The condition `stu != 0` is mandatory. Exceptional forward/collinear points are excluded prospectively and receive no PASS credit.

## Cross-projector consistency

Within the frozen source normalization,

`P3+[delta M_C3] = P3-[delta M_C3] = P4+[delta M_C3] = alpha`.

This gives a three-channel normalization control:

- holomorphic/parity branch;
- anti-holomorphic branch;
- real generic four-point all-plus channel.

A future FRG amplitude reconstruction that claims to realize the same local C3 coefficient should satisfy this low-energy consistency after common external-state normalization and signature conventions are reconciled.

## H5 — action on a dynamical 1PI vertex

Let a physically normalized analytically continued dynamical 1PI three-graviton vertex be

`Gamma^(3)_{mu nu,rho sigma,alpha beta}(p1,p2,p3)`.

Contract external legs with physical helicity-two polarization tensors:

`M_Gamma(+++) = epsilon_+^(mu nu)(p1) epsilon_+^(rho sigma)(p2) epsilon_+^(alpha beta)(p3) Gamma^(3)_{mu nu,rho sigma,alpha beta}`.

After LSZ/residue normalization appropriate to the physical amplitude, isolate the local homogeneous six-derivative term in its low-momentum expansion:

`[M_Gamma(+++)]_local,p6`.

Then the algebraic C3 projection is

`g_C3^fluc,phys = [M_Gamma(+++)]_local,p6 / B_+++`

in the common normalization.

The parity-conjugate channel gives an independent control.

At four points one can analogously contract `Gamma^(4)` with four positive-helicity polarizations and extract the local first-order C3 amplitude coefficient with `P4+`.

This is an explicit physical helicity projector definition. It is not yet an executed FRG flow.

## H6 — what remains unresolved

SF049 does not supply:

1. the Euclidean/off-shell FRG tensor projector needed to evaluate the running vertex before on-shell continuation;
2. the projected FRG flow equation for this C3 component;
3. the Nielsen/split-Ward map from SF043's background-essential `G_C3` to the dynamical fluctuation coefficient;
4. the physical Lorentzian analytic-continuation / spectral reconstruction for the target C3 vertex;
5. regulator-independent matching to the low-energy physical coefficient;
6. a numerical value for SF025 `b`.

Therefore P3-P6 of SF048 remain open.

## Positive controls

PC1: `P3+[alpha B_+++]=alpha` — PASS algebraically.

PC2: `P3-[alpha B_---]=alpha` — PASS algebraically.

PC3: `P4+[-10 alpha K_++++^2 stu]=alpha` — PASS for generic `stu != 0`.

## Negative controls

NC1: Einstein `+++` / `---` components vanish — PASS.

NC2: exceptional spinor or four-point configurations with zero normalization polynomial are explicitly outside projector domain — PASS by domain restriction, not by numerical regularization.

NC3: no equality between background `G_C3` and physical projected coefficient is used — PASS.

## Structural result

The SF048 P2 blocker can be split into two pieces:

- physical on-shell algebraic projector: CLOSED;
- Euclidean/off-shell FRG implementation of that projector: OPEN.

Thus:

`PHYSICAL HELICITY PROJECTION != PROJECTED FRG FLOW`.

The next theory bottleneck is now the embedding of this explicit physical projector into the dynamical FRG vertex flow and its background/fluctuation identity map.
