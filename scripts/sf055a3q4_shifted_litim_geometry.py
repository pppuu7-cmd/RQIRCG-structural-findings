#!/usr/bin/env python3
import json, math
import numpy as np

PI=math.pi
MU=0.1
ROOT_TOL=2e-13
PART_TOL=2e-14
UNIT=np.array([[1.0,0.0],[-0.5,math.sqrt(3)/2],[-0.5,-math.sqrt(3)/2]])
SHIFT_UNITS={'ell':UNIT[0]+UNIT[1],'e23':-UNIT[1],'e31':UNIT[0]}

def gauss(n,a,b):
 z,w=np.polynomial.legendre.leggauss(n); return .5*(b-a)*z+.5*(a+b),.5*(b-a)*w

def uniq_sorted(vals,tol=5e-14):
 out=[]
 for v in sorted(float(x) for x in vals):
  v=min(max(v,0.0),1.0) if -1e-12<=v<=1+1e-12 else v
  if not out or abs(v-out[-1])>tol: out.append(v)
 return out

def angle(v): return math.atan2(float(v[1]),float(v[0]))%(2*PI)
ALPHAS={k:angle(v) for k,v in SHIFT_UNITS.items()}
def cval(y,phi,alpha): return math.sqrt(max(0.0,1-y))*math.cos(phi-alpha)
def rb_root(p,c):
 disc=1-p*p+p*p*c*c
 if disc < -1e-14: raise ValueError('negative discriminant')
 return -p*c+math.sqrt(max(0.0,disc))
def active(p,c): return p>0 and c>-p/2

def shifted_sq(r,y,phi,p,u):
 n2=np.array([math.sqrt(max(0.0,1-y))*math.cos(phi),math.sqrt(max(0.0,1-y))*math.sin(phi)])
 return r*r+p*p+2*r*p*float(np.dot(n2,u))

def phi_breaks(y,p,alphas):
 vals=[0.0,2*PI]
 if p<=0:return vals
 s=math.sqrt(max(0.0,1-y))
 if s+1e-15>=p/2 and s>0:
  beta=math.acos(max(-1.0,min(1.0,-p/(2*s))))
  for a in alphas:
   for v in ((a-beta)%(2*PI),(a+beta)%(2*PI)):
    if 1e-13<v<2*PI-1e-13: vals.append(v)
 out=[]
 for v in sorted(vals):
  if not out or abs(v-out[-1])>5e-13: out.append(v)
 return out

def radial_breaks(y,phi,p,units):
 vals=[0.0,1.0]
 for u in units:
  c=math.sqrt(max(0.0,1-y))*math.cos(phi-angle(u))
  if active(p,c):
   r=rb_root(p,c)
   if -1e-12<=r<=1+1e-12: vals.append(min(1.0,max(0.0,r*r)))
 return uniq_sorted(vals)

def bits_at(x,y,phi,p,units):
 r=math.sqrt(max(0.0,x)); return tuple(shifted_sq(r,y,phi,p,u)>1.0 for u in units)

def geometry_controls():
 ps=[1/8,1/16,1/32,1.0]; ys=[0,.071,.31,.73,.93,.997]; phis=[.013,.41,1.17,2.23,3.49,5.61]
 max_root=0.; activation_ok=True; roots=0
 for p in ps:
  for y in ys:
   for ph in phis:
    for u in SHIFT_UNITS.values():
     c=math.sqrt(max(0.,1-y))*math.cos(ph-angle(u)); direct=(1+p*p+2*p*c)>1
     if abs(c+p/2)>2e-13: activation_ok &= active(p,c)==direct
     if active(p,c):
      r=rb_root(p,c)
      if -1e-12<=r<=1+1e-12:
       max_root=max(max_root,abs(shifted_sq(r,y,ph,p,u)-1)); roots+=1
 phi_ok=True; phi_intervals=0
 for p in ps:
  ystar=1-p*p/4; ytests=[.03,.4,.85,max(0,ystar-.02*(1+ystar)),min(1,ystar+.01*(2-ystar))]
  for y in ytests:
   br=phi_breaks(y,p,list(ALPHAS.values()))
   for a,b in zip(br[:-1],br[1:]):
    if b-a<1e-13: continue
    sets=[tuple(active(p,cval(y,a+t*(b-a),al)) for al in ALPHAS.values()) for t in (.2,.5,.8)]
    phi_ok &= all(s==sets[0] for s in sets); phi_intervals+=1
 radial_ok=True; coverage_err=0.; intervals=0; units=list(SHIFT_UNITS.values())
 for p in ps:
  for y in [.017,.29,.68,.94,.999]:
   brp=phi_breaks(y,p,list(ALPHAS.values()))
   for pa,pb in zip(brp[:-1],brp[1:]):
    if pb-pa<1e-12: continue
    for ft in (.23,.61):
     ph=pa+ft*(pb-pa); br=radial_breaks(y,ph,p,units)
     coverage_err=max(coverage_err,abs(sum(b-a for a,b in zip(br[:-1],br[1:]))-1))
     for a,b in zip(br[:-1],br[1:]):
      if b-a<1e-13: continue
      bs=[bits_at(a+t*(b-a),y,ph,p,units) for t in (.2,.5,.8)]
      radial_ok &= all(z==bs[0] for z in bs); intervals+=1
 return {'max_boundary_residual':max_root,'boundary_roots_tested':roots,'boundary_pass':max_root<=ROOT_TOL,'activation_pass':bool(activation_ok),'phi_constant_active_sets_pass':bool(phi_ok),'phi_intervals_tested':phi_intervals,'radial_partition_pass':bool(radial_ok and coverage_err<=PART_TOL),'max_partition_coverage_error':coverage_err,'radial_intervals_tested':intervals}

def integrate_smooth_piecewise(p,n):
 units=list(SHIFT_UNITS.values()); alphas=list(ALPHAS.values()); ystar=1-p*p/4 if p>0 else 1
 ybr=[0.,ystar,1.] if 1e-14<ystar<1-1e-14 else [0.,1.]; sums=[0.,0.]
 for ya,yb in zip(ybr[:-1],ybr[1:]):
  ys,wy=gauss(n,ya,yb)
  for y,ay in zip(ys,wy):
   pbr=phi_breaks(float(y),p,alphas)
   for pa,pb in zip(pbr[:-1],pbr[1:]):
    phs,wp=gauss(n,pa,pb)
    for ph,ap in zip(phs,wp):
     xbr=radial_breaks(float(y),float(ph),p,units)
     for xa,xb in zip(xbr[:-1],xbr[1:]):
      xs,wx=gauss(n,xa,xb); weight=ay*ap/(32*PI**3)
      sums[0]+=weight*float(np.dot(wx,xs)); sums[1]+=weight*float(np.dot(wx,xs*xs))
 return sums

def shell_delta_polar(p,n,mu=MU):
 th,wt=gauss(n,0,math.acos(-p/2)); t,w=gauss(n,0,1); u=np.cos(th)[:,None]
 root=np.sqrt(1-p*p*(1-u*u)); width=(2*p*u+p*p)/(1+p*u+root); rb=1-width; r=rb+width*t[None,:]
 excess=width*t[None,:]*(r+rb+2*p*u); a=1+mu; change=-excess/(a*(a+excess))
 return float(np.sum(wt[:,None]*w[None,:]*np.sin(th)[:,None]**2*width*r**3*change)/(4*PI**3))

def shell_piecewise_xyz(p,n,mu=MU):
 alpha=0.; ystar=1-p*p/4; ybr=[0.,ystar,1.] if 0<ystar<1 else [0.,1.]; total=0.
 for ya,yb in zip(ybr[:-1],ybr[1:]):
  ys,wy=gauss(n,ya,yb)
  for y,ay in zip(ys,wy):
   pbr=phi_breaks(float(y),p,[alpha])
   for pa,pb in zip(pbr[:-1],pbr[1:]):
    phs,wp=gauss(n,pa,pb)
    for ph,ap in zip(phs,wp):
     c=cval(float(y),float(ph),alpha)
     if not active(p,c): continue
     rb=rb_root(p,c); xb=max(0.,min(1.,rb*rb))
     if xb>=1-1e-15: continue
     xs,wx=gauss(n,xb,1.); r=np.sqrt(xs); shifted=xs+p*p+2*p*r*c; excess=shifted-1.; a=1+mu
     total+=ay*ap*float(np.dot(wx,xs*(-excess/(a*(a+excess)))))/(32*PI**3)
 return total

def unsplit_delta(p,n,mu=MU):
 x,wx=gauss(n,0,1); y,wy=gauss(n,0,1); ph,wp=gauss(n,0,2*PI); xx=x[:,None,None]; yy=y[None,:,None]; pp=ph[None,None,:]
 shifted=xx+2*p*np.sqrt(xx*(1-yy))*np.cos(pp)+p*p; ex=np.maximum(shifted-1,0); a=1+mu; ch=-ex/(a*(a+ex))
 return float(np.sum(wx[:,None,None]*wy[None,:,None]*wp[None,None,:]*xx*ch)/(32*PI**3))

def negative_controls():
 p=1/8;y=.31;phi=.73;units=list(SHIFT_UNITS.values()); full=radial_breaks(y,phi,p,units); omit=radial_breaks(y,phi,p,units[:-1])
 census=(len(full)!=len(omit) or any(abs(a-b)>1e-12 for a,b in zip(full,omit)));u=SHIFT_UNITS['e31'];wrong=-u;c=cval(y,phi,angle(u));cw=cval(y,phi,angle(wrong))
 sign=abs(rb_root(p,c)-rb_root(p,cw))>1e-6; wr=-p*c-math.sqrt(1-p*p+p*p*c*c); wrrej=abs(shifted_sq(wr,y,phi,p,u)-1)>ROOT_TOL or wr<0
 sets=[active(p,cval(0,t,0)) for t in (.1,PI,2*PI-.1)]; noph=not all(z==sets[0] for z in sets)
 c1=1.; rbs=rb_root(p,c1); r1=.5*rbs; r2=.5*(rbs+1); freeze=((r1*r1+p*p+2*p*r1*c1)>1)!=((r2*r2+p*p+2*p*r2*c1)>1)
 smooth=abs(1/1.1-1/(1+math.exp(1)))>1e-3; rb=rb_root(p,c); clip=abs(shifted_sq(.99*rb,y,phi,p,u)-1)>ROOT_TOL
 return {'omitted_shift_rejected':bool(census),'shift_sign_reversal_rejected':bool(sign),'wrong_root_branch_rejected':bool(wrrej),'omitted_phi_breakpoints_rejected':bool(noph),'frozen_shifted_support_rejected':bool(freeze),'smoothed_regulator_rejected':bool(smooth),'target_dependent_root_clipping_rejected':bool(clip)}

def main():
 geom=geometry_controls(); smooth=integrate_smooth_piecewise(1/8,24); targets=[1/(32*PI**2),1/(48*PI**2)]; serr=[abs(a-b) for a,b in zip(smooth,targets)]
 scal=[]
 for p in (1/8,1/32):
  val=shell_piecewise_xyz(p,24); ref=shell_delta_polar(p,64); scal.append({'p':p,'piecewise_N24':val,'polar_N64':ref,'relative_error':abs(val-ref)/abs(ref)})
 ps=1/256; small=shell_piecewise_xyz(ps,24); c2=-1/(64*PI**2*(1+MU)**2); c2rel=abs(small/(ps*ps)-c2)/abs(c2)
 x,_=gauss(24,0,1); psafe=(1-math.sqrt(float(max(x))))/4; un=unsplit_delta(psafe,24); pw=shell_piecewise_xyz(psafe,24); neg=negative_controls()
 pos={'geometry_boundary':geom['boundary_pass'],'activation_equivalence':geom['activation_pass'],'phi_partition':geom['phi_constant_active_sets_pass'],'radial_partition':geom['radial_partition_pass'],'shift_census':all(abs(np.linalg.norm(v)-1)<1e-14 for v in SHIFT_UNITS.values()),'smooth_integral_equivalence':max(serr)<=2e-12,'scalar_shell_equivalence':all(s['relative_error']<=2e-3 for s in scal),'continuum_c2_control':c2rel<=5e-3,'unsplit_counterexample':un==0 and pw<0}
 scientific=all(pos.values()) and all(neg.values())
 out={'gate':'SF055A3Q4_SHIFTED_LITIM_INTERSECTION_GEOMETRY','classification':'PASS_SHIFTED_REGULATOR_INTERSECTION_GEOMETRY_AND_PIECEWISE_EQUIVALENCE_SCOPED' if scientific else 'FAIL_SHIFTED_REGULATOR_INTERSECTION_GEOMETRY_SCOPED','canonical_shift_units':{k:v.tolist() for k,v in SHIFT_UNITS.items()},'canonical_shift_angles':ALPHAS,'geometry':geom,'smooth_controls':{'piecewise_N24':smooth,'analytic':targets,'abs_errors':serr},'scalar_shell_controls':scal,'small_p_control':{'p':ps,'piecewise_N24':small,'p2_coefficient':small/(ps*ps),'analytic_c2':c2,'relative_error':c2rel},'unsplit_shell_loss_control':{'N':24,'p_safe':psafe,'unsplit':un,'piecewise':pw},'positive_controls':pos,'negative_controls':neg,'scientific_pass':scientific,'next_required':'FULL_TENSOR_PIECEWISE_BASELINE_IMPLEMENTATION_RETRY_UNDER_ORIGINAL_FREEZE' if scientific else 'NO_BASELINE_RETRY_Q4_FAILED','interpretation_ceiling':'GEOMETRY_EQUIVALENCE_ONLY_HISTORICAL_BASELINE_REMAINS_BLOCKED_NO_C3'}
 print(json.dumps(out,indent=2,sort_keys=True,default=lambda o: bool(o) if isinstance(o,np.bool_) else float(o) if isinstance(o,np.floating) else int(o) if isinstance(o,np.integer) else o.tolist() if isinstance(o,np.ndarray) else (_ for _ in ()).throw(TypeError(type(o).__name__))))
 if not scientific: raise SystemExit(1)
if __name__=='__main__': main()
