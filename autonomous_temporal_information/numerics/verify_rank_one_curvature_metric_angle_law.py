#!/usr/bin/env python3
"""Adversarial validation for WP14 rank-one curvature-metric angle law.

Checks:
1. shorting a positive C to span{u,v} preserves exactly the feasible rank-one
   allocation inequality X<=C;
2. the analytic rank-one frontier y_max(x) matches direct PSD feasibility;
3. the closed piecewise formula for h_(alpha,beta) agrees with dense direct
   optimization on randomized complex two-dimensional instances;
4. the explicit interior optimizer satisfies the matrix constraint and the
   KKT stationary relation whenever the middle branch is active;
5. c=0 gives independent shorted capacities and c=1 gives the shared-budget
   identical-subspace limit;
6. the WP12 nonlinear Phi_a computed with the closed h formula agrees with
   direct primal maximization on randomized moderate-condition instances;
7. two examples with the same ordinary principal angle 60 degrees give
   curvature-whitened cosines 1/sqrt(13) and 2/sqrt(7), proving ordinary
   overlap alone is insufficient.

Only NumPy is required. The script validates the matrix-allocation geometry;
it does not assert novelty of rank-one SDP/SOCP mathematics.
"""

from __future__ import annotations

import math
import numpy as np

RNG = np.random.default_rng(20260822)


def normalize(v: np.ndarray) -> np.ndarray:
    return v / np.linalg.norm(v)


def short_to_span_pd(c: np.ndarray, u_basis: np.ndarray) -> np.ndarray:
    """Short positive-definite C to range(U), with U an isometry."""
    cinv = np.linalg.inv(c)
    middle = np.linalg.inv(u_basis.conj().T @ cinv @ u_basis)
    return u_basis @ middle @ u_basis.conj().T


def span_isometry(u: np.ndarray, v: np.ndarray, tol: float = 1e-11) -> np.ndarray:
    m = np.column_stack([u, v])
    q, r = np.linalg.qr(m)
    rank = int(np.sum(np.abs(np.diag(r)) > tol))
    return q[:, :rank]


def rank_one_invariants(c: np.ndarray, u: np.ndarray, v: np.ndarray) -> tuple[float, float, float]:
    """Return s_u, s_v, curvature-whitened cosine c_metric."""
    ci = np.linalg.inv(c)
    A = float(np.vdot(u, ci @ u).real)
    B = float(np.vdot(v, ci @ v).real)
    m = np.vdot(u, ci @ v)
    su = 1.0 / A
    sv = 1.0 / B
    cm = abs(m) / math.sqrt(A * B)
    cm = min(1.0, max(0.0, float(cm)))
    return su, sv, cm


def y_frontier(x: float, su: float, sv: float, cm: float) -> float:
    den = 1.0 - (1.0 - cm * cm) * x / su
    if abs(den) < 1e-14:
        return sv
    return sv * (1.0 - x / su) / den


def h_closed(alpha: float, beta: float, su: float, sv: float, cm: float) -> float:
    assert alpha > 0.0 and beta > 0.0 and su > 0.0 and sv > 0.0
    if cm < 1e-12:
        return alpha * su + beta * sv
    if 1.0 - cm < 1e-10:
        # Identical-subspace limit. In that case su=sv physically; use the
        # common capacity averaged only to suppress roundoff.
        s = 0.5 * (su + sv)
        return s * max(alpha, beta)

    r = alpha * su / (beta * sv)
    c2 = cm * cm
    if r <= c2:
        return beta * sv
    if r >= 1.0 / c2:
        return alpha * su
    return (
        alpha * su
        + beta * sv
        - 2.0 * cm * math.sqrt(alpha * beta * su * sv)
    ) / (1.0 - c2)


def direct_h(alpha: float, beta: float, su: float, sv: float, cm: float, n: int = 120001) -> float:
    x = np.linspace(0.0, su, n)
    y = np.array([max(0.0, y_frontier(float(xx), su, sv, cm)) for xx in x])
    return float(np.max(alpha * x + beta * y))


def direct_phi(a: float, su: float, sv: float, cm: float, n: int = 120001) -> float:
    x = np.linspace(0.0, su, n)
    y = np.array([max(0.0, y_frontier(float(xx), su, sv, cm)) for xx in x])
    vals = (np.sqrt(a + x) + np.sqrt(y)) ** 2
    return float(np.max(vals))


def variational_phi(a: float, su: float, sv: float, cm: float, n: int = 120001) -> float:
    eta = np.linspace(2e-6, 1.0 - 2e-6, n)
    vals = np.empty_like(eta)
    for i, t in enumerate(eta):
        vals[i] = a / t + h_closed(1.0 / t, 1.0 / (1.0 - t), su, sv, cm)
    return float(np.min(vals))


def check_short_to_span_equivalence() -> None:
    for _ in range(100):
        n = 4
        x = RNG.normal(size=(n, n)) + 1j * RNG.normal(size=(n, n))
        C = x @ x.conj().T + 0.8 * np.eye(n)
        u = normalize(RNG.normal(size=n) + 1j * RNG.normal(size=n))
        v = normalize(RNG.normal(size=n) + 1j * RNG.normal(size=n))
        U = span_isometry(u, v)
        assert U.shape[1] == 2
        Cs = short_to_span_pd(C, U)

        # Work in the S basis for the analytic capacities.
        C2 = U.conj().T @ Cs @ U
        u2 = U.conj().T @ u
        v2 = U.conj().T @ v
        su, sv, cm = rank_one_invariants(C2, u2, v2)

        for frac in (0.0, 0.13, 0.47, 0.81, 0.999):
            xx = frac * su
            yy = 0.7 * max(0.0, y_frontier(xx, su, sv, cm))
            X = xx * np.outer(u, u.conj()) + yy * np.outer(v, v.conj())
            mineig_c = float(np.min(np.linalg.eigvalsh((C - X + (C - X).conj().T) / 2.0)))
            mineig_s = float(np.min(np.linalg.eigvalsh(U.conj().T @ (Cs - X) @ U)))
            assert mineig_c > -2e-9
            assert mineig_s > -2e-9

    print("Short-to-span exact reduction PASS")


def check_random_frontier_and_h() -> None:
    for _ in range(250):
        x = RNG.normal(size=(2, 2)) + 1j * RNG.normal(size=(2, 2))
        C = x @ x.conj().T + 0.5 * np.eye(2)
        u = normalize(RNG.normal(size=2) + 1j * RNG.normal(size=2))
        v = normalize(RNG.normal(size=2) + 1j * RNG.normal(size=2))
        if abs(np.vdot(u, v)) > 0.9999:
            continue

        su, sv, cm = rank_one_invariants(C, u, v)
        alpha = 0.05 + 4.0 * RNG.random()
        beta = 0.05 + 4.0 * RNG.random()

        exact = h_closed(alpha, beta, su, sv, cm)
        direct = direct_h(alpha, beta, su, sv, cm, n=30001)
        assert abs(exact - direct) < 7e-5 * max(1.0, exact), (exact, direct, su, sv, cm)

        # Test a random interior point below the frontier directly in matrix form.
        frac = RNG.random()
        xx = frac * su
        yy = RNG.random() * max(0.0, y_frontier(xx, su, sv, cm))
        M = C - xx * np.outer(u, u.conj()) - yy * np.outer(v, v.conj())
        assert np.min(np.linalg.eigvalsh((M + M.conj().T) / 2.0)) > -2e-9

    print("Random rank-one frontier and linear allocation formula PASS")


def check_interior_optimizer() -> None:
    hits = 0
    for _ in range(2000):
        x = RNG.normal(size=(2, 2)) + 1j * RNG.normal(size=(2, 2))
        C = x @ x.conj().T + 0.5 * np.eye(2)
        u = normalize(RNG.normal(size=2) + 1j * RNG.normal(size=2))
        v = normalize(RNG.normal(size=2) + 1j * RNG.normal(size=2))
        su, sv, cm = rank_one_invariants(C, u, v)
        if cm < 1e-5 or cm > 0.999:
            continue
        alpha = 0.1 + 3.0 * RNG.random()
        beta = 0.1 + 3.0 * RNG.random()
        r = alpha * su / (beta * sv)
        if not (cm * cm < r < 1.0 / (cm * cm)):
            continue

        xs = (su - cm * math.sqrt((beta / alpha) * su * sv)) / (1.0 - cm * cm)
        ys = (sv - cm * math.sqrt((alpha / beta) * su * sv)) / (1.0 - cm * cm)
        assert xs > -2e-10 and ys > -2e-10
        assert abs(ys - y_frontier(xs, su, sv, cm)) < 3e-9 * max(1.0, ys)

        exact = h_closed(alpha, beta, su, sv, cm)
        val = alpha * xs + beta * ys
        assert abs(val - exact) < 3e-9 * max(1.0, exact)
        hits += 1
        if hits >= 100:
            break

    assert hits >= 50
    print("Interior optimizer/KKT formula PASS")


def check_limiting_geometries() -> None:
    # Whitened orthogonal: C=I, u=e0, v=e1.
    su = sv = 1.0
    cm = 0.0
    for alpha, beta in ((1.0, 2.0), (4.3, 0.7), (0.2, 0.5)):
        assert abs(h_closed(alpha, beta, su, sv, cm) - (alpha + beta)) < 1e-14

    # Identical subspace shared budget.
    cm = 1.0
    for alpha, beta in ((1.0, 2.0), (4.3, 0.7), (0.2, 0.5)):
        assert abs(h_closed(alpha, beta, 2.5, 2.5, cm) - 2.5 * max(alpha, beta)) < 1e-14

    print("Whitened-orthogonal and identical-subspace limits PASS")


def check_phi_reduction() -> None:
    for _ in range(25):
        x = RNG.normal(size=(2, 2)) + 1j * RNG.normal(size=(2, 2))
        C = x @ x.conj().T + 1.0 * np.eye(2)
        u = normalize(RNG.normal(size=2) + 1j * RNG.normal(size=2))
        v = normalize(RNG.normal(size=2) + 1j * RNG.normal(size=2))
        su, sv, cm = rank_one_invariants(C, u, v)
        a = 0.1 + 2.0 * RNG.random()

        direct = direct_phi(a, su, sv, cm, n=40001)
        var = variational_phi(a, su, sv, cm, n=40001)
        assert abs(direct - var) < 2.5e-4 * max(1.0, direct), (direct, var)

    print("Rank-one WP12 Phi: direct primal vs explicit-h variational form PASS")


def check_same_ordinary_angle_different_curvature_angle() -> None:
    u = np.array([1.0, 0.0])
    v = np.array([0.5, math.sqrt(3.0) / 2.0])
    assert abs(float(np.dot(u, v)) - 0.5) < 1e-15

    C1 = np.diag([4.0, 1.0])
    _, _, c1 = rank_one_invariants(C1, u, v)
    assert abs(c1 - 1.0 / math.sqrt(13.0)) < 2e-14

    C2 = np.diag([0.25, 1.0])
    _, _, c2 = rank_one_invariants(C2, u, v)
    assert abs(c2 - 2.0 / math.sqrt(7.0)) < 2e-14

    assert abs(c1 - c2) > 0.45
    print("Same ordinary angle / different curvature-metric angle counterexample PASS")


def main() -> None:
    check_short_to_span_equivalence()
    check_random_frontier_and_h()
    check_interior_optimizer()
    check_limiting_geometries()
    check_phi_reduction()
    check_same_ordinary_angle_different_curvature_angle()
    print("WP14 rank-one curvature-metric principal-angle validation PASS")


if __name__ == "__main__":
    main()
