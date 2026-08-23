#!/usr/bin/env python3
"""Hostile validator for WP20 multi-gap autonomous spectral-action sum law.

Checks:
1. random scalar bilateral allocations satisfy gamma_k F_k <= g+J+ + g-J-;
2. exact fixed-total-energy exchange commutators for m=1..5;
3. exact common nonlinear family normalization and tangent convention;
4. the total kernel Hessian is recovered by finite differences from the actual
   common multiparameter family, including cancellation of endpoint coherences;
5. canonical clean spectral cost and total action;
6. one discrete-Fourier measurement produces the complete 2m x 2m classical
   Fisher matrix with zero cross-mode/cos-sin blocks and diagonal entries
   2 c_k^2, hence Tr F_k=4 c_k^2 for every gap simultaneously;
7. the full frequency-weighted sum saturates the action law.

Units hbar*omega0=1.
"""

from __future__ import annotations

import math
import numpy as np

RNG = np.random.default_rng(20260823)


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


def common_state(m: int, cs: np.ndarray, pars: np.ndarray) -> np.ndarray:
    """pars=(x1,y1,...,xm,ym)."""
    d = 2 * m + 1
    psi = np.zeros(d, dtype=complex)
    normcost = 0.0
    for k, c in enumerate(cs, start=1):
        x = pars[2 * (k - 1)]
        y = pars[2 * (k - 1) + 1]
        normcost += 0.5 * c * c * (x * x + y * y)
        psi[m - k] = 0.5 * c * (x + 1j * y)
        psi[m + k] = 0.5 * c * (x - 1j * y)
    assert normcost < 1.0
    psi[m] = math.sqrt(1.0 - normcost)
    return psi


def rho_from_state(v: np.ndarray) -> np.ndarray:
    return np.outer(v, v.conj())


def fisher_matrix_from_tangents(rho: np.ndarray, tangents: list[np.ndarray], U: np.ndarray) -> np.ndarray:
    n = len(tangents)
    F = np.zeros((n, n), dtype=float)
    for j in range(U.shape[1]):
        v = U[:, j]
        p = float(np.vdot(v, rho @ v).real)
        if p <= 1e-14:
            continue
        ds = np.array([float(np.vdot(v, D @ v).real) for D in tangents])
        F += np.outer(ds, ds) / p
    return F


def check_star_shell() -> None:
    for m in range(1, 6):
        d = 2 * m + 1
        ns = np.arange(-m, m + 1)
        Hs = np.diag(m + ns.astype(float))
        Hc = np.diag(m - ns.astype(float))
        Htot = Hs + Hc
        assert np.linalg.norm(Htot - 2 * m * np.eye(d)) < 1e-13

        cs = 0.2 + RNG.random(m)
        rho0 = np.zeros((d, d), dtype=complex)
        rho0[m, m] = 1.0
        U = fourier_basis(d)
        assert np.linalg.norm(U.conj().T @ U - np.eye(d)) < 2e-12

        As: list[np.ndarray] = []
        tangents: list[np.ndarray] = []
        C_expected = np.zeros((d, d), dtype=complex)
        G = np.zeros((d, d), dtype=complex)

        for k, c in enumerate(cs, start=1):
            A = np.zeros((d, d), dtype=complex)
            A[m + k, m] = c
            A[m, m - k] = c
            As.append(A)
            assert np.linalg.norm(Hs @ A - A @ Hs - k * A) < 2e-12
            assert np.linalg.norm(Hc @ A - A @ Hc + k * A) < 2e-12
            assert np.linalg.norm(Htot @ A - A @ Htot) < 2e-12

            Dc = (A + A.conj().T) / 2.0
            Ds = (A - A.conj().T) / (2j)
            tangents.extend([Dc, Ds])

            C_expected[m - k, m - k] = c * c
            C_expected[m + k, m + k] = c * c
            G[m - k, m - k] = 2.0 * k
            G[m + k, m + k] = 2.0 * k

        # Tangent convention from the actual common family.
        h = 2e-6
        zero = np.zeros(2 * m)
        for a, D in enumerate(tangents):
            pp = zero.copy(); pp[a] = h
            pm = zero.copy(); pm[a] = -h
            num = (rho_from_state(common_state(m, cs, pp)) - rho_from_state(common_state(m, cs, pm))) / (2.0 * h)
            assert np.linalg.norm(num - D) < 2e-7

        # Recover C_Sigma=Q sum_a partial_a^2 rho Q from finite differences.
        Q = np.eye(d, dtype=complex) - rho0
        C_num = np.zeros((d, d), dtype=complex)
        rho_base = rho0
        h2 = 2e-4
        for a in range(2 * m):
            pp = zero.copy(); pp[a] = h2
            pm = zero.copy(); pm[a] = -h2
            rp = rho_from_state(common_state(m, cs, pp))
            rm = rho_from_state(common_state(m, cs, pm))
            sec = (rp - 2.0 * rho_base + rm) / (h2 * h2)
            C_num += Q @ sec @ Q
        assert np.linalg.norm(C_num - C_expected) < 3e-7, np.linalg.norm(C_num - C_expected)

        # Full common-record Fisher matrix.
        F = fisher_matrix_from_tangents(rho0, tangents, U)
        F_expected = np.zeros((2 * m, 2 * m), dtype=float)
        for k, c in enumerate(cs):
            F_expected[2 * k, 2 * k] = 2.0 * c * c
            F_expected[2 * k + 1, 2 * k + 1] = 2.0 * c * c
        assert np.linalg.norm(F - F_expected) < 2e-10, np.linalg.norm(F - F_expected)

        action = 0.25 * float(np.trace(G @ C_expected).real)
        expected_action = sum((k + 1) * cs[k] ** 2 for k in range(m))
        assert abs(action - expected_action) < 2e-12

        weighted_fisher = 0.0
        for k, c in enumerate(cs, start=1):
            block_trace = F[2 * (k - 1), 2 * (k - 1)] + F[2 * (k - 1) + 1, 2 * (k - 1) + 1]
            assert abs(block_trace - 4.0 * c * c) < 2e-11
            weighted_fisher += k * block_trace
        assert abs(0.25 * weighted_fisher - action) < 3e-11

        # Random exact physical states remain normalized and globally stationary.
        for _ in range(100):
            pars = RNG.normal(scale=0.06, size=2 * m)
            normcost = sum(0.5 * cs[k] ** 2 * (pars[2*k]**2 + pars[2*k+1]**2) for k in range(m))
            if normcost >= 0.8:
                continue
            v = common_state(m, cs, pars)
            rr = rho_from_state(v)
            assert abs(np.vdot(v, v).real - 1.0) < 3e-13
            assert np.linalg.norm(Htot @ rr - rr @ Htot) < 3e-12

    print("Fixed-shell common-Hessian and full Fourier-Fisher saturation PASS")


def main() -> None:
    check_scalar_modes()
    check_star_shell()
    print("Audited WP20 multi-gap spectral-action validation PASS")


if __name__ == "__main__":
    main()
