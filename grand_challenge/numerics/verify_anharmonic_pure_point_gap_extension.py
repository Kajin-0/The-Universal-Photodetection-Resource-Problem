#!/usr/bin/env python3
"""Numerical consistency checks for WP28 anharmonic pure-point gap extension.

This deliberately uses a globally incommensurate spectrum containing only a few
exact Bohr-gap pairs at a chosen base frequency nu.  It checks:

1. long-window random-time averages converge to complete energy dephasing;
2. cosine/sine tangents converge to the exact +/-nu gap tangent;
3. the arbitrary-gap tangent factorizes through a partial isometry;
4. random POVMs obey the paired-population / energy-tail FI bound;
5. one fixed POVM across multiples of nu gives a positive-semidefinite Toeplitz
   retention sequence.

The script is a consistency/adversarial check; it does not replace the analytic
proof in WP28.
"""

from __future__ import annotations

import math
import numpy as np


NU = 1.0
OMEGA = np.array(
    [0.13, 0.77, 1.13, 1.77, 2.13, math.sqrt(2.0) + 1.0, 3.77, math.pi + 1.0],
    dtype=float,
)
Q = np.array([0.08, 0.10, 0.13, 0.12, 0.18, 0.11, 0.16, 0.12], dtype=float)
Q /= Q.sum()
D = len(Q)
TOL = 2e-11
RNG = np.random.default_rng(20260822)


def average_exponential(delta: float, T: float) -> complex:
    if abs(delta) < 1e-14:
        return 1.0 + 0.0j
    return (np.exp(1j * delta * T) - 1.0) / (1j * delta * T)


def exact_gap_operator(m: int) -> np.ndarray:
    gap = m * NU
    A = np.zeros((D, D), dtype=complex)
    for a in range(D):
        for b in range(D):
            if abs((OMEGA[b] - OMEGA[a]) - gap) < TOL:
                A[b, a] = math.sqrt(Q[a] * Q[b])
    return A


def exact_gap_shift(m: int) -> np.ndarray:
    gap = m * NU
    V = np.zeros((D, D), dtype=complex)
    for a in range(D):
        for b in range(D):
            if (
                Q[a] > 0.0
                and Q[b] > 0.0
                and abs((OMEGA[b] - OMEGA[a]) - gap) < TOL
            ):
                V[b, a] = 1.0
    return V


def long_window_matrices(M: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    T = 2.0 * math.pi * M / NU
    rho = np.zeros((D, D), dtype=complex)
    Dc = np.zeros((D, D), dtype=complex)
    Ds = np.zeros((D, D), dtype=complex)

    for b in range(D):
        for a in range(D):
            amp = math.sqrt(Q[b] * Q[a])
            delta = OMEGA[b] - OMEGA[a]
            rho[b, a] = amp * average_exponential(-delta, T)
            Dc[b, a] = 0.5 * amp * (
                average_exponential(-(delta - NU), T)
                + average_exponential(-(delta + NU), T)
            )
            Ds[b, a] = amp * (
                average_exponential(-(delta - NU), T)
                - average_exponential(-(delta + NU), T)
            ) / (2j)
    return rho, Dc, Ds


def random_povm(number_outcomes: int) -> list[np.ndarray]:
    effects = []
    for _ in range(number_outcomes):
        X = RNG.normal(size=(D, D)) + 1j * RNG.normal(size=(D, D))
        effects.append(X @ X.conj().T)
    total = sum(effects)
    vals, vecs = np.linalg.eigh(total)
    total_inv_sqrt = vecs @ np.diag(1.0 / np.sqrt(vals)) @ vecs.conj().T
    return [total_inv_sqrt @ G @ total_inv_sqrt for G in effects]


def random_projective_povm() -> list[np.ndarray]:
    X = RNG.normal(size=(D, D)) + 1j * RNG.normal(size=(D, D))
    U, R = np.linalg.qr(X)
    phases = np.diag(R)
    U = U * (phases / np.abs(phases))
    return [np.outer(U[:, j], U[:, j].conj()) for j in range(D)]


def fisher_trace(
    povm: list[np.ndarray], rho: np.ndarray, Dc: np.ndarray, Ds: np.ndarray
) -> float:
    out = 0.0
    for M in povm:
        p = float(np.trace(rho @ M).real)
        dc = float(np.trace(Dc @ M).real)
        ds = float(np.trace(Ds @ M).real)
        if p > 1e-14:
            out += (dc * dc + ds * ds) / p
    return out


def check_long_window_convergence() -> None:
    rho0 = np.diag(Q.astype(complex))
    A = exact_gap_operator(1)
    Dc0 = (A + A.conj().T) / 2.0
    Ds0 = (A - A.conj().T) / (2j)

    errors = []
    for M in (5, 20, 100, 500, 2000):
        rho, Dc, Ds = long_window_matrices(M)
        errors.append(
            (
                np.linalg.norm(rho - rho0, ord="nuc"),
                np.linalg.norm(Dc - Dc0, ord="nuc"),
                np.linalg.norm(Ds - Ds0, ord="nuc"),
            )
        )

    # The deliberately incommensurate nonresonant terms must dephase.
    assert max(errors[-1]) < 4e-4, errors[-1]
    assert max(errors[-1]) < max(errors[0]) / 100.0
    print("Long-window anharmonic dephasing/gap-selection PASS")
    print("final trace-norm errors:", errors[-1])


def check_factorization_and_fi_bound() -> None:
    rho0 = np.diag(Q.astype(complex))
    sqrt_rho = np.diag(np.sqrt(Q).astype(complex))
    A = exact_gap_operator(1)
    V = exact_gap_shift(1)
    assert np.linalg.norm(A - sqrt_rho @ V @ sqrt_rho) < 2e-14

    domain = V.conj().T @ V
    ran = V @ V.conj().T
    Dmass = float(np.trace(rho0 @ domain).real)
    Umass = float(np.trace(rho0 @ ran).real)
    tail = float(Q[OMEGA >= NU].sum())
    assert Umass <= tail + 1e-15

    Dc = (A + A.conj().T) / 2.0
    Ds = (A - A.conj().T) / (2j)
    ceiling = min(Dmass, Umass)

    max_seen = 0.0
    for _ in range(600):
        povm = random_povm(10)
        value = fisher_trace(povm, rho0, Dc, Ds)
        max_seen = max(max_seen, value)
        assert value <= ceiling + 2e-11, (value, ceiling)

    for _ in range(600):
        povm = random_projective_povm()
        value = fisher_trace(povm, rho0, Dc, Ds)
        max_seen = max(max_seen, value)
        assert value <= ceiling + 2e-11, (value, ceiling)

    print("Arbitrary-gap factorization / random-POVM FI checks PASS")
    print(f"D={Dmass:.12f}, U={Umass:.12f}, tail={tail:.12f}, max random FI={max_seen:.12f}")


def check_common_measurement_toeplitz() -> None:
    rho0 = np.diag(Q.astype(complex))
    povm = random_projective_povm()
    retention = [1.0]

    for m in range(1, 8):
        A = exact_gap_operator(m)
        Dc = (A + A.conj().T) / 2.0
        Ds = (A - A.conj().T) / (2j)
        Rm = fisher_trace(povm, rho0, Dc, Ds)
        retention.append(Rm)

        tail = float(Q[OMEGA >= m * NU].sum())
        assert Rm <= tail + 2e-12

    for L in range(1, 8):
        toeplitz = np.array(
            [[retention[abs(i - j)] for j in range(L + 1)] for i in range(L + 1)],
            dtype=float,
        )
        mineig = float(np.linalg.eigvalsh(toeplitz).min())
        assert mineig >= -2e-12, (L, mineig, retention)

    print("Anharmonic fixed-measurement Toeplitz checks PASS")
    print("R(m nu), m=0..7:", retention)


def main() -> None:
    # Make sure this is not secretly one global equally spaced ladder.
    spacings = np.diff(np.sort(OMEGA))
    assert np.ptp(spacings) > 0.2
    assert any(abs((OMEGA[b] - OMEGA[a]) - NU) < TOL for a in range(D) for b in range(D))

    check_long_window_convergence()
    check_factorization_and_fi_bound()
    check_common_measurement_toeplitz()
    print("WP28 anharmonic pure-point gap extension consistency PASS")


if __name__ == "__main__":
    main()
