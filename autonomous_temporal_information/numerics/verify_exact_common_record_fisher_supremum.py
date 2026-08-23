#!/usr/bin/env python3
"""Adversarial validation for WP15 exact common-record Fisher supremum.

Checks:
1. the stated support/kernel basis is orthonormal and gives the exact block A;
2. the SLD-QFI matrix is diag(39/8,47/8) and the weak commutator is 5/4;
3. the explicit dual witness Y has trace 55/8;
4. the exact leading-minor formulas for the LMI positivity certificate agree
   with direct determinants on random lambda,theta values and are nonnegative;
5. random complex vectors satisfy
      |<phi|A|phi>|^2 <= <phi|rho|phi><phi|Y|phi>;
6. random projective and random rank-one POVMs obey Tr F <=55/8;
7. the explicit regular projective sequence converges to 55/8, with the
   support contribution approaching 9/8 and the near-kernel contribution
   approaching 23/4.

Only NumPy is required.
"""

from __future__ import annotations

import math
import numpy as np

RNG = np.random.default_rng(20260822)
TOL = 2e-10


def qfi_matrix(rho: np.ndarray, derivs: list[np.ndarray], tol: float = 1e-12) -> tuple[np.ndarray, list[np.ndarray]]:
    vals, vecs = np.linalg.eigh(rho)
    ls = []
    for d in derivs:
        de = vecs.conj().T @ d @ vecs
        le = np.zeros_like(de)
        for i, pi in enumerate(vals):
            for j, pj in enumerate(vals):
                den = pi + pj
                if den > tol:
                    le[i, j] = 2.0 * de[i, j] / den
        ls.append(vecs @ le @ vecs.conj().T)

    f = np.zeros((len(derivs), len(derivs)), dtype=float)
    for i, li in enumerate(ls):
        for j, lj in enumerate(ls):
            f[i, j] = float(np.real(np.trace(rho @ (li @ lj + lj @ li) / 2.0)))
    return f, ls


def fisher_trace_rank_one_povm(rho: np.ndarray, A: np.ndarray, effects: list[np.ndarray], tol: float = 1e-14) -> float:
    total = 0.0
    for M in effects:
        p = float(np.real(np.trace(rho @ M)))
        if p <= tol:
            continue
        z = np.trace(A @ M)
        total += abs(z) ** 2 / p
    return float(total)


def haar_unitary(n: int) -> np.ndarray:
    x = RNG.normal(size=(n, n)) + 1j * RNG.normal(size=(n, n))
    q, r = np.linalg.qr(x)
    phases = np.diag(r)
    phases = phases / np.where(np.abs(phases) > 0, np.abs(phases), 1.0)
    return q @ np.diag(np.conj(phases))


def random_rank_one_povm(d: int, m: int) -> list[np.ndarray]:
    """Generate a rank-one POVM from a Haar isometry C^d -> C^m."""
    x = RNG.normal(size=(m, d)) + 1j * RNG.normal(size=(m, d))
    q, _ = np.linalg.qr(x)
    V = q[:, :d]
    # Rows r_i obey sum_i r_i^dagger r_i=I_d.
    return [np.outer(V[i, :].conj(), V[i, :]) for i in range(m)]


def build_model():
    sq2 = math.sqrt(2.0)
    sq3 = math.sqrt(3.0)
    sq5 = math.sqrt(5.0)
    sq6 = math.sqrt(6.0)
    sq15 = math.sqrt(15.0)
    sq30 = math.sqrt(30.0)

    q = np.array([0.5, math.sqrt(5.0 / 8.0), 1.0 / (2.0 * sq2)], dtype=complex)
    e1 = np.array([1.0 / sq3, 0.0, -math.sqrt(2.0 / 3.0)], dtype=complex)
    e2 = np.array([-sq15 / 6.0, sq6 / 4.0, -sq30 / 12.0], dtype=complex)
    U = np.column_stack([e1, e2, q])
    assert np.linalg.norm(U.conj().T @ U - np.eye(3)) < 2e-13

    rho_orig = (np.eye(3) - np.outer(q, q.conj())) / 2.0
    A_orig = np.zeros((3, 3), dtype=complex)
    A_orig[1, 0] = 1.0
    A_orig[2, 1] = -sq2

    rho = U.conj().T @ rho_orig @ U
    A = U.conj().T @ A_orig @ U

    rho_expected = np.diag([0.5, 0.5, 0.0]).astype(complex)
    A_expected = np.array(
        [
            [0.0, sq2 / 2.0, sq30 / 6.0],
            [sq2 / 4.0, 0.0, sq6 / 3.0],
            [sq30 / 12.0, -sq6 / 3.0, 0.0],
        ],
        dtype=complex,
    )
    assert np.linalg.norm(rho - rho_expected) < 2e-13
    assert np.linalg.norm(A - A_expected) < 2e-13

    Y = np.array(
        [
            [9.0 / 16.0, 0.0, 0.0],
            [0.0, 9.0 / 16.0, 3.0 * sq15 / 8.0],
            [0.0, 3.0 * sq15 / 8.0, 23.0 / 4.0],
        ],
        dtype=complex,
    )
    return rho, A, Y


def check_basis_qfi_and_commutator(rho, A, Y) -> None:
    dc = (A + A.conj().T) / 2.0
    ds = (A - A.conj().T) / (2j)
    fq, ls = qfi_matrix(rho, [dc, ds])
    target = np.diag([39.0 / 8.0, 47.0 / 8.0])
    assert np.linalg.norm(fq - target) < 2e-12, fq

    comm = np.trace(rho @ (ls[0] @ ls[1] - ls[1] @ ls[0]) / (2j))
    assert abs(float(np.real(comm)) - 5.0 / 4.0) < 2e-12, comm
    assert abs(float(np.imag(comm))) < 2e-12

    assert abs(float(np.trace(Y).real) - 55.0 / 8.0) < 2e-14
    assert np.min(np.linalg.eigvalsh(Y)) > 0.0
    print("Exact basis, SLD-QFI, commutator, and witness trace PASS")


def check_lmi_certificate(rho, A, Y) -> None:
    for _ in range(10000):
        lam = 10.0 ** RNG.uniform(-3.0, 3.0)
        theta = RNG.uniform(0.0, 2.0 * math.pi)
        phase = np.exp(1j * theta)
        M = lam * rho + Y / lam - (phase * A + np.conj(phase) * A.conj().T)
        evals = np.linalg.eigvalsh((M + M.conj().T) / 2.0)
        assert float(np.min(evals)) > -3e-10

        x = lam * lam
        t = math.cos(theta) ** 2
        minor1 = (8.0 * x + 9.0) / (16.0 * lam)
        minor2 = (
            t * (8.0 * x - 9.0) ** 2
            + (1.0 - t) * (64.0 * x * x + 112.0 * x + 81.0)
        ) / (256.0 * x)
        det_formula = (
            t * (8.0 * x - 9.0) ** 2
            + (1.0 - t) * (40.0 * x + 81.0)
        ) / (128.0 * lam**3)

        assert minor1 > 0.0
        assert minor2 > -1e-14
        assert det_formula > -1e-14
        assert abs(np.linalg.det(M[:2, :2]).real - minor2) < 2e-7 * max(1.0, abs(minor2))
        assert abs(np.linalg.det(M).real - det_formula) < 3e-7 * max(1.0, abs(det_formula))

    # Isolated semidefinite equality point t=1, lambda^2=9/8.
    lam = math.sqrt(9.0 / 8.0)
    M = lam * rho + Y / lam - (A + A.conj().T)
    assert np.min(np.linalg.eigvalsh((M + M.conj().T) / 2.0)) > -3e-12
    assert abs(np.linalg.det(M)) < 2e-12
    print("Exact LMI positivity-certificate formulas PASS")


def check_random_vector_witness(rho, A, Y) -> None:
    min_gap = float("inf")
    for _ in range(200000):
        phi = RNG.normal(size=3) + 1j * RNG.normal(size=3)
        # Include highly kernel-dominated vectors.
        if RNG.random() < 0.25:
            phi[:2] *= 10.0 ** RNG.uniform(-5.0, -1.0)
        r = float(np.real(np.vdot(phi, rho @ phi)))
        y = float(np.real(np.vdot(phi, Y @ phi)))
        z = np.vdot(phi, A @ phi)
        gap = r * y - abs(z) ** 2
        min_gap = min(min_gap, gap)
        assert gap > -5e-9 * max(1.0, r * y, abs(z) ** 2)
    print(f"Random complex-vector quadratic witness PASS (min gap {min_gap:.3e})")


def check_random_povms(rho, A) -> None:
    ceiling = 55.0 / 8.0
    best = 0.0

    for _ in range(4000):
        U = haar_unitary(3)
        effects = [np.outer(U[:, i], U[:, i].conj()) for i in range(3)]
        f = fisher_trace_rank_one_povm(rho, A, effects)
        best = max(best, f)
        assert f <= ceiling + 3e-10

    for m in (4, 5, 6, 8, 9):
        for _ in range(1200):
            effects = random_rank_one_povm(3, m)
            comp = sum(effects)
            assert np.linalg.norm(comp - np.eye(3)) < 3e-12
            f = fisher_trace_rank_one_povm(rho, A, effects)
            best = max(best, f)
            assert f <= ceiling + 5e-10

    print(f"Random projective/rank-one POVM upper-bound gate PASS (best {best:.6f})")


def rotation_unitary(q: np.ndarray, t: np.ndarray, eps: float) -> np.ndarray:
    # U q = cos eps q + sin eps t; U t = cos eps t - sin eps q.
    Q = np.outer(q, q.conj())
    T = np.outer(t, t.conj())
    K = np.outer(t, q.conj()) - np.outer(q, t.conj())
    return np.eye(len(q), dtype=complex) + (math.cos(eps) - 1.0) * (Q + T) + math.sin(eps) * K


def check_projective_sequence(rho, A) -> None:
    sq2 = math.sqrt(2.0)
    sq6 = math.sqrt(6.0)
    sq30 = math.sqrt(30.0)

    e1 = np.array([1.0, 0.0, 0.0], dtype=complex)
    e2 = np.array([0.0, 1.0, 0.0], dtype=complex)
    q = np.array([0.0, 0.0, 1.0], dtype=complex)
    sp = (e1 + e2) / math.sqrt(2.0)
    sm = (e1 - e2) / math.sqrt(2.0)

    a = np.array([sq30 / 12.0, -sq6 / 3.0], dtype=float)
    b = np.array([sq30 / 6.0, sq6 / 3.0], dtype=float)
    r = (a - b) / np.linalg.norm(a - b)
    t = np.array([1j * r[0], 1j * r[1], 0.0], dtype=complex)
    assert abs(np.vdot(q, t)) < 1e-15
    assert abs(np.linalg.norm(t) - 1.0) < 1e-15
    assert abs(np.linalg.norm(a - b) ** 2 - 23.0 / 8.0) < 2e-14

    target = 55.0 / 8.0
    values = []
    dark_values = []
    for eps in (0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002):
        U = rotation_unitary(q, t, eps)
        assert np.linalg.norm(U.conj().T @ U - np.eye(3)) < 2e-12
        vecs = [U @ sp, U @ sm, U @ q]
        effects = [np.outer(v, v.conj()) for v in vecs]
        f = fisher_trace_rank_one_povm(rho, A, effects)
        values.append(f)

        Mdark = effects[2]
        pdark = float(np.real(np.trace(rho @ Mdark)))
        zdark = np.trace(A @ Mdark)
        assert pdark > 0.0
        dark_values.append(abs(zdark) ** 2 / pdark)

    assert abs(values[-1] - target) < 8e-3
    assert abs(dark_values[-1] - 23.0 / 4.0) < 8e-3
    assert values[-1] > values[0]

    # Exact limiting support contribution.
    support_effects = [np.outer(sp, sp.conj()), np.outer(sm, sm.conj())]
    fsupp = fisher_trace_rank_one_povm(rho, A, support_effects)
    assert abs(fsupp - 9.0 / 8.0) < 2e-14

    print(f"Regular projective sequence -> 55/8 PASS (last {values[-1]:.9f})")
    print(f"Near-kernel contribution -> 23/4 PASS (last {dark_values[-1]:.9f})")


def main() -> None:
    rho, A, Y = build_model()
    check_basis_qfi_and_commutator(rho, A, Y)
    check_lmi_certificate(rho, A, Y)
    check_random_vector_witness(rho, A, Y)
    check_random_povms(rho, A)
    check_projective_sequence(rho, A)
    print("WP15 exact common-record Fisher supremum validation PASS")


if __name__ == "__main__":
    main()
