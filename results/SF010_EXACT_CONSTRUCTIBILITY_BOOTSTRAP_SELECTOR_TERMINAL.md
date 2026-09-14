# SF010 — exact constructibility / bootstrap dynamical-weight selector — TERMINAL

Date: 2026-09-14
Status: **TERMINAL / new-principle class evaluated / no `chi_ABC` evaluation**

Preregistration: `0eb89e78e44f81f43c1582ba1c67d7a0c0a9f8c2`.

## Outcome lock

No connected observable or preferred coefficient was inspected. SF010 asks only whether exact on-shell constructibility supplies enough information to fix dynamical weights.

## Lane A — primitive seed audit

The inherited two-derivative massless spin-2 amplitude is not the only Lorentz/little-group-compatible graviton three-point structure once higher derivatives are admitted.

A direct external witness is the curvature-cubed deformation. Dunbar, Godwin, Jehu and Perkins explicitly extend the gravity S-matrix by adding a minimal higher-derivative three-point amplitude, equivalently an `R^3` interaction, and then study its loop consequences with unitarity methods:

- D. C. Dunbar, J. H. Godwin, G. R. Jehu, W. B. Perkins, *Loop Amplitudes in an Extended Gravity Theory*, arXiv:`1711.05526`.

Therefore the primitive on-shell seed data already contain a homogeneous direction not fixed by the Einstein/Newton normalization.

Factorization can propagate a chosen value of that seed coefficient into higher-point residues, but it cannot derive the seed coefficient from lower-point Einstein data because the new structure first appears as independent primitive data.

Lane classification:

`HIGHER_DERIVATIVE_GRAVITON_THREE_POINT_SEED_FREEDOM_SURVIVES`.

## Lane B — factorization / contact audit

Pole factorization determines residues on physical poles from lower-point amplitudes. A polynomial contact contribution has no factorization pole and is therefore a homogeneous solution of the factorization constraints unless additional soft/asymptotic information fixes it.

This is the on-shell counterpart of the SF003/SF004 decomposition

`Gamma = Gamma_forced + Gamma_homogeneous`.

At amplitude level:

`A = A_factorization-forced + A_contact/homogeneous`.

Even if a particular recursion reconstructs the pole part exactly, ordinary unitarity/factorization does not by itself determine all polynomial data.

The `R^3` witness makes the ambiguity stronger than a pure high-point contact term: it can enter as new three-point seed data and then generate consistent factorizing higher-point amplitudes.

Lane classification:

`FACTORIZATION_FIXES_RESIDUES_NOT_ALL_HOMOGENEOUS_AMPLITUDE_DATA`.

## Lane C — recursion-at-infinity audit

Standard on-shell recursion closes without an unknown boundary contribution only when the shifted amplitude has sufficiently good complex-momentum behavior or when additional soft subtractions compensate the large-parameter growth.

For EFTs and higher-derivative gravity, this behavior is not automatic. Soft-recursion literature develops modified shifts precisely to handle interactions that fail conventional BCFW falloff.

Representative references:

- C. Cheung, K. Kampf, J. Novotny, C.-H. Shen, J. Trnka, *On-Shell Recursion Relations for Effective Field Theories*, arXiv:`1509.03309`;
- R. Carballo-Rubio, F. Di Filippo, N. Moynihan, *Taming higher-derivative interactions and bootstrapping gravity with soft theorems*, arXiv:`1811.08192`.

Thus “constructible” is not equivalent to “contains only the inherited two-derivative interaction.” More general higher-derivative theories can also be constructible after the appropriate recursion data/soft behavior are supplied.

If one instead postulates the particular large-complex-momentum falloff that excludes every higher-derivative seed/contact term, that falloff carries exactly the missing selection information. Without an independent physical derivation it is a reparameterized minimality/no-higher-derivative axiom, which SF002 already showed is not inherited from RQIRCG.

Lane classification:

`EXACT_RECURSION_REQUIRES_EXTRA_ASYMPTOTIC_INPUT_AND_DOES_NOT_UNIQUELY_SELECT_LOW_DERIVATIVE_SEED`.

## Lane D — EFT/bootstrap sanity check

The higher-derivative bootstrap literature demonstrates both sides of the distinction:

1. enhanced soft behavior can make EFT amplitudes recursively constructible;
2. higher-derivative gravitational interactions can be included in soft/complex-shift recursion frameworks;
3. the primitive couplings/low-point amplitudes defining those theories remain theory data.

Therefore constructibility is a powerful **propagation/completion rule** once sufficient primitive data are declared, but it is not generically a **primitive-data selector**.

This mirrors SF009: a composition/recursion law specifies how local pieces determine larger objects, but not necessarily the weights of the primitive pieces.

Lane classification:

`BOOTSTRAP_PROPAGATES_PRIMITIVE_DATA_BUT_DOES_NOT_GENERICALLY_SELECT_THEM`.

## Terminal decision

The preregistered failure condition is satisfied:

`ECB_INSUFFICIENT_PRIMITIVE_SEED_OR_BOUNDARY_TERM_FREEDOM_SURVIVES`.

## Important qualification

This does not say that no special amplitude bootstrap can ever be unique. A stronger theory-specific bootstrap can succeed when enough independently justified assumptions fix:

- the complete three-point seed set;
- asymptotic/Regge behavior;
- spectrum;
- crossing/unitarity/analyticity;
- and any subtraction/contact data.

But that enlarged package contains microscopic information beyond generic constructibility itself. The question then moves to why Nature selects precisely that package.

## New structural finding

The missing information can now be identified on-shell as **primitive amplitude data / recursion-boundary data**.

This is equivalent in information content to the off-shell homogeneous-action/Wilson sector identified by SF003-SF006.

The same obstruction therefore appears in three representations:

- off-shell: homogeneous invariant functional coefficients;
- RG/dispersive: relevant trajectory / spectral matching data;
- on-shell: primitive higher-derivative seed / contact / recursion-boundary data.

These are not three unrelated failures. They are three coordinate systems for the same unresolved microscopic information.

`chi_ABC` remains embargoed.
