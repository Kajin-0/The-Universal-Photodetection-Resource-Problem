#!/usr/bin/env python3
"""Numerical validator for WP31.

The construction deliberately uses infinitely many target-energy shells whose
optimal shell-generator norms diverge, while the state-weighted quadratic cost
remains summable.  Every shell uses a zero-energy ancilla and therefore the
shell generator preserves total energy exactly.

The validator checks, on large finite truncations:
  * exact reduced first derivatives for two coordinates;
  * exact prescribed metric-contracted target kernel Hessian;
  * exact equality V_impl = (1/2) Tr C;
  * convergence of the unbounded-shell cost;
  * divergence of the unweighted shell-generator norm;
  * finiteness of the trace-norm C^2 domination sums used in WP31.
"""

from __future__ import annotations

import math
import numpy as np

R = 0.55
TARGET_DIM = 4
ANC_DIM = 2
DIM = TARGET_DIM * ANC_DIM
S, QX, QY, QZ = range(TARGET_DIM)


def idx(t: int, a: int) -> int:
    return t * ANC_DIM + a


def ket(t: int, a: int) -> np.ndarray:
    v = np.zeros(DIM, dtype=complex)
    v[idx(t, a)] = 1.0
    return v


def ptrace_anc(m: np.ndarray) -> np.ndarray:
    a = m.reshape(TARGET_DIM, ANC_DIM, TARGET_DIM, ANC_DIM)
    return np.einsum("iaja->ij", a)


def comm(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    return a @ b - b @ a


def shell_data(e: int) -> dict[str, float]:
    # Geometric shell weight.  The target energy itself is E=e and is
    # unbounded as e -> infinity.
    p = (1.0 - R) * (R**e)

    # The normalized tangent/flag amplitudes grow without bound, so the
    # direct-sum global generator is genuinely unbounded.  Geometric p_e
    # nevertheless makes the state-weighted quadratic cost summable.
    ax = (e + 1.0) ** 0.60
    ay = 0.70 * (e + 1.0) ** 0.45
    b = 0.40 * (e + 1.0) ** 0.55

    omega_vec = ket(S, 0)
    omega = np.outer(omega_vec, omega_vec.conj())

    # Horizontal tangent vectors plus an excess-curvature flag orthogonal in
    # the ancilla.  All target basis states S,QX,QY,QZ belong to the same
    # degenerate target-energy shell E=e; H_E=0.
    chi_x = ax * ket(QX, 0) + b * ket(QZ, 1)
    chi_y = ay * ket(QY, 0)

    kx = 1j * (
        np.outer(chi_x, omega_vec.conj())
        - np.outer(omega_vec, chi_x.conj())
    )
    ky = 1j * (
        np.outer(chi_y, omega_vec.conj())
        - np.outer(omega_vec, chi_y.conj())
    )

    # First reduced derivatives of the normalized shell state.
    dx = ptrace_anc(-1j * comm(kx, omega))
    dy = ptrace_anc(-1j * comm(ky, omega))

    expected_dx = np.zeros((TARGET_DIM, TARGET_DIM), dtype=complex)
    expected_dx[QX, S] = ax
    expected_dx[S, QX] = ax

    expected_dy = np.zeros((TARGET_DIM, TARGET_DIM), dtype=complex)
    expected_dy[QY, S] = ay
    expected_dy[S, QY] = ay

    # Second derivatives.  Only the target-kernel block is prescribed by the
    # resource theorem.  The ancilla flag removes horizontal/flag cross terms
    # after the partial trace.
    ddx = ptrace_anc(-comm(kx, comm(kx, omega)))
    ddy = ptrace_anc(-comm(ky, comm(ky, omega)))

    qproj = np.diag([0.0, 1.0, 1.0, 1.0])
    c_expected = np.zeros((TARGET_DIM, TARGET_DIM), dtype=complex)
    c_expected[QX, QX] = 2.0 * ax * ax
    c_expected[QY, QY] = 2.0 * ay * ay
    c_expected[QZ, QZ] = 2.0 * b * b

    # Shell contribution to the global mixed-state implementation variance.
    vx = float(np.vdot(omega_vec, kx @ kx @ omega_vec).real)
    vy = float(np.vdot(omega_vec, ky @ ky @ omega_vec).real)
    weighted_cost = p * (vx + vy)
    half_trace_c = 0.5 * p * float(np.trace(c_expected).real)

    # Trace-norm differentiation majorants used in the WP31 proof.
    nx = float(np.linalg.norm(kx, 2))
    ny = float(np.linalg.norm(ky, 2))

    return {
        "p": p,
        "dx_err": float(np.linalg.norm(dx - expected_dx)),
        "dy_err": float(np.linalg.norm(dy - expected_dy)),
        "c_err": float(np.linalg.norm(qproj @ (ddx + ddy) @ qproj - c_expected)),
        "cost": weighted_cost,
        "half_trace_c": half_trace_c,
        "norm_x": nx,
        "norm_y": ny,
        "first_majorant_x": 2.0 * p * nx,
        "first_majorant_y": 2.0 * p * ny,
        "second_majorant_xx": 4.0 * p * nx * nx,
        "second_majorant_yy": 4.0 * p * ny * ny,
        "second_majorant_xy": 4.0 * p * nx * ny,
    }


def main() -> None:
    # Local exact identities on widely separated shells.
    for e in (0, 1, 5, 20, 80, 160):
        d = shell_data(e)
        assert d["dx_err"] < 1e-12
        assert d["dy_err"] < 1e-12
        assert d["c_err"] < 1e-11
        assert abs(d["cost"] - d["half_trace_c"]) < 1e-12

    # Large truncation establishes convergence of the state-weighted cost and
    # the C^2 domination sums while the shell operator norms keep increasing.
    cutoffs = (10, 20, 40, 80, 160)
    costs = []
    first_x = []
    second_xx = []
    second_xy = []
    max_norms = []

    for n in cutoffs:
        data = [shell_data(e) for e in range(n + 1)]
        costs.append(sum(d["cost"] for d in data))
        first_x.append(sum(d["first_majorant_x"] for d in data))
        second_xx.append(sum(d["second_majorant_xx"] for d in data))
        second_xy.append(sum(d["second_majorant_xy"] for d in data))
        max_norms.append(max(max(d["norm_x"], d["norm_y"]) for d in data))

    # Cost convergence is rapid for the chosen geometric shell distribution.
    assert abs(costs[-1] - costs[-2]) < 1e-12
    assert abs(costs[-1] - 4.129595990907466) < 5e-12

    # The global direct-sum generator is not bounded: the shell norms increase
    # strongly with the cutoff.  This is the regime WP30 could not handle with
    # one coherent purification vector.
    assert max_norms[-1] > 2.0 * max_norms[1]
    assert max_norms[-1] > 20.0

    # The actual trace-class derivative majorants converge despite this.
    assert math.isfinite(first_x[-1])
    assert math.isfinite(second_xx[-1])
    assert math.isfinite(second_xy[-1])
    assert abs(first_x[-1] - first_x[-2]) < 1e-12
    assert abs(second_xx[-1] - second_xx[-2]) < 1e-11
    assert abs(second_xy[-1] - second_xy[-2]) < 1e-11

    print("WP31 infinite-shell energy-conserving dilation validator PASS")
    print(f"  V_impl = 1/2 Tr C = {costs[-1]:.15f}")
    print(f"  max shell generator norm at E=160: {max_norms[-1]:.6f}")
    print(f"  first-derivative majorant: {first_x[-1]:.12f}")
    print(f"  second xx majorant: {second_xx[-1]:.12f}")
    print(f"  second xy majorant: {second_xy[-1]:.12f}")


if __name__ == "__main__":
    main()
