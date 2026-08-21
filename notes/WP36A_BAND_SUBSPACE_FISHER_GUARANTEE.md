# WP36A — Exact Band-Subspace Fisher Guarantee

**Date:** 2026-08-20

## Purpose

Record the strongest operational corollary of WP36. Once `G(omega)` is recognized as the multiplication operator for local weak-waveform Fisher information, a complete frequency band has an exact worst-case and best-case information retention.

---

## Rayleigh quotient

For a scalar weak perturbation `s(t)` with Fourier transform `S(omega)`, WP36 gives

\[
F_{\rm out}[s]
=\frac{\Phi_0}{2\pi}\int G(\omega)|S(\omega)|^2d\omega,
\]

while

\[
F_{\rm in}[s]
=\frac{\Phi_0}{2\pi}\int |S(\omega)|^2d\omega.
\]

Therefore the source-normalized retention is

\[
\boxed{
\rho_G[s]
=\frac{\int G(\omega)|S(\omega)|^2d\omega}
{\int |S(\omega)|^2d\omega}.
}
\]

For spectra supported in a measurable set `E`, this is the Rayleigh quotient of the multiplication operator by `G`, so

\[
\boxed{
\operatorname*{ess\,inf}_{E}G
\le \rho_G[s]\le
\operatorname*{ess\,sup}_{E}G.
}
\]

The two bounds are sharp as infimum/supremum over admissible perturbations. Smooth compactly supported spectra may be concentrated arbitrarily near essential extrema; their inverse Fourier transforms are Schwartz and therefore belong to the manuscript source class `L2 cap L-infinity`.

---

## Universal band guarantee

For the symmetric band `|omega| <= Omega`, preserving at least an absolute Fisher fraction `q` for **every** admissible weak temporal waveform in that band is equivalent to

\[
\boxed{
G(\omega)\ge q
\quad\text{for almost every }|\omega|\le\Omega.
}
\]

This is stronger and more operational than specifying a flat spectral average. It means the detector cannot have a hidden information notch inside the advertised task band.

For square-integrable conditional delay densities,

\[
\int_{-\infty}^{\infty}G(\omega)d\omega
=\pi\mathfrak R_2.
\]

Hence the universal band guarantee implies

\[
\pi\mathfrak R_2
\ge 2\Omega q.
\]

With ordinary-frequency half-band `B = Omega/(2 pi)`, this is

\[
\boxed{
\mathfrak R_2\ge4Bq.
}
\]

Since `mathfrak R_2 <= mathfrak H`, also

\[
\boxed{
\mathfrak H\ge4Bq.
}
\]

Thus the same `4 B q` coefficient that Rev6 obtained as a necessary cost for flat-average retention also has a stronger interpretation:

> it is the necessary timing-resource cost of guaranteeing at least `q` Fisher retention for every weak temporal waveform in an entire band-limited subspace.

This is now part of the Rev7 significance upgrade.
