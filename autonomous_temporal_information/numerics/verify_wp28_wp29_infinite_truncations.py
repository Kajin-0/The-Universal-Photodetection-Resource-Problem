#!/usr/bin/env python3
"""Large-truncation checks for WP28/WP29 infinite-dimensional limits.

The script uses sequences with known infinite-series limits. It verifies:
1. finite-radius exact-gap survival on increasingly long geometric ladders;
2. one-sided and bilateral rank-boundary weighted tangent norms with rapidly
   decaying support eigenvalues and Hilbert--Schmidt right-relative tangents;
3. monotone convergence of finite-rank curvature forms to the claimed trace-
   class limits.
"""

from __future__ import annotations

import numpy as np


def finite_radius_ladder(N: int, r: float = 0.83, c: float = 0.6, k: int = 3):
    # Truncated geometric stationary state on energies n=0,...,N-1.
    p = (1.0 - r) * r ** np.arange(N, dtype=float)
    p /= p.sum()

    B = np.zeros((N, N), dtype=complex)
    for n in range(N - k):
        B[n + k, n] = c

    J = float(np.trace(np.diag(p) @ B @ B.conj().T).real)
    tail = float(np.sum(p[k:]))
    np.testing.assert_allclose(J, c * c * tail, rtol=2e-14, atol=2e-14)

    # R=1/c is a conservative valid radius because w(B)<=||B||=c.
    R = 1.0 / c
    assert (R * R / 4.0) * J <= tail + 1e-14
    return J, tail


def boundary_truncation(N: int, r: float = 0.79):
    # Support eigenvalues become exponentially small, so rho^+ becomes badly
    # conditioned with N. The theorem remains controlled by the HS relative
    # amplitudes, not by ||rho^+||.
    p = (1.0 - r) * r ** np.arange(N, dtype=float)
    p /= p.sum()

    a = 0.70 ** np.arange(N, dtype=float)
    b = 0.55 ** np.arange(N, dtype=float)

    # X,Y map the N-dimensional support into orthogonal N-dimensional kernel
    # copies. A_{q_n,p_n}=sqrt(p_n)*relative_amplitude_n.
    X = np.diag(np.sqrt(p) * a)
    Y = np.diag(np.sqrt(p) * b)
    rp = np.diag(1.0 / p)

    Zx = X @ rp @ X.conj().T
    Zy = Y @ rp @ Y.conj().T
    Jx = float(np.trace(Zx).real)
    Jy = float(np.trace(Zy).real)

    expected_x = float(np.sum(a * a))
    expected_y = float(np.sum(b * b))
    np.testing.assert_allclose(Jx, expected_x, rtol=2e-14, atol=2e-14)
    np.testing.assert_allclose(Jy, expected_y, rtol=2e-14, atol=2e-14)

    # Minimal bilateral kernel Laplacian.
    Cdelta = Zx + Zy
    np.testing.assert_allclose(np.trace(Cdelta).real, Jx + Jy, rtol=2e-14, atol=2e-14)

    # SLD trace for the two quadratures.
    Htrace = 2.0 * (Jx + Jy)
    np.testing.assert_allclose(Htrace, 2.0 * np.trace(Cdelta).real, rtol=2e-14, atol=2e-14)

    # Generic common-record Minkowski ceiling.
    F_ceiling = (np.sqrt(Jx) + np.sqrt(Jy)) ** 2
    assert F_ceiling <= 2.0 * (Jx + Jy) + 1e-14

    return Jx, Jy


def main() -> None:
    Ns = [4, 8, 16, 32, 64, 128, 256]

    fr = [finite_radius_ladder(N) for N in Ns if N > 3]
    # Infinite geometric tail and J limits.
    r = 0.83
    c = 0.6
    k = 3
    np.testing.assert_allclose(fr[-1][1], r**k, rtol=1e-12, atol=1e-12)
    np.testing.assert_allclose(fr[-1][0], c * c * r**k, rtol=1e-12, atol=1e-12)

    bd = [boundary_truncation(N) for N in Ns]
    jx_inf = 1.0 / (1.0 - 0.70**2)
    jy_inf = 1.0 / (1.0 - 0.55**2)
    np.testing.assert_allclose(bd[-1][0], jx_inf, rtol=1e-12, atol=1e-12)
    np.testing.assert_allclose(bd[-1][1], jy_inf, rtol=1e-12, atol=1e-12)

    # Monotone finite-rank form convergence.
    for seq_index in (0, 1):
        vals = [x[seq_index] for x in bd]
        if any(vals[i + 1] + 1e-14 < vals[i] for i in range(len(vals) - 1)):
            raise AssertionError("boundary quadratic forms are not monotone")

    print("WP28/WP29 infinite-dimensional truncation validator: PASS")


if __name__ == "__main__":
    main()
