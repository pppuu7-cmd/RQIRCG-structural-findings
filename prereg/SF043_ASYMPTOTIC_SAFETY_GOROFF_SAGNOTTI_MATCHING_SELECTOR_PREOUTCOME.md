# SF043 — asymptotic-safety Goroff–Sagnotti matching selector — PREOUTCOME

Date: 2026-09-15
Inherited theory frontier: `GENUINELY_NEW_MICROSCOPIC_MATCHING_PRINCIPLE_WITH_EXPLICIT_PHYSICAL_MAP_REQUIRED`.

## PURPOSE

Test whether an ultraviolet fixed-point / critical-surface principle in the **minimal essential asymptotic-safety scheme** supplies genuine nonzero selection power on the same physical positive-loop curvature-cubic matching direction isolated by SF025.

This is a successor-theory/source/map audit. It does not import asymptotic-safety dynamics into historical RCG-002 or parent RQIRCG.

## CANDIDATE PRINCIPLE

`ASGS = ASYMPTOTIC_SAFETY_GOROFF_SAGNOTTI_TRAJECTORY_SELECTION`.

Frozen principle statement:

A quantum gravitational law belongs to the relevant UV universality class only if its essential RG trajectory approaches a nontrivial ultraviolet fixed point with finitely many relevant directions and connects to the perturbative GR/Gaussian infrared domain. Irrelevant essential couplings are then fixed functions along the UV-safe critical trajectory once the relevant physical data are specified.

This is stronger than generic covariance/unitarity/anomaly freedom because it supplies a microscopic RG boundary condition, not merely a consistency condition.

## TARGET SF025 OBJECT

SF025 isolated a physical positive-loop on-shell matching direction represented by

`delta Gamma = epsilon^2 delta b(mu) kappa^2 I_3`,

`I_3 = integral sqrt(-g) R_ab{}^cd R_cd{}^ef R_ef{}^ab`,

after quotienting field-redefinition/EOM/pure-scheme directions.

`b` is a quantum-law/on-shell matching datum at fixed classical law and incoming preparation.

SF043 must not equate an off-shell FRG coupling with `b` by notation alone.

## REQUIRED MAP TESTS

M1. Operator identity: determine whether the essential Goroff–Sagnotti `C^3` coupling used in the audited asymptotic-safety source overlaps the same parity-even Ricci-flat/on-shell curvature-cubic amplitude direction as SF025 `I_3`, including normalization/equivalence qualifications.

M2. Essentiality: verify that the source treats the curvature-cubic coupling as essential rather than removable by local field redefinition in its declared universality class.

M3. Critical-surface selection: verify whether the curvature-cubic coupling is irrelevant at the UV fixed point and whether the UV-safe trajectory connected to perturbative GR is unique after relevant data/scale are fixed.

M4. IR matching output: identify whether the source derives a low-energy Wilson/matching constant for the curvature-cubic coupling rather than only a fixed-point coordinate.

M5. Physical-map closure: determine whether the derived low-energy constant is demonstrably regulator/truncation/field-parameterization independent at the physical on-shell level needed for SF025.

M6. Perturbative consistency: compare the low-energy running coefficient with known perturbative gravity running where the source itself performs that comparison. A mismatch must reduce physical-selector authority rather than be ignored.

M7. State independence: confirm the candidate selector acts on quantum-law matching and does not select `b` by choosing a state/vacuum/preparation.

## INFORMATION-RANK LABELS

### `R_ASGS_TRUNCATION = 1`

allowed if the audited finite essential truncation contains one UV-safe trajectory and predicts the low-energy curvature-cubic Wilson constant once relevant physical data are fixed.

This label is **truncation-level only**.

### `R_ASGS_PHYSICAL = 1`

allowed only if M1–M7 establish an explicit regulator/truncation-independent physical map to the SF025 on-shell matching coordinate.

### `R_ASGS_PHYSICAL = UNDEFINED_MAP_NOT_CLOSED`

if the truncation predicts an essential coupling but the exact physical on-shell matching map is not sufficiently controlled.

Do not relabel a missing physical map as rank zero.

## DECISION RULE

### STRONG PASS

`ASYMPTOTIC_SAFETY_SELECTS_SF025_PHYSICAL_MATCHING_DIRECTION_SCOPED`

requires `R_ASGS_PHYSICAL=1`.

### CONDITIONAL / ARCHITECTURE PASS

`ASYMPTOTIC_SAFETY_PROVIDES_NONZERO_TRUNCATION_LEVEL_MATCHING_SELECTION_SCOPED`

if `R_ASGS_TRUNCATION=1` but the physical map remains unclosed.

Required secondary label:

`PHYSICAL_ON_SHELL_MATCHING_AUTHORITY_BLOCKED_BY_TRUNCATION_OR_SCHEME_MAP`.

### FAIL

Use selector failure only if the audited ASGS principle itself leaves a continuous free curvature-cubic matching parameter even within its frozen essential truncation after relevant data are fixed.

### INVALID

Do not choose a regulator/PMS point or normalization after seeing a desired coefficient and call it physical selection.

## PRIMARY SOURCE SET

The gate may audit at minimum:

- Baldazzi, Falls, Kluth, Knorr, `Robustness of the derivative expansion in Asymptotic Safety`, arXiv:2312.03831;
- Baldazzi & Falls, `Essential Quantum Einstein Gravity`, arXiv:2107.00671;
- relevant original perturbative Goroff–Sagnotti / two-loop running authority referenced by the audited source, only as needed to understand its own IR comparison.

Additional sources may be used for operator/on-shell mapping but may not change the frozen decision rule.

## CLAIM CEILING

Even a truncation-level PASS does not establish asymptotic safety as the correct quantum theory of gravity, full quantum gravity, an experimental prediction, historical RCG-002 authority, or a unique exact value of SF025 `b`.

No `chi_ABC`, connected outcome or operational calibration result may influence this gate.
