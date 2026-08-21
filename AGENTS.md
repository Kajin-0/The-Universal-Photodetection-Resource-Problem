# AGENTS.md

## Purpose

Durable handoff for **The Universal Photodetection Resource Problem (UPRP)**. The repository, not chat history, is authoritative.

Research is analytical/theoretical only. Numerical work may be used for validation. Do not make experiments, fabrication, procurement, or laboratory campaigns necessary next steps.

Active branch:

`agent/uprp-core-theorem-round10`

## Read first

1. `docs/CURRENT_RESEARCH_STATE.md`
2. `notes/RESEARCH_LOG_ROUND18_TRANSLATIONAL_GROUNDING.md`
3. `submission/PRAPPLIED_PACKAGE_VALIDATION_REV9.md`
4. `submission/SUBMISSION_PACKAGE_CHECKLIST_REV9.md`
5. `manuscript/section_practical_grounding_rev9.tex`
6. `manuscript/apply_rev9_grounding.py`
7. `manuscript/REV9_SHA256SUMS.txt`
8. `notes/RESEARCH_LOG_ROUND17.md`
9. `notes/RESEARCH_LOG_ROUND16.md`
10. `notes/WP36_COMPLETE_WEAK_WAVEFORM_FISHER_OPERATOR.md`
11. `notes/WP36A_BAND_SUBSPACE_FISHER_GUARANTEE.md`
12. `docs/MANUSCRIPT_REV6_REFEREE_REPAIR_AUDIT.md`

---

# Current publication state — Rev9

**Rev9 is the preferred first-paper submission candidate.**

The version chain is deliberately reproducible:

1. frozen theorem source: `manuscript/event_resource_theorem_rev7.tex`;
2. Rev8 hostile-review repair: `manuscript/apply_rev8_referee_surgical.py`;
3. Rev9 translational grounding: `manuscript/apply_rev9_grounding.py`;
4. expected generated-source hashes: `manuscript/REV8_SHA256SUMS.txt` and `manuscript/REV9_SHA256SUMS.txt`.

Rev9 does **not** broaden the theorem class. It keeps the Rev8 theorem stack intact and adds operational translation for detector physicists.

Canonical generated Rev9 hashes:

- `event_resource_theorem_rev9.tex`: `79d0da661ba394b6064a73103cce4db157f634d2d4b5d47a674c7cd1552af6fc`;
- `section_practical_grounding_rev9.tex`: `b4702642705b01ef811e95f5a3d2d0686bb951122c337fd438d0b53fa0a18c3f`;
- inherited repaired Appendix: `f9afbdf7e0fd6cc1b57a3a4e00197148e907fc9ed7691a7f9dd42106e16ba665`.

Independent full Rev9 build:

- 30 pages;
- PDF SHA-256 `2d8c93a98840d303a1f32cc3c67cd4c2c6d46a4010e440317691cae09df1f0cc`;
- no undefined citations/references;
- only inherited material overfull warning: approximately `2.45667 pt` around `timing-concentration` in Appendix A;
- new pages visually inspected.

PRApplied copy:

- 30 pages;
- PDF SHA-256 `5e4c17e7a7e3a8f26172e770b43d9391f88d20e0252cfdc9425e530cbfec9111`;
- final package ZIP SHA-256 `c612899d536f4653e872f179f8b9fbea61264ed37e3120ac68fb1813ac5b913d`.

Steady-state CI is read-only. It generates Rev8, verifies Rev8 hashes, generates Rev9, verifies Rev9 hashes, compiles Rev9, and uploads the artifact. It performs no self-commit or source mutation.

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

At exact DC, the absolute incident FI rate is `Phi_0`, not `Phi_0/2`, but normalized transfer remains

\[
\boxed{G(0)=\eta.}
\]

Rev9 explicitly warns: do **not** multiply `G(0)` by two. The factor of two matters only when converting normalized transfer to absolute FI rate.

---

# Complete weak-waveform operator

For admissible finite-dimensional real weak perturbations,

\[
\boxed{
[F_{\rm out}]_{ab}
=\frac{\Phi_0}{2\pi}\int G(\omega)S_a^*(\omega)S_b(\omega)d\omega.
}
\]

Thus `G` is the spectral multiplier of the complete local weak-waveform Fisher operator within the declared model.

For two detectors,

\[
\boxed{
G_A(\omega)\ge G_B(\omega)\ \forall\omega
\iff
F_A\succeq F_B
\text{ for every admissible finite weak-waveform task.}
}
\]

This is local Fisher ordering, **not** generic Blackwell dominance.

For a compact band,

\[
\boxed{
\inf_{\operatorname{supp}S\subset[-\Omega,\Omega]}
\frac{F_{\rm out}}{F_{\rm in}}
=\min_{|\omega|\le\Omega}G(\omega).
}
\]

---

# Timing-resource hierarchy

Atomic timing residue:

\[
\lim_{\Omega\to\infty}\frac1{2\Omega}\int_{-\Omega}^{\Omega}G(\omega)d\omega
=\int\kappa(dm)\sum_jp_j(m)^2.
\]

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
B_{\rm FI}=\frac{\mathfrak R_2}{4\eta}
\le\frac{\mathfrak H}{4\eta}.
}
\]

A common hazard ceiling gives `B_FI <= Lambda/4`.

Minimum resource cost over ordinary-frequency half-band `B`:

\[
\boxed{
\mathfrak R_2\ge4Bq,
\qquad
\mathfrak H\ge4Bq.
}
\]

---

# Rev9 translational grounding — important formulas

For a **single unresolved mark**,

\[
\boxed{B_{\rm FI}=\frac12\int f(t)^2dt.}
\]

Canonical examples:

- Gaussian timing-error idealization: `B_FI = 1/(4 sqrt(pi) sigma)`;
- exponential wait: `B_FI=Lambda/4`, `f_3dB=Lambda/(2 pi)`, hence `B_FI/f_3dB=pi/2`;
- uniform delay on `[0,T]`: `G/eta=sinc^2(omega T/2)`, `B_FI=1/(2T)`;
- Gaussian timing error convolved with exponential wait:
  `B_FI=(Lambda/4) exp(Lambda^2 sigma^2) erfc(Lambda sigma)`.

## Histogram estimator

For equal bins `Delta t` and conditional-on-capture bin probabilities `p_i`,

\[
\boxed{
B_{\rm FI}^{(\Delta t)}=\frac{1}{2\Delta t}\sum_i p_i^2.
}
\]

For counts `n_i`, `N=sum_i n_i`, the unbiased finite-count estimator of the **binned** quantity is

\[
\boxed{
\widehat B_{\rm FI,U}^{(\Delta t)}
=\frac{1}{2\Delta t}\frac{\sum_i n_i(n_i-1)}{N(N-1)}.
}
\]

Finite binning obeys

\[
\boxed{B_{\rm FI}^{(\Delta t)}\le B_{\rm FI}.}
\]

## Finite support — do not reverse this inequality

If normalized `f` is supported on an interval of length `T`,

\[
\boxed{B_{\rm FI}\ge\frac1{2T}.}
\]

Finite support alone gives **no upper bound** on `B_FI`. An independent density ceiling `||f||_infty <= M` gives `B_FI <= M/2`.

## Mark gradient

Discarding a fine mark can only reduce transfer:

\[
G_{\rm no\ mark}\le G_{\rm fine}.
\]

If an accessible primary-event mark exactly identifies the realized latency, then `G=eta` at all frequency. A downstream TDC does **not** create missing pre-registration information merely by digitizing the same delayed event more finely.

## Preamplifier / cascade caveat

The product law applies to independent unresolved **stochastic delay stages**:

\[
G_{\rm total}=G_{\rm det}|H_a|^2.
\]

Do **not** multiply by a deterministic TIA transfer function merely because it has an RC pole. A known noiseless invertible filter does not itself reduce FI. Information loss requires downstream noise, finite sampling/bandwidth, saturation, thresholding, noninvertibility, unresolved stochastic latency, or another explicit observation limitation.

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

The stationary one-way activity convention is total directed stationary jump traffic.

The rare-fast construction is interpreted in Rev9 as a hidden fast local mode with `lambda_1 ~ R` but occupation `~1/R`, so time-averaged activity can remain finite while the conditional transient rate diverges.

---

# Conventional-jitter / clock / thermodynamic no-gos

- exact mean delay and exact RMS jitter do not bound finite temporal information bandwidth;
- no fixed-FWHM theorem is claimed;
- a free source-synchronous clock is an independent resource and can defeat detector-only timing bounds;
- stationary aggregate activity/EPR/throughput alone do not set the temporal scale without an absolute microscopic rate;
- high-flux/history-dependent capture lies outside the independent-event kernel.

---

# Novelty posture

Do not claim:

- first information-theoretic detector timing analysis;
- first IRF information-loss result;
- first generic FI transfer function;
- generic Blackwell dominance;
- arbitrary fixed-FWHM no-go;
- universal all-detector speed limit;
- deterministic TIA bandwidth as an automatic FI-loss factor.

Defensible contribution:

> A temporal-information resource theory for autonomous marked photodetection event channels in which the exact marked-delay spectrum is the complete local weak-waveform Fisher multiplier; pointwise spectral ordering completely characterizes local weak-waveform Fisher dominance; collision and hazard resources yield exact/inverse bandwidth laws; and the framework is now directly computable from canonical timing laws or existing digitized IRF histograms while explicit no-go results delimit what ordinary timing, clock, thermodynamic, support, and readout summaries can actually imply.

---

# Immediate next action

**Stop adding first-paper theory or “grounding” by default.**

The remaining submission blockers are factual/personal:

- author name/order;
- affiliation;
- corresponding-author email;
- ORCID;
- truthful substantive-AI disclosure describing the human verification process;
- applicable funding/conflict/prior-submission declarations.

Do not submit until those are supplied. Reopen the scientific manuscript only for a new concrete defect.
