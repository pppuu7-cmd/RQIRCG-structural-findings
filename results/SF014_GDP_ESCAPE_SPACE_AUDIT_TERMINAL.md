# SF014 — GDP escape-space audit — TERMINAL

Date: 2026-09-14
Status: **TERMINAL / decisive auxiliary-geometry escape found / no `chi_ABC` evaluation**

Preregistration: `143c2acbf0fd8811746f1eae49d964f98b078650`.

## Outcome lock

`chi_ABC` remained embargoed. SF014 tests the scope of GDP, not connected outcomes.

## Lane A — finite-jet pure-metric remainder

SF013 already established:

- strong positive selection in the local metric-only class whose Lagrangian depends at most on second derivatives of the metric;
- no theorem-level closure yet for arbitrary finite derivative order.

The present audit found no theorem sufficient to upgrade that broader finite-jet branch to a global uniqueness statement. This lane therefore remains:

`BLOCKED_ARBITRARY_FINITE_JET_PURE_METRIC_UNIQUENESS_NOT_PROVEN`.

This blocked lane is not needed for the aggregate decision because Lane B supplies a decisive escape once the metric-only representation restriction is relaxed.

## Lane B — metric-affine / auxiliary-geometry counterexample

A broad Ricci-based metric-affine class has action schematically

`S[g,Gamma] = Integral sqrt(-g) F(g^{-1}, R_(mu nu)(Gamma)) + S_m[g,Psi]`,

with metric and affine connection varied independently.

For the projectively invariant subclass depending on the **symmetric** Ricci tensor, the connection does not unleash the extra projective ghost sector associated with the antisymmetric Ricci tensor. The literature explicitly emphasizes that this symmetric/projectively invariant family has no additional gravitational propagating degrees of freedom, while breaking projective symmetry generically activates pathological connection modes.

Representative references:

- J. Beltran Jimenez, A. Delhom, *Ghosts in metric-affine higher order curvature gravity*, arXiv:`1901.08988` / Eur. Phys. J. C 79 (2019) 656;
- V. Vitagliano, T. P. Sotiriou, S. Liberati, *The dynamics of metric-affine gravity*, arXiv:`1008.0171`.

The second work also makes the crucial structural point: in a broad low-order metric-affine class the independent connection can be non-dynamical/auxiliary and eliminated algebraically, producing interactions different from GR; special `f(R)`-type classes illustrate this auxiliary behavior.

Ricci-based gravity analyses further show that projectively invariant RBGs can be written using an auxiliary metric `q_mu nu` so that the gravitational equations take an Einstein-frame form while nonlinear modifications are transferred into the relation with matter/source variables. Thus the same two tensorial gravitational propagating DOF can coexist with a continuous nonlinear functional freedom `F` affecting the physical source/geometry interface.

This satisfies the decisive SF014 logic at the level relevant to RQIRCG:

- no extra propagating gravitational connection mode on the protected/projective branch;
- full spacetime covariance;
- ordinary massless-spin-2/GR behavior in the appropriate weak/vacuum regime;
- continuous nonlinear functional/coupling freedom;
- modified nonlinear matter/source response.

The connection is not a hidden propagating DOF; it is auxiliary in the relevant branch. Therefore counting physical propagating DOF alone cannot exclude the family.

Lane classification:

`TWO_PROPAGATING_DOF_DO_NOT_FIX_AUXILIARY_GEOMETRY_OR_SOURCE_MAP`.

## Lane C — nonlocal no-new-pole branch

Ghost-free/nonlocal gravity constructions can be engineered so that the linearized propagator contains no additional poles when suitable entire form factors are used. However pole counting around a chosen background does not by itself establish exact generic-background GDP or a finite Cauchy-data theorem for the full nonlocal theory.

Therefore SF014 does not use nonlocal gravity as the decisive counterexample.

Classification:

`NONLOCAL_ESCAPE_NOT_NEEDED_AND_GENERIC_GLOBAL_DOF_STATUS_REMAINS_MODEL_DEPENDENT`.

## Lane D — covariance control

There are many “minimally modified” or spatially covariant gravity theories engineered to propagate only two tensor DOF. Their existence confirms that a bare two-DOF requirement is highly nonselective once full spacetime diffeomorphism invariance is relaxed.

A recent example constructs spatially covariant two-DOF theories perturbatively around cosmological backgrounds (arXiv:`2604.14490`). These are useful controls but do not defeat the stronger full-covariance version of GDP because they deliberately relax the relevant symmetry.

Classification:

`TWO_DOF_WITHOUT_FULL_SPACETIME_COVARIANCE_IS_MANIFESTLY_NONUNIQUE_CONTROL`.

## Aggregate decision

The preregistered decisive counterexample logic is satisfied by the auxiliary/projectively invariant metric-affine branch:

`GDP_INSUFFICIENT_BEYOND_METRIC_ONLY_REPRESENTATION_SCOPED`.

## Relation to SF013

SF014 does **not** retract SF013’s positive result.

The correct combined statement is:

1. `GDP + metric-only + full diffeomorphism invariance` has strong selector power and, in the classified second-derivative-Lagrangian scope, selects the Einstein-Hilbert class;
2. `GDP + full diffeomorphism invariance` **without** a metric-only/geometry-ontology rule does not uniquely select the nonlinear interface, because auxiliary geometric variables can change source mapping without adding propagating gravitational DOF.

Thus the metric-only restriction in SF013 was carrying genuine physical information, not merely notation.

## New structural finding

The selector deficit has split into two independent questions:

### Propagating-content selector

`Which local gravitational DOF are physically dynamical?`

GDP can answer this strongly.

### Geometric/source-ontology selector

`Which nonpropagating geometric/auxiliary variables and source map are physically fundamental/admissible?`

GDP does not answer this.

A complete principle must constrain both.

## Exact next admissible principle

The most economical strengthening is not “ban auxiliary fields by convention,” but a prospective **Source-Metric Sufficiency** principle:

> all gravitational influence accessible to matter/apparatus is mediated by the same physical metric/relational geometry whose two propagating tensor DOF constitute the inherited carrier; no independent auxiliary geometric variable may alter the matter-source map after elimination unless its effect is derivable from that metric dynamics alone.

This must be tested separately. It is a new ontology/interface principle, not part of GDP and not yet accepted.

`chi_ABC` remains embargoed.
