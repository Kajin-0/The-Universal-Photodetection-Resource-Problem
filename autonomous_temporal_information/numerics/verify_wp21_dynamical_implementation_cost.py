#!/usr/bin/env python3
"""Numerical checks for WP21 dynamical implementation coupling-cost law.

Checks:
1. exact target-kernel curvature identity for random correlated mixed
   target--ancilla baselines supported in P⊗E;
2. positive endpoint-weighted action <= hbar*nu times generator variance;
3. exact equality for the bilateral and one-sided fixed-shell extremizers.

The numerics validate algebra; they are not part of the proof.
"""

from __future__ import annotations

import numpy as np

RNG = np.random.default_rng(210826)


def random_density(n: int) -> np.ndarray:
    x = RNG.normal(size=(n, n)) + 1j * RNG.normal(size=(n, n))
    a = x @ x.conj().T
    return a / np.trace(a)


def random_hermitian(n: int) -> np.ndarray:
    x = RNG.normal(size=(n, n)) + 1j * RNG.normal(size=(n, n))
    return (x + x.conj().T) / 2


def ptrace_env(a: np.ndarray, dt: int, de: int) -> np.ndarray:
    a4 = a.reshape(dt, de, dt, de)
    return np.einsum("aibi->ab", a4)


def embed_supported_global(rho_pe: np.ndarray, dt: int, de: int, rp: int) -> np.ndarray:
    out = np.zeros((dt * de, dt * de), dtype=complex)
    idx = [a * de + e for a in range(rp) for e in range(de)]
    out[np.ix_(idx, idx)] = rho_pe
    return out


def variance(rho: np.ndarray, k: np.ndarray) -> float:
    mean = np.trace(rho @ k)
    return float(np.real(np.trace(rho @ k @ k) - mean * mean))


def random_identity_checks(trials: int = 100) -> None:
    dt, de, rp = 5, 3, 2
    p = np.diag([1.0] * rp + [0.0] * (dt - rp))
    q = np.eye(dt) - p
    qg = np.kron(q, np.eye(de))

    # Price only one subspace inside the empty target kernel.
    r = np.zeros((dt, dt))
    r[rp, rp] = 1.0
    rg = np.kron(r, np.eye(de))

    worst_identity = 0.0
    worst_margin = np.inf

    for _ in range(trials):
        omega_pe = random_density(rp * de)
        omega = embed_supported_global(omega_pe, dt, de, rp)
        k = random_hermitian(dt * de)

        comm = k @ omega - omega @ k
        second = -(k @ comm - comm @ k)
        lhs = q @ ptrace_env(second, dt, de) @ q
        rhs = 2 * ptrace_env(qg @ k @ omega @ k @ qg, dt, de)
        err = np.linalg.norm(lhs - rhs)
        worst_identity = max(worst_identity, err)

        leak = float(np.real(np.trace(rg @ k @ omega @ k)))
        var = variance(omega, k)
        worst_margin = min(worst_margin, var - leak)

    assert worst_identity < 1e-10, worst_identity
    assert worst_margin > -1e-10, worst_margin
    print(f"random correlated identity PASS; worst error={worst_identity:.3e}")
    print(f"random variance bound PASS; minimum margin={worst_margin:.3e}")


def fixed_shell_checks(c: float = 0.731, hbar_nu: float = 2.4) -> None:
    # Bilateral basis L,M,U, with baseline M.
    eL = np.array([1.0, 0.0, 0.0], complex)
    eM = np.array([0.0, 1.0, 0.0], complex)
    eU = np.array([0.0, 0.0, 1.0], complex)
    rho = np.outer(eM, eM.conj())

    # -i Kx|M> = c/2 (|L>+|U>)
    vx = 1j * c / 2 * (eL + eU)
    kx = np.outer(vx, eM.conj()) + np.outer(eM, vx.conj())

    # -i Ky|M> = i c/2 (|L>-|U>)
    vy = -c / 2 * (eL - eU)
    ky = np.outer(vy, eM.conj()) + np.outer(eM, vy.conj())

    vimpl = variance(rho, kx) + variance(rho, ky)
    action = hbar_nu * c * c
    assert abs(vimpl - c * c) < 1e-12
    assert abs(action - hbar_nu * vimpl) < 1e-12

    # One-sided basis D,U.
    eD = np.array([1.0, 0.0], complex)
    eU2 = np.array([0.0, 1.0], complex)
    rho2 = np.outer(eD, eD.conj())

    # derivatives c|U> and -i c|U>
    vx2 = 1j * c * eU2
    vy2 = c * eU2
    kx2 = np.outer(vx2, eD.conj()) + np.outer(eD, vx2.conj())
    ky2 = np.outer(vy2, eD.conj()) + np.outer(eD, vy2.conj())

    vimpl2 = variance(rho2, kx2) + variance(rho2, ky2)
    action2 = 2 * hbar_nu * c * c
    assert abs(vimpl2 - 2 * c * c) < 1e-12
    assert abs(action2 - hbar_nu * vimpl2) < 1e-12

    print("bilateral fixed-shell equality PASS")
    print("one-sided fixed-shell equality PASS")


def main() -> None:
    random_identity_checks()
    fixed_shell_checks()
    print("WP21 dynamical implementation validator: PASS")


if __name__ == "__main__":
    main()
