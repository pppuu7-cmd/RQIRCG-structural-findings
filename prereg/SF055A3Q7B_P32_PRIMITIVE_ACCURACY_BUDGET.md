# SF055A3Q7B p=1/32 primitive accuracy budget — PROSPECTIVE DIAGNOSTIC FREEZE

Date: 2026-09-16
Status: `FROZEN_BEFORE_Q7B_COMPUTATION`.

## Question

Translate the already-frozen historical 0.2% convergence criterion for `beta_g` into the corresponding required numerical stability of the dominant primitive `Flow_G(p=1/32)`, using only terminal Q6/Q7A authority and exact algebra. Quantify whether the inherited p=0 finite-N drift is large enough to obstruct the localized Q8 test.

This is a diagnostic/error-budget calculation only. It does not alter Q6, Q7A, Q8, SF055, programme disposition, or C3 authority.

## Frozen inputs

Use only:

- `results/raw/SF055A3Q6_TERMINAL_SUMMARY_RUN35040058701.json`;
- `results/raw/SF055A3Q6_DERIVATIVE_LADDER_CANONICAL.json`;
- historical convergence threshold `0.002`;
- `N_g^(-1)=0.00052874519051635`;
- `h=1/32`.

No Q8 N>24 values may be read or used.

## Frozen algebra

Historical derivative estimator:

`R=(4 D32-D16)/3`,

where

`D32=[F32-F0]/h^2`,

`D16=[F16-F0]/(1/16)^2`,

and

`beta_g = 2 + 2 N_g R`.

Therefore, holding the other primitives fixed,

`K32 = |d beta_g / d F32| = 8 N_g / (3 h^2)`.

At the authoritative Q6 N24 `beta_g`, define the local primitive accuracy budget

`deltaF32_budget = 0.002 |beta_g(N24)| / K32`.

This is a diagnostic local translation of the frozen beta criterion, not a new Q8 pass threshold. Q8 retains its own already-preregistered exact relative criterion evaluated at its N48 result.

Reconstruct `F0(N16)` and `F0(N24)` independently from

`F0(N)=F32(N)-D32(N) h^2`

using the terminal summary and canonical derivative ladder. Let

`deltaF0_obs = |F0(N24)-F0(N16)|`.

With F32 and F16 held fixed,

`K0 = |d beta_g/dF0| = |2 N_g [4(-1/h^2)-(-1/(1/16)^2)]/3|`.

Define the inherited p=0 propagated beta floor

`beta_floor_0 = K0 deltaF0_obs`.

Report its ratio to the historical allowed beta change

`0.002 |beta_g(N24)|`.

Also report the observed Q6 p=1/32 primitive drift

`deltaF32_obs = |F32(N24)-F32(N16)|`

and its ratio to `deltaF32_budget`.

## Frozen checks

The diagnostic passes construction iff:

1. all required Q6 records are present and finite;
2. reconstructed F0 drift is finite and nonnegative;
3. analytic sensitivity `K32` agrees with a direct symmetric finite-difference sensitivity check to relative tolerance `1e-8`;
4. no Q8 value is an input.

Classification on construction success:

`PASS_Q7B_P32_PRIMITIVE_ACCURACY_BUDGET_CONSTRUCTED_SCOPED`.

Otherwise:

`BLOCKED_Q7B_P32_PRIMITIVE_ACCURACY_BUDGET_CONSTRUCTION_SCOPED`.

## Interpretation ceiling

Q7B may establish a numerical accuracy requirement and inherited-error budget only. It does not establish Q8 convergence, continuum regularity, Q6 PASS, physical C3 flow, asymptotic-safety correctness/failure, programme disposition, or `chi_ABC`.
