# Manuscript Rev4 Integration Audit

**Date:** 2026-08-20

## Purpose
Record the exact publication-state transition from scientifically audited Rev3 to the deterministic Rev4 candidate without overstating compile status.

## Authoritative base

`manuscript/event_resource_theorem_rev3.tex` remains the fully reconstructed and line-by-line scientifically audited base manuscript.

Its central constants, source normalization, Parseval factor, hazard inequality, exact fixed-mean/fixed-variance counterexample, clock no-go, thermodynamic bridge, and rare-fast appendix have all survived the existing theorem/proof audits.

## Deterministic Rev4 generation

`manuscript/apply_rev4.py` reads Rev3 and generates `event_resource_theorem_rev4.tex` without modifying Rev3.

The generator is assertion-based: every replacement anchor must occur exactly once or generation raises an error.

Rev4 adds only:

1. the packages required for theorem figures (`graphicx`, `tikz`, `pgfplots`);
2. `figure_resource_hierarchy.tex` after the Introduction scope statement;
3. the WP34 inverse timing-resource corollary;
4. `figure_jitter_no_go.tex` after the exact WP33 fixed-moment no-go;
5. one Discussion sentence stating the flat-band inverse cost.

No underlying theorem is replaced by the Rev4 integration.

## WP34 inserted corollary

For a flat source-information task on `|omega|<=Omega`, define ordinary-frequency half-band

\[
B=\frac{\Omega}{2\pi}.
\]

If absolute average source-normalized transfer satisfies

\[
\bar\eta_I(\Omega)\ge q,
\]

then feasibility requires `q<=eta` and

\[
\boxed{\mathfrak R_2\ge4Bq,\qquad \mathfrak H\ge4Bq.}
\]

For a uniform markwise hazard ceiling `Lambda(m)<=Lambda`,

\[
\boxed{\Lambda\ge\frac{4Bq}{\eta}.}
\]

If `q=r eta` is retention relative to captured DC information,

\[
\boxed{\Lambda\ge4Br.}
\]

These are algebraic inversions of the already-proved WP32/WP25 upper bounds. No new physical assumption is introduced.

## Figure audit

### Resource hierarchy

`manuscript/figure_resource_hierarchy.tex`

The final version intentionally contains only the three intrinsic event-channel timing layers:

- atomic timing mass;
- collision resource `mathfrak R_2`;
- local hazard capacity `mathfrak H`.

The earlier clock/control box was removed because it competed visually with the intrinsic hierarchy and is already a separate theorem/scope boundary.

The final hierarchy figure was compiled locally with `pdflatex` in a minimal RevTeX/TikZ document. Visual inspection found no overlaps or clipping, and the compile produced no overfull/underfull-box warnings.

### Exact jitter no-go

`manuscript/figure_jitter_no_go.tex`

The plotted data correspond to the exact WP33 family at fixed mean `mu0=2 sigma` and exact variance `sigma^2`, for representative `(epsilon,n sigma)` values `(0.20,50)`, `(0.05,200)`, and `(0.01,1000)`.

The deterministic mean-fixing shift changes only Fourier phase and therefore leaves `|H|^2` unchanged.

The CSV values were checked against the exact WP33 formula. Plot markers were removed to avoid visual clutter. The final plot was compiled locally with `pdflatex`; visual inspection found no clipping/overlap and no layout warnings.

## Generator audit

`apply_rev4.py` passes Python syntax compilation. Its five exact replacement anchors are all present in the reconstructed Rev3 source:

1. package insertion anchor;
2. Introduction-scope figure anchor;
3. post-hazard inverse-cost anchor;
4. post-WP33 figure anchor;
5. Discussion resource-cost anchor.

Thus the deterministic transformation is structurally consistent with current Rev3.

## CI status

`.github/workflows/manuscript-check.yml` now:

1. checks out the branch;
2. runs `python manuscript/apply_rev4.py`;
3. compiles generated `event_resource_theorem_rev4.tex` with `xu-cheng/latex-action@v3`;
4. uploads the generated TeX and PDF as artifacts.

A temporary attempt to make CI self-report success through Issue #12 / branch persistence was removed. Connector-authored branch commits in this session have not produced an observable Actions result through the available connector interfaces.

Therefore:

**DO NOT claim that the complete Rev4 manuscript has a verified successful GitHub Actions compile yet.**

What is verified locally:

- figure TeX compilation;
- figure layout;
- generator Python syntax;
- generator anchors against Rev3;
- the Rev3 theorem/proof layer.

## Publication posture

Rev4 is the preferred next manuscript candidate because it adds the operational inverse theorem and two high-information figures without expanding scope.

Do not open new HgCdTe, non-Poisson, analog-detector, or quantum-pointer research branches merely to improve this manuscript. The next publication work is mechanical full-build verification and final claim/citation review.

## Status

**REV3 SCIENTIFIC BASE: VERIFIED**

**REV4 DETERMINISTIC INTEGRATION: VERIFIED AT GENERATOR/FIGURE LEVEL**

**REV4 FULL LATEX BUILD: NOT YET OBSERVED**
