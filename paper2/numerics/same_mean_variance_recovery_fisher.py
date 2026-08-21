#!/usr/bin/env python3
"""Same-mean/same-variance Type-II recovery counterexample.

This script supports WP19.  Two discrete recovery laws have exactly

    E[T] = 1,
    Var(T) = 1/4,
    CV(T) = 1/2,

so at lambda=1 they share the same conventional Type-II mean response
r(lambda)=lambda*exp(-lambda).  They nevertheless have different complete
registered-timestamp statistics and numerically different complete static Fisher
retention.

Law A:
    P(T=1/2)=1/2, P(T=3/2)=1/2.

Law B:
    P(T=1/4)=2/9, P(T=1)=5/9, P(T=7/4)=2/9.

The exact analytic short-cycle witness in WP19 does not depend on this numerical
solver.  The solver is only a full-interval-FI calibration.

For lambda=1, the classical registered-event renewal density is

    U(t) = F_T(t) * exp[-A(t)],
    A(t) = E[min(T,t)],

and the fractional-rate derivative is

    dot U(t) = U(t) * [1-A(t)].

The renewal equations are discretized on a uniform grid:

    U = f + h f*U,
    dot U = dot f + h dot f*U + h f*dot U.

As formal power series this gives

    f     = U / (1+hU),
    dot f = dot U / (1+hU)^2.

The reciprocal power series is computed by Newton iteration with FFT
convolutions, allowing fine grids efficiently.  The resulting discretization is
identical to the direct causal recurrence used in random_recovery_dc_fisher.py;
the FFT form has been cross-checked against that recurrence and against the
stored exponential-recovery benchmark.
"""

from __future__ import annotations

import csv
import math
from pathlib import Path

import numpy as np
from scipy.signal import fftconvolve

E_INV = math.exp(-1.0)

LAWS = {
    "A_two_point": (
        np.array([0.5, 1.5], dtype=float),
        np.array([0.5, 0.5], dtype=float),
    ),
    "B_three_point": (
        np.array([0.25, 1.0, 1.75], dtype=float),
        np.array([2.0 / 9.0, 5.0 / 9.0, 2.0 / 9.0], dtype=float),
    ),
}


def recovery_moments(atoms: np.ndarray, probs: np.ndarray):
    mean = float(np.dot(atoms, probs))
    var = float(np.dot((atoms - mean) ** 2, probs))
    return mean, var


def series_inverse(a: np.ndarray, n: int) -> np.ndarray:
    """First n coefficients of 1/a(z), with a[0] != 0."""
    r = np.array([1.0 / a[0]], dtype=float)
    m = 1
    while m < n:
        m2 = min(2 * m, n)
        ar = fftconvolve(a[:m2], r)[:m2]
        correction = np.zeros(m2, dtype=float)
        correction[0] = 2.0
        correction[: len(ar)] -= ar
        r = fftconvolve(r, correction)[:m2]
        m = m2
    return r[:n]


def renewal_density_from_discrete_recovery(
    atoms: np.ndarray,
    probs: np.ndarray,
    h: float,
    tmax: float,
):
    n = int(round(tmax / h)) + 1
    t = np.arange(n, dtype=float) * h

    F = np.zeros(n, dtype=float)
    A = np.zeros(n, dtype=float)
    for atom, prob in zip(atoms, probs):
        F += prob * (t >= atom)
        A += prob * np.minimum(atom, t)

    U = F * np.exp(-A)
    dU = U * (1.0 - A)
    return t, U, dU


def solve_interval_fisher(t: np.ndarray, U: np.ndarray, dU: np.ndarray):
    h = float(t[1] - t[0])
    n = len(t)

    denominator = np.zeros(n, dtype=float)
    denominator[0] = 1.0 + h * U[0]
    denominator[1:] = h * U[1:]

    inv = series_inverse(denominator, n)
    f = fftconvolve(U, inv)[:n]
    inv2 = fftconvolve(inv, inv)[:n]
    df = fftconvolve(dU, inv2)[:n]

    mass = float(np.trapezoid(f, t))
    mean_interval = float(np.trapezoid(t * f, t))
    score_mass = float(np.trapezoid(df, t))

    mask = f > 1.0e-13
    integrand = np.zeros_like(f)
    integrand[mask] = df[mask] ** 2 / f[mask]
    I_cycle = float(np.trapezoid(integrand, t))
    Gdc = E_INV * I_cycle

    return {
        "mass": mass,
        "mean_interval": mean_interval,
        "score_mass": score_mass,
        "I_cycle": I_cycle,
        "Gdc": Gdc,
    }


def exact_short_cycle_witness():
    """Exact binary statistic for Law B at delta=2/5.

    Law A has minimum possible interval 1/2, so P_A(D<=2/5)=0 exactly.

    Law B has minimum recovery 1/4.  For 1/4 <= t <= 2/5 < 1/2,
    a second registered renewal cannot occur, hence f_D(t)=U(t).  On this
    interval F=2/9 and A(t)=1/18+(7/9)t.  Therefore for general lambda

        p_B(lambda)=P(D<=2/5)
          =(2/7)[exp(-lambda/4)-exp(-11 lambda/30)].

    The derivative below is with respect to fractional rate epsilon in
    lambda_epsilon=lambda(1+epsilon), evaluated at lambda=1.
    """
    p = (2.0 / 7.0) * (math.exp(-1.0 / 4.0) - math.exp(-11.0 / 30.0))
    dp = (2.0 / 7.0) * (
        -(1.0 / 4.0) * math.exp(-1.0 / 4.0)
        + (11.0 / 30.0) * math.exp(-11.0 / 30.0)
    )
    I_binary = dp * dp / (p * (1.0 - p))
    G_binary_rate = E_INV * I_binary
    return p, dp, I_binary, G_binary_rate


def pair_correlation_at_three_quarters(atoms, probs):
    t = 0.75
    F = float(sum(p for a, p in zip(atoms, probs) if a <= t))
    R = float(sum(p * max(a - t, 0.0) for a, p in zip(atoms, probs)))
    g2 = F * math.exp(R)  # lambda=1
    dg2 = g2 * R          # fractional-rate derivative at lambda=1
    return F, R, g2, dg2


def main() -> None:
    outdir = Path(__file__).resolve().parent

    for name, (atoms, probs) in LAWS.items():
        mean, var = recovery_moments(atoms, probs)
        assert abs(mean - 1.0) < 1.0e-14, (name, mean)
        assert abs(var - 0.25) < 1.0e-14, (name, var)

    p, dp, Ibin, Gbin = exact_short_cycle_witness()
    print("Exact short-cycle witness at delta=2/5:")
    print("  Law A: P(D<=2/5)=0 exactly, binary FI=0")
    print(f"  Law B: p={p:.12f}, dp={dp:.12f}, I_cycle={Ibin:.12f}, normalized-rate witness={Gbin:.12f}")

    print("\nPair correlation at t=3/4, lambda=1:")
    for name, (atoms, probs) in LAWS.items():
        F, R, g2, dg2 = pair_correlation_at_three_quarters(atoms, probs)
        print(f"  {name}: F={F:.12f}, R={R:.12f}, g2={g2:.12f}, dot_g2={dg2:.12f}")

    rows = []
    for h in (0.01, 0.005, 0.0025, 0.00125, 0.000625, 0.0003125):
        for name, (atoms, probs) in LAWS.items():
            t, U, dU = renewal_density_from_discrete_recovery(
                atoms, probs, h=h, tmax=35.0
            )
            ans = solve_interval_fisher(t, U, dU)
            rows.append(
                {
                    "h": h,
                    "law": name,
                    "mass": ans["mass"],
                    "mean_interval": ans["mean_interval"],
                    "score_mass": ans["score_mass"],
                    "I_cycle": ans["I_cycle"],
                    "Gdc": ans["Gdc"],
                }
            )

    path = outdir / "same_mean_variance_recovery_fisher.csv"
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    print("\nFull interval-FI convergence:")
    for row in rows:
        print(
            f"  h={row['h']:<9g} {row['law']:<14s} "
            f"Gdc={row['Gdc']:.12f} mass={row['mass']:.12f} "
            f"meanD={row['mean_interval']:.12f}"
        )

    fine_A = next(
        row for row in rows
        if row["h"] == 0.0003125 and row["law"] == "A_two_point"
    )
    fine_B = next(
        row for row in rows
        if row["h"] == 0.0003125 and row["law"] == "B_three_point"
    )

    assert abs(fine_A["mass"] - 1.0) < 2.0e-10
    assert abs(fine_B["mass"] - 1.0) < 2.0e-10
    assert abs(fine_A["mean_interval"] - math.e) < 2.0e-8
    assert abs(fine_B["mean_interval"] - math.e) < 2.0e-8
    assert fine_B["Gdc"] / fine_A["Gdc"] > 1.08


if __name__ == "__main__":
    main()
