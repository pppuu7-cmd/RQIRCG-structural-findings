# SF047 — essential C3 to fluctuation-vertex authority audit

Date: 2026-09-15
Preregistration: `84302a4fe00181ba0526bc21ff199f1ecaa77c8a`.

## Primary sources

1. Christiansen, Knorr, Meibohm, Pawlowski, Reichert, `Local Quantum Gravity`, arXiv:1506.07016.
2. Denz, Pawlowski, Reichert, `Towards apparent convergence in asymptotically safe quantum gravity`, arXiv:1612.07315.
3. Knorr, `Momentum-dependent field redefinitions in Asymptotic Safety`, arXiv:2311.12097.
4. Pawlowski, Reichert, Wessely, arXiv:2507.22169.
5. Assant, Litim, Reichert, arXiv:2606.19321.
6. Baldazzi, Falls, Kluth, Knorr, arXiv:2312.03831.

## V1 dynamical graviton 3-point function

PASS as machinery.

The fluctuation approach explicitly computes a dynamical graviton three-point function and uses it to define a dynamical Newton coupling. Momentum-dependent vertex methods are established.

## V2 dynamical graviton 4-point function

PASS as machinery.

Denz-Pawlowski-Reichert extend the systematic vertex expansion to the dynamical graviton four-point function and close the propagator flow with dynamical vertices.

## V3 six-derivative C3 projection

NOT CLOSED.

The audited fluctuation-vertex calculations do not isolate the Goroff-Sagnotti / Weyl-cubic six-derivative tensor structure as the essential target coupling. Their covariant reconstructions access lower-derivative sectors and generic higher-derivative information, but no explicit `C^3` fluctuation form factor tied to the SF043 trajectory is provided.

## V4 background-essential to fluctuation-C3 relation

NOT CLOSED.

SF043's `G_C3` is obtained in a background-field essential scheme. Existing fluctuation calculations emphasize that background and fluctuation couplings need not coincide. Momentum-dependent field redefinitions sharpen the physical-coordinate issue but do not supply the missing `G_C3_background -> C3_fluctuation_vertex` map.

No audited split-Ward/Nielsen solution closes this target six-derivative relation.

## V5 Lorentzian/on-shell realization

PARTIAL.

Lorentzian mass-shell graviton spectral functions exist, and the Lorentzian effective-action program is active. But the 2026 direct Lorentzian effective action is only through quadratic curvature, not the cubic-curvature fluctuation vertex.

## V6 regulator/renormalization closure

NOT CLOSED for the target.

Physical mass-shell renormalization schemes exist for the propagator/spectral sector, but regulator cancellation and low-energy matching have not been demonstrated for the `C^3` vertex.

## Structural result

The missing target does not require inventing an entirely new computational language.

Existing asymptotic-safety machinery already supplies:

`FRG fluctuation expansion + dynamical 3-point + dynamical 4-point + momentum dependence + Lorentzian spectral/on-shell program`.

The missing computation is much more specific:

`SIX_DERIVATIVE_C3_FLUCTUATION_PROJECTION + BACKGROUND_FLUCTUATION_IDENTITY + LORENTZIAN_ON_SHELL_MATCHING`.

Thus the bottleneck is an unperformed/unaudited projection-and-bridge calculation, not absence of vertex technology.
