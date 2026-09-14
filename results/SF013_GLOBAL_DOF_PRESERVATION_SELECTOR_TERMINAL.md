# SF013 — global gravitational-DOF preservation selector gate — TERMINAL / PARTIAL POSITIVE

Date: 2026-09-14
Status: **TERMINAL FOR CURRENT EVIDENCE / PARTIAL POSITIVE SELECTOR RESULT / no `chi_ABC` evaluation**

Preregistration: `8bce278e718863c7c457291173efc3eb4093105a`.

## Outcome lock

`chi_ABC` remained embargoed. SF013 tested only whether the new physical principle GDP (Global DOF Preservation) reduces the microscopic selector fiber.

## Executive classification

Two different scopes must be separated.

### Proven/strongly supported sub-scope

For four-dimensional, local, metric-only, fully diffeomorphism-invariant theories whose Lagrangian depends on the metric and at most its second derivatives, the available Hamiltonian-degeneracy classification supports:

`GDP_SELECTS_EINSTEIN_HILBERT_CLASS_IN_SECOND-DERIVATIVE-LAGRANGIAN_SCOPE`.

### Full preregistered finite-derivative scope

SF013 preregistered a broader class allowing finitely many derivatives. The present audit did **not** establish a theorem covering every such higher-jet metric Lagrangian, and no exact generic-background two-DOF counterexample satisfying all frozen clauses was found either.

Therefore the full-scope classification is:

`GDP_GLOBAL_FINITE_DERIVATIVE_UNIQUENESS_NOT_YET_ESTABLISHED`.

This is a genuine narrowing, not a global PASS or FAIL.

## Lane A — theorem audit

Lovelock-type uniqueness results cannot be used naively because ordinary Lovelock statements assume restrictions on derivative order/equation form.

A more directly relevant result is:

- M. Crisostomi, K. Noui, C. Charmousis, D. Langlois, *Beyond Lovelock gravity: Higher derivative metric theories*, arXiv:`1710.04531`.

They study four-dimensional metric dynamics with a diffeomorphism-invariant Lagrangian depending at most on second derivatives of the metric. Importantly, they do **not** simply assume second-order field equations: they impose degeneracy conditions designed to eliminate Ostrogradsky modes. Their result is that, apart from Einstein-Hilbert, the fully degenerate possibilities are trivial or contain more than two degrees of freedom; partially degenerate parity-violating cases retain problematic extra structure.

This is substantially stronger for GDP than quoting Lovelock alone: it directly tests whether degeneracy can save non-Einstein higher-derivative metric theories in that Lagrangian class.

A complementary uniqueness theorem by Curiel derives a Lovelock-like Einstein-tensor uniqueness under a different physical-dimension assumption rather than assuming second derivatives from the outset:

- E. Curiel, *A Simple Proof of the Uniqueness of the Einstein Field Equation in All Dimensions*, arXiv:`1601.03032`.

Curiel's assumptions are not identical to GDP and are not imported as part of the selector, but they show that Einstein uniqueness can arise from physically motivated restrictions other than a bare derivative-counting convention.

Lane classification:

`GDP_HAS_THEOREM_LEVEL_SELECTION_POWER_IN_A_BROAD_SECOND-DERIVATIVE-METRIC_LAGRANGIAN_CLASS`.

## Lane B — adversarial higher-curvature search

Einsteinian cubic gravity (ECG) is an essential negative control because it is a nontrivial four-dimensional curvature-cubic metric theory sharing the Einstein massless-graviton spectrum on maximally symmetric backgrounds:

- P. Bueno, P. A. Cano, *Einsteinian cubic gravity*, arXiv:`1607.06463`.

That property is insufficient for GDP, whose preregistration requires generic-background exact DOF preservation.

A later exact/non-EFT perturbation analysis around static spherically symmetric ECG black holes finds three propagating modes in the odd-parity sector, with a ghost and a gradient instability when the cubic terms are treated as unsuppressed fundamental dynamics:

- A. De Felice, S. Tsujikawa, *Excluding static and spherically symmetric black holes in Einsteinian cubic gravity with unsuppressed higher-order curvature terms*, arXiv:`2305.07217`.

Therefore ECG is **not** an SF013 counterexample: its apparently Einstein-like spectrum on maximally symmetric backgrounds is a background-limited degeneracy, not global two-DOF preservation.

This directly validates the preregistered warning that linearized spectrum matching is too weak.

Other apparent two-DOF modified-gravity families found in the literature frequently evade the frozen class by at least one route:

- only spatial, not full spacetime, covariance;
- extra fields/connections;
- massive rather than inherited massless spin-2 dynamics;
- perturbative/background-specific two-mode counting rather than generic exact Hamiltonian DOF.

A 2026 spatially covariant gravity construction, for example, explicitly relaxes full spacetime diffeomorphism invariance and establishes two DOF only perturbatively up to cubic order around cosmological backgrounds (arXiv:`2604.14490`). It is therefore outside the frozen GDP class and not a counterexample.

Lane classification:

`KNOWN_EINSTEIN_LIKE_HIGHER_CURVATURE_LINEAR_SPECTRA_DO_NOT_DEFEAT_GLOBAL_DOF_PRINCIPLE`.

## Lane C — Cauchy / higher-derivative audit

Generic local higher-curvature/higher-derivative metric theories possess extra dynamical modes because higher-order equations require additional initial data unless sufficient constraints/degeneracies remove them.

A useful review of methods and pitfalls is:

- A. Belenchia, M. Letizia, S. Liberati, E. Di Casola, *Higher-order theories of gravity: diagnosis, extraction and reformulation via non-metric extra degrees of freedom*, arXiv:`1612.07749`.

The 2017 degeneracy analysis above closes a large and important sub-class, but the SF013 preregistration allowed arbitrary finite derivative order. The present search did not locate a general theorem proving that **every** local, fully diffeomorphism-invariant, pure-metric, finite-jet theory with exactly two generic physical DOF is field-redefinition/topological equivalent to Einstein-Hilbert.

Absence of a found counterexample is not a uniqueness proof.

Therefore the full finite-derivative claim remains blocked at theorem level.

Lane classification:

`ARBITRARY_FINITE_JET_TWO_DOF_METRIC_UNIQUENESS_REMAINS_UNPROVEN_IN_THIS_GATE`.

## Lane D — residual parameters

Even in the positive Einstein-Hilbert sub-scope, GDP does not fix every global/zero-derivative datum.

The local dynamical class may still contain:

- Newton normalization, already inherited/calibrated;
- a cosmological constant `Lambda`, which GDP does not determine;
- topological/boundary terms that do not alter local 4D gravitational DOF.

For the laboratory connected-phase programme, `Lambda` can often be treated as an independently calibrated/background datum, but it cannot be silently claimed as predicted by GDP.

Thus the correct scoped statement is selection of the **local dynamical form**, not selection of all boundary/cosmological data.

Lane classification:

`GDP_SELECTS_LOCAL_DYNAMICAL_CLASS_MORE_STRONGLY_THAN_GLOBAL_BACKGROUND_DATA`.

## Selector-fiber interpretation

SF012 provides the correct language for the result.

Before GDP, the local higher-order physical selector fiber contained homogeneous nonlinear directions.

In the broad second-derivative-metric Lagrangian class analyzed by Crisostomi et al., imposing exact generic two-DOF preservation collapses that fiber to the Einstein-Hilbert class (modulo trivial/topological/equivalent pieces and `Lambda`).

Therefore GDP is the **first tested new principle in this repository that demonstrably shrinks the physical selector fiber far beyond a bound or coordinate change.**

This makes GDP scientifically more promising than SF001-SF011’s failed selector candidates.

## Why this does not undo SF002

SF002 rejected an unmotivated rule of the form “forbid higher derivatives/new modes because minimality is nice.”

SF013 instead asks for an exact physical property of the nonlinear Cauchy problem: preserve the inherited physical gravitational phase-space content globally.

The derivative restriction emerges in a large classified sub-scope as a consequence of eliminating extra exact modes, rather than being inserted solely to force uniqueness.

The distinction is essential.

## Terminal decision

Record both levels simultaneously:

`PASS_SCOPED: GDP_SELECTS_EINSTEIN_HILBERT_CLASS_IN_SECOND_DERIVATIVE_LAGRANGIAN_SCOPE`

and

`BLOCKED_GLOBAL: GDP_GLOBAL_FINITE_DERIVATIVE_UNIQUENESS_NOT_YET_ESTABLISHED`.

## New scientific finding

RQIRCG structural findings now has its first plausible **positive physical selector mechanism**:

`global nonlinear preservation of the inherited massless-spin-2 DOF`.

Unlike positivity, gauge closure, universal coupling, fixed-point behavior, constructibility or entropy extremization, this principle can actually eliminate known higher-curvature nonlinear freedom when exact generic DOF counting is enforced in a broad local metric class.

## Exact next admissible work

Do **not** open `chi_ABC` yet.

Two gates must be completed first:

1. **SF014 — GDP escape-space audit:** test the arbitrary-finite-derivative, nonlocal, extra-field/auxiliary, and emergent escape classes separately and determine whether any satisfy the intended physical content without adding observable gravitational DOF.
2. **SF015 — quantum-state/influence closure after local-dynamics selection:** even if the classical local generator is Einstein-Hilbert-like, determine whether the quantum state/measure/influence rule is uniquely fixed or whether NP1-like phase/noise freedom survives at the quantum operational level.

Only if both are sufficiently closed should the embargo on the connected observable be reconsidered.
