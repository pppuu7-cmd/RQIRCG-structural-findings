# SF027 — quantum-constraint / anomaly-freedom authority notes

Status: source/theorem audit under prospective preregistration `de5e6b2ec26f9098f59c46bf0271e33326429230`.

## INHERITED OBJECT

The target is the one-dimensional physical matching slice exhibited in SF025:

`delta Gamma = epsilon^2 delta b(mu) kappa^2 I_3`,

`I_3 = integral sqrt(-g) R_ab{}^cd R_cd{}^ef R_ef{}^ab`.

SF025 already established in its declared formal EFT scope that `I_3` is diffeomorphism invariant, obeys the homogeneous Ward/BRST consistency condition, changes a physical on-shell graviton amplitude, and leaves the classical law and incoming preparation fixed.

The target is therefore not whether diffeomorphism invariance exists, but whether an explicit quantum-constraint condition has nonzero information rank on the physical matching coordinate `b`.

## LANE A — QCA-P: perturbative BV/QME

### A1. Fredenhagen–Rejzner renormalized BV/QME

Primary source:

K. Fredenhagen, K. Rejzner, `Batalin-Vilkovisky formalism in perturbative algebraic quantum field theory`, arXiv:1110.5232.

Relevant authority:

- the renormalized quantum master equation is formulated in the perturbative algebraic setting;
- Section 4.3 explicitly treats its behavior under the Stückelberg–Petermann renormalization group;
- Proposition 4.2 states that if an interaction solves the QME for one renormalized time ordering, its renormalization-group transform solves the corresponding QME for the transformed time ordering;
- the concluding discussion explicitly retains finite-renormalization freedom governed by the renormalization group while the QME and quantum BV operator transform correctly.

This is decisive against the inference `QME consistency => unique finite normalization/matching datum`.

It does not by itself prove that every possible physical Wilson coefficient is arbitrary. It shows that QME is a consistency condition compatible with nontrivial finite renormalization structure.

### A2. Brunetti–Fredenhagen–Rejzner perturbative gravity

Primary source:

R. Brunetti, K. Fredenhagen, K. Rejzner, `Quantum gravity from the point of view of locally covariant quantum field theory`, arXiv:1306.1058.

Relevant authority:

- perturbative quantum gravity is constructed generally covariantly using renormalized BV methods;
- the framework explicitly treats gravity as an effective theory rather than solving nonrenormalizability;
- the QME is used as a renormalization condition;
- the construction retains possible finite renormalizations and a renormalization-group action.

This is the same formal domain needed for the SF025 counterterm witness. The source does not provide a condition that fixes the physical `I_3` finite matching coefficient.

### A3. Einstein-gravity BRST/Wess–Zumino cohomology

Primary source:

G. Barnich, F. Brandt, M. Henneaux, `General solution of the Wess-Zumino consistency condition for Einstein gravity`, arXiv:hep-th/9409104, Phys. Rev. D 51 R1435 (1995).

The source constructs the local Wess–Zumino consistency cohomology for four-dimensional Einstein gravity. It is relevant authority for distinguishing anomalies/BRST-trivial pieces from allowed local cohomology classes.

For SF027 the decisive physical test remains the already-proved SF025 fact: the diffeomorphism-invariant `I_3` direction is a homogeneous allowed local direction with nonzero on-shell amplitude. Therefore perturbative BRST/QME consistency does not remove it.

### Lane A result

`R_QCA-P = 0` on the frozen SF025 matching slice.

Reason:

For every sufficiently small physical coefficient `b` in the common formal EFT domain, the `b I_3` finite local direction remains in the perturbative gauge-consistent/QME-compatible family while changing the matched on-shell amplitude.

This is stronger than saying a regulator choice is ambiguous: SF025 already quotiented scheme changes that leave the physical amplitude unchanged. The surviving `b` is physical matching data.

Lane A classification:

`PERTURBATIVE_BV_QME_CONSISTENCY_HAS_ZERO_SELECTION_RANK_ON_SF025_B_SCOPED`.

## LANE B — QCA-C: exact canonical quantum constraint / HDA

### B1. Thiemann anomaly-free Hamiltonian-constraint construction

Primary sources:

- T. Thiemann, `Anomaly-free formulation of non-perturbative, four-dimensional Lorentzian quantum gravity`, arXiv:gr-qc/9606088.
- T. Thiemann, `Quantum Spin Dynamics (QSD)`, arXiv:gr-qc/9606089.
- T. Thiemann, `QSD III: Quantum Constraint Algebra and Physical Scalar Product in Quantum General Relativity`, arXiv:gr-qc/9705017.

These are genuine explicit canonical quantum-gravity constructions. They define a continuum Wheeler–DeWitt/Hamiltonian constraint and formulate a non-anomalous constraint algebra in a specific connection/spin-network representation. QSD III describes implementation of the classical constraint algebra on the diffeomorphism-invariant Hilbert space in an appropriate sense.

These sources therefore defeat the overly strong statement `no explicit anomaly-free quantum constraint construction exists`.

However they do not satisfy the SF027 selector map requirement. They do not provide an audited map

`canonical constraint-operator ambiguity data -> SF025 weak-field positive-loop on-shell Riemann^3 matching coefficient b`

with the same fixed classical action/preparation and physical equivalence quotient.

Thus they cannot currently be assigned a physical information rank on the SF025 matching coordinate.

### B2. Constraint-algebra counter-audit

Primary source:

R. Gambini, J. Lewandowski, D. Marolf, J. Pullin, `On the consistency of the constraint algebra in spin network quantum gravity`, arXiv:gr-qc/9710018.

This paper directly audits the sense in which Thiemann-type Hamiltonian constraints realize the classical bracket. It points out that the vanishing quantum commutator on the relevant dual states can correspond to an effective quantum realization in which the classical `q^{ab} V_b` structure is represented trivially; alternative regularization choices can make the corresponding object nonzero while then exposing an anomaly.

SF027 does not use this as a universal refutation of loop quantization. It establishes that the word `anomaly-free` alone does not define a representation-independent strong HDA equality with unique physical content.

### B3. Regularization ambiguity

Primary source:

A. Perez, `On the regularization ambiguities in loop quantum gravity`, arXiv:gr-qc/0509118, Phys. Rev. D 73, 044007 (2006).

Perez states explicitly that regularization ambiguities lead to an apparently infinite set of possible theories. The paper studies the representation (`m`) ambiguity; in 2+1 dimensions continuum/topological consistency can select the fundamental representation, while the 3+1 analysis remains incomplete because of difficulties with the physical inner product and exhibits spurious solutions for other choices.

This is a particularly important SF027 countercontrol:

`well-defined/anomaly-controlled quantum constraints != unique four-dimensional quantum dynamics`.

The source does not establish that all ambiguities survive all future physical tests. It does show that constraint quantization and anomaly control do not automatically supply a unique quantum law.

### B4. Exact HDA in a model is not a matching selector for 4D Lorentzian GR

Comparator source:

T. Thiemann, `Exact quantisation of U(1)^3 quantum gravity via exponentiation of the hypersurface deformation algebroid`, arXiv:2207.08302.

The U(1)^3 model admits an exact anomaly-free representation of its hypersurface-deformation structure. This is a useful existence control for exact quantization technology, but it is a different model and does not provide a physical map to the SF025 matching coefficient of the RHPI/ADM weak-field graviton sector.

No dynamics or coefficient from this comparator is imported.

### Lane B result

The exact-canonical candidate is **not** assigned rank zero. The physical map required by the preregistration is absent:

`R_QCA-C = UNDEFINED_MATCHING_MAP_MISSING`.

The audited constructions supply constraint operators and anomaly/closure notions, but no source gives all of:

1. a common exact quantum total gravity+matter constraint object in the SF025 domain;
2. a closure criterion strong enough to identify the relevant physical representation;
3. a fixed physical-state/inner-product construction adequate for the matching comparison;
4. a map from the operator/regularization data to the on-shell coefficient `b`;
5. a uniqueness theorem for that mapped physical coordinate.

Lane B classification:

`EXACT_CANONICAL_QHDA_MATCHING_SELECTOR_BLOCKED_MISSING_PHYSICAL_MAP_SCOPED`.

This is `BLOCKED`, not a claim that exact quantum HDA can never constrain EFT matching.

## LANE C — ambiguity / counterexample audit

The strongest counterexample structure is two-level:

1. In the explicit perturbative BV/QME realization, the SF025 physical `b` direction already survives. This is an exact scoped rank-zero counterexample to the slogan `quantum gauge anomaly freedom fixes the matching law`.
2. In canonical nonperturbative constructions, anomaly-free/constraint-consistent operators exist, but the literature itself contains nontrivial regularization and representation issues and no audited map to `b`. Therefore these constructions cannot rescue complete selection on the present gate.

It would be invalid to combine the perturbative on-shell matching coordinate and a specific loop-quantization regularization parameter as though they were the same physical coordinate. SF027 explicitly does not make that identification.

## LANE D — state/law and UV-data firewall

The SF025 incoming preparation remains fixed.

No vacuum, state, density matrix, boundary condition or readout is changed to obtain the Lane A result.

No UV spectrum is chosen. SF005 already established that generic UV-completability/causality transfers matching information into spectral data rather than selecting a unique coefficient. SF027 does not repeat that gate.

Therefore the residual perturbative `b` freedom remains a quantum-law/on-shell-matching freedom, not a state ambiguity.

## INFORMATION-RANK SUMMARY

Frozen one-dimensional SF025 slice:

- before QCA: `d_before = 1`;
- perturbative QCA-P: `R_QCA-P = 0`, `d_after = 1`;
- exact canonical QCA-C: physical matching rank `UNDEFINED_MATCHING_MAP_MISSING`.

No audited realization reaches `R_QCA = 1_complete`.

No audited realization supplies a valid partial equality/bound on `b` using only already-fixed data that is new relative to SF005.

## CLAIM CEILING

This audit does not establish:

- that all conceivable quantum-constraint principles have zero selection power;
- that loop quantum gravity is inconsistent;
- that exact HDA is impossible;
- that `b` is arbitrary in a UV-complete theory;
- a preferred regulator or representation;
- a quantum state;
- a quantum matching coefficient;
- a new candidate law;
- `chi_ABC`.

It establishes only the preregistered scoped result: perturbative BV/QME anomaly freedom has zero information rank on the exhibited SF025 matching direction, while the audited exact canonical route lacks the physical map needed to claim selection on that direction.
