# SF055 Lane-B common C3 generator — reconciliation audit

Date: 2026-09-15
Current main read before this audit: `66c79bf6e18fd2ed0ff59e87af81751c996dd813`.
Parent authority: SF055 preregistration `9d998d984566aa5bf290312a6a062fd632c85561`.

## PURPOSE

Reconcile two concurrent GitHub-resident implementation/audit lines without rewriting either result and without promoting a failed/invalid control to PASS after outcome inspection.

## CURRENT MAIN RESULT RETAINED

Main contains the common-origin square-free covariant `sqrt(g) C^3` generator at commit

`2a7b350fbbfd9993aba914fd6a5a367c252744e3`,

with raw Lane-B result committed at

`66c79bf6e18fd2ed0ff59e87af81751c996dd813`.

That result reports

`PASS_C3_COMMON_ORIGIN_VERTEX_GENERATOR_SCOPED`

for the original SF055 Lane-B requirements:

- `Gamma_C3^(2)=0` on flat background;
- all 125 SF052 symmetric-point TT cubic components reproduce the C3 tensor with one global functional-derivative factor 6;
- one common covariant generator produces n=3,4,5 contracted vertices;
- generic n=3,4,5 controls scale linearly with the single common coupling;
- the tested vertices are Bose symmetric over all `3!`, `4!`, `5!` permutations;
- no FRG loop or C3 beta function is claimed.

This main result remains the current Lane-B authority unless a prospectively valid counterexample actually falsifies one of those original requirements.

## MAIN CI FAILURE IS INFRASTRUCTURAL, NOT A SCIENTIFIC FAIL

GitHub Actions run `34995303477`, job `104469925181`, recomputed the full Lane-B result successfully and retained every scientific PASS/classification flag. The job failed only because a byte-for-byte `git diff` saw platform-dependent floating differences of order roughly `1e-14` to `1e-16` in otherwise equivalent NumPy outputs.

This reconciliation branch replaces byte identity with a recursive JSON comparison that keeps strings/booleans/structure exact and permits only `1e-12` relative/absolute floating variation. That tolerance is far tighter than the Lane-B scientific control threshold `1e-10` and does not change any scientific criterion.

## CONCURRENT PROSPECTIVE STRICTER CONTROL — PRESERVED, NOT RESCUED

A concurrent branch `sf055-c3-generator-20260915` prospectively froze an additional stricter implementation control at commit

`3954844e318235d77eef85e6dfed3906d606f6b1`

before its output was inspected.

Its committed raw result `e786913608452a69cda83694dd14c30015da25b3` found:

- B0 n=2: PASS, exactly zero;
- B1 all 125 SF052 n=3 TT components: PASS, global factor 6 with maximum ratio error at the `1e-14` level;
- B3 n=5 fixed control: PASS and Bose symmetric;
- B4 common-origin API control: PASS;
- frozen B2 fixed n=4 positive-control component: exactly zero under the tested adjacent permutations.

Because B2 had prospectively required that one chosen component to be nonzero, that subtest is correctly classified

`INVALID_FROZEN_B2_POSITIVE_CONTROL_ACCIDENTAL_NULL_SCOPED`,

with `lane_B_terminal_pass=false` **for that stricter subtest**.

A post-outcome diagnostic at the same four momenta but a different explicitly stated TT polarization returned a nonzero Bose-symmetric value near `2.79166666666667`, demonstrating that the frozen B2 choice was an accidental component null. This diagnostic does not retroactively change B2 to PASS.

### Why this does not falsify the main Lane-B PASS

The original SF055 Lane-B contract requires common origin, Bose symmetry, the flat two-point zero, and the SF052 three-point response. It does not require every four-graviton TT polarization component of `C^3` to be nonzero.

Therefore one prospectively chosen four-point TT component being zero is compatible with a nonzero four-point vertex and with the original Lane-B PASS. The correct preserved distinction is

`ONE_FIXED_C3_FOUR_POINT_TT_COMPONENT_ZERO != GAMMA_C3^(4)_IDENTICALLY_ZERO`.

## INDEPENDENT DIRECT-GEOMETRY VERIFIER — FROZEN MISMATCH PRESERVED

The same concurrent branch prospectively froze an independent ordinary-metric finite-difference verifier at commit

`25d5580a2658294809dfaab274e1b681789b34a9`.

Raw result commit `c6d7404b9106272445f8e08b4dd6017573ece205` classified the frozen test

`COMMON_C3_GENERATOR_CROSS_IMPLEMENTATION_MISMATCH_SCOPED`.

V2, V3 and V5 passed and all direct geometric Weyl/metric controls passed. V4 missed the prospectively frozen tolerance when using Richardson steps `h=0.04,0.02`:

`D_R = 2.7914038347477956`

versus target approximately

`2.791666666666668`.

This mismatch is not erased.

Post-outcome step-halving diagnostic commit `07f3af187445144c96f9b941034166994133f097` showed convergence toward the square-free target:

- `(0.04,0.02)`: error about `-2.63e-4`;
- `(0.02,0.01)`: error about `-1.60e-5`;
- `(0.01,0.005)`: error about `-9.91e-7`;
- `(0.008,0.004)`: error about `-4.06e-7`.

This strongly diagnoses finite-difference truncation in the frozen coarse-step verifier, but because it is post-outcome it does not convert the frozen SF055B verdict into PASS.

## RECONCILED STATUS

Retain simultaneously:

1. main Lane-B classification: `PASS_C3_COMMON_ORIGIN_VERTEX_GENERATOR_SCOPED`;
2. additional frozen B2 classification: `INVALID_FROZEN_B2_POSITIVE_CONTROL_ACCIDENTAL_NULL_SCOPED`;
3. independent coarse-step SF055B classification: `COMMON_C3_GENERATOR_CROSS_IMPLEMENTATION_MISMATCH_SCOPED`;
4. post-outcome convergence evidence supports a numerical-step explanation but is not an independent PASS.

There is no logical contradiction among these statements because their frozen success conditions differ.

## NEW SCIENTIFIC / IMPLEMENTATION FACTS

- A single covariant `sqrt(g) C^3` generator has a nonzero four-point sector even though particular TT components can vanish exactly.
- The SF052 cubic C3 tensor is reproduced by the full covariant action derivative with one global factor 6.
- Direct ordinary-metric geometry agrees well at n=2,3,5 and converges toward the square-free n=4 value under step refinement, but the prospectively frozen coarse V4 tolerance was not met.

## INTERPRETATION CEILING

This reconciliation does **not** establish:

- an independently PASSed direct-geometry verification under the frozen SF055B criterion;
- a projected C3 beta function;
- baseline EH/ghost FRG reproduction;
- implemented Lane-C diagram completeness;
- regulator/scheme independence;
- background/fluctuation equality;
- Lorentzian on-shell matching or a successor selector.

## NEXT DEPENDENCIES

Lane B may remain closed under the original SF055 contract, with the additional audit qualifications above.

The blocking implementation work is now:

1. Lane C: source-faithful implemented three-point Wetterich topology/insertion manifest including every allowed one-C3 insertion from the common n=3,4,5 generator;
2. Lane A: reproduce the frozen published EH/ghost projected three-point baseline from the same loop implementation;
3. only after both are terminal may a substantive `P_E_6d[F3_TT]` C3 flow output be inspected.
