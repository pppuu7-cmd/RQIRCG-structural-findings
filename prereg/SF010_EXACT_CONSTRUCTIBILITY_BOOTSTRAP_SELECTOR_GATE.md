# SF010 — exact constructibility / bootstrap dynamical-weight selector — PREREGISTRATION

Date: 2026-09-14
Status: **FROZEN PRE-OUTCOME NEW-PRINCIPLE GATE**

## Candidate principle class — ECB

Call the principle **ECB** (`Exact Constructibility Bootstrap`).

The candidate principle is stronger than the SF005 consistency package:

> The physical graviton/interface amplitude or equivalent dynamical weight is completely reconstructible from its physical singularities, lower-point amplitudes, universal soft data and admissible asymptotic behavior. No independent polynomial/contact ambiguity is allowed unless it is itself fixed by the same recursive data.

This is tested as a new microscopic principle, not assumed to follow from ordinary locality/unitarity.

`chi_ABC` remains embargoed.

## Scientific question

Does exact constructibility remove the homogeneous/contact-term freedom that survived SF003-SF009 without merely restating “set all independent contact terms to zero”?

## Positive criterion

ECB passes only if:

1. the inherited massless spin-2 seed and weak-field normalization fix all primitive on-shell data;
2. recursion/factorization/soft/asymptotic conditions determine every higher-point amplitude uniquely;
3. no independent higher-derivative three-point seed or contact term survives;
4. the asymptotic condition used to close recursion is independently physical rather than a hidden derivative-order/minimality axiom.

Positive verdict:

`ECB_SELECTS_DYNAMICAL_WEIGHT_SCOPED`.

## Counterexample-first failure criteria

Return

`ECB_INSUFFICIENT_PRIMITIVE_SEED_OR_BOUNDARY_TERM_FREEDOM_SURVIVES`

if any of the following survives:

1. an independent higher-derivative three-point graviton amplitude consistent with little-group/Lorentz/locality data;
2. a contact polynomial invisible to factorization poles and ordinary soft constraints;
3. a recursion boundary term at complex infinity not fixed by physical factorization data;
4. the only way to remove such freedom is to postulate a large-complex-momentum falloff/no-contact rule equivalent in information content to excluding higher-derivative operators by hand.

## Mandatory lanes

### Lane A — primitive seed audit
Determine whether massless spin-2 kinematics admits higher-derivative three-point structures beyond the inherited two-derivative seed.

### Lane B — factorization/contact audit
Determine whether pole factorization fixes polynomial contact terms or leaves homogeneous amplitude solutions.

### Lane C — recursion-at-infinity audit
Determine what additional large-complex-momentum/asymptotic assumptions are required for exact recursion and whether they are independently justified.

### Lane D — EFT/bootstrap sanity check
Use amplitude/EFT literature only as external comparator to test whether consistent higher-derivative gravity amplitudes can be recursively/softly constructed without being fixed by Einstein normalization.

## Non-tautology rule

A principle stated as “the amplitude has no independent contact terms” is not considered derived unless a separate physical argument fixes that property. Likewise choosing the best BCFW falloff because it selects the desired low-derivative theory is forbidden.

## Claim ceiling

SF010 does not establish a full gravitational S-matrix nonperturbatively and does not reject bootstrap approaches. It tests whether constructibility alone contains enough information to select the nonlinear dynamical weights relevant to this programme.
