# SF038 — signed-amplitude parity calibration — PREOUTCOME

Date: 2026-09-15
Parent recovery: `56f56d2d927fecbafe3070348f2c9f84cedc0936`.

## PURPOSE

Test whether reversing the A transport direction provides parity information that materially separates the Q2 connected control-phase nuisance from the ordinary 1PN amplitude shape, at the same total row count as SF036/SF037.

## INDEPENDENT PARITY MOTIVATION

For the retained Q2 control nuisance

`zeta(lambda)=zeta0+zeta1 lambda+zeta2 lambda^2`,

a symmetric signed amplitude set makes

`lambda` odd and `lambda^2` even.

With symmetric weights the pure nuisance columns `lambda tau` and `lambda^2 tau` have zero odd/even cross moment before gravity is included.

This motivates the signed design prospectively. It is not chosen from a connected-gravity outcome.

## FROZEN SIGNED DESIGN

`lambda_A in {-1,-1/2,0,1/2,1}`.

Keep

`R/ell in {60,160,400}`,

`tau in {0.05,0.1,0.2}`.

Total rows: 45, exactly matching the positive five-point SF036/SF037 design.

At each signed amplitude recompute the exact A and compensating D branch centers and the full known-gravity coefficients. Do not infer negative-amplitude values by odd/even symmetry.

## DOMAIN CONTROL

All branch-center separations must remain positive for every signed amplitude and frozen R. Record the minimum separation.

Any collision/order failure is `BLOCKED_INVALID_SIGNED_GEOMETRY`, not a physics result.

## RETAINED Q2 MODEL

`zeta(lambda_A)=zeta0+zeta1 lambda_A+zeta2 lambda_A^2`.

Design columns:

`x_app=-Delta3 V_N(lambda,R) tau`,

`x_fb=[Delta3 A_N(lambda,R)/12] tau^3`,

`x_1PN=-Delta3 V_static^1PN(lambda,R) tau`,

`x_z0=tau`,

`x_z1=lambda tau`,

`x_z2=lambda^2 tau`.

No higher nuisance degree and no successor residual are allowed.

## STRUCTURAL METRICS

Column-normalized SVD with rank tolerance `1e-10*s_max`.

Record rank, `kappa`, `smin`, and near-null vector.

Frozen positive-five-point comparator:

`kappa_pos=219.1476037531367`,

`smin_pos=0.010076217942614964`.

## NOISE-AWARE METRICS

Use the SF037 iid model with `epsilon_PN=1e-6` as the representative diagnostic; the scaling law will be checked by one additional `epsilon_PN=1e-8` control.

Compute PN VIF relative to a known-only K3 fit on the **same signed 45 rows**, and compute

`sigma_y,SNR1/epsilon_PN`.

Frozen positive-five-point comparator:

`VIF_pos=909.166134380049`,

`q_pos=1.2636705529477296e-5`.

## STRONG INFORMATION-GAIN RULE

`SIGNED_AMPLITUDE_PARITY_STRONGLY_IMPROVES_Q2_CALIBRATION_SCOPED`

requires full rank 6 and at least TWO of:

1. `kappa_signed <= kappa_pos/3`;
2. `smin_signed >= 3*smin_pos`;
3. `VIF_signed <= VIF_pos/3`.

## MODEST / NULL RULES

`SIGNED_AMPLITUDE_PARITY_MODESTLY_IMPROVES_Q2_CALIBRATION_SCOPED`

if full rank is retained and at least one primary metric improves but the strong rule is not met.

`SIGNED_AMPLITUDE_PARITY_DOES_NOT_IMPROVE_Q2_CALIBRATION_SCOPED`

if full rank is retained but none of the three primary metrics improves.

Rank deficiency is recorded separately and is not converted into a gravity FAIL.

## MANDATORY CONTROLS

C1. Signed geometry collision/order audit.

C2. `lambda=0` exact connected known-gravity null.

C3. Positive endpoint `lambda=1` recovers SF036 values.

C4. Delete-one-label exact-zero controls over the signed grid.

C5. Recompute the positive five-point comparator with the same implementation for consistency.

C6. Check the pure nuisance parity inner product between `lambda tau` and `lambda^2 tau` is zero on the symmetric design.

C7. Verify `sigma_y,SNR1/epsilon_PN` stability between `epsilon_PN=1e-6` and `1e-8`.

## INTERPRETATION CEILING

A strong PASS would establish that signed transport reversal is a materially better calibration design against the frozen Q2 nuisance family.

It would not establish that negative-amplitude control is experimentally easy, that a real device obeys Q2, that the resulting precision is achievable, or that any residual is quantum gravity.

No quantum matching coefficient, quantum `chi_ABC`, new physics or parent promotion is authorized.
