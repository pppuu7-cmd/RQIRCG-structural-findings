# SF011 — extremal / information dynamical-weight selector — TERMINAL

Date: 2026-09-14
Status: **TERMINAL / new-principle class evaluated / no `chi_ABC` evaluation**

Preregistration: `7d62df38c9f5e1dc1ff26441da7618bbc7be7aa5`.

## Outcome lock

SF011 did not evaluate `chi_ABC` and did not choose an entropy/information functional after inspecting any nonlinear outcome.

## Lane A — conditional variational uniqueness

For a fixed positive reference measure `m(x)` and linear constraints, maximizing relative entropy

`S[p|m] = - Integral p(x) log[p(x)/m(x)] dx`

is a convex/concave variational problem whose solution has exponential-family form

`p_m(x) = m(x) exp(-lambda_0 - Sum_a lambda_a f_a(x))`.

Thus an extremal-information rule can indeed convert a declared reference measure and declared constraints into a unique selected distribution under standard regularity conditions.

This is real mathematical selection power, but it is conditional on the prior/reference measure and on the functional being specified.

Lane classification:

`EXTREMIZATION_CAN_SELECT_UNIQUELY_CONDITIONAL_ON_REFERENCE_MEASURE_AND_FUNCTIONAL`.

## Lane B — exact prior-dependence witness

Use the discrete variable

`x in {0,1,2}`

with frozen constraints

`Sum_i p_i = 1`,

`Sum_i x_i p_i = 1`.

Take two positive reference measures, written up to normalization,

`m_A = (1,1,1)`

and

`m_B = (1,4,1)`.

Both are symmetric under `x -> 2-x`. Therefore the mean-one constraint is satisfied at Lagrange multiplier `lambda=0` for both maximum-relative-entropy solutions.

The unique selected distributions are then

`p_A = (1/3, 1/3, 1/3)`

and

`p_B = (1/6, 4/6, 1/6)`.

They obey exactly the same normalization and mean constraint but are inequivalent.

Therefore the extremal rule does not select a unique microscopic distribution until the reference measure is itself physically selected.

Lane classification:

`SAME_MACRO_CONSTRAINTS_PLUS_MAXRELENT_GIVE_DIFFERENT_WEIGHTS_FOR_DIFFERENT_PRIORS`.

## Lane C — relational invariance audit

A naive differential entropy depends on parametrization. Relative entropy repairs this only after a reference measure is specified with the correct transformation law.

Relational/gauge invariance can constrain how the measure transforms and can require quotient/Faddeev-Popov/group-averaged structures, but invariance alone does not normally choose one unique positive gauge-invariant weight on the physical configuration/history space.

If `m` is admissible, then in a broad class

`m'(q) = F[I_1(q), I_2(q), ...] m(q)`

with positive invariant `F` is also covariant/invariant unless another principle fixes `F`.

This is the measure analogue of the homogeneous invariant sector found in SF003/SF004.

Lane classification:

`RELATIONAL_INVARIANCE_CONSTRAINS_MEASURE_TRANSFORMATION_BUT_DOES_NOT_FIX_INVARIANT_WEIGHT_FUNCTION`.

## Lane D — physical information-content audit

To use EIS ontically, one must decide:

- which entropy/information functional is physically fundamental;
- relative to which reference measure;
- which microscopic constraints are exact;
- why those constraints, and not a larger/smaller set, define the physical ensemble/history weights.

Those choices carry microscopic information. In particular, choosing the reference measure can be equivalent to choosing a density of states or microscopic counting rule—the very object SF006 localized as missing.

Therefore EIS does not eliminate the need for a microscopic principle; it **repackages it as the choice of measure/counting rule/information geometry**.

Lane classification:

`INFORMATION_EXTREMIZATION_RELOCATES_MISSING_PHYSICS_TO_MEASURE_FUNCTIONAL_AND_CONSTRAINT_CHOICE`.

## Terminal decision

The preregistered failure criterion is satisfied:

`EIS_INSUFFICIENT_REFERENCE_MEASURE_OR_FUNCTIONAL_FREEDOM_SURVIVES`.

## Important qualification

Maximum entropy remains a rigorous inference principle once the reference measure and constraints represent justified information. SF011 rejects only the stronger ontic claim that “maximize entropy” by itself determines the microscopic gravitational law.

A deeper microscopic counting principle could provide a canonical measure and thereby make an information extremum predictive. Such a counting principle would be additional physics and should be tested directly rather than hidden inside the entropy prescription.

## New structural finding

The same residual microscopic information again appears in a fourth representation:

- action language: homogeneous invariant coefficients;
- RG/spectral language: relevant trajectory / spectral data;
- amplitude language: primitive/contact/boundary data;
- information language: reference measure / state-counting weight.

This repeated equivalence strongly suggests that the project is not encountering unrelated technical gaps. It is encountering one conserved **information deficit** under changes of formalism.

## Exact next admissible step

Instead of testing additional generic consistency/extremization principles one-by-one, the programme should now formulate an **information-deficit theorem**: define the residual microscopic datum abstractly and prove that the currently tested transformations of representation merely move, rather than remove, that datum.

Only after that theorem is frozen should a genuinely new microscopic counting/representation principle be proposed.

`chi_ABC` remains embargoed.
