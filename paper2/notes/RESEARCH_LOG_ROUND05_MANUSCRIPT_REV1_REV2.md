# Research Log Round 05 — Paper 2 manuscript Rev1/Rev2

**Date:** 2026-08-21

## Status

The Paper-2 manuscript gate passed in WP27. Drafting is now active.

Working title:

> **Fisher Spectra and Information Singularities in Photodetectors with Memory**

The manuscript is organized around one thesis: a detector saturation curve is not an information-transfer law; local temporal information belongs to the complete trajectory channel.

## Durable manuscript assets

- `paper2/MANUSCRIPT_ARCHITECTURE.md` — theorem order, claim matrix, section plan, appendix plan, figure plan.
- `paper2/manuscript/fisher_spectra_memory_photodetectors_rev1.tex` — first complete science draft.
- `paper2/manuscript/paper2_refs.bib` — Paper-2 bibliography.
- `paper2/manuscript/apply_rev2_science_fix.py` — assertion-checked Rev1 -> Rev2 science-fix generator.
- `.github/workflows/paper2-manuscript-check.yml` — separate read-only Paper-2 LaTeX/BibTeX workflow. It does not modify the frozen Paper-1 CI chain.

## Main-text theorem order in Rev1/Rev2

1. General autonomous-channel temporal Fisher spectrum (WP10/WP17).
2. Deterministic Type-II static blindness with positive information at every nonzero temporal frequency and high-frequency limit `1/e` (WP07).
3. Arbitrary finite-mean iid-recovery zero-IFF-deterministic stationary Fisher theorem (WP25/WP26).
4. Exact mean+variance resource-incompleteness counterexample (WP19).
5. Atomic conditional-score timing paths retained as structural interpretation only (WP22–WP24).

## Required notation distinction

The manuscript must keep three objects distinct:

- `G(omega)`: the a.e.-defined autonomous-channel spectral Fisher multiplier from WP10/WP17; model-specific continuous/narrowband representatives may be used when proved.
- `G_cyc`: Palm regenerative-cycle normalized Fisher retention.
- `G_DC`: stationary long-window homogeneous-rate Fisher retention.

WP26 proves `G_DC=G_cyc=(r/lambda) I_D` for the finite-mean iid Type-II class. This does not turn the universal a.e. spectral multiplier into a pointwise value at zero without model-specific continuity.

## Rev1 defect and Rev2 correction

A static audit found one real notation defect in Rev1:

- the renewal-density Laplace transform was introduced as Greek `\nu_s`, while the subsequent equations use the intended Latin `u_s`.

The initial Rev2 generator was itself defective because its replacement target and replacement text were identical. This was caught before claiming build verification.

The generator has now been repaired. It:

1. replaces Greek `\nu_s` with Latin `u_s` exactly once;
2. asserts that `G_DC`, `G_cyc`, the equality `G_DC=G_cyc=(r/lambda)I_D`, and the WP07 all-nonzero-frequency statement remain present;
3. fails if Greek `\nu_s` survives or Latin `u_s` is absent.

Treat generated Rev2, not raw Rev1, as the current science draft once the build succeeds.

## Static bibliography audit

All citation keys presently used in Rev1 are present in `paper2_refs.bib`, including:

- Teich & Vannucci 1978;
- Vannucci & Teich 1978;
- Teich & Cantor 1978;
- Dvurecenskij & Ososkov 1984/1985;
- Apanasovich & Paltsev 1995;
- Zhao & Nagaraja 2011;
- Barat, Dautremer & Trigano 2006;
- Jorgensen & Johnson 2026;
- Clark 2026;
- Pollard 2013;
- Kallenberg 2021;
- Stein 1970;
- Daley & Vere-Jones 2003.

No unresolved citation key was found by static inspection.

## Verification boundary

Do **not** yet call Rev2 build-verified.

The GitHub connector available in this session exposes job-level readers but not a reliable listing of branch push-triggered workflow runs. Local container networking cannot clone GitHub. Therefore the actual Paper-2 Actions compilation result has not yet been inspected.

What is verified now:

- manuscript architecture exists;
- Rev1 is a complete science draft;
- bibliography keys used by Rev1 are present;
- the Rev2 notation generator defect has been fixed and guarded by assertions;
- Paper-1 CI remains untouched;
- a separate read-only Paper-2 compile workflow exists.

What remains mechanically unverified:

- successful Rev2 LaTeX/BibTeX compilation;
- absence of compiler warnings beyond benign layout warnings;
- rendered-page visual inspection;
- final figures.

## Immediate next actions

1. Obtain the Paper-2 Actions run/job by any available connector route and inspect the actual compiler log.
2. Patch the first genuine LaTeX/BibTeX failure, if any, using another reproducible revision step rather than silently modifying Rev1.
3. Once compile succeeds, persist the generated Rev2 source or hash-pinned equivalent and record page count / warnings / artifact hash.
4. Render and visually inspect all manuscript pages before calling the draft mechanically validated.
5. Replace figure placeholders with publication-quality figures from validated numerical/theoretical assets.
6. Perform an adversarial manuscript-level review after figures and mechanical validation, focusing on claim scope, proof handoffs, prior-art language, and significance.

## Scientific status

No new theorem defect was found during the manuscript transition. The manuscript gate remains **passed with conservative novelty language**. Priority language remains disabled, especially for generic queue-output identifiability, classical Type-II cycle formulas, Bartlett spectra, or generic Fisher/score machinery.
