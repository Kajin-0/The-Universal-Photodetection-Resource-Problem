#!/usr/bin/env python3
"""Independent Volterra solver for WP07 continuous paralyzable Fisher spectrum.

Dimensionless saturation point: lambda=tau=1.

The baseline next-recorded-event interval density k0 and its first-order
complex Fourier-mode derivative k1 obey the causal Volterra equations in WP07.
The complete source-normalized complex-mode Fisher multiplier is

    G(omega) = exp(-1) * integral_1^infty |k1(d)|^2/k0(d) dd.

This implementation uses only the Python standard library and trapezoidal
quadrature with the v=0 implicit term solved algebraically. It is intended as
an independent numerical validation, not as part of the analytic proof.
"""

import cmath
import csv
import math
from pathlib import Path


def mode_kernel(v: float, omega: float) -> complex:
    """h_omega(v) from the first-order exponential waiting-time density."""
    if abs(omega) < 1e-12:
        return 1.0 - v
    z = cmath.exp(1j * omega * v)
    return z - (z - 1.0) / (1j * omega)


def solve(omega: float, step: float = 0.005, dmax: float = 18.0):
    nmax = int(round(dmax / step))
    memory = int(round(1.0 / step))
    assert abs(memory * step - 1.0) < 1e-12

    k0 = [0.0] * (nmax + 1)
    k1 = [0j] * (nmax + 1)

    expv = [math.exp(-j * step) for j in range(memory + 1)]
    phase = [cmath.exp(1j * omega * j * step) for j in range(memory + 1)]
    hvals = [mode_kernel(j * step, omega) for j in range(memory + 1)]

    # Trapezoid endpoint v=0 contributes (step/2)*k(d) to each equation.
    implicit_denominator = 1.0 - step / 2.0

    for n in range(1, nmax + 1):
        d = n * step
        jmax = min(memory, n)

        source0 = math.exp(-d) if d > 1.0 + 1e-12 else 0.0
        accum0 = 0.0
        for j in range(1, jmax + 1):
            weight = 0.5 if j == jmax else 1.0
            accum0 += weight * expv[j] * k0[n - j]
        k0[n] = (source0 + step * accum0) / implicit_denominator

        source1 = (
            math.exp(-d) * mode_kernel(d, omega)
            if d > 1.0 + 1e-12
            else 0j
        )
        accum1 = 0j
        for j in range(1, jmax + 1):
            weight = 0.5 if j == jmax else 1.0
            accum1 += weight * expv[j] * (
                hvals[j] * k0[n - j] + phase[j] * k1[n - j]
            )

        # At v=0, h(0)=phase(0)=1, so the endpoint contains k0[n]+k1[n].
        k1[n] = (
            source1 + (step / 2.0) * k0[n] + step * accum1
        ) / implicit_denominator

    start = memory
    mass = 0.0
    fisher_integral = 0.0
    for n in range(start, nmax + 1):
        weight = 0.5 if n in (start, nmax) else 1.0
        mass += weight * k0[n]
        if k0[n] > 0.0:
            fisher_integral += weight * abs(k1[n]) ** 2 / k0[n]

    mass *= step
    fisher_integral *= step
    G = math.exp(-1.0) * fisher_integral
    return G, mass


def lower_bound_at_pi() -> float:
    return math.exp(-1.0) * (1.0 + 4.0 / math.pi**2)


def main() -> None:
    print("Continuous paralyzable Type-II exact-spectrum Volterra check")
    print("lambda=tau=1 (rho=1)")
    print(f"rigorous L_1(pi) = {lower_bound_at_pi():.12f}")

    convergence = []
    for step in (0.02, 0.01, 0.005, 0.0025):
        G, mass = solve(math.pi, step=step)
        convergence.append((step, G, mass))
        print(f"h={step:.4f}: G(pi)={G:.12f}, interval mass={mass:.12f}")

    # Linear-in-h Richardson estimate is adequate to demonstrate convergence
    # and agrees with a quadratic fit to the same sequence to ~1e-6.
    h1, g1, _ = convergence[-2]
    h2, g2, _ = convergence[-1]
    extrapolated = g2 + (g2 - g1) * h2 / (h1 - h2)
    print(f"first-order h->0 extrapolation: G(pi) ~ {extrapolated:.12f}")
    assert extrapolated > lower_bound_at_pi()
    assert 0.527 < extrapolated < 0.529

    conv_path = Path(__file__).with_name(
        "continuous_paralyzable_volterra_convergence.csv"
    )
    with conv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["step", "G_pi", "interval_density_mass"])
        for row in convergence:
            writer.writerow([f"{x:.15g}" for x in row])
    print(f"wrote {conv_path}")

    # Coarser spectrum snapshot used only to verify qualitative shape.
    spectrum_path = Path(__file__).with_name(
        "continuous_paralyzable_volterra_spectrum_snapshot.csv"
    )
    frequencies = (0.5, 1.0, math.pi, 3.325, 5.0, 10.0, 20.0, 30.0, 50.0)
    with spectrum_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["omega_tau", "G_step_0p005", "interval_density_mass"])
        for omega in frequencies:
            G, mass = solve(omega, step=0.005)
            writer.writerow([f"{omega:.15g}", f"{G:.15g}", f"{mass:.15g}"])
            print(f"omega*tau={omega:.6g}: G~{G:.9f}")
    print(f"wrote {spectrum_path}")


if __name__ == "__main__":
    main()
