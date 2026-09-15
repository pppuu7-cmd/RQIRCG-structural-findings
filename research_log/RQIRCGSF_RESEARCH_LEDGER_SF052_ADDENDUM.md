# RQIRCGSF research ledger — SF052 addendum

Date: 2026-09-15

## Gate

`SF052_DERIVATIVE_REDUNDANT_C3_PROJECTOR_COMPLETION_PREOUTCOME_GATE`.

## Why this gate

SF051 closed algebraic curvature-cubic Ricci/EOM redundancy but explicitly left derivative six-derivative redundancy open. The minimal essential scheme source fixes the relevant derivative action directions, making this the highest-information non-arbitrary continuation.

## Prospective freeze

Commit `9e4a0a16e47b82989fafe08ea78533cc397d6459`.

Frozen derivative basis:

- `R Delta R`;
- `S_mu_nu Delta S^mu_nu`.

No post-result operator enlargement permitted.

## Work

- source authority audit against Baldazzi et al. arXiv:2312.03831 eqs. (8)–(11);
- analytic TT proof that the `R Delta R` cubic tensor vanishes;
- full covariant cubic TT construction of `S Delta S`;
- complete redundant Gram quotient with inherited `[S3,SSC]` directions;
- exact algebra on the rationally reconstructed Gram matrix.

## Result

Primary:

`PASS_COMPLETE_SIX_DERIVATIVE_TT_QUOTIENT_SCOPED`.

Secondary:

`SOURCE_AUTHORIZED_DERIVATIVE_REDUNDANCY_REMOVABLE_WITH_NONZERO_C3_REMAINDER_SCOPED`.

Complete frozen essentialized tensor:

`T_C3_perp = T_C3 + (84/155)T_S3 + (364/155)T_SSC + (49/155)T_SDeltaS`.

Residual norm:

`243/9920 > 0`.

## New frontier

`PROJECTED_DYNAMICAL_C3_FLOW_RHS_REQUIRED`.

## Claim ceiling

No physical matching coefficient, background/fluctuation equality, regulator independence, Lorentzian matching, quantum `chi_ABC`, parent RCG-002 authority, full-QG or new-physics claim.

## Commits

- prereg `9e4a0a16e47b82989fafe08ea78533cc397d6459`
- code `cbf76a43f579a53bf94c68bd8609378870efa658`
- raw `7ceaabdcfef88edb8ad45858f481f608d5aa92d5`
- audit `9baf5d5f3b29b51c85e786c008f4778f770633a0`
- terminal `4016da484546167175236c9b8d4faf879597db37`
