# SF044 — asymptotic-safety amplitude/form-factor bridge — PREOUTCOME

Date: 2026-09-15
Parent theory terminal: SF043 `dff2f59cce67329d5fddddab16dc0efe9cc115b2`.

## PURPOSE

Test whether existing amplitude/form-factor implementations of asymptotic safety close the specific physical-map blocker left by SF043:

`essential FRG curvature-cubic trajectory -> regulator-independent on-shell graviton matching observable`.

## TARGET OBJECT

The target remains the SF025 physical curvature-cubic on-shell matching direction.

SF044 does not ask whether form factors or scattering amplitudes are in principle useful. It asks whether an audited construction actually computes enough of the **pure-gravity physical amplitude/form factor** to map the UV-safe Goroff–Sagnotti trajectory to the low-energy SF025 matching coordinate.

## REQUIRED BRIDGE ELEMENTS

B1. A physical observable object: on-shell graviton amplitude, physical form factor, or an explicitly demonstrated equivalent observable; not merely an off-shell background effective-action coupling.

B2. A curvature-cubic-sensitive tensor/kinematic structure overlapping the SF025/Goroff–Sagnotti physical direction.

B3. A UV fixed-point/critical-trajectory input derived from or consistently matched to the asymptotic-safety construction.

B4. An IR/low-energy expansion from which the finite curvature-cubic matching constant can be extracted.

B5. Regulator/gauge/field-redefinition independence at the claimed observable level, or a controlled theorem showing cancellation of the technical dependence relevant to the extracted coefficient.

B6. Correct perturbative low-energy limit, including the known curvature-cubic running structure where applicable.

B7. No state/vacuum/preparation choice used as a substitute for law matching.

## DECISION RULE

### PASS

`ASYMPTOTIC_SAFETY_AMPLITUDE_BRIDGE_CLOSES_PHYSICAL_C3_MATCHING_MAP_SCOPED`

requires B1–B7 and promotes

`R_ASGS_PHYSICAL=1`

in the exact audited scope.

### PARTIAL BRIDGE

`ASYMPTOTIC_SAFETY_OBSERVABLE_FRAMEWORK_EXISTS_BUT_C3_MATCHING_BRIDGE_INCOMPLETE_SCOPED`

if physical scattering/form-factor machinery exists but one or more of B2–B6 is not closed for the pure-gravity curvature-cubic direction.

`R_ASGS_PHYSICAL` remains `UNDEFINED_MAP_NOT_CLOSED`.

### FAIL

Use FAIL only if an explicit audited physical-amplitude calculation demonstrates that the UV-safe trajectory leaves a continuous free SF025 curvature-cubic matching datum.

### INVALID

Do not use a string-theory amplitude, matter-scattering example, quadratic-gravity toy form factor, or RG-improved tree amplitude as if it were the missing pure-gravity `C^3` physical bridge unless the source proves the required equivalence.

## SOURCE PRIORITY

Audit primary sources including, where relevant:

- Knorr, Ripken, Saueressig, `Form Factors in Asymptotically Safe Quantum Gravity`, arXiv:2210.16072;
- Kwapisz, Meissner, `Asymptotic safety and quantum gravity amplitudes`, arXiv:2005.03559;
- newer first-principles asymptotic-safety form-factor/amplitude computations if they contain the required pure-gravity observable.

## CLAIM CEILING

A partial bridge is valuable but does not fix SF025 `b`, establish asymptotic safety as correct QG, authorize `chi_ABC`, or alter parent RQIRCG.
