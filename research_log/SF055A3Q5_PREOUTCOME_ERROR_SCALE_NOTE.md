# SF055A3Q5 pre-outcome error-scale note

Date: 2026-09-16
Status: post-hoc diagnostic on the already-public original baseline aggregate; NOT a preregistered science gate and NOT a Q5 outcome.

## Purpose
Separate the scale of the original N16->N24 quadrature instability from the finite-h Richardson-stability signal already recorded at fixed N. This is only an error-source localization aid.

From the original archived aggregate:

N=24 final Richardson derivative
`R24=-0.002501405056967989`.

N=24 preceding derivative estimate
`R24_prev=-0.0024976818940992914`.

N=16 final derivative
`R16=-0.0025576781910747284`.

Therefore

`|R24-R16| = 5.6273134106739515e-05`,

while

`|R24-R24_prev| = 3.7231628686974425e-06`.

Their ratio is approximately

`15.114335872829225`.

Thus the observed inter-quadrature-order change in the final derivative is about fifteen times larger than the difference between the two frozen Richardson estimates at N=24. This supports treating quadrature resolution as the active observed blocker in the original run. It does NOT prove the h-truncation error is negligible or bounded by the preceding/final difference.

## If the leading nonanalytic correction were exactly linear in h

The Q5 regularity control shows a possible structure

`R_h=A+(2/3)B h+...`.

Under the *diagnostic assumption* that the difference between the two N24 Richardson estimates is dominated by that term, the linear-in-h extrapolate is

`A_hat=2 R24-R24_prev=-0.0025051282198366863`.

Using the frozen source normalization gives

`beta_g_hat=-7.475748488190634`,

with relative discrepancy to the frozen Eq.(14) target about `0.715973%`.

Propagating the same derivative estimate into lambda3 while keeping the N24 `Flow_Lambda(0)` fixed gives

`beta_lambda3_hat=-4.415004339431028`,

with relative target discrepancy about `0.425556%`.

Both remain inside the separate 1% target window. These values are NOT replacements for the frozen estimator and are NOT a PASS argument; they only show that a plausible O(h) correction at the scale suggested by the N24 internal Richardson difference would not by itself explain the much larger N16->N24 instability.

At N=16 the preceding/final derivative difference is `3.336834129277072e-05`, showing that the same internal h diagnostic is itself contaminated by quadrature order before convergence.

## Interpretation ceiling

No certified truncation-error bound is obtained. Adjacent h estimators can be affected by higher powers and quadrature error. The only science decision remains the prospectively frozen Q5 full piecewise matrix under the original classifier. C3 remains disabled.
