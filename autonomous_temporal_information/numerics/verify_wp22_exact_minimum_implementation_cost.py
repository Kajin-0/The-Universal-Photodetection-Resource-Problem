#!/usr/bin/env python3
"""Numerical validator for WP22 exact minimum energy-conserving implementation cost.

Checks random rank-deficient baselines and pure-boundary Hermitian tangents:
1. K_hor = i(QDP rho^+ - rho^+ PDQ) is Hermitian;
2. -i[K_hor,rho] = D;
3. Var_rho(K_hor) = H_SLD(D,D)/4.

Also checks a block-degenerate Hamiltonian example in which rho and D commute with
H and therefore the constructed horizontal generator commutes with H exactly.
"""

from __future__ import annotations

import numpy as np

RNG = np.random.default_rng(220826)


def qfi_scalar(rho_vals: np.ndarray, d: np.ndarray) -> float:
    out = 0.0
    n = len(rho_vals)
    for a in range(n):
        for b in range(n):
            den = rho_vals[a] + rho_vals[b]
            if den > 1e-14:
                out += 2.0 * abs(d[a, b]) ** 2 / den
    return float(np.real(out))


def variance(rho: np.ndarray, k: np.ndarray) -> float:
    m = np.trace(rho @ k)
    return float(np.real(np.trace(rho @ k @ k) - m * m))


def random_checks(trials: int = 200) -> None:
    worst_dyn = 0.0
    worst_var = 0.0
    worst_herm = 0.0

    for _ in range(trials):
        n = int(RNG.integers(4, 9))
        r = int(RNG.integers(1, n))
        vals = RNG.random(r)
        vals /= vals.sum()
        lam = np.concatenate([vals, np.zeros(n - r)])
        rho = np.diag(lam)
        rho_plus = np.diag(np.concatenate([1.0 / vals, np.zeros(n - r)]))
        p = np.diag(np.concatenate([np.ones(r), np.zeros(n - r)]))
        q = np.eye(n) - p

        z = RNG.normal(size=(n - r, r)) + 1j * RNG.normal(size=(n - r, r))
        d = np.zeros((n, n), dtype=complex)
        d[r:, :r] = z
        d[:r, r:] = z.conj().T

        c = q @ d @ p @ rho_plus
        k = 1j * (c - c.conj().T)

        worst_herm = max(worst_herm, np.linalg.norm(k - k.conj().T))
        reconstructed = -1j * (k @ rho - rho @ k)
        worst_dyn = max(worst_dyn, np.linalg.norm(reconstructed - d))

        h = qfi_scalar(lam, d)
        v = variance(rho, k)
        worst_var = max(worst_var, abs(v - h / 4.0))

    assert worst_herm < 1e-10, worst_herm
    assert worst_dyn < 1e-10, worst_dyn
    assert worst_var < 1e-9, worst_var

    print(f"horizontal Hermiticity PASS; worst={worst_herm:.3e}")
    print(f"horizontal tangent reconstruction PASS; worst={worst_dyn:.3e}")
    print(f"Var=H_SLD/4 PASS; worst={worst_var:.3e}")


def energy_conservation_check() -> None:
    # Two degenerate energy sectors, each containing one support and one kernel state.
    h = np.diag([0.0, 1.0, 0.0, 1.0])
    lam = np.array([0.4, 0.6, 0.0, 0.0])
    rho = np.diag(lam)
    rho_plus = np.diag([1 / 0.4, 1 / 0.6, 0.0, 0.0])
    p = np.diag([1.0, 1.0, 0.0, 0.0])
    q = np.eye(4) - p

    # Couple only equal-energy pairs 0<->2 and 1<->3.
    d = np.zeros((4, 4), dtype=complex)
    d[2, 0] = 0.37 + 0.11j
    d[0, 2] = d[2, 0].conjugate()
    d[3, 1] = -0.22 + 0.19j
    d[1, 3] = d[3, 1].conjugate()

    assert np.linalg.norm(h @ rho - rho @ h) < 1e-14
    assert np.linalg.norm(h @ d - d @ h) < 1e-14

    c = q @ d @ p @ rho_plus
    k = 1j * (c - c.conj().T)

    assert np.linalg.norm(h @ k - k @ h) < 1e-12
    assert np.linalg.norm(-1j * (k @ rho - rho @ k) - d) < 1e-12
    print("exact energy-conserving horizontal lift PASS")


def main() -> None:
    random_checks()
    energy_conservation_check()
    print("WP22 exact minimum implementation validator: PASS")


if __name__ == "__main__":
    main()
