# SF043 — asymptotic-safety Goroff–Sagnotti matching authority audit

Date: 2026-09-15
Preregistration: `10c8fee5e58f507ea5893c5c2c789d8ed11cce84`.

## Audited principle

`ASGS = ASYMPTOTIC_SAFETY_GOROFF_SAGNOTTI_TRAJECTORY_SELECTION`.

The question is not whether asymptotic safety exists in general. The gate asks whether the audited **minimal essential sixth-derivative realization** supplies nonzero selection power on the physical curvature-cubic matching direction exhibited by SF025.

## Primary sources

1. A. Baldazzi, K. Falls, Y. Kluth, B. Knorr, “Robustness of the derivative expansion in Asymptotic Safety,” arXiv:2312.03831.
2. A. Baldazzi, K. Falls, “Essential Quantum Einstein Gravity,” arXiv:2107.00671.
3. Z. Bern, C. Cheung, H.-H. Chi, S. Davies, L. Dixon, J. Nohle, “Evanescent Effects Can Alter Ultraviolet Divergences in Quantum Gravity without Physical Consequences,” arXiv:1507.06118.

## M1 — operator/on-shell overlap

SF025 uses the physical direction represented by

`I3 = integral sqrt(-g) R_ab{}^cd R_cd{}^ef R_ef{}^ab`.

The audited essential-scheme paper includes the Goroff–Sagnotti curvature-cubic coupling, conventionally written with a cubic Weyl/Riemann tensor invariant.

For vacuum on-shell perturbations around flat space, Ricci curvature vanishes at leading external-leg order, so Riemann and Weyl coincide on the physical graviton sector. Bern et al. explicitly relate the Goroff–Sagnotti non-evanescent `R^3` counterterm to the two-loop identical-helicity four-graviton amplitude.

Therefore there is a real physical overlap with the SF025 parity-even curvature-cubic on-shell matching direction.

Qualification: SF043 does **not** equate the numerical normalization of the FRG `g_{C^3}` coordinate with SF025 `b` without an explicit amplitude normalization map.

Verdict:

`M1 = PASS_OVERLAPPING_PHYSICAL_DIRECTION_SCOPED`.

## M2 — essentiality

Baldazzi et al. use scale-dependent nonlinear field redefinitions to remove redundant directions and report that, at sixth derivative order in their GR universality class, the dynamical essential couplings are Newton's coupling and the Goroff–Sagnotti coupling.

Thus the audited `C^3` direction is not being counted merely because an off-shell redundant operator was retained.

Verdict:

`M2 = PASS_ESSENTIAL_COUPLING_IN_AUDITED_SCHEME`.

## M3 — critical-surface selection

Within the audited sixth-order essential truncation, the nontrivial UV fixed point has one relevant direction. The Goroff–Sagnotti direction is irrelevant in the physical positive-Newton-coupling region.

The paper's phase portrait identifies a single asymptotically safe separatrix connecting the nontrivial UV fixed point to the Gaussian/perturbative-GR infrared domain. Generic neighboring trajectories have the curvature-cubic coupling diverge in the UV.

After the relevant datum/scale is fixed, this supplies genuine selection on the curvature-cubic coordinate within the truncation.

Verdict:

`M3 = PASS_NONZERO_SELECTION_TRUNCATION_SCOPED`.

## M4 — infrared matching output

The paper does not stop at a UV fixed-point coordinate. In its low-energy expansion it writes the dimensionless Goroff–Sagnotti coupling as

`g_C3 = [G_N k^2] [ A - (43/(645120 pi^3)) ln(G_N k^2) ]`

for the displayed approximation.

It states explicitly that the constant `A` depends on the RG trajectory, and that the asymptotically safe trajectory predicts it. For the displayed technical choice `alpha=beta=1` with the Litim shape function, the reported value is

`A = -3.988e-6`.

This is precisely the architecture of a finite matching constant selected by a microscopic UV boundary condition rather than by a state/preparation choice.

Verdict:

`M4 = PASS_IR_WILSON_CONSTANT_PREDICTED_IN_TRUNCATION`.

## M5 — physical map closure

This is where strong promotion fails.

The calculation uses a background-field functional RG approximation and a finite derivative expansion. The authors study regulator dependence explicitly. Qualitative properties are fairly robust, but fixed-point quantities and especially the irrelevant curvature-cubic direction retain technical-parameter dependence.

The displayed numerical `A` is quoted for a specific cutoff/parameter choice rather than demonstrated as a regulator-independent on-shell amplitude matching constant.

At the exact level physical observables should be regulator independent; the finite truncation does not establish that exact property for the SF025 amplitude coordinate.

Verdict:

`M5 = BLOCKED_PHYSICAL_ON_SHELL_MAP_NOT_CLOSED`.

## M6 — perturbative low-energy consistency

The same paper performs an important internal negative control.

It compares its infrared beta function for the Goroff–Sagnotti coupling with the perturbative gravity result and finds different quantum coefficients in the finite derivative-expansion FRG calculation. The authors explicitly caution that reproducing the perturbative two-loop result may require an infinite derivative expansion.

Bern et al. further show why two-loop gravity bookkeeping is subtle: evanescent Gauss–Bonnet effects alter ultraviolet divergences while the physical renormalized amplitude and its scale dependence require careful treatment.

Therefore the finite-truncation `A` cannot be promoted directly to the exact physical SF025 matching coefficient.

Verdict:

`M6 = PHYSICAL_PROMOTION_BLOCKED_BY_KNOWN_PERTURBATIVE_MISMATCH_SCOPED`.

## M7 — state/law separation

ASGS acts through a UV RG fixed point and essential coupling trajectory. No incoming density matrix, vacuum population, measurement setting or SF028B preparation is used to select the curvature-cubic coefficient.

Thus it genuinely targets the quantum-law/on-shell-matching slot rather than the state/measure slot.

Verdict:

`M7 = PASS_LAW_SLOT_NOT_STATE_SLOT`.

## Information-rank result

Within the frozen essential sixth-derivative truncation:

`R_ASGS_TRUNCATION = 1`.

Reason: the curvature-cubic direction is essential and irrelevant, and the unique UV-safe separatrix predicts its low-energy integration/matching constant after the relevant datum/scale is fixed.

For the exact physical SF025 on-shell matching coordinate:

`R_ASGS_PHYSICAL = UNDEFINED_MAP_NOT_CLOSED`.

This is not rank zero.

It is also not a physical PASS.

## New structural fact

SF027 showed that anomaly freedom by itself has zero perturbative selection rank on the exhibited matching fibre.

SF043 identifies a qualitatively different kind of principle:

`MICROSCOPIC RG BOUNDARY CONDITION + IR TRAJECTORY MAP`

can carry nonzero matching information.

The remaining question is no longer whether a conceivable principle can act on the matching fibre. The audited truncation demonstrates that it can.

The blocker is whether that map survives to a regulator/truncation-independent physical on-shell amplitude.

## Claim ceiling

Do not write:

- asymptotic safety is established as the correct quantum gravity;
- `A=-3.988e-6` is the exact physical SF025 coefficient;
- SF025 `b` is numerically selected;
- full quantum gravity is solved;
- historical RCG-002 implies asymptotic safety.

The correct result is truncation-level nonzero selection plus physical-map blockade.
