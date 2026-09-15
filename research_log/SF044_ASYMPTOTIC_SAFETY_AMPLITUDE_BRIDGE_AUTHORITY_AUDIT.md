# SF044 — asymptotic-safety amplitude/form-factor bridge authority audit

Date: 2026-09-15
Preregistration: `796f2432c3524af6623bb9f3f717921f5c6d94e4`.

## Primary sources

1. B. Knorr, C. Ripken, F. Saueressig, `Form Factors in Asymptotically Safe Quantum Gravity`, arXiv:2210.16072.
2. J. H. Kwapisz, K. A. Meissner, `Asymptotic safety and quantum gravity amplitudes`, arXiv:2005.03559.
3. SF043 source set for the essential Goroff–Sagnotti RG trajectory.

## B1 — physical observable framework

PASS at framework level.

Knorr–Ripken–Saueressig construct scattering amplitudes from the quantum effective action with form factors and explicitly emphasize that the combinations entering on-shell amplitudes are the physically essential ones. They provide detailed gravity-mediated scalar/photon amplitudes and a general scattering/form-factor framework.

Thus asymptotic safety has a legitimate route from effective-action information to gauge-invariant observables.

But this is not yet the target pure-gravity `C^3` amplitude.

## B2 — curvature-cubic target structure

NOT CLOSED.

The audited review discusses pure-gravity form factors, propagators and graviton vertices, but does not provide a first-principles on-shell extraction of the Goroff–Sagnotti `C^3/R^3` matching coefficient from a physical four-graviton amplitude.

The review does not use the Goroff–Sagnotti coupling as an explicit observable example.

Therefore the crucial SF025 matching direction is absent from the completed amplitude calculations surveyed there.

## B3 — UV fixed-point trajectory input

PARTIAL.

The form-factor program is designed to derive quantum effective-action data from the functional RG and fixed-point structure. It therefore has the correct conceptual dependency.

However the audited observable examples are not the completed physical continuation of the specific SF043 minimal-essential `C^3` trajectory. The exact source-to-source bridge

`SF043 essential g_C3(k) -> Lorentzian physical C^3 form factor/amplitude`

is not supplied.

## B4 — low-energy matching extraction

PARTIAL FRAMEWORK, TARGET NOT COMPUTED.

The form-factor review explicitly explains how a quantum effective action can be expanded at low energies to recover EFT Wilson operators and coefficients.

This is the correct mathematical architecture for matching.

But no low-energy expansion of a first-principles asymptotically-safe pure-gravity `C^3` observable is given from which the finite SF025 matching constant can be extracted.

## B5 — regulator/gauge/field independence

NOT CLOSED FOR TARGET.

The review stresses that background and fluctuation form factors need not agree because gauge fixing and the regulator break split symmetry; Nielsen/split-Ward identities are needed to reconstruct one from the other.

A fully physical amplitude would remove gauge/redundant ambiguities, but the target `C^3` amplitude has not yet been computed from the SF043 trajectory to demonstrate cancellation of the regulator/truncation dependence.

Thus the SF043 physical-map blocker survives.

## B6 — perturbative / Lorentzian consistency

NOT CLOSED FOR TARGET.

The review describes recent Lorentzian graviton spectral-function work as a crucial step **toward** computing asymptotically safe scattering amplitudes, noting that earlier correlation-function computations were Euclidean and that massless on-shell kinematics are genuinely Lorentzian.

This confirms that the exact physical-amplitude program is still under construction.

No audited source simultaneously reproduces the known perturbative curvature-cubic running and derives the SF043 finite matching constant in a regulator-independent Lorentzian graviton amplitude.

## B7 — state/law separation

PASS.

The form-factor/fixed-point bridge acts on the quantum effective action and physical amplitudes. It does not obtain the Wilson coefficient by selecting an incoming state or measurement setting.

## Kwapisz–Meissner comparator

Kwapisz and Meissner explicitly propose applying asymptotic-safety conditions directly to amplitudes rather than effective-action couplings to avoid ambiguities.

Their concrete illustration is the four-graviton amplitude in string theory and its symmetries, not a first-principles asymptotically-safe computation of the Goroff–Sagnotti matching datum.

Therefore it supports the *correct target philosophy* but cannot be used as the missing ASGS physical bridge.

## Aggregate decision

B1: framework PASS.

B2: target `C^3` observable missing.

B3: fixed-point-to-target bridge partial.

B4: low-energy EFT architecture present, target coefficient not extracted.

B5: regulator/gauge physical cancellation not demonstrated for target.

B6: perturbative/Lorentzian target consistency not closed.

B7: law/state separation PASS.

Classification:

`ASYMPTOTIC_SAFETY_OBSERVABLE_FRAMEWORK_EXISTS_BUT_C3_MATCHING_BRIDGE_INCOMPLETE_SCOPED`.

Retain:

`R_ASGS_PHYSICAL = UNDEFINED_MAP_NOT_CLOSED`.

## New localization

The missing theory object is now explicit rather than generic:

`LORENTZIAN_ON_SHELL_C3_FORM_FACTOR_OR_FOUR_GRAVITON_AMPLITUDE_FROM_THE_UV_SAFE_ESSENTIAL_TRAJECTORY`.

It must be carried to the low-energy expansion with regulator/truncation control and perturbative matching.

This is not presently supplied by the audited literature.
