#!/usr/bin/env python3
"""Deterministic y-shard execution for the frozen SF055A3Q6 quadrature."""
import argparse
import json
import math
from pathlib import Path
import numpy as np
import sf055a3q6_piecewise_baseline as q6
import sf055a3q5_piecewise_baseline as q5

PI=q5.PI
KEYS=['T5_GRAV','B43_GRAV','T333_GRAV','T333_GHOST']


def shard(pmag,N,shard_id,nshards):
    if not (0 <= shard_id < nshards): raise ValueError('bad shard id')
    TG,TL=q5.build_projectors(); want_lambda=abs(float(pmag))<1e-16
    total_g={k:0.0 for k in KEYS}; total_l={k:0.0 for k in KEYS}
    ys,wy,yalloc=q6.composite_nodes(q5.y_intervals(pmag),N,1)
    inds=[i for i in range(int(N)) if i % int(nshards)==int(shard_id)]
    points=0; max_phi=0; max_x=0
    for i in inds:
        y=float(ys[i]); ay=float(wy[i])
        pints=q5.phi_intervals(y,pmag); max_phi=max(max_phi,len(pints)); phis,wp,_=q6.composite_nodes(pints,N,1)
        for phi,ap in zip(phis,wp):
            xints=q5.radial_x_intervals(y,float(phi),pmag); max_x=max(max_x,len(xints)); xs,wx,_=q6.composite_nodes(xints,N,2)
            for x,ax in zip(xs,wx):
                qplane=math.sqrt(float(x)*(1-y)); qorth=math.sqrt(float(x)*y)
                q=np.array([qplane*math.cos(float(phi)),qplane*math.sin(float(phi)),qorth,0.0])
                g,l=q5.three_point_projected(float(pmag),q,TG,TL if want_lambda else None)
                w=float(ax)*ay*float(ap)*float(x)/(32.0*PI**3)
                for k in KEYS:
                    total_g[k]+=w*g[k]
                    if want_lambda: total_l[k]+=w*l[k]
                points+=1
    return {'mode':'q6p_shard','p':float(pmag),'N':int(N),'shard_id':int(shard_id),'nshards':int(nshards),
            'y_indices':inds,'quadrature_points':points,'topology_G':total_g,'Flow_G':float(sum(total_g.values())),
            'topology_Lambda':total_l if want_lambda else None,'Flow_Lambda':float(sum(total_l.values())) if want_lambda else None,
            'max_phi_segments':max_phi,'max_x_segments':max_x,'C3_enabled':False}


def merge(records):
    if not records: raise ValueError('no records')
    recs=sorted(records,key=lambda r:int(r['shard_id']))
    p=float(recs[0]['p']); N=int(recs[0]['N']); S=int(recs[0]['nshards'])
    if len(recs)!=S or [int(r['shard_id']) for r in recs] != list(range(S)):
        raise ValueError('incomplete shard-id coverage')
    if any(float(r['p'])!=p or int(r['N'])!=N or int(r['nshards'])!=S for r in recs):
        raise ValueError('inconsistent shard metadata')
    inds=[i for r in recs for i in r['y_indices']]
    coverage=(sorted(inds)==list(range(N)) and len(set(inds))==N)
    if not coverage: raise ValueError('y-index coverage failure')
    tg={k:0.0 for k in KEYS}; tl={k:0.0 for k in KEYS}; have_l=recs[0]['topology_Lambda'] is not None
    for r in recs:
        for k in KEYS:
            tg[k]+=float(r['topology_G'][k])
            if have_l: tl[k]+=float(r['topology_Lambda'][k])
    return {'mode':'three','implementation':'Q6P_y_sharded_Q6','p':p,'p2':p*p,'N':N,
            'quadrature_points':sum(int(r['quadrature_points']) for r in recs),'expected_points':N**3,
            'node_budget_exact':sum(int(r['quadrature_points']) for r in recs)==N**3,
            'y_coverage_exact':coverage,'nshards':S,'topology_G':tg,'Flow_G':float(sum(tg.values())),
            'topology_Lambda':tl if have_l else None,'Flow_Lambda':float(sum(tl.values())) if have_l else None,
            'max_phi_segments':max(int(r['max_phi_segments']) for r in recs),'max_x_segments':max(int(r['max_x_segments']) for r in recs),
            'measure':'x/(32*pi^3) dx dy dphi','C3_enabled':False}


def selftest(outdir):
    outdir=Path(outdir); outdir.mkdir(parents=True,exist_ok=True)
    serial=q6.integrate_three(0.125,8)
    shards=[]
    for s in range(2):
        r=shard(0.125,8,s,2); shards.append(r); (outdir/f'shard{s}.json').write_text(json.dumps(r,indent=2,sort_keys=True,default=q5.jdefault)+'\n')
    merged=merge(shards)
    errs={'Flow_G':abs(merged['Flow_G']-serial['Flow_G'])}
    for k in KEYS: errs[k]=abs(merged['topology_G'][k]-serial['topology_G'][k])
    tol={k:5e-12*(1+abs(serial['Flow_G'] if k=='Flow_G' else serial['topology_G'][k])) for k in errs}
    positive=all(errs[k]<=tol[k] for k in errs) and merged['node_budget_exact'] and merged['y_coverage_exact']
    drop_rejected=False; duplicate_rejected=False
    try: merge(shards[:1])
    except ValueError: drop_rejected=True
    bad=[dict(shards[0]),dict(shards[1])]; bad[1]['y_indices']=bad[0]['y_indices']
    try: merge(bad)
    except ValueError: duplicate_rejected=True
    passed=positive and drop_rejected and duplicate_rejected
    return {'classification':'PASS_Q6P_Y_SHARD_EXECUTION_EQUIVALENCE_SCOPED' if passed else 'BLOCKED_Q6P_EXECUTION_EQUIVALENCE_SCOPED',
            'scientific_pass':passed,'errors':errs,'limits':tol,'serial':serial,'merged':merged,
            'negative_controls':{'dropped_shard_rejected':drop_rejected,'duplicate_indices_rejected':duplicate_rejected},'C3_enabled':False}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--mode',choices=['shard','merge','selftest'],required=True); ap.add_argument('--p',type=float); ap.add_argument('--N',type=int); ap.add_argument('--shard-id',type=int); ap.add_argument('--nshards',type=int); ap.add_argument('--inputs',nargs='*'); ap.add_argument('--out',required=True); a=ap.parse_args()
    if a.mode=='shard': d=shard(a.p,a.N,a.shard_id,a.nshards)
    elif a.mode=='merge': d=merge([json.loads(Path(x).read_text()) for x in a.inputs])
    else: d=selftest(Path(a.out).parent/'q6p_selftest_parts')
    out=Path(a.out); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(d,indent=2,sort_keys=True,default=q5.jdefault)+'\n'); print(json.dumps(d,indent=2,sort_keys=True,default=q5.jdefault))
    if a.mode=='selftest' and not d['scientific_pass']: raise SystemExit(1)
if __name__=='__main__': main()
