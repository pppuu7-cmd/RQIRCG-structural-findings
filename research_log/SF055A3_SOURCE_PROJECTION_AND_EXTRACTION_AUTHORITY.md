# SF055A3 — exact source projection / extraction authority

Date: 2026-09-15
Parent gate: `SF055A3_SOURCE_FOURIER_BASELINE_LOOP_REPRODUCTION`.
Primary source: N. Christiansen, B. Knorr, J. Meibohm, J. M. Pawlowski, M. Reichert, *Local Quantum Gravity*, arXiv:1506.07016v2 (20 May 2016), especially Eqs. (3)–(11), (14) and the regulator paragraph below Table 1.

Status: source-authority closure before integrated baseline projection output is inspected. This note does not alter the already-frozen SF055A3 physical realization or numerical PASS thresholds.

## SOURCE VERTEX NORMALIZATION

The source ansatz is

`Gamma_k^(phi1...phin)(p) = [prod_i sqrt(Z_phi_i(p_i^2))] G_n^(n/2-1) T^(n)(p;Lambda_n)`

with

`T^(n)(p;Lambda_n)=G_N S^(n)(p;Lambda -> Lambda_n)`.

For the baseline comparison in SF055A3, `eta_h=eta_c=0`; wave-function factors therefore do not generate additional scale-derivative terms in the analytic Eq. (14) target.

## TT PROJECTION AND TENSOR DECOMPOSITION

The source projects all external graviton legs to their transverse-traceless spin-2 parts.

It decomposes

`T^(n)(p;Lambda_n) = Lambda_n T^(n)(0;1) + T^(n)(p;0)`.

The full TT tensor flow is contracted with:

- `T^(n)(0;1)` for the cosmological/momentum-independent channel;
- `T^(n)(p;0)/p^2` for the gravitational/momentum-dependent channel.

The source calls the resulting scalars

`Flow_Lambda^(n)` and `Flow_G^(n)`.

The factor `1/p^2` belongs to the definition of `Flow_G` because the gravitational tensor projector is itself proportional to `p^2`.

For convenience the source definition of `Flow^(n)` also includes `prod_i Z_h^(-1/2)(p_i)`.

Therefore the SF055A3 integrated projection must be implemented as a **full TT tensor contraction with the source EH tensor**, not as the value of one polarization component and not as an unnormalised six-permutation sum.

## SYMMETRIC KINEMATICS

For the coupling-flow extraction the source uses

`|p1|=|p2|=p`,

`theta_12=2 pi/3`,

with `p3=-(p1+p2)` and hence `p1^2=p2^2=p3^2=p^2`.

## FINITE-DIFFERENCE COUPLING EXTRACTION — SOURCE EQS. (10)–(11)

For `g_3=k^2 G_3`, the source finite-difference extraction is

`dot g_3 = (2+3 eta_h(k^2)) g_3`

`          - (24/19) [eta_h(k^2)-eta_h(0)] lambda_3 g_3`

`          + 2 N_g sqrt(g_3) k [Flow_G^(3)(k^2)-Flow_G^(3)(0)]`,

with

`N_g^(-1) = T^(3)(k;0) o Pi_TT^3 o T^(3)(k;0)`.

For `lambda_3=Lambda_3/k^2`,

`dot lambda_3 = [3 eta_h(0)/2 - 1 - dot g_3/(2 g_3)] lambda_3`

`               + N_lambda/sqrt(g_3) Flow_Lambda^(3)(0)`,

with

`N_lambda^(-1) = T^(3)(0;1) o Pi_TT^3 o T^(3)(0;1)`.

Here `o` is the source's pairwise tensor-index contraction.

At the SF055A3 analytic benchmark `eta_h=0`, `g_3=1`, `k=1`, these simplify only after the integrated source projectors are evaluated; their normalisations must be computed from the source EH tensors, not fitted to any target beta function.

## ANALYTIC EQ. (14) IS A DIFFERENT MOMENTUM PROJECTION

The source explicitly states that Eq. (10) has no closed analytic form. For the analytic presentation it instead obtains `dot g` by taking

`partial_{p^2} Flow_G^(3)` at `p=0`.

Equation (14) is the resulting **derivative-at-p=0** system with all anomalous dimensions set to zero.

Therefore:

`EQ14_ANALYTIC_TARGET != FINITE_DIFFERENCE_EQ10_TARGET`.

The two are alternative source-authorized momentum projections and are compared by the source itself.

The SF055A3 preregistered Eq. (14) numerical benchmark must therefore be tested against the derivative-at-`p=0` projection of the same diagram code path. The finite-difference Eqs. (10)–(11) must also be implemented/reproduced as a source-architecture control, but their numerical output must **not** be forced to equal Eq. (14).

This resolves the earlier ambiguity without changing any physics object or post-outcome tolerance: it specifies which source projection the already-frozen Eq. (14) benchmark actually belongs to.

## EQ. (14) BASELINE TARGETS

With `eta_phi=0`, the source gives analytic flows for `g`, `lambda_3`, `mu`, and `lambda_1/sqrt(g_1)`.

For the frozen SF055A3 point

`g=1`, `mu=1/10`, `lambda_3=-7/10`,

the already prospectively frozen exact targets remain

`beta_g = 2 - (274830865/9179907)/pi`,

`beta_lambda3 = 7/5 - (3364922887/183598140)/pi`,

`beta_mu = -1/5 + (6554/3993)/pi`.

The first two require the three-point projection machinery plus source coupling extraction. The third is a two-point-flow target and cannot be inferred from Figure-2 three-point diagrams.

Retain:

`THREE_POINT_FIGURE2_REPRODUCTION != BETA_MU_REPRODUCTION`.

Therefore a terminal Lane-A PASS under the existing SF055A3 preregistration requires an additional same-conventions two-point baseline integration/extraction path for `beta_mu`, or else the gate must terminalize BLOCKED if that source object cannot be reconstructed without an unsupported convention. It is not permissible to insert the printed Eq. (14) `beta_mu` formula as if it had been regenerated from the implementation.

## REGULATOR AUTHORITY

The source baseline uses

`R_phi(x)=Gamma_k^(phi phi)|_{mu=0}(x) r(x)`

with

`x r(x)=(1-x) theta(1-x)`.

This remains exactly the SF055A3 regulator already calibrated in A3.1.

## IMPLEMENTATION CONSEQUENCES BEFORE QUADRATURE

The next integrated implementation must:

1. generate the full external TT tensor flow by evaluating/summing a complete TT basis, not a single external polarization triple;
2. independently generate the TT-projected EH tensors `T^(3)(p;0)` and `T^(3)(0;1)` from the same source-Fourier action path;
3. compute `N_g` and `N_lambda` directly from their source contractions;
4. form `Flow_G(p^2)` and `Flow_Lambda(0)` with source normalization;
5. implement both finite-difference Eq. (10) and derivative-at-p=0 extraction without equating them;
6. use the derivative projection for the Eq. (14) `beta_g/beta_lambda3` benchmark;
7. separately reconstruct the same-conventions two-point flow needed for the Eq. (14) `beta_mu` benchmark;
8. keep C3 disabled until Lane A terminalizes.

## CLAIM / INTERPRETATION CEILING

This is a source-authority note only. It is not a quadrature PASS, not Eq. (14) reproduction, not Lane-A terminal PASS, not SF055 terminal PASS, and not a C3 result.
