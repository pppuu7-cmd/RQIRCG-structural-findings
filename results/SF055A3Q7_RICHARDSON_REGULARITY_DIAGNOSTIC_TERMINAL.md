# SF055A3Q7 — Richardson regularity diagnostic — TERMINAL

Date: 2026-09-16

Preregistration: `61461e28abc9a51cb697e20953033e46e7035aa4`.

No partial Q6/Q6P shard value was inspected or used. The authoritative Q6 fatal-point workflow remained non-terminal throughout this derivation.

## Classification

`PASS_Q7_RICHARDSON_REGULARITY_DIAGNOSTIC_CONSTRUCTED_SCOPED`.

Secondary:

`EXISTING_FROZEN_MOMENTUM_LADDER_SEPARATES_P2_P3_P4_CONTROL_SPAN_SCOPED`.

This is a numerical-analysis / regularity diagnostic result only. It is not Q6 baseline PASS and it does not establish a nonzero |p|^3 term in the full tensor flow.

## Frozen setup

Let

`h=1/32`,

and for `r in {1,2,4}` define

`D_r=[F(rh)-F(0)]/(rh)^2`.

On the control span

`F(p)=F0+c2 p^2+c3 p^3+c4 p^4`, for p>=0,

we have

`D_r=c2+c3 r h+c4 r^2 h^2`.

The moment matrix for r={1,2,4} has determinant

`det = 6`,

so the three coefficients are algebraically identifiable on this frozen control span.

## Exact c2 diagnostic

The unique weights returning c2 while annihilating the p^3 and p^4 control directions are

`(8/3,-2,1/3)` on `(D_1,D_2,D_4)`.

Thus

`C2_234 = (8 D_1 - 6 D_2 + D_4)/3`.

It satisfies exactly:

- p^2 moment = 1;
- p^3 moment = 0;
- p^4 moment = 0.

Its next moments are

- p^5 contamination `8 h^3`;
- p^6 contamination `56 h^4`.

Therefore Q7 does not assume an exact finite polynomial model for the real flow; it only constructs a controlled diagnostic on the frozen low-order span.

## Exact c3 / |p|^3-sensitive diagnostic

The unique dimensionless weights satisfying constant/c2 removal and p^4 removal are

`(-2,5/2,-1/2)`.

Define

`C3_234 = [-2 D_1 + (5/2)D_2 - (1/2)D_4]/h`.

On the frozen control span this returns exactly c3 and annihilates c2 and c4.

Higher-order contamination begins as

- p^5 -> `-14 h^2 c5`;
- p^6 -> `-90 h^3 c6`.

Thus `C3_234` is a regularity diagnostic, not a theorem that every nonzero value must be a pure |p|^3 coefficient.

## Exact relation to the historical Richardson estimator

The historical frozen estimator is

`R_h=(4D_1-D_2)/3`.

Its moments are:

- p^2 -> 1;
- p^3 -> `2h/3`;
- p^4 -> 0;
- p^5 -> `-4h^3/3`;
- p^6 -> `-4h^4`.

The following is an exact coefficient-vector identity for arbitrary input values D_1,D_2,D_4:

`R_h - C2_234 = (2h/3) C3_234`.

The residual coefficient vector is exactly `(0,0,0)` in rational arithmetic.

This sharpens the earlier derivative audit: the existing p=1/8 point makes the leading cubic-sensitive discrepancy observable without changing the historical Richardson definition.

## Conditioning cost

Direct weights on `(F0,Fh,F2h,F4h)` at h=1/32 are:

Historical Richardson:

- `F0=-1280`;
- `Fh=4096/3`;
- `F2h=-256/3`;
- `F4h=0`.

Primitive-error L1 amplification:

`8192/3 = 2730.666666...`.

C2_234:

- `F0=-2240`;
- `Fh=8192/3`;
- `F2h=-512`;
- `F4h=64/3`.

Primitive-error L1 amplification:

`5504`.

Ratio to historical Richardson:

`5504/(8192/3)=2.015625`.

C3_234 direct weights are

- `F0=46080`;
- `Fh=-65536`;
- `F2h=20480`;
- `F4h=-1024`,

with L1 amplification `133120` in its own c3 units.

Therefore the three-scale construction is highly informative as a diagnostic but is not automatically a numerically superior replacement estimator. A post-hoc substitution into the Q6 PASS/BLOCKED/FAIL contract is explicitly forbidden.

## Negative control: why two scales are insufficient

For any retained pair of radii `a,b` from `{1,2,4}`, the nonzero polynomial

`F(p)-F0 = p^2 (p-a h)(p-b h)`

has

`c2=ab h^2`,

`c3=-(a+b)h`,

`c4=1`,

but vanishes at both sampled nonzero momenta `p=ah` and `p=bh`.

Hence both corresponding D values are zero even though c2 and c3 are nonzero. This gives an explicit counterexample proving that any two-scale subset cannot uniquely separate c2/c3 while controlling c4.

All three negative controls `{1,2}`, `{1,4}`, `{2,4}` pass.

## Reproducibility

Script:

`scripts/sf055a3q7_richardson_regularity.py`.

Script creation commit:

`628e2352d5f867e6433cda305c0abbfe02f54cfc`.

Local script SHA256:

`87dde66306689295432660538b1cf7b1630ef417e75679f86ba22bd470188e96`.

Raw exact-rational output:

`results/raw/SF055A3Q7_RICHARDSON_REGULARITY_LOCAL.json`.

Raw creation commit:

`be73b44925b4bb46f6fbdbc92b5fdc069610b272`.

Local raw SHA256:

`07160497eca3673e3695d9fb1c8c47cc48e070508e86ab9b397a3c056212d641`.

All frozen positive and negative controls are true in exact `fractions.Fraction` arithmetic.

## Interpretation ceiling

Established:

1. the existing frozen h,2h,4h momentum ladder is algebraically sufficient to separate p^2, p^3 and p^4 on the prospectively frozen control span;
2. an exact cubic-sensitive diagnostic exists without any new flow evaluations;
3. the historical Richardson/cubic-sensitive discrepancy obeys an exact identity;
4. two nonzero momentum scales are provably insufficient for the same task;
5. using the cubic-aware c2 transform as a replacement would approximately double worst-case primitive-error L1 amplification.

Not established:

- a nonzero full-tensor |p|^3 coefficient;
- that c3 contamination explains the historical baseline discrepancy;
- certified derivative-truncation error;
- a Q6 science verdict;
- baseline PASS;
- projected C3 beta;
- physical matching b;
- Lorentzian/on-shell matching;
- parent RCG-002 authority change.

Retain:

`Q7_DIAGNOSTIC_PASS != Q6_BASELINE_PASS`.

`Q7_DIAGNOSTIC_PASS != NONZERO_FULL_TENSOR_ABS_P3`.

`Q7_DIAGNOSTIC_PASS != DERIVATIVE_TRUNCATION_CLOSURE`.

## Exact next use

Do not apply Q7 to partial Q6 shards.

After complete merged Q6 values for p=1/32,1/16,1/8 at a common N are authoritative, a separately bounded diagnostic may evaluate `C3_234` and `R_h-C2_234` using the already frozen formulas. Such a diagnostic cannot rewrite the original Q6 convergence/target verdict; it can only determine whether the existing full-tensor momentum ladder shows evidence consistent with a cubic/nonanalytic contamination direction and quantify its size relative to the historical derivative extraction.
