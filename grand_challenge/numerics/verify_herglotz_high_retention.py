#!/usr/bin/env python3
"""Numerical consistency checks for WP26 Herglotz/high-retention laws.

Validation only; the manuscript results are analytic.
"""

from __future__ import annotations

import math
import numpy as np


def A_of_q(q: float) -> float:
    if q >= 1.0:
        return math.inf
    theta = math.acos(q)
    M = int(math.floor(math.pi / (2.0 * theta)))
    if M <= 0:
        return 0.0
    return sum(math.cos(m * theta) for m in range(1, M + 1))


def A_closed(q: float) -> float:
    if q >= 1.0:
        return math.inf
    theta = math.acos(q)
    M = int(math.floor(math.pi / (2.0 * theta)))
    if M <= 0:
        return 0.0
    return (
        math.sin(M * theta / 2.0)
        * math.cos((M + 1) * theta / 2.0)
        / math.sin(theta / 2.0)
    )


def random_phase_mixture(rng: np.random.Generator, kmax: int = 14) -> np.ndarray:
    """Return R(k)=average_y |phi_y(k)|^2 from random discrete phase laws."""
    npost = 7
    nphase = 19
    py = rng.dirichlet(np.ones(npost))
    theta = np.linspace(-math.pi, math.pi, nphase, endpoint=False)
    R = np.zeros(kmax + 1)
    R[0] = 1.0
    for y in range(npost):
        w = rng.dirichlet(np.ones(nphase))
        for k in range(1, kmax + 1):
            phi = np.sum(w * np.exp(1j * k * theta))
            R[k] += py[y] * abs(phi) ** 2
    return R


def toeplitz_from_R(R: np.ndarray, L: int) -> np.ndarray:
    return np.array([[R[abs(i - j)] for j in range(L + 1)] for i in range(L + 1)])


def equality_source_energy(rates: np.ndarray, weights: np.ndarray, delta: float) -> tuple[np.ndarray, float]:
    """Geometric mixture tails T_k and mean n for r=exp(-beta delta)."""
    r = np.exp(-rates * delta)
    kmax = 25000
    ks = np.arange(kmax + 1)
    T = np.sum(weights[:, None] * r[:, None] ** ks[None, :], axis=0)
    nbar = np.sum(weights * r / (1.0 - r))
    return T, float(nbar)


def main() -> None:
    rng = np.random.default_rng(20260822)

    # 1. Random posterior phase mixtures: Toeplitz PSD and angle propagation.
    for _ in range(300):
        R = random_phase_mixture(rng)
        for L in (2, 4, 7):
            eigmin = np.linalg.eigvalsh(toeplitz_from_R(R, L)).min()
            assert eigmin > -2e-12, eigmin
        for k in range(1, 4):
            q = min(1.0, max(0.0, float(R[k])))
            theta = math.acos(q)
            for m in range(1, len(R) // k):
                if m * theta <= math.pi / 2 + 1e-14:
                    assert R[m * k] + 5e-12 >= math.cos(m * theta), (k, m, q, R[m * k])
                # The elementary bound remains valid for all multiples sampled.
                assert 1.0 - R[m * k] <= m * m * (1.0 - q) + 5e-12

    # 2. Exact equality sources: the block-tail energy inequality.
    for _ in range(200):
        rates = np.exp(rng.uniform(-1.5, 1.5, size=4))
        weights = rng.dirichlet(np.ones(4))
        delta = float(np.exp(rng.uniform(-2.0, -0.2)))
        T, nbar = equality_source_energy(rates, weights, delta)
        for k in (1, 2, 3, 5):
            q = float(T[k])
            assert nbar + 2e-10 >= k * A_of_q(q), (nbar, k, q, A_of_q(q))

    # 3. Closed cosine sum and high-retention asymptotic coefficient.
    for q in np.linspace(0.01, 0.9999, 1000):
        assert abs(A_of_q(float(q)) - A_closed(float(q))) < 3e-12
        assert A_of_q(float(q)) + 1e-14 >= q

    print("WP26 Herglotz/high-retention validation PASS")
    for q in (0.8, 0.9, 0.95, 0.99, 0.999, 0.9999):
        A = A_of_q(q)
        print(f"q={q:.4f} A(q)={A:.12f} scaled={math.sqrt(1-q)*A:.9f}")
    print(f"asymptotic target 1/sqrt(2)={1/math.sqrt(2):.9f}")


if __name__ == "__main__":
    main()
