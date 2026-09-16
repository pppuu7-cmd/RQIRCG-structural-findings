# SF055A3Q7 — Richardson regularity diagnostic preoutcome

Date: 2026-09-16

## Motivation frozen before Q7 result

The authoritative Q6/Q6P fatal-point workflow is non-terminal. No partial Q6 shard value is authorized or used here.

The retained derivative audit already established that the historical frozen Richardson extractor is exact for the p^2 coefficient on an even analytic p^2 expansion through p^4, but an allowed |p|^3 term would generate an O(h) bias. The scalar shifted-Litim witness demonstrates that such nonanalyticity can occur in a regulator-shell control, but does not establish it in the full tensor flow.

The existing frozen momentum ladder already contains p=1/32, 1/16, 1/8. Therefore an outcome-independent algebraic diagnostic can be constructed before any new Q6 output to test sensitivity to a p^3/|p|^3 component without changing the Q6 science contract.

## HYPOTHESIS

For p>=0 and h=1/32, the three reduced finite differences

`D_r = [F(r h)-F(0)]/(r h)^2`, for r in {1,2,4},

contain enough information to construct:

1. a unique linear estimator `C2_234` that returns c2 exactly for every polynomial
   `F(p)=F0+c2 p^2+c3 p^3+c4 p^4`;
2. a unique linear estimator `C3_234` that returns c3 exactly on the same span;
3. an exact identity relating the historical two-scale Richardson estimator
   `R_h=[4 D_1-D_2]/3`
   to `C2_234` and `C3_234`.

## OBJECT

Purely algebraic transform of the already-frozen momentum ladder. No new flow integration, no target value, no fitted coefficient and no partial Q6 output.

## FROZEN INPUTS

- `h=1/32`;
- momentum magnitudes `h,2h,4h = 1/32,1/16,1/8`;
- `D_r=[F(rh)-F(0)]/(rh)^2`;
- historical `R_h=(4D_1-D_2)/3`;
- basis span `{1,p^2,p^3,p^4}` for exact-control construction only.

The p=1 finite-difference control is excluded because it is a different projection object. No Q6 beta target is an input.

## REQUIRED CONTROLS

Positive controls:

1. constant term annihilated by every D_r;
2. pure p^2 returns `C2_234=c2`, `C3_234=0`;
3. pure p^3 returns `C2_234=0`, `C3_234=c3`;
4. pure p^4 returns `C2_234=0`, `C3_234=0`;
5. historical Richardson returns p^2 exactly, annihilates p^4, and has the retained p^3 moment `2h/3`.

Negative controls:

- dropping any one of r={1,2,4} must destroy unique simultaneous exactness for c2 and c3 while annihilating c4;
- substituting the p=1 finite-difference object is invalid;
- choosing weights after seeing Q6 output is invalid;
- using this diagnostic to rewrite the historical Q6 PASS/BLOCKED/FAIL criteria is invalid.

## PASS / BLOCKED / INVALID

PASS:

`PASS_Q7_RICHARDSON_REGULARITY_DIAGNOSTIC_CONSTRUCTED_SCOPED`

iff the linear systems are nonsingular and all symbolic controls and the exact Richardson identity hold.

BLOCKED:

`BLOCKED_Q7_RICHARDSON_REGULARITY_DIAGNOSTIC_NOT_IDENTIFIABLE_SCOPED`

if the three-scale system cannot uniquely separate c2,c3 while annihilating c4.

INVALID:

`INVALID_Q7_POSTHOC_OR_OBJECT_SUBSTITUTION`

for use of partial Q6 values, p=1 as a substitute object, post-output weight selection, or any change to the frozen Q6 classification criteria.

## INTERPRETATION CEILING

A Q7 PASS constructs a regularity/contamination diagnostic only. It does not establish that the full tensor flow contains a nonzero |p|^3 term, does not alter the frozen Q6 Richardson estimator, does not produce a Q6 baseline verdict, does not close derivative-truncation error, and does not authorize substantive C3 flow or physical matching.

Retain:

`Q7_DIAGNOSTIC_PASS != Q6_BASELINE_PASS`.

`Q7_DIAGNOSTIC_PASS != NONZERO_FULL_TENSOR_ABS_P3`.

`Q7_DIAGNOSTIC_PASS != DERIVATIVE_TRUNCATION_CLOSURE`.
