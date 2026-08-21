#!/usr/bin/env python3
"""Reproduce the analytic continuous-time Type-II spectral-survival bounds.

Model: homogeneous Poisson input of rate lambda with deterministic paralyzable
dead time tau.  Dimensionless operating point rho=lambda*tau and temporal
frequency y=omega*tau.

The script checks the saturation-point results from WP07:
  G(0)=0 for the complete record at rho=1,
  G(omega) >= L_1(omega*tau) > 0 for omega != 0,
  L_1(pi) = exp(-1)*(1+4/pi^2),
  lim_{|omega|->infty} G(omega) = exp(-1).

Only the Python standard library is required.
"""

import csv
import math
from pathlib import Path


def sinc(y: float) -> float:
    if abs(y) < 1e-8:
        y2 = y * y
        return 1.0 - y2 / 6.0 + y2 * y2 / 120.0
    return math.sin(y) / y


def mean_transfer_abs2(rho: float, y: float) -> float:
    if abs(y) < 1e-7:
        # Expansion of |1-rho*(1-exp(-iy))/(iy)|^2.
        # This branch is used only for numerical stability.
        s = sinc(y)
        one_minus_cos_over_y2 = 0.5 - y * y / 24.0 + y**4 / 720.0
    else:
        s = math.sin(y) / y
        one_minus_cos_over_y2 = (1.0 - math.cos(y)) / (y * y)
    return 1.0 - 2.0 * rho * s + 2.0 * rho * rho * one_minus_cos_over_y2


def renewal_noise_factor(rho: float, y: float) -> float:
    return 1.0 - 2.0 * rho * math.exp(-rho) * sinc(y)


def fisher_lower_bound(rho: float, y: float) -> float:
    return (
        math.exp(-rho)
        * mean_transfer_abs2(rho, y)
        / renewal_noise_factor(rho, y)
    )


def main() -> None:
    rho = 1.0
    exact_pi_bound = math.exp(-1.0) * (1.0 + 4.0 / math.pi**2)
    numerical_pi_bound = fisher_lower_bound(rho, math.pi)
    assert abs(numerical_pi_bound - exact_pi_bound) < 1e-14

    # Positivity on a dense nonzero grid.
    for j in range(1, 20001):
        y = 20.0 * math.pi * j / 20000.0
        assert renewal_noise_factor(rho, y) > 0.0
        assert fisher_lower_bound(rho, y) > 0.0

    # Check the small-y coefficient L_1(y) ~ y^2/[4(e-2)].
    coefficient = 1.0 / (4.0 * (math.e - 2.0))
    y_small = 1e-3
    small_ratio = fisher_lower_bound(rho, y_small) / (y_small * y_small)
    assert abs(small_ratio - coefficient) / coefficient < 2e-5

    # The analytic lower bound tends to exp(-1), consistent with the exact
    # complete-record high-frequency limit proved separately in WP07.
    asymptote = math.exp(-1.0)
    y_large = 1e6 + 0.37
    assert abs(fisher_lower_bound(rho, y_large) - asymptote) < 2e-6

    print(f"rho = {rho:.1f}")
    print("complete-record DC Fisher retention: G(0) = 0 (analytic theorem)")
    print(f"L_1(pi) = {numerical_pi_bound:.12f}")
    print(f"small-y coefficient = 1/[4(e-2)] = {coefficient:.12f}")
    print(f"exact high-frequency limit = exp(-1) = {asymptote:.12f}")

    out = Path(__file__).with_name("continuous_paralyzable_lower_bound_rho1.csv")
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["y_equals_omega_tau", "lower_bound_L1"])
        for j in range(0, 161):
            y = 8.0 * math.pi * j / 160.0
            value = 0.0 if j == 0 else fisher_lower_bound(rho, y)
            writer.writerow([f"{y:.15g}", f"{value:.15g}"])
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
