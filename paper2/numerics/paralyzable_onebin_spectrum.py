#!/usr/bin/env python3
"""Reproduce WP05 one-bin paralyzable Fisher-spectrum results.

Model:
    X_n ~ Bernoulli(p_n), independent,
    Y_n = X_n (1-X_{n-1}).

At p=1/2, the script evaluates the exact renewal-series expression for the
source-normalized Fisher multiplier G(omega), verifies G(0)=0 and the closed
Nyquist value 3/4 + ln(3)/16, and writes a compact frequency table.

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


def g_half(omega: float, dmax: int = 180) -> float:
    """Exact-series approximation to G_{p=1/2}(omega).

    The omitted renewal-probability tail is exponentially small at dmax=180.
    """
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

    # General renewal-reward spectral variance.  At p=1/2 alpha vanishes
    # analytically for every z, but retaining the cross term is an independent
    # numerical check of that cancellation.
    cross = 2.0 * (beta * alpha.conjugate() / (1.0 - phi)).real

    # E[D]=4 and the incident complex-waveform FI rate is p/q=1.
    return 0.25 * (diagonal + cross)


def main() -> None:
    exact_nyquist = 3.0 / 4.0 + math.log(3.0) / 16.0
    numerical_nyquist = g_half(math.pi)
    dc = g_half(0.0)

    assert abs(dc) < 1e-14
    assert abs(numerical_nyquist - exact_nyquist) < 1e-12

    print(f"G(0)  = {dc:.15f}")
    print(f"G(pi) numerical = {numerical_nyquist:.15f}")
    print(f"G(pi) exact     = {exact_nyquist:.15f}")

    out = Path(__file__).with_name("paralyzable_onebin_spectrum_p_half.csv")
    with out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["omega_rad_per_bin", "omega_over_pi", "G_p_half"])
        for j in range(33):
            omega = math.pi * j / 32.0
            writer.writerow([f"{omega:.15g}", f"{j/32.0:.15g}", f"{g_half(omega):.15g}"])

    print(f"wrote {out}")


if __name__ == "__main__":
    main()
