# RQIRCGSF research ledger — SF055 Lane B addendum

Date: 2026-09-15

## STATE_READ

- parent RQIRCG remains parked on `WAIT_FOR_EXPLICIT_PROGRAMME_DISPOSITION_DECLARATION`;
- SF055 parent preregistration: `9d998d984566aa5bf290312a6a062fd632c85561`;
- merged preflight commit: `c2b888363267d25b9e1443b6ce545abf3d396688`;
- preflight Actions run: `34993910636`, success, preflight-only;
- SF055 terminal PASS remained false before Lane-B construction.

## ITERATION QUERY

Highest-information bounded task selected for this iteration:

`Construct the one-common-coupling covariant C3 vertex generator before any C3 beta calculation; require Gamma2=0, full SF052 cubic match, Bose symmetry through n=5, common-coupling scaling, and independent reproducible CI before promoting Lane B.`

Rationale: this is a fatal upstream calibration object for all later C3 loop insertions and is much cheaper than implementing the full EH/ghost loop flow first.

## WORK_PERFORMED

A square-free multivariate flat-background expansion of the single operator `int sqrt(g) C^3` was implemented through n=5.

The first independent CI run `34995303477` found only byte-level floating serialization drift while recomputing all science controls successfully. A prospective reproducibility-only repair was frozen at commit `45845f09c0e08f816c19997a11dfdb0e3abcd714`.

Repair V2 uses the explicit SF050 analytic TT frame at the fixed SF052 geometry and serializes platform-stable threshold certificates; the science tolerance remains exactly `1e-10` on unrounded runtime values.

Independent retry run `34995827603`, job `104471676663`, passed all steps including byte-stable raw reproduction and artifact upload.

## RESULT

`PASS_C3_COMMON_ORIGIN_VERTEX_GENERATOR_SCOPED`.

Controls:

- `Gamma_C3^(2)=0`;
- all 125 SF052 cubic TT components match up to one common `3! = 6` functional-derivative factor;
- n=3,4,5 Bose tests cover 6, 24, 120 permutations respectively;
- zero/double common-coupling controls pass for n=3,4,5;
- no independent higher-vertex C3 coefficients are used.

Artifact id `10407234167`, digest `sha256:7db9004088f78bb8513c84373a5c4688790e28749727af866ab56a7518048e9c`.

## CLASSIFICATION

Lane B: terminal PASS scoped.

SF055 overall: NON-TERMINAL.

## NEW FACT

The SF054 correlated C3 3/4/5 requirement is computationally realizable from one covariant deformation in the frozen flat-Euclidean implementation.

## CLAIM CEILING

No C3 beta, fixed point, physical matching coefficient, regulator-independent result, background/fluctuation equality, quantum `chi_ABC`, parent authority, full-QG or new-physics claim.

## NEXT HIGHEST-INFORMATION WORK

1. Lane A: reproduce the prospectively frozen published EH/ghost baseline through the same diagram-generator code path, not by hard-coding Eq. (14).
2. Lane C: connect the implemented diagram topologies to the frozen machine-readable one-C3 insertion manifest and validate all allowed/forbidden slots.
3. Only if A/B/C terminalize may an actual projected C3 beta output be inspected.
