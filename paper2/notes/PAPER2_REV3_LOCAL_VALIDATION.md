# Paper 2 Rev3 — Local Mechanical and Visual Validation

**Date:** 2026-08-21

## Scope

This note records a reproducible local validation of the generated Paper-2 Rev3 manuscript. It does **not** claim that the GitHub Actions push-triggered job was inspected; the available connector did not expose a reliable branch-run listing in this session.

Current manuscript title:

> **Fisher Spectra and Information Singularities in Photodetectors with Memory**

## Revision chain

1. `fisher_spectra_memory_photodetectors_rev1.tex` — first complete science draft.
2. `apply_rev2_science_fix.py` — fixes Greek `\nu_s` versus intended Latin `u_s`, with assertions guarding the `G(omega)` / `G_cyc` / `G_DC` distinctions and WP07 spectral statement.
3. `apply_rev3_mechanical_polish.py` — hides hyperlink boxes, removes internal drafting language, and adds theorem-grade counting-process likelihood references.
4. `paper2_refs.bib` — includes the new Andersen–Borgan–Gill–Keiding and Jacobsen counting-process/point-process references.

The repository CI workflow now generates Rev2 then Rev3 and compiles Rev3.

## Local compilation

A clean local compilation was performed from the corrected Rev3 source with `latexmk`/`pdfLaTeX`. The container's `/usr/bin/bibtex` alternative was broken, so a local PATH shim to the installed `bibtex8` executable was used. This is an environment workaround, not a manuscript source change.

Result:

- **build succeeded**;
- **19 pages**;
- letter page size, 612 x 792 pt;
- all citations resolved;
- all cross-references resolved;
- no `Overfull \hbox` or `Overfull \vbox` warnings;
- no underfull box warnings;
- only remaining warning: benign `Package nameref Warning: The definition of \label has changed!`.

## Local hashes

Generated Rev3 source SHA-256:

`cca61b4182f52debabf7a68d1e6db1b83e7c75586e9fa9b88b236177f2ac2306`

Generated Rev3 PDF SHA-256:

`67efeee778119ffd946b07502b72cee316785a5bb8d565a4cb6f4e190736fdc4`

Local bibliography used for this build SHA-256:

`e4270610770176382cebc3383e5d43520ba40d7936f85b8436afeaee56b18595`

The bibliography hash includes the two new book references added for the stopped counting-process likelihood discussion.

## Visual inspection

The 19-page PDF was rendered at 150 dpi and inspected as a full contact sheet.

Observed:

- no clipped text;
- no equation/text overlaps;
- no margin overflow;
- no broken glyphs;
- no black boxes;
- hyperlink boxes are removed in Rev3;
- theorem/equation typography is consistent;
- bibliography renders normally;
- the preprint title/abstract pagination is mechanically clean.

The four intentionally temporary figure placeholders render cleanly but remain the largest obstacle to a publication-quality draft.

## Static cleanup completed in Rev3

Rev3 removes two internal drafting phrases that survived Rev1:

- `Rev1 leaves the final plotting input...`;
- `A final manuscript revision should attach...`.

It replaces the latter with explicit standard references:

- P. K. Andersen, Ø. Borgan, R. D. Gill, and N. Keiding, *Statistical Models Based on Counting Processes* (Springer, 1993), DOI `10.1007/978-1-4612-4348-9`;
- M. Jacobsen, *Point Process Theory and Applications: Marked Point and Piecewise Deterministic Processes* (Birkhäuser, 2006), DOI `10.1007/0-8176-4463-6`.

## Remaining mechanical/publication work

1. Replace Figure 1 placeholder with a trajectory-channel versus saturation-curve conceptual diagram.
2. Replace Figure 2 placeholder with the validated deterministic Type-II exact spectrum / analytic lower-bound plot.
3. Replace Figure 3 placeholder with the shared saturation-curve / deterministic-versus-random static-FI comparison.
4. Replace Figure 4 placeholder with the exact mean/variance-matched recovery-law counterexample.
5. Rebuild and re-render after each figure insertion.
6. After final figures, perform a manuscript-level hostile review of proof handoffs, novelty language, significance, and exposition.

## Verification boundary

Rev3 is now **locally build-verified and visually inspected**.

It is **not yet GitHub-Actions-run-verified** because the session did not expose the branch push workflow run through the available connector. Do not conflate those states.
