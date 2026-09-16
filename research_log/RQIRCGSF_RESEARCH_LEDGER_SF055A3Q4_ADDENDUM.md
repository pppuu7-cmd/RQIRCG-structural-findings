# RQIRCGSF research ledger — SF055A3Q4 addendum

Date: 2026-09-16

## STATE READ

Parent RQIRCG remained parked on `WAIT_FOR_EXPLICIT_PROGRAMME_DISPOSITION_DECLARATION`.

Successor authority had advanced autonomously to a completed SF055A3 baseline run with terminal classification

`BLOCKED_LANE_A_BASELINE_QUADRATURE_NOT_CONVERGED_SCOPED`.

All N24 targets were within the frozen 1% target tolerance, but N16-to-N24 convergence failed for beta_g and beta_lambda3. beta_mu had already converged and matched; it was not the active blocker.

The post-run derivative audit identified severe Richardson error amplification and a scalar shifted-Litim thin-shell control that finite unsplit grids can miss.

## GENERATED ITERATION QUERY

The chosen maximum-information successor was:

derive the exact shifted optimized-regulator intersection surfaces for all canonical Figure-2 shifted propagators and prove that a piecewise quadrature partition evaluates the same frozen integral, before any new full tensor baseline retry.

No C3 output was inspected.

## PREREGISTRATION

`prereg/SF055A3Q4_SHIFTED_LITIM_INTERSECTION_GEOMETRY_PREOUTCOME.md`

commit `cd4176921f009761250fc4a25c3e1dfb9841ce1d`.

Frozen science constraints retained the original source objects, regulator, momentum ladder, Richardson stencil, N sequence and thresholds.

## CONTROL-ONLY REPAIR

First local dry run exposed an ineffective negative-control mutation: two hard-coded radial samples were accidentally on the same side of the exact shell. All positive controls had passed, but the run was not accepted.

Before retry the repair was frozen in

`research_log/SF055A3Q4_CONTROL_ONLY_REPAIR_FREEZE.md`,

commit `124f712679aa912f1a710674a695a33ced3befa7`.

The only scientific-control change was to choose the negative-control probe points on opposite sides of the already-frozen exact shell root. A separate numpy-bool JSON adapter was serialization-only.

## EXECUTED RESULT

Checker:

`scripts/sf055a3q4_shifted_litim_geometry.py`, commit `176765d9e6e263ed8402ced0889fb7f3fa240472`.

Raw:

`results/raw/SF055A3Q4_SHIFTED_LITIM_INTERSECTION_GEOMETRY_LOCAL.json`, commit `9c9c817fee073fc10c19dcdb525d27a06eaacaf5`.

Terminal:

`results/SF055A3Q4_SHIFTED_LITIM_INTERSECTION_GEOMETRY_TERMINAL.md`, commit `9b3933fe70b0042374b10c9d25f5fb05fb01048f`.

Classification:

`PASS_SHIFTED_REGULATOR_INTERSECTION_GEOMETRY_AND_PIECEWISE_EQUIVALENCE_SCOPED`.

Key exact geometry:

`r_b=-p c+sqrt(1-p^2+p^2 c^2)`,

`c=sqrt(1-y) cos(phi-alpha)`,

active iff `c>-p/2`,

angular topology boundary `y_*=1-p^2/4`.

Executed controls:

- 303 shell roots, max residual `4.440892098500626e-16`;
- 110 phi intervals, active sets constant;
- 645 radial intervals, max coverage error `0.0`;
- smooth integral controls absolute errors `5.20e-18` and `1.21e-17`;
- scalar piecewise-vs-independent split relative errors `1.98e-08` at p=1/8 and `3.29e-07` at p=1/32;
- small-p p^2 coefficient relative error `0.0010059543` at p=1/256;
- at the N24 safe momentum, unsplit contribution exactly `0.0` while piecewise gives `-1.1851582767804493e-10`.

All final negative controls passed.

## REPRODUCIBILITY

Local pre-transfer script SHA256:

`44ad6ada243e8a6cb6a3dd710a20caa82f9509f68365101e9db4b67adfeedbd6`.

Local raw SHA256:

`79fc954419d5c505530a89adcd6c5c61dcf7e9a36e059043653f75f456f2e4a1`.

Independent GitHub Actions workflow:

`.github/workflows/sf055a3q4-shifted-litim-geometry.yml`, commit `bf3fedc6a7265d1bc065f79b399e003f6d7be594`.

Run `35038554188` was queued at terminalization; its queue status is infrastructure only and was not used as a science premise.

## RECOVERY

`recovery/CURRENT_FRONT.md` synchronized at commit

`b55007bf7f7e3fec46ea41eb3b5db9705addeb4f`.

The historical blocked baseline is preserved explicitly.

## CURRENT FRONTIER

`FULL_TENSOR_PIECEWISE_BASELINE_IMPLEMENTATION_RETRY_UNDER_ORIGINAL_FREEZE`.

Before output, prospectively freeze the implementation-only successor. Make all Q4 surfaces actual nested quadrature boundaries while preserving the same source physics, p ladder, Richardson stencil, `N={8,12,16,24}`, 0.2% convergence rule and 1% target thresholds.

Derivative truncation error remains separately unresolved.

## CLAIM CEILING

`Q4_GEOMETRY_PASS != BASELINE_PASS`.

`SCALAR_SHELL_MECHANISM != PROVEN_FULL_TENSOR_SOLE_ERROR_SOURCE`.

`R_ASGS_TRUNCATION=1`.

`R_ASGS_PHYSICAL=UNDEFINED_MAP_NOT_CLOSED`.

No physical SF025 b, no projected C3 beta, no background/fluctuation equality, no Lorentzian matching coefficient, no quantum chi_ABC, no parent disposition change and no theory-establishment claim.