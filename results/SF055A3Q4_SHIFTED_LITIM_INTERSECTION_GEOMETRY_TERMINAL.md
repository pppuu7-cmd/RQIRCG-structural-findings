# SF055A3Q4 — shifted Litim intersection geometry and piecewise equivalence — TERMINAL

Date: 2026-09-16
Prospective preregistration: `cd4176921f009761250fc4a25c3e1dfb9841ce1d`.
Control-only repair freeze: `124f712679aa912f1a710674a695a33ced3befa7`.
Repository checker: `scripts/sf055a3q4_shifted_litim_geometry.py`, commit `176765d9e6e263ed8402ced0889fb7f3fa240472`.
Durable local raw: `results/raw/SF055A3Q4_SHIFTED_LITIM_INTERSECTION_GEOMETRY_LOCAL.json`, commit `9c9c817fee073fc10c19dcdb525d27a06eaacaf5`.

## CLASSIFICATION

`PASS_SHIFTED_REGULATOR_INTERSECTION_GEOMETRY_AND_PIECEWISE_EQUIVALENCE_SCOPED`.

This is an implementation-geometry/equivalence PASS only.

The historical baseline remains

`BLOCKED_LANE_A_BASELINE_QUADRATURE_NOT_CONVERGED_SCOPED`.

`SF055_TERMINAL_PASS = FALSE`.

No substantive C3 projected-flow output is authorized.

## EXACT CANONICAL SHIFT CENSUS

For the frozen symmetric Figure-2 routing, the shifted non-differentiated propagators are

- `ell=q+p0+p1`, shift direction `(1/2,+sqrt(3)/2)`;
- `e23=q-p1`, shift direction `(1/2,-sqrt(3)/2)`;
- `e31=q+p0`, shift direction `(1,0)`.

All three shift vectors have magnitude `p`.

The differentiated line q remains supported on `q^2<1` and is not changed.

## EXACT INTERSECTION GEOMETRY

With the already-frozen reduced coordinates

`q=(sqrt(x(1-y)) cos(phi), sqrt(x(1-y)) sin(phi), sqrt(x y), 0)`,

set `r=sqrt(x)` and

`c=sqrt(1-y) cos(phi-alpha)`.

For any canonical shift `a` of magnitude p,

`|q+a|^2=1`

is exactly

`r^2 + 2 p c r + p^2 = 1`.

The nonnegative boundary root is

`r_b = -p c + sqrt(1-p^2+p^2 c^2)`.

An interior/boundary crossing is active iff

`c > -p/2`,

with equality at `r_b=1`.

The angular birth/death curves are

`phi = alpha +/- arccos[-p/(2 sqrt(1-y))]`

when `sqrt(1-y)>=p/2`, and the angular topology changes at

`y_* = 1-p^2/4`.

The resulting nested partition is therefore source- and routing-defined; no target value enters it.

## EXECUTED GEOMETRY CONTROLS

The exact retry after the prospectively frozen control-only repair gave:

- boundary roots tested: `303`;
- maximum direct boundary residual: `4.440892098500626e-16`;
- phi intervals tested: `110`;
- all phi active-shift sets constant on frozen interior samples;
- radial intervals tested: `645`;
- maximum radial partition coverage error: `0.0`;
- all radial support bit-vectors constant on frozen interior samples.

Thus the exact shifted-sphere surfaces generate a complete no-gap/no-overlap partition in the executed controls.

## SMOOTH-INTEGRAND EQUIVALENCE

Using the same parent reduced measure

`x/(32 pi^3) dx dy dphi`,

the N=24 piecewise integration reproduced two analytic smooth controls:

- constant integrand result `1/(32 pi^2)` with absolute error `5.204170427930421e-18`;
- x integrand result `1/(48 pi^2)` with absolute error `1.214306433183765e-17`.

This directly checks that the partition itself does not alter the parent integral measure.

## SCALAR LITIM-SHELL CONTROL

For the same scalar optimized-denominator control used in the post-baseline derivative audit, the new reduced-coordinate piecewise implementation was compared with an independent polar split:

At `p=1/8`:

- piecewise N24: `-1.976210890335743e-05`;
- independent polar N64: `-1.976210929438266e-05`;
- relative difference: `1.978661416381604e-08`.

At `p=1/32`:

- piecewise N24: `-1.2673470664854288e-06`;
- independent polar N64: `-1.2673466493857005e-06`;
- relative difference: `3.291125821931293e-07`.

At the prospectively frozen small momentum `p=1/256`,

`Delta J/p^2 = -0.001307066879642879`,

while the independently derived continuum coefficient is

`-1/[64 pi^2 (1+mu)^2] = -0.0013083830532326674`.

Relative difference: `0.0010059543239547334` (about 0.1006%), within the frozen 0.5% Q4 control.

## DIRECT COUNTEREXAMPLE TO UNSPLIT FINITE GRID

For N=24 the frozen safe momentum is

`p_safe = 0.00030097992802030626`.

At exactly this momentum:

- unsplit finite-grid shell contribution: `0.0`;
- piecewise shell contribution: `-1.1851582767804493e-10`.

Therefore a finite interior Gauss grid can return an exactly zero shell contribution even though the same continuum integral has a nonzero contribution of the correct sign. The piecewise construction removes this specific node-missing mechanism without changing the regulator or integral.

This confirms the regulator-shell mechanism as a real numerical pathology in the scalar control. It does **not** prove that it is the sole or quantitatively complete source of the gravitational baseline convergence failure.

## NEGATIVE CONTROLS AND REPAIR CHRONOLOGY

All final frozen negative controls passed:

- omission of a canonical shifted line rejected;
- canonical shift-sign reversal rejected;
- wrong radial-root branch rejected;
- omission of angular birth/death breakpoints rejected;
- frozen shifted support while moving q rejected;
- smoothed-regulator substitution rejected;
- target-dependent root clipping rejected.

The first local dry run had an ineffective frozen-support mutation because both hard-coded radial probes were on the same side of the shell. That first attempt is retained as `INVALID_NEGATIVE_CONTROL_IMPLEMENTATION / NON_TERMINAL`.

Before retry, commit `124f7126...` prospectively froze the control-only repair: choose probes on opposite sides of the exact root. No positive result, formula, tolerance, source object, regulator, momentum point, N sequence or science criterion changed.

A separate initial JSON `numpy.bool_` serialization issue was serialization-only and did not alter calculation criteria.

## REPRODUCIBILITY

Local exact retry was executed synchronously after the repair freeze.

Local source hashes before repository transfer:

- checker SHA256: `44ad6ada243e8a6cb6a3dd710a20caa82f9509f68365101e9db4b67adfeedbd6`;
- raw-output SHA256: `79fc954419d5c505530a89adcd6c5c61dcf7e9a36e059043653f75f456f2e4a1`.

The equivalent checker and raw output are durable in the repository. An independent GitHub Actions reproduction was launched as run `35038554188`; at terminalization it was queued, so queue/green status is not used as a scientific premise. The workflow is retained as additional reproducibility provenance when infrastructure executes it.

## NEW IMPLEMENTATION FACT

The exact shifted optimized-regulator intersection surfaces for all canonical non-differentiated Figure-2 lines can be used as nested quadrature boundaries in the existing reduced coordinates without changing the integral. The scalar control demonstrates that this partition captures continuum thin-shell contributions that the original unsplit finite grid can miss exactly.

## AUTHORIZED NEXT STEP

`FULL_TENSOR_PIECEWISE_BASELINE_IMPLEMENTATION_RETRY_UNDER_ORIGINAL_FREEZE`.

A successor implementation may now incorporate the Q4 partition into the SAME full tensor integrals while preserving:

- source objects and topology coefficients;
- external momentum points;
- Q1/Q2 normalisations;
- original Richardson stencil;
- original `N={8,12,16,24}` sequence;
- original convergence/target thresholds;
- C3 disabled.

Derivative truncation error remains a separate required control; Q4 does not establish it.

## INTERPRETATION CEILING

`Q4_GEOMETRY_PASS != BASELINE_PASS`.

`SCALAR_SHELL_MECHANISM != PROVEN_FULL_TENSOR_SOLE_ERROR_SOURCE`.

`Q4_GEOMETRY_PASS != SF055_PASS`.

No projected C3 beta, physical SF025 b, background/fluctuation equality, regulator-independent AS prediction or Lorentzian matching coefficient is obtained here.