#!/usr/bin/env python3
"""Reproduce the Rev10 literature-IRF worked example using only stdlib.

Input points are an approximate graphical digitization of the normalized
DJ-SPAD and MCP traces in Fig. 3 of Spinelli et al., IEEE JQE 34, 817 (1998),
DOI 10.1109/3.668769. The plotted ordinate is logarithmic. B_FI is invariant
to arbitrary vertical normalization, so relative counts are sufficient.

This script does not claim access to the authors' raw event data. The result
is a plot-digitization estimate intended only as an applied illustration.
"""
from pathlib import Path
import csv
import math

CSV = Path(__file__).with_name('spinelli1998_fig3_digitized_rev10.csv')
FWHM_PS = {'DJ-SPAD': 35.0, 'MCP': 25.0}
EXPECTED_GHZ = {'DJ-SPAD': 9.160, 'MCP': 5.977}

traces = {name: [] for name in FWHM_PS}
with CSV.open(newline='', encoding='utf-8') as fh:
    for row in csv.DictReader(fh):
        traces[row['device']].append(
            (float(row['time_ps']) * 1e-12, 10.0 ** float(row['log10_relative_counts']))
        )


def trapz(x, y):
    return sum((x[i + 1] - x[i]) * (y[i + 1] + y[i]) * 0.5 for i in range(len(x) - 1))


def bfi_from_trace(points):
    points = sorted(points)
    t = [p[0] for p in points]
    y = [p[1] for p in points]
    area = trapz(t, y)
    area2 = trapz(t, [v * v for v in y])
    return 0.5 * area2 / (area * area)


def gaussian_bfi_from_fwhm(fwhm_ps):
    sigma = fwhm_ps * 1e-12 / (2.0 * math.sqrt(2.0 * math.log(2.0)))
    return 1.0 / (4.0 * math.sqrt(math.pi) * sigma)


results = {}
for device in ('DJ-SPAD', 'MCP'):
    bfi = bfi_from_trace(traces[device])
    bfi_gauss = gaussian_bfi_from_fwhm(FWHM_PS[device])
    results[device] = bfi
    print(f'{device}:')
    print(f'  reported FWHM = {FWHM_PS[device]:.1f} ps')
    print(f'  figure-digitized B_FI = {bfi/1e9:.3f} GHz')
    print(f'  Gaussian-from-FWHM B_FI = {bfi_gauss/1e9:.3f} GHz')
    print(f'  digitized/Gaussian-FWHM ratio = {bfi/bfi_gauss:.3f}')
    assert abs(bfi / 1e9 - EXPECTED_GHZ[device]) < 0.001

assert FWHM_PS['MCP'] < FWHM_PS['DJ-SPAD']
assert results['DJ-SPAD'] > results['MCP']
print(f"Ranking reversal verified: DJ-SPAD/MCP B_FI = {results['DJ-SPAD']/results['MCP']:.3f}")
