#!/usr/bin/env python3
"""Validate the finite-chain sine-profile witness for the high-retention law.

The construction is prior phase-estimation mathematics.  Here it is used only
as an achievability witness showing that the Rev9/Rev10 lower-bound exponent
(1-R)^(-1/2) cannot be improved.
"""

from __future__ import annotations

import math
import numpy as np


def A_of_q(q: float) -> float:
    assert 0.0 <= q < 1.0
    theta = math.acos(q)
    M = int(math.floor(math.pi / (2.0 * theta)))
    if M < 1:
        return 0.0
    return sum(math.cos(m * theta) for m in range(1, M + 1))


def check_one(L: int) -> tuple[float, float, float]:
    assert L >= 2
    theta = math.pi / (L + 1)
    n = np.arange(L, dtype=float)
    a = math.sqrt(2.0 / (L + 1)) * np.sin((n + 1.0) * theta)
    qn = a * a

    assert abs(float(qn.sum()) - 1.0) < 5e-13

    overlap = float(np.sum(a[:-1] * a[1:]))
    mean_n = float(np.sum(n * qn))
    retention = overlap * overlap

    assert abs(overlap - math.cos(theta)) < 5e-13
    assert abs(retention - math.cos(theta) ** 2) < 5e-13
    assert abs(mean_n - (L - 1) / 2.0) < 5e-12

    exact_from_retention = math.pi / (2.0 * math.acos(math.sqrt(retention))) - 1.0
    assert abs(mean_n - exact_from_retention) < 2e-10

    # The universal Herglotz/tail lower bound must be obeyed.
    assert mean_n + 2e-12 >= A_of_q(retention)

    return retention, mean_n, mean_n * math.sqrt(1.0 - retention)


def main() -> None:
    for L in (2, 3, 4, 5, 10, 25, 100, 1000):
        retention, mean_n, scaled = check_one(L)
        print(
            f"L={L:4d}  R1={retention:.15f}  "
            f"nbar={mean_n:.9f}  nbar*sqrt(1-R1)={scaled:.12f}"
        )

    # Sharp exponent: nbar*sqrt(1-R) -> pi/2.
    retention, mean_n, scaled = check_one(20_000)
    assert abs(scaled - math.pi / 2.0) < 1.0e-4

    # Equivalent asymptotic inversion: 1-R ~ pi^2/(4 nbar^2).
    asymptotic_ratio = (1.0 - retention) * mean_n**2
    assert abs(asymptotic_ratio - math.pi**2 / 4.0) < 5.0e-4

    print("Sine-profile divergence exponent sharpness PASS")
    print(f"limit nbar*sqrt(1-R) -> pi/2 = {math.pi/2:.12f}")
    print(f"limit (1-R)*nbar^2 -> pi^2/4 = {math.pi**2/4:.12f}")


if __name__ == "__main__":
    main()
