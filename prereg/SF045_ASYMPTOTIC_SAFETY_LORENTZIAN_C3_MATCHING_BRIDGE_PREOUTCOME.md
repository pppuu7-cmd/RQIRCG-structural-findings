# SF045 — asymptotic-safety Lorentzian C3 matching bridge — PREOUTCOME

Date: 2026-09-15
Status: PROSPECTIVE
Parent authority: recovery/CURRENT_FRONT.md after SF044.

## Gate

`SF045_ASYMPTOTIC_SAFETY_LORENTZIAN_C3_MATCHING_BRIDGE_PREOUTCOME_GATE`

## Inherited facts

SF043 established only truncation-level nonzero selection power on the curvature-cubic matching fibre:

`R_ASGS_TRUNCATION=1`.

Physical selection remains

`R_ASGS_PHYSICAL=UNDEFINED_MAP_NOT_CLOSED`.

SF044 established that a physical observable architecture exists,

`UV fixed point -> effective action/form factors -> on-shell amplitude -> low-energy EFT`,

but did not locate a regulator-independent Lorentzian on-shell map for the pure-gravity Goroff-Sagnotti curvature-cubic direction.

## Exact target object

The target is one explicit, auditable map of the form

`UV-safe essential trajectory`
`-> regulator/scheme-independent Lorentzian 1PI or scattering object`
`-> pure-gravity on-shell amplitude sensitive to the cubic-curvature essential direction`
`-> low-energy physical matching coefficient equivalent to the SF025 positive-loop on-shell matching coordinate`.

The minimum acceptable observable is an on-shell graviton amplitude or equivalent Lorentzian spectral/form-factor observable whose dependence on the cubic-curvature essential coupling is explicitly derived and whose low-energy matching normalization is stated.

## Frozen source hierarchy

Primary literature only for substantive PASS/FAIL claims. Reviews may map the field but cannot close the bridge by themselves.

Search priority:

1. Lorentzian asymptotic-safety graviton amplitudes / scattering;
2. Lorentzian graviton 3- and 4-point functions or cubic-curvature form factors;
3. quantum effective action through cubic curvature with on-shell projection;
4. explicit essential-coupling to physical-amplitude matching;
5. regulator/scheme-dependence analyses of that same object.

## PASS

`PHYSICAL_C3_MATCHING_BRIDGE_DERIVED_SCOPED`

requires one source chain that explicitly provides all of:

1. Lorentzian physical observable or on-shell graviton amplitude;
2. sensitivity to the cubic-curvature/Goroff-Sagnotti essential direction;
3. map from the UV-safe trajectory/fixed-point data to that observable;
4. low-energy matching to the corresponding physical EFT amplitude coefficient;
5. regulator/scheme independence or a demonstrated cancellation/physical renormalization prescription sufficient to identify the coefficient across schemes.

Only then may `R_ASGS_PHYSICAL` receive nonzero finite rank.

## PARTIAL

`PHYSICAL_C3_MATCHING_BRIDGE_PARTIAL_SCOPED`

if at least items 1-4 are explicit but regulator/scheme independence remains quantitatively unresolved. No physical SF025 coefficient may be selected.

## BLOCKED

`BLOCKED_MISSING_LORENTZIAN_ON_SHELL_C3_MAP`

if the literature supplies propagators, spectral functions, quadratic-curvature form factors, Euclidean vertices, truncation-level running couplings, or general amplitude frameworks but not the exact cubic-curvature physical bridge.

## FAIL

A genuine FAIL requires an explicit theorem or calculation showing that no regulator-independent physical observable can depend on the retained essential cubic-curvature direction in the stated scope. Absence of a published map is BLOCKED, not FAIL.

## Controls / firewalls

- do not identify the SF043 representative trajectory constant with physical SF025 `b`;
- do not treat a Euclidean running coupling as an observable amplitude coefficient;
- do not treat regulator dependence of a truncation coordinate as physical nonuniqueness without an observable map;
- do not use state/vacuum choices to select a law/matching coefficient;
- no connected interferometer outcome enters this gate;
- no `chi_ABC`;
- no operational calibration result may select the quantum-law coefficient;
- no asymptotic-safety correctness or uniqueness claim follows from a bridge PASS.

## Interpretation ceiling

At most this gate may establish whether current primary literature closes, partially closes, or does not close the physical map from one asymptotic-safety essential cubic-curvature trajectory to one low-energy on-shell matching direction.

It cannot establish a complete quantum-gravity theory, the correctness of asymptotic safety, experimental feasibility, or historical RCG-002 authority.
