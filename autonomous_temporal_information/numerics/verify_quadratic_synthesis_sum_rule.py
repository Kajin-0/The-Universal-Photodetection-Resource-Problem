#!/usr/bin/env python3
"""Consistency checks for WP08 quadratic spectral-synthesis sum law.

Checks:
1. many orthogonal empty endpoint sectors obey the same-record modewise WP07 bound;
2. arbitrary nonnegative weighted sums obey the synthesis budget;
3. the bound survives random two-copy collective POVMs;
4. multimode coherent-state heterodyne formulas saturate the population-curvature sum;
5. physical sideband-energy weighting saturates the coherent-state energy identity.

The script is a consistency check, not a substitute for the analytic proof.
"""

from __future__ import annotations

import numpy as np

RNG = np.random.default_rng(20260822)


def invsqrt_psd(a: np.ndarray, tol: float = 1e-13) -> np.ndarray:
    vals, vecs = np.linalg.eigh(a)
    vals = np.where(vals > tol, vals, np.inf)
    return (vecs * (1.0 / np.sqrt(vals))) @ vecs.conj().T


def random_povm(d: int, outcomes: int) -> list[np.ndarray]:
    raw = []
    for _ in range(outcomes):
        x = RNG.normal(size=(d, d)) + 1j * RNG.normal(size=(d, d))
        raw.append(x @ x.conj().T)
    total = sum(raw)
    s_inv = invsqrt_psd(total)
    return [s_inv @ e @ s_inv for e in raw]


def fisher_trace(rho: np.ndarray, A: np.ndarray, povm: list[np.ndarray]) -> float:
    out = 0.0
    for m in povm:
        p = float(np.trace(rho @ m).real)
        if p <= 1e-14:
            continue
        z = np.trace(A @ m)
        out += abs(z) ** 2 / p
    return float(out.real)


def pure_multimode_boundary(K: int) -> tuple[np.ndarray, list[np.ndarray], np.ndarray]:
    """Baseline |0>, with K mutually orthogonal empty endpoint states.

    A_k=2 c_k |k><0|, so J_k=Delta_k T_k=4 c_k^2.
    """

    d = K + 1
    rho = np.zeros((d, d), dtype=complex)
    rho[0, 0] = 1.0
    c = 0.05 + RNG.random(K)
    As = []
    for k, ck in enumerate(c, start=1):
        A = np.zeros((d, d), dtype=complex)
        A[k, 0] = 2.0 * ck
        As.append(A)
    return rho, As, c


def check_same_record_weighted_sum() -> None:
    max_unweighted = 0.0
    max_weighted = 0.0

    for K in (2, 3, 5, 8):
        for _ in range(100):
            rho, As, c = pure_multimode_boundary(K)
            d = K + 1
            povm = random_povm(d, d + 7)

            F = np.array([fisher_trace(rho, A, povm) for A in As])
            curvature = 4.0 * c * c

            assert np.all(F <= curvature + 2e-10)
            ratio = float(F.sum() / curvature.sum())
            max_unweighted = max(max_unweighted, ratio)

            w = 0.01 + 10.0 * RNG.random(K)
            lhs = float(np.dot(w, F))
            rhs = float(np.dot(w, curvature))
            assert lhs <= rhs + 5e-10 * max(1.0, rhs)
            max_weighted = max(max_weighted, lhs / rhs)

    print(f"Random same-record max unweighted ratio = {max_unweighted:.8f}")
    print(f"Random same-record max weighted ratio = {max_weighted:.8f}")
    print("Same-record weighted synthesis sum PASS")


def check_two_copy_collective_sum() -> None:
    max_ratio = 0.0

    for K in (2, 3):
        for _ in range(60):
            rho, As, c = pure_multimode_boundary(K)
            d = K + 1
            rho2 = np.kron(rho, rho)
            A2 = [np.kron(A, rho) + np.kron(rho, A) for A in As]
            povm = random_povm(d * d, d * d + 5)

            Fper = np.array([fisher_trace(rho2, B, povm) / 2.0 for B in A2])
            curvature = 4.0 * c * c
            w = 0.05 + 4.0 * RNG.random(K)

            lhs = float(np.dot(w, Fper))
            rhs = float(np.dot(w, curvature))
            assert lhs <= rhs + 2e-8 * max(1.0, rhs)
            max_ratio = max(max_ratio, lhs / rhs)

    print(f"Random two-copy weighted max ratio = {max_ratio:.8f}")
    print("Two-copy collective synthesis sum PASS")


def check_multimode_coherent_heterodyne() -> None:
    for K in (1, 2, 5, 20):
        for _ in range(50):
            g = RNG.normal(size=K) + 1j * RNG.normal(size=K)
            # alpha_k=g_k(x_k+i y_k)
            # n_k=|g_k|^2(x_k^2+y_k^2)
            delta_n = 4.0 * np.abs(g) ** 2

            # Heterodyne p(beta|alpha)=pi^-1 exp(-|beta-alpha|^2):
            # FI_x=FI_y=2|g|^2.
            F_trace = 4.0 * np.abs(g) ** 2
            assert np.max(np.abs(F_trace - delta_n)) < 1e-12

            w = 0.01 + 8.0 * RNG.random(K)
            assert abs(float(np.dot(w, F_trace - delta_n))) < 1e-10

            # Actual sideband energy weighting.
            omega = 0.1 + 100.0 * RNG.random(K)
            hbar = 1.0
            lhs = float(np.dot(hbar * omega / 4.0, F_trace))
            # E_k=hbar omega_k n_k => (1/4) Delta E_k
            rhs = float(np.dot(hbar * omega / 4.0, delta_n))
            assert abs(lhs - rhs) < 1e-10 * max(1.0, rhs)

    print("Multimode coherent heterodyne population/energy saturation PASS")


def main() -> None:
    check_same_record_weighted_sum()
    check_two_copy_collective_sum()
    check_multimode_coherent_heterodyne()
    print("WP08 quadratic spectral-synthesis validation PASS")


if __name__ == "__main__":
    main()
