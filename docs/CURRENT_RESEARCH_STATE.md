# Current Research State

**Date:** 2026-08-20

Active branch:

`agent/uprp-core-theorem-round10`

## Immediate status

The first-paper foundational research phase is **closed by default**. The canonical science source is frozen Rev7:

`manuscript/event_resource_theorem_rev7.tex`

Primary submission target:

**Physical Review Applied — Regular Article**

The Physical Review Applied package has now been **mechanically compiled and visually validated**. The remaining blockers before actual submission are personal/administrative metadata and a truthful final APS substantive-AI disclosure; no additional theorem work is currently required.

Read next for submission work:

1. `submission/PRAPPLIED_PACKAGE_VALIDATION_REV7.md`
2. `submission/SUBMISSION_PACKAGE_CHECKLIST_REV7.md`
3. `submission/SUBMISSION_STRATEGY_REV7.md`
4. `submission/COVER_LETTER_PRAPPLIED_REV7.md`
5. `submission/AI_DISCLOSURE_DRAFT_REV7.md`
6. `submission/BIBLIOGRAPHY_AUDIT_REV7.md`

---

# Canonical Rev7 verification

Canonical main-TeX Git blob:

`f59e36e32a2d6eb36752c847cbdd40b07b241db0`

Science validation:

- push run `32433326375`: generation, full LaTeX compilation, artifact upload, and source persistence **SUCCESS**;
- independent proof-hardened run `32433375491`: generation, full LaTeX compilation, artifact upload **SUCCESS**;
- independent artifact `9429898246`;
- artifact ZIP SHA-256 `733262dc3b07b6959c175bbddb5ee1185016500b276dd932061342c75199f276`;
- independent Rev7 build: 24 pages, 360775 bytes;
- only previously identified nontrivial layout warning was the inherited approximately `2.45667 pt` appendix overfull line involving “timing-concentration.”

Temporary science-validation PR #13 is closed and unmerged.

---

# Physical Review Applied package validation

The canonical Rev7 source is **not modified** for journal packaging. Submission copy generation is assertion-based:

`manuscript/make_prapplied_submission.py`

It adds only:

1. a non-rendered comment reminding the submitter to finalize the APS substantive-AI disclosure with truthful human-verification wording;
2. the unnumbered Data Availability statement required for the purely mathematical paper.

Submission-package validation:

- temporary PR `#14` — **CLOSED, UNMERGED**;
- trigger SHA `9f74f1178aaea4595ca20d682dad840fc532d8c8`;
- Actions run `32434850102` — **SUCCESS**;
- job `96633863739` — **SUCCESS**;
- artifact `9430408451`;
- artifact ZIP size `384207 bytes`;
- artifact ZIP SHA-256 `0ce70d971c0038fe5eb13eccb95b4ede45272e4a2dcb8297d212eff579e2418f`.

Generated Physical Review Applied PDF:

- 24 pages;
- 361041 bytes;
- SHA-256 `e80562d69146514dede7c201c6aff29040002296ae10e4e8ff9876120dc6a2b8`.

Generated submission TeX SHA-256:

`3a26badedf7c1155801447f0dd803d2f93da09a574361998c26cea8dfabe4979`

All 24 pages were rendered and visually inspected. No clipping, malformed equation, broken figure, bibliography truncation, or new visually apparent layout defect was found. The Data Availability section appears immediately before the appendix as intended.

A unified-diff check found no scientific source change: the generated submission TeX differs from canonical Rev7 only by the intended compliance insertion before `\\appendix`.

Full record:

`submission/PRAPPLIED_PACKAGE_VALIDATION_REV7.md`

---

# Steady-state CI

After package validation, temporary PR-validation machinery was removed again.

Current workflow:

`.github/workflows/manuscript-check.yml`

Restored in commit:

`e311619993c743faa1b115ede0dcbcbab55eaadd`

Current workflow blob:

`2ced3dba39d3472f7a6328831d1d368f30e86fb5`

Steady-state behavior:

- `permissions: contents: read`;
- direct compilation of committed `event_resource_theorem_rev7.tex`;
- Rev7 artifact upload only;
- no source generation;
- no self-commit/push;
- no temporary pull-request validation trigger.

---

# Journal strategy

Primary:

1. **Physical Review Applied — Regular Article**

Fallbacks if rejected primarily on fit rather than correctness:

2. **Physical Review Research — Regular Article**
3. **Physical Review A — Regular Article**
4. reassess **Optica** / **Optics Express** based on editorial feedback.

The venue rationale and current APS requirements are recorded in:

`submission/SUBMISSION_STRATEGY_REV7.md`

Prepared support files:

- exact 100-word PRApplied suitability justification;
- PRApplied cover-letter draft;
- Data Availability statement;
- APS AI-use disclosure draft;
- bibliography/citation audit;
- package checklist.

Bibliography gate: **PASSED**. All current references contain titles, DOI/bibliographic metadata was checked, and no citation-driven scientific correction to Rev7 was identified.

---

# Remaining blockers before actual submission

Required personal/administrative items:

- replace `Anonymous` author metadata;
- truthful affiliation(s);
- corresponding author and active email;
- authenticated corresponding-author ORCID;
- confirm author list/order/contributions;
- finalize substantive-AI disclosure, including how the human author directed and verified AI output;
- insert the finalized disclosure into the generated submission copy;
- confirm funding/acknowledgments, conflicts, related manuscripts/preprints, and prior APS submission history as applicable.

Optional:

- recommended referees;
- excluded referees/conflicts if needed;
- repair the inherited approximately `2.45667 pt` appendix overfull line if a meaning-neutral fix is convenient. It is not a submission blocker.

Do **not** invent personal verification language or author metadata.

---

# Detector class

The first-paper theorem is restricted to:

- autonomous/time-translation-invariant processing;
- independent-event / low-overlap operation;
- one primary electrical registration per captured photon;
- complete accessible primary-event marks;
- weak coherent/Poisson direct-detection intensity modulation;
- parameter-independent downstream background/processing for the FI data-processing step.

It is not a universal speed law for every detector architecture.

Per incident photon,
\[
K(dm,d\tau)=\kappa(dm)\mu_m(d\tau),
\qquad
\eta=\kappa(\mathsf M)\le1.
\]

The exact sinusoidal source-normalized transfer is
\[
\boxed{G(\omega)=\int_{\mathsf M}|H_m(\omega)|^2\kappa(dm).}
\]

At exact DC, normalized transfer remains
\[
\boxed{G(0)=\eta.}
\]

---

# Rev7 significance layer

For finite-dimensional weak temporal perturbations,
\[
\boxed{
[F_{\rm out}]_{ab}
=\frac{\Phi_0}{2\pi}
\int G(\omega)S_a^*(\omega)S_b(\omega)d\omega.
}
\]

Thus `G` is the complete local weak-waveform Fisher multiplier for this detector class.

Regularity:
\[
\boxed{
0\le G(\omega)\le\eta,
\qquad G(-\omega)=G(\omega),
\qquad G\in C(\mathbb R).
}
\]

Detector ordering:
\[
\boxed{
G_A(\omega)\ge G_B(\omega)\ \forall\omega
\iff
F_A\succeq F_B
\text{ for every admissible finite weak-waveform task.}
}
\]

This is local Fisher ordering, **not** generic Blackwell dominance.

Band-subspace guarantee:
\[
\boxed{
\inf_{\substack{s\ne0\\\operatorname{supp}S\subset[-\Omega,\Omega]}}
\frac{F_{\rm out}[s]}{F_{\rm in}[s]}
=
\min_{|\omega|\le\Omega}G(\omega).
}
\]

Hence retaining at least absolute fraction `q` for every weak waveform in the band is equivalent to `G(omega)>=q` throughout that band.

---

# Timing-resource hierarchy and operational bounds

Collision resource:
\[
\boxed{
\mathfrak R_2=2\int\kappa(dm)\int f_m(t)^2dt,
\qquad
\int G(\omega)d\omega=\pi\mathfrak R_2.
}
\]

Capture-weighted hazard resource:
\[
\boxed{
\mathfrak H=\int\Lambda(m)\kappa(dm),
\qquad
\mathfrak R_2\le\mathfrak H.
}
\]

Exact Fisher-equivalent bandwidth:
\[
\boxed{
B_{\rm FI}
=\frac1\eta\int_0^\infty G(2\pi f)df
=\frac{\mathfrak R_2}{4\eta}
\le\frac{\mathfrak H}{4\eta}.
}
\]

Common conditional-hazard ceiling:
\[
\boxed{B_{\rm FI}\le\Lambda/4.}
\]

For ordinary-frequency half-band `B=Omega/(2pi)` and absolute required retention `q`,
\[
\boxed{
q\le\eta,
\qquad
\mathfrak R_2\ge4Bq,
\qquad
\mathfrak H\ge4Bq.
}
\]

For a common hazard ceiling,
\[
\boxed{\Lambda\ge4Bq/\eta.}
\]

For `q=r eta`,
\[
\boxed{\Lambda\ge4Br.}
\]

Independent unmarked delay-only cascade:
\[
\boxed{G_{12}=G_1G_2.}
\]

For `k` serial exponential waits,
\[
\boxed{
B_{\rm FI}
=\frac{\lambda}{4}
\frac{\binom{2k-2}{k-1}}{4^{k-1}}
\sim\frac{\lambda}{4\sqrt{\pi(k-1)}}.
}
\]

---

# Critical no-go / scope results retained from Rev6

- exact mean delay + exact RMS jitter do **not** bound finite temporal-information bandwidth;
- no fixed-FWHM counterexample is claimed;
- free source-synchronous timing reference defeats detector-only timing bounds unless the reference is counted as a resource;
- the safe finite-state CTMC mark-conditioned hazard ceiling uses the maximum **total escape rate**
  \[
  q_{\max}=\max_{x\in S_{\rm pre}}\sum_{y\ne x}W_{yx},
  \]
  not merely the successful-registration edge intensity;
- use **bidirectionally connected**, not “reversible,” for the nonequilibrium thermodynamic network;
- the thermodynamic bridge applies to the event theorem only through the explicit isolated-event / low-overlap reduction;
- stationary EPR/activity/throughput alone do not supply an absolute microscopic time scale;
- generic quantum-jump operator-norm extension remains deferred.

---

# Novelty posture

Do not claim:

- first information-theoretic detector timing analysis;
- first IRF-information result;
- first generic sensitivity-bandwidth tradeoff;
- generic Fisher-information transfer-function novelty;
- generic Blackwell dominance;
- generic finite-frequency response/noise novelty;
- arbitrary fixed-FWHM no-go;
- a universal all-detector speed limit.

Defensible contribution:

> A temporal-information resource theory for autonomous marked photodetection event channels in which the exact marked-delay spectrum is the complete local weak-waveform Fisher multiplier; pointwise spectral ordering is necessary and sufficient for local weak-waveform Fisher dominance; atomic timing, collision concentration, and capture-weighted hazard provide a resource hierarchy; the exact Fisher-equivalent bandwidth and inverse band-resource costs make that hierarchy operational; and explicit no-go/repair results show why low-order jitter metrics, free synchronous control, and aggregate stationary thermodynamics are incomplete resources.

Novelty is strongest in the combined theorem stack.

---

# Frozen work

Do not reopen unless a concrete Rev7 referee-level defect requires it:

- HgCdTe/Kane WP17--24;
- coherent quantum pointers;
- continuous analog detector generalization;
- non-Poisson/nonclassical source extensions;
- high-flux/history-dependent event channels;
- capacity/QFI generalizations.

Those are second-paper directions, not first-paper submission blockers.

---

# Next action

Do **not** continue foundational expansion.

When truthful author/affiliation/corresponding-author/ORCID and human-verification wording for the APS AI disclosure are available, generate the final named Physical Review Applied submission copy, compile it once more, visually inspect the metadata/compliance pages, and assemble the portal-ready source bundle.
