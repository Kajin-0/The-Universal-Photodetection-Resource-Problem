#!/usr/bin/env python3
"""Random finite-dimensional checks of WP25 approximate Bohr-gap robustness."""

from __future__ import annotations

import numpy as np


def run_trial(seed: int) -> None:
    rng = np.random.default_rng(seed)
    d = 10
    # Semibounded diagonal Hamiltonian with irregular spacings.
    E = np.sort(rng.uniform(0.0, 12.0, size=d))
    H = np.diag(E)

    p = rng.random(d)
    p /= p.sum()
    rho = np.diag(p)
    rho_plus = np.diag(1.0 / p)
    sr = np.diag(np.sqrt(p))

    B = rng.normal(size=(d, d)) + 1j * rng.normal(size=(d, d))
    # Enforce Tr A = Tr(rho B) = 0 without changing off-diagonal structure.
    mean = np.sum(p * np.diag(B))
    B = B - mean * np.eye(d)
    normB = np.linalg.norm(B, 2)
    if normB == 0:
        return
    B /= normB
    normB = 1.0

    A = sr @ B @ sr
    np.testing.assert_allclose(np.trace(A), 0.0, atol=2e-12)

    # R=1/||B|| is guaranteed to be a valid affine radius, though not
    # necessarily the maximal R_lin. The theorem holds for any valid R<=R_lin.
    R = 1.0 / normB

    nu = float(rng.uniform(1.0, 8.0))
    residual = H @ A - A @ H - nu * A  # hbar=1 units
    eta2 = float(np.trace(residual @ rho_plus @ residual.conj().T).real)
    J = float(np.trace(A @ rho_plus @ A.conj().T).real)

    # Direct matrix-element expression for J.
    J_matrix = 0.0
    for m in range(d):
        for n in range(d):
            J_matrix += p[m] * abs(B[m, n]) ** 2
    np.testing.assert_allclose(J, J_matrix, rtol=2e-12, atol=2e-12)

    for delta in np.linspace(0.1 * nu, 0.9 * nu, 9):
        near = 0.0
        off = 0.0
        eta_matrix = 0.0
        for m in range(d):
            for n in range(d):
                w = p[m] * abs(B[m, n]) ** 2
                mismatch = E[m] - E[n] - nu
                eta_matrix += w * mismatch * mismatch
                if abs(mismatch) < delta:
                    near += w
                else:
                    off += w
        np.testing.assert_allclose(near + off, J, rtol=2e-12, atol=2e-12)
        np.testing.assert_allclose(eta_matrix, eta2, rtol=2e-12, atol=2e-12)

        tail = float(np.sum(p[E >= E.min() + nu - delta]))
        near_bound = 4.0 * tail / (R * R)
        off_bound = eta2 / (delta * delta)
        if near > near_bound + 1e-11:
            raise AssertionError((seed, delta, near, near_bound))
        if off > off_bound + 1e-11:
            raise AssertionError((seed, delta, off, off_bound))
        if J > near_bound + off_bound + 1e-11:
            raise AssertionError((seed, delta, J, near_bound + off_bound))


def exact_gap_check() -> None:
    # Exact shift on an equally spaced ladder, hbar=1.
    d = 7
    E = np.arange(d, dtype=float)
    H = np.diag(E)
    p = np.arange(1, d + 1, dtype=float)
    p /= p.sum()
    rho = np.diag(p)
    rp = np.diag(1.0 / p)
    sr = np.diag(np.sqrt(p))

    nu = 2.0
    B = np.zeros((d, d), dtype=complex)
    for n in range(d - 2):
        B[n + 2, n] = 0.4 + 0.05j * (n + 1)
    A = sr @ B @ sr
    residual = H @ A - A @ H - nu * A
    np.testing.assert_allclose(residual, 0.0, atol=1e-13)

    J = float(np.trace(A @ rp @ A.conj().T).real)
    R = 1.0 / np.linalg.norm(B, 2)
    tail = float(np.sum(p[E >= nu]))
    if (R * R / 4.0) * J > tail + 1e-12:
        raise AssertionError(((R * R / 4.0) * J, tail))


def main() -> None:
    for seed in range(100):
        run_trial(seed)
    exact_gap_check()
    print("WP25 approximate-gap robustness validator: PASS")


if __name__ == "__main__":
    main()
