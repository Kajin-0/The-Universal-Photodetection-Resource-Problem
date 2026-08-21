# Research Roadmap — Rev9 Submission Freeze

**Updated:** 2026-08-20

## Guiding principle

The autonomous marked-event first paper has passed:

- theorem construction;
- hostile review and model-class repair;
- weak-waveform significance upgrade;
- proof hardening;
- Rev8 thermodynamic Appendix repair;
- Rev9 translational grounding for detector physicists;
- full LaTeX/bibliography/cross-reference validation;
- visual inspection of all newly affected pages.

**Do not perform another broad first-paper revision unless a new concrete defect is identified.**

Primary target: **Physical Review Applied — Regular Article**.

---

# Closed scientific gates

## G0 — Exact autonomous marked-event transfer
**PASSED**

\[
G(\omega)=\int_{\mathsf M}|H_m(\omega)|^2\kappa(dm).
\]

Exact DC convention repaired and explicit.

## G1 — Complete local weak-waveform Fisher operator
**PASSED**

\[
[F_{\rm out}]_{ab}
=\frac{\Phi_0}{2\pi}\int G(\omega)S_a^*(\omega)S_b(\omega)d\omega.
\]

## G2 — Universal local Fisher detector ordering
**PASSED**

Pointwise `G_A >= G_B` iff detector A Fisher-dominates B for every admitted finite weak-waveform task.

## G3 — Exact band-subspace guarantee
**PASSED**

Worst-case retention over a compact band equals `min G` on that band.

## G4 — Timing-resource hierarchy
**PASSED**

Atomic residue, collision resource `R_2`, hazard resource `H`, equivalent Fisher bandwidth, and inverse cost theorem all closed.

## G5 — Conventional-jitter no-go
**PASSED**

Exact fixed mean + exact variance do not bound finite temporal information bandwidth. No fixed-FWHM theorem is claimed.

## G6 — Clock/control no-go
**PASSED**

A free source-synchronous reference is a separate resource.

## G7 — CTMC microscopic rate repair
**PASSED**

The sufficient finite-state hazard ceiling is the maximum total first-exit rate from relevant pre-registration states, not merely a successful-registration edge rate.

## G8 — Thermodynamic bridge and rare-fast counterexample
**PASSED**

Rev8 enforces `acp >= bqs`, defines the directed one-way activity convention, and preserves the isolated-event/low-overlap bridge.

---

# Rev9 translational gate

## T1 — Canonical detector timing-law library
**PASSED**

Closed forms supplied for:

- Gaussian timing error;
- exponential delay;
- uniform finite-support delay;
- serial Erlang stages;
- Gaussian--exponential convolution.

## T2 — Existing-data estimator
**PASSED**

For equal histogram bins,

\[
B_{\rm FI}^{(\Delta t)}
=\frac{1}{2\Delta t}\sum_i p_i^2.
\]

Finite-count unbiased pair estimator:

\[
\widehat B_{\rm FI,U}^{(\Delta t)}
=\frac{1}{2\Delta t}\frac{\sum_i n_i(n_i-1)}{N(N-1)}.
\]

Finite binning is a lower/coarse-grained estimate of continuous `B_FI`.

## T3 — Physical support clarification
**PASSED**

Finite support of length `T` gives the **lower** bound

\[
B_{\rm FI}\ge\frac1{2T},
\]

not an upper speed limit. There is no support-only upper bound.

## T4 — Mark resource gradient
**PASSED**

Fine accessible event marks can preserve more FI than discarded/coarse marks. Perfect primary latency side information gives `G=eta`; a downstream TDC cannot manufacture information lost before the primary record.

## T5 — Preamplifier/readout interpretation
**PASSED**

The cascade product law applies to independent stochastic delay stages. It must not be misapplied to a deterministic invertible TIA RC pole without explicit downstream noise/coarse-graining/noninvertibility.

## T6 — DC pedagogical note
**PASSED**

`G(0)=eta` remains the correct normalized ratio. The factor-of-two distinction is only in absolute FI normalization.

## T7 — Thermodynamic engineering analogy
**PASSED**

The rare-fast CTMC is interpreted as a high-rate, low-duty-cycle hidden transient mode without making a false circuit high-pass identification.

---

# Mechanical validation

Generated Rev9 source is deterministic and hash-pinned.

Canonical build:

- 30 pages;
- PDF SHA-256 `2d8c93a98840d303a1f32cc3c67cd4c2c6d46a4010e440317691cae09df1f0cc`.

PRApplied build:

- 30 pages;
- PDF SHA-256 `5e4c17e7a7e3a8f26172e770b43d9391f88d20e0252cfdc9425e530cbfec9111`;
- final ZIP SHA-256 `c612899d536f4653e872f179f8b9fbea61264ed37e3120ac68fb1813ac5b913d`.

Steady-state CI is read-only and compiles generated/hash-checked Rev9.

---

# Remaining submission work

Only factual/personal items remain:

1. author name/order;
2. affiliation(s);
3. corresponding-author email;
4. ORCID;
5. truthful substantive-AI acknowledgment describing the author's actual verification;
6. applicable funding/conflict/prior-submission disclosures;
7. optional referee suggestions/exclusions after conflict review;
8. one final metadata-stage compile/visual inspection.

---

# Explicitly deferred to later papers

Do not add to the first paper absent a concrete referee demand:

- high-flux/history-dependent detection;
- arbitrary semi-Markov detectors;
- coherent continuous quantum pointers;
- nonclassical-light/QFI extensions;
- general Shannon-capacity theory;
- material-specific detector optimization.

Potential second-paper directions remain open, but the Rev9 first paper should now be treated as scientifically frozen.
