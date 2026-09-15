# SF055A — EH/ghost baseline seed engine — INVALID TERMINAL

Date: 2026-09-15
Parent SF055 preregistration: `9d998d984566aa5bf290312a6a062fd632c85561`.
SF055A prospective freeze: `86cf13ac59b03c21d48d67181e755935bfeb152d`.

## CLASSIFICATION

`INVALID_SEED_POSITIVE_CONTROL_MIXED_FOURIER_CONVENTIONS_SCOPED`.

This is **INVALID, not FAIL and not BLOCKED**.

The underlying Einstein-Hilbert / Faddeev-Popov / regulator seed objects remain reconstructible. The prospectively frozen TT positive control mixed two inequivalent momentum conventions.

SF055 remains non-terminal:

`SF055_TERMINAL_PASS = FALSE`.

## EXECUTED RESULT

GitHub Actions first run:

- run `34996889146`;
- job `104475264530` (`seed-engine`);
- implementation head `5073657af9f66885d677b72121b7a0872514f5f9`;
- artifact `10407474111` (`sf055a-eh-ghost-seed-engine`);
- artifact digest `sha256:5c10813938b58018366a754d3412028bc4370b5a36db4a7d1b5e6932dd815464`.

The workflow failed scientifically because the frozen TT two-point control did not pass. The artifact was nevertheless uploaded and its raw JSON is preserved verbatim at

`results/raw/SF055A_EH_GHOST_SEED_ENGINE_FIRST_RUN.json`.

## CONTROLS THAT PASSED

Before the invalid TT criterion was diagnosed, the same source-derived implementation established the following scoped implementation facts:

1. EH n=3 dense control: finite/nonzero, all 6 external permutations agree; raw value `0.005812296859691782`.
2. EH n=4 dense control: finite/nonzero, all 24 permutations agree; raw value `-0.0035006553060195757`.
3. EH n=5 dense control: finite/nonzero, all 120 permutations agree; raw value `0.0010632819763868261`.
4. Landau TT gauge function is zero on the five two-point TT test polarizations.
5. FP ghost two-point controls reproduce `p^2 (bar c.c)` exactly at the tested points.
6. Frozen generic ghost-ghost-h control is nonzero: `-0.3168020092097068`.
7. Ghost h-degree controls give h^2=h^3=0 in the source linear split/gauge implementation.
8. Optimized-regulator denominator controls pass exactly at all frozen q^2 and mu points.
9. Six Appendix-A threshold-function numerical controls pass, with maximum scaled error `3.95e-16`.
10. All eight prospectively frozen counterexample mutations were rejected.

These are seed-level facts only and do not constitute Lane-A PASS.

## FAILED / INVALID CONTROL

The frozen TT control required

`Gamma_TT^(2) = +K_EH (p^2 - 2 Lambda)`, `K_EH=1/(32 pi)`,

while the same preregistration fixed the local real-exponential convention

`partial_mu exp(p_real.x)=p_real,mu exp(p_real.x)`.

The direct covariant generator instead returned for every one of the five TT polarizations and all three Lambda values

`Gamma_raw^(2) = -K_EH (p_real^2 + 2 Lambda)`.

The three representative values are:

- Lambda `0`: `-0.00994718394324346`;
- Lambda `+0.15`: `-0.0129313391262165`;
- Lambda `-0.2`: `-0.00596831036594607`.

## SOURCE-AUTHORITY DIAGNOSIS

The primary source defines the source-Fourier TT coefficient as

`Z_h(p_source^2)(p_source^2 - 2 Lambda^(2))`.

For ordinary Fourier waves `exp(i p_source.x)`, `partial -> i p_source`.

The frozen real-exponential coordinate is related by

`p_source=-i p_real`, hence `p_source^2=-p_real^2`.

Therefore the source coefficient expressed in the frozen real coordinate is exactly

`-K_EH(p_real^2+2 Lambda)`,

matching the executed action generator.

The detailed audit is durable at

`research_log/SF055A_TT_MOMENTUM_CONVENTION_AUDIT.md`.

## NEW FACT

`REAL_EXPONENTIAL_MOMENTUM_COORDINATE != SOURCE_FOURIER_MOMENTUM_COORDINATE`.

A sign check cannot simultaneously use `partial -> p_real` and the uncontinued source formula `+K(p_source^2-2 Lambda)`.

## INTERPRETATION CEILING

No claim is made about:

- a full internal Landau graviton propagator;
- three-point loop integrands;
- Eq. (14) reproduction;
- Lane-A terminal PASS;
- an unprojected C3 loop RHS;
- a C3 beta function or fixed point;
- physical Lorentzian matching.

## NEXT RECOMMENDED GATE

Open a new prospective seed calibration with a single source-faithful Fourier convention throughout:

`partial_mu -> i p_mu`,

retain the published TT target `+K_EH(p^2-2 Lambda)`, regenerate the same EH/FP/regulator controls without changing their scientific thresholds, and only after that seed gate passes proceed to the full Figure-2 Lane-A loop implementation.
