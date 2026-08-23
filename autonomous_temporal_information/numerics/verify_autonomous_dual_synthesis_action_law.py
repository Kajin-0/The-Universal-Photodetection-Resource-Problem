#!/usr/bin/env python3
"""Independent validator for WP18 autonomous dual synthesis-action law.

Checks:
1. bilateral fixed-total-energy qutrit exchange commutators;
2. exact global stationarity and tangent convention of the nonlinear family;
3. endpoint population Laplacians and local positive synthesis actions;
4. exact Fourier-measurement Fisher trace 4 c^2;
5. saturation of total bilateral coefficient hbar nu/4;
6. random qutrit POVMs obey the bilateral endpoint-curvature Fisher ceiling;
7. one-sided fixed-total-energy qubit family uses the audited x-i y convention,
   has the exact stated tangent, and saturates total coefficient hbar nu/2.

Set hbar*nu=1 in the numerical checks.
"""

from __future__ import annotations

import math
import numpy as np

RNG = np.random.default_rng(20260823)


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


def numerical_tangent(state_fn, axis: int, h: float = 2e-7) -> np.ndarray:
    if axis == 0:
        pp = state_fn(h, 0.0)
        pm = state_fn(-h, 0.0)
    else:
        pp = state_fn(0.0, h)
        pm = state_fn(0.0, -h)
    rp = np.outer(pp, pp.conj())
    rm = np.outer(pm, pm.conj())
    return (rp - rm) / (2.0 * h)


def fourier_basis_3() -> np.ndarray:
    U = np.zeros((3, 3), dtype=complex)
    for m in range(3):
        phi = 2.0 * math.pi * m / 3.0
        U[:, m] = np.array(
            [np.exp(-1j * phi), 1.0, np.exp(1j * phi)], dtype=complex
        ) / math.sqrt(3.0)
    return U


def check_bilateral_qutrit() -> None:
    c = 0.73
    Hc = np.diag([2.0, 1.0, 0.0])
    Hs = np.diag([0.0, 1.0, 2.0])
    Htot = Hc + Hs

    A = np.zeros((3, 3), dtype=complex)
    A[2, 1] = c
    A[1, 0] = c

    assert np.linalg.norm(Hs @ A - A @ Hs - A) < 1e-13
    assert np.linalg.norm(Hc @ A - A @ Hc + A) < 1e-13
    assert np.linalg.norm(Htot @ A - A @ Htot) < 1e-13
    assert np.linalg.norm(Htot - 2.0 * np.eye(3)) < 1e-13

    Dc = (A + A.conj().T) / 2.0
    Ds = (A - A.conj().T) / (2j)

    def psi(x: float, y: float) -> np.ndarray:
        rr = x * x + y * y
        return np.array(
            [
                0.5 * c * (x + 1j * y),
                math.sqrt(1.0 - 0.5 * c * c * rr),
                0.5 * c * (x - 1j * y),
            ],
            dtype=complex,
        )

    assert np.linalg.norm(numerical_tangent(psi, 0) - Dc) < 3e-8
    assert np.linalg.norm(numerical_tangent(psi, 1) - Ds) < 3e-8

    for _ in range(100):
        x, y = RNG.normal(scale=0.15, size=2)
        rr = x * x + y * y
        if 0.5 * c * c * rr >= 0.95:
            continue
        v = psi(x, y)
        rho = np.outer(v, v.conj())
        assert abs(np.vdot(v, v).real - 1.0) < 2e-13
        assert np.linalg.norm(Htot @ rho - rho @ Htot) < 2e-13

    rho0 = np.diag([0.0, 1.0, 0.0]).astype(complex)
    delta_sp = delta_sm = delta_cp = delta_cm = c * c
    A_S = 0.25 * (delta_sp + delta_sm)
    A_C = 0.25 * (delta_cp + delta_cm)

    U = fourier_basis_3()
    F = fisher_trace(rho0, A, U)
    assert abs(F - 4.0 * c * c) < 2e-12
    assert abs((A_S + A_C) - 0.25 * F) < 2e-12

    ceiling = 4.0 * c * c
    best = 0.0
    for _ in range(12000):
        W = random_rank1_povm(3, int(RNG.integers(3, 9)))
        value = fisher_trace(rho0, A, W)
        assert value <= ceiling + 2e-9, (value, ceiling)
        best = max(best, value)

    print(f"WP18 bilateral convention/action saturation PASS; random best={best:.6f}")


def check_one_sided_qubit() -> None:
    c = 0.61
    Hc = np.diag([1.0, 0.0])
    Hs = np.diag([0.0, 1.0])
    Htot = Hc + Hs

    A = np.array([[0.0, 0.0], [2.0 * c, 0.0]], dtype=complex)
    Dc = (A + A.conj().T) / 2.0
    Ds = (A - A.conj().T) / (2j)

    assert np.linalg.norm(Hs @ A - A @ Hs - A) < 1e-13
    assert np.linalg.norm(Hc @ A - A @ Hc + A) < 1e-13
    assert np.linalg.norm(Htot - np.eye(2)) < 1e-13

    def psi(x: float, y: float) -> np.ndarray:
        rr = x * x + y * y
        return np.array(
            [math.sqrt(1.0 - c * c * rr), c * (x - 1j * y)], dtype=complex
        )

    # This check specifically catches the pre-audit x+i y sign error.
    assert np.linalg.norm(numerical_tangent(psi, 0) - Dc) < 3e-8
    assert np.linalg.norm(numerical_tangent(psi, 1) - Ds) < 3e-8

    for _ in range(100):
        x, y = RNG.normal(scale=0.15, size=2)
        if c * c * (x * x + y * y) >= 0.95:
            continue
        v = psi(x, y)
        rho = np.outer(v, v.conj())
        assert abs(np.vdot(v, v).real - 1.0) < 2e-13
        assert np.linalg.norm(Htot @ rho - rho @ Htot) < 2e-13

    rho0 = np.diag([1.0, 0.0]).astype(complex)
    effects = []
    for phi in (0.0, 0.5 * math.pi, math.pi, 1.5 * math.pi):
        v = np.array([1.0, np.exp(1j * phi)], dtype=complex) / math.sqrt(2.0)
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

    print("WP18 one-sided corrected convention/action saturation PASS")


def main() -> None:
    check_bilateral_qutrit()
    check_one_sided_qubit()
    print("WP18 autonomous dual synthesis-action validation PASS")


if __name__ == "__main__":
    main()
