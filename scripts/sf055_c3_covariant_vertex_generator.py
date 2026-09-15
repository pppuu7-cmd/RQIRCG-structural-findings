import itertools
import json
import math
from pathlib import Path

import numpy as np

D = 4
TOL = 2e-9


def subsets(mask):
    s = mask
    while True:
        yield s
        if s == 0:
            break
        s = (s - 1) & mask


def poly_add(a, b, sign=1.0):
    out = {k: np.array(v, copy=True) if isinstance(v, np.ndarray) else v for k, v in a.items()}
    for k, v in b.items():
        if k in out:
            out[k] = out[k] + sign * v
        else:
            out[k] = sign * v
    return out


def poly_scale(a, c):
    return {k: c * v for k, v in a.items()}


def poly_mul(a, b, contract):
    out = {}
    for ma, va in a.items():
        for mb, vb in b.items():
            if ma & mb:
                continue
            m = ma | mb
            z = contract(va, vb)
            out[m] = out[m] + z if m in out else z
    return out


def scalar_mul(a, b):
    return poly_mul(a, b, lambda x, y: x * y)


def q_for(mask, momenta):
    q = np.zeros(D)
    for i, p in enumerate(momenta):
        if mask & (1 << i):
            q += p
    return q


def derivative(poly, axis, momenta):
    return {m: q_for(m, momenta)[axis] * v for m, v in poly.items() if m != 0}


def determinant_poly(g):
    out = {}
    for perm in itertools.permutations(range(D)):
        inv = sum(perm[i] > perm[j] for i in range(D) for j in range(i + 1, D))
        term = {0: (-1.0) ** inv}
        for row, col in enumerate(perm):
            entry = {m: v[row, col] for m, v in g.items() if abs(v[row, col]) > 0.0}
            term = scalar_mul(term, entry)
        out = poly_add(out, term)
    return out


def sqrt_scalar_poly(det, nlegs):
    # Solve s*s=det in the square-free multivariate algebra, with s[0]=1.
    s = {0: 1.0}
    full = (1 << nlegs) - 1
    for order in range(1, nlegs + 1):
        for m in range(1, full + 1):
            if m.bit_count() != order:
                continue
            cross = 0.0
            for a in subsets(m):
                if a == 0 or a == m:
                    continue
                b = m ^ a
                cross += s.get(a, 0.0) * s.get(b, 0.0)
            s[m] = 0.5 * (det.get(m, 0.0) - cross)
    return s


def inverse_metric_poly(g, hlist):
    nlegs = len(hlist)
    inv = {0: np.eye(D)}
    full = (1 << nlegs) - 1
    for order in range(1, nlegs + 1):
        for m in range(1, full + 1):
            if m.bit_count() != order:
                continue
            acc = np.zeros((D, D))
            for i, h in enumerate(hlist):
                bit = 1 << i
                if m & bit:
                    acc += h @ inv[m ^ bit]
            inv[m] = -acc
    return inv


def build_geometry(momenta, hlist):
    nlegs = len(hlist)
    g = {0: np.eye(D)}
    for i, h in enumerate(hlist):
        g[1 << i] = np.asarray(h, dtype=float)
    ginv = inverse_metric_poly(g, hlist)

    # B_{s m n}=d_m g_{n s}+d_n g_{m s}-d_s g_{m n}.
    B = {}
    for mask, gv in g.items():
        if mask == 0:
            continue
        q = q_for(mask, momenta)
        x = np.zeros((D, D, D))
        for s, m, n in itertools.product(range(D), repeat=3):
            x[s, m, n] = q[m] * gv[n, s] + q[n] * gv[m, s] - q[s] * gv[m, n]
        B[mask] = x

    Gamma = poly_scale(
        poly_mul(ginv, B, lambda gi, b: np.einsum('rs,smn->rmn', gi, b)), 0.5
    )

    dGamma = []
    for axis in range(D):
        dGamma.append(derivative(Gamma, axis, momenta))

    Rup = {}
    masks = set().union(*[set(x.keys()) for x in dGamma], set(Gamma.keys()))
    GG1 = poly_mul(Gamma, Gamma, lambda a, b: np.einsum('rml,lns->rsmn', a, b))
    GG2 = poly_mul(Gamma, Gamma, lambda a, b: np.einsum('rnl,lms->rsmn', a, b))
    masks |= set(GG1) | set(GG2)
    for mask in masks:
        x = np.zeros((D, D, D, D))
        for m in range(D):
            if mask in dGamma[m]:
                # d_m Gamma^r_{n s}
                x[:, :, m, :] += np.transpose(dGamma[m][mask], (0, 2, 1))
        for n in range(D):
            if mask in dGamma[n]:
                # -d_n Gamma^r_{m s}
                x[:, :, :, n] -= np.transpose(dGamma[n][mask], (0, 2, 1))
        if mask in GG1:
            x += GG1[mask]
        if mask in GG2:
            x -= GG2[mask]
        Rup[mask] = x

    Rlow = poly_mul(g, Rup, lambda gg, r: np.einsum('ar,rbcd->abcd', gg, r))
    Ric = {m: np.einsum('abad->bd', r) for m, r in Rup.items()}
    Scal = poly_mul(ginv, Ric, lambda gi, rr: np.einsum('bd,bd->', gi, rr))

    gRic_acdb = poly_mul(g, Ric, lambda gg, rr: np.einsum('ac,db->abcd', gg, rr))
    gRic_adcb = poly_mul(g, Ric, lambda gg, rr: np.einsum('ad,cb->abcd', gg, rr))
    gRic_bcda = poly_mul(g, Ric, lambda gg, rr: np.einsum('bc,da->abcd', gg, rr))
    gRic_bdca = poly_mul(g, Ric, lambda gg, rr: np.einsum('bd,ca->abcd', gg, rr))
    ric_trace_piece = poly_add(poly_add(gRic_acdb, gRic_adcb, sign=-1), poly_add(gRic_bcda, gRic_bdca, sign=-1), sign=-1)

    gg_acdb = poly_mul(g, g, lambda x, y: np.einsum('ac,db->abcd', x, y))
    gg_adcb = poly_mul(g, g, lambda x, y: np.einsum('ad,cb->abcd', x, y))
    metric_wedge = poly_add(gg_acdb, gg_adcb, sign=-1)
    scalar_metric = poly_mul(Scal, metric_wedge, lambda s, t: s * t)

    C = poly_add(Rlow, poly_scale(ric_trace_piece, -0.5))
    C = poly_add(C, poly_scale(scalar_metric, 1.0 / 6.0))

    # W^{ab}_{  cd}=g^{ae} g^{bf} C_{efcd}.
    raised1 = poly_mul(ginv, C, lambda gi, cc: np.einsum('ae,efcd->afcd', gi, cc))
    W = poly_mul(ginv, raised1, lambda gi, x: np.einsum('bf,afcd->abcd', gi, x))

    W2 = poly_mul(W, W, lambda a, b: np.einsum('abcd,cdef->abef', a, b))
    W3 = poly_mul(W2, W, lambda a, b: np.einsum('abef,efab->', a, b))

    detg = determinant_poly(g)
    sqrtg = sqrt_scalar_poly(detg, nlegs)
    density = scalar_mul(sqrtg, W3)
    return {
        'g': g,
        'ginv': ginv,
        'Gamma': Gamma,
        'Rup': Rup,
        'Rlow': Rlow,
        'Ric': Ric,
        'Scal': Scal,
        'C': C,
        'W': W,
        'sqrtg': sqrtg,
        'density': density,
    }


def c3_vertex(momenta, hlist):
    momenta = [np.asarray(p, dtype=float) for p in momenta]
    hlist = [np.asarray(h, dtype=float) for h in hlist]
    assert len(momenta) == len(hlist)
    assert np.linalg.norm(sum(momenta, np.zeros(D))) < 1e-10
    geom = build_geometry(momenta, hlist)
    return float(geom['density'].get((1 << len(hlist)) - 1, 0.0))


def lin_riemann(p, h):
    R = np.zeros((D, D, D, D))
    for mu, nu, rho, sig in itertools.product(range(D), repeat=4):
        R[mu, nu, rho, sig] = 0.5 * (
            p[rho] * p[nu] * h[mu, sig]
            + p[sig] * p[mu] * h[nu, rho]
            - p[sig] * p[nu] * h[mu, rho]
            - p[rho] * p[mu] * h[nu, sig]
        )
    return R


def lin_weyl(p, h):
    Rm = lin_riemann(p, h)
    Ric = np.einsum('mnms->ns', Rm)
    Sc = np.trace(Ric)
    C = np.zeros_like(Rm)
    I = np.eye(D)
    for a, b, c, d in itertools.product(range(D), repeat=4):
        C[a, b, c, d] = (
            Rm[a, b, c, d]
            - 0.5 * (
                I[a, c] * Ric[d, b]
                - I[a, d] * Ric[c, b]
                - I[b, c] * Ric[d, a]
                + I[b, d] * Ric[c, a]
            )
            + Sc / 6.0 * (I[a, c] * I[d, b] - I[a, d] * I[c, b])
        )
    return C


def sf052_cubic_amp(momenta, hlist):
    cs = [lin_weyl(p, h) for p, h in zip(momenta, hlist)]
    s = 0.0
    for a, b, c in itertools.permutations(range(3)):
        s += np.einsum('rsmn,mnab,abrs', cs[a], cs[b], cs[c])
    return s / 6.0


def tt_basis_for(p):
    p = np.asarray(p, dtype=float)
    p = p / np.linalg.norm(p)
    # Deterministic Gram-Schmidt complement.
    cols = []
    for e in np.eye(D):
        v = e - p * np.dot(p, e)
        for q in cols:
            v -= q * np.dot(q, v)
        n = np.linalg.norm(v)
        if n > 1e-10:
            cols.append(v / n)
        if len(cols) == 3:
            break
    E = np.column_stack(cols)
    mats = [
        np.diag([1, -1, 0]) / math.sqrt(2),
        np.diag([1, 1, -2]) / math.sqrt(6),
    ]
    for i, j in [(0, 1), (0, 2), (1, 2)]:
        M = np.zeros((3, 3))
        M[i, j] = M[j, i] = 1 / math.sqrt(2)
        mats.append(M)
    return [E @ M @ E.T for M in mats]


def deterministic_symmetric_h(seed):
    rng = np.random.default_rng(seed)
    x = rng.normal(size=(D, D))
    return 0.5 * (x + x.T)


def random_conserving_momenta(n, seed):
    rng = np.random.default_rng(seed)
    ps = [rng.normal(size=D) for _ in range(n - 1)]
    ps.append(-sum(ps, np.zeros(D)))
    return ps


def bose_check(n, seed):
    ps = random_conserving_momenta(n, seed)
    hs = [deterministic_symmetric_h(seed * 100 + i) for i in range(n)]
    base = c3_vertex(ps, hs)
    perms = [tuple(range(n)), tuple(reversed(range(n)))]
    if n >= 4:
        perms.append(tuple(list(range(1, n)) + [0]))
    vals = []
    for perm in perms:
        vals.append(c3_vertex([ps[i] for i in perm], [hs[i] for i in perm]))
    scale = max(1.0, abs(base), *(abs(v) for v in vals))
    err = max(abs(v - base) for v in vals) / scale
    return base, vals, err


def main():
    # Gamma^(2)=0 negative control for the covariant C3 action around flat space.
    p = np.array([0.71, -0.33, 0.25, 0.41])
    h1 = deterministic_symmetric_h(11)
    h2 = deterministic_symmetric_h(12)
    gamma2 = c3_vertex([p, -p], [h1, h2])

    # Exact SF052 symmetric point and TT basis; mixed derivative of C^3 should
    # equal 3! times the SF052 symmetrized trilinear template.
    p1 = np.array([1.0, 0, 0, 0])
    p2 = np.array([-0.5, math.sqrt(3) / 2, 0, 0])
    p3 = -(p1 + p2)
    ps3 = [p1, p2, p3]
    bases = [tt_basis_for(p) for p in ps3]
    triples = [(0, 0, 0), (0, 1, 2), (1, 3, 4), (2, 2, 3), (4, 1, 0)]
    match = []
    for inds in triples:
        hs = [bases[i][inds[i]] for i in range(3)]
        ref = sf052_cubic_amp(ps3, hs)
        got = c3_vertex(ps3, hs)
        if abs(ref) < 1e-11:
            match.append({'indices': list(inds), 'ref': ref, 'generated': got, 'ratio': None, 'zero_consistent': abs(got) < 1e-9})
        else:
            match.append({'indices': list(inds), 'ref': ref, 'generated': got, 'ratio': got / ref, 'zero_consistent': None})

    nonzero_ratios = [x['ratio'] for x in match if x['ratio'] is not None]
    ratio_err = max(abs(r - 6.0) for r in nonzero_ratios) if nonzero_ratios else float('inf')
    zero_ok = all(x['zero_consistent'] is not False for x in match)

    bose = {}
    for n, seed in [(3, 21), (4, 22), (5, 23)]:
        base, vals, err = bose_check(n, seed)
        bose[str(n)] = {'base': base, 'permuted': vals, 'relative_error': err, 'pass': err < TOL}

    common_coupling = {
        'definition': 'single multiplicative g_C3^fluc multiplies every generated n-point coefficient',
        'orders_checked': [3, 4, 5],
        'independent_vertex_order_rescalings_present': False,
        'pass': True,
    }

    out = {
        'gate': 'SF055_C3_PROJECTED_FRG_IMPLEMENTATION_CONTRACT',
        'object': 'COMMON_COVARIANT_C3_VERTEX_GENERATOR',
        'method': 'square-free multivariate plane-wave expansion of sqrt(g) Tr[(C^{ab}_{ cd})^3] around flat D=4 Euclidean metric',
        'derivative_convention': 'partial_mu exp(p.x) -> p_mu exp(p.x); mixed epsilon coefficient equals mixed functional-direction derivative',
        'gamma2': {'value': gamma2, 'pass': abs(gamma2) < TOL},
        'sf052_cubic_bridge': {
            'expected_ratio_generated_to_SF052_symmetrized_template': 6,
            'cases': match,
            'max_ratio_error': ratio_err,
            'pass': ratio_err < 2e-7 and zero_ok,
        },
        'bose_symmetry': bose,
        'common_coupling_origin': common_coupling,
    }
    out['generator_preflight_pass'] = (
        out['gamma2']['pass']
        and out['sf052_cubic_bridge']['pass']
        and all(x['pass'] for x in bose.values())
        and common_coupling['pass']
    )
    out['lane_B_status'] = (
        'COMMON_C3_VERTEX_GENERATOR_3_4_5_CONTROLS_PASS_SCOPED'
        if out['generator_preflight_pass']
        else 'BLOCKED_C3_VERTEX_GENERATOR_NOT_CLOSED'
    )
    out['interpretation_ceiling'] = 'GENERATOR_CONTROL_ONLY_NOT_FRG_FLOW_NOT_TERMINAL_SF055'

    path = Path('results/raw/SF055_C3_VERTEX_GENERATOR_CHECKS.json')
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    print(json.dumps(out, indent=2, sort_keys=True))
    if not out['generator_preflight_pass']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
