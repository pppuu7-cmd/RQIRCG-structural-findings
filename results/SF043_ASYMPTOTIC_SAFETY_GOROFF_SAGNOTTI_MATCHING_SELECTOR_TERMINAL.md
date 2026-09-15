# SF043 — asymptotic-safety Goroff–Sagnotti matching selector — TERMINAL

Date: 2026-09-15
Preregistration: `10c8fee5e58f507ea5893c5c2c789d8ed11cce84`.
Source/map audit: `research_log/SF043_ASYMPTOTIC_SAFETY_MATCHING_AUTHORITY_AUDIT.md`, commit `a7435f6d48b17f25001f520d5f7c2cf8d41a97f2`.

## RESULT / CLASSIFICATION

`ASYMPTOTIC_SAFETY_PROVIDES_NONZERO_TRUNCATION_LEVEL_MATCHING_SELECTION_SCOPED`.

Required secondary classification:

`PHYSICAL_ON_SHELL_MATCHING_AUTHORITY_BLOCKED_BY_TRUNCATION_OR_SCHEME_MAP`.

Information-rank record:

`R_ASGS_TRUNCATION = 1`.

`R_ASGS_PHYSICAL = UNDEFINED_MAP_NOT_CLOSED`.

This is neither perturbative rank zero nor a physical-selector PASS.

## Operator / physical-direction overlap

The audited sixth-derivative minimal essential scheme retains Newton's coupling and the Goroff–Sagnotti curvature-cubic coupling as dynamical essential couplings.

SF025's physical matching witness is represented by a parity-even curvature-cubic `Riemann^3` direction after the physical field-redefinition/EOM quotient.

On vacuum on-shell graviton configurations around flat space, the Ricci tensor vanishes at leading external-leg order and the Weyl/Riemann cubic direction overlaps the same physical graviton-amplitude sector.

Bern et al. explicitly identify the Goroff–Sagnotti non-evanescent `R^3` counterterm in the two-loop identical-helicity four-graviton amplitude.

Therefore this is a real matching-fibre overlap, not a notation-only coincidence.

No exact numerical normalization map from the paper's `g_C3` coordinate to SF025 `b` is claimed.

## Why the truncation has nonzero selection rank

In the audited essential sixth-derivative truncation:

- the Goroff–Sagnotti coupling is essential;
- the nontrivial UV fixed point has one relevant direction;
- the curvature-cubic direction remains irrelevant in the physical positive-Newton-coupling region;
- the phase portrait contains a unique asymptotically safe separatrix connecting the UV fixed point to the perturbative-GR/Gaussian infrared region;
- generic neighboring trajectories have divergent curvature-cubic coupling in the UV.

Therefore, after the relevant physical datum and RG scale are fixed, the curvature-cubic integration constant is not free within this truncation.

This justifies

`R_ASGS_TRUNCATION=1`.

## Explicit low-energy matching output

The source derives a low-energy form

`g_C3 = [G_N k^2] [ A - (43/(645120 pi^3)) log(G_N k^2) ]`

within the displayed approximation.

It states that `A` is trajectory-dependent and is predicted by the asymptotically safe trajectory.

For the displayed technical choice `alpha=beta=1` and Litim cutoff, it reports

`A=-3.988e-6`.

This demonstrates the desired selector architecture:

`UV microscopic boundary condition -> unique safe trajectory -> finite IR matching constant`.

Crucially, no state/vacuum/preparation variable is used to obtain this selection.

## Why physical promotion is blocked

The calculation is a finite derivative expansion in a background-field FRG approximation.

Regulator dependence is explicitly present at finite approximation order. The paper reports substantial stability in broad regions but not exact regulator independence of the curvature-cubic physical matching prediction.

The numerical `A` quoted above is tied to a specific regulator/technical choice.

More decisively, the source itself compares its low-energy curvature-cubic beta function with the known perturbative gravity result and obtains a different quantum coefficient. It explains that reproducing the perturbative two-loop result may require an infinite derivative expansion.

Therefore the present truncation does not establish that its `A` is the exact regulator-independent physical on-shell matching datum isolated by SF025.

A missing exact amplitude bridge cannot be relabeled rank zero.

Thus

`R_ASGS_PHYSICAL=UNDEFINED_MAP_NOT_CLOSED`.

## Relation to SF027

SF027 found

`R_QCA-P=0`

for perturbative anomaly-freedom/QME consistency on the SF025 matching direction.

SF043 is qualitatively different.

It demonstrates that a genuinely microscopic RG boundary condition can carry nonzero matching information.

Therefore the theory-track question is now narrower than before:

not

`CAN ANY PRINCIPLE ACT ON THE MATCHING FIBRE?`

but

`CAN THE NONZERO UV-TRAJECTORY SELECTION BE CONNECTED TO A REGULATOR-INDEPENDENT ON-SHELL AMPLITUDE MATCHING MAP?`

## New theory frontier

`REGULATOR_INDEPENDENT_ON_SHELL_RG_TO_MATCHING_MAP_REQUIRED`.

Highest-information next audit:

`SF044_ASYMPTOTIC_SAFETY_AMPLITUDE_FORM_FACTOR_BRIDGE_PREOUTCOME_GATE`.

It should test amplitude/form-factor-based asymptotic-safety literature for an explicit physical observable bridge, not repeat the fixed-point calculation or select a regulator post hoc.

## Claim ceiling

SF043 does not establish:

- asymptotic safety as the correct theory of quantum gravity;
- exact physical value `b=A`;
- regulator-independent curvature-cubic matching;
- historical RCG-002 authority;
- a complete quantum law;
- full quantum gravity;
- quantum `chi_ABC`;
- new physics.
