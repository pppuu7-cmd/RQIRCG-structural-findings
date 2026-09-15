import itertools, json, math
import numpy as np

D=4

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

def direct_density(ps,hs,eps):
    ps=[np.asarray(p,float) for p in ps]; hs=[np.asarray(h,float) for h in hs]; eps=np.asarray(eps,float)
    g=np.eye(D); dg=np.zeros((D,D,D)); d2g=np.zeros((D,D,D,D))
    for e,p,h in zip(eps,ps,hs):
        g += e*h
        for a in range(D):
            dg[a] += e*p[a]*h
            for b in range(D): d2g[a,b] += e*p[a]*p[b]*h
    det=float(np.linalg.det(g))
    if not np.isfinite(det) or det<=0: raise ValueError('nonpositive metric determinant')
    gi=np.linalg.inv(g); dgi=np.zeros((D,D,D))
    for a in range(D): dgi[a] = -gi@dg[a]@gi
    B=np.zeros((D,D,D)); dB=np.zeros((D,D,D,D))
    for s,m,n in itertools.product(range(D),repeat=3):
        B[s,m,n]=dg[m,n,s]+dg[n,m,s]-dg[s,m,n]
        for lam in range(D):
            dB[lam,s,m,n]=d2g[lam,m,n,s]+d2g[lam,n,m,s]-d2g[lam,s,m,n]
    G=0.5*np.einsum('rs,smn->rmn',gi,B); dG=np.zeros((D,D,D,D))
    for lam in range(D):
        dG[lam]=0.5*(np.einsum('rs,smn->rmn',dgi[lam],B)+np.einsum('rs,smn->rmn',gi,dB[lam]))
    R=np.zeros((D,D,D,D))
    for r,s,m,n in itertools.product(range(D),repeat=4):
        R[r,s,m,n]=dG[m,r,n,s]-dG[n,r,m,s]
        R[r,s,m,n]+=sum(G[r,m,l]*G[l,n,s]-G[r,n,l]*G[l,m,s] for l in range(D))
    Ric=np.zeros((D,D))
    for s,n in itertools.product(range(D),repeat=2): Ric[s,n]=sum(R[r,s,r,n] for r in range(D))
    Sc=float(np.einsum('mn,mn',gi,Ric)); Rlow=np.einsum('ar,rsuv->asuv',g,R); C=Rlow.copy()
    for a,b,c,d in itertools.product(range(D),repeat=4):
        C[a,b,c,d] += -0.5*(g[a,c]*Ric[d,b]-g[a,d]*Ric[c,b]-g[b,c]*Ric[d,a]+g[b,d]*Ric[c,a])
        C[a,b,c,d] += Sc/6.0*(g[a,c]*g[d,b]-g[a,d]*g[c,b])
    trace=np.einsum('ac,abcd->bd',gi,C)
    anti1=float(np.max(np.abs(C+np.swapaxes(C,0,1)))); anti2=float(np.max(np.abs(C+np.swapaxes(C,2,3))))
    trnorm=float(np.max(np.abs(trace))); Cmix=np.einsum('ce,df,abef->abcd',gi,gi,C)
    tr3=float(np.einsum('abcd,cdef,efab',Cmix,Cmix,Cmix)); dens=math.sqrt(det)*tr3
    controls={'det':det,'weyl_trace_max':trnorm,'weyl_anti1_max':anti1,'weyl_anti2_max':anti2,
              'finite':bool(np.isfinite(dens) and np.all(np.isfinite(gi)))}
    return dens,controls

def mixed_derivative(ps,hs,h):
    n=len(ps); total=0.0
    worst={'weyl_trace_max':0.0,'weyl_anti1_max':0.0,'weyl_anti2_max':0.0,'min_det':float('inf'),'finite':True}
    for signs in itertools.product([-1.0,1.0], repeat=n):
        dens,c=direct_density(ps,hs,[h*s for s in signs]); total += float(np.prod(signs))*dens
        worst['weyl_trace_max']=max(worst['weyl_trace_max'],c['weyl_trace_max'])
        worst['weyl_anti1_max']=max(worst['weyl_anti1_max'],c['weyl_anti1_max'])
        worst['weyl_anti2_max']=max(worst['weyl_anti2_max'],c['weyl_anti2_max'])
        worst['min_det']=min(worst['min_det'],c['det']); worst['finite']=worst['finite'] and c['finite']
    return total/((2*h)**n),worst

def richardson(ps,hs):
    d1,c1=mixed_derivative(ps,hs,0.04); d2,c2=mixed_derivative(ps,hs,0.02); dr=(4*d2-d1)/3.0
    controls={k:(min(c1[k],c2[k]) if k=='min_det' else max(c1[k],c2[k]) if k!='finite' else c1[k] and c2[k]) for k in c1}
    return d1,d2,dr,controls

def geom_ok(c):
    return c['min_det']>0 and c['finite'] and c['weyl_trace_max']<=1e-9 and c['weyl_anti1_max']<=1e-9 and c['weyl_anti2_max']<=1e-9

def compare(dr,target,tol):
    return abs(dr-target)<=tol*(1+abs(target))

def run():
    out={}
    ps2=[np.array([1.,2.,0.,0.]),np.array([-1.,-2.,0.,0.])]; hs2=[tt_basis(ps2[0])[0],tt_basis(ps2[1])[1]]
    d1,d2,dr,c=richardson(ps2,hs2); out['V2']={'D_h004':d1,'D_h002':d2,'D_R':dr,'target':0.0,'geom':c,'pass':geom_ok(c) and abs(dr)<=1e-6}
    p1=np.array([1.,0,0,0]); p2=np.array([-0.5,math.sqrt(3)/2,0,0]); p3=-(p1+p2); ps3=[p1,p2,p3]; inds3=[1,3,3]; hs3=[tt_basis(p)[i] for p,i in zip(ps3,inds3)]
    target3=-0.5358258812338206; d1,d2,dr,c=richardson(ps3,hs3); out['V3']={'D_h004':d1,'D_h002':d2,'D_R':dr,'target':target3,'geom':c,'pass':geom_ok(c) and compare(dr,target3,5e-5)}
    ps4=[np.array([1.,0,0,0]),np.array([0,1.,0,0]),np.array([0,0,1.,0]),np.array([-1.,-1.,-1.,0])]; hs4=[tt_basis(p)[1] for p in ps4]
    target4=2.791666666666668; d1,d2,dr,c=richardson(ps4,hs4); out['V4']={'D_h004':d1,'D_h002':d2,'D_R':dr,'target':target4,'geom':c,'pass':geom_ok(c) and compare(dr,target4,5e-5)}
    ps5=[np.array([1.,0,0,0]),np.array([0,1.,0,0]),np.array([0,0,1.,0]),np.array([0,0,0,1.]),np.array([-1.,-1.,-1.,-1.])]; inds5=[0,1,2,3,4]; hs5=[tt_basis(p)[i] for p,i in zip(ps5,inds5)]
    target5=1.8561553006146843; d1,d2,dr,c=richardson(ps5,hs5); out['V5']={'D_h004':d1,'D_h002':d2,'D_R':dr,'target':target5,'geom':c,'pass':geom_ok(c) and compare(dr,target5,2e-4)}
    if all(out[k]['pass'] for k in ['V2','V3','V4','V5']): cls='INDEPENDENT_DIRECT_GEOMETRY_VERIFIES_COMMON_C3_GENERATOR_SCOPED'
    elif any(not geom_ok(out[k]['geom']) for k in ['V2','V3','V4','V5']): cls='INVALID_DIRECT_C3_GENERATOR_VERIFIER_SCOPED'
    else: cls='COMMON_C3_GENERATOR_CROSS_IMPLEMENTATION_MISMATCH_SCOPED'
    out['classification']=cls; out['scientific_pass']=cls.startswith('INDEPENDENT_'); out['execution_ok']=True
    return out

if __name__=='__main__':
    print(json.dumps(run(),indent=2,sort_keys=True))
