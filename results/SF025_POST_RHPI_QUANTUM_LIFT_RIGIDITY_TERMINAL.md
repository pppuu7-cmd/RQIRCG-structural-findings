# SF025 - post-RHPI quantum-lift rigidity - TERMINAL

Date: 2026-09-14
Preregistration: `9ef45ce5858f9271a450abef4adcb798d8dd2c85`.
Inherited immutable frontier: `b588d8e47c24c6bc12976d54f0a976dc9df099d3`.

## RESULT / CLASSIFICATION

`POST_RHPI_QUANTUM_COMPOSITION_DOES_NOT_FIX_FINITE_ON_SHELL_MATCHING_SCOPED`.

Quantum Local Composition (QLC) is **not selected as a complete quantum-law selector**. In a formal low-energy quantum continuation of the selected classical law, a finite, physically nonredundant matching direction survives even with the same incoming preparation. Exact nonperturbative quantum-HDA rigidity is **NOT TESTED/BLOCKED**, not disproved.

This is a new repository synthesis and scoped nonselection certificate, not a claim that the underlying EFT renormalization facts are new discoveries. The witness is quarantined as a counterexample; no higher-curvature coefficient is added to the SF021 predictive classical model.

## STATE_READ / CURRENT_FRONT / WHY_MAX_INFORMATION_GAIN

README, all preregistrations and all terminal results SF001-SF024, SF022 script/raw data and recent commits were read at the inherited SHA. The README still describes the initial search; later scoped terminals govern. SF021 selected the classical local RHPI-S/ADM class; SF020 retained source constitutive freedom; SF016 forbids counting ordinary preparation variation as theory variation; SF024 stopped at an instantaneous asymptotic release limit. The present question therefore fixes both classical law and preparation. It does not repeat SF015's different-state example or reopen classical SF003.

## FORMAL_PRINCIPLE / PHYSICAL_OBJECTS

QLC consists of local covariant perturbative quantum composition, causal factorization, perturbative unitarity, diffeomorphism Ward consistency and the fixed RHPI classical limit. The physical external sector is the same weak-field massless graviton sector with the same calibrated matter content. We fix the asymptotically flat boundary sector, Newton normalization, common incoming wave packets/polarizations, and a common infrared subtraction/dressing convention. The calculation is a formal series at energies well below its cutoff. It is not an exact higher-derivative Cauchy theory.

Let `Q_N` be such quantum prescriptions through loop order N, modulo changes that leave matched on-shell amplitudes unchanged. Let `pi_0:Q_N -> C` retain the classical action and classical source law. The already-selected classical class is `c_*`. The remaining fibre is

`F_N = {q in Q_N : pi_0(q)=c_*, fixed inherited calibration, QLC(q)} / physical equivalence`.

A singleton classical fibre does not mathematically imply a singleton inverse image under `pi_0`.

### Relative-lift obstruction: precise conditional statement

Suppose a local functional I at positive formal order n satisfies:

1. it is an allowed real homogeneous solution of the Ward/normalization problem at that order;
2. it changes no already-fixed lower-order data;
3. its variation has a nonzero physical on-shell amplitude, after EOM, field-redefinition and boundary equivalences are removed;
4. an open interval of its finite coefficient remains perturbatively admissible in one common low-energy domain.

Then `q_b=q_*+epsilon^n b I+O(epsilon^(n+1))` gives a non-singleton `F_n`. Here epsilon counts loops, not a new physical constant. Proof: conditions 1,2,4 keep the family in the fibre; condition 3 prevents distinct b values being identified in the physical quotient. This proves a local lower bound of one physical direction, not a dimension formula for all quantum gravity.

## GRAVITY-FACING WITNESS / EXISTENCE_ANALYSIS

Use units c=hbar=1 for engineering dimensions and a separate formal epsilon. Keep the classical action and all order-epsilon data fixed, and consider the order-epsilon^2 finite local difference

`delta Gamma = epsilon^2 delta b(mu) kappa^2 I_3`,

`I_3 = integral d^4x sqrt(-g) R_ab{}^cd R_cd{}^ef R_ef{}^ab`.

`kappa^2=32*pi*G` in the cited convention. The integral I_3 has mass dimension 2, kappa^2 has dimension -2, and b is dimensionless. Around flat space it starts at cubic field order; it introduces no different quadratic free propagator. Assigning this term positive loop order preserves the classical projection exactly. It is treated as a perturbative local counterterm, never resummed into an exact higher-derivative model.

Primary authority [1], equations (5)-(7), supplies its nonzero four-graviton insertion:

`delta M_4(++++) = -60 i delta c_R3 (kappa/2)^4 T_spinor^2 s12 s23 s13`,

where `delta c_R3=epsilon^2 kappa^2 delta b` and `T_spinor=[12][34]/(<12><34>)`. These normalization factors are an external counterexample convention, not a fitted RQIRCG prediction. The fixed kinematic control `s=4 E^2, t=-E^2, u=-3 E^2` obeys s+t+u=0 and has stu=12 E^6, which is nonzero at arbitrarily small nonzero E. Thus the difference is not just an off-shell action label or a three-point complex-kinematics artifact. Independent three- and four-point checks are supplied by [2], equations (39)-(42).

For the relevant local perturbative construction, [3], section 3.4, equations (46)-(50), imposes causal factorization and unitarity while explicitly retaining finite local normalization maps. Its background-independence analysis does not remove nonrenormalizability. This supports the declared formal EFT scope, not an exact convergent Hilbert-space theory.

## CONSERVATION_BIANCHI_CHECK / CAUSALITY_CHECK

For a compactly supported infinitesimal diffeomorphism, scalar-density invariance gives `delta_xi I_3=0` modulo a boundary. If `E_I^{mu nu}` denotes its metric variational derivative, integrating `E_I^{mu nu} (nabla_mu xi_nu+nabla_nu xi_mu)` by parts gives the Noether identity `nabla_mu E_I^{mu nu}=0`. Consequently this invariant does not create an unmatched source nonconservation term.

At the first order where the finite difference enters, the difference of two Ward equations is homogeneous: `s_0(delta Gamma)=0` modulo a total derivative. I_3 obeys it. The local BRST cohomology context is [4]. This does not mean that an exact quantum constraint algebra on every background has been constructed.

A real local insertion is compatible with causal perturbation theory and order-by-order unitarity at the retained low-energy order. Exact ultraviolet causality, positivity on a resummed higher-derivative branch, nonperturbative constraint propagation and universal UV completion are NOT established here. Restrict both members to a common sufficiently small-energy domain. No negative-probability artefact from a truncated density matrix is counted as a physical prediction.

## STATE_AND_BOUNDARY_DATA / POSITIVITY_MEASURE_CHECK

The incoming state and readout convention are held fixed; b is a law/matching datum, not a population, temperature, squeeze parameter or chosen wavefunction. Perturbative physical-state normalization is inherited from the common free sector and unitarity conditions. Exact complete positivity of a gravitational channel is not proven.

As an independently executable logical control only, take `H_b=(1+epsilon^2 b) sigma_z`, the same initial projector `rho=|+x><+x|`, and the same readout rho. Every member is exactly self-adjoint, unitary and compositional. With epsilon=1/2 and t=pi/2, b=0 and b=1 give probabilities 0 and `(2-sqrt(2))/4`. This is not a gravity model; it rules out the logical inference from normalized closed evolution plus a fixed preparation to a unique generator.

## UNIQUENESS_ANALYSIS / SCHEME ADVERSARY

Write a hard amplitude in one common scheme as `A=A_loop+b P`. Under a scheme change, `A_loop -> A_loop-delta P` and `b -> b+delta`; the sum is unchanged. That is one physical theory. In contrast, changing b at fixed scheme, fixed loop contribution and fixed physical input changes A by `delta b P`. Only the latter is the counterexample.

Similarly, the renormalization-group equation fixes running, not its initial matching value. If `db/d ln(mu)=beta` at the retained order, then `b(mu)=b(mu0)+beta ln(mu/mu0)`. Two solutions with the same beta differ by a constant. Choosing b(mu0)=0 without an independent condition would insert selection information. The two-loop discussion in [1], pages 9-10, explicitly distinguishes these issues from regulator-dependent evanescent divergences.

## INFORMATION_RANK / RESIDUAL_FREEDOM / ABLATION

On the exhibited one-dimensional matching slice, `d_before=1`, `R_QLC=0`, `d_after=1`. For the full quantum-law fibre we have only `d_after >= 1` in this formal domain; its global/functional dimension is not determined. The broader family of possible local normalization maps is not silently replaced by this finite slice.

Covariance alone, causal composition alone, Ward consistency alone, or their union with unitarity cannot remove this already-admissible b direction. Fixing the preparation removes no law direction. Fixing the common renormalization scale is not fixing the matching value. A separately justified on-shell condition with nonzero derivative with respect to b supplies one independent constraint and fixes this one coordinate, but does not fix every higher-order coordinate.

A useful external positive control is the supersymmetric Ward-identity example in [1]: extra symmetry can fix a finite part in an appropriate theory. That changes the physical assumptions/spectrum and is NOT adopted here. It shows why the required information must actually act on the surviving physical amplitude, rather than merely repeat a composition axiom.

Thus QLC supplies Type I/II information but not Type III selection on the exhibited slice. A globally minimal quantum selector has not been established. Nor is minimality of the entire earlier RHPI compound package proven by this gate.

## WEAK_FIELD_RECOVERY / CHI_ABC_EMBARGO_STATUS

The classical order, inherited Newtonian normalization, fixed matter data, and free graviton sector agree. The witness is an order-epsilon^2 difference in quantum matching, not a correction to SF022's classical 1PN coefficient. SF025 computes no chi_ABC and opens no quantum connected-outcome gate.

## COMPUTATIONAL EVIDENCE

`scripts/sf025_sf026_checks.py`, commit `36d3f61f35792177333ada9615983c595b3c9863`; SHA-256 `c9bea62cdb327cf7841959204b9f656163fd71a284f00176361f0a24da3399f8`.
`results/raw/SF025_CHECKS.json`, commit `76196971282e7e6ed7d9859d8b8f8fb547981a37`: 9 checks, failures=[]. Executed locally, not via GitHub Actions. These are logical/algebraic controls, not a fresh computation of a two-loop graviton amplitude.

## NEW_STRUCTURAL_FACT / CLAIM_CEILING / EXACT_NEXT_ADMISSIBLE_GATE

Classical-law selection and quantum-law selection occupy different fibres even after ordinary state/preparation freedom is removed. The missing datum can be localized to a finite nonredundant on-shell matching coordinate at positive loop order, rather than attributed vaguely to an unknown state of the universe.

Next theory gate: prospectively define a condition that acts on this relative quantum fibre, and test whether it fixes the physical matching coefficient without importing its desired value. Possible targets are an independently justified exact quantum constraint/representation condition or a microscopic matching rule. Merely writing 'anomaly free', 'no external boundary', 'unitary' or 'self-consistent' is insufficient without an explicit operator/measure construction and a nonzero information-rank argument. Nonperturbative promotion and all RQIR detector/resource gates remain open.

## Primary sources and audited locations

[1] Z. Bern, H.-H. Chi, L. Dixon, A. Edison, Two-Loop Renormalization of Quantum Gravity Simplified, arXiv:1701.02422, especially eqs. (4)-(8) and pp. 9-10. https://arxiv.org/abs/1701.02422

[2] D. C. Dunbar, J. H. Godwin, G. R. Jehu, W. B. Perkins, Loop Amplitudes in an Extended Gravity Theory, arXiv:1711.05526, section 4, eqs. (39)-(42). https://arxiv.org/abs/1711.05526

[3] R. Brunetti, K. Fredenhagen, K. Rejzner, Quantum gravity from the point of view of locally covariant quantum field theory, arXiv:1306.1058, section 3.4 eqs. (46)-(50), section 4. https://arxiv.org/abs/1306.1058

[4] G. Barnich, F. Brandt, M. Henneaux, General solution of the Wess-Zumino consistency condition for Einstein gravity, arXiv:hep-th/9409104. https://arxiv.org/abs/hep-th/9409104

[5] S. Hollands, R. M. Wald, Local Wick Polynomials and Time Ordered Products of Quantum Fields in Curved Spacetime, arXiv:gr-qc/0103074; Existence of Local Covariant Time Ordered Products, arXiv:gr-qc/0111108. Scalar-field mathematical sanity checks only, not a gravitational uniqueness theorem.
