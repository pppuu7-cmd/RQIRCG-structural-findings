# SF004 — closed-system composition + universal source coupling selector gate — TERMINAL

Date: 2026-09-14
Status: **TERMINAL / PRE-OUTCOME**

## Outcome lock

`chi_ABC` was not evaluated, estimated, or used for model selection in SF004.

Preregistration: `ea5e4f9432480b297bf438dfa08984bd335a0b5f`.

## Frozen candidate principle

SF004 tested **CUC** (`Closed Universal Composition`):

1. one closed generator for carrier + matter + apparatus/support;
2. one inherited weak-field coupling normalization for all sectors;
3. total source derived from that same generator, including carrier self-contribution;
4. physical independence of regrouping `(A ⊕ B) ⊕ C ~ A ⊕ (B ⊕ C)`.

No derivative-order restriction or no-new-mode axiom was permitted.

## Lane A — recursive source audit

Universal self-coupling has genuine constructive power. If the carrier couples to energy-momentum, consistency requires including the carrier contribution in the source, and iteration generates nonlinear interaction terms. This is the familiar structural content of spin-2 bootstrap/self-coupling arguments.

However the recursion fixes only the **particular solution forced by the coupling/source identity**. It does not eliminate a homogeneous sector consisting of additional functionals that already satisfy the same nonlinear invariance/source identity on their own.

Schematically, if

`Gamma_0[g,Psi]`

satisfies the universal source identity, and a pure-carrier functional `I[g]` is separately invariant under the same nonlinear gauge symmetry, then

`Gamma_alpha[g,Psi] = Gamma_0[g,Psi] + alpha I[g]`

also has a source/equation obtained from one generator. Matter and apparatus still couple through the same `g`; the new coefficient `alpha` belongs to the carrier constitutive sector and is not a species-dependent gravitational charge.

Thus “gravity also gravitates” does not by itself imply “there is only one invariant gravitational functional.”

This distinction is also visible in the universal-coupling literature: the massless universal-coupling construction removes the flat background from the physical field equations and leads to a generally covariant action, but higher-derivative generally covariant terms are not excluded merely by universal coupling. See J. B. Pitts, arXiv:1611.02673 and related universal-coupling analyses; Deser’s self-coupling construction establishes the lowest-derivative recursive completion but does not constitute a theorem excluding separately invariant higher-derivative homogeneous additions.

Lane classification:

`UNIVERSAL_RECURSION_FIXES_FORCED_PART_NOT_HOMOGENEOUS_INVARIANTS`.

## Lane B — associative composition audit

Let the closed generator have the form

`Gamma[g,{Psi_i}] = I_g[g] + Sum_i Gamma_i[g,Psi_i]`.

Regrouping the same physical sectors changes only parentheses in the matter/apparatus partition. The total set `{Psi_i}`, the common carrier `g`, and the pure-carrier term `I_g[g]` are unchanged. Therefore

`((A ⊕ B) ⊕ C)`

and

`(A ⊕ (B ⊕ C))`

produce the same total generator whenever the composition operation is ordinary closed union/addition with shared carrier constraints.

Now replace

`I_g[g] -> I_g[g] + alpha I_3[g]`

for a separately invariant pure-carrier functional `I_3`. It appears once in the total closed generator independently of how the non-carrier sectors are grouped. Hence associativity does not constrain `alpha`.

Associativity would select coefficients only if an additional law related intrinsic carrier invariants to subsystem counting/grouping. CUC contains no such law.

Lane classification:

`ASSOCIATIVE_REGROUPING_BLIND_TO_INTRINSIC_CARRIER_INVARIANT_COEFFICIENTS`.

## Lane C — explicit inequivalent deformation witness

The old RQIRCG G90 gate already supplies a programme-internal witness. It constructed a prospectively frozen local generally covariant curvature-cubic family with two pointwise-independent invariant directions, both vanishing through second perturbative order while giving nonzero cubic terms. Its terminal result was

`BLOCKED_C_EXPLICIT_COVARIANT_CUBIC_INVARIANT_FAMILY_PRESERVES_FROZEN_QUADRATIC_DATA_SCOPED`.

Therefore the present project does not need to invent a post-outcome deformation to challenge CUC.

For a sharper physical-equivalence audit, four-dimensional gravitational EFT provides a standard non-evanescent curvature-cubed direction. The Goroff-Sagnotti two-loop counterterm is proportional to a Riemann-cubed invariant and contributes to physical graviton amplitudes. Modern two-loop amplitude analyses continue to identify a non-evanescent `R^3` counterterm. This is sufficient evidence that the entire curvature-cubic sector cannot be dismissed as boundary or local-field-redefinition redundancy.

Representative references:

- M. H. Goroff and A. Sagnotti, *Quantum Gravity at Two Loops*, Phys. Lett. B 160 (1985) 81, DOI `10.1016/0370-2693(85)91470-4`.
- Z. Bern, H.-H. Chi, L. Dixon, A. Edison, *Two-Loop Renormalization of Quantum Gravity Simplified*, arXiv:`1701.02422`.
- programme-internal G90 terminal: `ITER088_G90_C_COVARIANT_CUBIC_LIFT_TERMINAL.md`.

The field-redefinition quotient can remove many Ricci-containing operators, but it does not remove every on-shell curvature-cubic graviton interaction.

Lane classification:

`GENUINE_HOMOGENEOUS_NONLINEAR_DIRECTION_SURVIVES_PHYSICAL_QUOTIENT_SCOPED`.

## Lane D — causality / positivity / health ceiling

A generic higher-curvature coefficient is not automatically a healthy fundamental theory. This does not restore CUC selector power.

Causality analyses of higher-derivative graviton three-point structures show a more specific result: such corrections are constrained, and in weakly coupled gravity a finite higher-derivative correction may require an infinite tower of massive higher-spin states near the corresponding scale to restore causal consistency. The conclusion is therefore not “the coefficient must identically vanish under universal coupling,” but rather that nonzero coefficients carry UV-completion obligations.

Representative reference:

- X. O. Camanho, J. D. Edelstein, J. Maldacena, A. Zhiboedov, *Causality constraints on corrections to the graviton three-point coupling*, JHEP 02 (2016) 020, arXiv:`1407.5597`.

Likewise, Einsteinian cubic gravity provides an explicit demonstration that a nontrivial four-dimensional curvature-cubic interaction can share the usual transverse massless-graviton spectrum on maximally symmetric backgrounds while differing nonlinearly:

- P. Bueno, P. A. Cano, *Einsteinian cubic gravity*, Phys. Rev. D 94, 104005 (2016), arXiv:`1607.06463`.

Neither example is imported as candidate physics. They serve only to defeat the claim that all nonzero homogeneous invariant coefficients are excluded by the already-frozen low-energy health requirements.

Causality/positivity can carve out or UV-condition the coefficient space; CUC still does not determine a unique coefficient from the inherited lower-order calibration.

Lane classification:

`HEALTH_CONDITIONS_CONSTRAIN_BUT_DO_NOT_CUC_FIX_HOMOGENEOUS_COEFFICIENT`.

## Terminal decision

All four preregistered falsification conditions are met by the homogeneous invariant sector.

`CUC_INSUFFICIENT_HOMOGENEOUS_INVARIANT_FREEDOM_SURVIVES`.

CUC is a useful consistency/organization principle, but it is **not** the missing nonlinear selector.

## New structural finding

The nonlinear underdetermination can now be decomposed more sharply into

`Gamma = Gamma_forced + Gamma_homogeneous`.

The inherited weak-field gauge structure, self-source recursion, one-generator closure, universal source coupling, nonlinear gauge closure, and associative subsystem composition strongly constrain `Gamma_forced`.

They do **not** determine the coefficients of every separately invariant term in `Gamma_homogeneous`.

This is a stronger localization than VB1/SF003: the missing information is not simply “how does the field source itself?” It is specifically **what physical law fixes the homogeneous invariant/Wilson-coefficient sector after all consistency-forced recursion has been satisfied?**

## Consequence for the principle search

A successful new principle must do something qualitatively stronger than:

- require a mediator;
- require positivity/CPTP evolution;
- require one closed generator;
- require universal coupling to total energy-momentum;
- require nonlinear gauge/Bianchi closure;
- require associative composition.

All of those can coexist with inequivalent higher-order invariant carrier terms.

The next useful gate should therefore test a principle that acts directly on the homogeneous sector. A natural candidate is **IR factorization + unitarity + causal analyticity / UV-completability**: perhaps S-matrix consistency fixes the otherwise free invariant coefficients. The decisive question must again be counterexample-first: do these conditions determine a number, or only inequalities/scales and matching data?

`chi_ABC` remains embargoed.
