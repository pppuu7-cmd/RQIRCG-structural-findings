# SF034 — control-phase transfer derivation and source authority notes

Date: 2026-09-15
Preregistration: `45a121c99f41e285b4f007984ffe55763831f343`.
Executed exact check script: `scripts/sf034_checks.py`, commit `a91d891da3982ceb052ffbb5f98d33b67b69eedf`.
Canonical raw: `results/raw/SF034_CHECKS.json`, commit `5c43b6c4a19a86fc18c1937e8880dccf271e8e72`.
Executed script SHA-256: `8aea50d69c895dcd8ebc4ecf0b602e987103a6ee07ee14a148ae2a712e5e9d1b`.

## 1. Exact Boolean control-phase result

For a diagonal branch-register phase function `f(a,b,c)`, the register contribution to the branch-reference coherence is

`Log K_s |_reg = -i [f(s)-f(000)] T`.

Because the seven coefficients in the frozen `C3` sum to one, the connected phase contribution is exactly

`Theta3_reg = - Delta3[f] T`,

where

`Delta3 f = f111-f110-f101-f011+f100+f010+f001-f000`.

The executed exact Boolean table is

- `Delta3[1]=0`;
- `Delta3[nA]=Delta3[nB]=Delta3[nC]=0`;
- `Delta3[nA nB]=Delta3[nA nC]=Delta3[nB nC]=0`;
- `Delta3[nA nB nC]=1`.

Thus every diagonal register phase through Boolean degree two is rejected exactly by the same connected observable used for gravity.

The lowest-degree diagonal register/control contaminant that survives is the cubic term

`hbar zeta nA nB nC`.

This algebraic localization is independent of its magnitude.

## 2. M0 control-separable map

The prospective M0 model freezes the register/control Hamiltonian independently of the A motional displacement setting `lambda_A`.

Science:

`lambda_A=1`,

`Theta3_reg^science = -zeta T`.

Delete-A:

`lambda_A=0`,

`Theta3_reg^deleteA = -zeta T`.

The delete-A change affects only A motional transport and the compensating D recoil translation. It does not remove the A qubit, alter its computational projector, or change `H_reg` in M0.

Therefore

`Theta3_reg^science - Theta3_reg^deleteA = 0`

exactly within the frozen effective model.

The inherited gravitational delete-A result remains separately exact at the retained order:

`x_app=x_fb=x_1PN=0`.

Hence the null control contains the cubic register nuisance but no retained connected known-gravity signal.

This closes all six SF033 transfer-map fields at the **effective-model** level.

## 3. M1 mandatory falsifier

The prospectively frozen countermodel is

`zeta(lambda_A)=zeta0+zeta1 lambda_A`.

Then

science: `Theta3_reg=-(zeta0+zeta1)T`,

control: `Theta3_reg=-zeta0 T`,

so the null-subtracted residual is

`-zeta1 T`.

A delete-A control alone cannot determine `zeta1`.

Therefore perfect transferability is not a generic consequence of a cubic register phase. It is a consequence of the explicit control-separability content `partial H_reg/partial lambda_A=0`.

This is why SF034 is not a laboratory-feasibility result.

## 4. External physical-realization sanity sources

External literature is used only to establish that the two ingredients of the effective model belong to physically realizable quantum-control classes. No listed platform is imported as the RQIRCGSF apparatus.

### State-dependent motion

P. C. Haljan, K.-A. Brickman, L. Deslauriers, P. J. Lee, C. Monroe,
“Spin-dependent forces on trapped ions for phase-stable quantum gates and motional Schrodinger-cat states,” arXiv:quant-ph/0411068.

The work experimentally demonstrates bichromatic spin-dependent forces coupling internal qubit states to external motion and explicitly studies phase stability of the resulting motional superpositions.

Source: https://arxiv.org/abs/quant-ph/0411068

Use in SF034: existence/plausibility of state-dependent motional control as a class only.

### Genuine higher-body register interactions

O. Katz, L. Feng, A. Risinger, C. Monroe, M. Cetina,
“Demonstration of three- and four-body interactions between trapped-ion spins,” arXiv:2209.05691.

The experiment realizes genuine three- and four-spin interactions, demonstrating that a cubic register Hamiltonian is not a mathematically empty nuisance class.

Source: https://arxiv.org/abs/2209.05691

Use in SF034: existence/plausibility of effective three-body register phase generators as a class only.

### Residual diagonal crosstalk as a control concern

Z. Ni et al.,
“Scalable Method for Eliminating Residual ZZ Interaction between Superconducting Qubits,” arXiv:2111.13292.

The paper treats unwanted diagonal `ZZ` interaction as a measurable crosstalk mechanism and calibrates/cancels the associated entangling phase.

Source: https://arxiv.org/abs/2111.13292

Use in SF034: sanity evidence that diagonal register interaction phases can be real control nuisances requiring explicit calibration. The source does not establish an SF034 cubic nuisance or its transferability.

## 5. What the literature does not supply

None of these sources establishes

`partial H_reg/partial lambda_A = 0`

for the RQIRCGSF experiment.

That equality is new prospective M0 model content. A physical device must independently validate it or constrain amplitude dependence.

Thus retain exactly:

`MODEL_LEVEL_TRANSFERABILITY != EXPERIMENTAL_TRANSFERABILITY`.

## 6. Information gain

SF033 ended with `0/6` transfer-map elements because no nuisance generator existed.

SF034 supplies a complete minimal effective map and simultaneously identifies its single decisive falsification direction:

`zeta1 = partial zeta / partial lambda_A`.

The next useful operational question is therefore not another generic noise scan. It is whether an amplitude ladder can identify or null this derivative without using a connected-gravity residual as a free fit parameter.
