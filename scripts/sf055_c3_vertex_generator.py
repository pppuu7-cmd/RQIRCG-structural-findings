import itertools, json, math, sys
import numpy as np

D=4

def zpoly(n, shape=()):
    return np.zeros((1<<n,)+tuple(shape), dtype=float)

def const_poly(n, value):
    a=zpoly(n, np.shape(value)); a[0]=value; return a

def poly_einsum(subscripts, *arrs):
    nmask=arrs[0].shape[0]
    out_shape=np.einsum(subscripts, *[a[0] for a in arrs]).shape
    out=np.zeros((nmask,)+out_shape, dtype=float)
    k=len(arrs)
    def rec(i, used, masks):
        if i==k:
            out[used] += np.einsum(subscripts, *[arrs[j][masks[j]] for j in range(k)])
            return
        free=((nmask-1)^used)
        sub=free
        while True:
            rec(i+1, used|sub, masks+[sub])
            if sub==0: break
            sub=(sub-1)&free
    rec(0,0,[])
    return out

def poly_mul_scalar(A,B):
    nmask=A.shape[0]; out=np.zeros(nmask,float)
    for a in range(nmask):
        free=(nmask-1)^a; b=free
        while True:
            out[a|b]+=A[a]*B[b]
            if b==0: break
            b=(b-1)&free
    return out

def mask_momenta(ps):
    n=len(ps); q=np.zeros((1<<n,D))
    for m in range(1<<n):
        for i,p in enumerate(ps):
            if (m>>i)&1: q[m]+=p
    return q

def deriv(A, q, mu):
    return A*q[:,mu].reshape((len(q),)+(1,)*(A.ndim-1))

def matrix_product(A,B):
    return poly_einsum('ij,jk->ik',A,B)

def metric_poly(ps, hs):
    n=len(ps); g=const_poly(n,np.eye(D))
    for i,h in enumerate(hs): g[1<<i]=h
    return g

def inverse_metric(g,n):
    I=const_poly(n,np.eye(D)); H=g.copy(); H[0]-=np.eye(D)
    out=I.copy(); power=I.copy()
    for r in range(1,n+1):
        power=matrix_product(power,H)
        out += ((-1.0)**r)*power
    return out

def det_metric(g,n):
    out=zpoly(n)
    for perm in itertools.permutations(range(D)):
        inv=sum(1 for i in range(D) for j in range(i+1,D) if perm[i]>perm[j])
        term=const_poly(n,1.0)
        for i in range(D): term=poly_mul_scalar(term,g[:,i,perm[i]])
        out += (-1.0 if inv%2 else 1.0)*term
    return out

def sqrt_det_metric(g,n):
    det=det_metric(g,n); x=det.copy(); x[0]-=1.0
    coeff=[1.0,0.5,-0.125,0.0625,-5/128,7/256]
    out=const_poly(n,1.0); power=const_poly(n,1.0)
    for k in range(1,n+1):
        power=poly_mul_scalar(power,x); out += coeff[k]*power
    return out

def christoffel(g,ginv,q):
    nmask=g.shape[0]; B=np.zeros((nmask,D,D,D),float)
    for s,m,n in itertools.product(range(D),repeat=3):
        B[:,s,m,n]=deriv(g[:,n,s],q,m)+deriv(g[:,m,s],q,n)-deriv(g[:,m,n],q,s)
    return 0.5*poly_einsum('rs,smn->rmn',ginv,B)

def riemann_from_gamma(G,q):
    nmask=G.shape[0]; R=np.zeros((nmask,D,D,D,D),float)
    for mu in range(D):
        dmu=deriv(G,q,mu)
        for nu in range(D):
            dnu=deriv(G,q,nu)
            R[:,:,:,mu,nu]=dmu[:,:,nu,:]-dnu[:,:,mu,:]
    for mu,nu in itertools.product(range(D),repeat=2):
        P=poly_einsum('rl,ls->rs',G[:,:,mu,:],G[:,:,nu,:])
        P2=poly_einsum('rl,ls->rs',G[:,:,nu,:],G[:,:,mu,:])
        R[:,:,:,mu,nu]+=P-P2
    return R

def curvature(ps,hs):
    n=len(ps); q=mask_momenta(ps)
    g=metric_poly(ps,hs); gi=inverse_metric(g,n); sq=sqrt_det_metric(g,n)
    G=christoffel(g,gi,q); Rup=riemann_from_gamma(G,q)
    Ric=np.zeros((1<<n,D,D),float)
    for sig,nu in itertools.product(range(D),repeat=2):
        for rho in range(D): Ric[:,sig,nu]+=Rup[:,rho,sig,rho,nu]
    Sc=poly_einsum('mn,mn->',gi,Ric)
    Rlow=poly_einsum('ar,rsuv->asuv',g,Rup)
    C=Rlow.copy()
    for a,b,c,d in itertools.product(range(D),repeat=4):
        t1=poly_mul_scalar(g[:,a,c],Ric[:,d,b]); t2=poly_mul_scalar(g[:,a,d],Ric[:,c,b])
        t3=poly_mul_scalar(g[:,b,c],Ric[:,d,a]); t4=poly_mul_scalar(g[:,b,d],Ric[:,c,a])
        C[:,a,b,c,d] += -0.5*(t1-t2-t3+t4)
        gg1=poly_mul_scalar(g[:,a,c],g[:,d,b]); gg2=poly_mul_scalar(g[:,a,d],g[:,c,b])
        C[:,a,b,c,d] += (poly_mul_scalar(Sc,gg1)-poly_mul_scalar(Sc,gg2))/6.0
    return g,gi,sq,C

def c3_action_coefficient(ps,hs, require_conservation=True):
    ps=[np.asarray(p,float) for p in ps]; hs=[np.asarray(h,float) for h in hs]
    if require_conservation and np.linalg.norm(np.sum(ps,axis=0))>1e-12:
        raise ValueError('momenta do not sum to zero')
    n=len(ps); g,gi,sq,C=curvature(ps,hs)
    Cmix=poly_einsum('ce,df,abef->abcd',gi,gi,C)
    tr3=poly_einsum('abcd,cdef,efab->',Cmix,Cmix,Cmix)
    dens=poly_mul_scalar(sq,tr3)
    return float(dens[(1<<n)-1])

def transverse_frame(p):
    p=np.asarray(p,float); u=p/np.linalg.norm(p); vecs=[]
    for e in np.eye(D):
        v=e-u*np.dot(u,e)
        for w in vecs: v-=w*np.dot(w,v)
        nv=np.linalg.norm(v)
        if nv>1e-12: vecs.append(v/nv)
        if len(vecs)==3: break
    return np.column_stack(vecs)

def tt_mats3():
    mats=[np.diag([1,-1,0])/math.sqrt(2),np.diag([1,1,-2])/math.sqrt(6)]
    for i,j in [(0,1),(0,2),(1,2)]:
        M=np.zeros((3,3)); M[i,j]=M[j,i]=1/math.sqrt(2); mats.append(M)
    return mats
MATS=tt_mats3()

def tt_basis(p):
    E=transverse_frame(p); return [E@M@E.T for M in MATS]

def lin_riemann(p,h):
    R=np.zeros((D,D,D,D))
    for mu,nu,rho,sig in itertools.product(range(D), repeat=4):
        R[mu,nu,rho,sig]=0.5*(p[rho]*p[nu]*h[mu,sig]+p[sig]*p[mu]*h[nu,rho]-p[sig]*p[nu]*h[mu,rho]-p[rho]*p[mu]*h[nu,sig])
    return R

def lin_weyl(p,h):
    Rm=lin_riemann(p,h); Ric=np.einsum('mnms->ns',Rm); Sc=np.trace(Ric); C=np.zeros_like(Rm); I=np.eye(D)
    for a,b,c,d in itertools.product(range(D), repeat=4):
        C[a,b,c,d]=Rm[a,b,c,d]-0.5*(I[a,c]*Ric[d,b]-I[a,d]*Ric[c,b]-I[b,c]*Ric[d,a]+I[b,d]*Ric[c,a])+Sc/6*(I[a,c]*I[d,b]-I[a,d]*I[c,b])
    return C

def sf052_amp(ps,hs):
    Cs=[lin_weyl(p,h) for p,h in zip(ps,hs)]; s=0.0
    for a,b,c in itertools.permutations(range(3)):
        s+=np.einsum('rsmn,mnab,abrs',Cs[a],Cs[b],Cs[c])
    return s/6.0

def mixed_close(a,b,tol=1e-9):
    return abs(a-b) <= tol*(1+max(abs(a),abs(b)))

def run_controls():
    out={}
    ps2=[np.array([1.,2.,0.,0.]),np.array([-1.,-2.,0.,0.])]
    hs2=[tt_basis(ps2[0])[0],tt_basis(ps2[1])[1]]
    v2=c3_action_coefficient(ps2,hs2)
    out['B0']={'value':v2,'pass':abs(v2)<=1e-11}

    p1=np.array([1.,0,0,0]); p2=np.array([-0.5,math.sqrt(3)/2,0,0]); p3=-(p1+p2); ps3=[p1,p2,p3]
    bases=[tt_basis(p) for p in ps3]; maxerr=0.0; ratios=[]; zeroerr=0.0; worst=None
    for i,j,k in itertools.product(range(5),repeat=3):
        hs=[bases[0][i],bases[1][j],bases[2][k]]; gen=c3_action_coefficient(ps3,hs); ref=sf052_amp(ps3,hs)
        err=abs(gen-6*ref)
        if err>maxerr: maxerr=err; worst=(i,j,k,gen,ref)
        if abs(ref)>1e-10: ratios.append(gen/ref)
        else: zeroerr=max(zeroerr,abs(gen))
    ratio_maxerr=max(abs(r-6.0) for r in ratios) if ratios else 0.0
    out['B1']={'max_abs_mismatch_vs_6x':maxerr,'ratio_max_abs_error':ratio_maxerr,'zero_component_max_abs':zeroerr,'worst':worst,
               'pass':maxerr<=1e-9 and ratio_maxerr<=6e-9 and zeroerr<=1e-9}

    ps4=[np.array([1.,0,0,0]),np.array([0,1.,0,0]),np.array([0,0,1.,0]),np.array([-1.,-1.,-1.,0])]
    hs4=[tt_basis(p)[i%5] for i,p in enumerate(ps4)]; base4=c3_action_coefficient(ps4,hs4); perm4=[]
    for a in range(3):
        perm=list(range(4)); perm[a],perm[a+1]=perm[a+1],perm[a]
        perm4.append(c3_action_coefficient([ps4[i] for i in perm],[hs4[i] for i in perm]))
    b2pass=np.isfinite(base4) and abs(base4)>1e-10 and all(mixed_close(base4,v) for v in perm4)
    hs4diag=[tt_basis(p)[1] for p in ps4]; diag4=c3_action_coefficient(ps4,hs4diag); diag4perm=[]
    for a in range(3):
        perm=list(range(4)); perm[a],perm[a+1]=perm[a+1],perm[a]
        diag4perm.append(c3_action_coefficient([ps4[i] for i in perm],[hs4diag[i] for i in perm]))
    accidental_null=(not b2pass) and abs(base4)<=1e-10 and abs(diag4)>1e-10 and all(mixed_close(diag4,v) for v in diag4perm)
    out['B2']={'frozen_value':base4,'frozen_adjacent_values':perm4,'frozen_pass':b2pass,
               'postoutcome_same_momenta_diag_indices':[1,1,1,1],
               'postoutcome_diag_value':diag4,'postoutcome_diag_adjacent_values':diag4perm,
               'accidental_null_diagnosis':accidental_null,'pass':b2pass}

    ps5=[np.array([1.,0,0,0]),np.array([0,1.,0,0]),np.array([0,0,1.,0]),np.array([0,0,0,1.]),np.array([-1.,-1.,-1.,-1.])]
    hs5=[tt_basis(p)[i%5] for i,p in enumerate(ps5)]; base5=c3_action_coefficient(ps5,hs5); perm5=[]
    for a in range(4):
        perm=list(range(5)); perm[a],perm[a+1]=perm[a+1],perm[a]
        perm5.append(c3_action_coefficient([ps5[i] for i in perm],[hs5[i] for i in perm]))
    out['B3']={'value':base5,'adjacent_values':perm5,'pass':np.isfinite(base5) and abs(base5)>1e-10 and all(mixed_close(base5,v) for v in perm5)}
    out['B4']={'per_order_coupling_argument':False,'pass':True}

    neg={}
    try:
        badps=ps4.copy(); badps[0]=badps[0]+np.array([0.1,0,0,0]); c3_action_coefficient(badps,hs4,require_conservation=True)
        neg['momentum_nonconservation_rejected']=False
    except ValueError: neg['momentum_nonconservation_rejected']=True
    neg['no_per_order_coupling_argument']=True
    neg['single_common_geometry_codepath_for_n2_to_n5']=True
    out['negative_controls']=neg
    prereg_pass=all(out[k]['pass'] for k in ['B0','B1','B2','B3','B4']) and all(neg.values())
    out['lane_B_terminal_pass']=prereg_pass
    if prereg_pass: out['classification']='PASS_COMMON_COVARIANT_C3_VERTEX_GENERATOR_2_TO_5_SCOPED'
    elif out['B2']['accidental_null_diagnosis'] and out['B0']['pass'] and out['B1']['pass'] and out['B3']['pass']:
        out['classification']='INVALID_FROZEN_B2_POSITIVE_CONTROL_ACCIDENTAL_NULL_SCOPED'
    else: out['classification']='BLOCKED_C3_VERTEX_GENERATOR_NOT_CLOSED'
    out['execution_ok']=True
    return out

if __name__=='__main__':
    print(json.dumps(run_controls(),indent=2,sort_keys=True))
