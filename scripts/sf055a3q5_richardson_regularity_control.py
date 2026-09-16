#!/usr/bin/env python3
"""Q5 sharp-regulator regularity counterexample and Richardson bias control."""
from __future__ import annotations
import json, math
import sympy as sp

pi=sp.pi
a=sp.symbols('a', positive=True)
h=sp.symbols('h', positive=True)
A,B,C,F0=sp.symbols('A B C F0', real=True)

# S^3 angular measure relative to a fixed unit direction is 4*pi*sqrt(1-u^2) du.
u=sp.symbols('u', nonnegative=True)
I1=sp.simplify(4*pi*sp.integrate(u*sp.sqrt(1-u**2),(u,0,1)))
I2=sp.simplify(4*pi*sp.integrate(u**2*sp.sqrt(1-u**2),(u,0,1)))
I3=sp.simplify(4*pi*sp.integrate(u**3*sp.sqrt(1-u**2),(u,0,1)))

# Q4 shell expansion: radial integrals of excess and excess^2.
c2=sp.simplify(-I2/((2*pi)**4*a**2))
c3=sp.simplify((-(I1-sp.Rational(5,3)*I3)/a**2 + sp.Rational(4,3)*I3/a**3)/(2*pi)**4)

# Equal-weight sum over the three canonical rotated directions: each J is identical by O(4).
sym_c2=sp.simplify(3*c2)
sym_c3=sp.simplify(3*c3)

# Frozen Richardson estimator applied to F(p)=F0+A p^2+B p^3+C p^4 for p>0.
p=sp.symbols('p', positive=True)
F=lambda z: F0+A*z**2+B*z**3+C*z**4
D1=sp.simplify((F(h)-F0)/h**2)
D2=sp.simplify((F(2*h)-F0)/(2*h)**2)
R=sp.expand((4*D1-D2)/3)
bias=sp.simplify(R-A)

mu=sp.Rational(1,10)
a0=1+mu
h0=sp.Rational(1,32)
c2n=sp.N(c2.subs(a,a0),18)
c3n=sp.N(c3.subs(a,a0),18)
biasn=sp.N((sp.Rational(2,3)*c3*h).subs({a:a0,h:h0}),18)
relbias=sp.N(abs((sp.Rational(2,3)*c3*h/c2).subs({a:a0,h:h0})),18)

# A signed sum with weights summing to zero cancels every rotated copy; this is an extra coefficient relation.
weights=(sp.Integer(1),sp.Integer(1),sp.Integer(-2))
negative_c3=sp.simplify(sum(weights)*c3)

checks={
 'hemisphere_I1': sp.simplify(I1-4*pi/3)==0,
 'hemisphere_I2': sp.simplify(I2-pi**2/4)==0,
 'hemisphere_I3': sp.simplify(I3-8*pi/15)==0,
 'c2_formula': sp.simplify(c2+1/(64*pi**2*a**2))==0,
 'c3_formula': sp.simplify(c3-(8-5*a)/(180*pi**3*a**3))==0,
 'c3_nonzero_at_mu_0p1': sp.simplify(c3.subs(a,a0))!=0,
 'equal_weight_three_shift_c3_survives': sp.simplify(sym_c3.subs(a,a0))!=0,
 'richardson_result': sp.simplify(R-(A+sp.Rational(2,3)*B*h))==0,
 'p4_cancels': sp.diff(R,C)==0,
 'zero_sum_negative_control': negative_c3==0,
}
classification=('BOSE_ROTATIONAL_SYMMETRY_DOES_NOT_IMPLY_P2_ANALYTICITY_SCOPED'
                if all(checks.values()) else 'REGULARITY_CONTROL_FAILURE')
out={
 'classification':classification,
 'checks':checks,
 'hemisphere_moments':{'I1':str(I1),'I2':str(I2),'I3':str(I3)},
 'single_shift':{'c2':str(c2),'c3':str(c3),'mu_0p1_c2':float(c2n),'mu_0p1_c3':float(c3n)},
 'equal_weight_three_shift':{'c2':str(sym_c2),'c3':str(sym_c3),'mu_0p1_c3':float(sp.N(sym_c3.subs(a,a0),18))},
 'frozen_richardson':{'symbolic':str(R),'bias_from_abs_p3':str(bias),'h':'1/32',
    'scalar_bias':float(biasn),'scalar_relative_bias_magnitude':float(relbias)},
 'negative_control':{'weights':[1,1,-2],'c3':str(negative_c3),'meaning':'cancellation requires an extra coefficient relation; it is not forced by rotations'},
 'claim_ceiling':'Counterexample regularity class only. It does not prove a nonzero |p|^3 coefficient in the full tensor flow and does not change the frozen Q5 stencil.',
 'C3_enabled':False,
}
print(json.dumps(out,indent=2,sort_keys=True))
if not all(checks.values()): raise SystemExit(1)
