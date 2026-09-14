# SF008 — UV fixed-point / self-similarity microscopic-selector gate — PREREGISTRATION

Date: 2026-09-14
Status: **FROZEN PRE-OUTCOME NEW-PRINCIPLE GATE**

## Why this is now admissible

SF007 established that frozen RQIR does not itself select microscopic generating data. SF008 therefore deliberately tests a **new physical principle class outside RQIR Core v1.0** rather than pretending it was already implicit in the old reconstruction.

`chi_ABC` remains embargoed.

## Candidate principle class — UFP

Call the class **UFP** (`UV Fixed Point`).

The proposed microscopic principle is:

> The gravitational microscopic theory lies on a UV-complete self-similar/fixed-point trajectory. Its low-energy nonlinear couplings are not arbitrary independent coefficients; they are coordinates on the UV critical surface and are determined by the fixed point plus the finite set of relevant trajectory data.

This is a principle class, not an import of any particular asymptotic-safety truncation or published numerical fixed point.

## Scientific question

Does UV fixed-point/self-similar completion, together with the already inherited weak-field normalization and low-energy limits, uniquely select the microscopic generating data needed to fix the homogeneous nonlinear sector?

## Formal information-content test

Let the microscopic theory space near a UV fixed point have coordinates decomposed into

- irrelevant directions `u_i`, fixed by UV regularity/self-similarity once the relevant trajectory is chosen;
- relevant/marginally relevant directions `r_a`, which parameterize the UV critical surface/renormalized trajectories.

Let `d_rel` be the number of physically inequivalent relevant coordinates after quotienting redundancies.

UFP is a complete selector only if the inherited RQIRCG calibrations plus the fixed-point condition determine all `r_a` uniquely.

Equivalently, if `N_cal` independent inherited calibrations constrain the relevant coordinates with rank `R_cal`, selection requires

`d_rel - R_cal = 0`

in the physical quotient.

## Positive criterion

Return

`UFP_SELECTS_MICROSCOPIC_TRAJECTORY_SCOPED`

only if there is a justified argument that:

1. a unique relevant fixed-point class is selected;
2. all relevant trajectory coordinates are fixed by already inherited calibrations or by the UFP principle itself;
3. no continuous microscopic matching freedom survives into nonlinear Wilson coefficients.

## Counterexample-first failure criterion

Return

`UFP_INSUFFICIENT_RELEVANT_TRAJECTORY_FREEDOM_SURVIVES`

if any of the following is established:

1. more than one relevant physical direction survives after the inherited weak-field normalization;
2. a fixed point exists but admits a nonzero-dimensional family of UV-complete trajectories with different nonlinear low-energy coefficients;
3. multiple admissible fixed points/universality classes survive without an independent selector;
4. the principle determines scaling exponents/relations but not the trajectory coordinates needed for a unique IR action.

A finite-dimensional predictive theory space is scientifically stronger than an arbitrary EFT, but **finite-dimensional is not the same as unique**.

## Mandatory lanes

### Lane A — RG geometry
Separate fixed-point data from trajectory/critical-surface data. Establish which quantities are fixed by self-similarity and which remain integration constants/relevant coordinates.

### Lane B — inherited-calibration rank
Identify what RQIRCG has actually calibrated (e.g. weak-field Newton normalization and lower-order carrier structure) and count only independent constraints on relevant directions.

### Lane C — literature sanity check
Use asymptotic-safety/fixed-point gravity only as an external comparator: ask whether known analyses generically find zero or nonzero relevant critical-surface dimension. Do not import their beta functions as the candidate model.

### Lane D — physical consequence
Determine whether surviving relevant coordinates can change higher-order/homogeneous nonlinear couplings while preserving the inherited lower-order calibration.

## Strict interpretation rule

Statements such as “only finitely many free parameters remain” or “the theory is predictive” do not pass the selector gate unless the particular nonlinear data required by this project become unique.

## Claim ceiling

SF008 does not validate asymptotic safety, prove existence of a gravitational UV fixed point, or select a published fixed point. It tests the information content of the fixed-point principle class conditional on such a structure.

## Next-step rule

If UFP fails only because relevant coordinates remain, the next high-value question is whether an independently motivated **boundary/state principle** can fix those coordinates. If UFP succeeds, freeze the selected microscopic trajectory before opening `chi_ABC`.
