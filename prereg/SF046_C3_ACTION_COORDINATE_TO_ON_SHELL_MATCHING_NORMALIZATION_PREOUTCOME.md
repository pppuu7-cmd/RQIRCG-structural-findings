# SF046 — C3 action-coordinate to on-shell matching normalization — PREOUTCOME

Date: 2026-09-15
Status: PROSPECTIVE
Parent: SF045 terminal `BLOCKED_MISSING_LORENTZIAN_ON_SHELL_C3_MAP`.

## Gate

`SF046_C3_ACTION_COORDINATE_TO_ON_SHELL_MATCHING_NORMALIZATION_PREOUTCOME_GATE`

## Exact question

Given the explicit SF043 essential-action convention

`Gamma_k superset G_C3(k) integral sqrt(g) C^rho sigma_mu nu C^mu nu_alpha beta C^alpha beta_rho sigma`

and the SF025 physical matching convention

`delta Gamma = epsilon^2 delta b(mu) kappa^2 I3`,

`I3 = integral sqrt(-g) R_ab^cd R_cd^ef R_ef^ab`,

`kappa^2=32 pi G`,

derive the convention-level map between `G_C3` and `b` on flat-space vacuum on-shell graviton amplitudes.

## Frozen controls

C1. Use only flat-space vacuum external gravitons, so Ricci-flat external equations imply `C=Riemann` on shell.

C2. Preserve the exact tensor contraction order. No alternative cubic invariant may be substituted.

C3. Track dimensions: `[G_C3]=-2`, `[kappa^2]=-2`, `b` dimensionless.

C4. Keep the formal loop-counting `epsilon^2` as bookkeeping; do not convert it into a physical constant.

C5. Any Euclidean/Lorentzian action-sign convention ambiguity must be stated explicitly rather than hidden.

C6. Do not use the SF043 representative value `A` as a physical prediction unless the map being derived is explicitly labeled truncation-coordinate only.

## PASS

`C3_ACTION_TO_MATCHING_COORDINATE_NORMALIZATION_DERIVED_SCOPED`

requires an unambiguous algebraic relation between the coefficient multiplying the common on-shell operator and the SF025 `b` coordinate, including dimensions and any convention sign.

## PARTIAL

Use `C3_NORMALIZATION_MAP_DERIVED_UP_TO_SIGNATURE_CONVENTION_SCOPED` if magnitude/scale are fixed but one sign depends on unreconciled Euclidean/Lorentzian or Riemann-sign convention.

## BLOCKED

Use BLOCKED if the operator normalization in either authority is insufficient to match coefficients even up to a discrete convention sign.

## Interpretation ceiling

This gate can close only the coordinate normalization bridge. It cannot close regulator/truncation independence, prove the UV-safe trajectory physically correct, or set the physical value of `b`.
