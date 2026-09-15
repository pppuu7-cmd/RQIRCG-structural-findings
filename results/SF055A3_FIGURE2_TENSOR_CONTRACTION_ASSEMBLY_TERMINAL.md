# SF055A3 — Figure-2 fixed-q tensor contraction assembly — TERMINAL

Date: 2026-09-15
Parent SF055A3 gate: `prereg/SF055A3_SOURCE_FOURIER_BASELINE_LOOP_REPRODUCTION_PREOUTCOME.md`.
Prospective contraction-interface freeze: `ec44f446d5c8f8fd91bfbc3b4fd46e9a5468f06d`.
Executed implementation head: `13317f3165d7f1afa9eae92a76f8971c19920388`.

## CLASSIFICATION

`PASS_A3_2_FIGURE2_TENSOR_CONTRACTION_ASSEMBLY_SCOPED`.

This closes fixed-q tensor contraction assembly only.

`SF055_LANE_A_TERMINAL_PASS = FALSE`.

`SF055_TERMINAL_PASS = FALSE`.

`C3_ENABLED = FALSE`.

## EXECUTED OBJECT

The baseline Figure-2 EH/ghost contractions were assembled from the already-passed source-Fourier seed vertices, the A3.1 six-dimensional Landau-transverse internal graviton spaces, the source tensor regulator, the frozen single-scale line

`S=G dotR G`,

and the inherited source coefficients

`(-1/2,+3,-3,+6)`

for `(T5_GRAV,B43_GRAV,T333_GRAV,T333_GHOST)`.

The canonical q edge was the differentiated line. All other internal edges carried ordinary regulated propagators. A single stored internal tensor basis was shared across the two opposite-momentum endpoints of each graviton edge, preventing arbitrary SVD-basis rotations from contaminating the contraction.

## FIXED-Q SCIENTIFIC CONTROLS

Two prospectively frozen dense loop controls were executed with external symmetric-point TT indices `(0,1,2)`.

At

`q1=(0.23,-0.31,0.17,0.29)`:

- `T5_GRAV = 0.958801881718869`;
- `B43_GRAV = -2.377571118958953`;
- `T333_GRAV = -0.708106137422964`;
- `T333_GHOST = 0.07586734663176124`.

At

`q2=(0.41,0.12,-0.27,0.19)`:

- `T5_GRAV = -1.3864528599809398`;
- `B43_GRAV = 1.563041804307983`;
- `T333_GRAV = 2.3819817770174008`;
- `T333_GHOST = -0.21823132873611936`.

Every topology was therefore numerically exercised with a finite nonzero value on at least one frozen control.

All six labelled external permutations were generated for every topology at both q controls before any later symmetry reduction.

## BASIS / PROPAGATOR ROBUSTNESS

Consistent independent orthogonal rotations of every internal graviton edge basis left the contracted scalar invariant at floating precision.

Largest observed absolute transformed-minus-canonical difference:

`1.6431300764452317e-14`.

Largest internal inverse residual:

`3.171254240824062e-16`.

The frozen full-loop ghost-arrow reversal control was exact to displayed floating precision.

## COUNTEREXAMPLE-FIRST CONTROLS

All frozen mutations were rejected:

- TT-only 5D internal graviton basis;
- untransported independent endpoint basis rotation;
- `G dotR` substituted for `G dotR G`;
- single-scale insertion moved to a noncanonical edge without coherent routing/regulator change;
- omitted ordinary bubble propagator;
- omitted ordinary triangle propagator;
- wrong ghost matrix order;
- wrong ghost `p_c` assignment;
- wrong inherited topology coefficient;
- scalar-identity graviton regulator substituted for `H0 r`.

This explicitly preserves

`EXTERNAL_TT_PROJECTION != TT_ONLY_INTERNAL_PROPAGATION`

and

`SINGLE_SCALE_PROPAGATOR = G dotR G`, not `G dotR`.

## REPRODUCIBILITY / PROVENANCE

Successful GitHub Actions run:

- run: `35000997597`;
- job: `104489066892` (`fixed-q-contraction`);
- executed head: `13317f3165d7f1afa9eae92a76f8971c19920388`;
- artifact id: `10409825944`;
- artifact name: `sf055a3-figure2-contraction`;
- artifact digest: `sha256:bc558d2fa44d1cde0103b6f4ca1bc059b1740161927c63fb847cb008f51fe4bb`.

Durable implementation/results:

- `research_log/SF055A3_FIGURE2_CONTRACTION_INTERFACE_FREEZE.md`;
- `scripts/sf055a3_figure2_contraction_assembly.py`;
- `.github/workflows/sf055a3-figure2-contraction.yml`;
- `results/raw/SF055A3_FIGURE2_CONTRACTION_ASSEMBLY_SUMMARY.json`;
- this terminal note.

## NEW IMPLEMENTATION FACT

Within the frozen source-Fourier Landau realization, the complete baseline Figure-2 tadpole, graviton bubble, graviton triangle and ghost triangle tensor contractions are constructible at fixed loop momentum from the same source-derived vertex/propagator code path, are insensitive to consistent internal tensor-basis rotations, and survive explicit contraction-level counterexample tests.

## INTERPRETATION CEILING

This result does not establish the integrated three-point flow. No quadrature convergence, Eq. (14) baseline reproduction, Lane-A terminal PASS, C3 projected beta function, UV fixed point, regulator independence, Lorentzian matching, or successor selector is authorized.

## NEXT REQUIRED DEPENDENCY

`DETERMINISTIC_FIGURE2_QUADRATURE_AND_EQ14_BASELINE_REPRODUCTION`.

The next gate must integrate this exact baseline contraction object under the already-frozen SF055A3 quadrature sequence and then reproduce all three frozen Eq. (14) targets through the same code path. No C3 insertion is permitted before that calibration terminalizes.
