#!/usr/bin/env python3
"""Run the frozen Q5 aggregate logic and relabel only for the prospectively frozen Q6 gate."""
import argparse
import json
import subprocess
import sys
from pathlib import Path

MAP={
 'BLOCKED_LANE_A_PIECEWISE_IMPLEMENTATION_CONTROL_SCOPED':'BLOCKED_LANE_A_Q6_IMPLEMENTATION_CONTROL_SCOPED',
 'BLOCKED_LANE_A_PIECEWISE_BASELINE_QUADRATURE_NOT_CONVERGED_SCOPED':'BLOCKED_LANE_A_Q6_PIECEWISE_BASELINE_NOT_CONVERGED_SCOPED',
 'BLOCKED_LANE_A_PIECEWISE_FINITE_DIFFERENCE_CONTROL_SCOPED':'BLOCKED_LANE_A_Q6_FINITE_DIFFERENCE_CONTROL_SCOPED',
 'FAIL_LANE_A_PIECEWISE_BASELINE_REPRODUCTION_SCOPED':'FAIL_LANE_A_Q6_PIECEWISE_BASELINE_REPRODUCTION_SCOPED',
 'PASS_LANE_A_PIECEWISE_BASELINE_REPRODUCTION_SCOPED':'PASS_LANE_A_Q6_PIECEWISE_BASELINE_REPRODUCTION_SCOPED',
}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); ap.add_argument('--historical',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    tmp=Path(a.out).with_suffix('.q5tmp.json')
    cmd=[sys.executable,str(Path(__file__).with_name('sf055a3q5_piecewise_aggregate.py')),'--root',a.root,'--historical',a.historical,'--out',str(tmp)]
    subprocess.run(cmd,check=False)
    if not tmp.exists(): raise SystemExit('Q5 aggregate logic produced no output')
    d=json.loads(tmp.read_text()); old=d.get('classification'); d['classification_source_logic']=old; d['classification']=MAP.get(old,old)
    d['gate']='SF055A3Q6_RADIAL_MIN2_PIECEWISE_BASELINE'; d['q6_radial_min2']=True; d['sf055_terminal_pass']=False; d['hard_stop_before_C3']=True
    out=Path(a.out); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(d,indent=2,sort_keys=True)+'\n'); print(json.dumps(d,indent=2,sort_keys=True))
    tmp.unlink(missing_ok=True)
    if not d.get('scientific_pass',False): raise SystemExit(1)
if __name__=='__main__': main()
