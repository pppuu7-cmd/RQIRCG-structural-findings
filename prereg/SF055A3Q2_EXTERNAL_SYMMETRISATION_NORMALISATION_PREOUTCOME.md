# SF055A3Q2 — Figure-2 external symmetrisation normalization — PREOUTCOME

Date: 2026-09-15
Parent gate: `SF055A3_SOURCE_FOURIER_BASELINE_LOOP_REPRODUCTION_PREOUTCOME`.

## PURPOSE

Fix the absolute normalization of the source statement “all diagrams are symmetrised with respect to interchange of external momenta” before any Eq. (14) integrated comparison. The normalization must be derived from the functional derivatives of the Wetterich trace and the already-source-frozen Figure-2 coefficients, never selected by target matching.

This gate does not change topology coefficients, loop measure, vertices, propagators, regulator, projectors, or numerical tolerances.

## SOURCE OBJECT

At vanishing fluctuation field, with a field-independent regulator insertion under fluctuation differentiation, write

`G=(Gamma^(2)+R)^(-1)`.

Take three labelled commuting fluctuation derivatives `D1 D2 D3` of the bosonic Wetterich trace `1/2 Tr[G dotR]`, and separately of the FP ghost trace with its Grassmann supertrace sign.

Identify the resulting source topology classes:

- one five-vertex tadpole;
- six labelled 4/3 terms before trace/orientation equivalence;
- six labelled 3/3/3 terms;
- six labelled ghost-triangle terms.

## FROZEN QUESTION

Let `Sym_3` act on one canonical labelled topology over all six permutations of `(p1,p2,p3)`.

Determine whether the published Figure-2 coefficients

`(-1/2, +3, -3, +6)`

are consistent with

A. `Sym_3 = sum_{sigma in S3}`,

B. `Sym_3 = (1/6) sum_{sigma in S3}`,

or neither,

when compared term-by-term with the exact three-functional-derivative combinatorics.

No Eq. (14) beta value may enter this determination.

## REQUIRED CONTROLS

1. A symbolic/noncommutative derivative expansion of `D1 D2 D3 G` must reproduce one `Gamma5`, six `Gamma4*Gamma3`, and six `Gamma3^3` labelled terms with the correct signs before the global bosonic `1/2`.
2. The ghost inverse derivative must reproduce six labelled ghost-triangle terms with the supertrace sign.
3. Permutation labels must be retained explicitly; no numerical equality at symmetric kinematics may be used to collapse terms before counting.
4. Applying the inferred `Sym_3` convention to a canonical representative must reproduce exactly the published Figure-2 coefficients without any fitted multiplier.
5. A sum-vs-average mutation must be rejected unless both are mathematically indistinguishable under the published coefficient convention (in which case classification is BLOCKED rather than selecting one).

## PASS

`PASS_SOURCE_EXTERNAL_SYMMETRISATION_NORMALISATION_SCOPED`

if the functional-derivative combinatorics uniquely determine the source symmetrisation normalization together with the published coefficients.

## BLOCKED

`BLOCKED_SOURCE_SYMMETRISATION_NORMALISATION_AMBIGUOUS`

if both conventions remain compatible after exact combinatorics and source coefficient accounting.

## FAIL

`FAIL_SOURCE_FIGURE2_COMBINATORICS_MISMATCH_SCOPED`

if neither convention can reproduce the source coefficients from the differentiated Wetterich trace.

## INTERPRETATION CEILING

This is an absolute-normalization/source-bookkeeping result only. It is not quadrature, Eq. (14) reproduction, Lane-A PASS, SF055 PASS, or any C3 result.
