# SF055A2 — source-Fourier EH/ghost baseline seed engine — PREOUTCOME

Date: 2026-09-15
Parent authority: SF055 preregistration `9d998d984566aa5bf290312a6a062fd632c85561`.
Predecessor outcome: `SF055A_EH_GHOST_SEED_ENGINE_INVALID_TERMINAL.md` classified `INVALID_SEED_POSITIVE_CONTROL_MIXED_FOURIER_CONVENTIONS_SCOPED`.

This is a new prospective calibration subgate. It does not alter or rescue the invalid SF055A gate. Its criteria are frozen before any SF055A2 implementation output is inspected.

## WHY A SUCCESSOR GATE IS LEGITIMATE

SF055A mixed two momentum coordinates in one positive control:

- a local real-exponential derivative convention `partial -> p_real`;
- the primary-source Fourier TT target `+K_EH(p_source^2-2 Lambda)`.

The source audit established `p_source=-i p_real`, so the old raw action result was exactly the analytic continuation of the source expression. The source object was reconstructible; the measurement convention was invalid.

SF055A2 therefore uses one source-faithful Fourier convention consistently throughout and retains the same scientific tolerances and seed-object scope.

## PRIMARY SOURCE AUTHORITY

Christiansen, Knorr, Pawlowski, Rodigast, *Global Flows in Quantum Gravity*, arXiv:1403.1232v2:

- Eq. (5): gauge-fixed Einstein-Hilbert + ghost action;
- Eq. (6): Faddeev-Popov operator;
- Eq. (7): linear gauge condition;
- Eq. (11): TT inverse propagator;
- Eq. (15): scalar TT coefficient `Z_h(p^2)(p^2-2 Lambda^(2))`;
- Eq. (16): `M^2=-2 Lambda^(2)`;
- regulator and threshold-function definitions used by SF055A.

Christiansen et al., *Local Quantum Gravity*, arXiv:1506.07016v2 supplies the active SF055 three-point baseline conventions and Eq. (14) target used only by the later full Lane-A loop gate.

## FROZEN FOURIER CONVENTION

For every source-action plane wave

`exp(i p.x)`,

use

`partial_mu -> i p_mu`.

All external momentum coordinates in this gate are real Euclidean Fourier momenta satisfying ordinary momentum conservation.

No vertex-order-dependent Fourier phase is permitted.

## EINSTEIN-HILBERT SEED

Use the same one covariant action and square-free multilinear extraction as SF055A:

`S_EH=(16 pi)^(-1) int sqrt(g)(-R+2 Lambda)`, `G_N=1`,

with D=4 flat Euclidean background and linear split `g=delta+h`.

The only implementation change from the invalid predecessor is the derivative map `partial -> i p` inside the covariant geometry.

No n-specific EH tensor template is allowed.

### TT two-point control

For `p=(1,0,0,0)`, all five normalized TT polarizations, and

`Lambda in {0, +3/20, -1/5}`,

require

`Gamma_EH,TT^(2)[p,h;-p,h] = K_EH (p^2 - 2 Lambda)`,

`K_EH=1/(32 pi)`,

with maximum absolute error <= `1e-11`.

The Landau gauge function must vanish on every TT test leg to <= `1e-13`.

The canonical graviton field convention remains prospectively

`h_can=sqrt(K_EH) h_raw`.

### EH n=3,4,5 controls

Use exactly the same external Fourier momenta, dense TT polarization construction, `Lambda=-7/10`, nonzero threshold and all-permutation Bose tolerance as SF055A:

- finite;
- `abs(V_n)>1e-10`;
- all `n!` external-leg permutations agree within `1e-10*(1+|V_n|)`.

A frozen dense control that unexpectedly vanishes is `INVALID_SEED_POSITIVE_CONTROL`; it is not replaced post-outcome.

## FADDEEV-POPOV RAW OPERATOR CONTROLS

Use the same source FP operator / gauge-variation representation as SF055A, now with every derivative carrying the common Fourier factor `i`.

At `h=0`, Eq. (6) reduces on the flat background to

`(M c)_mu = partial^2 c_mu`.

Therefore for Fourier momentum `p_c`,

`bar c^mu (M c)_mu = -p_c^2 (bar c.c)`.

Use the same three deterministic two-point momentum/polarization controls as SF055A. PASS requires absolute error <= `1e-12` against this raw source-operator value.

This raw FP sign is distinct from choosing a positive scalar propagator coordinate `p^2` in the regulator representation. No post-outcome sign flip is allowed.

### Ghost h-degree and generic interaction

Use the same frozen generic `ghost-ghost-h` kinematics and polarizations as SF055A.

Require:

- the Fourier ghost-ghost-h coefficient is finite and nonzero (`abs>1e-10`);
- ghost-ghost-h^2 coefficient zero within `1e-12`;
- ghost-ghost-h^3 coefficient zero within `1e-12`.

No target sign/magnitude for the nonzero h^1 control is fitted after execution.

## REGULATOR AND THRESHOLD CONTROLS

Retain SF055A without alteration:

- optimized `r(x)=(1-x)/x` for `0<x<1`, zero for `x>1`;
- positive scalar momentum coordinate `x=q^2/k^2`;
- frozen q^2/mu denominator tests and `1e-13` tolerance;
- the six frozen numerical `Phi_n^p[0](omega)` controls;
- analytic optimized-regulator target `2/(n! (1+omega)^p)`;
- numerical tolerance `2e-10*(1+|target|)`.

## COUNTEREXAMPLE-FIRST NEGATIVE CONTROLS

The executable checker must reject at least:

1. reverting the EH geometry to the predecessor real-exponential derivative phase `partial -> p` while keeping the source Fourier TT target;
2. wrong EH kinetic normalization `1/(16 pi)`;
3. wrong cosmological TT sign `p^2+2 Lambda`;
4. an independent n=4 EH rescaling;
5. a non-Bose n=3 mutation;
6. a nonzero ghost-ghost-h^2 mutation;
7. omission of the ghost-h interaction;
8. a raw Fourier FP two-point target with the wrong sign `+p^2(bar c.c)`;
9. regulator `r(x)=1-x`;
10. threshold derivative `dot r=2` instead of `2/x`.

All ten must be demonstrably rejected.

## PASS

`PASS_SOURCE_FOURIER_EH_GHOST_BASELINE_SEED_ENGINE_SCOPED`

only if every frozen positive control and all ten negative controls pass.

## BLOCKED / INVALID

`BLOCKED_SOURCE_FOURIER_SEED_OBJECT_NOT_RECONSTRUCTIBLE` if the primary-source action fails the internally consistent Fourier controls.

`INVALID_SOURCE_FOURIER_SEED_POSITIVE_CONTROL` if a prospectively frozen positive control is degenerate or ill-posed while the source object remains otherwise reconstructible.

`INVALID_SOURCE_FOURIER_SEED_CRITERIA_CHANGED_POSTOUTCOME` if any convention, threshold, kinematic control or normalization is changed after output inspection.

## INTERPRETATION CEILING

A PASS validates only source-Fourier EH/FP/regulator seed objects. It does not establish:

- the full internal Landau graviton propagator;
- Figure-2 three-point loop contractions;
- the published projected baseline flow;
- Eq. (14) reproduction;
- Lane-A terminal PASS;
- any C3 loop output or C3 beta function.

## NEXT IF PASS

Prospectively freeze the full source-Fourier internal propagator + Figure-2 EH/ghost loop realization and demand same-code-path reproduction of the already-frozen Local Quantum Gravity baseline before inspecting any substantive C3 projected flow.
