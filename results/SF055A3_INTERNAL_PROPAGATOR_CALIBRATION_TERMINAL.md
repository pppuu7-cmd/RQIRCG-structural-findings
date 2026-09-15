# SF055A3 phase A3.1 — Landau-transverse internal propagator/regulator calibration — TERMINAL

Date: 2026-09-15
Parent SF055 preregistration: `9d998d984566aa5bf290312a6a062fd632c85561`.
SF055A3 prospective freeze: `e38e2fcc1a2da0c39be1d2cb28a7c8d5a3db276a`.
Implementation head before durable result: `20b2ce0003b466940d1a46b384d2ef1c15052f3e`.

## RESULT / CLASSIFICATION

`PASS_A3_1_LANDAU_TRANSVERSE_INTERNAL_PROPAGATOR_CALIBRATION_SCOPED`.

This closes only SF055A3 phase A3.1. Lane A and SF055 remain non-terminal.

`SF055_LANE_A_TERMINAL_PASS = FALSE`.

`SF055_TERMINAL_PASS = FALSE`.

No C3 insertion or projected C3 flow was computed or inspected.

## EXECUTED FROZEN CONTROLS

The source gauge map

`F_mu[h;q]=q^nu h_mu nu-(1/2)q_mu tr(h)`

was represented on an orthonormal 10-dimensional real symmetric-tensor basis and its numerical kernel was constructed independently at every frozen nonzero internal momentum.

For all four preregistered q controls:

- `rank F(q)=4`;
- `dim K(q)=6`;
- all five TT polarizations lie in `K(q)` with TT rank 5;
- the one-dimensional transverse non-TT complement survives and has trace magnitude `sqrt(3)` within floating precision;
- the complement is orthogonal to all five TT directions to approximately `10^-16`;
- the source-Fourier EH Hessian is symmetric and reproduces the TT two-point source form;
- the full tensor regulator `R_h=H_0 r` reproduces the frozen regulated TT denominator;
- graviton and ghost inverse residuals are at floating roundoff scale.

Representative worst scales from the executed controls:

- maximum TT Hessian error: `< 6e-18`;
- maximum regulated TT error: `< 2e-17`;
- maximum graviton inverse residual: `< 2.3e-16`;
- maximum ghost inverse residual: `< 1.2e-16`;
- maximum kernel gauge residual: `< 1.4e-16`;
- maximum TT gauge residual: `< 5e-16`.

At the above-cutoff control `q^2=1.44`, the optimized regulator shape returned exactly `r=0` as prospectively frozen.

## COUNTEREXAMPLE-FIRST CONTROLS

All preregistered A3.1 negative controls were rejected:

- TT-only five-dimensional internal graviton replacement;
- deleting the transverse non-TT direction;
- replacing the full source tensor regulator with a scalar identity regulator;
- activating optimized-regulator support above cutoff;
- returning to the predecessor real-exponential momentum convention.

The scalar-regulator mutation differs nontrivially from the source tensor regulator at every below-cutoff control, with maximum-entry distances of order `2.8e-3` to `4.0e-3`.

Therefore external TT projection does not license a TT-only internal propagator in this frozen implementation.

## FIRST CI ATTEMPT / REPRODUCIBILITY REPAIR

The first Actions run `35000050831` reached the completed scientific calculation but failed before output persistence because `numpy.bool_` diagnostic values were not JSON serializable. No physics object, PASS threshold, momentum point, or numerical criterion was changed.

Commit `20b2ce0003b466940d1a46b384d2ef1c15052f3e` changed only the JSON serialization adapter and reran the identical frozen calculation.

This is classified as an implementation/reproducibility repair, not a scientific reroll.

## REPRODUCIBILITY / PROVENANCE

Successful GitHub Actions run:

- run: `35000156977`;
- job: `104486265741` (`internal-propagator`);
- conclusion: `success`;
- executed head: `20b2ce0003b466940d1a46b384d2ef1c15052f3e`;
- artifact id: `10409790029`;
- artifact name: `sf055a3-internal-propagator-calibration`;
- artifact digest: `sha256:09a4604d5eee8c1af801b958d58191a309e1a50f31555d0208efabc42461cb65`.

Durable files:

- `prereg/SF055A3_SOURCE_FOURIER_BASELINE_LOOP_REPRODUCTION_PREOUTCOME.md`;
- `scripts/sf055a3_internal_propagator_calibration.py`;
- `.github/workflows/sf055a3-internal-propagator-calibration.yml`;
- `results/raw/SF055A3_INTERNAL_PROPAGATOR_CALIBRATION.json`;
- this terminal note.

## NEW IMPLEMENTATION FACT

Within the frozen D=4 flat-Euclidean source-Fourier Landau realization, the internal graviton object required by the baseline three-point flow is numerically constructible as a six-dimensional transverse tensor subspace containing the five TT directions plus one independent transverse non-TT direction, with the source EH Hessian and source tensor regulator invertible and stable on the preregistered controls.

## INTERPRETATION CEILING

This PASS does not validate the Figure-2 loop contractions, loop routing, momentum integration, external three-point extraction, Eq. (14) reproduction, Lane-A terminal PASS, or any C3 flow quantity.

## NEXT REQUIRED DEPENDENCY

`A3.2_FIGURE2_BASELINE_LOOP_ASSEMBLY_AND_EQ14_REPRODUCTION`.

The next calculation must use this full six-dimensional internal Landau-transverse object, the already-passed SF055A2 source-Fourier EH/FP seed machinery, and the already-passed Lane-C Figure-2 topology/coefficient manifest. It must keep C3 disabled and reproduce the frozen published baseline through the same code path before any C3 output becomes authorized.
