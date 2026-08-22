#!/usr/bin/env python3
"""Consistency checks for WP03/WP04 autonomous relational temporal laws.

Checks:
1. random globally-stationary exchange tangents obey both clock and signal tail bounds;
2. symmetric two-qubit exchange model has weakly commuting SLDs and saturates
   both dual tails at the asymptotic SLD/Holevo limit;
3. finite exchange-shift numerical radius equals cos(pi/(L+2));
4. sine-chain history states exactly saturate the hard-cap first-harmonic law;
5. higher-harmonic numerical radius equals the longest residue-chain formula.

This is an adversarial consistency test, not a replacement for analytic proofs.
"""

from __future__ import annotations

import math
import numpy as np

RNG = np.random.default_rng(20260822)


def random_povm(d: int, outcomes: int) -> list[np.ndarray]:
    mats = []
    for _ in range(outcomes):
        x = RNG.normal(size=(d, d)) + 1j * RNG.normal(size=(d, d))
        mats.append(x @ x.conj().T)
    total = sum(mats)
    vals, vecs = np.linalg.eigh(total)
    invsqrt = vecs @ np.diag(1.0 / np.sqrt(vals)) @ vecs.conj().T
    return [invsqrt @ m @ invsqrt for m in mats]


def fisher_trace(povm: list[np.ndarray], rho: np.ndarray, A: np.ndarray) -> float:
    out = 0.0
    for M in povm:
        p = float(np.trace(rho @ M).real)
        z = np.trace(A @ M)
        if p > 1e-14:
            out += abs(z) ** 2 / p
    return float(out)


def numerical_radius(B: np.ndarray, phases: int = 6001) -> float:
    best = 0.0
    for phi in np.linspace(0.0, 2.0 * math.pi, phases, endpoint=False):
        h = (np.exp(-1j * phi) * B + np.exp(1j * phi) * B.conj().T) / 2.0
        best = max(best, float(np.linalg.eigvalsh(h).max()))
    return best


def exchange_shift(L: int, k: int = 1) -> np.ndarray:
    d = L + 1
    V = np.zeros((d, d), dtype=complex)
    for n in range(d - k):
        V[n + k, n] = 1.0
    return V


def check_random_dual_tail() -> None:
    # Fixed total shell L=5. Basis n=signal excitation, clock excitation=L-n.
    L = 5
    d = L + 1
    q = 0.1 + RNG.random(d)
    q /= q.sum()
    rho = np.diag(q.astype(complex))
    sq = np.diag(np.sqrt(q))

    # Generic weighted +1 exchange tangent, not the random-time special form.
    B = np.zeros((d, d), dtype=complex)
    weights = (0.15 + RNG.random(L)) * np.exp(2j * math.pi * RNG.random(L))
    for n, w in enumerate(weights):
        B[n + 1, n] = w
    A = sq @ B @ sq
    Rlin = 1.0 / numerical_radius(B, 3001)

    T_signal = float(q[1:].sum())  # n_S >= 1
    T_clock = float(q[:-1].sum())  # n_C=L-n >= 1
    ceiling = min(T_signal, T_clock)
    Fbound = 4.0 * ceiling / (Rlin * Rlin)

    for _ in range(500):
        F = fisher_trace(random_povm(d, 10), rho, A)
        assert F <= Fbound + 2e-10, (F, Fbound)

    print("Random globally-stationary dual-tail POVM checks PASS")


def check_symmetric_two_qubit_asymptotic_sharpness() -> None:
    p = 0.21
    c = 0.37
    # Active one-excitation subspace baseline is p I_2; ground flag has 1-2p.
    rho = np.diag([1.0 - 2.0 * p, p, p]).astype(complex)
    X = np.zeros((3, 3), dtype=complex)
    Y = np.zeros((3, 3), dtype=complex)
    X[1, 2] = X[2, 1] = 1.0
    Y[1, 2] = -1j
    Y[2, 1] = 1j
    Dc = c * X
    Ds = c * Y

    Lc = (c / p) * X
    Ls = (c / p) * Y
    weak = np.trace(rho @ (Lc @ Ls - Ls @ Lc))
    assert abs(weak) < 1e-13

    # SLD QFI trace: Tr rho Lc^2 + Tr rho Ls^2 = 4 c^2/p.
    Fq = float(np.trace(rho @ (Lc @ Lc + Ls @ Ls)).real)
    assert abs(Fq - 4.0 * c * c / p) < 1e-12

    Rlin2 = p * p / (c * c)
    K_asymptotic = (Rlin2 / 4.0) * Fq
    assert abs(K_asymptotic - p) < 1e-12

    print("Symmetric exchange weak-commutativity / sharp factor-2 energy check PASS")


def check_finite_shift_and_sine_extremizer() -> None:
    for L in (1, 2, 3, 5, 10, 30):
        V = exchange_shift(L, 1)
        w_num = numerical_radius(V, 4001)
        w_exact = math.cos(math.pi / (L + 2))
        assert abs(w_num - w_exact) < 3e-7, (L, w_num, w_exact)

        n = np.arange(L + 1, dtype=float)
        a = math.sqrt(2.0 / (L + 2)) * np.sin((n + 1.0) * math.pi / (L + 2))
        assert abs(float(np.sum(a * a)) - 1.0) < 2e-13
        overlap = float(np.sum(a[:-1] * a[1:]))
        assert abs(overlap - w_exact) < 3e-13
        retention = overlap * overlap
        assert abs(retention - math.cos(math.pi / (L + 2)) ** 2) < 5e-13
        # Symmetry gives equal local means L/2; total is exactly L in every basis state.
        mean_signal = float(np.sum(n * a * a))
        assert abs(mean_signal - L / 2.0) < 2e-12

    print("Finite-shift numerical radius / sine extremizer PASS")


def check_higher_harmonics() -> None:
    for L in (4, 5, 8, 13, 21):
        for k in range(1, L + 1):
            V = exchange_shift(L, k)
            w_num = numerical_radius(V, 3001)
            longest_edges = L // k
            w_exact = math.cos(math.pi / (longest_edges + 2))
            assert abs(w_num - w_exact) < 4e-7, (L, k, w_num, w_exact)

    print("Higher-harmonic hard-cap cosine law PASS")


def main() -> None:
    check_random_dual_tail()
    check_symmetric_two_qubit_asymptotic_sharpness()
    check_finite_shift_and_sine_extremizer()
    check_higher_harmonics()
    print("WP03/WP04 autonomous relational validation PASS")


if __name__ == "__main__":
    main()
