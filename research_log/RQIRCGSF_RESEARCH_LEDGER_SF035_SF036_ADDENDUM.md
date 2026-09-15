# RQIRCGSF research ledger — SF035 / SF036 addendum

Date: 2026-09-15

## SF035

Gate: `SF035_CONTROL_PHASE_AMPLITUDE_DEPENDENCE_CALIBRATION_PREOUTCOME_GATE`.

Preregistration: `854c33c5fde4092b76c506d39f6eea056784a182`.

Main script: `fa90297afc7040b7cf23d8b06cb89c97fe789c6b`.

Raw: `8a411f87e126b5e5186afb8e2bb850eb1cbc95be`.

Near-null diagnostic: `ccd96870843939cf4840487cfe0206f53b0b365e` / `532e0be167054184c80aa7228dbe271f8f5a3362`.

Terminal: `da807bcd82d1a64598ba9ba9252ceb6e6df4ffd6`.

Primary result:

`LINEAR_CONTROL_PHASE_AMPLITUDE_DEPENDENCE_IDENTIFIABLE_SCOPED`.

Qualified Q2 result:

`QUADRATIC_CONTROL_PHASE_AMPLITUDE_DEPENDENCE_IDENTIFIABLE_BUT_ILL_CONDITIONED_SCOPED`.

Three-point full L1 design: rank 5, `kappa=23.897`.

Three-point full Q2 design: rank 6, `kappa=899.709`.

Q2 near-null direction is dominated by 1PN versus `zeta1/zeta2`, not Newtonian feedback.

## SF036

Gate: `SF036_FIVE_POINT_AMPLITUDE_LADDER_INFORMATION_GAIN_PREOUTCOME_GATE`.

Preregistration: `b75f25c587ba32c55750ab40ce77a11edf4a6c34`.

Script: `164e432ce903dc1b7ca4b10e2d3e1663992dc644`.

Raw: `4d7046d6c6907cafa50211374664c67e30e92062`.

Terminal: `43c6422f251bba181593a7512ea57e470e0e061d`.

Result:

`FIVE_POINT_AMPLITUDE_LADDER_STRONGLY_IMPROVES_Q2_CONDITIONING_SCOPED`.

Five-point Q2 design: rank 6, `kappa=219.148`, `smin=0.0100762`.

Relative to SF035 three-point design:

- `kappa` improves by factor `4.1055`;
- `smin` improves by factor `4.1202`.

All leave-one-interior-amplitude designs remain rank 6.

Single-R and single-tau controls show that amplitude variation does not replace R/T leverage.

## FRONTIER EFFECT

The quadratic control nuisance is not exactly degenerate with the 1PN amplitude shape. Structural information can be increased by amplitude design.

The remaining bottleneck is now precision/estimability of 1PN while jointly fitting `zeta0,zeta1,zeta2`.

## NEXT

`SF037_NOISE_AWARE_Q2_CONTROL_CALIBRATION_ESTIMABILITY_PREOUTCOME_GATE`.

No successor residual, quantum matching coefficient, quantum `chi_ABC`, new physics or parent promotion is authorized.
