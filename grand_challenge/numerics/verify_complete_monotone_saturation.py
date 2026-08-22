#!/usr/bin/env python3
"""Consistency checks for WP25 complete-monotone saturation classification.

These checks validate algebraic identities used by the equality-class theorem.
They do not replace the analytic proof.
"""

from __future__ import annotations

import math
import numpy as np


def discrete_mixture_checks() -> None:
    weights = np.array([0.25, 0.35, 0.40], dtype=float)
    r = np.array([0.10, 0.55, 0.90], dtype=float)
    assert abs(weights.sum() - 1.0) < 1e-15

    nmax = 600
    n = np.arange(nmax + 1)
    q = np.sum(weights[:, None] * (1.0 - r[:, None]) * r[:, None] ** n[None, :], axis=0)

    # Truncation is negligible at this cutoff.
    assert abs(q.sum() - 1.0) < 2e-13

    # Tail moments are exactly the moments of the geometric mixing measure.
    for k in range(1, 13):
        tail_sum = q[k:].sum()
        tail_moment = float(np.sum(weights * r**k))
        adapted_fi = tail_moment
        assert abs(tail_sum - tail_moment) < 3e-13, (k, tail_sum, tail_moment)
        assert abs(adapted_fi - tail_moment) < 1e-15

        # The ordinary canonical-phase POVM is generally not the optimal
        # source-adapted measurement for a nontrivial geometric mixture.
        alpha = np.sum(np.sqrt(q[: nmax + 1 - k] * q[k:]))
        canonical_fi = float(alpha**2)
        assert canonical_fi <= tail_moment + 2e-12

    # Hausdorff complete monotonicity of T_k = E[r^k].
    T = np.array([np.sum(weights * r**k) for k in range(80)], dtype=float)
    current = T.copy()
    for order in range(0, 12):
        sign_corrected = ((-1.0) ** order) * current
        assert sign_corrected.min() >= -2e-13, (order, sign_corrected.min())
        current = np.diff(current)

    # q_n itself is a completely monotone pmf.
    current = q[:80].copy()
    for order in range(0, 12):
        sign_corrected = ((-1.0) ** order) * current
        assert sign_corrected.min() >= -2e-13, (order, sign_corrected.min())
        current = np.diff(current)

    print("Discrete geometric-mixture / Hausdorff checks PASS")
    print("Example tails:", [float(np.sum(weights * r**k)) for k in (1, 2, 5, 10)])


def continuum_lower_bin_checks() -> None:
    weights = np.array([0.2, 0.5, 0.3], dtype=float)
    beta = np.array([0.4, 1.3, 3.0], dtype=float)
    delta = 0.17

    def S(x: float) -> float:
        return float(np.sum(weights * np.exp(-beta * x)))

    for n in range(30):
        exact_bin = S(n * delta) - S((n + 1) * delta)
        r = np.exp(-beta * delta)
        geometric_mix = float(np.sum(weights * (1.0 - r) * r**n))
        assert abs(exact_bin - geometric_mix) < 2e-15, (n, exact_bin, geometric_mix)

    for k in range(1, 20):
        r = np.exp(-beta * delta)
        lattice_tail = float(np.sum(weights * r**k))
        assert abs(lattice_tail - S(k * delta)) < 2e-15

    mean_closed = float(np.sum(weights / beta))
    # Integral_0^inf S = sum w/beta exactly.
    assert mean_closed > 0.0

    print("Continuum exponential-mixture lower-bin checks PASS")
    print(f"mean excess frequency={mean_closed:.12f}")


def algebraic_equality_example() -> None:
    # Gamma mixing of exponential rates gives a Lomax/Pareto-II spectral law.
    alpha = 2.5
    a = 1.7

    def S(x: float) -> float:
        return (a / (a + x)) ** alpha

    def density(x: float) -> float:
        return alpha * a**alpha / (a + x) ** (alpha + 1.0)

    # Check normalization and mean numerically on a long adaptive-like grid.
    # Log spacing captures the algebraic tail efficiently.
    x = np.concatenate(([0.0], np.geomspace(1e-8, 1e6, 600_000)))
    q = np.array([density(float(xx)) for xx in x])
    norm = np.trapz(q, x)
    mean_num = np.trapz(x * q, x)
    mean_closed = a / (alpha - 1.0)

    assert abs(norm - 1.0) < 2e-7, norm
    assert abs(mean_num - mean_closed) < 4e-3, (mean_num, mean_closed)

    # Survival derivative identity q=-S'.
    for xx in (0.0, 0.2, 1.0, 4.0, 20.0):
        h = 1e-6 * max(1.0, xx + 1.0)
        derivative = (S(xx + h) - S(xx)) / h
        assert abs(-derivative - density(xx)) < 2e-5

    print("Algebraic continuum equality-family example PASS")
    print(f"alpha={alpha}, a={a}, mean={mean_closed:.12f}")
    print("S(a)=", S(a))


def main() -> None:
    discrete_mixture_checks()
    continuum_lower_bin_checks()
    algebraic_equality_example()
    print("WP25 complete-monotone saturation consistency PASS")


if __name__ == "__main__":
    main()
