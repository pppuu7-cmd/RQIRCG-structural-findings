# SF055A3Q7A full-tensor regularity application — TERMINAL

Date: 2026-09-16

Formula authority: Q7 prospective preregistration `61461e28abc9a51cb697e20953033e46e7035aa4` and terminal formula result `053211a5c3ebcbb6c929a0f84d6c292e2861c3f2`.

Input authority: terminal Q6 `7fb39877f2415c6367c83af6c9ec0b183509178e` and canonical derivative ladder `results/raw/SF055A3Q6_DERIVATIVE_LADDER_CANONICAL.json`.

No Q7 weights or thresholds were chosen from these Q6 values. The formulas were frozen before complete Q6 output existed. This application does not rewrite the Q6 verdict.

## Classification

`INCONCLUSIVE_Q7_FULL_TENSOR_CUBIC_DIRECTION_SCOPED`.

Secondary:

`Q6_DERIVATIVE_INSTABILITY_DOMINATED_BY_SMALLEST_FROZEN_MOMENTUM_SCOPED`.

## Frozen formulas applied

For `h=1/32` and

`D_r=[F(rh)-F(0)]/(rh)^2`, r={1,2,4},

Q7 fixed

`R_h=(4D_1-D_2)/3`,

`C2_234=(8D_1-6D_2+D_4)/3`,

`C3_234=[-2D_1+(5/2)D_2-(1/2)D_4]/h`,

with exact identity

`R_h-C2_234=(2h/3)C3_234`.

## Full Q6 ladder application

`C3_234` sequence:

- N=8: `+0.11047520333196903`;
- N=12: `-0.15822591014134924`;
- N=16: `-0.04860017786014337`;
- N=24: `+0.0015123122084195195`.

The sequence changes sign and magnitude strongly. Q7 had no preregistered numerical convergence threshold for `C3_234`, so this is not converted into a post-hoc PASS/FAIL threshold. The correct interpretation is that a stable nonzero full-tensor cubic/nonanalytic direction is **not established** by the present Q6 ladder.

At N=16,

`|R_h-C2_234|/|R_h| = 0.6993455337472965`.

At N=24,

`|R_h-C2_234|/|R_h| = 0.012426064091445388`.

Thus the cubic-sensitive discrepancy collapses from about 69.9% of the historical Richardson estimate at N16 to about 1.24% at N24, while changing sign through the sequence.

This behavior is more consistent with unresolved finite-N derivative sensitivity than with an already-resolved, stable nonzero cubic coefficient. It is not a theorem that the continuum cubic coefficient vanishes.

## Exact N16->N24 Richardson error budget

For the frozen historical Richardson estimator,

`Delta R_h = (4 Delta D_1 - Delta D_2)/3`.

Observed Q6 changes:

- `Delta D_1` (p=1/32) = `-0.0008249207987136575`;
- `Delta D_2` (p=1/16) = `-0.000036492790310538314`;
- `Delta D_4` (p=1/8, not used by historical R_h) = `-0.000014811385983241887`.

Contributions to `Delta R_h`:

- from p=1/32: `-0.0010998943982848768`;
- from p=1/16: `+0.000012164263436846104`;
- total: `-0.0010877301348480308`.

Therefore the p=1/32 term accounts for `101.1183%` of the signed change, with the p=1/16 term canceling about `1.1183%` of it. In absolute-contribution terms, p=1/32 carries about `98.9061%` of the N16->N24 Richardson instability.

This uniquely localizes the active numerical sensitivity to the smallest frozen momentum point. It does not justify changing the historical stencil or dropping that point.

## Reproducible record

Raw application record:

`results/raw/SF055A3Q7A_FULL_TENSOR_REGULARITY_APPLICATION.json`.

All inputs are archived in

`results/raw/SF055A3Q6_DERIVATIVE_LADDER_CANONICAL.json`.

The exact Q7 identity is independently established in the Q7 terminal result.

## Interpretation ceiling

Established:

1. Q6 does not show a stable resolved nonzero `C3_234` across N=8,12,16,24;
2. the historical N16->N24 Richardson instability is overwhelmingly localized to the p=1/32 primitive quotient;
3. the p=1/16 contribution is small and partially cancels the p=1/32 change;
4. the already-frozen Q7 diagnostic does not rescue Q6 and does not alter its BLOCKED classification.

Not established:

- continuum `|p|^3` coefficient zero or nonzero;
- derivative-truncation closure;
- baseline PASS;
- projected physical C3 flow;
- physical matching b;
- asymptotic-safety correctness or failure.

Retain:

`UNSTABLE_C3_DIAGNOSTIC != NONZERO_CONTINUUM_ABS_P3`.

`P32_ERROR_LOCALIZATION != PERMISSION_TO_DROP_P32`.

`Q7A_INCONCLUSIVE != Q6_PASS`.

## Highest-information next gate

A future prospectively frozen successor should target **only the p=1/32 derivative-sensitive object** with stronger resolution/error control while leaving the historical Q6 verdict intact. Recomputing the entire matrix is lower information-per-cost because p=1/16, p=1/8, p=0 and beta_mu are not the dominant source of the current derivative instability.
