# SF006 — spectral localization and moment-nonuniqueness gate — PREREGISTRATION

Date: 2026-09-14
Status: **FROZEN PRE-OUTCOME MATHEMATICAL/STRUCTURAL GATE**

## Motivation

SF005 showed that unitarity/crossing/analyticity can bound higher-curvature Wilson coefficients while leaving dependence on a mass gap and other UV data. SF006 asks a narrower and more mathematical question:

> If the surviving homogeneous coefficients are represented as dispersive/spectral moments, do positivity plus any finite inherited lower-order calibration uniquely determine the spectral measure?

This gate does not attempt to construct a UV theory.

## Outcome embargo

`chi_ABC` remains fully embargoed.

## Frozen spectral abstraction

Where an EFT coefficient admits a dispersive/matching representation, abstract it as

`c_n = Integral dmu(x) w_n(x)`

with a nonnegative spectral measure `dmu >= 0` in the channel/domain where positivity applies.

For a simple inverse-mass expansion one may use `x = 1/M^2 > 0` and moments

`m_k = Integral dmu(x) x^k`.

The gate does not assume every gravitational coefficient has this exact one-variable form. It uses the moment model as a minimal witness: if even positive spectral measures with finite lower-moment constraints are nonunique, then positivity + finite calibration cannot generically be treated as a spectral selector without extra assumptions.

## Selector criterion

Spectral consistency would select the nonlinear homogeneous sector only if the inherited finite set of lower-order data and positivity determines the relevant spectral measure (or at least all higher moments entering the nonlinear coefficients) uniquely.

Positive verdict:

`SPECTRAL_DATA_FIXED_BY_INHERITED_MOMENTS_SCOPED`.

## Counterexample-first falsifier

Construct two positive measures `mu_A`, `mu_B` such that:

1. both satisfy the same normalization;
2. both satisfy the same frozen finite set of lower moments used as calibration;
3. both are supported on positive masses/positive inverse-mass variable;
4. at least one higher moment differs.

If so, the result is

`FINITE_IR_MOMENTS_DO_NOT_SELECT_MICROSCOPIC_SPECTRAL_MEASURE`.

## Frozen explicit control

For the minimal two-moment witness, freeze

`m_0 = 1`, `m_1 = 1`.

Candidate positive measures:

`mu_A = delta(x-1)`

and

`mu_B = (1/2) delta(x-1/2) + (1/2) delta(x-3/2)`.

Before evaluating the second moment, note that both are positive and normalized, and both have first moment 1 by construction.

The preregistered decisive quantity is `m_2`.

If `m_2(A) != m_2(B)`, finite lower-moment calibration leaves higher matching data free.

## Mandatory lanes

### Lane A — exact moment witness
Evaluate the frozen measures exactly.

### Lane B — physical interpretation
Relate the abstract witness to dispersive Wilson-coefficient matching without claiming a one-to-one literal spectrum for every gravity coefficient.

### Lane C — finite-vs-complete information audit
Distinguish a finite set of moments/bounds from specification of a full spectral density, UV S-matrix, or microscopic Hamiltonian.

### Lane D — RQIR-facing consequence
State exactly what kind of missing object must be sought in frozen RQIR: not another positivity constraint, but a rule fixing microscopic spectral/state content or equivalent complete generating data.

## Claim ceiling

This is a structural moment-problem witness, not a theorem about all quantum-gravity spectral representations. It does not prove that the true UV completion is discrete, weakly coupled, or described by this one-variable measure.
