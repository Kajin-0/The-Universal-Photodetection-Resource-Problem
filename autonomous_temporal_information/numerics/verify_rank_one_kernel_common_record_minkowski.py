#!/usr/bin/env python3
"""Independent adversarial validator for WP16.

Checks:
1. closed form kappa = ||a||^2+||b||^2+2|a^dagger b| against random
   directional maximization;
2. traceless 2x2 numerical-radius formula and support Fisher identity
   R(B)=4 w(B)^2;
3. random full qutrit rank-one POVMs satisfy
   Tr F <= [2 w(B)+sqrt(2 kappa)]^2;
4. the signed three-cycle has exact WP16 ceiling 9 and its spectral projective
   measurement attains 9;
5. the false additive law would give only 5 for that exact extremizer;
6. a second model with the same R(B)=1 and kappa=2 obeys the independent
   orientation-sensitive WP11 ceiling 6, proving the two WP16 scalar invariants
   do not determine the exact common-record optimum.

Uses NumPy only.
"""

from __future__ import annotations

import math
import numpy as np

RNG = np.random.default_rng(20260822)


def random_rank1_povm(d: int, m: int) -> np.ndarray:
    """Columns w_j define effects |w_j><w_j| summing to I."""
    v = RNG.normal(size=(d, m)) + 1j * RNG.normal(size=(d, m))
    s = v @ v.conj().T
    vals, vecs = np.linalg.eigh((s + s.conj().T) / 2.0)
    s_inv_half = vecs @ np.diag(1.0 / np.sqrt(vals)) @ vecs.conj().T
    return s_inv_half @ v


def fisher_trace(A: np.ndarray, W: np.ndarray) -> float:
    rho = np.diag([0.5, 0.5, 0.0]).astype(complex)
    out = 0.0
    for j in range(W.shape[1]):
        w = W[:, j]
        p = float(np.vdot(w, rho @ w).real)
        z = np.vdot(w, A @ w)
        if p > 1e-13:
            out += abs(z) ** 2 / p
    return float(out)


def numerical_radius_traceless_2x2(B: np.ndarray) -> float:
    """w(B)^2=(Tr B^dag B + 2|det B|)/4 for Tr B=0."""
    assert abs(np.trace(B)) < 1e-10
    w2 = (
        float(np.trace(B.conj().T @ B).real)
        + 2.0 * abs(np.linalg.det(B))
    ) / 4.0
    return math.sqrt(max(0.0, w2))


def kappa_closed(a: np.ndarray, b: np.ndarray) -> float:
    return float(
        np.vdot(a, a).real
        + np.vdot(b, b).real
        + 2.0 * abs(np.vdot(a, b))
    )


def check_kappa() -> None:
    for _ in range(40):
        a = RNG.normal(size=2) + 1j * RNG.normal(size=2)
        b = RNG.normal(size=2) + 1j * RNG.normal(size=2)
        exact = kappa_closed(a, b)
        sampled = 0.0
        for _ in range(3000):
            u = RNG.normal(size=2) + 1j * RNG.normal(size=2)
            u /= np.linalg.norm(u)
            tau = np.exp(1j * RNG.uniform(0.0, 2.0 * math.pi))
            val = abs(tau * np.vdot(u, b) + np.conj(tau) * np.vdot(a, u)) ** 2
            sampled = max(sampled, float(val))
        assert sampled <= exact + 1e-10
        assert sampled >= 0.92 * exact
    print("WP16 kappa closed form PASS")


def check_support_identity() -> None:
    for _ in range(50):
        B = RNG.normal(size=(2, 2)) + 1j * RNG.normal(size=(2, 2))
        B -= 0.5 * np.trace(B) * np.eye(2)
        w = numerical_radius_traceless_2x2(B)
        target = 4.0 * w * w

        # Random support rank-one POVMs cannot exceed target.
        best = 0.0
        for _ in range(300):
            W = random_rank1_povm(2, int(RNG.integers(2, 7)))
            value = 0.0
            for j in range(W.shape[1]):
                x = W[:, j]
                p = 0.5 * float(np.vdot(x, x).real)
                z = np.vdot(x, B @ x)
                value += abs(z) ** 2 / p
            best = max(best, float(value))
        assert best <= target + 5e-10
    print("Traceless-qutrit support identity R(B)=4w(B)^2 PASS")


def check_random_full_povms() -> None:
    worst_ratio = 0.0
    for _ in range(35):
        B = RNG.normal(size=(2, 2)) + 1j * RNG.normal(size=(2, 2))
        B -= 0.5 * np.trace(B) * np.eye(2)
        a = RNG.normal(size=2) + 1j * RNG.normal(size=2)
        b = RNG.normal(size=2) + 1j * RNG.normal(size=2)
        A = np.block(
            [
                [B, b[:, None]],
                [a.conj()[None, :], np.zeros((1, 1), dtype=complex)],
            ]
        )
        w = numerical_radius_traceless_2x2(B)
        kap = kappa_closed(a, b)
        bound = (2.0 * w + math.sqrt(2.0 * kap)) ** 2

        for _ in range(400):
            W = random_rank1_povm(3, int(RNG.integers(3, 10)))
            value = fisher_trace(A, W)
            assert value <= bound + 2e-9, (value, bound)
            worst_ratio = max(worst_ratio, value / bound if bound > 0 else 0.0)
    print(f"Random arbitrary-rank-one-POVM WP16 bound PASS; max sampled ratio={worst_ratio:.6f}")


def check_signed_cycle_extremizer() -> None:
    A = np.array(
        [
            [0.0, 1.0, 0.0],
            [0.0, 0.0, -1.0],
            [1.0, 0.0, 0.0],
        ],
        dtype=complex,
    )
    assert np.linalg.norm(A.conj().T @ A - np.eye(3)) < 1e-12
    assert np.linalg.norm(A @ A @ A + np.eye(3)) < 1e-12

    B = A[:2, :2]
    a = np.conj(A[2, :2])
    b = A[:2, 2]
    w = numerical_radius_traceless_2x2(B)
    kap = kappa_closed(a, b)
    R = 4.0 * w * w
    singular = 2.0 * kap
    bound = (math.sqrt(R) + math.sqrt(singular)) ** 2
    additive_false = R + singular

    assert abs(R - 1.0) < 1e-12
    assert abs(kap - 2.0) < 1e-12
    assert abs(bound - 9.0) < 1e-12
    assert abs(additive_false - 5.0) < 1e-12

    vals, vecs = np.linalg.eig(A)
    # Normalize eigenvectors and use their spectral projectors.
    for j in range(3):
        vecs[:, j] /= np.linalg.norm(vecs[:, j])
    # np.linalg.eig returns an orthonormal basis for this normal matrix up to tiny error.
    assert np.linalg.norm(vecs.conj().T @ vecs - np.eye(3)) < 2e-12
    achieved = fisher_trace(A, vecs)
    assert abs(achieved - 9.0) < 2e-11

    print("Signed three-cycle exact Tr F=9 saturation PASS")
    print("Naive additive compatibility 5 vs exact 9 counterexample PASS")


def check_same_scalars_different_optima() -> None:
    # Same B as the signed cycle, but only one kernel orientation.
    B = np.array([[0.0, 1.0], [0.0, 0.0]], dtype=complex)
    a = np.array([math.sqrt(2.0), 0.0], dtype=complex)
    b = np.zeros(2, dtype=complex)
    A = np.block(
        [
            [B, b[:, None]],
            [a.conj()[None, :], np.zeros((1, 1), dtype=complex)],
        ]
    )

    w = numerical_radius_traceless_2x2(B)
    kap = kappa_closed(a, b)
    assert abs(4.0 * w * w - 1.0) < 1e-12
    assert abs(kap - 2.0) < 1e-12

    # Specialized WP11 one-sided weighted-tangent ceiling:
    # rho^+=2P, J_B=2 Tr(BB^dag)=2, J_+=2||a||^2=4.
    J_B = 2.0 * float(np.trace(B @ B.conj().T).real)
    J_plus = 2.0 * float(np.vdot(a, a).real)
    orientation_ceiling = J_B + J_plus
    assert abs(orientation_ceiling - 6.0) < 1e-12
    assert orientation_ceiling < 9.0

    # Adversarial random POVMs should obey the sharper orientation ceiling.
    best = 0.0
    for _ in range(12000):
        W = random_rank1_povm(3, int(RNG.integers(3, 8)))
        value = fisher_trace(A, W)
        assert value <= orientation_ceiling + 2e-9
        best = max(best, value)

    print(f"Same (R,kappa) but independent ceiling 6<9 PASS; sampled best={best:.6f}")


def main() -> None:
    check_kappa()
    check_support_identity()
    check_random_full_povms()
    check_signed_cycle_extremizer()
    check_same_scalars_different_optima()
    print("WP16 rank-one-kernel common-record validation PASS")


if __name__ == "__main__":
    main()
