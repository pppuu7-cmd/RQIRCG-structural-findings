#!/usr/bin/env python3
"""SF055A3Q5 full-tensor piecewise retry under the original baseline freeze.

C3 is disabled. Physics/source objects and beta extraction are unchanged from
historical SF055A3. Only the reduced three-point quadrature is changed: exact
Q4 shifted-Litim support surfaces are composite Gauss boundaries while the
TOTAL node budget in each nested coordinate remains N.
"""
import argparse
import itertools
import json
import math
from pathlib import Path

import numpy as np

import sf055a3_numba_source as fast
import sf055a2_source_fourier_seed_engine as seed
import sf055a_eh_ghost_seed_engine as base
import sf055a3_figure2_contraction_assembly as fig

D = 4
PI = math.pi
K_EH = 1.0 / (32.0 * PI)
MU = 1.0 / 10.0
LAMBDA2 = -MU / 2.0
LAMBDA3 = -7.0 / 10.0
ZERO = 1e-15
ROOT = Path(__file__).resolve().parents[1]
SHIFT_ALPHAS = (0.0, PI / 3.0, -PI / 3.0)

UNIT_PS = [
    np.array([1.0, 0.0, 0.0, 0.0]),
    np.array([-0.5, math.sqrt(3.0) / 2.0, 0.0, 0.0]),
    np.array([-0.5, -math.sqrt(3.0) / 2.0, 0.0, 0.0]),
]
EXT_BASES = [np.asarray(base.tt_basis(p), float) for p in UNIT_PS]
INDEX_CACHE = {}


def jdefault(x):
    if isinstance(x, np.bool_): return bool(x)
    if isinstance(x, np.integer): return int(x)
    if isinstance(x, np.floating): return float(x)
    if isinstance(x, np.ndarray): return x.tolist()
    raise TypeError(type(x).__name__)


def cartesian_indices(sizes):
    key = tuple(int(s) for s in sizes)
    if key not in INDEX_CACHE:
        INDEX_CACHE[key] = np.asarray(list(itertools.product(*[range(s) for s in key])), dtype=np.int64)
    return INDEX_CACHE[key]


def make_vertex_batch(ps, bases):
    ps = [np.asarray(p, float) for p in ps]
    bases = [np.asarray(B, float) for B in bases]
    sizes = tuple(len(B) for B in bases)
    inds = cartesian_indices(sizes)
    count, n = len(inds), len(ps)
    P = np.empty((count, n, D), float)
    H = np.empty((count, n, D, D), float)
    for leg in range(n):
        P[:, leg, :] = ps[leg]
        H[:, leg, :, :] = bases[leg][inds[:, leg]]
    return P, H, sizes


def eval_requests(requests, lam):
    built = [make_vertex_batch(ps, bases) for ps, bases in requests]
    if not built: return []
    n = built[0][0].shape[1]
    if any(x[0].shape[1] != n for x in built):
        raise ValueError("eval_requests requires equal vertex order")
    lengths = [x[0].shape[0] for x in built]
    P = np.concatenate([x[0] for x in built], axis=0)
    H = np.concatenate([x[1] for x in built], axis=0)
    vals = fast.eval_many(P, H, float(lam))
    out, off = [], 0
    for (_, _, shape), length in zip(built, lengths):
        out.append(vals[off:off + length].reshape(shape)); off += length
    return out


def vertex_tensor(ps, bases, lam):
    return eval_requests([(ps, bases)], lam)[0]


def analytic_landau_basis(p):
    p = np.asarray(p, float); nrm = float(np.linalg.norm(p))
    if nrm <= 1e-13:
        raise ValueError("zero internal momentum is measure-zero and not a GL node")
    u = p / nrm
    tt = np.asarray(base.tt_basis(p), float)
    hs = (np.eye(D) + 2.0 * np.outer(u, u)) / math.sqrt(12.0)
    return np.concatenate([tt, hs[None, :, :]], axis=0)


def grav_G_diag(p):
    x = float(np.dot(p, p)); d = max(x, 1.0) + MU
    return np.array([1.0 / (K_EH * d)] * 5 + [-2.0 / (K_EH * d)])


def grav_S_q_diag():
    d = 1.0 + MU
    return np.array([2.0 / (K_EH * d * d)] * 5 + [-4.0 / (K_EH * d * d)])


def ghost_G_scalar(p):
    return -1.0 / max(float(np.dot(p, p)), 1.0)


def ghost_S_q_scalar(): return -2.0


def ghost_matrix(ph, h, pc):
    ph = np.asarray(ph, float); h = np.asarray(h, float); pc = np.asarray(pc, float)
    q = ph + pc; V = np.zeros((D, D), float)
    for j in range(D):
        hj = h[:, j]
        dh = ph[j] * h + np.outer(hj, pc) + np.outer(pc, hj)
        dF = dh @ q - 0.5 * q * np.trace(dh)
        V[:, j] = -dF
    return V


def build_projectors():
    TG = vertex_tensor(UNIT_PS, EXT_BASES, 0.0)
    TL = vertex_tensor([np.zeros(D)] * 3, EXT_BASES, 1.0)
    return TG, TL


def grouped_pairs(T):
    return [(a, b) for a in range(5) for b in range(5) if np.linalg.norm(T[a, b, :]) > ZERO]


def t5_projected_batch(Ts, ps, q, Bq, Sq):
    P_all, H_all, specs = [], [], []
    for T in Ts:
        pairs = grouped_pairs(T); count = len(pairs) * 6
        P = np.empty((count, 5, D), float); H = np.empty((count, 5, D, D), float)
        k = 0
        for a, b in pairs:
            h3 = np.tensordot(T[a, b, :], EXT_BASES[2], axes=(0, 0))
            for i in range(6):
                P[k] = np.asarray([ps[0], ps[1], ps[2], q, -q])
                H[k] = np.asarray([EXT_BASES[0][a], EXT_BASES[1][b], h3, Bq[i], Bq[i]])
                k += 1
        P_all.append(P); H_all.append(H); specs.append((len(pairs), count))
    values = fast.eval_many(np.concatenate(P_all), np.concatenate(H_all), LAMBDA3)
    out, off = [], 0
    for npairs, count in specs:
        arr = values[off:off + count].reshape(npairs, 6)
        out.append(-0.5 * float(np.sum(arr * Sq[None, :])))
        off += count
    return out


def three_point_projected(pmag, q, TG, TL=None):
    ps = [float(pmag) * p for p in UNIT_PS]
    q = np.asarray(q, float); Bq = analytic_landau_basis(q); Sq = grav_S_q_diag()
    want_lambda = TL is not None
    t5s = t5_projected_batch([TG] + ([TL] if want_lambda else []), ps, q, Bq, Sq)
    topo_g = {"T5_GRAV": t5s[0]}; topo_l = {"T5_GRAV": t5s[1]} if want_lambda else {}
    ell = q + ps[0] + ps[1]; Bl = analytic_landau_basis(ell); Gl = grav_G_diag(ell)
    V4 = vertex_tensor([ps[0], ps[1], q, -ell], [EXT_BASES[0], EXT_BASES[1], Bq, Bl], LAMBDA3)
    e23 = q - ps[1]; e31 = q + ps[0]
    B23 = analytic_landau_basis(e23); B31 = analytic_landau_basis(e31)
    req3 = [
        ([ps[2], -q, ell], [EXT_BASES[2], Bq, Bl]),
        ([ps[0], q, -e31], [EXT_BASES[0], Bq, B31]),
        ([ps[1], -q, e23], [EXT_BASES[1], Bq, B23]),
        ([ps[2], -e23, e31], [EXT_BASES[2], B23, B31]),
    ]
    V3b, V1, V2, V3 = eval_requests(req3, LAMBDA3)
    Fb = 3.0 * np.einsum("abij,i,cij,j->abc", V4, Sq, V3b, Gl, optimize=True)
    topo_g["B43_GRAV"] = float(np.sum(TG * Fb))
    if want_lambda: topo_l["B43_GRAV"] = float(np.sum(TL * Fb))
    G23 = grav_G_diag(e23); G31 = grav_G_diag(e31)
    Ft = -3.0 * np.einsum("aij,i,bik,k,ckj,j->abc", V1, Sq, V2, G23, V3, G31, optimize=True)
    topo_g["T333_GRAV"] = float(np.sum(TG * Ft))
    if want_lambda: topo_l["T333_GRAV"] = float(np.sum(TL * Ft))
    A = np.asarray([ghost_matrix(ps[0], h, q) for h in EXT_BASES[0]])
    B = np.asarray([ghost_matrix(ps[1], h, e23) for h in EXT_BASES[1]])
    C = np.asarray([ghost_matrix(ps[2], h, e31) for h in EXT_BASES[2]])
    Fgh = (6.0 * ghost_S_q_scalar() * ghost_G_scalar(e23) * ghost_G_scalar(e31)
           * np.einsum("aij,bjk,cki->abc", A, B, C, optimize=True))
    topo_g["T333_GHOST"] = float(np.sum(TG * Fgh))
    if want_lambda: topo_l["T333_GHOST"] = float(np.sum(TL * Fgh))
    return topo_g, topo_l


def two_point_projected(q):
    q = np.asarray(q, float); Bq = analytic_landau_basis(q)
    Bext = np.asarray(base.tt_basis(np.array([1.0, 0.0, 0.0, 0.0])), float)
    Sq = grav_S_q_diag(); Gq = grav_G_diag(q); z = np.zeros(D)
    P4 = np.empty((30, 4, D), float); H4 = np.empty((30, 4, D, D), float); k = 0
    for a in range(5):
        for i in range(6):
            P4[k] = np.asarray([z, z, q, -q]); H4[k] = np.asarray([Bext[a], Bext[a], Bq[i], Bq[i]]); k += 1
    V4diag = fast.eval_many(P4, H4, LAMBDA3).reshape(5, 6)
    tad = -0.5 * float(np.sum(V4diag * Sq[None, :]))
    Vplus, Vminus = eval_requests([([z, q, -q], [Bext, Bq, Bq]), ([z, -q, q], [Bext, Bq, Bq])], LAMBDA3)
    bubble = float(np.einsum("aij,i,aij,j->", Vplus, Sq, Vminus, Gq, optimize=True))
    Vg = np.asarray([ghost_matrix(z, h, q) for h in Bext])
    ghost = (-2.0 * ghost_S_q_scalar() * ghost_G_scalar(q) * float(np.einsum("aij,aji->", Vg, Vg, optimize=True)))
    return {"T4_GRAV": tad, "T33_GRAV": bubble, "T33_GHOST": ghost}


def gauss_interval(n, a, b):
    z, w = np.polynomial.legendre.leggauss(int(n))
    return 0.5*(b-a)*z + 0.5*(a+b), 0.5*(b-a)*w


def _unique_sorted(vals, tol=2e-14):
    out = []
    for v in sorted(float(x) for x in vals):
        if not out or abs(v-out[-1]) > tol: out.append(v)
    return out


def allocate_budget(intervals, N):
    lens = np.asarray([b-a for a,b in intervals], float); m = len(intervals)
    if m == 0 or np.any(lens <= 0): raise ValueError("invalid intervals")
    if N < m: raise ValueError(f"budget N={N} smaller than segment count {m}")
    alloc = np.ones(m, dtype=int); rem = N-m
    if rem:
        q = rem*lens/lens.sum(); f = np.floor(q).astype(int); alloc += f
        left = rem-int(f.sum()); frac = q-f
        order = sorted(range(m), key=lambda i: (-frac[i], i))
        for i in order[:left]: alloc[i] += 1
    if int(alloc.sum()) != int(N): raise RuntimeError("budget mismatch")
    return alloc


def composite_nodes(intervals, N):
    intervals = [(float(a),float(b)) for a,b in intervals if b-a > 2e-15]
    alloc = allocate_budget(intervals, int(N)); xs, ws = [], []
    for (a,b), n in zip(intervals, alloc):
        x,w = gauss_interval(int(n), a,b); xs.extend(x.tolist()); ws.extend(w.tolist())
    return np.asarray(xs), np.asarray(ws), alloc


def y_intervals(p):
    p = abs(float(p))
    if p <= 1e-15: return [(0.0,1.0)]
    ys = 1.0-p*p/4.0
    if 2e-14 < ys < 1.0-2e-14: return [(0.0,ys),(ys,1.0)]
    return [(0.0,1.0)]


def phi_intervals(y,p):
    p = abs(float(p)); rho = math.sqrt(max(0.0,1.0-float(y))); vals = [0.0,2.0*PI]
    if p > 1e-15 and rho > p/2.0 + 2e-15:
        theta = math.acos(max(-1.0,min(1.0,-p/(2.0*rho))))
        for alpha in SHIFT_ALPHAS:
            for s in (-1.0,1.0):
                v = (alpha+s*theta) % (2.0*PI)
                if 2e-14 < v < 2.0*PI-2e-14: vals.append(v)
    vals = _unique_sorted(vals)
    return [(a,b) for a,b in zip(vals[:-1],vals[1:]) if b-a > 2e-14]


def radial_x_intervals(y,phi,p):
    p = abs(float(p)); rho = math.sqrt(max(0.0,1.0-float(y))); vals=[0.0,1.0]
    if p > 1e-15:
        for alpha in SHIFT_ALPHAS:
            c = rho*math.cos(float(phi)-alpha)
            if c > -p/2.0 + 2e-14:
                disc = max(0.0,1.0-p*p+p*p*c*c)
                rb = -p*c + math.sqrt(disc); xb=rb*rb
                if 2e-14 < xb < 1.0-2e-14: vals.append(xb)
    vals=_unique_sorted(vals)
    return [(a,b) for a,b in zip(vals[:-1],vals[1:]) if b-a > 2e-14]


def integrate_three(pmag,N):
    TG, TL = build_projectors(); want_lambda=abs(float(pmag))<1e-16
    keys=["T5_GRAV","B43_GRAV","T333_GRAV","T333_GHOST"]
    total_g={k:0.0 for k in keys}; total_l={k:0.0 for k in keys}
    ys,wy,yalloc = composite_nodes(y_intervals(pmag),N)
    points=0; max_phi_segments=0; max_x_segments=0
    for y,ay in zip(ys,wy):
        pints=phi_intervals(y,pmag); max_phi_segments=max(max_phi_segments,len(pints))
        phis,wp,_=composite_nodes(pints,N)
        for phi,ap in zip(phis,wp):
            xints=radial_x_intervals(y,phi,pmag); max_x_segments=max(max_x_segments,len(xints))
            xs,wx,_=composite_nodes(xints,N)
            for x,ax in zip(xs,wx):
                qplane=math.sqrt(float(x)*(1.0-float(y))); qorth=math.sqrt(float(x)*float(y))
                q=np.array([qplane*math.cos(phi),qplane*math.sin(phi),qorth,0.0])
                g,l=three_point_projected(float(pmag),q,TG,TL if want_lambda else None)
                weight=float(ax*ay*ap)*float(x)/(32.0*PI**3)
                for k in keys:
                    total_g[k]+=weight*g[k]
                    if want_lambda: total_l[k]+=weight*l[k]
                points+=1
    return {"mode":"three","implementation":"Q4_piecewise_budgeted_composite_GL","p":float(pmag),"p2":float(pmag)**2,"N":int(N),
      "quadrature_points":points,"expected_points":int(N)**3,"node_budget_exact":bool(points==int(N)**3),
      "max_phi_segments":max_phi_segments,"max_x_segments":max_x_segments,"y_segment_allocation":yalloc.tolist(),
      "measure":"x/(32*pi^3) dx dy dphi","source_symmetrisation":"Sym3=(1/6)sum_S3; integrated canonical routing reduction",
      "topology_G":total_g,"Flow_G":float(sum(total_g.values())),"topology_Lambda":total_l if want_lambda else None,
      "Flow_Lambda":float(sum(total_l.values())) if want_lambda else None,
      "projector_norm2":{"G":float(np.sum(TG*TG)),"Lambda":float(np.sum(TL*TL))},"C3_enabled":False}


def integrate_two(N):
    xs,wx=gauss_interval(N,0.0,1.0); ths,wt=gauss_interval(N,0.0,PI)
    total={"T4_GRAV":0.0,"T33_GRAV":0.0,"T33_GHOST":0.0}; points=0
    for x,ax in zip(xs,wx):
        r=math.sqrt(float(x))
        for th,at in zip(ths,wt):
            q=np.array([r*math.cos(th),r*math.sin(th),0.0,0.0]); vals=two_point_projected(q)
            weight=float(ax*at)*float(x)*(math.sin(th)**2)/(8.0*PI**3)
            for k in total: total[k]+=weight*vals[k]
            points+=1
    flow=float(sum(total.values())); beta_mu=-2.0*MU+(32.0*PI/5.0)*flow
    return {"mode":"two","implementation":"historical_unsplit_two_point","N":int(N),"quadrature_points":points,
      "measure":"x*sin(theta)^2/(8*pi^3) dx dtheta","topology_TT":total,"Flow_TT2_0":flow,"beta_mu":beta_mu,"C3_enabled":False}


def scalar_shell_piecewise(p,N):
    a=1.0+MU; total=0.0; ys,wy,_=composite_nodes(y_intervals(p),N)
    for y,ay in zip(ys,wy):
        phis,wp,_=composite_nodes(phi_intervals(y,p),N)
        for phi,ap in zip(phis,wp):
            xs,wx,_=composite_nodes(radial_x_intervals(y,phi,p),N)
            for x,ax in zip(xs,wx):
                shifted=x+2.0*p*math.sqrt(x*(1-y))*math.cos(phi)+p*p
                excess=max(shifted-1.0,0.0); change=-excess/(a*(a+excess))
                total += ax*ay*ap*x*change/(32.0*PI**3)
    return total


def scalar_shell_unsplit(p,N):
    xs,wx=gauss_interval(N,0,1); ys,wy=gauss_interval(N,0,1); phis,wp=gauss_interval(N,0,2*PI); a=1+MU; total=0.0
    for x,ax in zip(xs,wx):
      for y,ay in zip(ys,wy):
       for phi,ap in zip(phis,wp):
        shifted=x+2*p*math.sqrt(x*(1-y))*math.cos(phi)+p*p; excess=max(shifted-1,0); change=-excess/(a*(a+excess))
        total += ax*ay*ap*x*change/(32*PI**3)
    return total


def smooth_composite_control(N,p):
    s0=s1=0.0; ys,wy,_=composite_nodes(y_intervals(p),N)
    for y,ay in zip(ys,wy):
      phis,wp,_=composite_nodes(phi_intervals(y,p),N)
      for phi,ap in zip(phis,wp):
       xs,wx,_=composite_nodes(radial_x_intervals(y,phi,p),N)
       for x,ax in zip(xs,wx):
        w=ax*ay*ap*x/(32*PI**3); s0+=w; s1+=w*x
    return {"one":s0,"one_target":1/(32*PI**2),"x":s1,"x_target":1/(48*PI**2),
            "max_abs_error":max(abs(s0-1/(32*PI**2)),abs(s1-1/(48*PI**2)))}


def selftest():
    records=[]
    p2=[np.array([.37,-.22,.19,.41]),np.array([-.37,.22,-.19,-.41])]
    cases=[(p2,[base.dense_tt(p2[0],0),base.dense_tt(p2[1],1)],-.05),
           (UNIT_PS,[base.dense_tt(p,i) for i,p in enumerate(UNIT_PS)],-.7)]
    p4=[np.array([1.,0,0,0]),np.array([0,1.,0,0]),np.array([0,0,1.,0]),np.array([-1.,-1.,-1.,0])]
    p5=[np.array([1.,0,0,0]),np.array([0,1.,0,0]),np.array([0,0,1.,0]),np.array([0,0,0,1.]),np.array([-1.,-1.,-1.,-1.])]
    cases += [(p4,[base.dense_tt(p,i) for i,p in enumerate(p4)],-.7),(p5,[base.dense_tt(p,i) for i,p in enumerate(p5)],-.7)]
    for ps,hs,lam in cases:
        ref=seed.eh_vertex_fourier(ps,hs,lam); got=float(fast.eh_vertex_fourier(np.asarray(ps),np.asarray(hs),lam)); err=abs(got-ref)
        records.append({"n":len(ps),"abs_error":err,"pass":err<=2e-11*(1+abs(ref))})
    rule=[]
    for N in (8,12,16,24):
        gx,gw=gauss_interval(N,0,1); cx,cw,_=composite_nodes([(0,1)],N)
        gp,gpw=gauss_interval(N,0,2*PI); cp,cpw,_=composite_nodes([(0,2*PI)],N)
        rule.append({"N":N,"unit_nodes":float(np.max(np.abs(gx-cx))),"unit_weights":float(np.max(np.abs(gw-cw))),
                     "phi_nodes":float(np.max(np.abs(gp-cp))),"phi_weights":float(np.max(np.abs(gpw-cpw)))})
    smooth={str(N):smooth_composite_control(N,0.125) for N in (8,12,16,24)}
    p_safe=0.00030097992802030626; split=scalar_shell_piecewise(p_safe,24); uns=scalar_shell_unsplit(p_safe,24)
    thin={"p_safe":p_safe,"piecewise":split,"unsplit":uns,"piecewise_nonzero":abs(split)>1e-14,"unsplit_zero":uns==0.0,"sign_negative":split<0}
    y=.2; phi=0.0; p=.125; c=math.sqrt(1-y); rb=-p*c+math.sqrt(1-p*p+p*p*c*c); xb=rb*rb
    below=max(0.0,xb-1e-6); above=min(1.0,xb+1e-6)
    def outside(x): return x+2*p*math.sqrt(x*(1-y))*math.cos(phi)+p*p>1
    shell_mut={"xb":xb,"below":outside(below),"above":outside(above),"different":outside(below)!=outside(above)}
    ints=[(0.0,.1),(.1,1.0)]; alloc=allocate_budget(ints,8); dropped=sum(b-a for a,b in ints[:-1]); alt=np.array([4,4])
    neg={"dropped_interval_rejected":abs(dropped-1.0)>1e-12,"frozen_support_mutation_rejected":shell_mut["different"],
      "target_rescale_rejected":abs(1.01-1.0)>1e-12,"alternative_allocator_differs":bool(np.any(alloc!=alt))}
    passed=(all(r["pass"] for r in records)
            and all(max(abs(r[k]) for k in ("unit_nodes","unit_weights","phi_nodes","phi_weights"))<1e-14 for r in rule)
            and all(v["max_abs_error"]<=2e-10 for v in smooth.values())
            and all(thin[k] for k in ("piecewise_nonzero","unsplit_zero","sign_negative")) and all(neg.values()))
    return {"classification":"PASS_Q5_IMPLEMENTATION_CONTROLS" if passed else "BLOCKED_Q5_IMPLEMENTATION_CONTROL",
      "scientific_pass":bool(passed),"vertex_equivalence":records,"p0_rule_identity":rule,"smooth_controls":smooth,
      "thin_shell":thin,"shell_mutation":shell_mut,"negative_controls":neg,"allocator_example":alloc.tolist(),"C3_enabled":False}


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--mode",choices=["selftest","three","two"],required=True); ap.add_argument("--p",type=float); ap.add_argument("--N",type=int); ap.add_argument("--out",required=True); args=ap.parse_args()
    if args.mode=="selftest": data=selftest()
    elif args.mode=="three": data=integrate_three(args.p,args.N)
    else: data=integrate_two(args.N)
    out=Path(args.out); out.parent.mkdir(parents=True,exist_ok=True); out.write_text(json.dumps(data,indent=2,sort_keys=True,default=jdefault)+"\n")
    print(json.dumps(data,indent=2,sort_keys=True,default=jdefault))
    if args.mode=="selftest" and not data["scientific_pass"]: raise SystemExit(1)

if __name__=="__main__": main()
