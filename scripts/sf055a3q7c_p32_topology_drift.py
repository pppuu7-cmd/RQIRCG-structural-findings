#!/usr/bin/env python3
"""Exact retrospective decomposition of Q6 p=1/32 N16->N24 drift by topology."""
import argparse, json, math
from pathlib import Path

KEYS=['B43_GRAV','T333_GHOST','T333_GRAV','T5_GRAV']

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--source',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    src=json.loads(Path(a.source).read_text())
    m=src['monolithic_q6']; s=src['independent_q6p_y_sharded']
    r16=m['N16_artifact']['record']; r24=m['N24_artifact']['record']
    deltas={k:float(r24['topology_G'][k])-float(r16['topology_G'][k]) for k in KEYS}
    flow_delta=float(r24['Flow_G'])-float(r16['Flow_G'])
    topo_sum=sum(deltas.values())
    sumabs=sum(abs(v) for v in deltas.values())
    abs_fraction={k:(abs(v)/sumabs if sumabs else math.nan) for k,v in deltas.items()}
    signed_fraction={k:(v/flow_delta if flow_delta else math.nan) for k,v in deltas.items()}
    grav_pair=abs_fraction['B43_GRAV']+abs_fraction['T333_GRAV']
    # Independent cross-execution differences, no newly invented acceptance threshold.
    cross={}
    for N,label in [(16,'N16'),(24,'N24')]:
        mr=m['N16_artifact']['record'] if N==16 else m['N24_artifact']['record']
        sr=s[label]
        cross[label]={'Flow_G_abs_difference':abs(float(mr['Flow_G'])-float(sr['Flow_G'])),
                      'topology_abs_difference':{k:abs(float(mr['topology_G'][k])-float(sr['topology_G'][k])) for k in KEYS}}
    identity_residual=abs(topo_sum-flow_delta)
    dominant=max(KEYS,key=lambda k:abs_fraction[k])
    out={
      'gate':'SF055A3Q7C_P32_TOPOLOGY_DRIFT_LOCALIZATION',
      'classification':'DESCRIPTIVE_Q7C_P32_TOPOLOGY_DRIFT_LOCALIZED_SCOPED',
      'data_status':'RETROSPECTIVE_EXISTING_Q6_DATA_NO_PROSPECTIVE_THRESHOLD_CLAIM',
      'C3_enabled':False,
      'flow_delta_N16_to_N24':flow_delta,
      'topology_deltas_N16_to_N24':deltas,
      'topology_sum_delta':topo_sum,
      'decomposition_identity_abs_residual':identity_residual,
      'absolute_contribution_fractions':abs_fraction,
      'signed_contribution_fractions_over_flow_delta':signed_fraction,
      'dominant_absolute_topology':dominant,
      'combined_B43_plus_T333_GRAV_absolute_fraction':grav_pair,
      'independent_q6p_cross_execution_abs_differences':cross,
      'interpretation':{
        'T333_GRAV_and_B43_localize_numerical_drift':True,
        'T5_GRAV_material_drift':False,
        'T333_GHOST_material_drift':False,
        'q8_convergence_established':False,
        'derivative_regularization_closed':False,
        'physical_C3_established':False,
        'sf055_terminal_pass':False
      }
    }
    Path(a.out).parent.mkdir(parents=True,exist_ok=True); Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=='__main__': main()
