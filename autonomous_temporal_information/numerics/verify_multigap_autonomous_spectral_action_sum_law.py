#!/usr/bin/env python3
"""Independent validator for WP20 multi-gap autonomous spectral-action sum law.

Checks:
1. random scalar bilateral allocations satisfy gamma_k F_k <= g+J+ + g-J-;
2. summed random multi-mode instances obey sum gamma_k F_k <= 4 A_G;
3. exact fixed-total-energy star-shell exchange commutators for m=1..4;
4. exact common nonlinear family normalization/global stationarity;
5. total kernel Hessian and spectral action;
6. one discrete-Fourier measurement simultaneously gives Tr F_k=4 c_k^2
   for every gap;
7. the complete frequency-weighted sum saturates the WP20 action law.

Units hbar*omega0=1.
"""

from __future__ import annotations

import math
import numpy as np

RNG = np.random.default_rng(20260822)


def harmonic(p: float, q: float) -> float:
    return 1.0 / (1.0 / p + 1.0 / q)


def check_scalar_modes() -> None:
    for _ in range(20000):
        nm = int(RNG.integers(1, 8))
        total_cost = 0.0
        total_info = 0.0
        for _k in range(nm):
            p = 10.0 ** RNG.uniform(-2.0, 2.0)
            q = 10.0 ** RNG.uniform(-2.0, 2.0)
            jp = 10.0 ** RNG.uniform(-4.0, 2.0)
            jm = 10.0 ** RNG.uniform(-4.0, 2.0)
            f = (math.sqrt(jp) + math.sqrt(jm)) ** 2 * RNG.random()
            gamma = harmonic(p, q)
            assert gamma * f <= p * jp + q * jm + 2e-12 * max(1.0, p * jp + q * jm)
            total_info += gamma * f
            total_cost += p * jp + q * jm
        assert total_info <= total_cost + 1e-9
    print("Random multi-mode harmonic Fisher allocation PASS")


def fourier_basis(d: int) -> np.ndarray:
    m = (d - 1) // 2
    ns = np.arange(-m, m + 1)
    U = np.zeros((d, d), dtype=complex)
    for j in range(d):
        phi = 2.0 * np.pi * j / d
        U[:, j] = np.exp(1j * ns * phi) / np.sqrt(d)
    return U


def fisher_trace(rho: np.ndarray, A: np.ndarray, U: np.ndarray) -> float:
    val = 0.0
    for j in range(U.shape[1]):
        v = U[:, j]
        p = float(np.vdot(v, rho @ v).real)
        z = np.vdot(v, A @ v)
        if p > 1e-14:
            val += abs(z) ** 2 / p
    return float(val)


def check_star_shell() -> None:
    for m in range(1, 5):
        d = 2 * m + 1
        ns = np.arange(-m, m + 1)
        Hs = np.diag(m + ns.astype(float))
        Hc = np.diag(m - ns.astype(float))
        Htot = Hs + Hc
        assert np.linalg.norm(Htot - 2 * m * np.eye(d)) < 1e-13

        cs = 0.2 + RNG.random(m)
        rho = np.zeros((d, d), dtype=complex)
        rho[m, m] = 1.0
        U = fourier_basis(d)
        assert np.linalg.norm(U.conj().T @ U - np.eye(d)) < 2e-12

        Csig = np.zeros((d, d), dtype=complex)
        G = np.zeros((d, d), dtype=complex)
        weighted_fisher = 0.0

        for k, c in enumerate(cs, start=1):
            A = np.zeros((d, d), dtype=complex)
            A[m + k, m] = c
            A[m, m - k] = c
            assert np.linalg.norm(Hs @ A - A @ Hs - k * A) < 2e-12
            assert np.linalg.norm(Hc @ A - A @ Hc + k * A) < 2e-12
            assert np.linalg.norm(Htot @ A - A @ Htot) < 2e-12

            F = fisher_trace(rho, A, U)
            assert abs(F - 4.0 * c * c) < 3e-11, (m, k, F, 4.0 * c * c)
            weighted_fisher += k * F

            Csig[m - k, m - k] += c * c
            Csig[m + k, m + k] += c * c
            G[m - k, m - k] = 2 * k
            G[m + k, m + k] = 2 * k

        action = 0.25 * float(np.trace(G @ Csig).real)
        expected = sum((k + 1) * cs[k] ** 2 for k in range(m))
        assert abs(action - expected) < 2e-12
        assert abs(0.25 * weighted_fisher - action) < 3e-11

        for _ in range(100):
            x = RNG.normal(scale=0.08, size=m)
            y = RNG.normal(scale=0.08, size=m)
            normcost = 0.5 * np.sum(cs**2 * (x * x + y * y))
            if normcost >= 0.8:
                continue
            psi = np.zeros(d, dtype=complex)
            psi[m] = math.sqrt(1.0 - normcost)
            for k, c in enumerate(cs, start=1):
                psi[m - k] += 0.5 * c * (x[k - 1] + 1j * y[k - 1])
                psi[m + k] += 0.5 * c * (x[k - 1] - 1j * y[k - 1])
            assert abs(np.vdot(psi, psi).real - 1.0) < 3e-13
            rr = np.outer(psi, psi.conj())
            assert np.linalg.norm(Htot @ rr - rr @ Htot) < 3e-12

    print("Fixed-total-energy star-shell simultaneous Fourier saturation PASS")


def main() -> None:
    check_scalar_modes()
    check_star_shell()
    print("WP20 multi-gap autonomous spectral-action validation PASS")


if __name__ == "__main__":
    main()
