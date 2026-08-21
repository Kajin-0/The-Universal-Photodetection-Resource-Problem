#!/usr/bin/env python3
"""Reproduce the core WP07 continuous paralyzable saturation results.

Dimensionless convention:
    tau = 1,
    lambda = 1,
    rho = lambda*tau = 1,
    r = lambda*exp(-rho) = 1/e.

The script uses only the Python standard library.  It prints

1. the rigorous Fourier-count lower bound at omega*tau = pi;
2. the exact high-frequency plateau 1/e;
3. a method-of-steps numerical evaluation of the exact complete-record
   one-dimensional Fisher integral at omega*tau = pi.

The numerical integration is not part of the proof of the >0.5169 lower bound.
The proof-level formulas are recorded in WP07.
"""

import cmath
import math

R = math.exp(-1.0)


def q_survival(t: float) -> float:
    """Exact delayed-exponential survival q(t)=P(D>t) at rho=tau=1."""
    if t < 0.0:
        return 1.0
    n = int(math.floor(t + 1.0e-12))
    value = 1.0
    for k in range(1, n + 1):
        x = t - k
        if x >= 0.0:
            value += ((-R) ** k) * (x**k) / math.factorial(k)
    return value


def interval_density(t: float) -> float:
    """Baseline registered-event renewal density f_D(t)."""
    if t < 1.0:
        return 0.0
    return R * q_survival(t - 1.0)


def mean_response(omega: float) -> complex:
    """M_1(y) with y=omega in the tau=1 convention."""
    if abs(omega) < 1.0e-15:
        return 0.0j
    return 1.0 - (1.0 - cmath.exp(-1j * omega)) / (1j * omega)


def rigorous_count_lower_bound(omega: float) -> float:
    """Rigorous lower bound from the registered-count Fourier statistic."""
    if abs(omega) < 1.0e-15:
        return 0.0
    m = mean_response(omega)
    denominator = 1.0 - 2.0 * R * math.sin(omega) / omega
    return R * abs(m) ** 2 / denominator


def exact_integral_midpoint(omega: float, h: float = 0.0005, tmax: float = 25.0) -> float:
    """Method-of-steps evaluation of the exact complete-record WP07 integral.

    c'(t) = f_D(t) + i*omega*c(t) - r*exp(i*omega)*c(t-1),
    c(t)=0 for t<1.

    G(omega) = r*|M_1(omega)|^2 * integral |c'(t)|^2/f_D(t) dt.

    A midpoint method is used.  The step h must divide the unit dead time.
    """
    delay_steps = round(1.0 / h)
    if abs(delay_steps * h - 1.0) > 1.0e-12:
        raise ValueError("h must divide tau=1 exactly")

    n_steps = int(round(tmax / h))
    c = [0.0j] * (n_steps + 1)
    phase = cmath.exp(1j * omega)
    integral = 0.0

    for n in range(n_steps):
        t = n * h
        current = c[n]

        delay_index = n - delay_steps
        delayed = 0.0j if delay_index < 0 else c[delay_index]
        f0 = interval_density(t)
        rhs0 = f0 + 1j * omega * current - R * phase * delayed

        midpoint_state = current + 0.5 * h * rhs0
        tm = t + 0.5 * h

        delayed_time = tm - 1.0
        if delayed_time < 0.0:
            delayed_mid = 0.0j
        else:
            j = int(math.floor(delayed_time / h))
            frac = delayed_time / h - j
            delayed_mid = c[j] * (1.0 - frac) + c[j + 1] * frac

        fmid = interval_density(tm)
        rhs_mid = fmid + 1j * omega * midpoint_state - R * phase * delayed_mid
        c[n + 1] = current + h * rhs_mid

        if tm >= 1.0 and fmid > 0.0:
            integral += h * abs(rhs_mid) ** 2 / fmid

    return R * abs(mean_response(omega)) ** 2 * integral


def main() -> None:
    omega = math.pi
    lower = rigorous_count_lower_bound(omega)
    plateau = R

    print("Continuous paralyzable detector at lambda*tau = 1")
    print(f"G(0) = 0 exactly")
    print(f"rigorous G(pi/tau) lower bound = {lower:.12f}")
    print(f"high-frequency plateau = 1/e = {plateau:.12f}")
    print()

    expected_lower = math.exp(-1.0) * (1.0 + 4.0 / math.pi**2)
    assert abs(lower - expected_lower) < 1.0e-14
    assert lower > 0.5
    assert lower > plateau

    for h in (0.002, 0.001, 0.0005, 0.00025):
        g = exact_integral_midpoint(omega, h=h, tmax=25.0)
        print(f"exact-integral numerical G(pi), h={h:g}: {g:.12f}")

    # The second-order method approaches ~0.528142425 as h -> 0.
    fine = exact_integral_midpoint(omega, h=0.00025, tmax=25.0)
    assert abs(fine - 0.528142425) < 3.0e-6


if __name__ == "__main__":
    main()
