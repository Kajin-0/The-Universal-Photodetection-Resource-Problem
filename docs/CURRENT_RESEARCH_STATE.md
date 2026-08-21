# Current Research State

**Date:** 2026-08-20

Active branch:

`agent/uprp-core-theorem-round10`

## Immediate status

The first-paper foundational research phase is **closed by default**.

Current preferred submission candidate: **Rev9**.

Rev9 preserves the full Rev8 theorem stack and adds translational/operational grounding plus a short full-text-verified empirical anchor subsection for detector physicists and experimentalists.

Read first:

1. `AGENTS.md`
2. `notes/RESEARCH_LOG_ROUND19_EMPIRICAL_GROUNDING.md`
3. `notes/RESEARCH_LOG_ROUND18_TRANSLATIONAL_GROUNDING.md`
4. `submission/PRAPPLIED_PACKAGE_VALIDATION_REV9.md`
5. `submission/SUBMISSION_PACKAGE_CHECKLIST_REV9.md`
6. `submission/BIBLIOGRAPHY_AUDIT_REV9.md`
7. `notes/SUPPLEMENTAL_GROUNDING_LITERATURE_REV9.md`

## Reproducible source chain

Rev9 is generated in two assertion-based steps:

1. frozen Rev7 -> Rev8 via `manuscript/apply_rev8_referee_surgical.py`;
2. Rev8 -> Rev9 via `manuscript/apply_rev9_grounding.py`.

Pinned generated hashes:

- main Rev9 source: `8ae3e4eb89e3af48823e62332481dbb63912281aa75b653cf46f35166b892611`;
- practical section: `b4702642705b01ef811e95f5a3d2d0686bb951122c337fd438d0b53fa0a18c3f`;
- empirical section: `512d1d6b43c89933bf723476fa3bae6f0ed54d4d45688f3784602a70a8f12af4`;
- repaired Appendix: `f9afbdf7e0fd6cc1b57a3a4e00197148e907fc9ed7691a7f9dd42106e16ba665`.

## Validation

Canonical Rev9 build:

- 31 pages;
- 390412 bytes;
- PDF SHA-256 `ef566682d6b47eb0d133bca497f76503fc57817b98846ee4241e7a45fb4bd08d`;
- no undefined citations or cross-references;
- empirical pages and final reference pages visually inspected;
- only material overfull warning is the inherited approximately `2.45667 pt` `timing-concentration` line in Appendix A.

PRApplied copy:

- 32 pages;
- 391123 bytes;
- PDF SHA-256 `770bd2c58a5adcef0c88c6275a29e2a9a74441b02dca63415af6da394815533e`;
- submission TeX SHA-256 `6d71ea050b047000eed027e3fa1b0d6523c9aa4a52f5315b370fe3b4e6b1d0c0`;
- final package ZIP SHA-256 `4cde598d5aa88a4d1c66269148690aad4f5e5b4fe535bf49204901d1f7bdb665`.

Steady-state CI remains read-only and regenerates/hash-checks/compiles Rev9 without committing generated sources.

---

# Empirical grounding closure

Five historical SPAD timing papers supplied by the author were read in full and added only where they directly support phenomenological statements:

- Cova et al. 1989, DOI `10.1063/1.1140324` — TCPC timing histograms, timing-chain contributions, and sub-FWHM statistical/convolution inference;
- Lacaita and Mastrapasqua 1990, DOI `10.1049/el:19901324` — detector diameter, absorption position, avalanche spreading, and discriminator-crossing timing;
- Lacaita et al. 1993, DOI `10.1063/1.108870` — stochastic photon-assisted avalanche spreading and timing jitter;
- Spinelli et al. 1998, DOI `10.1109/3.668769` — Gaussian-like fast IRF component, diffusion tails, and why tail suppression matters beyond FWHM;
- Assanelli et al. 2011, DOI `10.1109/JQE.2010.2068038` — injection-position, discriminator-threshold, and propagation-statistics contributions to jitter.

These experiments motivate the timing structures formalized by Rev9; no experimental result is an assumption in a theorem or proof.

The supplemental literature audit now concludes that **no missing-paper blocker remains**. Do not mine further literature by default.

---

# Theorem status

No theorem changed in the empirical grounding pass.

The theorem class remains autonomous/time-translation-invariant, independent-event / low-overlap, one-primary-registration photodetection under weak coherent/Poisson direct-detection intensity modulation with complete accessible primary-event marks.

Core result:

\[
G(\omega)=\int_{\mathsf M}|H_m(\omega)|^2\kappa(dm),
\]

with complete weak-waveform Fisher operator

\[
[F_{\rm out}]_{ab}=\frac{\Phi_0}{2\pi}\int G(\omega)S_a^*(\omega)S_b(\omega)d\omega.
\]

For square-integrable timing densities,

\[
B_{\rm FI}=\frac{\mathfrak R_2}{4\eta}\le\frac{\mathfrak H}{4\eta}.
\]

The inverse resource cost remains

\[
\mathfrak R_2\ge4Bq,\qquad \mathfrak H\ge4Bq.
\]

## Rev9 operational formulas

Single unresolved mark:

\[
B_{\rm FI}=\frac12\int f^2dt.
\]

Equal timing bins `Delta t`:

\[
B_{\rm FI}^{(\Delta t)}=\frac{1}{2\Delta t}\sum_i p_i^2,
\]

and the unbiased finite-count estimator of that binned quantity is

\[
\widehat B_{\rm FI,U}^{(\Delta t)}
=\frac{1}{2\Delta t}\frac{\sum_i n_i(n_i-1)}{N(N-1)}.
\]

Finite support of length `T` gives `B_FI >= 1/(2T)` and **does not** provide a support-only upper bound.

A deterministic known noiseless invertible TIA response is not automatically an FI loss; the stochastic cascade product law must not be misapplied to generic electrical amplitude poles.

---

# Submission state

Primary target remains:

**Physical Review Applied — Regular Article**

The scientific, mathematical, translational, empirical-grounding, bibliography, compilation, and visual gates are closed.

Remaining blockers are factual human metadata/compliance only:

- author name/order;
- affiliation(s);
- corresponding-author email;
- ORCID;
- truthful substantive-AI acknowledgment describing the human verification process;
- applicable funding/conflict/prior-submission declarations.

Do not start another science/literature revision unless a new concrete mathematical/model-class defect or a specific referee request appears.
