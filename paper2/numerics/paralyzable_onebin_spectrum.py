#!/usr/bin/env python3
"""Reproduce WP05/WP06 one-bin paralyzable Fisher-spectrum results.

Model:
    X_n ~ Bernoulli(p_n), independent,
    Y_n = X_n (1-X_{n-1}).

At p=1/2, this script evaluates both:
  1. the exact renewal-series representation; and
  2. the WP06 closed form

      G(omega) = 1 - 1/(2x) + ln(1+4x)/(8x^2),
      x = 1-cos(omega),

with continuous value G(0)=0.  It verifies the Nyquist value
3/4 + ln(3)/16, checks series/closed-form agreement, checks sampled strict
monotonicity on (0,pi), and writes the frequency table.

Only the Python standard library is required.
"""

import cmath
import csv
import math
from pathlib import Path


def interval_response_half(d: int, z: complex) -> complex:
    """A_d(z) at p=q=1/2, conditional on a renewal interval D=d."""
    total = 0j
    for n in range(1, d):
        c = (d - 1 - 2 * n) / (d - 1)
        total += c * z**n
    total += z**d
    return total


def g_half_series(omega: float, dmax: int = 180) -> float:
    """Renewal-series evaluation of G_{p=1/2}(omega)."""
    if abs(omega) < 1e-14:
        return 0.0

    z = cmath.exp(1j * omega)
    alpha = 0j
    beta = 0j
    phi = 0j
    diagonal = 0.0

    for d in range(2, dmax + 1):
        probability = (d - 1) * 2.0 ** (-d)
        response = interval_response_half(d, z)
        alpha += probability * response
        beta += probability * response * z ** (-d)
        phi += probability * z ** (-d)
        diagonal += probability * abs(response) ** 2

    # WP06 proves alpha=0 exactly for every unit-circle z.  Retain the general
    # renewal cross term here as an independent numerical check.
    cross = 2.0 * (beta * alpha.conjugate() / (1.0 - phi)).real

    # E[D]=4 and the incident complex-waveform FI rate is p/q=1.
    return 0.25 * (diagonal + cross)


def g_half_closed(omega: float) -> float:
    """WP06 closed form, with the removable DC limit filled explicitly."""
    if abs(omega) < 1e-12:
        return 0.0
    x = 1.0 - math.cos(omega)
    return 1.0 - 1.0 / (2.0 * x) + math.log1p(4.0 * x) / (8.0 * x * x)


def main() -> None:
    exact_nyquist = 3.0 / 4.0 + math.log(3.0) / 16.0

    assert abs(g_half_closed(0.0)) < 1e-14
    assert abs(g_half_closed(math.pi) - exact_nyquist) < 1e-14
    assert abs(g_half_series(math.pi) - exact_nyquist) < 1e-12

    previous = -1.0
    for j in range(1, 257):
        omega = math.pi * j / 256.0
        series = g_half_series(omega)
        closed = g_half_closed(omega)
        assert abs(series - closed) < 2e-10
        assert closed > previous
        previous = closed

    print(f"G(0)  = {g_half_closed(0.0):.15f}")
    print(f"G(pi) = {g_half_closed(math.pi):.15f}")
    print(f"exact = {exact_nyquist:.15f}")
    print("series/closed-form agreement: PASS")
    print("sampled strict monotonicity: PASS")

    out = Path(__file__).with_name("paralyzable_onebin_spectrum_p_half.csv")
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["omega_rad_per_bin", "omega_over_pi", "G_p_half"])
        for j in range(33):
            omega = math.pi * j / 32.0
            writer.writerow([
                f"{omega:.15g}",
                f"{j/32.0:.15g}",
                f"{g_half_closed(omega):.15g}",
            ])

    print(f"wrote {out}")


if __name__ == "__main__":
    main()
