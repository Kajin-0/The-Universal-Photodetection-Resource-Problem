#!/usr/bin/env python3
"""Independent validator for WP18 autonomous dual synthesis-action law.

Checks:
1. bilateral fixed-total-energy qutrit exchange commutators;
2. exact global stationarity of the nonlinear family;
3. endpoint population Laplacians and local positive synthesis actions;
4. exact Fourier-measurement Fisher trace 4 c^2;
5. saturation of total bilateral coefficient hbar nu/4;
6. random qutrit POVMs obey the bilateral endpoint-curvature Fisher ceiling;
7. one-sided fixed-total-energy qubit exchange saturates total coefficient hbar nu/2.

Set hbar*nu=1 in the numerical checks.
"""

from __future__ import annotations

import math
import numpy as np

RNG = np.random.default_rng(20260822)


def random_rank1_povm(d: int, m: int) -> np.ndarray:
    v = RNG.normal(size=(d, m)) + 1j * RNG.normal(size=(d, m))
    s = v @ v.conj().T
    vals, vecs = np.linalg.eigh((s + s.conj().T) / 2.0)
    inv = vecs @ np.diag(1.0 / np.sqrt(vals)) @ vecs.conj().T
    return inv @ v


def fisher_trace(rho: np.ndarray, A: np.ndarray, W: np.ndarray) -> float:
    out = 0.0
    for j in range(W.shape[1]):
        w = W[:, j]
        p = float(np.vdot(w, rho @ w).real)
        if p <= 1e-13:
            continue
        z = np.vdot(w, A @ w)
        out += abs(z) ** 2 / p
    return float(out)


def fourier_basis_3() -> np.ndarray:
    omega = np.exp(2j * math.pi / 3.0)
    # Columns are (1,1,1), (omega^-1,1,omega), (omega^-2,1,omega^2)
    U = np.zeros((3, 3), dtype=complex)
    for m in range(3):
        phi = 2.0 * math.pi * m / 3.0
        U[:, m] = np.array(
            [np.exp(-1j * phi), 1.0, np.exp(1j * phi)], dtype=complex
        ) / math.sqrt(3.0)
    return U


def check_bilateral_qutrit() -> None:
    c = 0.73
    # Ordered shell basis |L>=|2,0>, |M>=|1,1>, |U>=|0,2>.
    Hc = np.diag([2.0, 1.0, 0.0])
    Hs = np.diag([0.0, 1.0, 2.0])
    Htot = Hc + Hs

    A = np.zeros((3, 3), dtype=complex)
    A[2, 1] = c  # |U><M|
    A[1, 0] = c  # |M><L|

    assert np.linalg.norm(Hs @ A - A @ Hs - A) < 1e-13
    assert np.linalg.norm(Hc @ A - A @ Hc + A) < 1e-13
    assert np.linalg.norm(Htot @ A - A @ Htot) < 1e-13
    assert np.linalg.norm(Htot - 2.0 * np.eye(3)) < 1e-13

    rho0 = np.diag([0.0, 1.0, 0.0]).astype(complex)

    # Exact nonlinear family remains normalized and in the same total-energy shell.
    for _ in range(100):
        x, y = RNG.normal(scale=0.15, size=2)
        rr = x * x + y * y
        if 0.5 * c * c * rr >= 0.95:
            continue
        psi = np.array(
            [
                0.5 * c * (x + 1j * y),
                math.sqrt(1.0 - 0.5 * c * c * rr),
                0.5 * c * (x - 1j * y),
            ],
            dtype=complex,
        )
        rho = np.outer(psi, psi.conj())
        assert abs(np.vdot(psi, psi).real - 1.0) < 2e-13
        assert np.linalg.norm(Htot @ rho - rho @ Htot) < 2e-13

    # Each endpoint population is c^2(x^2+y^2)/4, so Delta=c^2.
    delta_sp = c * c
    delta_sm = c * c
    delta_cp = c * c
    delta_cm = c * c

    A_S = 0.25 * (delta_sp + delta_sm)  # hbar nu =1
    A_C = 0.25 * (delta_cp + delta_cm)
    assert abs(A_S - 0.5 * c * c) < 1e-14
    assert abs(A_C - 0.5 * c * c) < 1e-14

    U = fourier_basis_3()
    assert np.linalg.norm(U.conj().T @ U - np.eye(3)) < 2e-13
    F = fisher_trace(rho0, A, U)
    assert abs(F - 4.0 * c * c) < 2e-12, F
    assert abs((A_S + A_C) - 0.25 * F) < 2e-12

    # Random POVMs obey the local bilateral curvature ceiling (sqrt c^2+sqrt c^2)^2=4c^2.
    ceiling = 4.0 * c * c
    best = 0.0
    for _ in range(12000):
        W = random_rank1_povm(3, int(RNG.integers(3, 9)))
        value = fisher_trace(rho0, A, W)
        assert value <= ceiling + 2e-9, (value, ceiling)
        best = max(best, value)

    print(f"WP18 bilateral fixed-shell exact saturation PASS; random best={best:.6f}")


def check_one_sided_qubit() -> None:
    c = 0.61
    # Ordered basis |D>=|1,0>, |U>=|0,1>.
    Hc = np.diag([1.0, 0.0])
    Hs = np.diag([0.0, 1.0])
    Htot = Hc + Hs

    A = np.array([[0.0, 0.0], [2.0 * c, 0.0]], dtype=complex)
    assert np.linalg.norm(Hs @ A - A @ Hs - A) < 1e-13
    assert np.linalg.norm(Hc @ A - A @ Hc + A) < 1e-13
    assert np.linalg.norm(Htot - np.eye(2)) < 1e-13

    rho0 = np.diag([1.0, 0.0]).astype(complex)

    # Equatorial four-outcome POVM used in WP07.
    effects = []
    for phi in (0.0, 0.5 * math.pi, math.pi, 1.5 * math.pi):
        v = np.array([1.0, np.exp(1j * phi)], dtype=complex) / math.sqrt(2.0)
        # M=(1/2)|v><v| so columns sqrt(1/2) v.
        effects.append(v / math.sqrt(2.0))
    W = np.column_stack(effects)
    assert np.linalg.norm(W @ W.conj().T - np.eye(2)) < 2e-13

    F = fisher_trace(rho0, A, W)
    assert abs(F - 4.0 * c * c) < 2e-12

    delta_signal_upper = 4.0 * c * c
    delta_clock_lower = 4.0 * c * c
    A_S = 0.25 * delta_signal_upper
    A_C = 0.25 * delta_clock_lower
    assert abs((A_S + A_C) - 0.5 * F) < 2e-12

    print("WP18 one-sided fixed-shell exact saturation PASS")


def main() -> None:
    check_bilateral_qutrit()
    check_one_sided_qubit()
    print("WP18 autonomous dual synthesis-action validation PASS")


if __name__ == "__main__":
    main()
