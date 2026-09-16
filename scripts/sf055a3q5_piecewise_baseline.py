#!/usr/bin/env python3
"""SF055A3Q5 full-tensor piecewise baseline retry.

Implementation-only successor to the original SF055A3 baseline. The physics
integrand is imported unchanged from sf055a3_baseline_quadrature. Only the
three-point reduced integration domain is partitioned at exact Q4 shifted-Litim
surfaces. C3 is disabled.
"""
from __future__ import annotations
import argparse, json, math
from pathlib import Path
import numpy as np
import sf055a3_baseline_quadrature as old

PI=math.pi
ROOT=Path(__file__).resolve().parents[1]
UNIT2=np.array([[1.0,0.0],[-0.5,math.sqrt(3)/2],[-0.5,-math.sqrt(3)/2]],float)
SHIFT_UNITS={
    'ell': UNIT2[0]+UNIT2[1],
    'e23': -UNIT2[1],
    'e31': UNIT2[0],
}


def angle(v): return math.atan2(float(v[1]),float(v[0]))%(2*PI)
ALPHAS={k:angle(v) for k,v in SHIFT_UNITS.items()}


def gauss(n,a,b):
    z,w=np.polynomial.legendre.leggauss(int(n))
    return .5*(b-a)*z+.5*(a+b), .5*(b-a)*w


def cval(y,phi,alpha):
    return math.sqrt(max(0.0,1.0-float(y)))*math.cos(float(phi)-float(alpha))


def active(p,c): return float(p)>0 and float(c)>-float(p)/2


def rb_root(p,c):
    p=float(p); c=float(c)
    disc=1-p*p+p*p*c*c
    if disc < -2e-13: raise ValueError('negative shifted-sphere discriminant')
    return -p*c+math.sqrt(max(0.0,disc))


def uniq(vals,tol=5e-13):
    out=[]
    for v in sorted(float(x) for x in vals):
        if -1e-12<=v<=1+1e-12: v=min(1.0,max(0.0,v))
        if not out or abs(v-out[-1])>tol: out.append(v)
    return out


def phi_breaks(y,p):
    vals=[0.0,2*PI]
    p=float(p); y=float(y)
    if p<=0: return vals
    s=math.sqrt(max(0.0,1-y))
    if s>0 and s+1e-15>=p/2:
        beta=math.acos(max(-1.0,min(1.0,-p/(2*s))))
        for alpha in ALPHAS.values():
            for v in ((alpha-beta)%(2*PI),(alpha+beta)%(2*PI)):
                if 1e-13<v<2*PI-1e-13: vals.append(v)
    return uniq(vals,tol=5e-12)


def x_breaks(y,phi,p):
    vals=[0.0,1.0]
    for alpha in ALPHAS.values():
        c=cval(y,phi,alpha)
        if active(p,c):
            r=rb_root(p,c)
            if -1e-12<=r<=1+1e-12: vals.append(r*r)
    return uniq(vals)


def shifted_sq(r,y,phi,p,u):
    n2=np.array([math.sqrt(max(0.0,1-y))*math.cos(phi),math.sqrt(max(0.0,1-y))*math.sin(phi)])
    return r*r+p*p+2*r*p*float(np.dot(n2,u))


def partition_controls():
    maxroot=0.0; intervals=0; coverage=0.0; constant=True
    for p in (1/8,1/16,1/32,1.0):
        ystar=1-p*p/4
        ytests=[.07,.31,.73,min(.999,max(0.0,ystar-.01)),min(.999,ystar+.005)]
        for y in ytests:
            for pa,pb in zip(phi_breaks(y,p)[:-1],phi_breaks(y,p)[1:]):
                if pb-pa<1e-12: continue
                ph=pa+.43*(pb-pa)
                br=x_breaks(y,ph,p)
                coverage=max(coverage,abs(sum(b-a for a,b in zip(br[:-1],br[1:]))-1))
                for xa,xb in zip(br[:-1],br[1:]):
                    if xb-xa<1e-13: continue
                    bits=[]
                    for t in (.2,.5,.8):
                        x=xa+t*(xb-xa); r=math.sqrt(max(0.0,x))
                        bits.append(tuple(shifted_sq(r,y,ph,p,u)>1 for u in SHIFT_UNITS.values()))
                    constant &= all(z==bits[0] for z in bits)
                    intervals+=1
        for y in (.03,.4,.85):
            for ph in (.17,1.13,2.71,5.33):
                for u in SHIFT_UNITS.values():
                    c=cval(y,ph,angle(u))
                    if active(p,c):
                        r=rb_root(p,c)
                        if 0<=r<=1: maxroot=max(maxroot,abs(shifted_sq(r,y,ph,p,u)-1))
    return {'max_root_residual':maxroot,'coverage_error':coverage,'constant_support_bits':bool(constant),'intervals_tested':intervals,
            'pass':bool(maxroot<=2e-12 and coverage<=2e-13 and constant)}


def integrate_three_piecewise(pmag,N):
    p=float(pmag); N=int(N)
    TG,TL=old.build_projectors(); want_lambda=abs(p)<1e-16
    keys=['T5_GRAV','B43_GRAV','T333_GRAV','T333_GHOST']
    total_g={k:0.0 for k in keys}; total_l={k:0.0 for k in keys}
    points=0; radial_intervals=0; phi_intervals=0; y_intervals=0
    ystar=1-p*p/4 if p>0 else 1.0
    ybr=[0.0,ystar,1.0] if 1e-14<ystar<1-1e-14 else [0.0,1.0]
    for ya,yb in zip(ybr[:-1],ybr[1:]):
        if yb-ya<1e-14: continue
        y_intervals+=1
        ys,wy=gauss(N,ya,yb)
        for y,ay in zip(ys,wy):
            pbr=phi_breaks(float(y),p)
            for pa,pb in zip(pbr[:-1],pbr[1:]):
                if pb-pa<1e-13: continue
                phi_intervals+=1
                phs,wp=gauss(N,pa,pb)
                for phi,ap in zip(phs,wp):
                    xbr=x_breaks(float(y),float(phi),p)
                    for xa,xb in zip(xbr[:-1],xbr[1:]):
                        if xb-xa<1e-14: continue
                        radial_intervals+=1
                        xs,wx=gauss(N,xa,xb)
                        pref=float(ay*ap)/(32*PI**3)
                        for x,ax in zip(xs,wx):
                            qplane=math.sqrt(float(x)*(1-float(y)))
                            qorth=math.sqrt(float(x)*float(y))
                            q=np.array([qplane*math.cos(phi),qplane*math.sin(phi),qorth,0.0])
                            g,l=old.three_point_projected(p,q,TG,TL if want_lambda else None)
                            weight=pref*float(ax)*float(x)
                            for k in keys:
                                total_g[k]+=weight*g[k]
                                if want_lambda: total_l[k]+=weight*l[k]
                            points+=1
    return {'mode':'three','implementation':'Q5_exact_Q4_piecewise_partition','p':p,'p2':p*p,'N':N,
      'quadrature_points':points,'partition_counts':{'y_intervals':y_intervals,'phi_intervals_over_nodes':phi_intervals,'radial_intervals_over_nodes':radial_intervals},
      'measure':'x/(32*pi^3) dx dy dphi','source_symmetrisation':'Sym3=(1/6)sum_S3; exact integrated canonical reduction retained',
      'topology_G':total_g,'Flow_G':float(sum(total_g.values())),'topology_Lambda':total_l if want_lambda else None,
      'Flow_Lambda':float(sum(total_l.values())) if want_lambda else None,
      'projector_norm2':{'G':float(np.sum(TG*TG)),'Lambda':float(np.sum(TL*TL))},'C3_enabled':False}


def smooth_controls(p=1/8,N=8):
    sums=[0.0,0.0]; ystar=1-p*p/4; ybr=[0.,ystar,1.]
    for ya,yb in zip(ybr[:-1],ybr[1:]):
        ys,wy=gauss(N,ya,yb)
        for y,ay in zip(ys,wy):
            br=phi_breaks(float(y),p)
            for pa,pb in zip(br[:-1],br[1:]):
                phs,wp=gauss(N,pa,pb)
                for phi,ap in zip(phs,wp):
                    xb=x_breaks(float(y),float(phi),p)
                    for xa,xx in zip(xb[:-1],xb[1:]):
                        xs,wx=gauss(N,xa,xx); pref=float(ay*ap)/(32*PI**3)
                        sums[0]+=pref*float(np.dot(wx,xs)); sums[1]+=pref*float(np.dot(wx,xs*xs))
    targets=[1/(32*PI**2),1/(48*PI**2)]
    return {'computed':sums,'analytic':targets,'abs_error':[abs(a-b) for a,b in zip(sums,targets)],'pass':max(abs(a-b) for a,b in zip(sums,targets))<=3e-12}


def scalar_shell_piecewise(p,N,mu=.1):
    total=0.0; ystar=1-p*p/4; ybr=[0.,ystar,1.] if 0<ystar<1 else [0.,1.]
    for ya,yb in zip(ybr[:-1],ybr[1:]):
        ys,wy=gauss(N,ya,yb)
        for y,ay in zip(ys,wy):
            # one canonical shift only, alpha=0, for Q4 scalar regression
            vals=[0.,2*PI]; s=math.sqrt(max(0.,1-y))
            if s>0 and s+1e-15>=p/2:
                beta=math.acos(max(-1.,min(1.,-p/(2*s))))
                for v in ((-beta)%(2*PI),(beta)%(2*PI)):
                    if 1e-13<v<2*PI-1e-13: vals.append(v)
            vals=sorted(set(vals))
            for pa,pb in zip(vals[:-1],vals[1:]):
                phs,wp=gauss(N,pa,pb)
                for phi,ap in zip(phs,wp):
                    c=cval(float(y),float(phi),0.0)
                    if not active(p,c): continue
                    rb=rb_root(p,c); xa=max(0.,min(1.,rb*rb))
                    if xa>=1-1e-15: continue
                    xs,wx=gauss(N,xa,1.); r=np.sqrt(xs); shifted=xs+p*p+2*p*r*c; ex=shifted-1; a=1+mu
                    total+=float(ay*ap)*float(np.dot(wx,xs*(-ex/(a*(a+ex)))))/(32*PI**3)
    return total


def equivalence_controls():
    parent=old.selftest(); part=partition_controls(); smooth=smooth_controls(1/8,8)
    p0=[]
    for N in (8,12):
        uns=old.integrate_three(0.0,N); pw=integrate_three_piecewise(0.0,N)
        p0.append({'N':N,'unsplit_G':uns['Flow_G'],'piecewise_G':pw['Flow_G'],'abs_G':abs(uns['Flow_G']-pw['Flow_G']),
          'unsplit_Lambda':uns['Flow_Lambda'],'piecewise_Lambda':pw['Flow_Lambda'],'abs_Lambda':abs(uns['Flow_Lambda']-pw['Flow_Lambda']),
          'pass':abs(uns['Flow_G']-pw['Flow_G'])<=2e-10 and abs(uns['Flow_Lambda']-pw['Flow_Lambda'])<=2e-10})
    q4refs={1/8:-1.976210890335743e-05,1/32:-1.2673470664854288e-06}
    scalar=[]
    for p,ref in q4refs.items():
        val=scalar_shell_piecewise(p,24); scalar.append({'p':p,'computed':val,'Q4_reference':ref,'relative_difference':abs(val-ref)/abs(ref),'pass':abs(val-ref)/abs(ref)<=2e-6})
    passed=bool(parent['pass'] and part['pass'] and smooth['pass'] and all(x['pass'] for x in p0) and all(x['pass'] for x in scalar))
    return {'classification':'PASS_Q5_PIECEWISE_FULL_TENSOR_IMPLEMENTATION_EQUIVALENCE_SCOPED' if passed else 'INVALID_OR_BLOCKED_Q5_PIECEWISE_IMPLEMENTATION',
      'parent_selftest':parent,'partition':part,'smooth':smooth,'p0_tensor_product_equivalence':p0,'scalar_Q4_regression':scalar,
      'C3_enabled':False,'science_matrix_evaluated':False,'pass':passed}


def jdefault(x):
    if isinstance(x,np.bool_): return bool(x)
    if isinstance(x,np.integer): return int(x)
    if isinstance(x,np.floating): return float(x)
    if isinstance(x,np.ndarray): return x.tolist()
    raise TypeError(type(x).__name__)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--mode',choices=['equivalence','three','two','selftest'],required=True)
    ap.add_argument('--N',type=int); ap.add_argument('--p',type=float,default=0.0); ap.add_argument('--out',required=True)
    args=ap.parse_args()
    if args.mode=='equivalence': result=equivalence_controls()
    elif args.mode=='selftest': result=old.selftest()
    elif args.mode=='two':
        if args.N is None: raise SystemExit('--N required')
        result=old.integrate_two(args.N); result['implementation']='Q5_two_point_unchanged_original'
    else:
        if args.N is None: raise SystemExit('--N required')
        result=integrate_three_piecewise(args.p,args.N)
    path=ROOT/args.out; path.parent.mkdir(parents=True,exist_ok=True)
    text=json.dumps(result,indent=2,sort_keys=True,default=jdefault)+'\n'; path.write_text(text); print(text,end='')
    if args.mode=='equivalence' and not result['pass']: raise SystemExit(1)

if __name__=='__main__': main()
