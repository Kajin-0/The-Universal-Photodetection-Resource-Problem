# WP36A — Exact Band-Subspace Fisher Guarantee

**Date:** 2026-08-20  
**Status:** Proof-hardened for Rev7.

## Purpose

Record the strongest operational corollary of WP36. Once `G(omega)` is recognized as the multiplication operator for local weak-waveform Fisher information, a complete frequency band has an exact worst-case and best-case information retention.

---

## Rayleigh quotient

For a scalar weak perturbation `s(t)` with Plancherel Fourier transform `S(omega)`, WP36 gives

\[
F_{\rm out}[s]
=\frac{\Phi_0}{2\pi}\int G(\omega)|S(\omega)|^2d\omega,
\]

and

\[
F_{\rm in}[s]
=\frac{\Phi_0}{2\pi}\int |S(\omega)|^2d\omega.
\]

Therefore

\[
\boxed{
\rho_G[s]
=\frac{\int G(\omega)|S(\omega)|^2d\omega}
{\int |S(\omega)|^2d\omega}.
}
\]

For spectra supported in a symmetric measurable set `E`, this is the Rayleigh quotient of multiplication by `G`:

\[
\boxed{
\operatorname*{ess\,inf}_{E}G
\le \rho_G[s]\le
\operatorname*{ess\,sup}_{E}G.
}
\]

The bounds are sharp. To approach either essential extremum, choose a symmetric finite-measure subset on which `G` lies within `epsilon` of the extremum and take `S` to be its real-even indicator. Then `S in L1 cap L2`, so its inverse Fourier transform is real, bounded, and square-integrable and is admissible under the Rev7 source class.

---

## Continuity upgrades a physical compact band

Every mark-conditioned characteristic function `H_m` is continuous and obeys `H_m(-omega)=H_m(omega)^*`. Since `|H_m|<=1` and `kappa` is finite, dominated convergence gives

\[
\boxed{G\in C(\mathbb R),\qquad G(-\omega)=G(\omega).}
\]

For the compact symmetric band `[-Omega,Omega]`, essential extrema therefore equal ordinary extrema. The exact worst-case retention is

\[
\boxed{
\inf_{\operatorname{supp}S\subset[-\Omega,\Omega]}
\rho_G[s]
=
\min_{|\omega|\le\Omega}G(\omega).
}
\]

Hence preserving at least an absolute Fisher fraction `q` for **every** admissible weak temporal waveform in that band is equivalent to the pointwise condition

\[
\boxed{
G(\omega)\ge q
\qquad\text{for every }|\omega|\le\Omega.
}
\]

This is stronger and more operational than a flat spectral-average requirement: an advertised information band cannot hide a narrow Fisher-information notch.

---

## Universal band resource cost

For square-integrable conditional delay densities,

\[
\int_{-\infty}^{\infty}G(\omega)d\omega
=\pi\mathfrak R_2.
\]

The pointwise band guarantee gives

\[
\pi\mathfrak R_2
\ge\int_{-\Omega}^{\Omega}G(\omega)d\omega
\ge2\Omega q.
\]

With ordinary-frequency half-band

\[
B=\frac{\Omega}{2\pi},
\]

we obtain

\[
\boxed{
\mathfrak R_2\ge4Bq.
}
\]

Since

\[
\mathfrak R_2\le\mathfrak H,
\]

also

\[
\boxed{
\mathfrak H\ge4Bq.
}
\]

Thus the same `4Bq` coefficient first obtained in Rev6 for flat-average retention has a stronger Rev7 interpretation:

> it is also the necessary timing-resource cost of guaranteeing at least `q` Fisher retention for every admissible weak temporal waveform in a complete band-limited subspace.
