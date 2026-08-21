# AGENTS.md

## Purpose

Durable handoff for **The Universal Photodetection Resource Problem (UPRP)**. The repository, not chat history, is authoritative.

Research is analytical/theoretical only. Numerical work may be used for validation. Do not make experiments, fabrication, procurement, or laboratory campaigns necessary next steps.

Active branch:

`agent/uprp-core-theorem-round10`

## Read first

1. `docs/CURRENT_RESEARCH_STATE.md`
2. `submission/PRAPPLIED_PACKAGE_VALIDATION_REV7.md`
3. `submission/SUBMISSION_PACKAGE_CHECKLIST_REV7.md`
4. `submission/SUBMISSION_STRATEGY_REV7.md`
5. `manuscript/event_resource_theorem_rev7.tex`
6. `notes/RESEARCH_LOG_ROUND16.md`
7. `notes/WP36_COMPLETE_WEAK_WAVEFORM_FISHER_OPERATOR.md`
8. `notes/WP36A_BAND_SUBSPACE_FISHER_GUARANTEE.md`
9. `docs/MANUSCRIPT_REV6_REFEREE_REPAIR_AUDIT.md`
10. `notes/RESEARCH_LOG_ROUND15.md`
11. `notes/WP35_MARK_CONDITIONED_MARKOV_RATE_CORRECTION.md`
12. `notes/WP34_MINIMUM_TIMING_RESOURCE_COST_THEOREM.md`
13. `notes/WP32_GENERAL_MARKED_POISSON_EVENT_KERNEL_THEOREM.md`
14. `notes/WP33_EXACT_FIXED_MEAN_VARIANCE_JITTER_NO_GO.md`
15. `notes/WP29_THERMODYNAMIC_BRIDGE_TO_REGISTRATION_INTENSITY.md`
16. `notes/WP30_WIENER_ATOMIC_DELAY_INFORMATION_THEOREM.md`
17. `docs/NOVELTY_AUDIT_ROUND5_EVENT_THEOREM_STACK.md`

---

# Current publication state

Canonical first-paper science source:

`manuscript/event_resource_theorem_rev7.tex`

Rev7 is **frozen for submission** unless a concrete referee-level defect is found.

Primary target:

**Physical Review Applied — Regular Article**

Fallback order:

1. Physical Review Research;
2. Physical Review A;
3. reassess Optica / Optics Express from actual editorial feedback.

Do not reopen foundational derivations merely to make the paper broader.

## Canonical Rev7 verification

Main TeX Git blob:

`f59e36e32a2d6eb36752c847cbdd40b07b241db0`

Successful science-validation runs:

- `32433326375` — generation, compile, artifact upload, source persistence;
- `32433375491` — independent proof-hardened compile/artifact validation.

Independent Rev7 artifact:

- artifact ID `9429898246`;
- ZIP SHA-256 `733262dc3b07b6959c175bbddb5ee1185016500b276dd932061342c75199f276`;
- PDF 24 pages, 360775 bytes.

Temporary validation PR #13 is closed and unmerged.

## Physical Review Applied package validation

Submission generator:

`manuscript/make_prapplied_submission.py`

It leaves canonical Rev7 untouched and assertion-generates a submission copy with only:

1. a comment-only reminder to finalize the APS substantive-AI disclosure truthfully;
2. the required purely mathematical Data Availability section.

Validation:

- temporary PR #14 — **closed, unmerged**;
- trigger SHA `9f74f1178aaea4595ca20d682dad840fc532d8c8`;
- Actions run `32434850102` — **SUCCESS**;
- job `96633863739` — **SUCCESS**;
- artifact ID `9430408451`;
- artifact ZIP SHA-256 `0ce70d971c0038fe5eb13eccb95b4ede45272e4a2dcb8297d212eff579e2418f`.

Generated PRApplied PDF:

- 24 pages;
- 361041 bytes;
- SHA-256 `e80562d69146514dede7c201c6aff29040002296ae10e4e8ff9876120dc6a2b8`.

Generated PRApplied TeX SHA-256:

`3a26badedf7c1155801447f0dd803d2f93da09a574361998c26cea8dfabe4979`

All 24 pages were visually inspected and passed. A unified diff confirmed no scientific modification beyond the intended compliance insertion before `\\appendix`.

Full record:

`submission/PRAPPLIED_PACKAGE_VALIDATION_REV7.md`

## Steady-state CI

Current workflow:

`.github/workflows/manuscript-check.yml`

Latest cleanup commit:

`e311619993c743faa1b115ede0dcbcbab55eaadd`

Workflow blob:

`2ced3dba39d3472f7a6328831d1d368f30e86fb5`

Steady state is read-only:

- `permissions: contents: read`;
- direct compile of committed Rev7;
- artifact upload only;
- no source generation;
- no self-commit/push;
- no PR-validation side effects.

---

# Remaining blockers before actual submission

These are personal/administrative, not scientific:

- replace `Anonymous` author name and affiliation;
- corresponding author and active email;
- authenticated corresponding-author ORCID;
- confirm author list/order/contributions;
- finalize a truthful APS substantive-AI disclosure, including how the **human author directed and verified** AI output;
- insert that disclosure into the submission copy;
- confirm funding, acknowledgments, conflicts, related manuscripts/preprints, and prior APS submission history as applicable;
- optionally choose recommended/excluded referees.

Do **not** invent author metadata or human-verification claims.

Prepared submission files include:

- `submission/COVER_LETTER_PRAPPLIED_REV7.md`
- `submission/PRAPPLIED_100_WORD_JUSTIFICATION_REV7.txt`
- `submission/DATA_AVAILABILITY_REV7.txt`
- `submission/AI_DISCLOSURE_DRAFT_REV7.md`
- `submission/BIBLIOGRAPHY_AUDIT_REV7.md`
- `submission/SUBMISSION_PACKAGE_CHECKLIST_REV7.md`

Bibliography/citation gate is passed; no citation-driven scientific repair was required.

---

# First-paper theorem class

The theorem concerns autonomous/time-translation-invariant, independent-event / low-overlap, one-primary-registration photodetection under weak coherent/Poisson direct-detection intensity modulation, retaining the complete accessible primary-event mark.

Do **not** describe it as a universal all-detector speed limit.

Per incident photon,
\[
K(dm,d\tau)=\kappa(dm)\mu_m(d\tau),
\qquad
\eta=\kappa(\mathsf M)\le1.
\]

Exact sinusoidal source-normalized Fisher transfer:
\[
\boxed{G(\omega)=\int_{\mathsf M}|H_m(\omega)|^2\kappa(dm).}
\]

At exact DC,
\[
\boxed{G(0)=\eta.}
\]

Parameter-independent downstream processing cannot increase primary-record FI.

---

# Rev7 core results

## Complete weak-waveform Fisher operator

For finite-dimensional real weak temporal perturbations,
\[
\boxed{
[F_{\rm out}]_{ab}
=\frac{\Phi_0}{2\pi}
\int G(\omega)S_a^*(\omega)S_b(\omega)d\omega.
}
\]

Thus `G(omega)` is the complete local weak-waveform Fisher multiplier.

Regularity:
\[
\boxed{
0\le G(\omega)\le\eta,
\qquad G(-\omega)=G(\omega),
\qquad G\in C(\mathbb R).
}
\]

## Universal weak-waveform Fisher ordering

\[
\boxed{
G_A(\omega)\ge G_B(\omega)\ \forall\omega
\iff
F_A\succeq F_B
\text{ for every admissible finite weak-waveform task.}
}
\]

This is local Fisher ordering, **not** generic Blackwell dominance.

## Exact band-subspace guarantee

\[
\boxed{
\inf_{\substack{s\ne0\\\operatorname{supp}S\subset[-\Omega,\Omega]}}
\frac{F_{\rm out}[s]}{F_{\rm in}[s]}
=
\min_{|\omega|\le\Omega}G(\omega).
}
\]

Therefore retaining at least absolute FI fraction `q` for every weak waveform in the band is equivalent to `G(omega)>=q` throughout the band.

---

# Timing-resource hierarchy

Atomic flat-band residue:
\[
\boxed{
\lim_{\Omega\to\infty}\frac1{2\Omega}
\int_{-\Omega}^{\Omega}G(\omega)d\omega
=
\int\kappa(dm)\sum_jp_j(m)^2.
}
\]

Collision resource:
\[
\boxed{
\mathfrak R_2=2\int\kappa(dm)\int f_m(t)^2dt,
\qquad
\int G(\omega)d\omega=\pi\mathfrak R_2.
}
\]

Capture-weighted local-hazard resource:
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

Common hazard ceiling:
\[
\boxed{B_{\rm FI}\le\Lambda/4.}
\]

Inverse resource cost, with `B=Omega/(2pi)`:
\[
\boxed{
q\le\eta,
\qquad
\mathfrak R_2\ge4Bq,
\qquad
\mathfrak H\ge4Bq.
}
\]

Common ceiling:
\[
\boxed{\Lambda\ge4Bq/\eta.}
\]

Relative retention `q=r eta`:
\[
\boxed{\Lambda\ge4Br.}
\]

Independent unresolved unmarked delay stages:
\[
\boxed{G_{12}=G_1G_2.}
\]

For `k` serial exponential waits of rate `lambda`,
\[
\boxed{
B_{\rm FI}
=\frac{\lambda}{4}
\frac{\binom{2k-2}{k-1}}{4^{k-1}}
\sim\frac{\lambda}{4\sqrt{\pi(k-1)}}.
}
\]

---

# Mandatory scope / no-go boundaries

- exact mean delay + exact RMS jitter do not bound finite temporal-information bandwidth;
- no fixed-FWHM counterexample is claimed;
- a free source-synchronous clock/reference defeats detector-only timing bounds unless counted as a resource;
- finite-state CTMC conditional-hazard completion uses
  \[
  q_{\max}=\max_{x\in S_{\rm pre}}\sum_{y\ne x}W_{yx},
  \]
  the maximum **total escape rate**, not merely the successful-registration edge rate;
- the generic quantum-jump operator-norm extension remains deferred;
- use **bidirectionally connected**, not “reversible,” for the nonequilibrium CTMC network;
- stationary thermodynamic constraints bridge to the event theorem only through the explicit isolated-event / low-overlap reduction;
- if capture/recovery is history dependent, the independent-event theorem is not claimed;
- stationary EPR/activity/throughput alone do not supply the missing absolute microscopic time scale.

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

Novelty is strongest in the **combined theorem stack**.

---

# Frozen branches

Keep frozen unless a concrete Rev7 defect forces reopening:

- HgCdTe/Kane WP17--24;
- coherent quantum pointers;
- continuous analog detector generalization;
- non-Poisson/nonclassical source extensions;
- high-flux/history-dependent event channels;
- capacity/QFI extensions.

These are second-paper directions.

---

# Immediate next action

Do **not** continue foundational first-paper expansion.

When truthful author/affiliation/corresponding-author/ORCID data and human-verification wording for the APS AI disclosure are available:

1. generate the final named PRApplied submission copy from frozen Rev7;
2. insert the finalized AI acknowledgment;
3. compile once more;
4. visually inspect the metadata/compliance pages;
5. assemble the journal-portal source bundle.

Status vocabulary: **PROVED**, **VERIFIED**, **CONJECTURE**, **COUNTEREXAMPLE**, **OPEN**, **BLOCKED**, **REJECTED**.
