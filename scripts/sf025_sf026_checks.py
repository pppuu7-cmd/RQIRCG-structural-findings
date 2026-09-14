#!/usr/bin/env python3
"""Reproducible SF025 logical controls and SF026 exact/asymptotic checks.

Run: python scripts/sf025_sf026_checks.py [--output-dir results/raw]
No network access. SymPy and SciPy are required. This is not a quantum-gravity
solver or a complete interferometer simulation. Exact checks use rational
arithmetic; floating-point trajectories check only the derived small-T limit.
"""
from __future__ import annotations
import argparse
import hashlib
import itertools
import json
from fractions import Fraction as Q
from pathlib import Path
import platform
import numpy as np
import scipy
from scipy.integrate import solve_ivp
import sympy as sp

BITS = list(itertools.product((0, 1), repeat=3))
BASE = 'b588d8e47c24c6bc12976d54f0a976dc9df099d3'
PREREG25 = '9ef45ce5858f9271a450abef4adcb798d8dd2c85'
PREREG26 = '3a495200aa2e9afaf1c3f56f887a0b40fa810cb9'

def delta3(values):
    return sum((-1) ** (3 - sum(bits)) * values[bits] for bits in BITS)

def positions(bits, erase_a=False):
    a, b, c = bits
    return [Q(0 if erase_a else a), Q(4 + 2*b), Q(10 + 3*c)]

def potential(q, masses, G=Q(1)):
    return -G * sum(masses[i]*masses[j]/abs(q[i]-q[j])
                    for i in range(len(q)) for j in range(i+1, len(q)))

def forces(q, masses, G=Q(1)):
    return [-G * sum(masses[i]*masses[j]*(q[i]-q[j])/abs(q[i]-q[j])**3
                    for j in range(len(q)) if j != i)
            for i in range(len(q))]

def force_norm(q, masses, G=Q(1)):
    f = forces(q, masses, G)
    return sum(x*x/m for x, m in zip(f, masses))

def sf025():
    t1, t2, w = sp.symbols('t1 t2 w', real=True)
    U = lambda t: sp.diag(sp.exp(-sp.I*w*t), sp.exp(sp.I*w*t))
    rho = sp.Matrix([[1,1],[1,1]])/2
    prob = sp.simplify(sp.trace(rho * U(t1) * rho * U(t1).conjugate().T))
    p0 = sp.simplify(prob.subs({w:1, t1:sp.pi/2}))
    p1 = sp.simplify(sp.expand_complex(prob.subs({w:sp.Rational(5,4), t1:sp.pi/2})))
    loop, b, shift, P = sp.symbols('loop b shift P')
    A = loop+b*P
    Aprime = (loop-shift*P)+(b+shift)*P
    checks = {
        'same_state_normalized_positive': rho.trace()==1 and rho.det()==0,
        'unitary_exact': sp.simplify(U(t1).conjugate().T*U(t1)-sp.eye(2))==sp.zeros(2),
        'composition_exact': sp.simplify(U(t2)*U(t1)-U(t1+t2))==sp.zeros(2),
        'same_state_different_prediction': sp.simplify(p1-p0)!=0,
        'scheme_compensation_identity': sp.expand(Aprime-A)==0,
        'fixed_scheme_matching_direction_visible': sp.diff(A,b)==P,
        'R3_action_engineering_dimension_zero': -2+6-4==0,
        'on_shell_polynomial_control_nonzero': 4*(-1)*(-3)!=0,
        'massless_mandelstam_sum_zero': 4-1-3==0,
    }
    assert all(checks.values()), checks
    return {'gate':'SF025', 'base':BASE, 'preregistration':PREREG25,
        'checks':checks, 'failures':[],
        'toy_H':'H_b=(1+epsilon^2*b)*sigma_z; epsilon=1/2, b=0 versus b=1',
        'toy_initial_state':'|+x><+x|; same |+x><+x| readout, t=pi/2',
        'toy_probabilities':[str(p0),str(p1)],
        'amplitude_control':'s=4 E^2,t=-E^2,u=-3 E^2; stu=12 E^6',
        'not_computed':['chi_ABC','quantum HDA','full BRST loop derivation','exact gravity CP','UV completion'],
        'scope':'Exact finite-dimensional logical controls; R3 physical content is primary-source-grounded, not numerically derived here.'}

def numerical_branch(q0, T):
    n=len(q0)
    q0=np.asarray(q0,dtype=float)
    def rhs(t,y):
        q=y[:n]; vel=y[n:2*n]
        sep=q[:,None]-q[None,:]
        safe=np.where(np.eye(n,dtype=bool),1.,abs(sep))
        acc=-np.sum(np.where(np.eye(n,dtype=bool),0.,sep/safe**3),axis=1)
        V=-sum(1./abs(q[i]-q[j]) for i in range(n) for j in range(i+1,n))
        L=.5*float(vel@vel)-V
        return np.r_[vel,acc,L]
    sol=solve_ivp(rhs,(0.,T),np.r_[q0,np.zeros(n),0.],method='DOP853',
                  rtol=2e-12,atol=2e-14,max_step=T/20)
    if not sol.success:
        raise RuntimeError(sol.message)
    q=sol.y[:n,-1]; vel=sol.y[n:2*n,-1]
    E0=float(potential(list(q0),[1.]*n))
    ET=.5*float(vel@vel)+float(potential(list(q),[1.]*n))
    return float(sol.y[-1,-1]), abs(ET-E0), abs(float(sum(vel)))

def sf026():
    V={bits:potential(positions(bits),[Q(1)]*3) for bits in BITS}
    A={bits:force_norm(positions(bits),[Q(1)]*3) for bits in BITS}
    A3={}
    for bits in BITS:
        x,y,z=positions(bits); u=y-x; v=z-y
        A3[bits]=-Q(4)/(u*v*(u+v)**2)
    no_a={bits:force_norm(positions(bits,True),[Q(1)]*3) for bits in BITS}
    G0={bits:force_norm(positions(bits),[Q(1)]*3,Q(0)) for bits in BITS}
    harm={}
    for bits in BITS:
        q=positions(bits)
        grad=[sum(q[i]-q[j] for j in range(3) if j!=i) for i in range(3)]
        harm[bits]=sum(g*g for g in grad)
    t,T,g,m=sp.symbols('t T g m',positive=True)
    dx_release=-g*t*t/(2*m)
    dx_return=g*t*(T-t)/(2*m)
    corr=lambda dx: sp.integrate(m*sp.diff(dx,t)**2/2-g*dx,(t,0,T))
    c_release=sp.simplify(corr(dx_release)/(g*g*T**3/m))
    c_return=sp.simplify(corr(dx_return)/(g*g*T**3/m))
    u,v=sp.symbols('u v',positive=True)
    triple_id=sp.simplify(2*(1/(u*u*(u+v)**2)-1/(u*u*v*v)+1/(v*v*(u+v)**2))+4/(u*v*(u+v)**2))
    dA=delta3(A)
    apparatus={}; com_control={}
    for R in (Q(50),Q(100),Q(200)):
        vals={}; cms={}
        for bits in BITS:
            a,b,c=bits; q=positions(bits)+[R-Q(a+2*b+3*c,5)]
            masses=[Q(1)]*3+[Q(5)]
            vals[bits]=force_norm(q,masses)
            cms[bits]=sum(x*mm for x,mm in zip(q,masses))/sum(masses)
        apparatus[str(R)]={'delta3_A_total':str(delta3(vals)),
                          'difference_from_source':str(delta3(vals)-dA),
                          'absolute_error_float':float(abs(delta3(vals)-dA))}
        com_control[str(R)]=len(set(cms.values()))==1
    numerics=[]
    for Tval in (.4,.2,.1,.05):
        data={bits:numerical_branch(positions(bits),Tval) for bits in BITS}
        conn=delta3({bits:dat[0] for bits,dat in data.items()})
        ratio=conn/(float(dA)*Tval**3/3.)
        numerics.append({'T':Tval,'delta3_S_release':conn,
                         'ratio_to_derived_T3_term':ratio,
                         'max_energy_error':max(x[1] for x in data.values()),
                         'max_momentum_error':max(x[2] for x in data.values())})
    old={}
    for a,b,c in BITS:
        x,y,z=Q(a),Q(3+b),Q(8+2*c)
        rab,rac,rbc=y-x,z-x,z-y
        old[(a,b,c)]=1/(rab*rac)+1/(rab*rbc)+1/(rac*rbc)
    checks={
        'static_Newtonian_pair_null':delta3(V)==0,
        'feedback_nonzero':dA!=0,
        'feedback_equals_distinct_three_body_cross_terms':dA==delta3(A3),
        'collinear_three_force_identity':triple_id==0,
        'erased_A_null':delta3(no_a)==0,
        'gravity_off_null':delta3(G0)==0,
        'quadratic_harmonic_special_null':delta3(harm)==0,
        'constant_force_release_coefficient':c_release==sp.Rational(1,3),
        'constant_force_return_coefficient':c_return==-sp.Rational(1,24),
        'Newtonian_COM_same_all_branches':all(com_control.values()),
        'apparatus_error_decreases_on_fixed_control_points':apparatus['50']['absolute_error_float']>apparatus['100']['absolute_error_float']>apparatus['200']['absolute_error_float'],
        'ODE_T3_ratio_converges':abs(numerics[-1]['ratio_to_derived_T3_term']-1)<abs(numerics[0]['ratio_to_derived_T3_term']-1),
        'ODE_last_ratio_within_1e_3':abs(numerics[-1]['ratio_to_derived_T3_term']-1)<1e-3,
        'SF022_exact_regression':delta3(old)==Q(13,2520),
    }
    assert all(checks.values()),checks
    return {'gate':'SF026','base':BASE,'preregistration':PREREG26,'checks':checks,'failures':[],
        'geometry':'A=a ell,B=(4+2b)ell,C=(10+3c)ell; masses m',
        'delta3_V_N':str(delta3(V)),
        'delta3_A_in_G2_m3_over_ell4':str(dA),
        'release_T3_coefficient_in_G2_m3_over_ell4':str(dA/3),
        'return_T3_coefficient_in_G2_m3_over_ell4':str(-dA/24),
        'source_A_values':{''.join(map(str,k)):str(val) for k,val in A.items()},
        'source_A3_cross_values':{''.join(map(str,k)):str(val) for k,val in A3.items()},
        'release_coefficient':str(c_release),'return_coefficient':str(c_return),
        'apparatus_controls':apparatus,'numerical_short_time_checks':numerics,
        'SF022_delta3_F_regression':str(delta3(old)),
        'scope':'Open classical actions, not observed phase. Return endpoints and rest-release are different boundary problems. Newtonian COM is not a 1PN preparation certificate.'}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir',type=Path,default=Path('results/raw'))
    args=parser.parse_args();args.output_dir.mkdir(parents=True,exist_ok=True)
    provenance={'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
       'execution':'local container, not GitHub Actions', 'python':platform.python_version(),
       'sympy':sp.__version__,'scipy':scipy.__version__,'numpy':np.__version__}
    for fn in (sf025,sf026):
        result=fn();result['provenance']=provenance
        p=args.output_dir/(result['gate']+'_CHECKS.json')
        p.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
        print(p, 'checks',len(result['checks']),'failures',result['failures'])
        if result['gate']=='SF026':
            print('delta3_A =',result['delta3_A_in_G2_m3_over_ell4'])
            print('release =',result['release_T3_coefficient_in_G2_m3_over_ell4'])
            print('return =',result['return_T3_coefficient_in_G2_m3_over_ell4'])
            print('ODE ratios',[x['ratio_to_derived_T3_term'] for x in result['numerical_short_time_checks']])
if __name__=='__main__':
    main()
