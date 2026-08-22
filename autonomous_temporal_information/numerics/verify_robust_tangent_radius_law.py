#!/usr/bin/env python3
"""Adversarial numerical checks for WP02 robust tangent-radius law.

Checks:
1. qubit fixed-energy/high-frequency counterexample;
2. exact numerical-radius formula for the linear physical tangent radius;
3. random POVMs obey the one-copy robust Fisher bound;
4. random collective POVMs on two copies obey the per-copy bound;
5. the qubit family asymptotically saturates the energy corollary.

The script is a consistency check, not a substitute for the analytic proof.
"""

from __future__ import annotations

import math
import numpy as np

RNG = np.random.default_rng(20260822)


def random_povm(d: int, outcomes: int) -> list[np.ndarray]:
    effects = []
    for _ in range(outcomes):
        x = RNG.normal(size=(d, d)) + 1j * RNG.normal(size=(d, d))
        effects.append(x @ x.conj().T)
    total = sum(effects)
    vals, vecs = np.linalg.eigh(total)
    invsqrt = vecs @ np.diag(1.0 / np.sqrt(vals)) @ vecs.conj().T
    return [invsqrt @ g @ invsqrt for g in effects]


def fisher_trace(povm: list[np.ndarray], rho: np.ndarray, A: np.ndarray) -> float:
    # D_c=(A+A^dag)/2, D_s=(A-A^dag)/(2i). For outcome y,
    # derivatives are Re z_y and Im z_y, so trace-FI contribution is |z_y|^2/p_y.
    out = 0.0
    for M in povm:
        p = float(np.trace(rho @ M).real)
        z = np.trace(A @ M)
        if p > 1e-14:
            out += abs(z) ** 2 / p
    return float(out)


def numerical_radius(B: np.ndarray, phase_steps: int = 4001) -> float:
    # w(B)=max_phi lambda_max[ Re(e^{-i phi} B) ].
    best = 0.0
    for phi in np.linspace(0.0, 2.0 * math.pi, phase_steps, endpoint=False):
        h = (np.exp(-1j * phi) * B + np.exp(1j * phi) * B.conj().T) / 2.0
        best = max(best, float(np.linalg.eigvalsh(h).max()))
    return best


def check_qubit_no_go_and_sharpness() -> None:
    c = 0.5
    E = 1.0
    last_ratio = None
    for nu in (10.0, 100.0, 1000.0, 10000.0):
        p = E / nu
        rho = np.diag([1.0 - p, p]).astype(complex)
        # A=2c|1><0| gives D_c=c sigma_x, D_s=c sigma_y.
        A = np.array([[0.0, 0.0], [2.0 * c, 0.0]], dtype=complex)
        Rlin = math.sqrt(p * (1.0 - p)) / c

        # Equatorial covariant POVM approximated by a fine discrete phase POVM.
        m = 4000
        povm = []
        for j in range(m):
            th = 2.0 * math.pi * (j + 0.5) / m
            M = np.array(
                [
                    [1.0, np.exp(-1j * th)],
                    [np.exp(1j * th), 1.0],
                ],
                dtype=complex,
            ) / m
            povm.append(M)

        F = fisher_trace(povm, rho, A)
        assert abs(F - 4.0 * c * c) < 2e-7, (nu, F)

        tail = p
        robust = (Rlin * Rlin / 4.0) * F
        assert robust <= tail + 1e-12
        assert abs(robust / tail - (1.0 - p)) < 2e-8

        # Mean energy remains exactly E while nu grows and F remains constant.
        mean_energy = p * nu
        assert abs(mean_energy - E) < 1e-12
        energy_rhs = nu * robust
        assert energy_rhs <= E + 1e-12
        last_ratio = energy_rhs / E

    assert last_ratio is not None and last_ratio > 0.9998
    print("Fixed-energy/high-frequency local-Fisher no-go PASS")
    print("Qubit robust energy-law asymptotic sharpness PASS")


def check_random_one_copy() -> None:
    d = 7
    for _ in range(30):
        q = RNG.random(d)
        q /= q.sum()
        rho = np.diag(q.astype(complex))
        sq = np.diag(np.sqrt(q))

        # One positive nearest-neighbor Bohr mode.
        B = np.zeros((d, d), dtype=complex)
        weights = (0.1 + RNG.random(d - 1)) * np.exp(2j * math.pi * RNG.random(d - 1))
        for n, w in enumerate(weights):
            B[n + 1, n] = w

        wnum = numerical_radius(B, 1201)
        Rlin = 1.0 / wnum
        A = sq @ B @ sq

        # Positivity at random points inside the disk.
        Dc = (A + A.conj().T) / 2.0
        Ds = (A - A.conj().T) / (2j)
        for _ in range(100):
            radius = Rlin * math.sqrt(RNG.random())
            phi = 2.0 * math.pi * RNG.random()
            state = rho + radius * math.cos(phi) * Dc + radius * math.sin(phi) * Ds
            assert float(np.linalg.eigvalsh(state).min()) >= -5e-10

        U = float(q[1:].sum())
        D = float(q[:-1].sum())
        bound = 4.0 * min(U, D) / (Rlin * Rlin)

        for _ in range(80):
            F = fisher_trace(random_povm(d, 12), rho, A)
            assert F <= bound + 2e-10, (F, bound)

    print("Random one-copy robust Fisher bound PASS")


def check_random_two_copy_collective() -> None:
    d = 3
    q = np.array([0.62, 0.27, 0.11], dtype=float)
    rho = np.diag(q.astype(complex))
    sq = np.diag(np.sqrt(q))

    B = np.zeros((d, d), dtype=complex)
    B[1, 0] = 0.9
    B[2, 1] = 0.55 * np.exp(0.37j)
    Rlin = 1.0 / numerical_radius(B, 4001)
    A = sq @ B @ sq

    rho2 = np.kron(rho, rho)
    A2 = np.kron(A, rho) + np.kron(rho, A)

    U = float(q[1:].sum())
    D = float(q[:-1].sum())
    per_copy_bound = 4.0 * min(U, D) / (Rlin * Rlin)

    for _ in range(300):
        povm = random_povm(d * d, 14)
        F2 = fisher_trace(povm, rho2, A2)
        assert F2 / 2.0 <= per_copy_bound + 5e-10, (F2 / 2.0, per_copy_bound)

    print("Two-copy collective-POVM robust Fisher bound PASS")


def main() -> None:
    check_qubit_no_go_and_sharpness()
    check_random_one_copy()
    check_random_two_copy_collective()
    print("WP02 robust tangent-radius validation PASS")


if __name__ == "__main__":
    main()
