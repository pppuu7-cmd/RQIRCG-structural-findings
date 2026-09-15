#!/usr/bin/env python3
"""Replay an archived SF055A3 aggregate and audit derivative conditioning.

No gravity integrals are recomputed and no C3 coupling is enabled.  The separate
scalar integral is a regulator-regularity control, not a graviton amplitude.
Run with --input SF055A3_BASELINE_AGGREGATE.json --out SF055A3_DERIVATIVE_AUDIT.json.
Requires numpy, scipy and sympy. No network access or fitted parameters.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from pathlib import Path
import platform
import numpy as np
import scipy
from scipy.integrate import quad
import sympy as sp

NG_INV = 0.00052874519051635
NL_INV = 0.0026385724906858796
NG, NL, LAM, MU = 1/NG_INV, 1/NL_INV, -0.7, 0.1
NSEQ = (8, 12, 16, 24)
EXPECTED_CLASS = 'BLOCKED_LANE_A_BASELINE_QUADRATURE_NOT_CONVERGED_SCOPED'
PREREG = '052eb59b2155adbfbc2e52b6dbf0137525578e68'


def gauss(n: int, a: float, b: float):
    z, w = np.polynomial.legendre.leggauss(n)
    return a+(b-a)*(z+1)/2, (b-a)*w/2


def shell_delta(p: float, n: int, mu: float=MU) -> float:
    """J(p)-J(0), with the regulator sphere intersected before quadrature."""
    if not 0 < p < 1 or mu <= -1:
        raise ValueError('Require 0<p<1 and mu>-1')
    th, wt = gauss(n, 0, math.acos(-p/2))
    t, w = gauss(n, 0, 1)
    u = np.cos(th)[:, None]
    root = np.sqrt(1-p*p*(1-u*u))
    # Stable 1-r_b avoids subtracting nearly identical square roots.
    width = (2*p*u+p*p)/(1+p*u+root)
    rb = 1-width
    r = rb+width*t[None, :]
    excess = width*t[None, :]*(r+rb+2*p*u)
    a = 1+mu
    change = -excess/(a*(a+excess))
    return float(np.sum(wt[:, None]*w[None, :]*np.sin(th)[:, None]**2
                        *width*r**3*change)/(4*math.pi**3))


def adaptive_shell_delta(p: float, mu: float=MU) -> float:
    a=1+mu
    def angular(theta):
        u=math.cos(theta)
        root=math.sqrt(1-p*p*(1-u*u))
        width=(2*p*u+p*p)/(1+p*u+root)
        rb=1-width
        def radial(t):
            r=rb+width*t
            excess=width*t*(r+rb+2*p*u)
            return width*r**3*(-excess/(a*(a+excess)))
        inner=quad(radial,0,1,epsabs=1e-22,epsrel=2e-12)[0]
        return math.sin(theta)**2*inner
    return quad(angular,0,math.acos(-p/2),epsabs=1e-22,epsrel=2e-12)[0]/(4*math.pi**3)


def unsplit_delta(p: float, n: int, mu: float=MU) -> float:
    """The x,y,phi Gauss rule used in the archived implementation, scalar only."""
    x,wx=gauss(n,0,1); y,wy=gauss(n,0,1); phi,wp=gauss(n,0,2*math.pi)
    xx=x[:,None,None]; yy=y[None,:,None]; pp=phi[None,None,:]
    shifted=xx+2*p*np.sqrt(xx*(1-yy))*np.cos(pp)+p*p
    excess=np.maximum(shifted-1,0)
    a=1+mu
    change=-excess/(a*(a+excess))
    return float(np.sum(wx[:,None,None]*wy[None,:,None]*wp[None,None,:]
                        *xx*change)/(32*math.pi**3))


def close(a,b,atol=2e-12):
    return abs(float(a)-float(b))<=atol


def audit(path: Path):
    original=path.read_bytes()
    raw=json.loads(original)
    if raw.get('classification')!=EXPECTED_CLASS or raw.get('C3_enabled') is not False:
        raise ValueError('Unexpected source artifact or C3 not disabled')
    if raw.get('missing'):
        raise ValueError('Source aggregate reports missing inputs')
    h=sp.Rational(1,32)
    weights=[-sp.Rational(5,4)/h**2, sp.Rational(4,3)/h**2, -sp.Rational(1,12)/h**2]
    xs=[0,h,2*h]
    moments={str(k):sp.simplify(sum(w*x**k for w,x in zip(weights,xs))) for k in (0,2,3,4,6)}
    l1=sum(abs(w) for w in weights)
    checks={
      'source_classification_retained':raw['scientific_pass'] is False and raw['target_pass'] is True,
      'stencil_constant_null':moments['0']==0,
      'stencil_p2_exact':moments['2']==1,
      'stencil_p4_null':moments['4']==0,
      'stencil_p6_bias':moments['6']==-4*h**4,
      'stencil_abs_p3_not_cancelled':moments['3']==2*h/3,
      'stencil_l1_amplification':l1==sp.Rational(8,3)/h**2,
      'worst_case_error_bound_attained':sum(w*sp.sign(w) for w in weights)==l1,
    }
    replay={}
    for N in NSEQ:
        row=raw['beta_sequence'][str(N)]
        f0,f8,f16,f32=(row[k] for k in ('Flow_G_0','Flow_G_1_8','Flow_G_1_16','Flow_G_1_32'))
        d8=(f8-f0)/(1/8)**2; d16=(f16-f0)/(1/16)**2; d32=(f32-f0)/(1/32)**2
        R=(4*d32-d16)/3
        bg=2+2*NG*R
        bl=(-1-bg/2)*LAM+NL*row['Flow_Lambda_0']
        bm=-.2+(32*math.pi/5)*row['Flow_TT2_0']
        errors=[abs(bg-row['beta_g']),abs(bl-row['beta_lambda3']),abs(bm-row['beta_mu'])]
        replay[str(N)]={'derivative':R,'beta_g':bg,'beta_lambda3':bl,'beta_mu':bm,
             'derivative_insensitive_combination':bl+LAM*bg/2,
             'max_replay_error':max(errors)}
    checks['all_four_aggregate_rows_reproduced']=all(r['max_replay_error']<3e-12 for r in replay.values())
    b16,b24=raw['beta_sequence']['16'],raw['beta_sequence']['24']
    dr=b24['Flow_G_prime_0']-b16['Flow_G_prime_0']
    dfl=b24['Flow_Lambda_0']-b16['Flow_Lambda_0']
    dbg=b24['beta_g']-b16['beta_g']; dbl=b24['beta_lambda3']-b16['beta_lambda3']
    checks['delta_beta_g_from_one_derivative']=close(dbg,2*NG*dr)
    checks['delta_beta_lambda_from_derivative_and_p0']=close(dbl,-LAM*NG*dr+NL*dfl)
    R,F,L,nG,nL=sp.symbols('R F L nG nL')
    bg=2+2*nG*R; bl=(-1-bg/2)*L+nL*F
    combo=sp.expand(bl+L*bg/2)
    checks['combo_derivative_cancels_exactly']=sp.diff(combo,R)==0
    checks['jacobian_full_rank_two_not_global_rank_one']=sp.simplify(sp.det(sp.Matrix([bg,bl]).jacobian([R,F]))-2*nG*nL)==0
    combo_target=(raw['target_checks']['beta_lambda3']['target']
                  +LAM*raw['target_checks']['beta_g']['target']/2)
    combo24=replay['24']['derivative_insensitive_combination']
    amp=float(l1)*2*NG
    epsilon_sufficient=.002*abs(b24['beta_g'])/amp
    diag={'N16_to_N24_derivative_change':dr,
          'beta_g_change':dbg,'beta_lambda3_change':dbl,
          'beta_lambda_change_due_derivative':-LAM*NG*dr,
          'beta_lambda_change_due_Flambda0':NL*dfl,
          'combo_N24':combo24,'combo_target':combo_target,
          'combo_relative_target_error':abs(combo24-combo_target)/abs(combo_target),
          'derivative_stencil_weights':[str(x) for x in weights],
          'stencil_moments':{k:str(v) for k,v in moments.items()},
          'L1_derivative_amplification':float(l1),
          'L1_beta_g_amplification':amp,
          'worst_case_beta_g_change_for_each_input_change_le_2e_6':amp*2e-6,
          'sufficient_common_input_bound_for_0p2pct_beta_g':epsilon_sufficient,
          'bound_note':'Worst-case sufficient, NOT necessary. Inter-order differences are NOT certified error bounds.',
          'original_failed_convergence_keys':[k for k,v in raw['convergence'].items() if not v['pass']]}
    a=1+MU
    c2=-1/(64*math.pi**2*a*a)
    c3=(8-5*a)/(180*math.pi**3*a**3)
    scalar=[]
    for exp in (3,4,5,6,7,8,10,12):
        p=2.**(-exp)
        s24=shell_delta(p,24); s48=shell_delta(p,48)
        entry={'p':p,'J_delta_N24':s24,'J_delta_N48':s48,
          'coefficient_p2_N24':s24/(p*p),
          'ratio_to_analytic_c2':s24/(p*p*c2),
          'estimated_c3':(s24/(p*p)-c2)/p,
          'Richardson_N24':(4*s24/(p*p)-shell_delta(2*p,24)/(4*p*p))/3}
        scalar.append(entry)
    controls=[]
    for p in (1/8,1/32,1/256):
        adaptive=adaptive_shell_delta(p)
        gauss48=shell_delta(p,48)
        controls.append({'p':p,'adaptive':adaptive,'split_GL48':gauss48,
                         'relative_difference':abs(gauss48-adaptive)/abs(adaptive)})
    checks['independent_adaptive_and_split_GL_agree']=all(c['relative_difference']<1e-10 for c in controls)
    checks['split_GL24_to_GL48_stable']=all(abs(r['J_delta_N24']-r['J_delta_N48'])<2e-14 for r in scalar)
    checks['scalar_c2_analytic_limit']=abs(scalar[-1]['ratio_to_analytic_c2']-1)<1e-4
    checks['scalar_c3_exploratory_analytic_coefficient']=abs(scalar[-1]['estimated_c3']/c3-1)<1e-3
    unsplit=[]
    node_gaps={}
    for N in NSEQ:
        x,_=gauss(N,0,1)
        gap=1-math.sqrt(float(max(x)))
        node_gaps[str(N)]=gap
        safe_p=gap/4
        assert unsplit_delta(safe_p,N)==0
        for p in (1/8,1/16,1/32,safe_p):
            val=unsplit_delta(p,N)
            unsplit.append({'N':N,'p':p,'finite_N_delta':val,
                'finite_N_p2_coefficient':val/p**2,'safe_interior_test':p==safe_p})
    checks['all_finite_grids_miss_sufficiently_thin_shell']=all(r['finite_N_delta']==0 for r in unsplit if r['safe_interior_test'])
    checks['continuum_coefficient_nonzero_while_nodewise_derivative_zero']=c2!=0
    failures=[k for k,v in checks.items() if not v]
    return {'classification':'PASS_SCOPED_DERIVATIVE_CONDITIONING_AND_REGULATOR_SHELL_DIAGNOSTIC' if not failures else 'DIAGNOSTIC_CONTROL_FAILURE',
        'historical_classification':EXPECTED_CLASS,
        'programme_classification':'MISSING_OBJECT_OR_CONTROL_BLOCKER_SCOPED',
        'lane_A_terminal_pass':False,'sf055_terminal_pass':False,'C3_enabled':False,
        'new_quantum_principle_selected':False,'quantum_chi_ABC_computed':False,
        'checks':checks,'failures':failures,'aggregate_replay':replay,'conditioning':diag,
        'scalar_control':{'mu':MU,'J0':1/(32*math.pi**2*a),
          'analytic_c2':c2,'exploratory_analytic_abs_p3_coefficient':c3,
          'small_p_formula':'J=J0-p^2/[64*pi^2*(1+mu)^2]+(8-5*(1+mu))*abs(p)^3/[180*pi^3*(1+mu)^3]+O(p^4)',
          'split_sequences':scalar,'independent_integration_controls':controls,
          'unsplit_sequences':unsplit,'guaranteed_interior_p_gaps':node_gaps,
          'claim_ceiling':'Same regulator regularity class only; not the gravitational flow and not proof of its sole error source.'},
        'provenance':{'source_run':35019599951,'aggregate_artifact':10421617496,
          'source_head':'1828aeb994265cb78691493a21bdd4f120a30d58',
          'source_aggregate_sha256':hashlib.sha256(original).hexdigest(),
          'preregistration':PREREG,'execution':'local, synchronous; not a new GitHub Actions run',
          'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'sympy':sp.__version__}}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path,required=True)
    parser.add_argument('--out',type=Path,required=True)
    args=parser.parse_args()
    result=audit(args.input)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(result['classification'],'checks=',len(result['checks']),'failures=',result['failures'])
    print(json.dumps(result['conditioning'],indent=2))
    s=result['scalar_control']
    print('c2,c3',s['analytic_c2'],s['exploratory_analytic_abs_p3_coefficient'])
    print('smallest p control',s['split_sequences'][-1])
    print('adaptive controls',s['independent_integration_controls'])
    if result['failures']:
        raise SystemExit(1)

if __name__=='__main__':
    main()
