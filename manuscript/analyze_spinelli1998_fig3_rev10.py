#!/usr/bin/env python3
"""Reproduce the Rev10 literature-IRF worked example.

Input points are an approximate graphical digitization of the normalized
DJ-SPAD and MCP traces in Fig. 3 of Spinelli et al., IEEE JQE 34, 817 (1998),
DOI 10.1109/3.668769. The plotted ordinate is logarithmic. B_FI is invariant
to arbitrary vertical normalization, so relative counts are sufficient.

This script does not claim access to the authors' raw event data. The result
is a plot-digitization estimate intended only as an applied illustration.
"""
from pathlib import Path
import math
import numpy as np
import pandas as pd

CSV = Path(__file__).with_name('spinelli1998_fig3_digitized_rev10.csv')
df = pd.read_csv(CSV)

FWHM_PS = {'DJ-SPAD': 35.0, 'MCP': 25.0}


def bfi_from_trace(g):
    t = g['time_ps'].to_numpy(float) * 1e-12
    y = 10.0 ** g['log10_relative_counts'].to_numpy(float)
    order = np.argsort(t)
    t, y = t[order], y[order]
    area = np.trapezoid(y, t)
    area2 = np.trapezoid(y * y, t)
    return 0.5 * area2 / (area * area)


def gaussian_bfi_from_fwhm(fwhm_ps):
    sigma = fwhm_ps * 1e-12 / (2.0 * math.sqrt(2.0 * math.log(2.0)))
    return 1.0 / (4.0 * math.sqrt(math.pi) * sigma)


for device in ('DJ-SPAD', 'MCP'):
    g = df[df.device == device]
    bfi = bfi_from_trace(g)
    bfi_gauss = gaussian_bfi_from_fwhm(FWHM_PS[device])
    print(f'{device}:')
    print(f'  reported FWHM = {FWHM_PS[device]:.1f} ps')
    print(f'  figure-digitized B_FI = {bfi/1e9:.3f} GHz')
    print(f'  Gaussian-from-FWHM B_FI = {bfi_gauss/1e9:.3f} GHz')
    print(f'  digitized/Gaussian-FWHM ratio = {bfi/bfi_gauss:.3f}')
