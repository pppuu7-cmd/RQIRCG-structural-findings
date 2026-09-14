# SF013 — global gravitational-DOF preservation selector gate — PREREGISTRATION

Date: 2026-09-14
Status: **FROZEN PRE-OUTCOME NEW-PHYSICAL-PRINCIPLE GATE**

## Why this candidate is different

SF002 rejected “no higher derivatives/new modes” when used as an unmotivated minimality convention. SF013 instead tests a physical statement about **initial-data content**:

> The nonlinear gravitational completion must possess exactly the same local physical gravitational degrees of freedom as the inherited massless spin-2 carrier, not merely around Minkowski or one symmetric background, but throughout its declared dynamical domain. No hidden scalar/tensor/ghost branch or extra independent gravitational initial data may appear nonlinearly.

Call this principle **GDP** (`Global DOF Preservation`).

This is explicitly a new physical principle beyond frozen RQIR, not something claimed to have been derived there.

`chi_ABC` remains embargoed.

## Frozen inherited carrier

The inherited weak-field gravitational sector contains one massless spin-2 field with the usual gauge redundancy and two local propagating tensor polarizations in four dimensions, together with the calibrated Newtonian/weak-field normalization.

SF013 asks whether demanding exact preservation of that physical phase-space content selects the nonlinear generator.

## Scope frozen for the first GDP gate

To make the decision falsifiable rather than universal-by-wording, freeze the following class:

1. four spacetime dimensions;
2. local metric-only classical gravitational generator, possibly with finitely many derivatives;
3. full spacetime diffeomorphism invariance;
4. no additional fundamental matter-like gravitational fields introduced solely to rewrite higher derivatives;
5. exact/fundamental dynamics, not an EFT truncation interpreted order-by-order with spurious high-frequency solutions discarded by prescription;
6. same weak-field massless spin-2 branch and Newton normalization;
7. admissible domain includes generic backgrounds for which the theory claims fundamental validity, not only maximally symmetric backgrounds.

This scope is intentionally narrower than “all possible quantum gravity.” If GDP succeeds here, later gates must audit nonlocal/emergent/extra-field escape classes separately.

## GDP condition

A completion passes GDP only if its full constrained Hamiltonian/Cauchy problem has exactly two local physical gravitational configuration DOF per spatial point (equivalently four-dimensional reduced phase space per point), with no additional independent local initial-data functions on generic admissible backgrounds.

Linearized two-polarization behavior on one background is insufficient.

## Positive selector criterion

Return

`GDP_SELECTS_EINSTEIN_LOVELOCK_CLASS_SCOPED`

only if, within the frozen class, the GDP condition plus the inherited normalization reduces the physical selector fiber to Einstein-Hilbert dynamics with at most:

- a cosmological constant/boundary datum requiring separate treatment;
- four-dimensional topological/boundary terms that do not change local dynamics;
- physically equivalent field redefinitions.

A remaining continuous dynamical coefficient that changes generic local evolution falsifies uniqueness.

## Counterexample-first failure criterion

Return

`GDP_INSUFFICIENT_TWO_DOF_NON_EINSTEIN_FREEDOM_SURVIVES`

if there exists a local, metric-only, fully diffeomorphism-invariant 4D theory with:

1. exactly two local physical gravitational DOF on generic backgrounds in its fundamental exact formulation;
2. the same weak-field massless spin-2/Newton branch;
3. genuinely different nonlinear local dynamics from Einstein-Hilbert after physical quotient;
4. an independent continuous coupling not fixed by the inherited normalization.

## Mandatory lanes

### Lane A — theorem audit
Audit what Lovelock-type uniqueness theorems actually assume. Do not replace GDP by “second-order equations” unless GDP itself is shown to entail that condition in the frozen class.

### Lane B — higher-derivative/degeneracy counterexample search
Search for metric-only generally covariant higher-curvature theories claimed to propagate only the massless graviton. Distinguish:

- same spectrum only on maximally symmetric backgrounds;
- perturbative EFT two-DOF interpretation;
- exact generic-background Hamiltonian two-DOF theories.

Only the third category falsifies GDP selector power.

### Lane C — constraint/Cauchy analysis
Determine whether generic finite higher-time-derivative metric dynamics necessarily adds initial-data modes unless degenerate/topological/field-redefinition-equivalent, and whether known degeneracies evade that implication.

### Lane D — residual parameters
Audit cosmological constant, topological terms and any integration/boundary constants separately. GDP is not allowed to claim a unique `Lambda` unless it actually fixes it.

## Strict anti-shortcut rules

- “Einsteinian cubic gravity has two modes around AdS/Minkowski” is not sufficient to falsify GDP; generic-background exact DOF must be checked.
- “Lovelock theorem says GR” is not sufficient to prove GDP unless its derivative-order assumptions are derived or explicitly scoped.
- EFT order reduction does not count as exact fundamental GDP preservation.

## Claim ceiling

A positive SF013 result would be a scoped uniqueness result for local 4D metric-only fundamental dynamics, not a proof that Nature chooses GR, not quantum gravity, and not a rejection of nonlocal/emergent/extra-field completions.

## Next-step rule

If GDP selects a unique local dynamics class, freeze that class **before** computing `chi_ABC`, then audit whether the remaining quantum/influence-state rule is separately fixed. If GDP fails, record the exact two-DOF counterexample and identify what additional principle distinguishes it.
