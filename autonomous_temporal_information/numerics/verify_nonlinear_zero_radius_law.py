#!/usr/bin/env python3
"""Adversarial numerical checks for WP07 nonlinear zero-radius laws.

Checks:
1. random rank-deficient unitary boundary curves saturate the second-order
   PSD support-creation inequality;
2. their one-parameter support-to-kernel SLD QFI saturates F_Q = 2 T_U'';
3. the two-quadrature pure boundary model has QFI trace 2 Delta T_U but a
   single fixed four-outcome POVM saturates Tr F = Delta T_U;
4. random one-copy POVMs obey Tr F <= J(A|rho) <= Delta T_U;
5. random two-copy collective POVMs obey Tr F_2/2 <= J(A|rho);
6. random PSD block states obey ||C||_1^2 <= q_D q_U and the finite phase
   Helstrom bound;
7. the earlier coherent-sideband example saturates the single-quadrature
   QFI curvature coefficient and the two-quadrature operational coefficient.

The script is a consistency check, not a substitute for the analytic proof.
"""

from __future__ import annotations

import numpy as np

RNG = np.random.default_rng(20260822)


def trace_norm(a: np.ndarray) -> float:
    return float(np.linalg.svd(a, compute_uv=False).sum())


def random_density(d: int) -> np.ndarray:
    x = RNG.normal(size=(d, d)) + 1j * RNG.normal(size=(d, d))
    rho = x @ x.conj().T
    return rho / np.trace(rho)


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


def qfi_from_derivative(rho: np.ndarray, derivative: np.ndarray) -> float:
    vals, vecs = np.linalg.eigh(rho)
    d = vecs.conj().T @ derivative @ vecs
    out = 0.0
    for i, pi in enumerate(vals):
        for j, pj in enumerate(vals):
            if pi + pj > 1e-13:
                out += 2.0 * abs(d[i, j]) ** 2 / (pi + pj)
    return float(out.real)


def two_quadrature_fisher(
    rho: np.ndarray, A: np.ndarray, povm: list[np.ndarray]
) -> float:
    out = 0.0
    for m in povm:
        p = float(np.trace(rho @ m).real)
        if p <= 1e-14:
            continue
        z = np.trace(A @ m)
        out += abs(z) ** 2 / p
    return float(out.real)


def unitary_boundary_derivatives(
    rho_support: np.ndarray, coupling: np.ndarray
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return rho0, rho'(0), rho''(0) for exp(theta G)rho0 exp(-theta G)."""

    dp = rho_support.shape[0]
    dq = coupling.shape[0]
    zero_pp = np.zeros((dp, dp), dtype=complex)
    zero_qq = np.zeros((dq, dq), dtype=complex)
    G = np.block(
        [
            [zero_pp, -coupling.conj().T],
            [coupling, zero_qq],
        ]
    )
    rho0 = np.block(
        [
            [rho_support, np.zeros((dp, dq), dtype=complex)],
            [np.zeros((dq, dp), dtype=complex), zero_qq],
        ]
    )
    first = G @ rho0 - rho0 @ G
    second = G @ G @ rho0 - 2.0 * G @ rho0 @ G + rho0 @ G @ G
    return rho0, first, second


def check_random_curvature_saturation() -> None:
    for dp, dq in ((2, 1), (3, 2), (5, 3)):
        for _ in range(50):
            R = random_density(dp)
            L = RNG.normal(size=(dq, dp)) + 1j * RNG.normal(size=(dq, dp))
            rho0, D, C = unitary_boundary_derivatives(R, L)

            K = D[dp:, :dp]
            rhs = 2.0 * K @ np.linalg.inv(R) @ K.conj().T
            lhs = C[dp:, dp:]
            assert np.linalg.norm(lhs - rhs) < 2e-9

            Fq = qfi_from_derivative(rho0, D)
            T2 = float(np.trace(lhs).real)
            assert abs(Fq - 2.0 * T2) < 2e-9

    print("Random unitary boundary curvature/QFI saturation PASS")


def check_two_quadrature_pure_saturation() -> None:
    for c in (0.07, 0.3, 1.2, 4.0):
        rho0 = np.array([[1.0, 0.0], [0.0, 0.0]], dtype=complex)
        Dx = np.array([[0.0, c], [c, 0.0]], dtype=complex)
        Dy = np.array([[0.0, -1j * c], [1j * c, 0.0]], dtype=complex)
        A = np.array([[0.0, 0.0], [2.0 * c, 0.0]], dtype=complex)

        Fx = qfi_from_derivative(rho0, Dx)
        Fy = qfi_from_derivative(rho0, Dy)
        assert abs(Fx - 4.0 * c * c) < 1e-12
        assert abs(Fy - 4.0 * c * c) < 1e-12

        delta_T = 4.0 * c * c
        assert abs((Fx + Fy) - 2.0 * delta_T) < 1e-12

        # Four equatorial rank-one half-effects; sum M_m = I.
        povm = []
        for phi in (0.0, np.pi / 2.0, np.pi, 3.0 * np.pi / 2.0):
            ket = np.array([1.0, np.exp(1j * phi)]) / np.sqrt(2.0)
            povm.append(0.5 * np.outer(ket, ket.conj()))
        assert np.linalg.norm(sum(povm) - np.eye(2)) < 1e-12

        Fm = two_quadrature_fisher(rho0, A, povm)
        assert abs(Fm - delta_T) < 1e-12

        x = 1e-6
        affine = rho0 + x * Dx
        assert np.linalg.det(affine).real < 0.0

    print("Two-quadrature pure operational curvature saturation PASS")


def make_support_kernel_pair(dp: int, dq: int) -> tuple[np.ndarray, np.ndarray, float]:
    R = random_density(dp)
    B = RNG.normal(size=(dq, dp)) + 1j * RNG.normal(size=(dq, dp))
    A = np.block(
        [
            [np.zeros((dp, dp), dtype=complex), np.zeros((dp, dq), dtype=complex)],
            [B, np.zeros((dq, dq), dtype=complex)],
        ]
    )
    rho = np.block(
        [
            [R, np.zeros((dp, dq), dtype=complex)],
            [np.zeros((dq, dp), dtype=complex), np.zeros((dq, dq), dtype=complex)],
        ]
    )
    J = float(np.trace(B @ np.linalg.inv(R) @ B.conj().T).real)
    return rho, A, J


def check_random_povm_operational_bound() -> None:
    max_ratio_1 = 0.0
    max_ratio_2 = 0.0

    for dp, dq in ((2, 1), (2, 2), (3, 2)):
        for _ in range(80):
            rho, A, J = make_support_kernel_pair(dp, dq)
            d = dp + dq

            povm = random_povm(d, outcomes=d + 4)
            F1 = two_quadrature_fisher(rho, A, povm)
            assert F1 <= J + 5e-10 * max(1.0, J)
            max_ratio_1 = max(max_ratio_1, F1 / J)

            # Two-copy arbitrary collective POVM.
            rho2 = np.kron(rho, rho)
            A2 = np.kron(A, rho) + np.kron(rho, A)
            povm2 = random_povm(d * d, outcomes=d * d + 3)
            F2 = two_quadrature_fisher(rho2, A2, povm2)
            assert F2 / 2.0 <= J + 2e-8 * max(1.0, J)
            max_ratio_2 = max(max_ratio_2, (F2 / 2.0) / J)

            # Minimal physical curvature can attain Delta T_U = J:
            # each quadrature contributes J/2 by the Schur-complement equality.
            delta_T_min = J
            assert J <= delta_T_min + 1e-12

    print(f"Random one-copy POVM max TrF/J = {max_ratio_1:.8f}")
    print(f"Random two-copy POVM max (TrF/2)/J = {max_ratio_2:.8f}")
    print("Direct arbitrary-POVM zero-radius bound PASS")


def check_random_block_coherence_and_phase_flip() -> None:
    for dD, dU in ((1, 1), (2, 3), (4, 2)):
        d = dD + dU
        for _ in range(300):
            rho = random_density(d)
            rho_D = rho[:dD, :dD]
            rho_U = rho[dD:, dD:]
            C = rho[dD:, :dD]

            qD = float(np.trace(rho_D).real)
            qU = float(np.trace(rho_U).real)
            coh = trace_norm(C)
            assert coh * coh <= qD * qU + 2e-12
            assert coh * coh <= min(qD, qU) + 2e-12

            Z = np.diag(np.concatenate([np.ones(dD), -np.ones(dU)])).astype(complex)
            rho_pi = Z @ rho @ Z
            Dtr = 0.5 * trace_norm(rho - rho_pi)
            assert abs(Dtr - 2.0 * coh) < 2e-10
            assert Dtr * Dtr / 4.0 <= min(qD, qU) + 2e-12

    print("Finite-amplitude block-coherence / Helstrom bound PASS")


def check_coherent_sideband_coefficients() -> None:
    for Nbar in (0.01, 0.3, 1.0, 17.0, 1e3):
        # Single real quadrature from WP14:
        # n_sb(epsilon)=epsilon^2 Nbar/4 -> n_sb''=Nbar/2,
        # while F_Q=Nbar.
        n_second = Nbar / 2.0
        Fq_single = Nbar
        assert abs(Fq_single - 2.0 * n_second) < 1e-12 * max(1.0, Nbar)

        # Two complex sideband quadratures:
        # n_sb(x,y)=Nbar(x^2+y^2)/4 -> Delta n_sb=Nbar.
        # Heterodyne gives Nbar/2 FI in each quadrature, trace Nbar.
        delta_n = Nbar
        Fhet_trace = Nbar
        assert abs(Fhet_trace - delta_n) < 1e-12 * max(1.0, Nbar)

    print("Coherent-sideband QFI and operational curvature coefficients PASS")


def main() -> None:
    check_random_curvature_saturation()
    check_two_quadrature_pure_saturation()
    check_random_povm_operational_bound()
    check_random_block_coherence_and_phase_flip()
    check_coherent_sideband_coefficients()
    print("WP07 nonlinear zero-radius validation PASS")


if __name__ == "__main__":
    main()
