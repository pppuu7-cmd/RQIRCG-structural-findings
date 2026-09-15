import itertools
import sympy as sp

D = 4
sqrt = sp.sqrt
p1 = sp.Matrix([1, 0, 0, 0])
p2 = sp.Matrix([-sp.Rational(1, 2), sqrt(3)/2, 0, 0])
p3 = -(p1 + p2)
ps = [p1, p2, p3]

# Orthonormal transverse 3-frames for the symmetric Euclidean momenta.
E1 = sp.Matrix.hstack(sp.Matrix([0,1,0,0]), sp.Matrix([0,0,1,0]), sp.Matrix([0,0,0,1]))
E2 = sp.Matrix.hstack(sp.Matrix([-sqrt(3)/2,-sp.Rational(1,2),0,0]), sp.Matrix([0,0,1,0]), sp.Matrix([0,0,0,1]))
E3 = sp.Matrix.hstack(sp.Matrix([sqrt(3)/2,-sp.Rational(1,2),0,0]), sp.Matrix([0,0,1,0]), sp.Matrix([0,0,0,1]))
Es = [E1, E2, E3]

# Five orthonormal symmetric traceless tensors in each transverse 3-space.
mats = [sp.diag(1,-1,0)/sqrt(2), sp.diag(1,1,-2)/sqrt(6)]
for i,j in [(0,1),(0,2),(1,2)]:
    M = sp.zeros(3)
    M[i,j] = M[j,i] = 1/sqrt(2)
    mats.append(M)
bases = [[sp.simplify(E*M*E.T) for M in mats] for E in Es]

def lin_riemann(p, h):
    R = sp.MutableDenseNDimArray.zeros(D,D,D,D)
    for mu,nu,rho,sig in itertools.product(range(D), repeat=4):
        R[mu,nu,rho,sig] = sp.Rational(1,2)*(
            p[rho]*p[nu]*h[mu,sig] + p[sig]*p[mu]*h[nu,rho]
            - p[sig]*p[nu]*h[mu,rho] - p[rho]*p[mu]*h[nu,sig]
        )
    return R

def ricci_and_scalar(R):
    Ric = sp.zeros(D,D)
    for n in range(D):
        for s in range(D):
            Ric[n,s] = sum(R[m,n,m,s] for m in range(D))
    Sc = sum(Ric[i,i] for i in range(D))
    return Ric, sp.simplify(Sc)

def lin_weyl(p, h):
    R = lin_riemann(p, h)
    Ric, Sc = ricci_and_scalar(R)
    C = sp.MutableDenseNDimArray.zeros(D,D,D,D)
    for a,b,c,d in itertools.product(range(D), repeat=4):
        C[a,b,c,d] = sp.simplify(
            R[a,b,c,d]
            - sp.Rational(1,D-2)*(
                int(a==c)*Ric[d,b] - int(a==d)*Ric[c,b]
                - int(b==c)*Ric[d,a] + int(b==d)*Ric[c,a]
            )
            + Sc/sp.Rational((D-1)*(D-2))*(int(a==c and d==b) - int(a==d and c==b))
        )
    return C, Ric

def c3_contract(A, B, C):
    total = 0
    for r,s,m,n,a,b in itertools.product(range(D), repeat=6):
        total += A[r,s,m,n]*B[m,n,a,b]*C[a,b,r,s]
    return sp.simplify(total)

Cs = [[None]*5 for _ in range(3)]
Rs = [[None]*5 for _ in range(3)]
for leg in range(3):
    for i,h in enumerate(bases[leg]):
        C, Ric = lin_weyl(ps[leg], h)
        Cs[leg][i] = C
        Rs[leg][i] = Ric

def amp_c3(i,j,k):
    arr = [Cs[0][i], Cs[1][j], Cs[2][k]]
    return sp.simplify(sum(c3_contract(arr[a],arr[b],arr[c]) for a,b,c in itertools.permutations(range(3)))/6)

def amp_ric3(i,j,k):
    arr = [Rs[0][i], Rs[1][j], Rs[2][k]]
    return sp.simplify(sum(sp.trace(arr[a]*arr[b]*arr[c]) for a,b,c in itertools.permutations(range(3)))/6)

norm_c3 = sp.Rational(0)
norm_ric3 = sp.Rational(0)
inner = sp.Rational(0)
for i,j,k in itertools.product(range(5), repeat=3):
    a = amp_c3(i,j,k)
    b = amp_ric3(i,j,k)
    norm_c3 += a*a
    norm_ric3 += b*b
    inner += a*b

print('p_i^2 =', [sp.simplify(p.dot(p)) for p in ps])
print('p_i.p_j offdiag =', sp.simplify(ps[0].dot(ps[1])))
print('||T_C3||^2 =', sp.simplify(norm_c3))
print('||T_Ric3||^2 =', sp.simplify(norm_ric3))
print('<T_C3,T_Ric3> =', sp.simplify(inner))
print('naive C3 projector contamination from unit Ric3 =', sp.simplify(inner/norm_c3))
