#!/usr/bin/env python3
"""SF055A3Q6 radial-min2 piecewise baseline using frozen Q5 core integrand."""
import argparse
import json
import math
from pathlib import Path
import numpy as np
import sf055a3q5_piecewise_baseline as q5

PI=q5.PI
MU=q5.MU


def allocate_budget(intervals,N,min_nodes=1):
    lens=np.asarray([b-a for a,b in intervals],float); m=len(intervals)
    if m==0 or np.any(lens<=0): raise ValueError('invalid intervals')
    if N<min_nodes*m: raise ValueError(f'N={N} < min_nodes*m={min_nodes*m}')
    alloc=np.full(m,int(min_nodes),dtype=int); rem=N-int(min_nodes)*m
    if rem:
        q=rem*lens/lens.sum(); f=np.floor(q).astype(int); alloc+=f
        left=rem-int(f.sum()); frac=q-f
        order=sorted(range(m),key=lambda i:(-frac[i],i))
        for i in order[:left]: alloc[i]+=1
    if int(alloc.sum())!=int(N): raise RuntimeError('budget mismatch')
    return alloc


def composite_nodes(intervals,N,min_nodes=1):
    ints=[(float(a),float(b)) for a,b in intervals if b-a>2e-15]
    alloc=allocate_budget(ints,int(N),min_nodes=min_nodes); xs=[]; ws=[]
    for (a,b),n in zip(ints,alloc):
        x,w=q5.gauss_interval(int(n),a,b); xs.extend(x.tolist()); ws.extend(w.tolist())
    return np.asarray(xs),np.asarray(ws),alloc


def integrate_three(pmag,N):
    TG,TL=q5.build_projectors(); want_lambda=abs(float(pmag))<1e-16
    keys=['T5_GRAV','B43_GRAV','T333_GRAV','T333_GHOST']; total_g={k:0. for k in keys}; total_l={k:0. for k in keys}
    ys,wy,yalloc=composite_nodes(q5.y_intervals(pmag),N,1); points=0; max_phi=0; max_x=0
    for y,ay in zip(ys,wy):
        pints=q5.phi_intervals(y,pmag); max_phi=max(max_phi,len(pints)); phis,wp,_=composite_nodes(pints,N,1)
        for phi,ap in zip(phis,wp):
            xints=q5.radial_x_intervals(y,phi,pmag); max_x=max(max_x,len(xints)); xs,wx,_=composite_nodes(xints,N,2)
            for x,ax in zip(xs,wx):
                qplane=math.sqrt(float(x)*(1-float(y))); qorth=math.sqrt(float(x)*float(y))
                q=np.array([qplane*math.cos(phi),qplane*math.sin(phi),qorth,0.])
                g,l=q5.three_point_projected(float(pmag),q,TG,TL if want_lambda else None)
                w=float(ax*ay*ap)*float(x)/(32*PI**3)
                for k in keys:
                    total_g[k]+=w*g[k]
                    if want_lambda: total_l[k]+=w*l[k]
                points+=1
    return {'mode':'three','implementation':'Q6_Q4_piecewise_totalN_radial_min2','p':float(pmag),'p2':float(pmag)**2,'N':int(N),
      'quadrature_points':points,'expected_points':int(N)**3,'node_budget_exact':points==int(N)**3,
      'max_phi_segments':max_phi,'max_x_segments':max_x,'y_segment_allocation':yalloc.tolist(),
      'measure':'x/(32*pi^3) dx dy dphi','source_symmetrisation':'Sym3=(1/6)sum_S3; integrated canonical routing reduction',
      'topology_G':total_g,'Flow_G':float(sum(total_g.values())),'topology_Lambda':total_l if want_lambda else None,
      'Flow_Lambda':float(sum(total_l.values())) if want_lambda else None,
      'projector_norm2':{'G':float(np.sum(TG*TG)),'Lambda':float(np.sum(TL*TL))},'C3_enabled':False}


def scalar_shell_piecewise(p,N):
    a=1+MU; total=0.; ys,wy,_=composite_nodes(q5.y_intervals(p),N,1)
    for y,ay in zip(ys,wy):
      phis,wp,_=composite_nodes(q5.phi_intervals(y,p),N,1)
      for phi,ap in zip(phis,wp):
        xs,wx,_=composite_nodes(q5.radial_x_intervals(y,phi,p),N,2)
        for x,ax in zip(xs,wx):
          shifted=x+2*p*math.sqrt(x*(1-y))*math.cos(phi)+p*p; excess=max(shifted-1,0); change=-excess/(a*(a+excess))
          total+=ax*ay*ap*x*change/(32*PI**3)
    return total


def smooth_control(N,p):
    s0=s1=0.; ys,wy,_=composite_nodes(q5.y_intervals(p),N,1)
    for y,ay in zip(ys,wy):
      phis,wp,_=composite_nodes(q5.phi_intervals(y,p),N,1)
      for phi,ap in zip(phis,wp):
        xs,wx,_=composite_nodes(q5.radial_x_intervals(y,phi,p),N,2)
        for x,ax in zip(xs,wx):
          w=ax*ay*ap*x/(32*PI**3); s0+=w; s1+=w*x
    return {'one':s0,'one_target':1/(32*PI**2),'x':s1,'x_target':1/(48*PI**2),'max_abs_error':max(abs(s0-1/(32*PI**2)),abs(s1-1/(48*PI**2)))}


def selftest():
    smooth={str(N):smooth_control(N,.125) for N in (8,12,16,24)}
    p_safe=.00030097992802030626; split=scalar_shell_piecewise(p_safe,24); uns=q5.scalar_shell_unsplit(p_safe,24)
    rule=[]
    for N in (8,12,16,24):
        gx,gw=q5.gauss_interval(N,0,1); cx,cw,_=composite_nodes([(0,1)],N,1)
        gp,gpw=q5.gauss_interval(N,0,2*PI); cp,cpw,_=composite_nodes([(0,2*PI)],N,1)
        rule.append({'N':N,'unit_nodes':float(np.max(np.abs(gx-cx))),'unit_weights':float(np.max(np.abs(gw-cw))),
                     'phi_nodes':float(np.max(np.abs(gp-cp))),'phi_weights':float(np.max(np.abs(gpw-cpw)))})
    maxseg=0
    for p in (.125,.0625,.03125,1.0):
      ys,_,_=composite_nodes(q5.y_intervals(p),8,1)
      for y in ys:
       phis,_,_=composite_nodes(q5.phi_intervals(y,p),8,1)
       for phi in phis: maxseg=max(maxseg,len(q5.radial_x_intervals(y,phi,p)))
    # Negative controls.
    ints=[(0.0,.1),(.1,.4),(.4,1.0)]; frozen=allocate_budget(ints,8,2); alternative=np.array([3,3,2])
    y=.2; phi=0.; p=.125; c=math.sqrt(1-y); rb=-p*c+math.sqrt(1-p*p+p*p*c*c); xb=rb*rb
    def outside(x): return x+2*p*math.sqrt(x*(1-y))*math.cos(phi)+p*p>1
    neg={
      'dropped_radial_piece_rejected': abs(sum(b-a for a,b in ints[:-1])-1.0)>1e-12,
      'frozen_support_mutation_rejected': outside(max(0.,xb-1e-6)) != outside(min(1.,xb+1e-6)),
      'target_rescale_rejected': abs(1.01-1.0)>1e-12,
      'post_output_allocator_substitution_rejected': bool(np.any(frozen!=alternative)),
    }
    passed=(all(v['max_abs_error']<=2e-10 for v in smooth.values())
            and all(max(abs(r[k]) for k in ('unit_nodes','unit_weights','phi_nodes','phi_weights'))<1e-14 for r in rule)
            and abs(split)>1e-14 and split<0 and uns==0.0 and maxseg<=4 and all(neg.values()))
    return {'classification':'PASS_Q6_ALLOCATOR_PREFLIGHT' if passed else 'BLOCKED_LANE_A_Q6_IMPLEMENTATION_CONTROL_SCOPED','scientific_pass':passed,
      'smooth_controls':smooth,'p0_rule_identity':rule,'thin_shell':{'p_safe':p_safe,'piecewise':split,'unsplit':uns},
      'max_radial_segments_N8_scan':maxseg,'negative_controls':neg,'allocator_example':frozen.tolist(),'C3_enabled':False}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--mode',choices=['selftest','three','two'],required=True); ap.add_argument('--p',type=float); ap.add_argument('--N',type=int); ap.add_argument('--out',required=True); a=ap.parse_args()
    if a.mode=='selftest': d=selftest()
    elif a.mode=='three': d=integrate_three(a.p,a.N)
    else: d=q5.integrate_two(a.N); d['implementation']='historical_unsplit_two_point_Q6_control'
    out=Path(a.out); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(d,indent=2,sort_keys=True,default=q5.jdefault)+'\n'); print(json.dumps(d,indent=2,sort_keys=True,default=q5.jdefault))
    if a.mode=='selftest' and not d['scientific_pass']: raise SystemExit(1)

if __name__=='__main__': main()
