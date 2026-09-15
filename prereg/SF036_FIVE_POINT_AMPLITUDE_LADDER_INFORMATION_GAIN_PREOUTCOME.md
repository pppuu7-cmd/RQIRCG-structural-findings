# SF036 — five-point amplitude ladder information gain — PREOUTCOME

Date: 2026-09-15
Parent terminal: SF035 `da807bcd82d1a64598ba9ba9252ceb6e6df4ffd6`.

## PURPOSE

Test whether a denser prospectively fixed A-displacement ladder materially reduces the SF035 Q2 near-degeneracy between the 1PN amplitude shape and quadratic connected control-phase curvature, without changing the gravitational model, R/T design, Q2 nuisance degree or readout.

## RETAINED OBJECT

Keep exactly the SF028B/SF035 boundary-complete `C3` object, masses, branch geometry, COM-closure rule, Newtonian/EIH baselines and Q2 nuisance family.

No successor residual is allowed.

## FROZEN FIVE-POINT AMPLITUDE DESIGN

`lambda_A in {0,1/4,1/2,3/4,1}`.

Retain

`R/ell in {60,160,400}`,

`tau in {0.05,0.1,0.2}`.

Total rows: `5 x 3 x 3 = 45`.

For every new amplitude recompute the exact known-gravity basis with the A and compensating D displacement changed together.

Do not interpolate the three SF035 amplitude cells.

## RETAINED Q2 MODEL

`zeta(lambda_A)=zeta0+zeta1 lambda_A+zeta2 lambda_A^2`.

Design columns:

`x_app=-Delta3 V_N(lambda_A,R) tau`,

`x_fb=[Delta3 A_N(lambda_A,R)/12] tau^3`,

`x_1PN=-Delta3 V_static^1PN(lambda_A,R) tau`,

`x_z0=tau`,

`x_z1=lambda_A tau`,

`x_z2=lambda_A^2 tau`.

No cubic-or-higher control nuisance is permitted in SF036.

## FROZEN METRICS

Column-normalize to unit Euclidean norm before SVD.

Rank tolerance: `1e-10*s_max`.

Record

- rank;
- all normalized singular values;
- condition number;
- smallest singular value;
- right-singular near-null vector.

The SF035 three-point Q2 comparator is fixed at

`kappa_3pt = 899.7091025733095`,

`smin_3pt = 0.002445567828550082`.

## MATERIAL INFORMATION-GAIN RULE

### STRONG PASS

`FIVE_POINT_AMPLITUDE_LADDER_STRONGLY_IMPROVES_Q2_CONDITIONING_SCOPED`

if the full five-point design has rank 6 and BOTH

`kappa_5pt <= kappa_3pt/3`

and

`smin_5pt >= 3*smin_3pt`.

### MODEST PASS

`FIVE_POINT_AMPLITUDE_LADDER_MODESTLY_IMPROVES_Q2_CONDITIONING_SCOPED`

if rank 6 is retained and conditioning improves but one or both factor-three criteria are not met.

### NULL

`ADDITIONAL_UNIFORM_AMPLITUDE_POINTS_DO_NOT_MATERIALLY_BREAK_Q2_NEAR_DEGENERACY_SCOPED`

if rank remains 6 but `kappa` does not improve.

### BLOCKED

Use `BLOCKED` only for an invalid exact-gravity object or failed control, not for poor conditioning.

## MANDATORY CONTROLS

C1. `lambda_A=0` exact gravity null.

C2. `lambda_A=1` endpoint recovery.

C3. Delete-one-label exact-zero controls on every new amplitude cell.

C4. Leave-one-interior-amplitude-out designs for drops `1/4`, `1/2`, `3/4`; record rank and kappa.

C5. Retain the SF035 three-point design `{0,1/2,1}` as a frozen comparator computed by the same implementation.

C6. One fixed-R ablation remains rank-deficient or otherwise records its exact limitation; no rescue by amplitude points is assumed.

C7. One fixed-tau ablation records rank/conditioning; no time-lever replacement is assumed.

## INTERPRETATION CEILING

A strong PASS would show that **amplitude design** can break much of the Q2/1PN shape near-degeneracy at the structural level.

It would not establish phase precision, device linearity, shot noise, laboratory feasibility, higher-than-quadratic nuisance control, successor quantum residuals, quantum matching coefficients, quantum `chi_ABC` or new physics.

Retain:

`DESIGN_INFORMATION_GAIN != DEVICE_FEASIBILITY`.
