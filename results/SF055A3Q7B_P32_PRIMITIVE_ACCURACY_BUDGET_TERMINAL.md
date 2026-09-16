# SF055A3Q7B p=1/32 primitive accuracy budget — TERMINAL

Date: 2026-09-16

Prospective diagnostic preregistration: `7f4dec270e50d2c63427e3187daf06497c562b55`.

Executable diagnostic: `scripts/sf055a3q7b_p32_accuracy_budget.py`, creation commit `a2c837bedb481fd15b4d6e2930f3faab31e89786`.

Raw deterministic record: `results/raw/SF055A3Q7B_P32_PRIMITIVE_ACCURACY_BUDGET.json`.

No Q8 N>24 value is used by this diagnostic.

## Classification

`PASS_Q7B_P32_PRIMITIVE_ACCURACY_BUDGET_CONSTRUCTED_SCOPED`.

This is a numerical error-budget diagnostic only. It does not rewrite Q6 or pre-judge Q8.

## Exact sensitivity

For the historical Richardson derivative

`R=(4 D32-D16)/3`,

with

`D32=[F32-F0]/h^2`, `h=1/32`,

and

`beta_g=2+2 N_g R`,

Q7B obtains

`|d beta_g / d F32| = 5,164,428.3780624345`.

An independent symmetric finite-difference check gives

`5,164,428.3578511365`,

with relative discrepancy

`3.913559553763567e-09`,

below the frozen `1e-8` construction tolerance.

## Primitive accuracy budget implied by the historical 0.2% criterion

At the authoritative Q6 N24 scale

`beta_g=-7.590697586295343`,

the historical 0.2% convergence criterion corresponds to an allowed absolute beta change

`0.015181395172590687`.

If the dominant p=1/32 primitive alone changes, this translates locally to

`|Delta Flow_G(p=1/32)| <= 2.9396080381477514e-09`.

This is not a replacement Q8 threshold; it is an exact local translation of the already-existing historical beta criterion at the Q6 N24 scale.

## How far Q6 was from that numerical regime

Observed Q6 values:

- N16: `Flow_G(p=1/32)=0.0005545825645617668`;
- N24: `Flow_G(p=1/32)=0.0005537769479482976`.

Absolute drift:

`8.056166134691499e-07`.

Therefore the N16->N24 p=1/32 drift was

`274.05579349849967`

times larger than the local primitive-stability budget implied by the frozen 0.2% beta criterion.

This quantitatively explains why merely being target-close at N24 could not establish derivative convergence.

## Inherited p=0 error floor

Using the canonical Q6 derivative ladder to reconstruct the common primitive,

- `F0(N16)=0.0005562382713360568`;
- `F0(N24)=0.0005562382414400815`;
- `|Delta F0|=2.9895975343745274e-11`.

The exact anchored sensitivity is

`|d beta_g/dF0|=4,841,651.604433533`,

so the propagated absolute beta floor is

`0.00014474589698914965`.

This is only

`0.009534426536138242`

of the historical allowed beta change, i.e. about **0.9534% of that budget**.

Therefore the inherited p=0 finite-N drift is too small to explain or obstruct the dominant p=1/32 resolution problem at the present error-budget level.

## New retained numerical fact

The current numerical target is now sharply quantified:

`P32_PRIMITIVE_STABILITY_REQUIRED_AT_FEW_TIMES_1E-9_FLOW_G_SCALE_SCOPED`.

The earlier Q6 N16->N24 p=1/32 drift was about 274 times too large for the historical beta convergence requirement, while the inherited p=0 drift consumes only about 0.95% of the corresponding beta budget.

Retain:

`TARGET_PROXIMITY != PRIMITIVE_RESOLUTION`.

`P0_FINITE_N_FLOOR_SMALL != DERIVATIVE_REGULARITY_CLOSED`.

`Q7B_DIAGNOSTIC_PASS != Q8_CONVERGENCE_PASS`.

## Interpretation ceiling

Not established:

- Q8 convergence;
- continuum derivative regularity;
- Q6 baseline PASS;
- continuum `|p|^3` coefficient zero or nonzero;
- projected physical C3 flow;
- physical matching;
- asymptotic-safety correctness or failure;
- programme disposition;
- `chi_ABC`.

## Operational consequence

Q8 is now testing a quantitatively meaningful regime rather than an unspecified notion of "higher resolution". If its N40->N48 anchored beta convergence passes the prospectively frozen contract, the dominant primitive-resolution blocker is numerically closed at that gate. If it remains blocked, Q7B measures exactly how far the primitive remains from the required stability scale.
