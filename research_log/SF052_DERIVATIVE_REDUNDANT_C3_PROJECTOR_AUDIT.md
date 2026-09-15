# SF052 — derivative-redundant C3 projector completion — AUTHORITY / DERIVATION AUDIT

Date: 2026-09-15
Preregistration: `9e4a0a16e47b82989fafe08ea78533cc397d6459`.

## Source-authorized derivative sector

Primary source: A. Baldazzi, K. Falls, Y. Kluth, B. Knorr, *Robustness of the derivative expansion in Asymptotic Safety*, arXiv:2312.03831, section II.2–II.3.

The minimal essential scheme uses the sixth-order redundant kernel basis displayed in eq. (8). The classical-side action contribution in eq. (10) shows the two derivative redundant invariants relevant here:

`- gamma_DeltaR R Delta R + gamma_DeltaS S_mu_nu Delta S^mu_nu`,

with `Delta=-nabla^2`.

The same source explains that the `nabla_mu nabla_nu R` kernel direction is a diffeomorphism and that its corresponding tree-level redundant operator lies outside the background-field approximation. It is therefore not added as an extra action direction in SF052.

This makes the frozen derivative basis source-complete for the audited MES approximation; no arbitrary tensor enlargement is used.

## R Delta R zero theorem in the frozen TT cubic domain

For every frozen external TT plane wave around flat space,

`R^(1)=0`.

Therefore for any linear combination of the three external TT waves the full first-order scalar curvature vanishes identically.

Using metric compatibility and dropping the boundary term,

`integral sqrt(g) R Delta R = integral sqrt(g) nabla_mu R nabla^mu R`.

Since `R=R^(2)+O(h^3)` on the frozen TT sector, `nabla R=O(h^2)`. Hence the integrated operator starts at `O(h^4)` and its cubic TT vertex vanishes exactly:

`T[R Delta R]_(TT,h^3)=0`.

This is an analytic result, not a numerical smallness claim.

## Full cubic S Delta S construction

Again by metric compatibility and integration by parts,

`integral sqrt(g) S_mu_nu Delta S^mu_nu = integral sqrt(g) nabla_rho S_mu_nu nabla^rho S^mu_nu`.

The cubic coefficient is constructed from:

1. `S^(1)` on each external TT leg;
2. the full pairwise `S^(2)` obtained from `Ricci^(2) - delta R^(2)/4`;
3. `Gamma^(1) S^(1)` terms in the covariant derivative;
4. the three `O(h)` inverse-metric corrections contracting the derivative index and the two tensor indices;
5. no linear measure correction, because every frozen TT polarization is trace-free.

The pairwise `Ricci^(2)` is computed from `partial Gamma^(2) + Gamma^(1)Gamma^(1)` with the exact frozen momenta. No lower-order surrogate is substituted for the covariant operator.

The calculation uses the same `1/6` trilinear normalization convention as SF051.

## Reproduction control

Before using the derivative tensor, the code reproduces the complete SF051 algebraic Gram block:

`[[95/768,-35/768,7/512],[-35/768,5/192,-1/128],[7/512,-1/128,15/1024]]`.

The executed linearized scalar-curvature maximum is zero to machine precision, matching the analytic TT theorem above.

## Complete nonzero Gram system

After removing the identically-zero `R Delta R` direction, the nonzero basis is

`[C3,S3,SSC,SDeltaS]`.

The reconstructed simple-rational Gram matrix is

`[[95/768,-35/768,7/512,-259/768],`
` [-35/768,5/192,-1/128,121/768],`
` [7/512,-1/128,15/1024,-71/512],`
` [-259/768,121/768,-71/512,1403/768]]`.

The redundant `[S3,SSC,SDeltaS]` block has

`det = 4185/67108864 > 0`,

`rank = 3`.

Thus `SDeltaS` supplies a genuinely new off-shell redundant direction beyond the SF051 algebraic span.

## Complete frozen quotient

Write

`T_perp = T_C3 - c1 T_S3 - c2 T_SSC - c3 T_SDeltaS`.

Solving the redundant Gram system gives

`(c1,c2,c3)=(-84/155,-364/155,-49/155)`.

Therefore

`T_C3_perp = T_C3 + (84/155) T_S3 + (364/155) T_SSC + (49/155) T_SDeltaS`.

Its norm is

`||T_C3_perp||^2 = 243/9920 > 0`.

The full four-direction Gram determinant is

`6561/4294967296 > 0`.

The quotient overlaps with all three nonzero redundant directions vanish exactly in the reconstructed rational system.

The normalized projector therefore returns

`P_E_6d[C3]=1`,

`P_E_6d[S3]=0`,

`P_E_6d[SSC]=0`,

`P_E_6d[RDeltaR]=0`,

`P_E_6d[SDeltaS]=0`.

## Numerical/exactness qualification

The covariant tensor amplitudes were executed in double precision for speed after an exact-symbolic implementation exceeded the bounded runtime after completing all 125 TT amplitudes. The displayed Gram entries are simple-rational reconstructions. The inherited SF051 block is reproduced exactly as known authority, and the reconstructed rational matrix is internally checked algebraically for determinant, rank, coefficients, residual norm and zero overlaps.

Accordingly, the result is authoritative for the frozen rationally-reconstructed TT Gram system, but it is not advertised as a machine-verified symbolic identity for arbitrary kinematics.

## Interpretation

Within the source-authorized minimal-essential-scheme sixth-derivative action basis and the frozen flat-Euclidean TT symmetric-point cubic domain, the complete redundant quotient does not remove the physical C3 direction.

This closes the off-shell projector-definition problem in that scoped domain.

It does NOT compute the FRG flow projected onto this direction, identify background and fluctuation couplings, remove regulator dependence, perform Lorentzian matching, or select physical SF025 `b`.
