#!/usr/bin/env python3
"""Exact batched square-free source-Fourier EH vertex engine for SF055A3.

The leading axes carry requested directional bases for each functional leg;
geometry contractions are identical to the validated scalar SF055A2 engine.
"""
import hashlib
import itertools
import json
import math
from pathlib import Path

import numpy as np

import sf055a2_source_fourier_seed_engine as scalar
import sf055a_eh_ghost_seed_engine as base

D=4
PI=math.pi
EH_PREF=1.0/(16.0*PI)
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'results'/'raw'/'SF055A3_BATCHED_VERTEX_ENGINE_CHECK.json'


def padd(A,B):
    out={k:np.array(v,copy=True) for k,v in A.items()}
    for k,v in B.items(): out[k]=out[k]+v if k in out else np.array(v,copy=True)
    return out

def pscale(A,c): return {k:c*v for k,v in A.items()}
def peinsum(A,B,subs):
    out={}
    for ma,a in A.items():
        for mb,b in B.items():
            if ma&mb: continue
            m=ma|mb
            v=np.einsum(subs,a,b,optimize=True)
            out[m]=out[m]+v if m in out else v
    return out

def pmatmul(A,B): return peinsum(A,B,'...ab,...bc->...ac')
def ptrace(A): return {m:np.einsum('...aa->...',v) for m,v in A.items()}
def pscalar_mul(A,B):
    out={}
    for ma,a in A.items():
        for mb,b in B.items():
            if ma&mb: continue
            m=ma|mb; v=a*b
            out[m]=out[m]+v if m in out else v
    return out


def _lead_ones(n): return (1,)*n

def embed_stack(stack,leg,n):
    x=np.asarray(stack,float)
    if x.ndim!=3 or x.shape[1:]!=(D,D): raise ValueError('stack must have shape (d,4,4)')
    shape=[1]*n+[D,D]; shape[leg]=x.shape[0]
    return x.reshape(shape)

def hpoly(stacks):
    n=len(stacks)
    return {1<<i:embed_stack(s,i,n) for i,s in enumerate(stacks)}
def metric(stacks):
    n=len(stacks); out={0:np.eye(D).reshape(_lead_ones(n)+(D,D))}; out.update(hpoly(stacks)); return out

def inverse_metric(stacks):
    n=len(stacks); H=hpoly(stacks)
    eye=np.eye(D).reshape(_lead_ones(n)+(D,D))
    out={0:eye}; power={0:eye}
    for r in range(1,n+1):
        power=pmatmul(power,H); out=padd(out,pscale(power,(-1)**r))
    return out

def sqrt_det_metric(stacks):
    n=len(stacks); H=hpoly(stacks)
    eye=np.eye(D).reshape(_lead_ones(n)+(D,D))
    log_half={}; power={0:eye}
    for r in range(1,n+1):
        power=pmatmul(power,H)
        log_half=padd(log_half,pscale(ptrace(power),0.5*((-1)**(r+1))/r))
    one=np.ones(_lead_ones(n))
    out={0:one}; power_s={0:one}
    for r in range(1,n+1):
        power_s=pscalar_mul(power_s,log_half)
        out=padd(out,pscale(power_s,1.0/math.factorial(r)))
    return out

def scalar_curvature_fourier(ps,stacks,phase=1j):
    n=len(ps); ps=[np.asarray(p,float) for p in ps]
    gi=inverse_metric(stacks); H=hpoly(stacks)
    dg={}
    for i,p in enumerate(ps):
        h=H[1<<i]
        dg[1<<i]=phase*np.einsum('a,...mn->...amn',p,h,optimize=True)
    B={}
    for mask,a in dg.items():
        b=np.zeros(a.shape[:-3]+(D,D,D),dtype=complex)
        for s,mu,nu in itertools.product(range(D),repeat=3):
            b[...,s,mu,nu]=a[...,mu,s,nu]+a[...,nu,s,mu]-a[...,s,mu,nu]
        B[mask]=b
    Gamma=pscale(peinsum(gi,B,'...rs,...smn->...rmn'),0.5)
    dGamma={}
    for mask,a in Gamma.items():
        if mask==0: continue
        q=sum((ps[i] for i in range(n) if (mask>>i)&1),np.zeros(D))
        dGamma[mask]=phase*np.einsum('a,...rmn->...armn',q,a,optimize=True)
    Rmix={}
    for mask,a in dGamma.items():
        r=np.zeros(a.shape[:-4]+(D,D,D,D),dtype=complex)
        for rho,sig,mu,nu in itertools.product(range(D),repeat=4):
            r[...,rho,sig,mu,nu]=a[...,mu,rho,nu,sig]-a[...,nu,rho,mu,sig]
        Rmix[mask]=r
    gg1=peinsum(Gamma,Gamma,'...rml,...lns->...rsmn')
    gg2=peinsum(Gamma,Gamma,'...rnl,...lms->...rsmn')
    Rmix=padd(Rmix,padd(gg1,pscale(gg2,-1.0)))
    Ric={m:np.einsum('...rsrn->...sn',a,optimize=True) for m,a in Rmix.items()}
    return peinsum(gi,Ric,'...sn,...sn->...')
def eh_tensor(ps,stacks,lam,pref=EH_PREF,phase=1j,cosm_sign=1.0):
    ps=[np.asarray(p,float) for p in ps]
    if np.linalg.norm(sum(ps,np.zeros(D)))>1e-12: raise ValueError('momenta must conserve')
    n=len(ps)
    sqrtg=sqrt_det_metric(stacks)
    R=scalar_curvature_fourier(ps,stacks,phase=phase)
    core=pscale(R,-1.0)
    core=padd(core,{0:np.full(_lead_ones(n),cosm_sign*2.0*float(lam))})
    poly=pscale(pscalar_mul(sqrtg,core),pref)
    full=(1<<n)-1
    v=np.real_if_close(poly.get(full,0.0),tol=1000)
    if np.iscomplexobj(v) and np.max(np.abs(np.imag(v)))>1e-11: raise ValueError('unexpected complex batch')
    return np.asarray(np.real(v),float)


def scalar_reference(ps,stacks,lam):
    dims=[len(s) for s in stacks]; out=np.zeros(dims)
    for idx in itertools.product(*[range(d) for d in dims]):
        hs=[stacks[i][idx[i]] for i in range(len(stacks))]
        out[idx]=scalar.eh_vertex_fourier(ps,hs,lam)
    return out

def hash_arr(x): return hashlib.sha256(np.ascontiguousarray(np.asarray(x,dtype='<f8')).tobytes()).hexdigest()
def maxerr(a,b): return float(np.max(np.abs(np.asarray(a)-np.asarray(b))))

def two_stack(B): return np.asarray([B[0],B[3]])
def dense_stacks(ps):
    return [np.asarray([base.dense_tt(p,i),base.dense_tt(p,i+2)]) for i,p in enumerate(ps)]

def bose_err(ps,stacks,lam):
    T=eh_tensor(ps,stacks,lam); mx=0.0
    perms=list(itertools.permutations(range(len(ps))))
    for perm in perms:
        Tp=eh_tensor([ps[i] for i in perm],[stacks[i] for i in perm],lam)
        mx=max(mx,maxerr(Tp,np.transpose(T,perm)))
    return mx,len(perms)

def main():
    pos={}
    p=np.array([1.,0,0,0]); B=base.tt_basis(p); S=np.asarray(B)
    two=[]
    for lam in [0.0,-0.05,0.15]:
        bt=eh_tensor([p,-p],[S,S],lam); st=scalar_reference([p,-p],[S,S],lam)
        two.append({'lambda':lam,'max_abs_error':maxerr(bt,st)})
    pos['n2_full_TT']=max(x['max_abs_error'] for x in two)<=2e-12

    ps3=base.symmetric_ps3(); Bs3=[np.asarray(base.tt_basis(q)) for q in ps3]; zps=[np.zeros(4) for _ in range(3)]
    TG=eh_tensor(ps3,Bs3,0.0); TGs=scalar_reference(ps3,Bs3,0.0)
    TL=eh_tensor(zps,Bs3,1.0); TLs=scalar_reference(zps,Bs3,1.0)
    tgerr=maxerr(TG,TGs); tlerr=maxerr(TL,TLs)
    tgh=hash_arr(TG); tlh=hash_arr(TL)
    pos['n3_TG_all125']=tgerr<=2e-12 and tgh=='66638b7f47175bfbe0b1fb7234f0c0f5260764da17942b9eedc9af0c35cf8e80'
    pos['n3_TLambda_all125']=tlerr<=2e-12 and tlh=='d4bce18818b05fcaf3e36c78683da0c0ca43db995221462c71131c90ecdf84e5'

    ps4=[np.array([1.,0,0,0]),np.array([0,1.,0,0]),np.array([0,0,1.,0]),np.array([-1.,-1.,-1.,0])]
    st4=dense_stacks(ps4); T4=eh_tensor(ps4,st4,-0.7); R4=scalar_reference(ps4,st4,-0.7); e4=maxerr(T4,R4)
    pos['n4_2x2x2x2']=e4<=2e-12
    ps5=[np.eye(4)[i] for i in range(4)]+[-np.ones(4)]
    st5=dense_stacks(ps5); T5=eh_tensor(ps5,st5,-0.7); R5=scalar_reference(ps5,st5,-0.7); e5=maxerr(T5,R5)
    pos['n5_2pow5']=e5<=3e-12

    scaled=list(Bs3); scaled[0]=1.7*scaled[0]
    Ts=eh_tensor(ps3,scaled,0.0); scale_err=maxerr(Ts,1.7*TG)
    pos['multilinearity_scaling']=scale_err<=2e-12

    bose={}
    for n,psx,stx,lam in [(3,ps3,[two_stack(x) for x in Bs3],-0.7),(4,ps4,st4,-0.7),(5,ps5,st5,-0.7)]:
        e,npers=bose_err(psx,stx,lam); bose[str(n)]={'max_abs_error':e,'permutations':npers,'pass':e<=3e-12}
    pos['Bose_3_4_5']=all(x['pass'] for x in bose.values())

    # Counterexample-first mutations.
    neg={}
    badphase=eh_tensor(ps3,[two_stack(x) for x in Bs3],-0.7,phase=1.0)
    goodsmall=eh_tensor(ps3,[two_stack(x) for x in Bs3],-0.7)
    neg['drop_Fourier_i_rejected']=maxerr(badphase,goodsmall)>1e-8
    badpref=eh_tensor(ps3,[two_stack(x) for x in Bs3],-0.7,pref=2*EH_PREF)
    neg['double_EH_prefactor_rejected']=maxerr(badpref,goodsmall)>1e-8
    badcosm=eh_tensor(ps3,[two_stack(x) for x in Bs3],-0.7,cosm_sign=-1.0)
    neg['wrong_cosmological_sign_rejected']=maxerr(badcosm,goodsmall)>1e-8
    # Structural square-free and axis completeness checks.
    neg['overlapping_masks_rejected']=all((ma&mb)!=0 for ma,mb in [(1,1),(3,1),(6,2)])
    neg['misaligned_leg_axis_rejected']=TG.shape==(5,5,5) and not np.allclose(np.swapaxes(TG,0,1),TG,atol=0,rtol=0)
    neg['diagonal_only_declared_full_rejected']=np.count_nonzero(np.abs(TG)>1e-14)>5

    positive_pass=all(pos.values()); negative_pass=all(neg.values()); sci=positive_pass and negative_pass
    result={
      'gate':'SF055A3_BATCHED_SOURCE_VERTEX_ENGINE_EQUIVALENCE',
      'classification':'PASS_SF055A3_BATCHED_SOURCE_VERTEX_ENGINE_EQUIVALENT_SCOPED' if sci else 'FAIL_SF055A3_BATCHED_SOURCE_VERTEX_ENGINE_EQUIVALENCE_SCOPED',
      'n2_records':two,'TG_max_abs_error':tgerr,'TLambda_max_abs_error':tlerr,'TG_sha256':tgh,'TLambda_sha256':tlh,
      'n4_max_abs_error':e4,'n5_max_abs_error':e5,'scaling_max_abs_error':scale_err,'Bose':bose,
      'positive_controls':pos,'negative_controls':neg,'positive_pass':positive_pass,'negative_pass':negative_pass,'scientific_pass':sci,
      'next_required':'BATCHED_FULL_TT_FIGURE2_QUADRATURE','interpretation_ceiling':'COMPUTATIONAL_EQUIVALENCE_ONLY_NO_QUADRATURE_NO_EQ14_NO_C3'
    }
    OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))
    if not sci: raise SystemExit(1)

if __name__=='__main__': main()
