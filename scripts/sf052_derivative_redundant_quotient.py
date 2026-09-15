import itertools, math
import numpy as np
from fractions import Fraction

# Frozen SF052 geometry: D=4 real-Euclidean symmetric point.
D=4
p1=np.array([1.,0,0,0]); p2=np.array([-0.5,math.sqrt(3)/2,0,0]); p3=-(p1+p2); ps=[p1,p2,p3]
E1=np.column_stack(([0,1,0,0],[0,0,1,0],[0,0,0,1])).astype(float)
E2=np.column_stack(([-math.sqrt(3)/2,-0.5,0,0],[0,0,1,0],[0,0,0,1])).astype(float)
E3=np.column_stack(([math.sqrt(3)/2,-0.5,0,0],[0,0,1,0],[0,0,0,1])).astype(float)
Es=[E1,E2,E3]
mats=[np.diag([1,-1,0])/math.sqrt(2),np.diag([1,1,-2])/math.sqrt(6)]
for i,j in [(0,1),(0,2),(1,2)]:
    M=np.zeros((3,3)); M[i,j]=M[j,i]=1/math.sqrt(2); mats.append(M)
bases=[[E@M@E.T for M in mats] for E in Es]

def lin_riemann(p,h):
    R=np.zeros((D,D,D,D))
    for mu,nu,rho,sig in itertools.product(range(D), repeat=4):
        R[mu,nu,rho,sig]=0.5*(p[rho]*p[nu]*h[mu,sig]+p[sig]*p[mu]*h[nu,rho]-p[sig]*p[nu]*h[mu,rho]-p[rho]*p[mu]*h[nu,sig])
    return R

def curv(p,h):
    Rm=lin_riemann(p,h); Ric=np.einsum('mnms->ns',Rm); Sc=np.trace(Ric); C=np.zeros_like(Rm); I=np.eye(D)
    for a,b,c,d in itertools.product(range(D), repeat=4):
        C[a,b,c,d]=Rm[a,b,c,d]-0.5*(I[a,c]*Ric[d,b]-I[a,d]*Ric[c,b]-I[b,c]*Ric[d,a]+I[b,d]*Ric[c,a])+Sc/6*(I[a,c]*I[d,b]-I[a,d]*I[c,b])
    return C,Ric-I*Sc/4,Sc

def gamma1(p,h):
    G=np.zeros((D,D,D))
    for r,m,n in itertools.product(range(D),repeat=3):
        G[r,m,n]=0.5*(p[m]*h[n,r]+p[n]*h[m,r]-p[r]*h[m,n])
    return G

def gamma2(pi,hi,pj,hj):
    G=np.zeros((D,D,D))
    for r,m,n in itertools.product(range(D),repeat=3):
        for s in range(D):
            Dj=pj[m]*hj[n,s]+pj[n]*hj[m,s]-pj[s]*hj[m,n]
            Di=pi[m]*hi[n,s]+pi[n]*hi[m,s]-pi[s]*hi[m,n]
            G[r,m,n]+=-0.5*(hi[r,s]*Dj+hj[r,s]*Di)
    return G

Cs=[[None]*5 for _ in range(3)]; Ss=[[None]*5 for _ in range(3)]; Scs=[[None]*5 for _ in range(3)]; G1=[[None]*5 for _ in range(3)]
for l in range(3):
    for i,h in enumerate(bases[l]):
        C,S,Sc=curv(ps[l],h); Cs[l][i]=C; Ss[l][i]=S; Scs[l][i]=Sc; G1[l][i]=gamma1(ps[l],h)

# Full O(h^2) traceless-Ricci and covariant-derivative cross coefficients.
pair={}
def getpair(a,ia,b,ib):
    if a>b: a,ia,b,ib=b,ib,a,ia
    key=(a,ia,b,ib)
    if key in pair:return pair[key]
    pa,pb=ps[a],ps[b]; ha,hb=bases[a][ia],bases[b][ib]; G2=gamma2(pa,ha,pb,hb); q=pa+pb
    Ric2=np.zeros((D,D))
    for m,n in itertools.product(range(D),repeat=2):
        val=sum(q[r]*G2[r,m,n] for r in range(D))-sum(q[n]*G2[r,m,r] for r in range(D))
        val+=sum(G1[a][ia][r,r,l]*G1[b][ib][l,m,n]+G1[b][ib][r,r,l]*G1[a][ia][l,m,n] for r in range(D) for l in range(D))
        val-=sum(G1[a][ia][r,n,l]*G1[b][ib][l,m,r]+G1[b][ib][r,n,l]*G1[a][ia][l,m,r] for r in range(D) for l in range(D))
        Ric2[m,n]=val
    R2=np.trace(Ric2)-np.einsum('mn,mn',ha,Ss[b][ib])-np.einsum('mn,mn',hb,Ss[a][ia])
    S2=Ric2-np.eye(D)*R2/4
    A2=np.zeros((D,D,D))
    for rho,m,n in itertools.product(range(D),repeat=3):
        val=q[rho]*S2[m,n]
        for lam in range(D):
            val-=G1[a][ia][lam,rho,m]*Ss[b][ib][lam,n]+G1[b][ib][lam,rho,m]*Ss[a][ia][lam,n]
            val-=G1[a][ia][lam,rho,n]*Ss[b][ib][m,lam]+G1[b][ib][lam,rho,n]*Ss[a][ia][m,lam]
        A2[rho,m,n]=val
    pair[key]=(S2,A2,R2); return pair[key]

A1c=[[np.einsum('r,mn->rmn',ps[l],Ss[l][i]) for i in range(5)] for l in range(3)]

def amp_E(i,j,k):
    arr=[Cs[0][i],Cs[1][j],Cs[2][k]]; s=0
    for a,b,c in itertools.permutations(range(3)): s+=np.einsum('rsmn,mnab,abrs',arr[a],arr[b],arr[c])
    return s/6

def amp_R1(i,j,k):
    arr=[Ss[0][i],Ss[1][j],Ss[2][k]]
    return sum(np.trace(arr[a]@arr[b]@arr[c]) for a,b,c in itertools.permutations(range(3)))/6

def amp_R2(i,j,k):
    Sa=[Ss[0][i],Ss[1][j],Ss[2][k]]; Ca=[Cs[0][i],Cs[1][j],Cs[2][k]]; s=0
    for a,b,c in itertools.permutations(range(3)): s+=np.einsum('mn,rs,mrns',Sa[a],Sa[b],Ca[c])
    return s/6

def amp_SDS(i,j,k):
    # int sqrt(g) S Delta S = int sqrt(g) nabla S nabla S, Delta=-nabla^2.
    # Includes S^(1)-S^(2), Gamma^(1)S^(1), and all three inverse-metric O(h) contractions.
    inds=[i,j,k]; val=0.0
    for lone in range(3):
        oth=[x for x in range(3) if x!=lone]; A2=getpair(oth[0],inds[oth[0]],oth[1],inds[oth[1]])[1]
        val+=2*np.einsum('rmn,rmn',A1c[lone][inds[lone]],A2)
    for a,b,l in itertools.permutations(range(3),3):
        Aa=A1c[a][inds[a]]; Ab=A1c[b][inds[b]]; h=bases[l][inds[l]]
        val-=np.einsum('rs,rmn,smn',h,Aa,Ab)
        val-=np.einsum('ma,rmn,ran',h,Aa,Ab)
        val-=np.einsum('nb,rmn,rmb',h,Aa,Ab)
    return val/6

vec=[[],[],[],[]]
for i,j,k in itertools.product(range(5),repeat=3):
    vec[0].append(amp_E(i,j,k)); vec[1].append(amp_R1(i,j,k)); vec[2].append(amp_R2(i,j,k)); vec[3].append(amp_SDS(i,j,k))
V=np.array(vec); G=V@V.T
assert max(abs(x) for row in Scs for x in row)<1e-14  # hence R Delta R cubic TT tensor is exactly zero analytically
print('Gram4=',G)
print('SF051 block=',G[:3,:3])
print('fractions=',[[str(Fraction(float(x)).limit_denominator(10**7)) for x in row] for row in G])
GR=G[1:,1:]; v=G[1:,0]; coeff=np.linalg.solve(GR,v); norm=G[0,0]-v@coeff
print('redundant_rank=',np.linalg.matrix_rank(GR,tol=1e-10))
print('coeff=',coeff,[str(Fraction(float(x)).limit_denominator(10**7)) for x in coeff])
print('norm=',norm,str(Fraction(float(norm)).limit_denominator(10**7)))
print('overlaps=',G[0,1:]-coeff@GR)
