# SF055 Lane A — source/object audit for same-code-path baseline reproduction

Date: 2026-09-15
Parent preregistration: `9d998d984566aa5bf290312a6a062fd632c85561`.
Status: non-terminal implementation progress only.

## SOURCE AUTHORITY

Primary source: N. Christiansen, B. Knorr, J. Meibohm, J. M. Pawlowski, M. Reichert, *Local Quantum Gravity*, arXiv:1506.07016v2 / Phys. Rev. D 92, 121501.

The source explicitly fixes the architecture needed by SF055 Lane A:

- Wetterich flow with graviton and Faddeev-Popov ghost traces;
- linear split about flat Euclidean background;
- vertex ansatz with wave-function factors and Einstein-Hilbert-derived classical tensor structures;
- De-Donder-type linear gauge in the Landau limit;
- TT external projection;
- symmetric three-point kinematics;
- regulator `R_phi(x)=Gamma_k^(phi phi)|_{mu=0}(x) r(x)` with `x r(x)=(1-x) theta(1-x)`;
- three-point flow depending on dressed vertex orders n=3,4,5;
- finite-difference extraction at `p=k` and `p=0`;
- analytic Eq. (14) benchmark used by the already merged SF055 preflight.

The source also states that its executed vertex ansatz keeps the selected classical gauge-fixed Einstein-Hilbert tensor structures and neglects other tensor structures. This is precisely why SF055 must reproduce the baseline before adding the independently projected p6 C3 direction.

## IMPORTANT OBJECT-DEFINITION FACT

The paper writes the projected flow schematically as

`Flow^(3)_{Lambda/G} = integral_q (dot r - eta r) F_{phi_i,Lambda/G}(p,q,G_n,Lambda_n)`

but does not print the full tensor/integrand kernels `F_{phi_i,Lambda/G}` in the article.

Therefore Lane A cannot be closed by transcribing a published scalar kernel. The required same-code-path baseline must be freshly generated from the source-fixed gauge-fixed Einstein-Hilbert + ghost action, propagators, regulator insertion and differentiated Wetterich topologies.

This is an implementation requirement, not a missing-physics blocker: the underlying action and flow prescription are defined, but the tensor algebra/combinatorics must be reconstructed rather than hard-coded from Eq. (14).

## CONSEQUENCE FOR IMPLEMENTATION ORDER

The next legitimate Lane-A implementation should first generate and validate the source baseline vertices/propagators and topology symmetry factors, then reproduce the frozen Eq. (14)/finite-difference benchmark through that same diagram code path.

It must not:

- hard-code the Eq. (14) beta functions as the baseline;
- use an EH scalar dressing in place of the unprojected TT loop RHS;
- omit ghost diagrams;
- reuse the C3 Lane-B PASS as evidence that the EH/ghost loop machinery is correct.

## STATUS

`LANE_A_SOURCE_OBJECT_DEFINED_IMPLEMENTATION_REQUIRED`.

This is non-terminal progress, not a PASS/BLOCKED verdict for Lane A.

SF055 remains non-terminal and projected C3 beta output remains unauthorized.
