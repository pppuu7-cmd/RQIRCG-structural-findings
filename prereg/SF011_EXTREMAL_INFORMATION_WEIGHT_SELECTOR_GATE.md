# SF011 — extremal / information dynamical-weight selector — PREREGISTRATION

Date: 2026-09-14
Status: **FROZEN PRE-OUTCOME NEW-PRINCIPLE GATE**

## Candidate principle class — EIS

Call the principle **EIS** (`Extremal Information Selection`).

The candidate principle is:

> Given the physically admissible relational histories/states and the frozen macroscopic constraints, the microscopic weight/measure is selected uniquely by extremizing a physically defined information functional (for example relative entropy, entropy production, information action, or equivalent variational information quantity).

No specific entropy functional or prior measure is imported in the principle statement.

`chi_ABC` remains embargoed.

## Scientific question

Can an extremal/information rule uniquely fix microscopic dynamical weights without hiding the missing physics in the choice of entropy, reference measure, coordinates or constraint set?

## Positive criterion

EIS passes only if the information functional and its reference measure/metric are independently fixed by the inherited relational/closed architecture, and the extremum uniquely determines the nonlinear microscopic weights after the inherited calibrations.

Positive verdict:

`EIS_SELECTS_DYNAMICAL_WEIGHT_SCOPED`.

## Counterexample-first failure criteria

Return

`EIS_INSUFFICIENT_REFERENCE_MEASURE_OR_FUNCTIONAL_FREEDOM_SURVIVES`

if:

1. maximum entropy gives different selected distributions for different admissible reference measures while satisfying the same frozen constraints;
2. coordinate/reparameterization choices change a naive differential-entropy extremum;
3. different convex information functionals select different microscopic weights from the same admissible set;
4. the required prior/reference measure is itself equivalent in information content to the missing microscopic law.

## Frozen minimal mathematical control

For a positive variable `x` with only normalization and mean fixed, compare maximum *relative* entropy with respect to two positive reference measures `m_A(x)` and `m_B(x)`.

The generic solution has exponential-family form

`p_m(x) ∝ m(x) exp(-lambda x)`.

Thus unless the reference measure `m(x)` is independently fixed, the selected distribution is not unique even though the variational problem is strictly convex for each fixed `m`.

The evaluation must verify this logic exactly and then ask whether the relational/gravitational architecture supplies a canonical `m`.

## Mandatory lanes

### Lane A — variational uniqueness conditional on prior
Establish whether the optimization is unique once a reference measure and constraints are fixed.

### Lane B — prior/measure dependence
Show whether different admissible priors/reference measures give inequivalent microscopic weights under identical macroscopic constraints.

### Lane C — relational invariance audit
Determine whether coordinate/gauge/relational invariance fixes the reference measure or only constrains its transformation law.

### Lane D — physical information-content audit
Determine whether choosing the information functional/prior constitutes new microscopic physics rather than a consequence of RQIRCG.

## Non-tautology rule

A unique answer after arbitrarily choosing a prior or entropy functional is not a physical selection result. The selector must determine the prior/functional from an independently motivated principle.

## Claim ceiling

SF011 does not reject maximum-entropy inference as an epistemic tool. It tests whether such an extremal rule can serve as an ontic nonlinear-gravity selector without additional microscopic input.
