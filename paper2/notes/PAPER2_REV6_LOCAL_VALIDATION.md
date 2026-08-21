# Paper 2 Rev6 — Local build and visual validation

**Date:** 2026-08-21

## Status

Generated Rev6 is the current frozen Paper-2 science draft after the manuscript-level hostile review in WP28.

Title:

> **Fisher Spectra and Information Singularities in Photodetectors with Memory**

## Revision chain

1. Rev1 — first complete science draft.
2. Rev2 — `nu_s` / `u_s` notation repair with theorem-invariant assertions.
3. Rev3 — mechanical polish, hidden hyperlinks, removal of internal drafting text, stopped-counting-process citations.
4. Rev4 — publication figures replace all placeholders; figure overflow and annotation issues repaired.
5. Rev5 — hostile-review proof/exposition hardening; `L2` extension clarified, Volterra equations made self-contained, stationary-window domination stated, internal repository wording removed.
6. Rev6 — explicit classical queue-output identifiability positioning using Daley (1976).

The repository's dedicated read-only Paper-2 workflow now generates through Rev6 and compiles Rev6. Paper-1 CI is untouched.

## Local build result

A clean local `latexmk`/pdfLaTeX build succeeded using installed `bibtex8` through a temporary PATH shim because the container's default `/usr/bin/bibtex` alternative was broken.

Result:

- **21 pages**;
- letter page size, 612 x 792 pt;
- PDF openable and unencrypted;
- all citations resolved;
- all cross-references resolved;
- zero overfull hboxes/vboxes;
- zero underfull boxes;
- only remaining warning: benign `Package nameref Warning: The definition of \label has changed!`.

PDF preflight:

- encrypted: no;
- openable with PyMuPDF: yes;
- scanned: no;
- XFA: no.

## Local hashes

Generated Rev6 source SHA-256:

`ebbecd8e3d82ad7bffdb3209ab125058b1c6400733ce9ccd82ba0163ff4df2dd`

Generated Rev6 PDF SHA-256:

`9ec937f2a7352f53869c03e3af13030174d97c870855e131e7de022f49719d4e`

Local self-contained source ZIP SHA-256:

`7b65b31b2bc173c6a47721bc9f71b10a0efbb7763f39b37bdec43d163ad8aa58`

Figure-2 numerical CSV SHA-256:

`8702bf54e7585d529b4eeac8c8fc0077c1f288c57659d82c2fc178fb5f07863a`

## Figure provenance and validation

### Figure 1

Pure schematic. No quantitative data. Shows incident Poisson trajectory -> autonomous hidden-memory detector -> accessible record, and contrasts scalar summaries with the trajectory Fisher operator/spectrum.

Final layout was visually inspected after removal of top-label collisions and a redundant time label.

### Figure 2

Uses the exact deterministic Type-II Volterra renewal-score calculation at `lambda*tau=1` and the analytic one-statistic lower bound.

The numerical curve was obtained from `h=0.005` and `h=0.0025` causal trapezoidal solutions with first-order Richardson extrapolation. At `omega*tau=pi`:

- `h=0.005`: `0.52783253`;
- `h=0.0025`: `0.52798759`;
- extrapolated: `0.52814265`;
- rigorous lower bound: `0.51697536`.

The final plot clips data outside the displayed `0 <= omega*tau <= 20` range correctly; no plotted data extend outside the axis box.

### Figure 3

Left panel is the exact universal conventional curve

`r*m=(lambda*m) exp[-lambda*m]`

for every iid recovery law of fixed mean `m`.

Right panel compares the theorem-exact deterministic value `G_DC=0` with the independently calibrated exponential-recovery value `G_DC approximately 0.06915579` at `lambda*m=1`.

### Figure 4

Shows the two exact mean/variance-matched discrete laws from WP19 and the analytic common-statistic Fisher witness:

- law A: zero;
- law B: `0.00443520488427` normalized per-time FI.

The common-statistic result, not a numerical full-record fit, is the theorem.

## Visual inspection

Rev6 was rendered to 21 page images and inspected as a complete contact sheet. The figure pages were additionally inspected at readable scale.

No observed:

- clipped text;
- figure/data spill beyond axes;
- label collisions after final repairs;
- equation/text overlap;
- margin overflow;
- broken glyphs or black boxes;
- unresolved hyperlink boxes.

The final bibliography occupies the end of page 20 and a short page 21 containing its final entries. This is mechanically valid and was not compressed artificially merely to save one preprint page.

## Verification boundary

Rev6 is **locally build-verified, preflighted, and visually inspected**.

The actual branch push-triggered GitHub Actions Rev6 job has not been directly inspected because the available connector in this session does not expose a reliable listing of push-triggered workflow runs. Do not claim GitHub-Actions-run verification until that job itself is read.

## Current decision

Rev6 is the current **frozen science draft**. Further changes should be driven by:

- a concrete defect;
- an external/referee-style objection;
- a verified novelty collision;
- or submission-stage metadata/package requirements.
