# SF055A3 — batched source-vertex engine equivalence — PROSPECTIVE FREEZE

Date: 2026-09-15
Parent: `SF055A3_SOURCE_FOURIER_BASELINE_LOOP_REPRODUCTION`.
Status: implementation-equivalence freeze before batched-engine output is inspected.

## PURPOSE

Replace repeated directional calls to the already validated scalar source-Fourier EH vertex engine by an exact batched multilinear implementation that returns all requested basis-direction coefficients in one square-free polynomial evaluation.

This is a computational acceleration only. It is not a new physical approximation and may be used in later quadrature only if it reproduces the scalar source engine under the controls below.

## REPRESENTATION

For n legs with requested direction stacks of dimensions `d_i`, every square-free polynomial coefficient is stored with leading shape

`(d_1_or_1, ..., d_n_or_1, geometry_indices...)`.

A leg bit that is absent from a monomial carries leading dimension 1; a present leg carries its full requested basis dimension. Products of disjoint masks use ordinary NumPy broadcasting on these leading axes and the same geometry-index contractions as the scalar engine.

The full-mask coefficient therefore has shape `(d_1,...,d_n)` and is exactly the multilinear directional vertex tensor.

The Fourier convention, EH prefactor, curvature formula, determinant expansion, source gauge conventions and momentum conservation are unchanged:

`partial_mu -> i p_mu`,

`EH_PREF = 1/(16 pi)`.

## POSITIVE EQUIVALENCE CONTROLS

Before use in quadrature require:

1. n=2 TT Hessian tensor: batched 5x5 output equals the scalar engine for every 25 component at lambda values `0`, `-1/20`, `3/20`, max abs error <= `2e-12`.
2. n=3 symmetric-point TT tensor at lambda=0: all 125 components equal scalar source output, max abs error <= `2e-12` and deterministic SHA-256 equals the already-authoritative `T_G` hash `66638b7f47175bfbe0b1fb7234f0c0f5260764da17942b9eedc9af0c35cf8e80`.
3. n=3 zero-momentum lambda tensor: all 125 components equal scalar source output, max abs error <= `2e-12` and SHA-256 equals authoritative `T_Lambda` hash `d4bce18818b05fcaf3e36c78683da0c0ca43db995221462c71131c90ecdf84e5`.
4. n=4 dense conserved momentum control with requested direction dimensions `(2,2,2,2)`: all 16 batched components equal independent scalar calls <= `2e-12`.
5. n=5 dense conserved momentum control with requested direction dimensions `(2,2,2,2,2)`: all 32 batched components equal independent scalar calls <= `3e-12`.
6. Full output is multilinear: scaling one input direction stack by a fixed factor rescales only components using that direction by the same factor; max relative residual <= `2e-12`.
7. Bose permutation controls for n=3,4,5: simultaneous permutation of momenta and leading basis axes reproduces the permuted tensor within `3e-12`.

## NEGATIVE CONTROLS

The equivalence checker must reject at least:

- dropping the Fourier `i` phase;
- changing `EH_PREF` by factor 2;
- allowing overlapping square-free masks to multiply;
- misaligning one batched leading leg axis during a product;
- changing the cosmological-term sign;
- returning only diagonal basis components while declaring a full tensor.

## PASS

`PASS_SF055A3_BATCHED_SOURCE_VERTEX_ENGINE_EQUIVALENT_SCOPED`

only if all positive and negative controls pass.

## FAIL

`FAIL_SF055A3_BATCHED_SOURCE_VERTEX_ENGINE_EQUIVALENCE_SCOPED`

if the batched engine is constructible but differs from the validated scalar engine under any frozen control.

## INTERPRETATION CEILING

Passing authorizes the batched engine only as an exact computational accelerator for the already-defined source vertices. It does not validate quadrature, Eq. (14), Lane A, SF055, or any C3 output.
