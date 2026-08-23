#!/usr/bin/env python3
"""Random hostile checks of WP27 approximate-gap boundary synthesis law."""

from __future__ import annotations

import math
import numpy as np


def weighted_norm(X: np.ndarray, rho_plus: np.ndarray) -> float:
    return float(np.trace(X @ rho_plus @ X.conj().T).real)


def run_trial(seed: int) -> None:
    rng = np.random.default_rng(seed)
    d = 10
    r = 5

    energies = np.sort(rng.uniform(0.0, 10.0, d))
    H = np.diag(energies)

    p = np.zeros(d)
    vals = rng.random(r)
    vals /= vals.sum()
    p[:r] = vals
    rho_plus = np.diag([1.0 / x if x > 0 else 0.0 for x in p])

    X = np.zeros((d, d), dtype=complex)
    Y = np.zeros_like(X)
    X[r:, :r] = rng.normal(size=(d - r, r)) + 1j * rng.normal(size=(d - r, r))
    Y[r:, :r] = rng.normal(size=(d - r, r)) + 1j * rng.normal(size=(d - r, r))
    A = X + Y.conj().T

    Zx = X @ rho_plus @ X.conj().T
    Zy = Y @ rho_plus @ Y.conj().T
    extra = rng.normal(size=(d - r, d - r)) + 1j * rng.normal(size=(d - r, d - r))
    S = np.zeros((d, d), dtype=complex)
    S[r:, r:] = 0.1 * extra @ extra.conj().T
    C = Zx + Zy + S

    nu = float(rng.uniform(1.0, 6.0))
    delta = 0.3 * nu

    Xn = np.zeros_like(X)
    Yn = np.zeros_like(Y)
    plus_rows = np.zeros(d, dtype=bool)
    minus_rows = np.zeros(d, dtype=bool)
    for m in range(r, d):
        for n in range(r):
            if abs(energies[m] - energies[n] - nu) < delta:
                Xn[m, n] = X[m, n]
                plus_rows[m] = True
            if abs(energies[m] - energies[n] + nu) < delta:
                Yn[m, n] = Y[m, n]
                minus_rows[m] = True

    Xo = X - Xn
    Yo = Y - Yn

    Jx = weighted_norm(X, rho_plus)
    Jy = weighted_norm(Y, rho_plus)
    Jxn = weighted_norm(Xn, rho_plus)
    Jyn = weighted_norm(Yn, rho_plus)
    Jxo = weighted_norm(Xo, rho_plus)
    Jyo = weighted_norm(Yo, rho_plus)

    Rplus = H @ A - A @ H - nu * A  # hbar=1 units
    Ad = A.conj().T
    Rminus = H @ Ad - Ad @ H + nu * Ad
    eta_plus2 = weighted_norm(Rplus, rho_plus)
    eta_minus2 = weighted_norm(Rminus, rho_plus)

    if Jxo > eta_plus2 / delta**2 + 2e-10:
        raise AssertionError((seed, "plus residual", Jxo, eta_plus2 / delta**2))
    if Jyo > eta_minus2 / delta**2 + 2e-10:
        raise AssertionError((seed, "minus residual", Jyo, eta_minus2 / delta**2))

    Pi_plus = np.diag(plus_rows.astype(float))
    Pi_minus = np.diag(minus_rows.astype(float))
    DTplus = float(np.trace(Pi_plus @ C).real)
    DTminus = float(np.trace(Pi_minus @ C).real)

    if Jxn > DTplus + 2e-10:
        raise AssertionError((seed, "plus curvature", Jxn, DTplus))
    if Jyn > DTminus + 2e-10:
        raise AssertionError((seed, "minus curvature", Jyn, DTminus))

    eps = math.sqrt(eta_plus2) / delta + math.sqrt(eta_minus2) / delta

    # Test at the strongest generic common-record ceiling supplied by the
    # original bilateral Minkowski law. Any actual POVM Fisher trace is <= this.
    F_ceiling = (math.sqrt(Jx) + math.sqrt(Jy)) ** 2
    corrected = max(0.0, math.sqrt(F_ceiling) - eps)
    rhs_amp = math.sqrt(DTplus) + math.sqrt(DTminus)
    if corrected > rhs_amp + 2e-10:
        raise AssertionError((seed, "amplitude law", corrected, rhs_amp))

    lhs_sq = corrected**2
    if lhs_sq > 2.0 * (DTplus + DTminus) + 2e-10:
        raise AssertionError((seed, "bilateral action law"))


def exact_one_sided_check() -> None:
    # Equal-spacing ladder with a rank-deficient support and exact +2 gap.
    d = 6
    r = 3
    energies = np.arange(d, dtype=float)
    H = np.diag(energies)
    p = np.array([0.2, 0.3, 0.5, 0.0, 0.0, 0.0])
    rp = np.diag([1.0 / x if x > 0 else 0.0 for x in p])

    X = np.zeros((d, d), dtype=complex)
    X[2, 0] = 0.7
    X[3, 1] = -0.4j
    X[4, 2] = 0.3 + 0.2j
    A = X
    R = H @ A - A @ H - 2.0 * A
    np.testing.assert_allclose(R, 0.0, atol=1e-13)

    Z = X @ rp @ X.conj().T
    C = Z.copy()
    J = weighted_norm(X, rp)
    np.testing.assert_allclose(np.trace(C).real, J, rtol=0, atol=1e-13)


def main() -> None:
    for seed in range(100):
        run_trial(seed)
    exact_one_sided_check()
    print("WP27 approximate-boundary action validator: PASS")


if __name__ == "__main__":
    main()
