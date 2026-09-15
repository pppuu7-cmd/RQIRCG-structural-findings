# SF055A3Q3 — two-point beta_mu source authority audit

Date: 2026-09-16
Parent preregistration: `prereg/SF055A3Q3_TWO_POINT_BETA_MU_TOPOLOGY_PROJECTOR_PREOUTCOME.md`.
Status: source/object audit only; written while the independent Q3 workflow is queued and without using its substantive output.

## PRIMARY SOURCE

N. Christiansen, B. Knorr, J. Meibohm, J. M. Pawlowski, M. Reichert, *Local Quantum Gravity*, arXiv:1506.07016v2.

Primary URL:

`https://arxiv.org/abs/1506.07016`

## SOURCE FACTS RELEVANT TO Q3

The paper defines the n-point vertex ansatz and classical tensor structures from the gauge-fixed Einstein-Hilbert plus Faddeev-Popov source action in Eqs. (3)–(5).

The text explicitly states that the setup is complemented by the graviton mass parameter

`mu = -2 Lambda_2/k^2`

and that the flow of `mu` is extracted from the graviton two-point function at vanishing external momentum.

The regulator used for the analytic/fixed-point system is

`R_phi(x)=Gamma_k^(phi phi)|_(mu=0)(x) r(x)`

with

`x r(x)=(1-x) theta(1-x)`.

The same source paragraph states the closure identification

`lambda_3 = lambda_4 = lambda_5`.

Thus the Q3 same-conventions two-point object is source-connected to the already frozen SF055A3 regulator and higher-vertex closure; it is not a new post-hoc realization.

## TWO-POINT TOPOLOGY AUTHORITY

The topology coefficients used in Q3 are not read from the printed analytic beta_mu target. They are derived prospectively from two labelled functional derivatives of the same Wetterich inverse propagator used by Lane C/Q2:

`delta_1 delta_2 G = G A_1 G A_2 G + G A_2 G A_1 G - G A_12 G`.

Combined with the bosonic prefactor `1/2`, ghost supertrace sign and the prospectively frozen `Sym_2=(1/2)sum_S2`, this is the authority being tested by Q3.

The inherited SF055A2 source-Fourier seed independently fixes that the frozen FP seed contains a ghost two-point object and a ghost-ghost-graviton vertex but no ghost-hh or higher external-graviton seed vertex. Therefore the frozen two-point ghost flow contains a ghost bubble but no ghost tadpole.

## MASS-PROJECTOR AUTHORITY

The inherited SF055A2 seed has already validated the transverse-traceless two-point source normalisation

`Gamma_TT^(2)(p)=K_EH [p^2 + mu_h k^2]`,

`K_EH=1/(32 pi)`.

At eta_h=0,

`partial_t [K_EH k^2 mu_h] = K_EH k^2 [beta_mu + 2 mu_h]`.

Hence at `k=1`

`beta_mu = Flow_TT_mass(0)/K_EH - 2 mu_h`.

This is an algebraic scale-derivative identity and is fixed before any numerical comparison with Eq. (14).

## INTERPRETATION CEILING

This source audit does not establish the Q3 PASS, does not perform two-point loop quadrature, does not reproduce the Eq. (14) beta_mu number, and does not authorize any C3 flow output.