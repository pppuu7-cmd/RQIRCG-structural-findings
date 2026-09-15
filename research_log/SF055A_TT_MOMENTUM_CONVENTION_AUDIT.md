# SF055A — TT momentum-convention audit after first seed-engine run

Date: 2026-09-15
Parent preregistration: `prereg/SF055A_EH_GHOST_BASELINE_SEED_ENGINE_PREOUTCOME.md`, commit `86cf13ac59b03c21d48d67181e755935bfeb152d`.
First executed implementation head: `5073657af9f66885d677b72121b7a0872514f5f9`.

This is a **post-outcome diagnostic**. It does not change the frozen SF055A success criterion and cannot convert the first run into PASS.

## FIRST-RUN FACT

GitHub Actions run `34996889146`, job `104475264530`, executed all prospectively frozen seed controls.

All controls except the frozen TT two-point normalization/sign control passed:

- common EH n=3,4,5 dense controls: finite, nonzero and Bose symmetric over 6, 24 and 120 permutations;
- FP ghost two-point: PASS;
- FP ghost-h interaction and h-degree controls: PASS;
- optimized regulator denominators: PASS;
- six numerical threshold-function controls: PASS;
- all eight prospectively frozen negative mutations: rejected.

The TT control instead returned, for every one of the five TT polarizations,

`Gamma_raw^(2) = -K_EH (p_real^2 + 2 Lambda)`,

with `K_EH=1/(32 pi)` and `p_real^2=1`.

Examples from the preserved raw artifact:

- `Lambda=0`: `-0.00994718394324346`;
- `Lambda=+0.15`: `-0.0129313391262165`;
- `Lambda=-0.2`: `-0.00596831036594607`.

The frozen positive control had required

`+K_EH (p^2 - 2 Lambda)`.

## PRIMARY-SOURCE CHECK

Primary source: Christiansen, Knorr, Pawlowski, Rodigast, *Global Flows in Quantum Gravity*, arXiv:1403.1232v2.

The paper fixes:

- Eq. (5): `S_EH=(16 pi G_N)^(-1) int sqrt(g)(-R+2 Lambda)`;
- Eq. (11): `Gamma_TT^(2)(p^2)=Z_h(p^2)(p^2-M^2) Pi_TT(p)`;
- Eq. (15): the scalar TT coefficient is `Z_h(p^2)(p^2-2 Lambda_k^(2))`;
- Eq. (16): `M_k^2=-2 Lambda_k^(2)`.

Thus the source momentum `p_source` is the ordinary Fourier momentum for plane waves `exp(i p_source.x)`, so source derivatives act as

`partial_mu -> i p_source,mu`.

## WHY THE FROZEN CONTROL WAS ILL-POSED

The SF055A preregistration simultaneously froze a **real-exponential** local derivative convention

`partial_mu exp(p_real.x)=p_real,mu exp(p_real.x)`

and required the source-Fourier TT coefficient

`+K_EH(p^2-2 Lambda)`

without the analytic continuation between the two momentum coordinates.

They are not the same coordinate convention.

The analytic relation is

`p_source = -i p_real`,

hence

`p_source^2 = -p_real^2`.

Substituting this into the source TT coefficient gives

`K_EH(p_source^2-2 Lambda)`
`= K_EH(-p_real^2-2 Lambda)`
`= -K_EH(p_real^2+2 Lambda)`,

which is exactly what the direct covariant action generator returned for all 15 frozen TT records.

Therefore the source action is reconstructible; the mismatch is caused by an internally inconsistent positive-control convention.

## CLASSIFICATION

The preregistration explicitly provided

`INVALID_SEED_POSITIVE_CONTROL`

for a positive control that is degenerate or ill-posed while the underlying source object remains reconstructible.

That condition is met.

The first SF055A seed-engine subgate is therefore scientifically classified:

`INVALID_SEED_POSITIVE_CONTROL_MIXED_FOURIER_CONVENTIONS_SCOPED`.

The raw program output originally labeled the result `BLOCKED_EH_GHOST_SEED_OBJECT_NOT_RECONSTRUCTIBLE`; that raw label is preserved verbatim in `results/raw/SF055A_EH_GHOST_SEED_ENGINE_FIRST_RUN.json` and is superseded only at the scientific interpretation layer by this source audit. It is not rewritten.

## WHAT THIS DOES NOT AUTHORIZE

This INVALID result does not authorize changing the first gate's criterion and rerunning it as though it had passed.

It also does not establish Lane-A PASS, a loop integrand, Eq. (14) reproduction, or any C3 beta function.

## LEGITIMATE SUCCESSOR

A new prospectively frozen seed gate may be opened using one internally consistent convention throughout. The preferred source-faithful choice is ordinary Fourier external momenta

`partial_mu -> i p_mu`,

for which the TT target remains exactly the published/source-normalized

`+K_EH(p^2-2 Lambda)`.

Such a successor is a correction of an invalid measurement convention, not a post-hoc change to the first gate.
