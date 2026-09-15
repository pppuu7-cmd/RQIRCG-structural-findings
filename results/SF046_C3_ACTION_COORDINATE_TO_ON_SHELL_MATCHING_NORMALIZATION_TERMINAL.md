# SF046 — C3 action-coordinate to on-shell matching normalization — TERMINAL

Date: 2026-09-15
Preregistration: `0b84c461737d5d308e19d9382fc5a262acfa4f1e`.
Derivation: `research_log/SF046_C3_NORMALIZATION_DERIVATION.md`, commit `ad9aa88c57ab457ac982b1555c10b9c18828bd2b`.

## RESULT / CLASSIFICATION

`C3_NORMALIZATION_MAP_DERIVED_UP_TO_SIGNATURE_CONVENTION_SCOPED`

Secondary structural result:

`TRUNCATION_TO_SF025_COORDINATE_CONVERSION_DOES_NOT_REMOVE_PHYSICAL_MAP_BLOCKER_SCOPED`.

## Derived map

On flat-space vacuum external gravitons the essential `C^3` operator and the SF025 `Riemann^3` witness coincide on shell.

After stripping SF025's formal loop-counting symbol, the coefficient coordinates satisfy

`b = s * G_C3/kappa^2`

with

`kappa^2=32 pi G_N`,

and `s=+1 or -1` is the unreconciled global Euclidean/Lorentzian/Riemann-sign convention.

Therefore

`b = s * G_C3/(32 pi G_N)`.

For the SF043 finite-truncation IR trajectory

`G_C3=G_N[A-q ln(G_N k^2)]`,

`q=43/(645120 pi^3)`,

so

`b_trunc(k)=s/(32 pi)[A-q ln(G_N k^2)]`.

The representative technical constant `A=-3.988e-6` corresponds only to

`b_trunc,const approximately s*(-3.966e-8)`.

This is a coordinate conversion, not a physical selector result.

## Perturbative mismatch survives the coordinate map

The finite-derivative FRG and perturbative low-energy quantum coefficients differ by

`-43/42`

in the common `g_C3` coordinate, and the same ratio remains after converting to `b`.

Thus the previously known mismatch is not a normalization artifact.

## Information-rank consequence

SF046 removes one bookkeeping ambiguity but does not increase physical selector rank:

`R_ASGS_TRUNCATION=1` remains.

`R_ASGS_PHYSICAL=UNDEFINED_MAP_NOT_CLOSED` remains.

The missing object is still the regulator/truncation-independent Lorentzian cubic-curvature observable computed from the UV-safe essential trajectory.

## Exact next theory action

`LORENTZIAN_C3_FLUCTUATION_VERTEX_FROM_ESSENTIAL_FLOW_REQUIRED`.

A future gate should target the minimal physical object needed to close SF045: a Lorentzian three-/four-graviton `C^3` vertex or form factor derived from the same essential flow, with split-symmetry/background-fluctuation and regulator dependence controlled.

Further generic selector-principle scans or mere convention conversions are lower information value.

## Claim ceiling

No physical value of SF025 `b` is selected. No asymptotic-safety correctness, complete quantum law, historical RCG-002 authority, quantum `chi_ABC`, full quantum gravity, or new physics is established.
