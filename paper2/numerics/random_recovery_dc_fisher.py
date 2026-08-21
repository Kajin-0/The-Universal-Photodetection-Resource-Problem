#!/usr/bin/env python3
"""Numerical calibration for WP13/WP14 generalized Type-II recovery.

Requires NumPy and SciPy.

All examples are scaled to mean recovery E[T]=1 and are evaluated at the common
paralysis maximum lambda=1.  Every recovery law therefore has the same ordinary
mean output curve r(lambda)=lambda*exp(-lambda), but its complete timestamp DC
Fisher information can differ.

The recorded-event renewal density is exact:
    U(t) = F_T(t) * exp[-A(t)]
where A(t)=E[min(T,t)].  For the fractional rate tangent lambda_e=lambda(1+e),
    dot U(t) = U(t) * [1-A(t)]
at lambda=1.

The renewal equations
    U = f + f*U
    dot U = dot f + dot f*U + f*dot U
are solved by trapezoidal Volterra quadrature.  Since U(0)=f(0)=0 for the
families used here, the endpoint terms vanish and the recursion has the simple
form implemented below.

The complete static Fisher retention is
    G(0) = exp(-1) * integral [dot f(t)^2 / f(t)] dt.

This script is validation/calibration; the strict-positive and uniqueness proofs
in WP13/WP14 do not depend on numerical results.
"""

from __future__ import annotations

import csv
import math
from pathlib import Path

import numpy as np
from scipy import special

E_INV = math.exp(-1.0)


def solve_from_U(t: np.ndarray, U: np.ndarray, dU: np.ndarray):
    """Solve renewal and tangent Volterra equations on a uniform grid."""
    h = float(t[1] - t[0])
    n = len(t)
    f = np.zeros(n, dtype=float)
    df = np.zeros(n, dtype=float)

    # U[0]=f[0]=0 for the continuous positive recovery laws considered here.
    for i in range(1, n):
        if i > 1:
            conv = np.dot(f[1:i], U[i - 1 : 0 : -1])
            dconv = (
                np.dot(df[1:i], U[i - 1 : 0 : -1])
                + np.dot(f[1:i], dU[i - 1 : 0 : -1])
            )
        else:
            conv = 0.0
            dconv = 0.0
        f[i] = U[i] - h * conv
        df[i] = dU[i] - h * dconv

    mass = float(np.trapezoid(f, t))
    mean = float(np.trapezoid(t * f, t))
    dmass = float(np.trapezoid(df, t))

    mask = f > 1.0e-14
    integrand = np.zeros_like(f)
    integrand[mask] = df[mask] ** 2 / f[mask]
    I_cycle = float(np.trapezoid(integrand, t))
    G0 = E_INV * I_cycle

    return {
        "f": f,
        "df": df,
        "mass": mass,
        "mean": mean,
        "dmass": dmass,
        "I_cycle": I_cycle,
        "G0": G0,
    }


def gamma_recovery(shape: float, h: float, tmax: float):
    """Mean-one Gamma(shape=k, rate=k) recovery at lambda=1."""
    k = float(shape)
    n = int(round(tmax / h)) + 1
    t = np.arange(n, dtype=float) * h

    # F_T(t)=P(k,k t); survival=Q(k,k t).
    F = special.gammainc(k, k * t)
    survival = special.gammaincc(k, k * t)

    # For mean-one gamma:
    # E[T 1_{T<=t}] = P(k+1,k t), hence
    # A(t)=E[min(T,t)] = P(k+1,k t) + t Q(k,k t).
    A = special.gammainc(k + 1.0, k * t) + t * survival

    U = F * np.exp(-A)
    dU = U * (1.0 - A)
    return t, U, dU


def exponential_convergence(outdir: Path):
    rows = []
    for h in (0.01, 0.005, 0.0025, 0.00125):
        t, U, dU = gamma_recovery(shape=1.0, h=h, tmax=35.0)
        ans = solve_from_U(t, U, dU)
        rows.append(
            {
                "h": h,
                "mass": ans["mass"],
                "mean_interval": ans["mean"],
                "score_mass": ans["dmass"],
                "I_cycle": ans["I_cycle"],
                "G0": ans["G0"],
            }
        )

    path = outdir / "exponential_recovery_dc_fisher_convergence.csv"
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    fine = rows[-1]
    assert abs(fine["mass"] - 1.0) < 5.0e-6
    assert abs(fine["mean_interval"] - math.e) < 2.0e-5
    assert abs(fine["G0"] - 0.06915579) < 5.0e-7

    return rows


def gamma_family(outdir: Path):
    rows = []
    for k in (0.5, 1, 2, 4, 8, 16, 32, 64):
        t, U, dU = gamma_recovery(shape=float(k), h=0.005, tmax=35.0)
        ans = solve_from_U(t, U, dU)
        rows.append(
            {
                "shape_k": k,
                "cv": 1.0 / math.sqrt(k),
                "mass": ans["mass"],
                "mean_interval": ans["mean"],
                "I_cycle": ans["I_cycle"],
                "G0": ans["G0"],
            }
        )

    path = outdir / "gamma_recovery_dc_fisher.csv"
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

    # This monotonicity is an empirical property of this gamma family only.
    gvals = [row["G0"] for row in rows]
    assert all(gvals[i] > gvals[i + 1] for i in range(len(gvals) - 1))
    return rows


def main() -> None:
    outdir = Path(__file__).resolve().parent

    conv = exponential_convergence(outdir)
    print("Exponential recovery convergence at lambda=mu=1:")
    for row in conv:
        print(
            f"  h={row['h']:<8g} G0={row['G0']:.10f} "
            f"mass={row['mass']:.10f} meanD={row['mean_interval']:.10f}"
        )

    print("\nMean-one gamma recovery family at lambda=1:")
    for row in gamma_family(outdir):
        print(
            f"  k={row['shape_k']:<4} CV={row['cv']:.5f} "
            f"G0={row['G0']:.10f}"
        )


if __name__ == "__main__":
    main()
