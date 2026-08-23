#!/usr/bin/env python3
"""Adversarial validation for WP09 bilateral-synthesis Minkowski law.

Checks:
1. random rank-deficient baselines and arbitrary one-copy POVMs obey
   sqrt(Tr F) <= sqrt(J_X)+sqrt(J_Y);
2. random two-copy collective POVMs obey the same per-copy law and the
   weighted tangent norms scale exactly as N J_X and N J_Y;
3. the exact qutrit positive-gap Fourier measurement saturates the bound;
4. the naive additive endpoint-curvature law fails by exactly factor two;
5. the equal-gap hbar*nu/8 synthesis-action coefficient is sharp;
6. the unequal-cost harmonic-combination inequality is numerically checked.

The script is a consistency/adversarial check, not a substitute for the
analytic proof in WP09.
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


def psd_pinv(rho: np.ndarray, tol: float = 1e-12) -> np.ndarray:
    vals, vecs = np.linalg.eigh(rho)
    inv = np.array([1.0 / v if v > tol else 0.0 for v in vals])
    return vecs @ np.diag(inv) @ vecs.conj().T


def random_rank_deficient_case(d: int = 5, rank: int = 3):
    q = 0.2 + RNG.random(rank)
    q /= q.sum()
    rho = np.diag(np.r_[q, np.zeros(d - rank)]).astype(complex)
    P = np.diag(np.r_[np.ones(rank), np.zeros(d - rank)]).astype(complex)
    Q = np.eye(d, dtype=complex) - P

    # General complex tangent with Q A Q = 0 and Tr A = 0.
    App = RNG.normal(size=(rank, rank)) + 1j * RNG.normal(size=(rank, rank))
    App -= np.trace(App) * np.eye(rank) / rank
    Aqp = RNG.normal(size=(d - rank, rank)) + 1j * RNG.normal(size=(d - rank, rank))
    Apq = RNG.normal(size=(rank, d - rank)) + 1j * RNG.normal(size=(rank, d - rank))

    A = np.zeros((d, d), dtype=complex)
    A[:rank, :rank] = App
    A[rank:, :rank] = Aqp
    A[:rank, rank:] = Apq

    X = A @ P
    Y = Q @ A.conj().T @ P
    rho_plus = psd_pinv(rho)
    JX = float(np.trace(X @ rho_plus @ X.conj().T).real)
    JY = float(np.trace(Y @ rho_plus @ Y.conj().T).real)
    return rho, P, Q, A, X, Y, rho_plus, JX, JY


def check_random_one_copy() -> None:
    for _ in range(40):
        rho, _, _, A, _, _, _, JX, JY = random_rank_deficient_case()
        bound = (math.sqrt(JX) + math.sqrt(JY)) ** 2
        for _ in range(80):
            F = fisher_trace(random_povm(rho.shape[0], 11), rho, A)
            assert F <= bound + 2e-9, (F, bound)
    print("Random one-copy mixed-support Minkowski checks PASS")


def check_random_two_copy_collective() -> None:
    for _ in range(8):
        rho, P, _, A, X, Y, rho_plus, JX, JY = random_rank_deficient_case(d=3, rank=2)
        d = rho.shape[0]
        rho2 = np.kron(rho, rho)
        A2 = np.kron(A, rho) + np.kron(rho, A)
        P2 = np.kron(P, P)
        Q2 = np.eye(d * d, dtype=complex) - P2
        X2 = A2 @ P2
        Y2 = Q2 @ A2.conj().T @ P2
        rho2_plus = np.kron(rho_plus, rho_plus)

        JX2 = float(np.trace(X2 @ rho2_plus @ X2.conj().T).real)
        JY2 = float(np.trace(Y2 @ rho2_plus @ Y2.conj().T).real)
        assert abs(JX2 - 2.0 * JX) < 2e-10, (JX2, JX)
        assert abs(JY2 - 2.0 * JY) < 2e-10, (JY2, JY)

        per_copy_bound = (math.sqrt(JX) + math.sqrt(JY)) ** 2
        for _ in range(100):
            F2 = fisher_trace(random_povm(d * d, 13), rho2, A2)
            assert F2 / 2.0 <= per_copy_bound + 3e-9, (F2 / 2.0, per_copy_bound)
    print("Random two-copy collective Minkowski checks PASS")


def check_qutrit_exact_extremizer() -> None:
    c = 0.73
    rho = np.diag([0.0, 1.0, 0.0]).astype(complex)
    A = np.zeros((3, 3), dtype=complex)
    A[2, 1] = c
    A[1, 0] = c

    povm = []
    for m in range(3):
        phi = 2.0 * math.pi * m / 3.0
        v = np.array([np.exp(-1j * phi), 1.0, np.exp(1j * phi)], dtype=complex) / math.sqrt(3.0)
        povm.append(np.outer(v, v.conj()))

    F = fisher_trace(povm, rho, A)
    JX = c * c
    JY = c * c
    Delta_T_plus = c * c
    Delta_T_minus = c * c
    minkowski = (math.sqrt(JX) + math.sqrt(JY)) ** 2

    assert abs(F - 4.0 * c * c) < 2e-12
    assert abs(F - minkowski) < 2e-12

    additive = Delta_T_plus + Delta_T_minus
    assert abs(F / additive - 2.0) < 2e-12

    # Set hbar*nu=1. E_bi,syn^(2)=(1/4)(Delta_T+ + Delta_T-).
    E_syn = 0.25 * additive
    rhs = 0.125 * F
    assert abs(E_syn - rhs) < 2e-12

    print("Qutrit Fourier exact Minkowski saturation PASS")
    print("Naive additive endpoint law factor-two failure PASS")
    print("Equal-gap hbar*nu/8 coefficient sharpness PASS")


def check_unequal_cost_harmonic_bound() -> None:
    for _ in range(10000):
        a = 10.0 ** RNG.uniform(-5.0, 3.0)
        b = 10.0 ** RNG.uniform(-5.0, 3.0)
        ep = 10.0 ** RNG.uniform(-4.0, 4.0)
        em = 10.0 ** RNG.uniform(-4.0, 4.0)
        lhs = (math.sqrt(a) + math.sqrt(b)) ** 2
        weighted = ep * a + em * b
        dual = 1.0 / ep + 1.0 / em
        assert lhs <= weighted * dual + 2e-10 * max(1.0, lhs)

        eparallel = 1.0 / dual
        E_syn = 0.25 * weighted
        # If Fisher reached the Minkowski ceiling, E_syn >= eparallel*F/4.
        assert E_syn + 2e-12 >= 0.25 * eparallel * lhs

    print("Unequal-cost harmonic-combination bound PASS")


def main() -> None:
    check_random_one_copy()
    check_random_two_copy_collective()
    check_qutrit_exact_extremizer()
    check_unequal_cost_harmonic_bound()
    print("WP09 bilateral-synthesis Minkowski validation PASS")


if __name__ == "__main__":
    main()
