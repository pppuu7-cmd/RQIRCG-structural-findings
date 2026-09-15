#!/usr/bin/env python3
"""Numba JIT implementation of the validated square-free source-Fourier EH vertex.

This is an execution backend only. It computes the same full-mask coefficient
as sf055a2_source_fourier_seed_engine.eh_vertex_fourier.
"""
import math
import numpy as np
from numba import njit

D = 4
EH_PREF = 1.0 / (16.0 * math.pi)


@njit(cache=True)
def _matpoly_mul(A, B, M):
    out = np.zeros((M, D, D), np.float64)
    for ma in range(M):
        for mb in range(M):
            if ma & mb:
                continue
            mm = ma | mb
            for i in range(D):
                for j in range(D):
                    s = 0.0
                    for k in range(D):
                        s += A[ma, i, k] * B[mb, k, j]
                    out[mm, i, j] += s
    return out


@njit(cache=True)
def _scalpoly_mul(A, B, M):
    out = np.zeros(M, np.float64)
    for ma in range(M):
        for mb in range(M):
            if ma & mb:
                continue
            out[ma | mb] += A[ma] * B[mb]
    return out


@njit(cache=True)
def eh_vertex_fourier(ps, hs, lam):
    n = ps.shape[0]
    M = 1 << n
    full = M - 1

    # Momentum conservation is checked by the caller; all quadrature routings
    # are generated from the already-validated incidence map.
    H = np.zeros((M, D, D), np.float64)
    for i in range(n):
        H[1 << i] = hs[i]

    Ipoly = np.zeros((M, D, D), np.float64)
    Ipoly[0] = np.eye(D)
    gi = Ipoly.copy()
    power = Ipoly.copy()
    log_half = np.zeros(M, np.float64)

    for r in range(1, n + 1):
        power = _matpoly_mul(power, H, M)
        c = 0.5 * ((-1.0) ** (r + 1)) / r
        for m in range(M):
            tr = 0.0
            for a in range(D):
                tr += power[m, a, a]
            log_half[m] += c * tr
        sign = -1.0 if r % 2 else 1.0
        for m in range(M):
            for a in range(D):
                for b in range(D):
                    gi[m, a, b] += sign * power[m, a, b]

    sqrtg = np.zeros(M, np.float64)
    sqrtg[0] = 1.0
    power_s = np.zeros(M, np.float64)
    power_s[0] = 1.0
    fact = 1.0
    for r in range(1, n + 1):
        power_s = _scalpoly_mul(power_s, log_half, M)
        fact *= r
        for m in range(M):
            sqrtg[m] += power_s[m] / fact

    B = np.zeros((M, D, D, D), np.complex128)
    for i in range(n):
        msk = 1 << i
        for s in range(D):
            for mu in range(D):
                for nu in range(D):
                    B[msk, s, mu, nu] = 1j * (
                        ps[i, mu] * hs[i, s, nu]
                        + ps[i, nu] * hs[i, s, mu]
                        - ps[i, s] * hs[i, mu, nu]
                    )

    Gamma = np.zeros((M, D, D, D), np.complex128)
    for ma in range(M):
        for mb in range(M):
            if ma & mb:
                continue
            mm = ma | mb
            for r0 in range(D):
                for mu in range(D):
                    for nu in range(D):
                        z = 0j
                        for sig in range(D):
                            z += gi[ma, r0, sig] * B[mb, sig, mu, nu]
                        Gamma[mm, r0, mu, nu] += 0.5 * z

    dGamma = np.zeros((M, D, D, D, D), np.complex128)
    for msk in range(1, M):
        q = np.zeros(D, np.float64)
        for i in range(n):
            if msk & (1 << i):
                q += ps[i]
        for a in range(D):
            for r0 in range(D):
                for mu in range(D):
                    for nu in range(D):
                        dGamma[msk, a, r0, mu, nu] = 1j * q[a] * Gamma[msk, r0, mu, nu]

    Rmix = np.zeros((M, D, D, D, D), np.complex128)
    for msk in range(1, M):
        for rho in range(D):
            for sig in range(D):
                for mu in range(D):
                    for nu in range(D):
                        Rmix[msk, rho, sig, mu, nu] = (
                            dGamma[msk, mu, rho, nu, sig]
                            - dGamma[msk, nu, rho, mu, sig]
                        )

    for ma in range(M):
        for mb in range(M):
            if ma & mb:
                continue
            mm = ma | mb
            for r0 in range(D):
                for sig in range(D):
                    for mu in range(D):
                        for nu in range(D):
                            z1 = 0j
                            z2 = 0j
                            for ell in range(D):
                                z1 += Gamma[ma, r0, mu, ell] * Gamma[mb, ell, nu, sig]
                                z2 += Gamma[ma, r0, nu, ell] * Gamma[mb, ell, mu, sig]
                            Rmix[mm, r0, sig, mu, nu] += z1 - z2

    Ric = np.zeros((M, D, D), np.complex128)
    for msk in range(M):
        for s in range(D):
            for nu in range(D):
                z = 0j
                for rho in range(D):
                    z += Rmix[msk, rho, s, rho, nu]
                Ric[msk, s, nu] = z

    Rsc = np.zeros(M, np.complex128)
    for ma in range(M):
        for mb in range(M):
            if ma & mb:
                continue
            mm = ma | mb
            z = 0j
            for s in range(D):
                for nu in range(D):
                    z += gi[ma, s, nu] * Ric[mb, s, nu]
            Rsc[mm] += z

    core = -Rsc
    core[0] += 2.0 * lam
    density = np.zeros(M, np.complex128)
    for ma in range(M):
        for mb in range(M):
            if ma & mb:
                continue
            density[ma | mb] += sqrtg[ma] * core[mb]

    return density[full].real * EH_PREF


@njit(cache=True)
def eval_many(ps_batch, hs_batch, lam):
    """Evaluate independent vertices; shapes (B,n,4), (B,n,4,4)."""
    B = ps_batch.shape[0]
    out = np.empty(B, np.float64)
    for i in range(B):
        out[i] = eh_vertex_fourier(ps_batch[i], hs_batch[i], lam)
    return out
