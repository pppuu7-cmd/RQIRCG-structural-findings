# SF039 — reversible harmonic transport implementation — TERMINAL

Date: 2026-09-15
Preregistration: `de31d7e3c6c6bbd97045709ff032e7f6a951f98d`.
Derivation/source authority: `research_log/SF039_REVERSIBLE_HARMONIC_TRANSPORT_DERIVATION_AND_AUTHORITY.md`, commit `6bbc2cf28ee6d65bea52ab4bdab5d2a71caf06aa`.

## RESULT / CLASSIFICATION

`QUADRATIC_REVERSIBLE_TRANSPORT_GENERATES_NO_CONNECTED_CONTROL_PHASE_SCOPED`.

Secondary structural result:

`CONNECTED_CONTROL_PHASE_REQUIRES_NONQUADRATIC_OR_GENUINE_MULTILABEL_CONTROL_CONTENT_SCOPED`.

Qualification:

`IDEAL_REVERSIBLE_TRANSPORT_NULL != DEVICE_ERROR_NULL`.

## Frozen implementation class

Each motional body is transported in a moving quadratic trap

`H_I=p_I^2/(2m_I)+(m_I omega_I^2/2)[x_I-Q_I(t;s)]^2`,

with branch-independent frequency and center

`Q_I=q_I^0+d_I(s;lambda_A) f(t)`.

The displacements are

`d_A=lambda_A a ell`,

`d_B=2b ell`,

`d_C=3c ell`,

`d_D=-(lambda_A a+2b+3c)ell/5`.

COM closure holds at every time because all four centers share the same interpolation `f(t)`.

Signed transport is the exact program reversal `lambda_A -> -lambda_A`.

## Exact forced-harmonic degree result

For a forced harmonic oscillator with center linear in one prescribed amplitude, the exact branch-dependent c-number phase has generic form

`phi_I=const_I+alpha_I d_I+beta_I d_I^2`.

The coefficients may contain arbitrary dependence on the common pulse shape, frequency and duration. No coefficient value was used in the connected proof.

The shared recoil-body square is

`(lambda a+2b+3c)^2`

which reduces on Boolean labels to

`lambda^2 a+4b+9c+4lambda ab+6lambda ac+12bc`.

There is no `abc` monomial.

Thus the full ideal transport/recombination phase is a Boolean polynomial of degree at most 2.

Since `C3` is the third Boolean difference,

`Delta3 Phi_ctrl=0`

exactly.

## Robust simple-control errors

A common multiplicative A-amplitude error

`lambda -> (1+g)lambda`

does not change the Boolean-degree bound and gives exact connected null.

A body-local branch-independent center offset similarly produces only degree 0,1,2 phase terms under the quadratic functional and remains connected-null.

Signed reversal changes odd/even lambda dependence but does not generate a degree-three branch monomial.

## Exact symbolic negative control

A generic symbolic expansion with arbitrary `alpha_I,beta_I` returned

`Delta3_generic_quadratic=0`.

With multiplicative gain error:

`Delta3_gain_error=0`.

Adding a prospective cubic counterterm

`chi a b c`

returns

`Delta3=chi`.

This confirms the Boolean-order discriminator.

## Minimum evasion content

A connected control phase requires new content outside the frozen class, e.g.

- a genuine three-register interaction `hbar chi n_A n_B n_C`;
- a nonlinear actuator/crosstalk term with degree-three branch dependence;
- branch-dependent trap parameters carrying an `abc` component;
- another genuine multilabel nonquadratic control mechanism.

Anharmonicity by itself is not automatically a connected contaminant; its branch dependence must generate degree-three content in the complete protocol.

Retain:

`NONQUADRATIC != AUTOMATIC_CONNECTED_CONTAMINATION`.

## External sanity authority

Moving harmonic trap protocols with no final vibrational heating and robust transport are established in the shortcuts-to-adiabaticity literature (Torrontegui et al., arXiv:1010.3271; Guery-Odelin & Muga, arXiv:1410.4957).

State-dependent force control coupling internal states to motion is experimentally established (Haljan et al., arXiv:quant-ph/0411068).

These sources make the implementation class non-vacuous but do not establish any particular RQIRCGSF hardware or error budget.

## Relation to SF034–SF038

SF034's cubic `zeta n_A n_B n_C` remains a valid adversarial connected-control nuisance.

SF039 now shows that this nuisance is **not a generic consequence of the minimal quadratic reversible transport used to realize signed displacements**.

SF035–SF038 amplitude/parity calibration remains useful if a real device contains genuine multilabel nonlinear crosstalk, but such crosstalk is additional device content that must be measured/bounded rather than assumed inevitable.

## New operational frontier

`BOUND_OR_CALIBRATE_GENUINE_MULTILABEL_NONLINEAR_CONTROL_CONTENT`.

The highest-information next control should exploit the already exact gravitational nulls to localize genuine cubic crosstalk rather than adding another generic noise amplitude.

## Claim ceiling

SF039 establishes no real-device error null, laboratory feasibility, actuator technology, upper bound on nonlinear crosstalk, successor quantum residual, quantum matching coefficient, quantum `chi_ABC`, GR-vs-QG discriminator or new physics.
