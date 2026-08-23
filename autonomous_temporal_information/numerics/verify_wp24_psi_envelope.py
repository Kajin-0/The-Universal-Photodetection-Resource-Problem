#!/usr/bin/env python3
"""Numerical hostile check of the WP13/WP19 scalar envelope Psi_a(e;p,q)."""

from __future__ import annotations

import numpy as np


def psi(a: float, e: float, p: float, q: float) -> float:
    if e <= a * p * p / q:
        return (np.sqrt(a) + np.sqrt(e / q)) ** 2
    return (e + p * a) * (1.0 / p + 1.0 / q)


def brute(a: float, e: float, p: float, q: float, n: int = 200001) -> float:
    if e == 0.0:
        return a
    x = np.linspace(0.0, e / p, n)
    y = np.maximum((e - p * x) / q, 0.0)
    vals = (np.sqrt(a + x) + np.sqrt(y)) ** 2
    return float(vals.max())


def main() -> None:
    rng = np.random.default_rng(11)
    worst = 0.0
    for _ in range(100):
        a = 10.0 ** rng.uniform(-2.0, 2.0)
        e = 10.0 ** rng.uniform(-2.0, 2.0)
        p = 10.0 ** rng.uniform(-1.0, 1.0)
        q = 10.0 ** rng.uniform(-1.0, 1.0)
        exact = psi(a, e, p, q)
        grid = brute(a, e, p, q)
        rel = abs(grid - exact) / max(1.0, abs(exact))
        worst = max(worst, rel)
        if rel > 5e-8:
            raise AssertionError((a, e, p, q, exact, grid, rel))

    # Shared-kernel qutrit benchmark.
    a = 5.0 / 4.0
    e = 247.0 / 16.0
    p = q = 13.0 / 4.0
    np.testing.assert_allclose(psi(a, e, p, q), 12.0, rtol=0, atol=1e-13)

    # Continuity at the branch threshold.
    for a, p, q in [(0.7, 1.3, 2.1), (3.0, 0.4, 1.7), (0.02, 5.0, 0.3)]:
        e = a * p * p / q
        left = (np.sqrt(a) + np.sqrt(e / q)) ** 2
        right = (e + p * a) * (1.0 / p + 1.0 / q)
        np.testing.assert_allclose(left, right, rtol=2e-14, atol=2e-14)

    print(f"WP24 Psi envelope validator: PASS; worst grid relative error={worst:.3e}")


if __name__ == "__main__":
    main()
