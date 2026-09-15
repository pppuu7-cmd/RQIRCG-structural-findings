# SF048 — six-derivative C3 fluctuation projection authority audit

Date: 2026-09-15
Preregistration: `3e0a7bf408e211273ceeb2e5a818a62bcfa02775`.

## Question audited

Does current asymptotic-safety / functional-RG fluctuation-vertex work already contain an explicit six-derivative Weyl-cubic (`C^3`) dynamical graviton projection that can be connected to the SF043 essential `G_C3` trajectory without introducing a new physical assumption?

The gate freezes six required elements P1-P6. This audit evaluates exactly those elements.

## Primary authorities

1. N. Christiansen, B. Knorr, J. Meibohm, J. M. Pawlowski, M. Reichert, *Local Quantum Gravity*, arXiv:1506.07016.
2. T. Denz, J. M. Pawlowski, M. Reichert, *Towards apparent convergence in asymptotically safe quantum gravity*, arXiv:1612.07315.
3. J. M. Pawlowski, M. Tränkle, *Effective action and black hole solutions in asymptotically safe quantum gravity*, arXiv:2309.17043.
4. B. Knorr, *Momentum-dependent field redefinitions in Asymptotic Safety*, arXiv:2311.12097.
5. A. Baldazzi, K. Falls, Y. Kluth, B. Knorr, *Robustness of the derivative expansion in Asymptotic Safety*, arXiv:2312.03831.
6. J. M. Pawlowski, M. Reichert, J. Wessely, *Self-consistent graviton spectral function in Lorentzian quantum gravity*, arXiv:2507.22169.
7. G. Assant, D. F. Litim, M. Reichert, *Spectral Functions of Lorentzian Quantum Gravity*, arXiv:2606.19321.
8. Z. Bern et al., *Two-Loop Renormalization of Quantum Gravity Simplified*, arXiv:1701.02422.
9. D. C. Dunbar et al., *Loop Amplitudes in an Extended Gravity Theory*, arXiv:1711.05526.

## P1 — physical six-derivative C3 direction

Verdict:

`PASS_PHYSICAL_ESSENTIAL_C3_DIRECTION_DEFINED_SCOPED`.

Knorr's essential-scattering analysis identifies, in four-dimensional pure gravity within the local field-redefinition class used there, the Goroff-Sagnotti Weyl-cubic operator

`int sqrt(-g) c_C3 C_{rho sigma}^{mu nu} C_{mu nu}^{alpha beta} C_{alpha beta}^{rho sigma}`

as the independent local essential third-curvature pure-gravity direction relevant for four-graviton scattering after redundant directions are removed.

SF046 already established the action-coordinate relation to the SF025 on-shell `Riemann^3` direction, up to the global signature/Riemann convention sign.

Therefore the target physical basis direction is not ambiguous at the level relevant to this gate.

This P1 PASS does not mean an FRG fluctuation projector has been executed.

## P2 — explicit dynamical projector

Verdict:

`NOT_CLOSED`.

Christiansen et al. establish a dynamical momentum-dependent graviton three-point function.

Denz-Pawlowski-Reichert extend the systematic fluctuation-vertex expansion through the dynamical graviton four-point function. Their explicit projections use transverse-traceless Einstein-Hilbert-type tensor structures at symmetric momentum configurations and study higher momentum dependence through the chosen vertex parametrization.

Their covariant operator discussion permits higher-derivative structures in principle, including cubic-curvature structures. But the executed projection is not an explicit projector onto the Weyl-cubic Goroff-Sagnotti tensor.

A crucial scope distinction is required: statements in that literature about scalar `R^3` or Ricci-cubic structures are not automatically statements about the on-shell Weyl-cubic `C^3` direction. The current audit gives no credit from notation resemblance.

Pawlowski-Tränkle reconstruct a fully momentum-dependent effective action from 3-/4-graviton correlation functions but explicitly truncate the covariant curvature expansion at second order. They note that `p^6 / R^3` contributions can in principle be present but are not included in that reconstruction.

Thus no audited source supplies the explicit P2 projector.

## P3 — projected C3 fluctuation flow / reconstruction

Verdict:

`NOT_CLOSED`.

Because P2 is not implemented, no audited mainstream fluctuation-vertex calculation evolves or reconstructs the specific projected dynamical `C^3` coefficient.

The existing vertex machinery proves calculational capability at the 3-/4-point level; it does not by itself constitute an executed six-derivative C3 flow.

The Baldazzi et al. sixth-derivative result is a background/essential derivative-expansion flow and supplies the SF043 truncation-level selector, not the missing dynamical fluctuation projection.

## P4 — background essential to fluctuation C3 identity map

Verdict:

`NOT_CLOSED`.

Denz et al. and later fluctuation-vertex work discuss Nielsen / split-Ward relations between background and fluctuation sectors. These identities are structurally the correct bridge.

However, the specific relation

`G_C3^(background essential) -> g_C3^(dynamical fluctuation)`

has not been derived and closed for the target six-derivative tensor in the audited source chain.

Later effective-action reconstructions use approximate background-fluctuation relations adequate for their retained lower-curvature sectors. That is not an exact identity map for the SF043 C3 trajectory.

Therefore a background coupling cannot be promoted to the fluctuation amplitude coefficient by equality-by-notation.

## P5 — Lorentzian/on-shell realization

Verdict:

`PARTIAL_FRAMEWORK_ONLY`.

Lorentzian asymptotic-safety work now contains a physical mass-shell graviton spectral function and, in 2026, a Lorentzian quantum effective action through quadratic curvature.

This establishes a viable Lorentzian observable framework.

It does not include the cubic-curvature C3 target. No audited source performs the target six-derivative fluctuation projection and continues or reconstructs it into the physical all-equal-helicity / four-graviton R3 amplitude used by the SF025 matching coordinate.

Thus P5 is not a target-level PASS.

## P6 — physical regulator/renormalization closure

Verdict:

`NOT_CLOSED`.

SF043 already found that the finite derivative expansion retains technical/regulator dependence and that its low-energy C3 quantum coefficient does not reproduce the perturbative two-loop result.

SF046 proved that this mismatch survives conversion to the SF025 action coordinate and is therefore not a normalization artifact.

Without a target Lorentzian on-shell fluctuation amplitude, there is no demonstrated cancellation/removal of regulator/background dependence for the C3 matching coefficient.

Therefore P6 remains open.

## Literature recency audit through 2026

A targeted search for 2024-2026 `Goroff-Sagnotti`, `Weyl cubed`, `C^3`, `Riemann cubed`, `fluctuation vertex`, and `asymptotic safety / FRG` was performed after the prospective freeze.

The recent Lorentzian papers strengthen P5 framework authority but do not supply P2/P3.

The search returned the Baldazzi sixth-derivative background truncation and unrelated modified/nonassociative gravity work, but no mainstream asymptotic-safety fluctuation calculation that executes the required Weyl-cubic dynamical 3-/4-graviton projector.

Absence from this audit is not a universal proof that no unpublished or inaccessible calculation exists. It is sufficient for the scoped repository claim about the audited source chain through 2026.

## Element table

| Element | Result |
|---|---|
| P1 physical essential C3 direction | PASS scoped |
| P2 explicit dynamical C3 projector | NOT CLOSED |
| P3 projected C3 fluctuation flow | NOT CLOSED |
| P4 essential-background to fluctuation C3 identity | NOT CLOSED |
| P5 Lorentzian/on-shell target realization | PARTIAL framework only |
| P6 physical regulator/renormalization closure | NOT CLOSED |

## Falsifier / negative-control result

The strongest prospective falsifier of a BLOCKED verdict would have been an auditable paper containing all of:

1. a dynamical 3-/4-graviton six-derivative tensor basis;
2. an explicit projector onto the Weyl-cubic tensor;
3. its FRG flow or reconstruction;
4. a background-fluctuation identity linking it to the essential `G_C3` trajectory;
5. a Lorentzian on-shell amplitude extraction.

No such source was found.

Conversely, the existence of general vertex machinery prevents a stronger claim that the calculation is impossible.

## Structural result

The missing theory object is now narrower than `vertex machinery`.

The physical C3 direction is known and the 3-/4-point FRG machinery exists.

What is absent is the actual six-derivative projection and its identity/physical continuation chain.

Therefore retain:

`KNOWN_PHYSICAL_C3_DIRECTION + GENERAL_VERTEX_MACHINERY != EXECUTED_C3_FLUCTUATION_PROJECTOR`.

## Claim ceiling

This audit does not establish a no-go theorem for constructing the C3 projector, does not select physical SF025 `b`, does not establish asymptotic safety as correct quantum gravity, and does not authorize `chi_ABC`.
