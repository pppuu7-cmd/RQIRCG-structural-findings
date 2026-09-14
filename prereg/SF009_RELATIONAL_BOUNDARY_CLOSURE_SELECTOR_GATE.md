# SF009 — relational boundary closure / state-composition selector gate — PREREGISTRATION

Date: 2026-09-14
Status: **FROZEN PRE-OUTCOME NEW-PRINCIPLE GATE**

## Context

SF008 showed that a UV fixed point can reduce microscopic freedom to finitely many relevant trajectory coordinates without choosing their values. SF009 tests whether a stronger **closed relational boundary/state principle** can fix those coordinates.

`chi_ABC` remains embargoed.

## Candidate principle class — RBC

Call the principle **RBC** (`Relational Boundary Closure`).

The strongest non-tautological version admitted in this gate is:

1. the physical realization is closed: no external classical source, reference frame, clock, environment, or prescribed physical boundary datum is fundamental;
2. amplitudes/states assigned to composable regions/subsystems obey an exact gluing/composition law over shared *physical relational* boundary data;
3. gauge/reference redundancy is quotiented or constrained consistently under gluing;
4. a closed history/region is obtained by internal identification/trace/group averaging rather than by supplying an external boundary wavefunction;
5. the same microscopic rule supplies both the dynamical amplitudes and the relational state composition.

RBC may not simply assert “there is one unique state/measure.” Uniqueness has to follow from clauses 1–5; otherwise the desired selector has been inserted by definition.

## Scientific question

Does exact relational gluing plus absence of external physical boundary data determine the microscopic generator/measure/trajectory coordinates uniquely?

## Positive criterion

Return

`RBC_SELECTS_MICROSCOPIC_GENERATING_DATA_SCOPED`

only if clauses 1–5 force a unique microscopic amplitude/generator/measure in the physical quotient after inherited weak-field normalization.

## Counterexample-first failure criterion

RBC fails if there exists a continuous family of inequivalent microscopic generators `Gamma_alpha` such that:

1. every member has the same relational boundary/state space and the same exact gluing law;
2. every member defines closed amplitudes without external physical boundary data;
3. all inherited lower-order weak-field data can be held fixed;
4. `alpha` changes higher-order nonlinear dynamics or spectral/matching data;
5. no RBC clause fixes `alpha`.

Failure verdict:

`RBC_INSUFFICIENT_DYNAMICAL_WEIGHT_FREEDOM_SURVIVES`.

## Frozen mathematical control

For any self-adjoint generator `H_alpha`, the unitary propagator

`U_alpha(t) = exp(-i H_alpha t)`

obeys exact composition

`U_alpha(t2+t1) = U_alpha(t2) U_alpha(t1)`.

Closing the time boundary by a trace gives

`Z_alpha(T) = Tr U_alpha(T)`.

The composition/closure law alone therefore does not distinguish different `H_alpha`. SF009 must determine whether the *relational/gauge* strengthening removes this generic freedom or whether the same phenomenon survives for candidate gravitational generators.

A valid gravity-facing counterexample may reuse only already-frozen structural facts such as SF003/SF004’s existence of separately invariant higher-order functionals; it may not choose `alpha` from `chi_ABC`.

## Mandatory lanes

### Lane A — composition algebra
Determine what exact gluing fixes mathematically: normalization/associativity/constraint matching versus the local dynamical generator.

### Lane B — no-external-boundary audit
Determine whether tracing/group-averaging over boundary data removes generator parameters or only removes external state preparation.

### Lane C — gravity-facing deformation witness
Test whether `Gamma_alpha = Gamma_0 + alpha I_homogeneous` can preserve the same relational/gauge gluing structure and lower-order calibration.

### Lane D — information-content audit
Identify what extra datum would still be needed if RBC leaves `alpha` free: local amplitude weight, measure, boundary proposal, microscopic Hamiltonian constraint, or equivalent.

## Strict interpretation rule

“Background independent,” “closed,” “relational,” “sum over histories,” and “satisfies gluing” are not selector labels by themselves. The gate asks whether they mathematically determine the *weights* assigned to histories/states.

## Claim ceiling

SF009 does not judge any specific no-boundary, spin-foam, causal-set, tensor-network, group-field, or canonical quantum-gravity proposal. It tests the information content of the generic relational-boundary-closure principle class.

## Next-step rule

If RBC fails, the next admissible principle must act on the **dynamical weights themselves** rather than only on how amplitudes compose. Candidate examples would include an extremal/information principle or an exact bootstrap/completeness condition, each prospectively defined and tested for nonuniqueness before `chi_ABC` is opened.
