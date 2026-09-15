# SF055 Lane B — reproducibility-only repair record

Date: 2026-09-15
Parent gate: `SF055_C3_PROJECTED_FRG_IMPLEMENTATION_CONTRACT`, preregistration `9d998d984566aa5bf290312a6a062fd632c85561`.
Failed validation run: GitHub Actions `34995303477`, job `104469925181`.

## Failure classification

The first independent runner execution recomputed the Lane-B generator successfully and all frozen scientific controls remained PASS, including `Gamma_C3^(2)=0`, the SF052 cubic-tensor match, Bose symmetry for n=3,4,5, and one-common-coupling scaling.

The workflow failed only at byte-for-byte comparison of the committed raw JSON. The differences were machine-level floating/LAPACK diagnostics at approximately `1e-14` to `1e-13`, far below the unchanged scientific tolerance `1e-10`.

Therefore this is classified as an implementation/provenance reproducibility issue, not a scientific Lane-B FAIL.

## Frozen repair scope

This repair is control-only. It MUST NOT change:

- the operator `int sqrt(g) C^3`;
- D=4 flat Euclidean background;
- the square-free functional-derivative expansion;
- external kinematics;
- the single common C3 coupling;
- required vertex orders 3,4,5;
- the SF052 cubic tensor target;
- the frozen scientific tolerance `1e-10`;
- any PASS/BLOCKED criterion of SF055.

Allowed changes are only:

1. replace the SVD-generated TT frame at the fixed SF052 symmetric three-point geometry by the explicit analytic TT frames already used by SF050;
2. evaluate PASS decisions on the full unrounded runtime values exactly as before;
3. serialize machine-stable threshold certificates for near-zero diagnostics rather than platform-dependent `1e-14` residuals;
4. serialize nonzero diagnostic amplitudes with fixed decimal rounding, without using those rounded values for PASS decisions.

## Required retry

The repaired generator must be independently recomputed on GitHub Actions and its canonical raw result must be byte-for-byte stable. Only after that retry succeeds may Lane B be terminalized as `PASS_C3_COMMON_ORIGIN_VERTEX_GENERATOR_SCOPED`.

SF055 overall remains non-terminal regardless of Lane-B outcome; Lane A and implemented Lane C remain separately required. No C3 beta value may be inspected or interpreted.
