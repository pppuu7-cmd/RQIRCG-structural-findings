# SF019 — closed-system microscopic reversibility audit — TERMINAL

Date: 2026-09-14
Status: **TERMINAL / HKT assumption accounting corrected / no `chi_ABC` evaluation**

Preregistration: `5b7e38c72e2234402f31fa44bbd7393fd6efcffe`.

## Outcome lock

`chi_ABC` remained embargoed. SF019 tests only whether the reversibility ingredient used in the SF018/HKT discussion is independent physical input.

## Executive classification

Two statements that must not be conflated are simultaneously true:

`CLOSED_UNITARITY_DOES_NOT_ENTAIL_TIME_REVERSAL_SYMMETRY`

and

`HKT_REVERSIBILITY_IS_REDUNDANT_WITHIN_THE_STRONG_GEOMETRODYNAMICAL_POSTULATE_PACKAGE_SCOPED`.

Thus the reversibility caveat in SF018 should be **downgraded as an independent blocker**, but not because fundamental closure implies microscopic T symmetry.

## Lane A — HKT semantic / redundancy audit

The original Hojman-Kuchar-Teitelboim reconstruction is often summarized as a uniqueness theorem for the time-reversible canonical representation of hypersurface deformations on the spatial-metric phase space.

However a later detailed reconstruction analysis by Kouletsis explicitly reports that the HKT authors themselves pointed out redundancy in their postulate set, including the **reversibility postulate**. Kouletsis states that HKT did not reduce their assumptions to a minimum and that reversibility, as well as one of the closure relations, was redundant once the other strong geometrodynamical requirements were imposed.

Reference:

- I. Kouletsis, *A classical history theory: Geometrodynamics and general field dynamics regained*, arXiv:`gr-qc/9801019`.

Therefore it is scientifically incorrect to treat the word “time-reversible” in the compact HKT theorem statement as automatically proving that an **independent microscopic T-symmetry axiom** must be added to RHPI.

The correct object to audit is the full strong geometrodynamical representation: choice/meaning of canonical variables, reshuffling/normal deformation properties, strong representation/embedding structure and path independence.

Lane classification:

`HKT_REVERSIBILITY_NOT_AN_INDEPENDENT_POSTULATE_AFTER_STRONG_GEOMETRODYNAMICAL_STRUCTURE_IS_IMPOSED_SCOPED`.

## Lane B — closed quantum evolution does not imply T symmetry

For any self-adjoint Hamiltonian `H`,

`U(t) = exp(-i H t)`

is unitary and invertible, with

`U(t)^-1 = U(-t)`.

This algebraic invertibility is not the same as time-reversal symmetry of the law. Time-reversal invariance requires an appropriate antiunitary operation `Theta` relating the dynamics under reversal; schematically one needs the Hamiltonian and any T-odd external/internal parameters to transform so that the reversed process obeys the same physical law.

A decisive physical counterexample is the direct observation of T violation in the neutral B-meson system by BABAR:

- J. P. Lees et al. (BABAR), *Observation of Time-Reversal Violation in the B0 Meson System*, Phys. Rev. Lett. 109, 211801 (2012).

The system is described within ordinary quantum mechanics with normalized unitary microscopic evolution, yet transition probabilities of T-conjugate processes differ.

Therefore neither normalization, reversibility of the evolution map as an inverse, nor closed-system bookkeeping logically entails microscopic T invariance.

Lane classification:

`UNITARY_INVERTIBLE_EVOLUTION_IS_STRICTLY_WEAKER_THAN_TIME_REVERSAL_SYMMETRY`.

## Lane C — frozen RQIR/RQIRCG authority audit

The frozen RQIR consistency framework requires, where applicable:

- normalized/positive/unitary quantum evolution;
- causal/no-signalling structure;
- retarded support for response functions;
- conservation/gauge consistency;
- correct limits.

Its Foundations explicitly distinguishes the symmetrized/noise kernel from the commutator/retarded response and uses a causal `theta(x0-y0)` retarded susceptibility. These requirements do not state a microscopic T-symmetry axiom.

Likewise the RQIR Candidate Gravity contract demands unitarity/positivity and causal support, not fundamental time-reversal invariance.

Hence no independent HKT-T axiom can honestly be claimed to have been inherited from frozen RQIR.

But, by Lane A, none is needed merely because the compact HKT theorem is often phrased with “time-reversible”: in the strong HKT package the reversibility postulate was recognized as redundant.

Lane classification:

`FROZEN_RQIR_DOES_NOT_IMPOSE_MICROSCOPIC_T_SYMMETRY_AND_NEED_NOT_BE_RETROFITTED_TO_DO_SO`.

## Lane D — selector consequence

SF018 should therefore be refined as follows.

Incorrect interpretation:

`RHPI + separately postulated microscopic T symmetry -> ADM`.

Better scoped interpretation:

`strong embeddable metric geometrodynamics / strong HDA representation + correct geometric action on the metric phase space -> HKT ADM class`,

with the historical reversibility postulate not counted as an independent new information bit in that strong package.

This **strengthens** RHPI as a prospective physical selector because one apparent extra axiom is removed from the information budget.

The remaining caution is different and more important:

- weak/on-constraint path independence is nonunique;
- the strong representation/geometric metric-action conditions carry real selector information;
- regularity/locality scope still has to be stated honestly;
- pure HKT geometrodynamics still does not determine the general matter/source Hamiltonian.

Lane classification:

`RHPI_PURE_GRAVITY_SELECTOR_STRENGTHENED_BY_REMOVAL_OF_INDEPENDENT_REVERSIBILITY_BLOCKER`.

## Terminal decision

Record both results:

`NEGATIVE_GENERAL: CLOSED_UNITARITY_DOES_NOT_ENTAIL_TIME_REVERSAL_SYMMETRY`

`POSITIVE_HKT_SCOPED: HKT_REVERSIBILITY_IS_REDUNDANT_WITHIN_STRONG_GEOMETRODYNAMICAL_SELECTION_PACKAGE`.

## New structural finding

The RHPI programme does **not** need to spend an additional microscopic axiom on time-reversal symmetry merely to recover the HKT pure-gravity uniqueness result.

This makes the information accounting cleaner:

- the selector content lives primarily in **complete metric phase space + strong spacetime embeddability/hypersurface-deformation representation**;
- generic quantum closure supplies invertibility/unitarity but is not the source of the HKT uniqueness;
- retarded laboratory boundary conditions may break solution-level time symmetry without altering the local geometrodynamical law.

## Updated frontier

The dominant unresolved gate is now SF020: whether applying hypersurface path independence to the **total closed gravity+matter system**, with flat-space matter independently frozen, selects the source coupling or leaves generally covariant nonminimal coupling freedom.

`chi_ABC` remains embargoed.
