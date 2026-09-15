# SF055A3Q3 — same-conventions two-point beta_mu topology/projector contract — PREOUTCOME

Date: 2026-09-16
Parent gate: `SF055A3_SOURCE_FOURIER_BASELINE_LOOP_REPRODUCTION`.
Inherited authorities: SF055A2 source-Fourier seed PASS; SF055A3 A3.1 full Landau-transverse propagator/regulator PASS; SF055A3Q2 external-symmetrisation source normalisation PASS; Q1 exact projector regrouping is irrelevant to this two-point gate.

Status: prospectively frozen before the two-point topology/projector derivation output is inspected.

## PURPOSE

Close the exact source/combinatorial object needed before numerical reconstruction of the independently required Eq. (14) `beta_mu` target.

This gate does NOT integrate the two-point flow. It freezes and verifies the unique same-conventions two-point flow topology coefficients, ghost content, TT mass projector normalisation and the eta=0 relation between the projected two-point flow and `beta_mu`.

## FROZEN SOURCE OBJECT

Start from the same Wetterich source convention already used by SF055 Lane C/Q2:

`partial_t Gamma = (1/2) Tr_h[G_h dotR_h] - Tr_gh[G_gh dotR_gh]`,

with `G=(Gamma^(2)+R)^(-1)` and external functional derivatives acting on `G` through the source vertices.

The source-Fourier seed authority fixes:

- EH `Gamma_h^(3)` and `Gamma_h^(4)` from one source action path;
- FP `Gamma_barcc^(2)` and `Gamma_barcc h^(3)`;
- no FP ghost-hh or higher external-graviton seed vertex in the frozen linear-gauge FP object;
- TT two-point source normalisation `K_EH=1/(32 pi)`;
- `mu_h=-2 lambda_2`.

## FROZEN COMBINATORICS

For two labelled external derivatives `1,2`, differentiate the inverse exactly:

`delta_1 delta_2 G`

`= + G A_1 G A_2 G + G A_2 G A_1 G - G A_12 G`,

where `A_i` is a three-point insertion and `A_12` a four-point insertion.

The physical/source two-leg symmetriser is prospectively defined by the same labelled-derivative logic as Q2:

`Sym_2 = (1/2) sum_{sigma in S2}`.

The gate must determine whether the source-equivalent topology coefficients are exactly

- graviton four-vertex tadpole `T4_GRAV = -1/2`;
- graviton 3/3 bubble `B33_GRAV = +1`;
- ghost 3/3 bubble `B33_GHOST = -2`;

under this `Sym_2` convention.

These numbers are hypotheses to be checked from the exact derivative algebra; they may not be chosen from the printed Eq. (14) beta_mu coefficient.

## FROZEN TWO-POINT TT MASS PROJECTOR

Use the already-validated source-Fourier EH two-point object

`Gamma_TT^(2)(p) = K_EH [p^2 + mu_h k^2]`

at eta_h=0, with `K_EH=1/(32 pi)` and `mu_h=-2 lambda_2`.

At `p -> 0`, retain an arbitrary deterministic momentum direction only to construct a five-dimensional orthonormal TT basis `E_a`, `a=0..4`; the scalar mass channel is

`Flow_TT_mass(0) = (1/5) sum_a Flow^(2)(0)[E_a,E_a]`.

A future integration must show direction/basis invariance; this gate only fixes the scalar projector algebra and source normalisation.

At k=1 and eta_h=0, differentiating `K_EH k^2 mu_h` freezes the extraction identity

`beta_mu = Flow_TT_mass(0)/K_EH - 2 mu_h`.

No Eq. (14) numeric target may be used in deriving this relation.

## SOURCE LOOP MEASURE

Inherit Q2:

`int_q = int d^4q/(2 pi)^4`.

## POSITIVE CONTROLS

1. Exact ordered inverse-derivative enumeration yields two `Gamma3*Gamma3` terms with positive unit coefficient and one `Gamma4` term with negative unit coefficient before the bosonic `1/2`.
2. Applying the bosonic `1/2` and `Sym_2` yields exactly `T4_GRAV=-1/2`, `B33_GRAV=+1`.
3. Applying the ghost supertrace sign with no ghost-hh vertex yields exactly `B33_GHOST=-2` under `Sym_2`.
4. The source seed reproduces `K_EH=1/(32 pi)` and `Gamma_TT^(2)(0)=K_EH mu_h` for all five TT basis vectors at a frozen nonzero direction taken to zero in the vertex momenta.
5. The extraction identity `beta_mu = Flow_TT_mass/K_EH - 2 mu_h` follows algebraically from eta_h=0 scale differentiation.

## NEGATIVE CONTROLS

The checker must reject:

- omission of the bosonic `1/2`;
- use of an unnormalised two-leg permutation sum with the same topology coefficients;
- sign flip of the ghost supertrace;
- insertion of a nonexistent ghost-hh tadpole;
- factor-two mutation of `K_EH`;
- omission of the canonical `-2 mu_h` term in beta extraction.

## PASS

`PASS_SF055A3Q3_TWO_POINT_BETA_MU_TOPOLOGY_PROJECTOR_CONTRACT_SCOPED`

only if every positive/negative control passes.

## BLOCKED

`BLOCKED_SF055A3Q3_TWO_POINT_SOURCE_OBJECT`

if the frozen source seed is insufficient to determine the two-point topology or mass-projector relation without an additional unsupported convention.

## FAIL

`FAIL_SF055A3Q3_TWO_POINT_TOPOLOGY_PROJECTOR_CONTRACT_SCOPED`

if the source-defined objects are well-defined but violate the prospectively frozen relations above.

## INTERPRETATION CEILING

A PASS validates only the two-point topology/projector/extraction contract. It is not two-point quadrature, not Eq. (14) beta_mu reproduction, not Lane-A PASS, not SF055 PASS, and not a C3 result.