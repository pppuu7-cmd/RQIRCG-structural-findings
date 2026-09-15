# SF034 — minimal connected control-phase transfer map — TERMINAL

Date: 2026-09-15
Preregistration: `45a121c99f41e285b4f007984ffe55763831f343`.
Script: `scripts/sf034_checks.py`, commit `a91d891da3982ceb052ffbb5f98d33b67b69eedf`.
Canonical raw: `results/raw/SF034_CHECKS.json`, commit `5c43b6c4a19a86fc18c1937e8880dccf271e8e72`.
Authority/derivation notes: `research_log/SF034_CONTROL_PHASE_TRANSFER_AUTHORITY_NOTES.md`, commit `2257ef1c8ad6a496811286d5d9f2f15350f636d4`.
Executed script SHA-256: `8aea50d69c895dcd8ebc4ecf0b602e987103a6ee07ee14a148ae2a712e5e9d1b`.

## RESULT / CLASSIFICATION

`CONNECTED_CONTROL_PHASE_TRANSFER_MAP_DERIVED_UNDER_CONTROL_SEPARABILITY_SCOPED`

Mandatory qualification:

`MODEL_LEVEL_TRANSFERABILITY_NOT_DEVICE_VALIDATION`.

Secondary structural result:

`C3_REJECTS_DIAGONAL_CONTROL_PHASES_THROUGH_BOOLEAN_DEGREE_TWO_SCOPED`.

## Exact connected-phase algebra

For the frozen branch-reference coherence definition, a diagonal register phase `f(a,b,c)` contributes

`Theta3_reg=-Delta3[f] T`.

The exact Boolean third differences are

`Delta3[1]=0`,

`Delta3[nA]=Delta3[nB]=Delta3[nC]=0`,

`Delta3[nA nB]=Delta3[nA nC]=Delta3[nB nC]=0`,

`Delta3[nA nB nC]=1`.

Therefore all constant, one-body and pairwise diagonal register/control phases cancel exactly from `C3`.

The lowest-degree diagonal register nuisance that can mimic an additive connected time-linear phase is

`H_err = hbar zeta nA nB nC`.

Its contribution is

`Theta3_reg=-zeta T`.

## M0 transfer result

Science uses `lambda_A=1`.

Delete-A uses `lambda_A=0` but leaves the A branch qubit present and changes only A motional displacement plus the compensating D recoil displacement.

Under the prospectively frozen control-separability condition

`partial H_reg/partial lambda_A = 0`,

the same cubic nuisance acts in both configurations:

`Theta3_reg^science=-zeta T`,

`Theta3_reg^deleteA=-zeta T`.

Thus

`Theta3_reg^science-Theta3_reg^deleteA=0`

exactly within M0.

The inherited delete-A gravitational connected basis remains exactly null at the retained order:

`x_app=x_fb=x_1PN=0`.

Hence the null-control channel contains the connected control phase while carrying no retained connected known-gravity signal.

## SF033 six-element closure

The explicit effective model supplies all six elements required by SF033:

1. nuisance generator: `H_reg`;
2. science action: `lambda_A=1`;
3. delete-A action: `lambda_A=0`;
4. equality reason: prospective control separability;
5. fixed-vs-changed variables: register Hamiltonian/readout/time fixed, A/D motional transport changed;
6. falsification condition: any nonzero dependence of the cubic connected phase on `lambda_A`.

Score:

`6/6` at the **effective-model** level.

This supersedes the SF033 `0/6` object absence only for this newly defined prospective model class. It does not retroactively change SF033.

## Mandatory M1 falsifier

For

`zeta(lambda_A)=zeta0+zeta1 lambda_A`,

science contains

`-(zeta0+zeta1)T`,

while delete-A contains

`-zeta0 T`.

The null-subtracted control residual is

`-zeta1 T`.

Delete-A alone cannot identify `zeta1`.

Therefore transferability is not a generic property of cubic control phases. It is a specific, falsifiable property of the M0 separable class.

## Relation to SF032

SF032 established a very large calibration gain **conditional** on a shared time-linear nuisance.

SF034 now supplies one explicit effective model in which that sharing is exact.

The logical chain becomes

`EXACT GRAVITY NULL`
`+ EXPLICIT CONTROL-SEPARABLE CUBIC PHASE MODEL`
`=> EXACT MODEL-LEVEL SHARED TAU-LINEAR NUISANCE`
`=> SF032 CALIBRATION BENEFIT APPLIES WITHIN THAT MODEL CLASS`.

Do not remove the model qualifier.

## Physical-realization scope

Primary experimental literature demonstrates physically realizable classes of state-dependent motional control and genuine higher-body register interactions. Residual diagonal register couplings are also established control/calibration concerns in quantum processors.

These sources support non-vacuity of the model class only. They do not validate `zeta1=0` in a specific RQIRCGSF device.

## New operational frontier

The dominant remaining transfer uncertainty has collapsed to one explicit derivative-like datum:

`zeta1 = partial zeta / partial lambda_A`.

The next high-information gate is

`SF035_CONTROL_PHASE_AMPLITUDE_DEPENDENCE_CALIBRATION_PREOUTCOME_GATE`.

It should prospectively freeze an A-displacement amplitude ladder, retain the same `C3` observable and known-gravity model, and test whether `zeta0` and `zeta1` are separately identifiable from known gravity without fitting a successor residual.

## Claim ceiling

SF034 does not establish:

- that a real device satisfies M0;
- experimental common-mode transferability;
- a hardware platform;
- pulse/control fidelity;
- detector feasibility;
- a successor quantum residual;
- a quantum matching coefficient;
- quantum `chi_ABC`;
- new physics.

Retain:

`MODEL_LEVEL_TRANSFERABILITY != EXPERIMENTAL_TRANSFERABILITY`.

Retain:

`CONTROL_CALIBRATION != DEVICE_VALIDATION`.
