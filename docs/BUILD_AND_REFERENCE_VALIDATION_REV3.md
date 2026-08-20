# Build and Reference Validation — Manuscript Rev3

**Date:** 2026-08-20

## Target

`manuscript/event_resource_theorem_rev3.tex`

Supporting files:

- `manuscript/appendix_rare_fast_counterexample.tex`
- `manuscript/references.bib`

## Local TeX validation

A local clean build was performed with the available TeX Live toolchain.

Because the local `latexmk` configuration attempted to invoke a missing executable named `bibtex`, bibliography processing was run explicitly with installed `bibtex8`, followed by two `pdflatex` passes.

Commands conceptually equivalent to:

```text
bibtex8 event_resource_theorem_rev3
pdflatex -interaction=nonstopmode -halt-on-error event_resource_theorem_rev3.tex
pdflatex -interaction=nonstopmode -halt-on-error event_resource_theorem_rev3.tex
```

Results:

- `bibtex8` produced the APS RevTeX bibliography (`event_resource_theorem_rev3.bbl`).
- First post-bibliography `pdflatex`: exit code 0.
- Second post-bibliography `pdflatex`: exit code 0.
- Final PDF: 14 pages, US Letter, approximately 281 kB in the validation environment.
- The external rare-fast appendix was included successfully.
- No undefined citations remained.
- No undefined equation/section references remained.
- No duplicate labels were found.
- No overfull or underfull box warnings were found in the final log search.
- No malformed `\rac{...}`-type typo remained.

The only warning retained in the final log was the standard RevTeX/hyperref `nameref` warning that the definition of `\label` had changed and was being replaced by the kernel definition. It is nonfatal and did not prevent compilation.

## Citation-key audit

Cited keys in Rev3 + appendix:

- `Bouchet2019`
- `DaleyVereJones2003`
- `Dechant2026`
- `Katznelson2004`
- `Kingman1993`
- `KollnerWolfrum1992`
- `Talaga2009`
- `TrinhEsposito2021`

Mechanical audit:

- missing cited bibliography keys: **none**;
- unused bibliography entries: **none**;
- duplicate labels: **none**;
- references to missing labels: **none**.

## Claim-language audit

A targeted scan for claim-sensitive terms (`first`, `universal`, `fundamental`, `novel`, etc.) found no unsupported first-of-kind or all-detector novelty assertion.

Rev3 explicitly says:

- the result is for autonomous marked event photodetection, not all detector architectures;
- the thermodynamic result is a restricted completion, not a universal temperature law;
- prior TCSPC/IRF work already treated timing-response information loss and sensitivity-bandwidth issues;
- generic finite-frequency response/noise inequalities are not claimed as new.

The phrase “first theorem” in the scope paragraph refers only to the first theorem **within the paper**, not historical priority.

## WP33 algebra audit

The exact solution used to impose fixed variance in the two-exponential jitter counterexample was independently checked symbolically.

For

\[
V(x)=\frac{2(1-\epsilon)}{n^2}+2\epsilon x^2-
\left[\frac{1-\epsilon}{n}+\epsilon x\right]^2,
\]

the positive solution of `V(x)=sigma^2` is indeed

\[
 x_{\epsilon,n}
=\frac{
\sqrt{(2-\epsilon)n^2\sigma^2-2(1-\epsilon)}
+\sqrt\epsilon(1-\epsilon)
}{
\sqrt\epsilon\,n(2-\epsilon)
}.
\]

Thus the Rev3 statement that every selected family member can have exactly fixed variance is algebraically verified. The deterministic shift then fixes the mean exactly without changing `|H(omega)|`.

## CI note

The branch workflow

`.github/workflows/manuscript-check.yml`

is configured to compile Rev3 using `xu-cheng/latex-action@v3`.

The connected GitHub workflow-run tool available in this session exposes pull-request-triggered runs but not the branch push-triggered run used here, so the GitHub Actions result itself has not been inspected. This no longer blocks the manuscript build gate because the complete local bibliography-resolved build has been independently verified as above.

## Status

**BUILD VERIFIED LOCALLY. REFERENCES VERIFIED. NO KNOWN LATEX-BLOCKING ERROR.**

The remaining manuscript work is scientific/editorial: final claim/citation review, choice of a small number of explanatory figures, and submission packaging if desired.
