# SF007 — frozen RQIR latent microscopic-selector audit — TERMINAL

Date: 2026-09-14
Status: **TERMINAL / frozen-core boundary audit / no `chi_ABC` evaluation**

Preregistration: `0a851bdabc1ec897ca03750e135ce0c16ec8cd0a`.

## Outcome lock

The decision rule was frozen before reading the authoritative RQIR core documents in this gate. `chi_ABC` remained embargoed.

## Authoritative RQIR objects audited

Primary frozen/core authority:

- `README.md`;
- `RQIR_VERSION.json`;
- `docs/RQIR_CORE_V1_FREEZE_MANIFEST_2026-09-09.md`;
- `docs/FOUNDATIONS.md`;
- `docs/MASTER_TABLE.md`.

Candidate-interface authority used to determine whether state space/dynamics are supplied by the core or by a future model:

- `candidate_gravity/MODEL_TO_RQIR_CONTRACT.md`;
- `candidate_gravity/NEW_MODEL_CHECKLIST.md`;
- `candidate_gravity/MODEL_SPEC_TEMPLATE.md`;
- `candidate_gravity/GATE_STATUS_TEMPLATE.yaml`;
- `candidate_gravity/recovery/CURRENT_QG_FRONT.md`.

This is stronger than a keyword absence test: the declared scope, freeze manifest, foundations, operational master table, model contract, model boot rules and gate semantics were read directly.

## Lane A — scope / claim audit

RQIR Core v1.0 declares itself a **model-independent reconstruction/evaluation framework**, not a microscopic physical theory.

Its objective is to reconstruct, from consistency requirements and observables, what operational structure the gravity-quantum interface must possess without choosing a preferred quantum-gravity theory in advance.

The README explicitly separates:

1. established baseline physics;
2. model-independent residuals/null tests;
3. candidate realizations.

Candidate realizations are tested against the same observable channels rather than used as starting axioms.

The README also states that a successful outcome need not be a single microscopic theory: it may be a sharply constrained equivalence class plus discriminants.

`docs/FOUNDATIONS.md` is even more explicit: its status is “operational reconstruction framework; not a physical theory.” Its inverse problem returns an experimentally indistinguishable equivalence class `[I]` from detector probabilities.

Therefore the declared target of the frozen core is not microscopic uniqueness.

Lane classification:

`RQIR_CORE_TARGET_IS_OPERATIONAL_EQUIVALENCE_CLASS_NOT_MICROSCOPIC_UNIQUENESS`.

## Lane B — frozen requirement inventory

The freeze manifest lists the frozen core as:

- operational-first observable hierarchy;
- baseline/residual discipline;
- source calibration and identifiability;
- nuisance geometry/covariance;
- negative controls;
- physical resource/experiment architecture;
- detector-facing estimability;
- comparator/failure-state semantics;
- provenance/reproducibility and governance.

The Foundations consistency gates include dimensional, gauge/relational, conservation/Bianchi, positivity/unitarity/CP, spectral/commutator consistency, causality, classical/gravity-off/flat/Newtonian limits, EFT power counting, renormalization, known tests, degeneracy and operational measurability.

Critically, the Foundations document itself states:

`Passing the gates is necessary, not sufficient.`

These are constraints on candidate predictions, not a generator for microscopic spectrum/dynamics.

The Master Table’s single-dynamics rule says a concrete model must derive all RQIR-facing objects from one coherent dynamics; it does not supply that dynamics.

Lane classification:

`FROZEN_REQUIREMENTS_ARE_OBSERVABLE_CONSISTENCY_IDENTIFIABILITY_AND_RESOURCE_CONSTRAINTS`.

## Lane C — microscopic ontology/dynamics audit

The strongest possible apparent latent selector is the CTP source-side object `[Z_T]` in Foundations. But RQIR explicitly treats it as a **candidate source-side information object** and inserts an unspecified gravity-interface map

`[Z_T] -> I_G -> [Z_obs] -> detector probabilities`.

Thus the CTP object organizes source information; it does not specify the physical gravitational state space, spectrum, nonlinear carrier generator or microscopic interface law.

Likewise Q3 (“Backreaction/source rule”) is posed as an operational question among expectation-value, stochastic, conditional, operator-valued or other structures. It does not choose one.

The Candidate Gravity contract resolves the ownership question unambiguously. A concrete model must supply:

- model state preparation and boundary conditions;
- first/noise/response/higher source hierarchy;
- a parent CTP/influence/channel object or alternative fundamental representation;
- conservation/causality/positivity evidence.

The model boot checklist requires, **before model-specific RQIR fitting/search**, declaration of:

- physical state space;
- gravity and matter variables;
- primary dynamics;
- interaction/coupling;
- constraints/gauge structure;
- parameter domain and approximation/EFT order.

The model specification template likewise requires a model to provide Hilbert/algebraic/state space, boundary/asymptotic data, action/Hamiltonian/master equation/channel/influence functional/path integral or equivalent, couplings and initial/boundary conditions.

These are exactly the kinds of objects SF006 identified as the missing microscopic generating data. RQIR assigns them to the **candidate model**, not to the frozen core.

Lane classification:

`MICROSCOPIC_STATE_SPACE_DYNAMICS_AND_BOUNDARY_DATA_ARE_MODEL_INPUTS_TO_RQIR`.

## Lane D — entailment / gate-order audit

`GATE_STATUS_TEMPLATE.yaml` makes the logical order explicit:

- `QG-001 Physical state space` — blocker: specify physical/gauge state space and observables;
- `QG-002 Matter-gravity dynamics` — blocker: supply action/Hamiltonian/channel/influence dynamics;
- only then come Newtonian/GR limits, unitarity/positivity, gauge closure, model discriminator, RQIR propagation, identifiability and resources.

Promotion from ansatz to candidate requires QG-001 and QG-002 to pass.

This is decisive for the SF007 entailment test. The frozen judge does not logically derive QG-001/QG-002 from the later consistency gates; it treats them as independently supplied model content that must be evidenced before promotion.

The current Candidate Gravity front is historically consistent with this reading: despite mature comparator/infrastructure machinery, the active promotable ansatz is `none`, and the rubric assigns zero credit to frozen parent dynamics/ANSATZ. This historical state is supporting evidence only; the terminal classification follows from the frozen architecture above.

Lane classification:

`RQIR_TESTS_MICROSCOPIC_DYNAMICS_AFTER_SUPPLY_IT_DOES_NOT_ENTAIL_THEM`.

## Terminal decision

The preregistered negative criterion is satisfied:

`RQIR_FROZEN_REQUIREMENTS_DO_NOT_SELECT_MICROSCOPIC_GENERATING_DATA_SCOPED`.

## Stronger programme-boundary statement

Combining VB1, NP1/CM1, and SF001-SF007 gives the following scoped chain:

`RQIR observable/consistency requirements`

`+ RCG-002 relational operational architecture`

`+ closed total-source bookkeeping`

`+ positivity / normalized evolution`

`+ one closed generator`

`+ nonlinear gauge/Bianchi closure`

`+ universal self-source coupling`

`+ associative closed composition`

`+ soft/factorization/unitarity/crossing/causal analyticity`

`+ finite positive IR/spectral calibration`

`DO NOT, AS CURRENTLY FROZEN, SELECT A UNIQUE MICROSCOPIC GENERATING DATUM.`

The residual information can be represented schematically as

`S_micro = {physical state/spectrum, microscopic dynamics/couplings, boundary or equivalent generating rule}`.

Without an independently chosen rule for `S_micro`, the homogeneous nonlinear/Wilson sector remains matching data rather than a prediction of RQIR.

## Scientific meaning

This is not a failure of RQIR. It is consistent with RQIR’s declared purpose: the frozen core is a model-independent operational judge and reconstruction framework. Its scientific strength is precisely that it does not hide a preferred microscopic ontology inside the evaluation criteria.

It follows that the new structural-findings repository has reached the point where **continuing to mine frozen RQIR for another generic consistency selector is no longer justified**.

A further nonlinear theory requires a genuinely new, prospectively declared physical principle beyond RQIR Core v1.0.

## What the new principle must now accomplish

A successful post-RQIR principle must fix, rather than merely constrain, enough microscopic generating data to determine the homogeneous nonlinear sector. Candidate classes may include, for example:

- a state/spectrum reconstruction principle;
- a microscopic relational-composition law with a unique representation;
- a UV boundary/fixed-point principle;
- a complete amplitude/state-sum bootstrap condition;
- another rule of equivalent information content.

These examples are search classes, not imported physics and not selected candidates.

## Exact next admissible step

Open a **new-principle class search** outside frozen RQIR semantics, with all candidate classes frozen before calculating `chi_ABC`.

The next gate should compare candidate principle classes by information content and falsifiability, not by whether they produce a preferred connected-phase outcome.

`chi_ABC` remains embargoed.
