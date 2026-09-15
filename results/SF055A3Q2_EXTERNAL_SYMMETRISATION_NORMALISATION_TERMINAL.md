# SF055A3Q2 — Figure-2 external symmetrisation normalization — TERMINAL

Date: 2026-09-15
Prospective freeze: `9e26ddae3d40d8a1e96330304b639947d0b3e681`.
Executed implementation head: `b9e99399176633e9bcb64e1e8aeec9756abec840`.

## CLASSIFICATION

`PASS_SOURCE_EXTERNAL_SYMMETRISATION_NORMALISATION_SCOPED`.

This closes one absolute source-bookkeeping factor required before integrated Eq. (14) comparison.

It does **not** terminalize SF055A3 Lane A or SF055.

No C3 flow was computed or inspected.

## EXACT LABELLED INVERSE-PROPAGATOR COMBINATORICS

For `G=A^{-1}` and three distinct commuting fluctuation derivatives, the executed noncommutative product-rule expansion gives, before the overall bosonic `1/2`:

- one `Gamma5` / `A_(123)` term, coefficient `-1`;
- six labelled `Gamma4*Gamma3` terms, each coefficient `+1`;
- six labelled `Gamma3^3` terms, each coefficient `-1`.

Therefore the exact bosonic weight per labelled term is

- five-vertex: `-1/2` for the unique fully symmetric term;
- 4/3 terms: `+1/2` each;
- 3/3/3 graviton terms: `-1/2` each.

For the FP ghost inverse, the six triangle orderings carry inverse-derivative coefficient `-1`; the Grassmann supertrace contributes another minus, giving `+1` per labelled ghost-triangle term.

## SOURCE FIGURE-2 COEFFICIENT MATCH

The already-frozen source coefficients are

`(-1/2, +3, -3, +6)`

for `(T5_GRAV, B43_GRAV, T333_GRAV, T333_GHOST)`.

Define the source external symmetrisation operator on one canonical labelled representation as

`Sym_3 = (1/6) sum_(sigma in S3)`.

Then the effective labelled weights are exactly

- `(-1/2)` for the permutation-invariant five-vertex object;
- `+3/6 = +1/2` for each 4/3 labelled term;
- `-3/6 = -1/2` for each graviton triangle labelled term;
- `+6/6 = +1` for each ghost triangle labelled term.

These exactly reproduce the functional-derivative expansion.

The competing interpretation

`Sym_3 = sum_(sigma in S3)`

would instead assign effective weights `(-3,+3,-3,+6)` and fails the exact derivative combinatorics, including the five-vertex control.

Thus, in the frozen Figure-2 coefficient convention,

`SOURCE_SYM_3 = (1/6) SUM_OVER_S3_LABELLED_EXTERNAL_PERMUTATIONS`.

This result is obtained without any Eq. (14) target value.

## LOOP MEASURE AUTHORITY

The source flow definition uses

`int d^4 q / (2 pi)^4`.

This factor is therefore fixed before quadrature and may not be adjusted by baseline matching.

## COUNTEREXAMPLE-FIRST RESULT

The sum-vs-average mutation was explicitly tested:

- normalized average: exact combinatoric match;
- unnormalized sum: mismatch.

The ghost sign was also independently controlled from inverse differentiation plus the supertrace sign.

## REPRODUCIBILITY / PROVENANCE

GitHub Actions:

- run: `35016518420`;
- job: `104541230200`;
- conclusion: `success`;
- head: `b9e99399176633e9bcb64e1e8aeec9756abec840`;
- artifact id: `10416150077`;
- artifact name: `sf055a3q2-external-sym-normalization`;
- artifact digest: `sha256:afa657ca7a4c8e70eff5013c91123c63ef352b025a63f1f2062edc7120538f85`.

## NEW IMPLEMENTATION FACT

The external-permutation normalization and loop measure required for absolute Figure-2 baseline integration are now source-locked independently of Eq. (14):

`Sym_3=(1/6) sum_S3`,

`int_q = int d^4q/(2 pi)^4`.

## INTERPRETATION CEILING

No quadrature, Eq. (14) reproduction, Lane-A PASS, SF055 PASS, C3 beta function, fixed point, regulator-independence, Lorentzian matching, or physical SF025 coefficient is established here.

## NEXT REQUIRED DEPENDENCY

Continue the already-active exact-TT projector regrouping workflow. If that implementation-equivalence gate passes, use the grouped projector with the source-normalized `Sym_3` above in the frozen `N=8,12,16,24` quadrature. If it fails, fall back to the brute-force complete TT contraction without changing the Lane-A science contract.
