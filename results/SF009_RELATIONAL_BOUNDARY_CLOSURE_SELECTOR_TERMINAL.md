# SF009 — relational boundary closure / state-composition selector gate — TERMINAL

Date: 2026-09-14
Status: **TERMINAL / new-principle class evaluated / no `chi_ABC` evaluation**

Preregistration: `b5e06ca719975aa9b3cdd4115dc53812a68d3b4e`.

## Outcome lock

`chi_ABC` remained embargoed. No connected coefficient or preferred nonlinear outcome was used.

## Lane A — composition algebra

The frozen mathematical control already exposes the central distinction.

For every self-adjoint generator `H_alpha`,

`U_alpha(t) = exp(-i H_alpha t)`

satisfies exactly

`U_alpha(t2+t1) = U_alpha(t2) U_alpha(t1)`.

Thus exact associative composition constrains **how amplitudes propagate/glue**, but it does not determine the generator whose exponential is being composed.

The same statement survives in path-integral language. If a local action/measure defines a kernel `K_alpha(q2,t2;q1,t1)`, gluing over the intermediate physical data yields the longer kernel. Changing an allowed local dynamical term changes the kernel’s weight while preserving the gluing identity.

Therefore composition is an algebraic consistency condition on amplitudes, not by itself a dynamical-weight selector.

Lane classification:

`EXACT_GLuing_COMPOSITION_DOES_NOT_DETERMINE_LOCAL_GENERATOR`.

## Lane B — no-external-boundary audit

Closing the boundary does not remove this freedom.

For the frozen control,

`Z_alpha(T) = Tr U_alpha(T)`

contains no externally supplied initial/final wavefunction, yet it still depends on `H_alpha` and therefore on `alpha`.

Likewise, group averaging or integrating/summing over shared boundary data can remove dependence on an external reference or preparation without selecting the local action/constraint/measure used inside the sum.

Hence

`no external boundary state`

is logically different from

`no dynamical coupling/boundary-condition parameter`.

The first can hold while the second remains false.

Lane classification:

`CLOSING_OR_AVERAGING_BOUNDARY_DATA_DOES_NOT_REMOVE_GENERATOR_PARAMETERS`.

## Lane C — gravity-facing homogeneous deformation witness

SF003 and SF004 already established the needed gravity-facing witness class before SF009: a separately invariant higher-order pure-carrier functional can be added as

`Gamma_alpha = Gamma_0 + alpha I_homogeneous`

while preserving the inherited quadratic carrier, nonlinear gauge closure, one-generator structure, universal matter coupling and associative closed composition.

RBC adds relational boundary gluing/no-external-state requirements. But if both `Gamma_0` and `I_homogeneous` are defined from the same physical carrier variables and obey the same gauge/constraint quotient, the path integral/canonical amplitude built from `Gamma_alpha` uses the same boundary state space and the same gluing operation for every `alpha`.

The local history weight changes:

`weight_alpha[history] ~ exp(i Gamma_alpha[history]/hbar)`,

but the rule for gluing histories over shared relational data does not fix the coefficient multiplying an independently admissible invariant.

Thus the same homogeneous freedom that survived SF004 also survives RBC.

Lane classification:

`RELATIONAL_GLuing_STRUCTURE_IS_COMPATIBLE_WITH_CONTINUOUS_HOMOGENEOUS_DYNAMICAL_WEIGHTS`.

## Lane D — information-content audit

RBC fixes or constrains:

- absence of fundamental external reference systems;
- the physical meaning of boundary data;
- how amplitudes/states compose;
- consistency of gauge/constraint reduction under composition;
- how a closed amplitude is formed from open-region amplitudes.

It does **not** fix:

- the local action/Hamiltonian-constraint coefficients;
- the measure/Jacobian beyond what gauge consistency demands;
- spectral weights;
- relevant RG trajectory coordinates;
- independently invariant higher-order carrier weights.

To turn RBC into a selector one must add a rule that assigns the local amplitude/history weights themselves. Simply naming that rule “unique relational state” would assume the desired conclusion and fails the preregistered non-tautology condition.

Lane classification:

`RBC_LEAVES_LOCAL_WEIGHT_OR_MEASURE_DATA_AS_INDEPENDENT_MICROSCOPIC_INPUT`.

## Terminal decision

The preregistered counterexample criterion is satisfied:

`RBC_INSUFFICIENT_DYNAMICAL_WEIGHT_FREEDOM_SURVIVES`.

## New structural finding

The project can now distinguish three conceptually different layers that are often conflated:

1. **kinematic/relational closure** — what counts as physical state/boundary/reference data;
2. **composition law** — how amplitudes for regions/subsystems glue;
3. **dynamical weight** — which amplitudes/histories are assigned what relative phase/weight.

RQIR strongly constrains layer 1 at the observable level. SF001/SF004/SF009 strongly constrain layers 1–2 in the new branch. The unresolved selector resides in layer 3.

This is sharper than merely saying “a microscopic theory is missing.” What is missing is a **law for dynamical weights** that is not reducible to positivity, covariance, universal coupling, closure, gluing, or UV-manifold membership.

## Consequence for further search

The next candidate principle must act directly on dynamical weights. Two classes are sufficiently sharp to test prospectively:

1. **extremal/information selection** — derive weights by extremizing a physically defined entropy/information/action functional;
2. **exact constructibility/bootstrap selection** — require the full amplitude/weight to be reconstructible from lower-point/causal factorization data with no independent contact ambiguity.

The first risks dependence on a prior/reference measure; the second risks hiding the selector in a “no contact term” assumption. These risks should be the preregistered adversarial tests.

`chi_ABC` remains embargoed.
