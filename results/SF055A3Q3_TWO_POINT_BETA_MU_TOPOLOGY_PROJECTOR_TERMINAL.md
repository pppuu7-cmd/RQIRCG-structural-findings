# SF055A3Q3 — same-conventions two-point beta_mu topology/projector contract — TERMINAL

Date: 2026-09-16
Prospective freeze: `353a69b2544c12403dd25151c8abf0fc86b00c96`.
Implementation: `94754e156da1c805ee551cc1a586cf909f93ed4f`.
Workflow definition: `a9e202b49e03601ed6b2b9dba6fc86cfd34e1ebb`.
Exact analytic raw authority: `results/raw/SF055A3Q3_TWO_POINT_BETA_MU_ANALYTIC_PROOF.json`.

## CLASSIFICATION

`PASS_SF055A3Q3_TWO_POINT_BETA_MU_TOPOLOGY_PROJECTOR_CONTRACT_SCOPED`.

This closes only the exact two-point topology/projector/extraction contract required before numerical beta_mu reconstruction.

## EXACT INVERSE-PROPAGATOR DERIVATIVE ALGEBRA

For `G=A^{-1}` and two distinct labelled external derivatives,

`delta_1 delta_2 G`

`= + G A_1 G A_2 G + G A_2 G A_1 G - G A_12 G`.

Thus before trace prefactors there are exactly:

- one four-point insertion with coefficient `-1`;
- two ordered three-point-pair insertions, each with coefficient `+1`.

No Eq. (14) number enters this derivation.

## SOURCE-EQUIVALENT TOPOLOGY COEFFICIENTS

With the bosonic Wetterich prefactor `1/2` and

`Sym_2=(1/2) sum_(sigma in S2)`, 

the exact graviton topology coefficients are

`T4_GRAV=-1/2`,

`B33_GRAV=+1`.

For the frozen FP source seed, the ghost-hh vertex vanishes. Therefore the two-point ghost sector has no ghost tadpole. The two ordered ghost-h bubble terms each acquire the ghost-supertrace prefactor `-1`; under the same `Sym_2` convention this is

`B33_GHOST=-2`.

## TT MASS PROJECTOR

Inherited source-Fourier authority fixes

`K_EH=1/(32 pi)`

and

`Gamma_TT^(2)(p)=K_EH[p^2+mu_h k^2]`,

with `mu_h=-2 lambda_2`.

At the frozen benchmark

`lambda_2=-1/20`,

`mu_h=1/10`.

At `p=0`, for every unit orthonormal TT basis vector,

`Gamma_TT^(2)(0)=K_EH mu_h=1/(320 pi)`.

This also follows directly from the TT expansion of the cosmological term: for `tr h=0`, the bilinear coefficient of `sqrt(det(I+h))` is `-(1/2) tr(h_1 h_2)`, yielding exactly `-lambda_2/(16 pi)=K_EH(-2 lambda_2)`.

The frozen scalar mass projector is

`Flow_TT_mass(0)=(1/5) sum_(a=0)^4 Flow^(2)(0)[E_a,E_a]`.

At `eta_h=0`, `k=1`, exact scale differentiation gives

`beta_mu = Flow_TT_mass(0)/K_EH - 2 mu_h`.

## INDEPENDENT PUBLISHED NORMALISATION CROSS-CHECK

Denz, Pawlowski and Reichert, *Towards apparent convergence in asymptotically safe quantum gravity*, Appendix E, give

`partial_t mu = (eta_h(0)-2)mu + (32 pi/5) Flow_TT^(hh)(0)`.

Because `1/K_EH=32 pi`, this independently matches the frozen complete five-polarisation average used here. The factor `1/5` is therefore not inferred from the Eq. (14) numeric target.

## NEGATIVE CONTROLS

The exact contract rejects:

- omission of the bosonic `1/2`;
- use of an unnormalised two-leg permutation sum with unchanged topology coefficients;
- sign reversal of the ghost supertrace;
- a nonzero ghost-hh tadpole in the frozen FP source object;
- factor-two mutation of `K_EH`;
- omission of the canonical `-2 mu_h` term.

## REPRODUCIBILITY STATUS

A machine checker implementing the same frozen contract exists at

`scripts/sf055a3q3_two_point_beta_mu_contract.py`.

Actions run `35037794353` was queued at the time this exact analytic gate terminalized. The queue state is treated as infrastructure only and is not used as a scientific premise.

The terminal PASS rests on exact finite combinatorics, exact source normalisation, inherited validated source objects, and an independent published projector normalisation cross-check. A later runner result may provide additional machine-reproduction provenance but cannot change the frozen contract post hoc.

## INTERPRETATION CEILING

`TWO_POINT_TOPOLOGY_PROJECTOR_PASS != TWO_POINT_QUADRATURE_PASS`.

`TWO_POINT_TOPOLOGY_PROJECTOR_PASS != EQ14_BETA_MU_REPRODUCTION`.

`TWO_POINT_TOPOLOGY_PROJECTOR_PASS != LANE_A_PASS`.

`TWO_POINT_TOPOLOGY_PROJECTOR_PASS != SF055_PASS`.

No C3 projected-flow output has been computed or authorized.

## NEXT REQUIRED DEPENDENCY

`SAME_CONVENTIONS_TWO_POINT_FIXED_Q_CONTRACTION_AND_QUADRATURE_BETA_MU`.

This may now be developed independently of the three-point Figure-2 quadrature, while both remain required for Lane-A closure.