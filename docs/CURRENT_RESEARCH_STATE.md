# Current Research State

**Date:** 2026-08-20

Active branch:

`agent/uprp-core-theorem-round10`

## Immediate status

The first-paper foundational research phase is **closed by default**.

Current preferred submission candidate: **Rev9**.

Rev9 preserves the full Rev8 theorem stack and adds only translational/operational grounding for detector physicists and experimentalists.

Read first:

1. `AGENTS.md`
2. `notes/RESEARCH_LOG_ROUND18_TRANSLATIONAL_GROUNDING.md`
3. `submission/PRAPPLIED_PACKAGE_VALIDATION_REV9.md`
4. `submission/SUBMISSION_PACKAGE_CHECKLIST_REV9.md`
5. `manuscript/section_practical_grounding_rev9.tex`

## Reproducible source chain

Rev9 is generated in two assertion-based steps:

1. frozen Rev7 -> Rev8 via `manuscript/apply_rev8_referee_surgical.py`;
2. Rev8 -> Rev9 via `manuscript/apply_rev9_grounding.py`.

Source hashes are pinned in:

- `manuscript/REV8_SHA256SUMS.txt`;
- `manuscript/REV9_SHA256SUMS.txt`.

Generated Rev9 main source SHA-256:

`79d0da661ba394b6064a73103cce4db157f634d2d4b5d47a674c7cd1552af6fc`

Practical section SHA-256:

`b4702642705b01ef811e95f5a3d2d0686bb951122c337fd438d0b53fa0a18c3f`

## Validation

Canonical Rev9 build:

- 30 pages;
- PDF SHA-256 `2d8c93a98840d303a1f32cc3c67cd4c2c6d46a4010e440317691cae09df1f0cc`;
- no undefined citations or cross-references;
- new pages visually inspected;
- only material overfull warning is the inherited approximately `2.45667 pt` `timing-concentration` line in Appendix A.

PRApplied copy:

- 30 pages;
- PDF SHA-256 `5e4c17e7a7e3a8f26172e770b43d9391f88d20e0252cfdc9425e530cbfec9111`;
- final package ZIP SHA-256 `c612899d536f4653e872f179f8b9fbea61264ed37e3120ac68fb1813ac5b913d`.

Steady-state CI is read-only and generates/hash-checks/compiles Rev9 without committing generated sources.

---

# Theorem status

No Rev9 theorem changes were made.

The current theorem class remains autonomous/time-translation-invariant, independent-event / low-overlap, one-primary-registration photodetection under weak coherent/Poisson direct-detection intensity modulation with complete accessible primary-event marks.

Core exact result:

\[
G(\omega)=\int_{\mathsf M}|H_m(\omega)|^2\kappa(dm).
\]

For arbitrary finite-dimensional weak temporal perturbations,

\[
[F_{\rm out}]_{ab}
=\frac{\Phi_0}{2\pi}\int G(\omega)S_a^*(\omega)S_b(\omega)d\omega.
\]

Pointwise ordering of `G` is necessary and sufficient for local Fisher dominance over every admitted weak temporal waveform task.

For square-integrable timing densities,

\[
B_{\rm FI}=\frac{\mathfrak R_2}{4\eta}
\le\frac{\mathfrak H}{4\eta}.
\]

The exact inverse resource cost remains

\[
\mathfrak R_2\ge4Bq,\qquad \mathfrak H\ge4Bq.
\]

---

# What Rev9 adds operationally

## Canonical timing laws

Single unresolved mark:

\[
B_{\rm FI}=\frac12\int f^2dt.
\]

Closed forms are supplied for Gaussian timing error, exponential wait, uniform delay, Erlang serial waits, and Gaussian--exponential convolution.

Important examples:

\[
B_{\rm FI}^{\rm Gaussian}=\frac{1}{4\sqrt\pi\sigma},
\qquad
B_{\rm FI}^{\rm exp}=\frac{\Lambda}{4},
\qquad
B_{\rm FI}^{\rm uniform}=\frac{1}{2T}.
\]

For the exponential model,

\[
\frac{B_{\rm FI}}{f_{3\rm dB}}=\frac\pi2.
\]

## Fit-free histogram estimator

For equal bins `Delta t` with conditional-on-capture probabilities `p_i`,

\[
B_{\rm FI}^{(\Delta t)}
=\frac{1}{2\Delta t}\sum_i p_i^2.
\]

With counts `n_i`, `N=sum_i n_i`, an unbiased finite-count estimator of the binned quantity is

\[
\widehat B_{\rm FI,U}^{(\Delta t)}
=\frac{1}{2\Delta t}\frac{\sum_i n_i(n_i-1)}{N(N-1)}.
\]

Finite binning obeys

\[
B_{\rm FI}^{(\Delta t)}\le B_{\rm FI}.
\]

## Support correction

Finite support does **not** upper-bound Fisher bandwidth. If a normalized density lies in an interval of length `T`,

\[
B_{\rm FI}\ge\frac1{2T}.
\]

There is no support-only upper bound. A separate density ceiling `||f||_infty <= M` gives `B_FI <= M/2`.

## Mark resource

Fine accessible marks can increase retained FI relative to discarding those marks. Exact latency-resolving primary marks give `G=eta` at all frequency.

A downstream TDC does not recreate information already lost before the primary record merely by increasing digitization resolution.

## Preamplifier distinction

Independent unresolved stochastic delays multiply transfer spectra. A deterministic, known, noiseless, invertible TIA filter does not automatically reduce FI. Any information loss attributed to an amplifier must come through an explicit observation limitation such as additive noise, finite sampling/bandwidth, saturation, thresholding, noninvertibility, or stochastic latency.

## DC normalization

`G(0)=eta` is already correctly normalized. The absolute FI prefactor differs by two between exact DC and nonzero sinusoidal modulation under the paper's parameterization, but the normalized transfer ratio does not require multiplying `G(0)` by two.

---

# Submission state

Primary target remains:

**Physical Review Applied — Regular Article**

Rev9 submission support files are complete except for personal factual metadata. The remaining blockers are:

- author name/order;
- affiliation(s);
- corresponding-author email;
- ORCID;
- truthful substantive-AI acknowledgment describing the human verification process;
- applicable funding/conflict/prior-submission declarations.

Do not start another science revision unless a new concrete mathematical or model-class defect is identified.
