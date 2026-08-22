#!/usr/bin/env python3
"""Verify the closed-form truncated-Gaussian single-photon example in Rev7.

This is a manuscript consistency check, not part of the theorem proof.
"""

from __future__ import annotations

import math
import numpy as np


def q(x: np.ndarray, sigma: float = 1.0) -> np.ndarray:
    Z = math.erfc(-1.0 / math.sqrt(2.0))
    pref = math.sqrt(2.0 / math.pi) / (sigma * Z)
    out = pref * np.exp(-((x - sigma) ** 2) / (2.0 * sigma**2))
    return np.where(x >= 0.0, out, 0.0)


def survival_closed(nu: float, sigma: float = 1.0) -> float:
    Z = math.erfc(-1.0 / math.sqrt(2.0))
    return math.erfc((nu - sigma) / (math.sqrt(2.0) * sigma)) / Z


def retention_closed(nu: float, sigma: float = 1.0) -> float:
    Z = math.erfc(-1.0 / math.sqrt(2.0))
    affinity = math.exp(-(nu**2) / (8.0 * sigma**2)) * math.erfc(
        (nu / 2.0 - sigma) / (math.sqrt(2.0) * sigma)
    ) / Z
    return affinity**2


def mean_closed(sigma: float = 1.0) -> float:
    Z = math.erfc(-1.0 / math.sqrt(2.0))
    return sigma * (
        1.0 + math.sqrt(2.0 / math.pi) * math.exp(-0.5) / Z
    )


def main() -> None:
    sigma = 1.0
    x = np.linspace(0.0, 10.0, 1_000_001)
    qx = q(x, sigma)

    norm = np.trapz(qx, x)
    mean_num = np.trapz(x * qx, x)
    assert abs(norm - 1.0) < 2e-10, norm
    assert abs(mean_num - mean_closed(sigma)) < 2e-9, (mean_num, mean_closed())

    for nu in (0.25, 0.5, 1.0, 1.5, 2.0):
        mask = x + nu <= 10.0
        xx = x[mask]
        affinity_num = np.trapz(np.sqrt(q(xx, sigma) * q(xx + nu, sigma)), xx)
        R_num = affinity_num**2
        S_num = np.trapz(q(x[x >= nu], sigma), x[x >= nu])
        R = retention_closed(nu, sigma)
        S = survival_closed(nu, sigma)
        assert abs(R_num - R) < 3e-9, (nu, R_num, R)
        assert abs(S_num - S) < 3e-9, (nu, S_num, S)
        assert R <= S + 1e-14, (nu, R, S)

    R05 = retention_closed(0.5)
    S05 = survival_closed(0.5)
    R10 = retention_closed(1.0)
    S10 = survival_closed(1.0)

    assert abs(S05 - 0.8218539005622801) < 2e-15
    assert abs(R05 - 0.7937545665723014) < 2e-15
    assert abs(R05 / S05 - 0.9658098185446898) < 2e-15
    assert abs(S10 - 0.5942867086725301) < 2e-15
    assert abs(R10 - 0.5260361867382674) < 2e-15
    assert abs(R10 / S10 - 0.8851555639083444) < 2e-15
    assert abs(mean_closed() - 1.2875999709391783) < 2e-15

    print("Rev7 truncated-Gaussian single-photon example PASS")
    print(f"normalization={norm:.12f}")
    print(f"mean excess frequency/sigma={mean_closed():.12f}")
    print(f"nu=0.5 sigma: S={S05:.12f}, R={R05:.12f}, R/S={R05/S05:.12f}")
    print(f"nu=1.0 sigma: S={S10:.12f}, R={R10:.12f}, R/S={R10/S10:.12f}")


if __name__ == "__main__":
    main()
