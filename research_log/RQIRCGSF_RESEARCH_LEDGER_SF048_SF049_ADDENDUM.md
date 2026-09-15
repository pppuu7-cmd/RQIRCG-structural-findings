# RQIRCGSF research ledger — SF048 / SF049 addendum

Date: 2026-09-15
Inherited recovery head before SF048: `ac926b7529b8cb6ce8f7117fec9a65d6b23a1ea4`.

## SF048 — six-derivative C3 fluctuation projection audit

Prospective preregistration:

`3e0a7bf408e211273ceeb2e5a818a62bcfa02775`.

Authority audit:

`4d84ac3c5ab3b00708bde6179c328e586726b2e8`.

Terminal:

`c4f0137af15e70681fca595b8ef5e68f46545220`.

Classification:

`BLOCKED_MISSING_EXPLICIT_C3_FLUCTUATION_PROJECTION`.

Secondary:

`PHYSICAL_C3_DIRECTION_UNIQUE_BUT_FRG_PROJECTOR_NOT_CONSTRUCTED_SCOPED`.

Element results:

- P1 physical essential C3 direction: PASS scoped;
- P2 explicit dynamical C3 projector: NOT CLOSED;
- P3 projected C3 flow/reconstruction: NOT CLOSED;
- P4 background-essential to fluctuation identity map: NOT CLOSED;
- P5 Lorentzian target: PARTIAL framework only;
- P6 physical regulator/renormalization closure: NOT CLOSED.

New fact:

`KNOWN_PHYSICAL_C3_DIRECTION + GENERAL_VERTEX_MACHINERY != EXECUTED_C3_FLUCTUATION_PROJECTOR`.

No rank-zero inference was made from the missing map.

## SF049 — physical on-shell helicity projector

Prospective preregistration:

`f04367fa06d44ccb62f236f2ea7c011587ad702f`.

Analytic derivation:

`bd882edb7abb3c2ecd392dbab038813db9642bf3`.

Terminal:

`15f7f9f02d45d4008e45cffccb9cda293d1d309a`.

Classification:

`PHYSICAL_ON_SHELL_C3_HELICITY_PROJECTOR_CONSTRUCTED_SCOPED`.

Qualification:

`FRG_FLOW_AND_BACKGROUND_FLUCTUATION_MAP_REMAIN_OPEN_SCOPED`.

### Exact algebraic result

Little-group weights for a local `+++` three-graviton amplitude force

`B_+++ = [12]^2[23]^2[31]^2`.

Parity gives

`B_--- = <12>^2<23>^2<31>^2`.

Define

`P3+[M] = [M3(+++)]_local,p6 / B_+++`,

`P3-[M] = [M3(---)]_local,p6 / B_---`.

For the Dunbar-normalized R3 deformation:

`P3+ = P3- = alpha`.

Einstein gravity has no local `+++`/`---` three-point component, so both projectors vanish on the EH negative control.

Independent four-point control:

`P4+[delta M] = -delta M4(++++)/(10 K_++++^2 s t u)`

at generic `stu != 0`, returning the same `alpha`.

Thus:

`P3+ = P3- = P4+ = alpha`

on the frozen leading C3/R3 deformation.

### Updated SF048 element interpretation

`P2_ON_SHELL_ALGEBRAIC = CLOSED`.

`P2_EUCLIDEAN_OFF_SHELL_FRG_IMPLEMENTATION = OPEN`.

P3-P6 remain open.

## Information-rank status

Retain:

`R_ASGS_TRUNCATION = 1`.

`R_ASGS_PHYSICAL = UNDEFINED_MAP_NOT_CLOSED`.

A physical coefficient-extraction functional is now explicit, but no projected FRG solution has been connected to it.

## New exact frontier

`C3_HELICITY_PROJECTOR_TO_DYNAMICAL_FRG_FLOW_EMBEDDING_REQUIRED`.

The next high-information gate must operate on the actual dynamical fluctuation flow or a direct Lorentzian equivalent. It must not repeat background fixed-point calculations or generic form-factor reviews.

Minimum missing chain:

`PHYSICAL HELICITY PROJECTOR`
`-> EUCLIDEAN/OFF-SHELL OR DIRECT LORENTZIAN FRG IMPLEMENTATION`
`-> PROJECTED C3 FLOW`
`-> BACKGROUND/FLUCTUATION IDENTITY CONTROL`
`-> LOW-ENERGY PHYSICAL MATCHING`.

## Claim locks

No physical SF025 `b` selected.
No background/fluctuation equality assumed.
No regulator-independent matching claimed.
No quantum `chi_ABC` computed.
No asymptotic-safety correctness or complete-QG claim.
