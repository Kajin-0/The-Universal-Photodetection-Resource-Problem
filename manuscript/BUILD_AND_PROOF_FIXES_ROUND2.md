# Manuscript Build and Proof Fixes — Round 2

**Date:** 2026-08-20

This file records exact manuscript edits found during the post-draft hostile audit. It exists so the large LaTeX source does not need to be reconstructed through a truncated connector response.

## Required build fixes

1. In `event_resource_theorem_draft.tex`, in the uniform-exponential tightness calculation, replace

```tex
=rac{\Lambda}{\Omega}\tan^{-1}\left(\frac{\Omega}{\Lambda}\right)
```

with

```tex
=\frac{\Lambda}{\Omega}\tan^{-1}\left(\frac{\Omega}{\Lambda}\right)
```

This is a typographical LaTeX error only; the theorem audit independently verified the coefficient.

2. Include the self-contained thermodynamic rare-fast appendix before the bibliography, e.g.

```tex
\appendix
\input{appendix_rare_fast_counterexample}
\bibliography{references}
```

and remove any duplicate appendix heading if the included file already supplies one.

## Required theorem-scope clarification

In the thermodynamic gateway section, the statement

```tex
D\mid M=T_1+Y_M
```

requires the accessible downstream mark `M` not to contain an independent record of the hidden gateway dwell time `T_1`. More precisely, conditioned on the exit route and subsequent autonomous dynamics, `T_1` must remain independent of the downstream mark/delay. If the detector exposes `T_1` itself as an accessible timing mark, that constitutes an additional pre-primary timing record and must be handled by the general WP32 marked-kernel resource accounting rather than the WP29 gateway corollary.

## Citation placement

Add direct citations in the theorem sections, not only in the Introduction:

- Poisson marking/displacement theorem: cite `Kingman1993` and/or `DaleyVereJones2003` in the proof of the exact marked-event transfer theorem.
- Wiener atomic theorem / Fourier-Stieltjes result: cite `Katznelson2004` at the statement invoking Wiener theory.
- Dechant 2026 should remain only contextual to finite-frequency response/noise bounds; do not present it as support for the WP25/WP32 timing theorem.

## Source-spectrum scope

Immediately before the arbitrary-spectrum concentration theorem, state that `w(omega)` is an absolutely continuous normalized spectral-FI density. Discrete line spectra require the corresponding measure-theoretic concentration functional and are outside the first manuscript's stated theorem.

## Scientific status

These corrections do not change any proved constants or conclusions. Round-1 theorem audit found the source FI normalization, marked-kernel formula, Parseval factor, hazard inequality, Wiener residual, jitter counterexample, clock no-go, thermodynamic prefactor, and rare-fast construction internally consistent.
