#!/usr/bin/env python3
"""SF055A3Q7B exact p=1/32 primitive-accuracy budget diagnostic."""
import argparse
import json
import math
from pathlib import Path

H=1.0/32.0
P16=1.0/16.0
NG_INV=0.00052874519051635
NG=1.0/NG_INV
THRESH=0.002
PREREG='7f4dec270e50d2c63427e3187daf06497c562b55'


def finite(x):
    return isinstance(x,(int,float)) and math.isfinite(float(x))


def beta_from_primitives(f32,f16,f0):
    d32=(f32-f0)/(H*H)
    d16=(f16-f0)/(P16*P16)
    r=(4.0*d32-d16)/3.0
    return 2.0+2.0*NG*r


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--summary',required=True)
    ap.add_argument('--ladder',required=True)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()

    summary=json.loads(Path(a.summary).read_text())
    ladder=json.loads(Path(a.ladder).read_text())
    n16=summary['N16']; n24=summary['N24']
    l16=ladder['records']['16']; l24=ladder['records']['24']

    vals=[n16['Flow_G_p32'],n16['Flow_G_p16'],n24['Flow_G_p32'],n24['Flow_G_p16'],
          n24['beta_g'],l16['D_1_32'],l24['D_1_32']]
    inputs_ok=all(finite(v) for v in vals)

    f0_16=float(n16['Flow_G_p32'])-float(l16['D_1_32'])*H*H
    f0_24=float(n24['Flow_G_p32'])-float(l24['D_1_32'])*H*H
    delta_f0=abs(f0_24-f0_16)
    delta_f32=abs(float(n24['Flow_G_p32'])-float(n16['Flow_G_p32']))

    k32=abs(8.0*NG/(3.0*H*H))
    allowed_beta=THRESH*abs(float(n24['beta_g']))
    budget_f32=allowed_beta/k32
    ratio_obs=delta_f32/budget_f32

    coeff_r_f0=(4.0*(-1.0/(H*H))-(-1.0/(P16*P16)))/3.0
    k0=abs(2.0*NG*coeff_r_f0)
    beta_floor0=k0*delta_f0
    floor_ratio=beta_floor0/allowed_beta

    f32=float(n24['Flow_G_p32']); f16=float(n24['Flow_G_p16']); f0=f0_24
    eps=1.0e-12
    bp=beta_from_primitives(f32+eps,f16,f0)
    bm=beta_from_primitives(f32-eps,f16,f0)
    k32_fd=abs((bp-bm)/(2.0*eps))
    sens_rel=abs(k32_fd-k32)/k32
    sensitivity_pass=sens_rel<=1.0e-8

    construction_pass=bool(inputs_ok and finite(delta_f0) and delta_f0>=0.0 and sensitivity_pass)
    classification=('PASS_Q7B_P32_PRIMITIVE_ACCURACY_BUDGET_CONSTRUCTED_SCOPED'
                    if construction_pass else
                    'BLOCKED_Q7B_P32_PRIMITIVE_ACCURACY_BUDGET_CONSTRUCTION_SCOPED')

    out={
      'gate':'SF055A3Q7B_P32_PRIMITIVE_ACCURACY_BUDGET',
      'preregistration_commit':PREREG,
      'classification':classification,
      'construction_pass':construction_pass,
      'q8_values_used':False,
      'C3_enabled':False,
      'inputs':{
        'threshold_beta_g_relative':THRESH,
        'N_g_inverse':NG_INV,
        'h':H,
        'beta_g_N24':float(n24['beta_g']),
      },
      'sensitivity':{
        'K32_abs_d_beta_g_d_F32':k32,
        'K32_finite_difference':k32_fd,
        'relative_difference':sens_rel,
        'check_tolerance':1.0e-8,
        'pass':sensitivity_pass,
        'K0_abs_d_beta_g_d_F0':k0,
      },
      'historical_beta_budget':{
        'allowed_abs_beta_g_change_at_Q6_N24_scale':allowed_beta,
        'local_isolated_F32_budget':budget_f32,
      },
      'observed_Q6_resolution_gap':{
        'F32_N16':float(n16['Flow_G_p32']),
        'F32_N24':float(n24['Flow_G_p32']),
        'abs_F32_N16_to_N24_drift':delta_f32,
        'drift_over_local_budget':ratio_obs,
      },
      'inherited_p0_error_floor':{
        'F0_reconstructed_N16':f0_16,
        'F0_reconstructed_N24':f0_24,
        'abs_F0_N16_to_N24_drift':delta_f0,
        'propagated_abs_beta_g_floor':beta_floor0,
        'floor_over_allowed_beta_change':floor_ratio,
      },
      'interpretation_ceiling':{
        'q8_convergence_established':False,
        'q6_pass_established':False,
        'derivative_regularization_closed':False,
        'physical_C3_established':False,
        'sf055_terminal_pass':False,
      }
    }
    p=Path(a.out); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))
    if not construction_pass:
        raise SystemExit(1)

if __name__=='__main__':
    main()
