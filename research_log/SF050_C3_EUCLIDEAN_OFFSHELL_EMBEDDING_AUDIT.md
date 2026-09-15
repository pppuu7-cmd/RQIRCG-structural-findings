# SF050 — C3 Euclidean/off-shell embedding audit

Date: 2026-09-15
Preregistration: `ae2d3414e87dd1b364a97b69349330267e88faff`.
Exact symbolic control: `scripts/sf050_tt_gram_check.py`, commit `ba1bac6a1490e75aafce0e16faef9b6272eb2a8d`.
Raw exact output: `results/raw/SF050_TT_GRAM_CHECK.json`, commit `1b8cba99d1f33f596485e5a50d0ad80d6e52b30b`.

## 1. Primary authorities

1. A. Baldazzi, K. Falls, Y. Kluth, B. Knorr, *Robustness of the derivative expansion in Asymptotic Safety*, Phys. Rev. D 113, 026005 (2026), arXiv:2312.03831.
2. J. M. Pawlowski, J. Tränkle, *Effective action and black hole solutions in asymptotically safe quantum gravity*, Phys. Rev. D 110, 086011 (2024), arXiv:2309.17043.
3. J. M. Pawlowski, M. Reichert, *Quantum Gravity from dynamical metric fluctuations*, arXiv:2309.10785.
4. T. Denz, J. M. Pawlowski, M. Reichert, *Towards apparent convergence in asymptotically safe quantum gravity*, arXiv:1612.07315.
5. N. Christiansen et al., *Local Quantum Gravity*, arXiv:1506.07016.
6. D. C. Dunbar et al., *Loop Amplitudes in an Extended Gravity Theory*, arXiv:1711.05526.

## 2. Explicit cubic C3 tensor template exists

Take

`S_C3 = integral sqrt(g) C_{rho sigma}^{mu nu} C_{mu nu}^{alpha beta} C_{alpha beta}^{rho sigma}`

and expand

`g = delta + h`.

Flat space has `C[delta]=0`. Therefore

`C = C^(1)[h] + C^(2)[h,h] + ...`.

Power counting gives

`S_C3^(3) = integral C^(1)[h] C^(1)[h] C^(1)[h]`.

There is no `O(h^3)` contribution from `sqrt(g)-1`: that begins as `O(h) * O(C^3)=O(h^4)`.

There is no `O(h^3)` contribution containing `C^(2)`: `C^(2) C^(1) C^(1)=O(h^4)`.

Hence the full cubic vertex of the local C3 operator is exactly determined by the product of three linearized Weyl tensors.

Define

`T_C3^(3)(p1,p2,p3) = delta^3 S_C3 / [delta h(p1) delta h(p2) delta h(p3)] at h=0`.

Properties:

- homogeneous degree six in external momenta;
- Bose symmetric;
- linearized-diffeomorphism transverse because `C^(1)` is gauge invariant around flat space;
- annihilates a pure conformal external perturbation because the Weyl tensor vanishes on conformally flat metric variations;
- after Lorentzian/complex on-shell continuation its physical helicity contractions reduce to the SF049 all-plus/all-minus C3 structures.

Thus the missing object after SF049 was not the existence of a C3 tensor template. It exists explicitly and is local.

## 3. Why a naive Euclidean one-template projector is not physical

A real Euclidean FRG vertex is evaluated off shell. On-shell EOM-redundant curvature invariants therefore need not vanish.

Use the prospective control

`O_Ric3 = integral sqrt(g) R_mu^nu R_nu^rho R_rho^mu`.

For a flat-background TT plane wave,

`p^mu h_{mu nu}=0`, `h_mu^mu=0`.

The linearized Ricci tensor is then

`R_mu nu^(1) = -1/2 p^2 h_mu nu`

up to the overall Riemann-sign convention.

Thus `O_Ric3` has a nonzero cubic TT vertex at generic Euclidean `p_i^2 != 0`, with the same total momentum degree six as C3.

For on-shell external gravitons `p_i^2=0`, the linearized Ricci tensor vanishes and this control disappears. It is therefore exactly the kind of off-shell redundant direction that must not be interpreted as physical C3 matching.

## 4. Exact symmetric-point Gram witness

Freeze the real Euclidean symmetric point

`p_i^2=1`,

`p_i.p_j=-1/2` for `i != j`,

with `p1+p2+p3=0`.

For each leg use an orthonormal basis of the five transverse-traceless symmetric tensors.

The exact symbolic 5 x 5 x 5 trilinear tensors give

`||T_C3||^2 = 95/768`,

`||T_Ric3||^2 = 5/192`,

`<T_C3,T_Ric3> = -35/768`.

Therefore a naive normalized Euclidean contraction

`P_naive[Gamma] = <T_C3,Gamma>/<T_C3,T_C3>`

returns, for a unit `Ric3` contamination,

`P_naive[T_Ric3] = -7/19`.

The sign can flip with the overall curvature convention; the nonzero overlap and magnitude of the contamination witness do not disappear by declaring the C3 template to be the physical direction.

This directly falsifies:

`KNOWN C3 TEMPLATE => SINGLE EUCLIDEAN TEMPLATE CONTRACTION IS PHYSICAL C3 PROJECTOR`.

## 5. Relation to the essential sixth-derivative scheme

Baldazzi et al. give a complete sixth-derivative redundant RG-kernel basis in the GR universality class. Their Eq. (25) includes curvature/Ricci tensor structures and derivative structures; the induced action flow in Eq. (27) shows explicitly how terms containing at least one Ricci tensor or Ricci scalar are absorbed by scale-dependent field redefinitions, while the Goroff-Sagnotti C3 term remains essential.

This is exactly the structural cure demanded by the Gram witness.

The physical C3 direction is unique only **after the essential/redundant quotient is specified**. It is not a unique coordinate in a generic off-shell tensor expansion before that quotient.

## 6. Audit of current dynamical-vertex ansatz

Pawlowski and Tränkle reconstruct their effective action from momentum-dependent three- and four-graviton correlation functions, but their vertex ansatz approximates the explicit tensor structures by those generated by the classical Einstein-Hilbert action. They state that higher-curvature tensor structures are not explicitly included; their effects are carried by momentum dependence of the retained vertex dressings.

This is sufficient for their declared curvature-order <=2 reconstruction, but it is not an executed C3 projector.

A momentum-dependent Einstein-Hilbert dressing can contain information generated by higher-curvature operators without uniquely identifying which six-derivative operator produced it.

Therefore

`MOMENTUM DEPENDENCE != OPERATOR IDENTIFICATION`.

and

`EH-TENSOR VERTEX DRESSING != C3 ESSENTIAL COEFFICIENT`.

## 7. Correct embedding architecture

Let

`T_E = T_C3^(3)`

and let `{T_a}` span the redundant six-derivative fluctuation tensor directions relevant to the chosen vertex/kinematic domain.

At one or more nonexceptional Euclidean momentum configurations construct the Gram matrix

`G_AB = <T_A,T_B>`.

If the redundant sub-Gram matrix is full rank, define the essentialized tensor

`T_E_perp = T_E - T_a (G_R^-1)^{ab} <T_b,T_E>`.

Then the projected coefficient is schematically

`g_E = <T_E_perp,Gamma^(3)>/<T_E_perp,T_E>`.

This is only a tensor-space realization of the quotient. A physically acceptable FRG implementation must additionally make it consistent with the scale-dependent field redefinitions / split-Nielsen identities used to define the essential scheme.

A single symmetric point may have accidental tensor degeneracies. A complete implementation must therefore either prove full rank there or use a multi-kinematic momentum family.

## 8. SF050 element verdicts

D1 cubic C3 expansion: CLOSED.

D2 explicit tensor template: CLOSED.

D3 relation to SF049 physical helicity projector: CLOSED at algebraic/analytic-continuation level.

D4 uniqueness of naive single Euclidean contraction: FAILS; exact Ricci-cubic contamination witness.

D5 current FRG explicit tensor ansatz: target C3 structure NOT explicitly projected.

D6 minimum next object: complete essential six-derivative tensor quotient/projector embedded into the dynamical vertex flow.

## 9. Interpretation

This is positive progress despite the negative naive-projector result.

Before SF050 the gap was phrased as `C3 helicity projector -> FRG flow embedding`.

After SF050 the embedding problem is split into two concrete pieces:

1. **template construction** — solved;
2. **essential/redundant off-shell quotient inside the fluctuation flow** — still open.

The next gate should use the complete redundant basis already supplied by the essential sixth-derivative analysis rather than inventing arbitrary tensor structures.

## Claim ceiling

No physical SF025 `b` is selected.
No background/fluctuation equality is assumed.
No finite-truncation `A` is promoted to physical matching.
No regulator independence is established.
No full FRG C3 flow is computed.
No quantum `chi_ABC` is computed.
