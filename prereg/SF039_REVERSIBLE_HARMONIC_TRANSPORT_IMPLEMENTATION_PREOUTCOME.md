# SF039 — reversible harmonic transport implementation — PREOUTCOME

Date: 2026-09-15
Inherited recovery: `87b07bb9d0966141c2b20c74e18274f822de05ec`.

## PURPOSE

Provide one explicit finite-duration control implementation class for the SF038 signed A-transport operation and determine whether its own ideal/control phases can contaminate the connected readout `C3`.

This gate addresses the operational frontier

`EXPLICIT_REVERSIBLE_TRANSPORT_IMPLEMENTATION_MODEL_REQUIRED`.

It does not change gravitational dynamics or authorize a successor residual.

## INDEPENDENT PHYSICAL MOTIVATION

Moving harmonic traps and state-dependent forces are established reversible quantum-control classes. SF039 uses only their generic forced-harmonic structure; no external apparatus-specific coefficient is imported.

The specific model below is frozen before evaluating its `C3` consequence.

## FROZEN FINITE-DURATION CONTROL MODEL

For each motional body `I in {A,B,C,D}`, during preparation use

`H_I(t;s)=p_I^2/(2m_I) + (m_I omega_I^2/2) [x_I-Q_I(s,t)]^2`,

with branch-independent positive `omega_I`.

The branch-programmed trap center is

`Q_I(s,t)=q_I^0 + d_I(s;lambda_A) f(t)`.

The common real trajectory `f(t)` satisfies

`f(0)=0`, `f(t_p)=1`,

`dot f(0)=dot f(t_p)=0`.

A no-final-excitation shortcut may additionally impose the standard zero-residual-oscillation condition on the trap acceleration; the exact polynomial schedule is not selected in this gate because the connected-degree theorem below must hold for every such common trajectory.

Frozen branch displacements are

`d_A=lambda_A a ell`,

`d_B=2 b ell`,

`d_C=3 c ell`,

`d_D=-(lambda_A a+2b+3c) ell/5`,

with `m_A=m_B=m_C=m`, `m_D=5m`.

Thus COM closure is exact at every `f(t)`:

`sum_I m_I d_I=0`.

Signed reversal is

`lambda_A -> -lambda_A`

with all timing, frequencies, branch register and B/C controls unchanged.

## READOUT IMPLEMENTATION

Use the exact time-reversed/inverse center program for recombination, with the same `omega_I` and reference clock.

The authoritative final object remains the reduced three-qubit `C3` after free gravitational evolution and recombination.

No open control action is promoted by itself.

## CONTROL-PHASE THEOREM TO TEST

For a forced harmonic oscillator whose center enters linearly, the exact propagator can be written as an ordinary harmonic propagator times a phase-space displacement and a c-number phase functional that is at most quadratic in the prescribed center trajectory `Q(t)`.

Because every `d_I(s;lambda_A)` above is linear in Boolean branch labels `(a,b,c)`, any ideal preparation/recombination c-number phase must be a Boolean polynomial of total degree at most 2 if the four oscillators are otherwise independent and quadratic.

The shared recoil-body D is the critical cross-term audit because `d_D^2` contains AB, AC and BC pair terms.

## REQUIRED CHECKS

H1. Expand `sum_I F_I[d_I]` symbolically under the generic fact that each forced-harmonic phase functional is quadratic in `d_I`; verify its Boolean degree is <=2, including the D recoil square.

H2. Apply exact `Delta3` and verify the ideal connected control phase vanishes for arbitrary branch-independent trajectory/frequency coefficients.

H3. Verify signed reversal `lambda_A -> -lambda_A` changes only terms odd in `lambda_A`; no cubic Boolean term is generated.

H4. Verify multiplicative common amplitude calibration error `lambda_A -> (1+g)lambda_A` preserves the degree<=2 null property.

H5. Verify body-local additive center offsets independent of branch labels preserve the degree<=2 null property.

H6. Construct one explicit lowest-order countermodel that can generate a cubic connected control phase, such as a branch-dependent nonlinear actuator/crosstalk term proportional to `a b c` or a genuine three-register interaction. Do not set its coefficient from outcome.

H7. Keep the free gravitational SF028B/SF038 contribution logically separate from the control theorem.

## DECISION RULE

### PASS

`QUADRATIC_REVERSIBLE_TRANSPORT_GENERATES_NO_CONNECTED_CONTROL_PHASE_SCOPED`

if H1-H5 establish exact `Delta3=0` for the frozen implementation class and H6 identifies the minimum type of extra nonlinear control content required to evade the theorem.

Secondary expected structural result if PASS:

`CONNECTED_CONTROL_PHASE_REQUIRES_NONQUADRATIC_OR_GENUINE_MULTILABEL_CONTROL_CONTENT_SCOPED`.

### FAIL

`QUADRATIC_REVERSIBLE_TRANSPORT_GENERATES_CONNECTED_CONTROL_PHASE_SCOPED`

only if the exact forced-harmonic/recoil structure itself contains a surviving Boolean-degree-3 phase.

### BLOCKED

Use BLOCKED if the exact phase-degree statement cannot be derived for the frozen Hamiltonian class.

### INVALID

Any post-result addition of anharmonicity, branch-dependent trap frequencies, cross-body control potentials, nonlinear actuator response or higher-register interaction changes the implementation class and requires a new prospective gate.

## EXTERNAL SOURCE ROLE

Primary literature on fast transport in moving harmonic traps and spin-dependent forces may support that the implementation class is physically non-vacuous. It does not establish that a future RQIRCGSF device realizes this Hamiltonian or its error bounds.

## INTERPRETATION CEILING

A PASS would establish an exact connected-control-phase null for one explicit ideal quadratic transport class and specified simple calibration errors.

It would not establish laboratory feasibility, suppress gravitational baseline terms, validate a real actuator, bound nonlinear crosstalk, authorize quantum-gravity residuals, select a quantum matching coefficient, compute quantum `chi_ABC`, or establish new physics.

Retain:

`IDEAL_REVERSIBLE_TRANSPORT_NULL != DEVICE_ERROR_NULL`.
