#!/usr/bin/env python3
"""Adversarial validation for WP10 one-sided mixed survival+synthesis law.

Checks:
1. random energy-diagonal rank-deficient baselines with an exact +1 shift
   tangent containing support-preserving and upper support-to-kernel pieces;
2. arbitrary one-copy POVMs obey Tr F <= J_B+J_K;
3. random two-copy collective POVMs obey the per-copy law;
4. the support-preserving resource obeys J_B <= 4 T_pre/R_B^2;
5. the normalized congruence family realizes the exact tangent and has
   Delta T_syn = J_K in the qutrit extremizer;
6. one three-outcome Fourier measurement simultaneously saturates
   Tr F = J_B+J_K = 4T_pre/R_B^2 + Delta T_syn;
7. the mixed energy/action coefficient is exactly saturated.

The script is a consistency/adversarial check, not a substitute for the
analytic proof in WP10.
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


def psd_invsqrt(rho: np.ndarray, tol: float = 1e-12) -> np.ndarray:
    vals, vecs = np.linalg.eigh(rho)
    inv = np.array([1.0 / math.sqrt(v) if v > tol else 0.0 for v in vals])
    return vecs @ np.diag(inv) @ vecs.conj().T


def numerical_radius(B: np.ndarray, phases: int = 4001) -> float:
    best = 0.0
    for phi in np.linspace(0.0, 2.0 * math.pi, phases, endpoint=False):
        h = (np.exp(-1j * phi) * B + np.exp(1j * phi) * B.conj().T) / 2.0
        best = max(best, float(np.linalg.eigvalsh(h).max()))
    return best


def random_commuting_case(d: int = 5, rank: int = 3):
    # Support is the first `rank` equally-spaced energy levels and therefore
    # commutes with H. The +1 tangent acts only from occupied domain levels:
    # internal links 0->1,...,rank-2->rank-1 plus one synthesis link
    # rank-1->rank.
    q = 0.15 + RNG.random(rank)
    q /= q.sum()
    rho = np.diag(np.r_[q, np.zeros(d - rank)]).astype(complex)
    P = np.diag(np.r_[np.ones(rank), np.zeros(d - rank)]).astype(complex)
    Q = np.eye(d, dtype=complex) - P

    coeff = (0.2 + RNG.random(rank)) * np.exp(2j * math.pi * RNG.random(rank))
    A = np.zeros((d, d), dtype=complex)
    for n in range(rank):
        A[n + 1, n] = coeff[n]

    B = P @ A @ P
    K = Q @ A @ P
    rho_plus = psd_pinv(rho)
    J_B = float(np.trace(B @ rho_plus @ B.conj().T).real)
    J_K = float(np.trace(K @ rho_plus @ K.conj().T).real)

    invsqrt = psd_invsqrt(rho)
    Bwhite = invsqrt @ B @ invsqrt
    w = numerical_radius(Bwhite, 2201)
    R_B = math.inf if w < 1e-14 else 1.0 / w
    T_pre = float(q[1:].sum())

    return rho, P, Q, A, B, K, rho_plus, J_B, J_K, R_B, T_pre


def check_random_one_copy_and_resource() -> None:
    for _ in range(25):
        rho, _, _, A, _, _, _, J_B, J_K, R_B, T_pre = random_commuting_case()
        total = J_B + J_K
        assert J_B <= 4.0 * T_pre / (R_B * R_B) + 2e-7, (J_B, R_B, T_pre)
        for _ in range(80):
            F = fisher_trace(random_povm(rho.shape[0], 12), rho, A)
            assert F <= total + 2e-9, (F, total)
    print("Random one-copy mixed information/resource checks PASS")


def check_random_two_copy_collective() -> None:
    for _ in range(10):
        rho, _, _, A, _, _, _, J_B, J_K, _, _ = random_commuting_case(d=4, rank=2)
        d = rho.shape[0]
        rho2 = np.kron(rho, rho)
        A2 = np.kron(A, rho) + np.kron(rho, A)
        bound = J_B + J_K
        for _ in range(120):
            F2 = fisher_trace(random_povm(d * d, 14), rho2, A2)
            assert F2 / 2.0 <= bound + 3e-9, (F2 / 2.0, bound)
    print("Random two-copy collective mixed checks PASS")


def exact_family(rho0: np.ndarray, A: np.ndarray, x: float, y: float) -> np.ndarray:
    rho_plus = psd_pinv(rho0)
    G = 0.5 * A @ rho_plus
    z = x - 1j * y
    M = np.eye(rho0.shape[0], dtype=complex) + z * G
    out = M @ rho0 @ M.conj().T
    return out / float(np.trace(out).real)


def check_qutrit_exact_extremizer() -> None:
    for p0 in (0.17, 0.41, 0.73):
        p1 = 1.0 - p0
        kappa = 0.81
        rho = np.diag([p0, p1, 0.0]).astype(complex)
        A = np.zeros((3, 3), dtype=complex)
        A[1, 0] = kappa * p0
        A[2, 1] = kappa * p1

        B = np.zeros_like(A)
        B[1, 0] = kappa * p0
        K = np.zeros_like(A)
        K[2, 1] = kappa * p1
        rho_plus = psd_pinv(rho)
        J_B = float(np.trace(B @ rho_plus @ B.conj().T).real)
        J_K = float(np.trace(K @ rho_plus @ K.conj().T).real)
        assert abs(J_B - kappa * kappa * p0) < 2e-13
        assert abs(J_K - kappa * kappa * p1) < 2e-13

        R_B2 = 4.0 * p1 / (kappa * kappa * p0)
        T_pre = p1
        assert abs(4.0 * T_pre / R_B2 - J_B) < 2e-13

        # Fourier projective measurement.
        povm = []
        for m in range(3):
            phi = 2.0 * math.pi * m / 3.0
            v = np.array(
                [1.0, np.exp(-1j * phi), np.exp(-2j * phi)], dtype=complex
            ) / math.sqrt(3.0)
            povm.append(np.outer(v, v.conj()))
        F = fisher_trace(povm, rho, A)
        assert abs(F - kappa * kappa) < 3e-13
        assert abs(F - (J_B + J_K)) < 3e-13

        # Finite-difference check of the exact physical congruence family.
        h = 2e-5
        rp = exact_family(rho, A, h, 0.0)
        rm = exact_family(rho, A, -h, 0.0)
        ip = exact_family(rho, A, 0.0, h)
        im = exact_family(rho, A, 0.0, -h)
        d2x = (float(rp[2, 2].real) - 2.0 * 0.0 + float(rm[2, 2].real)) / (h * h)
        d2y = (float(ip[2, 2].real) - 2.0 * 0.0 + float(im[2, 2].real)) / (h * h)
        Delta_T_syn = d2x + d2y
        assert abs(Delta_T_syn - J_K) < 2e-8, (Delta_T_syn, J_K)

        # Set hbar*nu=1. The baseline mean excess energy is p1.
        Ebar = p1
        E_syn2 = 0.25 * J_K
        lhs = Ebar / R_B2 + E_syn2
        rhs = 0.25 * F
        assert abs(lhs - rhs) < 3e-13

    print("Qutrit simultaneous information/resource saturation PASS")
    print("Exact normalized congruence-family synthesis curvature PASS")
    print("Mixed energy/action coefficient sharpness PASS")


def main() -> None:
    check_random_one_copy_and_resource()
    check_random_two_copy_collective()
    check_qutrit_exact_extremizer()
    print("WP10 one-sided mixed survival+synthesis validation PASS")


if __name__ == "__main__":
    main()
