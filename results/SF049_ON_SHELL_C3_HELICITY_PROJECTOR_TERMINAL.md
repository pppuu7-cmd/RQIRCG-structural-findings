# SF049 — on-shell C3 helicity projector construction — TERMINAL

Date: 2026-09-15
Preregistration: `f04367fa06d44ccb62f236f2ea7c011587ad702f`.
Derivation: `research_log/SF049_ON_SHELL_C3_HELICITY_PROJECTOR_DERIVATION.md`, commit `bd882edb7abb3c2ecd392dbab038813db9642bf3`.

## RESULT / CLASSIFICATION

`PHYSICAL_ON_SHELL_C3_HELICITY_PROJECTOR_CONSTRUCTED_SCOPED`.

Required qualification:

`FRG_FLOW_AND_BACKGROUND_FLUCTUATION_MAP_REMAIN_OPEN_SCOPED`.

This closes the algebraic/physical projection layer only.

It does not change:

`R_ASGS_TRUNCATION = 1`.

`R_ASGS_PHYSICAL = UNDEFINED_MAP_NOT_CLOSED`.

## H1 — unique local all-plus structure

For complex massless three-point kinematics on the anti-holomorphic branch, little-group covariance for three `h=+2` gravitons requires

`M3(+++) proportional to [12]^a [23]^b [31]^c`

with

`a+c=4`,

`a+b=4`,

`b+c=4`.

Therefore

`a=b=c=2`.

The unique local all-plus structure is

`B_+++=[12]^2[23]^2[31]^2`.

Its mass dimension is six, so the channel directly isolates the local six-derivative sector from lower-derivative local gravity interactions.

Parity gives

`B_---=<12>^2<23>^2<31>^2`.

## H2 — three-point physical projector

Define on a non-exceptional physical amplitude

`P3+[M] = [M3(+++)]_local,p6 / B_+++`,

`P3-[M] = [M3(---)]_local,p6 / B_---`.

Using the frozen Dunbar et al. source normalization for the R3 deformation,

`delta M3(+++) = alpha B_+++`,

`delta M3(---) = alpha B_---`.

Hence

`P3+[delta M_C3]=alpha`,

`P3-[delta M_C3]=alpha`.

## H3 — Einstein/lower-sector negative control

Einstein gravity supplies the mixed-helicity three-point structures `--+` and `++-`, not `+++` or `---`.

Therefore

`P3+[M_EH]=P3-[M_EH]=0`.

The all-plus local graviton three-point amplitude itself has six momentum powers by little-group covariance, providing a derivative-order null against lower-derivative local sectors.

Within the inherited essential 4D field-redefinition/EOM quotient, the Goroff-Sagnotti C3 direction is the relevant local third-curvature physical scattering direction.

## H4 — four-point cross-projector

For the same leading R3 deformation, Dunbar et al. give

`delta M4(++++) = -10 alpha K_++++^2 s t u`.

Thus at generic kinematics with `stu != 0`, define

`P4+[delta M] = -delta M4(++++)/(10 K_++++^2 s t u)`.

Then

`P4+[delta M_C3]=alpha`.

This provides an independent generic four-point control of the same deformation coordinate.

Therefore, in the frozen normalization,

`P3+ = P3- = P4+ = alpha`

when acting on the C3/R3 deformation.

## H5 — explicit action on a dynamical 1PI vertex

For an analytically continued physically normalized dynamical graviton vertex `Gamma^(3)`, contract with three physical positive-helicity polarization tensors, extract the local homogeneous p6 term, and divide by `B_+++`.

Symbolically:

`g_C3^fluc,phys = [epsilon_+ epsilon_+ epsilon_+ . Gamma^(3)]_local,p6 / ([12]^2[23]^2[31]^2)`.

The parity channel supplies an independent check.

At four points, the corresponding all-plus physical projection uses `P4+`.

Thus the missing physical tensor direction now has an explicit coefficient-extraction functional.

## What is actually closed

SF048 P2 can now be refined:

`P2_ON_SHELL_ALGEBRAIC = CLOSED`.

But:

`P2_EUCLIDEAN_OFF_SHELL_FRG_IMPLEMENTATION = OPEN`.

This distinction is mandatory.

## What remains open

P3 projected FRG C3 flow:

`OPEN`.

P4 background-essential `G_C3` -> fluctuation projected coefficient with split-Ward/Nielsen control:

`OPEN`.

P5 Lorentzian/on-shell reconstruction from the actual FRG solution:

`PARTIAL_FRAMEWORK_ONLY`.

P6 regulator-independent physical matching:

`OPEN`.

Therefore the physical selector rank cannot be promoted.

## New exact theory frontier

The next highest-information theory problem is:

`C3_HELICITY_PROJECTOR_TO_DYNAMICAL_FRG_FLOW_EMBEDDING_REQUIRED`.

A legitimate successor must prospectively specify how the helicity projector is represented in the Euclidean/off-shell fluctuation calculation or in a direct Lorentzian flow, and how external-leg normalization and split identities are controlled.

Merely evaluating the SF043 background `G_C3` beta function again is not this calculation.

## Claim ceiling

SF049 does not establish:

- a projected C3 FRG beta function;
- equality of background and fluctuation C3 couplings;
- Lorentzian physical matching from the UV-safe trajectory;
- regulator-independent `b`;
- correctness of asymptotic safety;
- quantum `chi_ABC`;
- full quantum gravity;
- new physics.

Retain:

`PHYSICAL HELICITY PROJECTOR != PROJECTED FRG FLOW`.
