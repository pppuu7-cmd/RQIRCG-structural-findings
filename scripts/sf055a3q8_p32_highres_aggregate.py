#!/usr/bin/env python3
"""Aggregate prospectively frozen SF055A3Q8 p=1/32 high-resolution results."""
import argparse
import json
import math
from pathlib import Path

H=1.0/32.0
F0=0.0005562382414400815
F16=0.0005465706425780851
NG_INV=0.00052874519051635
NG=1.0/NG_INV
DF0_FLOOR=2.9895975343745274e-11
EXPECTED={32,40,48}


def load(root):
    recs={}
    for p in Path(root).rglob('*.json'):
        try: d=json.loads(p.read_text())
        except Exception: continue
        if d.get('mode')=='three' and abs(float(d.get('p',-1))-H)<1e-15 and int(d.get('N',-1)) in EXPECTED:
            recs[int(d['N'])]=d
    return recs


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--root',required=True); ap.add_argument('--out',required=True); a=ap.parse_args()
    recs=load(a.root); missing=sorted(EXPECTED-set(recs))
    out={'gate':'SF055A3Q8_P32_HIGH_RESOLUTION_DERIVATIVE_CONVERGENCE_AND_ERROR_BUDGET',
         'preregistration_commit':'47121c499fc036a6e0723f6c52266cae1c809207',
         'C3_enabled':False,'missing':missing}
    if missing:
        out.update({'classification':'INVALID_Q8_P32_HIGH_RESOLUTION_PROVENANCE_OR_CONTROL_SCOPED','scientific_pass':False})
    else:
        controls={}
        rows={}
        d16_anchor=(F16-F0)/((1.0/16.0)**2)
        for N in sorted(EXPECTED):
            r=recs[N]
            ctrl=(r.get('node_budget_exact') is True and r.get('y_coverage_exact') is True and
                  int(r.get('N',-1))==N and abs(float(r.get('p',-1))-H)<1e-15 and
                  r.get('C3_enabled') is False and math.isfinite(float(r.get('Flow_G'))))
            controls[str(N)]=bool(ctrl)
            f32=float(r['Flow_G'])
            d32=(f32-F0)/(H*H)
            ranchor=(4.0*d32-d16_anchor)/3.0
            bg=2.0+2.0*NG*ranchor
            rows[str(N)]={'Flow_G_p32':f32,'D32':d32,'D16_anchor':d16_anchor,'R_anchor':ranchor,'beta_g_anchor':bg,
                          'node_budget_exact':r.get('node_budget_exact'),'y_coverage_exact':r.get('y_coverage_exact'),
                          'nshards':r.get('nshards'),'quadrature_points':r.get('quadrature_points')}
        provenance=all(controls.values())
        b32=rows['32']['beta_g_anchor']; b40=rows['40']['beta_g_anchor']; b48=rows['48']['beta_g_anchor']
        i1=abs(b40-b32); i2=abs(b48-b40); rel=i2/abs(b48) if b48!=0 else math.inf
        conv=rel<=0.002; monotone=i2<=i1
        # d beta_g / dF0 with F16 and F32 held fixed in the anchored diagnostic.
        coeff_dR_dF0=(4.0*(-1.0/(H*H)) - (-1.0/((1.0/16.0)**2)))/3.0
        bg_floor=abs(2.0*NG*coeff_dR_dF0*DF0_FLOOR)
        out.update({'controls':controls,'provenance_controls_pass':provenance,'rows':rows,
                    'successive_beta_g_anchor_increments':{'N32_to_N40':i1,'N40_to_N48':i2},
                    'rel_40_48':rel,'threshold':0.002,'criterion_rel_pass':conv,
                    'criterion_nonincreasing_increment_pass':monotone,
                    'p0_inherited_error_floor':{'abs_Delta_F0_N16_N24':DF0_FLOOR,'propagated_abs_beta_g_anchor_floor':bg_floor}})
        if not provenance:
            cl='INVALID_Q8_P32_HIGH_RESOLUTION_PROVENANCE_OR_CONTROL_SCOPED'; passed=False
        elif conv and monotone:
            cl='PASS_Q8_P32_HIGH_RESOLUTION_NUMERICAL_CONVERGENCE_SCOPED'; passed=True
        else:
            cl='BLOCKED_Q8_P32_HIGH_RESOLUTION_NUMERICAL_CONVERGENCE_SCOPED'; passed=False
        out.update({'classification':cl,'scientific_pass':passed,'q6_verdict_rewritten':False,
                    'derivative_truncation_regularization_closure':False,'sf055_terminal_pass':False})
    Path(a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(a.out).write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
    print(json.dumps(out,indent=2,sort_keys=True))
    if not out.get('scientific_pass',False): raise SystemExit(1)

if __name__=='__main__': main()
