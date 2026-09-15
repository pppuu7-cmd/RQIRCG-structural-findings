# SF055A3 — TT projector normalisation pre-quadrature controls — PROSPECTIVE FREEZE

Date: 2026-09-15
Parent gate: `SF055A3_SOURCE_FOURIER_BASELINE_LOOP_REPRODUCTION`.
Source authority: `research_log/SF055A3_SOURCE_PROJECTION_AND_EXTRACTION_AUTHORITY.md` and arXiv:1506.07016v2 Eqs. (6), (9)–(11).
Status: frozen before normalisation output is inspected.

## PURPOSE

Compute the source normalisations `N_g` and `N_lambda` directly from the source-Fourier Einstein-Hilbert three-graviton tensors and complete external TT basis sums, before loop quadrature. This prevents any later rescaling of an integrated flow to match Eq. (14).

## FROZEN DEFINITIONS

Use the same D=4 real-Euclidean symmetric momentum directions already used by SF052/SF055A2:

`p1=(1,0,0,0)`,

`p2=(-1/2,sqrt(3)/2,0,0)`,

`p3=-(p1+p2)`.

For each leg construct the already-validated orthonormal 5-dimensional TT basis `E_i^(a)`, `a=0..4`.

The source-Fourier EH tensor generator `T3(p;lambda)` is the SF055A2 implementation of `G_N S^(3)` with `partial -> i p` and prefactor `1/(16 pi)`.

### Gravitational channel

Define the complete 125-component TT tensor

`T_G[a,b,c] = T3([p1,p2,p3]; lambda=0)[E_1^a,E_2^b,E_3^c]`.

Then, because the TT bases are orthonormal representations of `Pi_TT` on each leg,

`N_g^(-1) = sum_{a,b,c} T_G[a,b,c]^2`.

No subset of polarizations and no fitted multiplicative factor is permitted.

### Lambda channel

The source tensor `T^(3)(0;1)` is momentum independent but Eq. (11) still refers to the external TT projection. Implement its `p -> 0` value by keeping the symmetric momentum **directions** fixed while setting all momenta entering the EH tensor generator exactly to zero:

`T_Lambda[a,b,c] = T3([0,0,0]; lambda=1)[E_1^a,E_2^b,E_3^c]`.

Then

`N_lambda^(-1) = sum_{a,b,c} T_Lambda[a,b,c]^2`.

This is accepted as source-faithful only if the scalar norm is invariant under global rotations of the entire symmetric configuration and under alternative deterministic embeddings of the same 120-degree symmetric momentum triangle. If that invariance fails materially, the result is `BLOCKED_ZERO_MOMENTUM_TT_PROJECTOR_CONVENTION`, not an invitation to choose a preferred embedding by target matching.

## DECOMPOSITION CONTROL

For frozen test values `lambda in {-7/10,-1/5,2/5}`, verify component-wise over all 125 TT triples:

`T3(p;lambda) = T_G + lambda T_Lambda`

with absolute residual <= `2e-12`.

This directly checks the source Eq. (6) decomposition in the implementation basis.

## NORMALISATION ROBUSTNESS CONTROLS

Required:

1. each TT Gram matrix differs from identity by <= `2e-12`;
2. `N_g^(-1)>0` and `N_lambda^(-1)>0`;
3. complete 125-component sums are deterministic under basis sign changes and independent orthogonal basis rotations on each external TT space to relative `2e-11`;
4. global O(4) rotations of momenta and tensors preserve both inverse normalisations to relative `2e-11`;
5. at least three alternative deterministic symmetric-plane embeddings preserve `N_lambda^(-1)` to relative `2e-11`;
6. Bose permutation of external labelled legs preserves the norms to relative `2e-11`;
7. replacing the complete TT sum by one polarization triple must be detected as a non-equivalent mutation;
8. rescaling `T_G` or `T_Lambda` by an arbitrary fitted constant must be rejected by direct comparison with the source generator.

## OUTPUT

Persist:

- exact floating values of `N_g^(-1)`, `N_g`, `N_lambda^(-1)`, `N_lambda`;
- full 125-component `T_G` and `T_Lambda` arrays or their exact deterministic hashes plus sufficient raw data to reproduce them;
- Gram, decomposition, rotation, embedding and permutation residuals;
- negative-control results.

## PASS

`PASS_SF055A3_SOURCE_TT_PROJECTOR_NORMALISATION_SCOPED`

only if every frozen positive and negative control passes.

## BLOCKED

`BLOCKED_ZERO_MOMENTUM_TT_PROJECTOR_CONVENTION`

if `N_lambda` materially depends on an otherwise source-equivalent symmetric `p->0` embedding.

## FAIL

`FAIL_SF055A3_SOURCE_TT_PROJECTOR_NORMALISATION_SCOPED`

if the source-generated tensors are well-defined but violate Eq. (6), TT completeness, or normalisation invariance under the frozen controls.

## INTERPRETATION CEILING

This validates only source projector normalisations. It is not loop integration, Eq. (14) reproduction, Lane-A PASS, SF055 PASS, or any C3 result.
