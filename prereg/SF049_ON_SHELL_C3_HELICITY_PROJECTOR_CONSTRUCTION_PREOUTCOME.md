# SF049 — on-shell C3 helicity projector construction — PREOUTCOME

Date: 2026-09-15
Status: PROSPECTIVE
Parent: SF048 `BLOCKED_MISSING_EXPLICIT_C3_FLUCTUATION_PROJECTION`.

## Gate

`SF049_ON_SHELL_C3_HELICITY_PROJECTOR_CONSTRUCTION_PREOUTCOME_GATE`

## Purpose

Close only the algebraic projection layer P2 of SF048, if possible, by constructing a physical on-shell helicity projector for the unique local six-derivative Weyl/Riemann-cubic direction.

This gate does NOT compute an FRG beta function, does NOT identify the background and fluctuation couplings, and does NOT select the physical SF025 matching coefficient.

## Frozen prior inputs

The following source facts are treated as prior inputs, not outcomes of SF049:

1. Dunbar et al. arXiv:1711.05526 eqs. (39)-(40): after stripping their common amplitude factor, the R3 deformation supplies
   `M3(+++) = alpha [12]^2[23]^2[31]^2`
   and its parity conjugate, while Einstein gravity supplies the mixed-helicity `--+` / `++-` three-point amplitudes.
2. The same source eqs. (41)-(42): at leading order in the deformation, the four-point all-plus amplitude is proportional to `-10 alpha K_++++^2 s t u`.
3. SF046: the physical local C3/Riemann3 direction overlaps the SF025 matching coordinate; absolute background-to-physical promotion remains blocked.
4. SF048/Knorr authority: after the declared local field-redefinition quotient, the Goroff-Sagnotti Weyl-cubic operator is the relevant local essential third-curvature pure-gravity scattering direction in 4D.

## Frozen construction tasks

H1. Derive the unique all-plus three-point local spinor monomial from little-group weights and mass dimension rather than assuming its exponents.

H2. Define an explicit normalized three-point projector `P3+` and parity-conjugate `P3-` that return the R3/C3 deformation coefficient in the Dunbar normalization when evaluated on the corresponding local amplitude.

H3. Prove the Einstein mixed-helicity three-point structures are annihilated by the all-plus/all-minus projectors.

H4. Define an independent four-point all-plus projector at generic non-exceptional kinematics (`s t u != 0`) and show it returns the same deformation coordinate at leading order.

H5. State exactly how the projector would act on an analytically continued dynamical 1PI graviton vertex: contract external legs with physical helicity-2 polarizations, take the local six-derivative / low-momentum coefficient, then divide by the frozen spinor polynomial.

H6. Identify the unresolved steps preventing this physical projector from being an FRG physical-selector map.

## PASS

`PHYSICAL_ON_SHELL_C3_HELICITY_PROJECTOR_CONSTRUCTED_SCOPED` requires H1-H5 and both positive/negative controls below.

## BLOCKED

`BLOCKED_HELICITY_PROJECTOR_NORMALIZATION_OR_DEGENERACY` if the physical C3 direction cannot be isolated from already-authorized lower-derivative sectors with the frozen helicity channels.

## FAIL

Only an explicit contradiction with the frozen on-shell source amplitudes or loss of linear independence at generic kinematics qualifies as FAIL.

## Positive controls

PC1. `P3+` applied to the normalized `C3/R3` all-plus amplitude returns `alpha`.
PC2. `P3-` applied to parity conjugate returns `alpha`.
PC3. generic four-point all-plus projector returns `alpha` from the frozen leading deformation.

## Negative controls

NC1. Pure Einstein three-point amplitude has no `+++` or `---` component and therefore projects to zero.
NC2. projector is undefined at deliberately exceptional spinor/kinematic points where its normalization polynomial vanishes; those points may not be used for PASS.
NC3. no off-shell/background coefficient is identified with the projected physical coefficient by notation alone.

## Interpretation ceiling

A PASS closes only the algebraic/physical projector definition. It may upgrade SF048 P2 from NOT CLOSED to CLOSED AT ON-SHELL ALGEBRAIC LEVEL.

It does not close:
- P3 projected FRG flow;
- P4 background/fluctuation identity map;
- P5 target Lorentzian continuation from Euclidean FRG data;
- P6 regulator-independent matching;
- physical SF025 `b` selection;
- quantum `chi_ABC`.