# AGENTS.md

## Purpose

Durable handoff for **The Universal Photodetection Resource Problem (UPRP)**. The repository, not chat history, is authoritative.

Research is analytical/theoretical only. Numerical work may be used for validation. Do not make experiments, fabrication, procurement, or laboratory campaigns necessary next steps.

Active branch:

`agent/uprp-core-theorem-round10`

## Read first

1. `docs/CURRENT_RESEARCH_STATE.md`
2. `notes/RESEARCH_LOG_ROUND19_EMPIRICAL_GROUNDING.md`
3. `notes/RESEARCH_LOG_ROUND18_TRANSLATIONAL_GROUNDING.md`
4. `submission/PRAPPLIED_PACKAGE_VALIDATION_REV9.md`
5. `submission/SUBMISSION_PACKAGE_CHECKLIST_REV9.md`
6. `submission/BIBLIOGRAPHY_AUDIT_REV9.md`
7. `notes/SUPPLEMENTAL_GROUNDING_LITERATURE_REV9.md`
8. `manuscript/section_practical_grounding_rev9.tex`
9. `manuscript/section_empirical_grounding_rev9.tex`
10. `manuscript/apply_rev9_grounding.py`
11. `manuscript/REV9_SHA256SUMS.txt`
12. `notes/RESEARCH_LOG_ROUND17.md`
13. `notes/RESEARCH_LOG_ROUND16.md`

---

# Current publication state — Rev9

**Rev9 is the preferred first-paper submission candidate.**

The reproducible version chain is:

1. frozen theorem source: `manuscript/event_resource_theorem_rev7.tex`;
2. Rev8 hostile-review repair: `manuscript/apply_rev8_referee_surgical.py`;
3. Rev9 translational + empirical grounding: `manuscript/apply_rev9_grounding.py`;
4. expected generated-source hashes: `manuscript/REV8_SHA256SUMS.txt` and `manuscript/REV9_SHA256SUMS.txt`.

Rev9 does **not** broaden or modify the theorem class. The five newly cited historical SPAD papers are empirical anchors only.

Current generated hashes:

- `event_resource_theorem_rev9.tex`: `8ae3e4eb89e3af48823e62332481dbb63912281aa75b653cf46f35166b892611`;
- `section_practical_grounding_rev9.tex`: `b4702642705b01ef811e95f5a3d2d0686bb951122c337fd438d0b53fa0a18c3f`;
- `section_empirical_grounding_rev9.tex`: `512d1d6b43c89933bf723476fa3bae6f0ed54d4d45688f3784602a70a8f12af4`;
- repaired Appendix: `f9afbdf7e0fd6cc1b57a3a4e00197148e907fc9ed7691a7f9dd42106e16ba665`.

Validated canonical Rev9 build:

- 31 pages;
- 390412 bytes;
- PDF SHA-256 `ef566682d6b47eb0d133bca497f76503fc57817b98846ee4241e7a45fb4bd08d`;
- no undefined citations or references;
- only inherited material overfull warning: approximately `2.45667 pt` around `timing-concentration` in Appendix A;
- new empirical pages and final references visually inspected.

Validated PRApplied copy:

- 32 pages;
- 391123 bytes;
- PDF SHA-256 `770bd2c58a5adcef0c88c6275a29e2a9a74441b02dca63415af6da394815533e`;
- submission TeX SHA-256 `6d71ea050b047000eed027e3fa1b0d6523c9aa4a52f5315b370fe3b4e6b1d0c0`;
- final package ZIP SHA-256 `4cde598d5aa88a4d1c66269148690aad4f5e5b4fe535bf49204901d1f7bdb665`.

Steady-state CI is read-only. It generates Rev8, checks Rev8 hashes, generates Rev9, checks Rev9 hashes, compiles Rev9, and uploads the artifact. It performs no source mutation.

---

# First-paper theorem class

Autonomous/time-translation-invariant, independent-event / low-overlap, one-primary-registration photodetection under weak coherent/Poisson direct-detection intensity modulation, retaining the complete accessible primary-event mark.

Do **not** describe this as a universal speed limit for all photodetectors.

Per incident photon,

\[
K(dm,d\tau)=\kappa(dm)\mu_m(d\tau),\qquad \eta=\kappa(\mathsf M)\le1.
\]

Exact sinusoidal transfer:

\[
\boxed{G(\omega)=\int_{\mathsf M}|H_m(\omega)|^2\kappa(dm).}
\]

At exact DC the normalized transfer remains

\[
\boxed{G(0)=\eta.}
\]

For admissible finite weak temporal perturbations,

\[
\boxed{
[F_{\rm out}]_{ab}=\frac{\Phi_0}{2\pi}\int G(\omega)S_a^*(\omega)S_b(\omega)d\omega.
}
\]

Pointwise ordering of `G` is necessary and sufficient for local Fisher dominance over every admitted finite weak-waveform task. This is local Fisher ordering, **not** generic Blackwell dominance.

---

# Timing-resource hierarchy

For square-integrable delay densities,

\[
\boxed{
\mathfrak R_2=2\int\kappa(dm)\int f_m^2dt,
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

Equivalent Fisher bandwidth:

\[
\boxed{
B_{\rm FI}=\frac{\mathfrak R_2}{4\eta}\le\frac{\mathfrak H}{4\eta}.
}
\]

Minimum resource cost over ordinary-frequency half-band `B`:

\[
\boxed{
\mathfrak R_2\ge4Bq,
\qquad
\mathfrak H\ge4Bq.
}
\]

---

# Rev9 operational grounding — formulas that must not be corrupted

Single unresolved mark:

\[
\boxed{B_{\rm FI}=\frac12\int f(t)^2dt.}
\]

Histogram bins `Delta t`:

\[
\boxed{B_{\rm FI}^{(\Delta t)}=\frac{1}{2\Delta t}\sum_i p_i^2.}
\]

Unbiased finite-count estimator of the binned quantity:

\[
\boxed{
\widehat B_{\rm FI,U}^{(\Delta t)}
=\frac{1}{2\Delta t}\frac{\sum_i n_i(n_i-1)}{N(N-1)}.
}
\]

Finite binning obeys `B_FI^(Delta t) <= B_FI`.

If a normalized density is supported on an interval of length `T`,

\[
\boxed{B_{\rm FI}\ge\frac1{2T}.}
\]

Finite support gives **no upper bound**. A separate density ceiling `||f||_infty <= M` gives `B_FI <= M/2`.

A known noiseless invertible deterministic TIA filter does not automatically reduce Fisher information. The scalar cascade product law is for independent unresolved stochastic delay stages, not generic electrical amplitude poles.

---

# Empirical grounding closure

Five full historical SPAD timing papers were supplied and checked directly. They are now cited in `section_empirical_grounding_rev9.tex`:

- Cova et al. 1989 — DOI `10.1063/1.1140324`: TCPC timing histogram, measurement-chain contributions, and sub-FWHM statistical/convolution inference.
- Lacaita & Mastrapasqua 1990 — DOI `10.1049/el:19901324`: absorption-position and detector-diameter dependence of avalanche timing.
- Lacaita et al. 1993 — DOI `10.1063/1.108870`: stochastic photon-assisted avalanche spreading as a timing-jitter mechanism.
- Spinelli et al. 1998 — DOI `10.1109/3.668769`: Gaussian-like fast IRF component, diffusion tails, and practical importance of tail suppression beyond FWHM.
- Assanelli et al. 2011 — DOI `10.1109/JQE.2010.2068038`: injection-position, discriminator-threshold, and avalanche-propagation contributions to jitter.

These papers **motivate** the physical timing structures modeled in Rev9. They do not prove or enter the assumptions of the theorem stack.

The supplemental literature audit now concludes: **no missing-paper blocker remains**. Do not continue literature mining by default.

---

# Rev8 thermodynamic repair remains mandatory

Appendix A must keep

\[
\boxed{acp\ge bqs}
\]

so that for every `R>0`,

\[
f_R-r_R=\frac{R(acp-bqs)}{RD+E}\ge0.
\]

The rare-fast construction is a hidden fast local mode with `lambda_1 ~ R` but occupation `~1/R`, so stationary activity can remain finite while conditional transient rate diverges.

---

# Novelty posture

Do not claim generic firsts for Fisher information, IRF information loss, detector timing analysis, Blackwell dominance, fixed-FWHM no-go, or universal all-detector speed limits.

Defensible contribution is the **combined theorem/resource stack** and its operational translation within the declared autonomous event-channel class.

---

# Immediate next action

**Stop adding first-paper theory, grounding, or literature by default.**

Remaining submission blockers are factual/personal:

- author name/order;
- affiliation(s);
- corresponding-author email;
- ORCID;
- truthful substantive-AI acknowledgment describing the human verification process;
- applicable funding/conflict/prior-submission declarations.

Do not submit until those are supplied. Reopen science only for a new concrete mathematical/model-class defect or a specific referee request.
