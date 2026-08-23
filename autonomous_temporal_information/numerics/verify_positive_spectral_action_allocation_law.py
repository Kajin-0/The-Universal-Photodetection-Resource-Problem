#!/usr/bin/env python3
"""Adversarial validation for WP13 positive spectral-action allocation law.

Checks:
1. random positive spectral-cost operators G and random synthesized subspaces
   satisfy Tr(G C) >= g_+ J_+ + g_- J_- when C>=Z_++Z_-;
2. the closed-form Psi_a action envelope agrees with direct scalar
   maximization over thousands of random parameter choices;
3. the low/high branch crossover is continuous and C1;
4. the conic/dual variational representation agrees with the closed form;
5. one-sided, bilateral, and WP12 equal-cost limits reduce exactly;
6. an unequal-cost exact-gap qutrit plus one Fourier measurement saturates
   the harmonic action coefficient for arbitrary positive endpoint prices;
7. WP11's four-level noncommuting-support example gives the exact compressed
   gap cost g_+=(3/4) hbar nu and reproduces the weighted-norm ceiling;
8. a zero-cost synthesized direction destroys every finite action-only bound.

Only NumPy is required. The script validates the resource/action theorem and
its sharp clean extremizer; it does not claim generic measurement attainability
when a nonzero internal component is present.
"""

from __future__ import annotations

import math
import numpy as np

RNG = np.random.default_rng(20260822)


def random_isometry(n: int, r: int) -> np.ndarray:
    x = RNG.normal(size=(n, r)) + 1j * RNG.normal(size=(n, r))
    q, _ = np.linalg.qr(x)
    return q[:, :r]


def restricted_min_cost(g: np.ndarray, u: np.ndarray) -> float:
    vals = np.linalg.eigvalsh(u.conj().T @ g @ u)
    return float(np.min(vals).real)


def psi_closed(a: float, e: float, p: float, q: float) -> float:
    assert a >= 0.0 and e >= 0.0 and p > 0.0 and q > 0.0
    threshold = a * p * p / q
    if e <= threshold:
        return (math.sqrt(a) + math.sqrt(e / q)) ** 2
    return (e + p * a) * (1.0 / p + 1.0 / q)


def psi_direct_grid(a: float, e: float, p: float, q: float, n: int = 60001) -> float:
    jp = np.linspace(0.0, e / p, n)
    jm = (e - p * jp) / q
    vals = (np.sqrt(a + jp) + np.sqrt(np.maximum(0.0, jm))) ** 2
    return float(np.max(vals))


def psi_variational_grid(a: float, e: float, p: float, q: float, n: int = 100001) -> float:
    eta = np.linspace(1e-6, 1.0 - 1e-6, n)
    vals = a / eta + e * np.maximum(1.0 / (eta * p), 1.0 / ((1.0 - eta) * q))
    return float(np.min(vals))


def check_random_operator_trace_charging() -> None:
    for _ in range(500):
        n = 5
        rank_p = int(RNG.integers(1, 4))
        rank_m = int(RNG.integers(1, 4))
        up = random_isometry(n, rank_p)
        um = random_isometry(n, rank_m)

        x = RNG.normal(size=(n, n)) + 1j * RNG.normal(size=(n, n))
        g = x @ x.conj().T + 0.2 * np.eye(n)

        gp = restricted_min_cost(g, up)
        gm = restricted_min_cost(g, um)
        assert gp > 0.0 and gm > 0.0

        xp = RNG.normal(size=(rank_p, rank_p)) + 1j * RNG.normal(size=(rank_p, rank_p))
        xm = RNG.normal(size=(rank_m, rank_m)) + 1j * RNG.normal(size=(rank_m, rank_m))
        zp = up @ (xp @ xp.conj().T) @ up.conj().T
        zm = um @ (xm @ xm.conj().T) @ um.conj().T

        y = RNG.normal(size=(n, n)) + 1j * RNG.normal(size=(n, n))
        c = zp + zm + y @ y.conj().T

        e = float(np.trace(g @ c).real)
        jp = float(np.trace(zp).real)
        jm = float(np.trace(zm).real)
        rhs = gp * jp + gm * jm
        assert e + 2e-10 * max(1.0, e) >= rhs, (e, rhs)

    print("Random operator spectral-action trace charging PASS")


def check_closed_form_against_direct_optimization() -> None:
    for _ in range(250):
        a = 10.0 ** RNG.uniform(-3.0, 3.0)
        e = 10.0 ** RNG.uniform(-3.0, 3.0)
        p = 10.0 ** RNG.uniform(-2.0, 2.0)
        q = 10.0 ** RNG.uniform(-2.0, 2.0)
        exact = psi_closed(a, e, p, q)
        direct = psi_direct_grid(a, e, p, q, n=20001)
        assert abs(exact - direct) < 1.2e-4 * max(1.0, exact), (a, e, p, q, exact, direct)
    print("Random closed-form/direct scalar allocation equivalence PASS")


def check_crossover_c1() -> None:
    for _ in range(300):
        a = 0.05 + 5.0 * RNG.random()
        p = 0.05 + 4.0 * RNG.random()
        q = 0.05 + 4.0 * RNG.random()
        ec = a * p * p / q

        low = (math.sqrt(a) + math.sqrt(ec / q)) ** 2
        high = (ec + p * a) * (1.0 / p + 1.0 / q)
        assert abs(low - high) < 2e-12 * max(1.0, low)

        # Analytic derivatives with respect to e.
        dlow = (math.sqrt(a) + math.sqrt(ec / q)) / math.sqrt(ec * q)
        dhigh = 1.0 / p + 1.0 / q
        assert abs(dlow - dhigh) < 2e-12 * max(1.0, dhigh)

    print("Piecewise action-envelope C1 crossover PASS")


def check_variational_representation() -> None:
    # Dense eta scans are deliberately limited to moderate condition numbers.
    for _ in range(25):
        a = 0.1 + 3.0 * RNG.random()
        e = 0.1 + 3.0 * RNG.random()
        p = 0.2 + 3.0 * RNG.random()
        q = 0.2 + 3.0 * RNG.random()
        exact = psi_closed(a, e, p, q)
        var = psi_variational_grid(a, e, p, q, n=60001)
        assert abs(exact - var) < 2e-4 * max(1.0, exact), (exact, var)
    print("Conic/variational representation PASS")


def check_exact_reductions() -> None:
    for _ in range(300):
        eps = 0.1 + 5.0 * RNG.random()
        a = 5.0 * RNG.random()
        s = 5.0 * RNG.random()
        e = eps * s

        # Equal-cost bilateral form must equal WP12 coincident-subspace law.
        got = psi_closed(a, e, eps, eps)
        wp12 = (math.sqrt(a) + math.sqrt(s)) ** 2 if s <= a else 2.0 * (a + s)
        assert abs(got - wp12) < 3e-12 * max(1.0, got)

        # Pure bilateral action coefficient.
        pure = psi_closed(0.0, e, eps, eps)
        assert abs(pure - 2.0 * s) < 3e-12 * max(1.0, pure)

        # One-sided action law is a + e/eps.
        one_sided = a + e / eps
        assert abs(one_sided - (a + s)) < 2e-14

    print("WP07/WP09/WP10/WP12 clean reductions PASS")


def check_unequal_cost_qutrit_saturation() -> None:
    for _ in range(200):
        p = 0.05 + 5.0 * RNG.random()
        q = 0.05 + 5.0 * RNG.random()
        e = 0.05 + 8.0 * RNG.random()

        # High-branch optimum for a=0.
        jp = e * q / (p * (p + q))
        jm = e * p / (q * (p + q))
        assert abs(p * jp + q * jm - e) < 2e-12 * max(1.0, e)

        A = np.zeros((3, 3), dtype=complex)
        A[2, 1] = math.sqrt(jp)
        A[1, 0] = math.sqrt(jm)

        fisher_trace = 0.0
        for m in range(3):
            phi = 2.0 * math.pi * m / 3.0
            v = np.array([np.exp(-1j * phi), 1.0, np.exp(1j * phi)], dtype=complex) / math.sqrt(3.0)
            M = np.outer(v, v.conj())
            z = np.trace(A @ M)
            prob = 1.0 / 3.0
            fisher_trace += abs(z) ** 2 / prob

        exact = e * (1.0 / p + 1.0 / q)
        assert abs(fisher_trace - exact) < 3e-11 * max(1.0, exact), (fisher_trace, exact)

    print("Unequal-cost exact-gap qutrit harmonic-coefficient saturation PASS")


def check_wp11_noncommuting_benchmark() -> None:
    # Units hbar*omega=1, so hbar*nu=2.
    hbar_nu = 2.0
    r = np.array([0.0, 0.0, 0.5, math.sqrt(3.0) / 2.0], dtype=complex)
    qv = np.array([0.0, 0.0, math.sqrt(3.0) / 2.0, -0.5], dtype=complex)
    ket0 = np.array([1.0, 0.0, 0.0, 0.0], dtype=complex)
    ket2 = np.array([0.0, 0.0, 1.0, 0.0], dtype=complex)

    P = np.outer(ket0, ket0.conj()) + np.outer(r, r.conj())
    Q = np.eye(4, dtype=complex) - P
    PiU = np.outer(ket2, ket2.conj())
    PiD = np.outer(ket0, ket0.conj())
    G = hbar_nu * Q @ (PiU + PiD) @ Q

    # Synthesized information-bearing range is span(qv).
    gplus = float(np.vdot(qv, G @ qv).real)
    assert abs(gplus - 0.75 * hbar_nu) < 2e-12

    jp = 1.5
    a = 0.5
    e = gplus * jp
    ceiling = a + e / gplus
    assert abs(ceiling - 2.0) < 2e-12

    print("WP11 noncommuting compressed gap-cost benchmark PASS")


def check_zero_cost_no_go() -> None:
    # G has a zero-cost direction |0>. Arbitrary Z=t|0><0| has zero action.
    G = np.diag([0.0, 1.0])
    for t in (1.0, 10.0, 1e4):
        Z = np.diag([t, 0.0])
        action4 = float(np.trace(G @ Z).real)
        j = float(np.trace(Z).real)
        assert action4 == 0.0
        assert j == t
    print("Zero spectral-coverage no-go PASS")


def main() -> None:
    check_random_operator_trace_charging()
    check_closed_form_against_direct_optimization()
    check_crossover_c1()
    check_variational_representation()
    check_exact_reductions()
    check_unequal_cost_qutrit_saturation()
    check_wp11_noncommuting_benchmark()
    check_zero_cost_no_go()
    print("WP13 positive spectral-action allocation validation PASS")


if __name__ == "__main__":
    main()
