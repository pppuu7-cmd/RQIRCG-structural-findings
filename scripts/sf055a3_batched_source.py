#!/usr/bin/env python3
"""Exact batched lift of the validated SF055A2 source-Fourier EH vertex algebra.

Leading array axes label independent component evaluations. The square-free
mask algebra and Fourier convention are unchanged.
"""
import math
import numpy as np

D = 4
PI = math.pi
EH_PREF = 1.0 / (16.0 * PI)


def padd(A, B):
    out = {k: np.array(v, copy=True) for k, v in A.items()}
    for k, v in B.items():
        out[k] = out[k] + v if k in out else np.array(v, copy=True)
    return out


def pscale(A, c):
    return {k: c * v for k, v in A.items()}


def peinsum(A, B, subs):
    out = {}
    for ma, a in A.items():
        for mb, b in B.items():
            if ma & mb:
                continue
            m = ma | mb
            v = np.einsum(subs, a, b, optimize=True)
            out[m] = out[m] + v if m in out else v
    return out


def pscalar_mul(A, B):
    out = {}
    for ma, a in A.items():
        for mb, b in B.items():
            if ma & mb:
                continue
            m = ma | mb
            v = a * b
            out[m] = out[m] + v if m in out else v
    return out


def _broadcast_inputs(ps, hs):
    shapes = [np.asarray(p).shape[:-1] for p in ps] + [np.asarray(h).shape[:-2] for h in hs]
    batch = np.broadcast_shapes(*shapes) if shapes else ()
    P = [np.broadcast_to(np.asarray(p, float), batch + (D,)) for p in ps]
    H = [np.broadcast_to(np.asarray(h, float), batch + (D, D)) for h in hs]
    return batch, P, H


def inverse_metric(hs, batch):
    H = {1 << i: h for i, h in enumerate(hs)}
    I = np.broadcast_to(np.eye(D), batch + (D, D))
    out = {0: I.copy()}
    power = {0: I.copy()}
    for r in range(1, len(hs) + 1):
        power = peinsum(power, H, "...ab,...bc->...ac")
        out = padd(out, pscale(power, (-1) ** r))
    return out


def sqrt_det_metric(hs, batch):
    n = len(hs)
    H = {1 << i: h for i, h in enumerate(hs)}
    I = np.broadcast_to(np.eye(D), batch + (D, D))
    log_half = {}
    power = {0: I.copy()}
    for r in range(1, n + 1):
        power = peinsum(power, H, "...ab,...bc->...ac")
        tr = {m: np.trace(v, axis1=-2, axis2=-1) for m, v in power.items()}
        log_half = padd(log_half, pscale(tr, 0.5 * ((-1) ** (r + 1)) / r))
    one = np.ones(batch, float)
    out = {0: one}
    power_s = {0: one}
    for r in range(1, n + 1):
        power_s = pscalar_mul(power_s, log_half)
        out = padd(out, pscale(power_s, 1.0 / math.factorial(r)))
    return out


def scalar_curvature_fourier(ps, hs, batch):
    gi = inverse_metric(hs, batch)
    dg = {
        1 << i: 1j * np.einsum("...a,...mn->...amn", p, h, optimize=True)
        for i, (p, h) in enumerate(zip(ps, hs))
    }
    B = {}
    for mask, a in dg.items():
        B[mask] = (
            np.einsum("...msn->...smn", a, optimize=True)
            + np.einsum("...nsm->...smn", a, optimize=True)
            - a
        )
    Gamma = pscale(peinsum(gi, B, "...rs,...smn->...rmn"), 0.5)
    dGamma = {}
    for mask, a in Gamma.items():
        if mask == 0:
            continue
        q = np.zeros(batch + (D,), float)
        for i, p in enumerate(ps):
            if (mask >> i) & 1:
                q = q + p
        dGamma[mask] = 1j * np.einsum("...a,...rmn->...armn", q, a, optimize=True)
    Rmix = {}
    for mask, a in dGamma.items():
        Rmix[mask] = (
            np.einsum("...mrns->...rsmn", a, optimize=True)
            - np.einsum("...nrms->...rsmn", a, optimize=True)
        )
    gg1 = peinsum(Gamma, Gamma, "...rml,...lns->...rsmn")
    gg2 = peinsum(Gamma, Gamma, "...rnl,...lms->...rsmn")
    Rmix = padd(Rmix, padd(gg1, pscale(gg2, -1.0)))
    Ric = {m: np.einsum("...rsrn->...sn", a, optimize=True) for m, a in Rmix.items()}
    return peinsum(gi, Ric, "...sn,...sn->...")


def eh_vertex_fourier(ps, hs, lam):
    batch, P, H = _broadcast_inputs(ps, hs)
    total = np.zeros(batch + (D,), float)
    for p in P:
        total = total + p
    if np.max(np.linalg.norm(total, axis=-1)) > 2e-10:
        raise ValueError("EH vertex requires conserved Fourier momenta")
    sqrtg = sqrt_det_metric(H, batch)
    Rsc = scalar_curvature_fourier(P, H, batch)
    core = pscale(Rsc, -1.0)
    core = padd(core, {0: np.full(batch, 2.0 * float(lam))})
    density = pscale(pscalar_mul(sqrtg, core), EH_PREF)
    full = (1 << len(P)) - 1
    value = np.real_if_close(density.get(full, np.zeros(batch)), tol=1000)
    if np.iscomplexobj(value) and np.max(np.abs(np.imag(value))) > 1e-10:
        raise ValueError("unexpected complex EH vertex")
    return np.real(value).astype(float)


def vertex_tensor(ps, bases, lam):
    """Return the complete multilinear vertex tensor over supplied leg bases."""
    n = len(ps)
    sizes = [len(b) for b in bases]
    shape = tuple(sizes)
    hs = []
    pbatch = []
    for i, (p, B) in enumerate(zip(ps, bases)):
        B = np.asarray(B, float)
        rs = [1] * n + [D, D]
        rs[i] = sizes[i]
        h = np.broadcast_to(B.reshape(tuple(rs)), shape + (D, D)).reshape((-1, D, D))
        hs.append(h)
        pbatch.append(np.broadcast_to(np.asarray(p, float), (h.shape[0], D)))
    return eh_vertex_fourier(pbatch, hs, lam).reshape(shape)
