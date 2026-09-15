import itertools
import sympy as sp

D = 4
sqrt = sp.sqrt
p1 = sp.Matrix([1,0,0,0])
p2 = sp.Matrix([-sp.Rational(1,2),sqrt(3)/2,0,0])
p3 = -(p1+p2)
ps = [p1,p2,p3]

E1 = sp.Matrix.hstack(sp.Matrix([0,1,0,0]),sp.Matrix([0,0,1,0]),sp.Matrix([0,0,0,1]))
E2 = sp.Matrix.hstack(sp.Matrix([-sqrt(3)/2,-sp.Rational(1,2),0,0]),sp.Matrix([0,0,1,0]),sp.Matrix([0,0,0,1]))
E3 = sp.Matrix.hstack(sp.Matrix([sqrt(3)/2,-sp.Rational(1,2),0,0]),sp.Matrix([0,0,1,0]),sp.Matrix([0,0,0,1]))
Es = [E1,E2,E3]

mats = [sp.diag(1,-1,0)/sqrt(2), sp.diag(1,1,-2)/sqrt(6)]
for i,j in [(0,1),(0,2),(1,2)]:
    M = sp.zeros(3)
    M[i,j] = M[j,i] = 1/sqrt(2)
    mats.append(M)
bases = [[sp.simplify(E*M*E.T) for M in mats] for E in Es]

def lin_riemann(p,h):
    R = sp.MutableDenseNDimArray.zeros(D,D,D,D)
    for mu,nu,rho,sig in itertools.product(range(D), repeat=4):
        R[mu,nu,rho,sig] = sp.Rational(1,2)*(
            p[rho]*p[nu]*h[mu,sig] + p[sig]*p[mu]*h[nu,rho]
            - p[sig]*p[nu]*h[mu,rho] - p[rho]*p[mu]*h[nu,sig]
        )
    return R

def ricci_scalar(R):
    Ric = sp.zeros(D,D)
    for n in range(D):
        for s in range(D):
            Ric[n,s] = sum(R[m,n,m,s] for m in range(D))
    Sc = sp.simplify(sum(Ric[i,i] for i in range(D)))
    return Ric, Sc

def lin_weyl(p,h):
    R = lin_riemann(p,h)
    Ric,Sc = ricci_scalar(R)
    C = sp.MutableDenseNDimArray.zeros(D,D,D,D)
    for a,b,c,d in itertools.product(range(D), repeat=4):
        C[a,b,c,d] = sp.simplify(
            R[a,b,c,d]
            - sp.Rational(1,D-2)*(
                int(a==c)*Ric[d,b] - int(a==d)*Ric[c,b]
                - int(b==c)*Ric[d,a] + int(b==d)*Ric[c,a]
            )
            + Sc/sp.Rational((D-1)*(D-2))*(
                int(a==c and d==b)-int(a==d and c==b)
            )
        )
    return C,Ric,Sc

def c3_contract(A,B,C):
    return sp.simplify(sum(
        A[r,s,m,n]*B[m,n,a,b]*C[a,b,r,s]
        for r,s,m,n,a,b in itertools.product(range(D), repeat=6)
    ))

def ssc_contract(S1,S2,C):
    return sp.simplify(sum(
        S1[mu,nu]*S2[rho,sig]*C[mu,rho,nu,sig]
        for mu,nu,rho,sig in itertools.product(range(D), repeat=4)
    ))

Cs = [[None]*5 for _ in range(3)]
Ss = [[None]*5 for _ in range(3)]
Scs = [[None]*5 for _ in range(3)]
for leg in range(3):
    for i,h in enumerate(bases[leg]):
        C,Ric,Sc = lin_weyl(ps[leg],h)
        S = sp.simplify(Ric-sp.eye(D)*Sc/D)
        Cs[leg][i] = C
        Ss[leg][i] = S
        Scs[leg][i] = Sc

def amp_E(i,j,k):
    arr = [Cs[0][i],Cs[1][j],Cs[2][k]]
    return sp.simplify(sum(c3_contract(arr[a],arr[b],arr[c]) for a,b,c in itertools.permutations(range(3)))/6)

def amp_R1(i,j,k):
    arr = [Ss[0][i],Ss[1][j],Ss[2][k]]
    return sp.simplify(sum(sp.trace(arr[a]*arr[b]*arr[c]) for a,b,c in itertools.permutations(range(3)))/6)

def amp_R2(i,j,k):
    Sarr = [Ss[0][i],Ss[1][j],Ss[2][k]]
    Carr = [Cs[0][i],Cs[1][j],Cs[2][k]]
    return sp.simplify(sum(ssc_contract(Sarr[a],Sarr[b],Carr[c]) for a,b,c in itertools.permutations(range(3)))/6)

vecs = [[],[],[]]
for i,j,k in itertools.product(range(5), repeat=3):
    vecs[0].append(amp_E(i,j,k))
    vecs[1].append(amp_R1(i,j,k))
    vecs[2].append(amp_R2(i,j,k))

G = sp.Matrix(3,3,lambda a,b: sp.simplify(sum(vecs[a][n]*vecs[b][n] for n in range(125))))
GR = G[1:3,1:3]
v = sp.Matrix([G[1,0],G[2,0]])
coeff = sp.simplify(GR.inv()*v)
norm_perp = sp.simplify(G[0,0]-(v.T*GR.inv()*v)[0])

print('all linearized scalar curvatures zero =', all(sp.simplify(Scs[l][i])==0 for l in range(3) for i in range(5)))
print('Gram =', G)
print('redundant det =', sp.factor(GR.det()))
print('redundant rank =', GR.rank())
print('subtraction coefficients =', coeff)
print('T_E_perp = T_E - coeff[0] T_R1 - coeff[1] T_R2')
print('norm_perp =', norm_perp)
print('overlap R1 =', sp.simplify(G[0,1]-(coeff[0]*G[1,1]+coeff[1]*G[2,1])))
print('overlap R2 =', sp.simplify(G[0,2]-(coeff[0]*G[1,2]+coeff[1]*G[2,2])))
print('naive R1 contamination =', sp.simplify(G[0,1]/G[0,0]))
print('naive R2 contamination =', sp.simplify(G[0,2]/G[0,0]))
