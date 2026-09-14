# SF008 — UV fixed-point / self-similarity microscopic-selector gate — TERMINAL

Date: 2026-09-14
Status: **TERMINAL / new-principle class evaluated / no `chi_ABC` evaluation**

Preregistration: `11a807e4981405655c3ad8a9a0bdb7595aed179c`.

## Outcome lock

SF008 evaluates only the information content of a UV fixed-point/self-similarity principle class. It does not adopt any published asymptotic-safety truncation as the RQIRCG theory. `chi_ABC` remained embargoed.

## Lane A — RG geometry

Near a fixed point `u_i*`, linearized RG flow has the standard form

`u_i(t) = u_i* + Sum_I C_I V_Ii exp(-theta_I t)`

up to convention for the sign of `theta_I`.

The fixed-point/UV-completeness condition eliminates directions that would run away from the fixed point in the UV. It therefore fixes the UV-irrelevant coordinates as functions of the surviving critical-surface coordinates.

But the coefficients `C_I` along UV-relevant directions are trajectory data. They label different UV-complete renormalized trajectories sharing the same fixed point.

Thus a finite-dimensional UV critical surface means

`infinite Wilson freedom -> finite relevant-parameter freedom`,

not

`finite relevant-parameter freedom -> unique trajectory`.

This distinction is built into the RG geometry and does not depend on the details of any gravity truncation.

Lane classification:

`FIXED_POINT_CONDITION_REMOVES_IRRELEVANT_FREEDOM_BUT_LEAVES_RELEVANT_TRAJECTORY_COORDINATES`.

## Lane B — inherited-calibration rank

RQIRCG has a calibrated lower-order weak-field carrier/normalization, including the Newtonian coupling scale and pairwise weak-field response. These data can constrain trajectory coordinates that control the corresponding IR normalization.

However the UFP principle contains no theorem that the physical UV critical surface is one-dimensional, nor that every relevant coordinate is a function of the inherited Newton normalization.

The information-counting condition preregistered in SF008 is

`d_rel - R_cal = 0`.

UFP alone establishes at most that `d_rel` is finite under the asymptotic-safety hypothesis. It does not establish the equality above. If `d_rel > R_cal`, a family of UV-complete trajectories remains with identical inherited lower-order calibration but different higher-order couplings.

Therefore the inherited weak-field normalization is insufficient to turn the fixed-point condition into a unique microscopic selector unless an additional relation among relevant coordinates is supplied.

Lane classification:

`INHERITED_LOW_ORDER_NORMALIZATION_DOES_NOT_UFP_FIX_ALL_RELEVANT_COORDINATES`.

## Lane C — asymptotic-safety literature sanity check

The external literature confirms that the distinction above is not merely formal.

A review of asymptotically safe gravity explains that the UV-critical hypersurface is finite-dimensional and that its trajectory coefficients along relevant directions are a priori free parameters to be fixed by observation. In a representative `f(R)` truncation it reports three relevant directions plus one irrelevant direction, yielding a relation for the higher coupling rather than a unique trajectory.

Representative reference:

- G. Gubitosi, C. Ripken, F. Saueressig, *Scales and Hierarchies in Asymptotically Safe Quantum Gravity: A Review*, Found. Phys. 49 (2019) 972–990, DOI `10.1007/s10701-019-00263-1`.

A higher-curvature study including Riemann-tensor interactions reports a four-dimensional UV critical surface in its approximation:

- Y. Kluth, D. F. Litim, *Fixed Points of Quantum Gravity and the Dimensionality of the UV Critical Surface*, arXiv:`2008.09181`.

Earlier work explicitly frames finite relevant dimensionality as a finite number of free parameters rather than zero free parameters:

- D. Benedetti, *On the number of relevant operators in asymptotically safe gravity*, arXiv:`1301.4422`.

These are external comparators only. Their truncation-dependent numbers are not imported as RQIRCG predictions. Their role is to demonstrate that the fixed-point principle is perfectly compatible with `d_rel > 0` and hence does not logically imply uniqueness.

Lane classification:

`KNOWN_FIXED_POINT_GRAVITY_REALIZATIONS_HAVE_NONZERO_RELEVANT_CRITICAL_SURFACES_SCOPED`.

## Lane D — nonlinear consequence

Different relevant trajectory coordinates generally feed into different IR values of higher-order operators after the RG flow is integrated from the UV to the laboratory regime.

Thus two trajectories may share:

- the same UV fixed point;
- the same massless weak-field carrier;
- the same calibrated Newton normalization;
- all RQIR consistency gates;

while differing in higher-order/homogeneous nonlinear coefficients if at least one additional relevant coordinate remains.

The fixed-point principle therefore transforms arbitrary Wilson coefficients into correlated matching data, but it does not by itself choose a unique value for those data.

Lane classification:

`UFP_CORRELATES_HIGHER_COUPLINGS_WITH_RELEVANT_DATA_BUT_DOES_NOT_SELECT_RELEVANT_DATA`.

## Terminal decision

The preregistered failure criterion is satisfied at the level of principle information content:

`UFP_INSUFFICIENT_RELEVANT_TRAJECTORY_FREEDOM_SURVIVES`.

## Important qualification

This is **not** a rejection of asymptotic safety or of fixed-point UV completion.

A stronger compound principle could still select uniquely if, for example, it independently established:

- a unique physical fixed point/universality class;
- a zero-dimensional physical critical surface; or
- enough boundary/state conditions to fix every relevant coordinate after the inherited low-energy calibration.

Those would be additional microscopic principles, not consequences of “UV fixed point exists” alone.

## New structural finding

SF006 localized the missing information to microscopic spectral/generating data. SF008 shows that even a powerful UV self-similarity principle may reduce this to a **finite trajectory-coordinate problem** without eliminating it.

The selector hierarchy is now:

`generic EFT` -> infinitely many Wilson data,

`IR consistency/dispersion` -> bounded/correlated Wilson region,

`UV fixed-point principle` -> finite-dimensional critical-surface data,

`unique theory` -> still requires a rule selecting the trajectory coordinates.

## Exact next admissible gate

Test a principle class that can fix **trajectory/boundary data**, rather than only the RG manifold on which those data live.

A natural next class is a microscopic boundary/state principle: require the physical state/measure to be uniquely determined by relational composition plus a no-external-background/no-external-boundary rule. The gate must first make such a rule mathematically precise enough to admit counterexamples; vague appeals to “background independence” or “simplicity” are not admissible selectors.

`chi_ABC` remains embargoed.
