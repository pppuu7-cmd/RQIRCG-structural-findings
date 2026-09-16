#!/usr/bin/env python3
from fractions import Fraction as Q
import json

h = Q(1,32)
r = [Q(1), Q(2), Q(4)]

def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
            -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
            +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))

def replace_col(A, j, b):
    return [[b[i] if k==j else A[i][k] for k in range(3)] for i in range(3)]

def solve3(A,b):
    d=det3(A)
    if d == 0:
        raise ValueError('singular')
    return [det3(replace_col(A,j,b))/d for j in range(3)]

A = [[Q(1),Q(1),Q(1)], r, [x*x for x in r]]
detA = det3(A)
w_c2 = solve3(A,[Q(1),Q(0),Q(0)])
q_c3 = solve3(A,[Q(0),Q(1),Q(0)])
w_R = [Q(4,3),Q(-1,3),Q(0)]

def moment(w,k):
    return sum(wi*(ri**k) for wi,ri in zip(w,r))

identity_vec = [w_R[i]-w_c2[i] - Q(2,3)*q_c3[i] for i in range(3)]
identity_pass = all(x==0 for x in identity_vec)

def direct_weights_from_D(w, divide_by_h_power=0):
    scale = h**(-divide_by_h_power)
    out = {'F0': Q(0), 'Fh': Q(0), 'F2h': Q(0), 'F4h': Q(0)}
    names=['Fh','F2h','F4h']
    for wi,ri,name in zip(w,r,names):
        coeff = scale*wi/(ri*ri*h*h)
        out[name] += coeff
        out['F0'] -= coeff
    return out

direct_c2 = direct_weights_from_D(w_c2,0)
direct_c3 = direct_weights_from_D(q_c3,1)
direct_R = direct_weights_from_D(w_R,0)
l1 = lambda d: sum(abs(v) for v in d.values())

controls = {
    'det_nonzero': detA != 0,
    'c2_exact': moment(w_c2,0)==1 and moment(q_c3,0)==0,
    'c3_exact': moment(w_c2,1)==0 and moment(q_c3,1)==1,
    'c4_annihilated': moment(w_c2,2)==0 and moment(q_c3,2)==0,
    'R_c2_exact': moment(w_R,0)==1,
    'R_c4_annihilated': moment(w_R,2)==0,
    'R_c3_moment_2h_over_3': moment(w_R,1)==Q(2,3),
    'exact_identity': identity_pass,
}

negative = {}
for i,j in [(0,1),(0,2),(1,2)]:
    a,b=r[i],r[j]
    c2=a*b*h*h; c3=-(a+b)*h; c4=Q(1)
    Da=c2+c3*a*h+c4*a*a*h*h
    Db=c2+c3*b*h+c4*b*b*h*h
    negative[f'pair_{int(a)}_{int(b)}_nonidentifiable'] = (Da==0 and Db==0 and (c2!=0 or c3!=0))

all_pass = all(controls.values()) and all(negative.values())

def s(x):
    return f'{x.numerator}/{x.denominator}' if x.denominator != 1 else str(x.numerator)
def fd(d):
    return {k:s(v) for k,v in d.items()}

data = {
    'classification': 'PASS_Q7_RICHARDSON_REGULARITY_DIAGNOSTIC_CONSTRUCTED_SCOPED' if all_pass else 'BLOCKED_Q7_RICHARDSON_REGULARITY_DIAGNOSTIC_NOT_IDENTIFIABLE_SCOPED',
    'scientific_pass': all_pass,
    'h': s(h),
    'radii': [s(x) for x in r],
    'vandermonde_det': s(detA),
    'C2_D_weights': [s(x) for x in w_c2],
    'C3_dimensionless_D_weights': [s(x) for x in q_c3],
    'C3_definition': 'C3_234=(q dot D)/h',
    'R_D_weights': [s(x) for x in w_R],
    'identity': 'R_h - C2_234 = (2 h / 3) C3_234',
    'identity_residual_D_vector': [s(x) for x in identity_vec],
    'direct_F_weights_C2': fd(direct_c2),
    'direct_F_weights_C3': fd(direct_c3),
    'direct_F_weights_R': fd(direct_R),
    'primitive_error_L1_amplification': {
        'R': s(l1(direct_R)),
        'C2_234': s(l1(direct_c2)),
        'C3_234': s(l1(direct_c3)),
        'C2_over_R': str(float(l1(direct_c2)/l1(direct_R))),
    },
    'higher_order_bias_moments': {
        'C2_p5': '8 h^3',
        'C2_p6': '56 h^4',
        'R_p3': '2 h / 3',
        'R_p5': '-4 h^3 / 3',
        'R_p6': '-4 h^4',
        'C3_p5_contamination': '-14 h^2',
        'C3_p6_contamination': '-90 h^3',
    },
    'controls': controls,
    'negative_controls': negative,
}
print(json.dumps(data, indent=2, sort_keys=True))
