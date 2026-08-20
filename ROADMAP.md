# Research Roadmap — Submission Package Phase

**Updated:** 2026-08-20

## Guiding principle
The autonomous marked-event branch has passed its scientific and manuscript-hardening gates. The first-paper task is now **submission packaging and journal positioning**, not additional foundational derivation.

Do not reopen material-specific, coherent-pointer, analog-detector, or non-Poisson branches unless a concrete referee-level defect in Rev5 requires it.

---

# Closed theorem stack

## E0 — Exact marked-event kernel
**PROVED**

\[
K(dm,d\tau)=\kappa(dm)\mu_m(d\tau),
\qquad
G(\omega)=\int_{\mathsf M}|H_m(\omega)|^2\kappa(dm).
\]

## E1 — Atomic high-band residue
**PROVED**

\[
\boxed{
\lim_{\Omega\to\infty}\frac1{2\Omega}
\int_{-\Omega}^{\Omega}G(\omega)d\omega
=
\int\kappa(dm)\sum_jp_j(m)^2.
}
\]

## E2 — Timing-collision spectral resource
**PROVED**

\[
\boxed{
\mathfrak R_2=2\int\kappa(dm)\int f_m^2dt,
\qquad
\int G(\omega)d\omega=\pi\mathfrak R_2.
}
\]

## E3 — Capture-weighted local-hazard resource
**PROVED; WP35-CORRECTED MICROSCOPIC INTERPRETATION**

\[
\boxed{
\mathfrak H=\int\Lambda(m)\kappa(dm),
\qquad
\mathfrak R_2\le\mathfrak H.
}
\]

For a finite-state CTMC, the safe generic uniform bound after complete mark conditioning is
\[
\boxed{
q_{\max}=\max_{x\in S_{\rm pre}}\sum_{y\ne x}W_{yx},
}
\]
provided the mark does not independently expose realized pre-registration holding times.

The old registration-edge-only statement is rejected. The generic quantum-jump operator-norm extension is deferred.

## E4 — Operational inverse cost
**PROVED**

For ordinary-frequency half-band `B=Omega/(2pi)` and required absolute average transfer `q`,
\[
\boxed{
q\le\eta,
\qquad
\mathfrak R_2\ge4Bq,
\qquad
\mathfrak H\ge4Bq.
}
\]

For a common per-captured-event hazard ceiling,
\[
\boxed{\Lambda\ge4Bq/\eta.}
\]
For relative retention `q=r eta`,
\[
\boxed{\Lambda\ge4Br.}
\]

## E5 — No-go/repair layer
**PROVED FOR MANUSCRIPT CLAIMS**

- exact mean + exact RMS jitter do not bound information bandwidth;
- a free synchronous clock/reference defeats detector-only timing bounds;
- stationary EPR/activity/throughput do not supply an absolute microscopic time scale;
- deterministic latency is not information loss;
- parameter-independent downstream processing cannot improve the primary-record FI.

---

# Thermodynamic completion
**PROVED FOR THE RESTRICTED GATEWAY CLASS**

For the finite-state time-homogeneous reversible optical gateway,
\[
\boxed{
\lambda_1\le
\Lambda_*
=\frac{\mathcal A d}{f_*}g^{-1}(\Sigma/f_*),
\qquad
g(z)=(1-z^{-1})\ln z.
}
\]

`lambda1` is the **total first-exit rate**, so WP29 is already consistent with WP35. The absolute microscopic reverse rate `d` remains indispensable.

---

# Publication state

## Rev4
`manuscript/event_resource_theorem_rev4.tex`

**Historical build-verified revision.** Contains the later-corrected WP35 microscopic wording.

## Rev5
`manuscript/event_resource_theorem_rev5.tex`

**CURRENT FIRST-PAPER SOURCE — COMMITTED + BUILD VERIFIED.**

The committed Git blob SHA

`23ad1c27be95bdbf79d88176d438c8a305f844f0`

matches the exact TeX source retrieved from the successful CI artifact.

Rev5 contains:

1. the WP35 total-pre-registration-escape-rate correction;
2. removal of the generic quantum-jump sentence;
3. explicit prose references to both theorem figures;
4. the versioned hierarchy figure with local-rate wording;
5. conservative finite-frequency prior-work wording after the final citation audit.

No central theorem or numerical constant changed.

Steady-state CI now has read-only permissions and directly compiles committed Rev5. There are no self-commit or issue-comment side effects.

---

# Closed publication gates

## P1 — Rev5 mechanical verification
**PASSED.** Generation, full LaTeX compilation, and artifact upload succeeded for the final Rev5 transformer state.

## P2 — Final claim/reference audit
**PASSED.** Prior-work claims remain conservative; novelty is reserved for the combined resource-completeness stack.

## P3 — Source persistence / clean CI
**PASSED.** Verified source is committed and byte-matched to the CI artifact; CI directly compiles committed Rev5.

---

# Next gate — Submission package

Prepare the submission-ready package and journal positioning. This may include:

- final author/affiliation metadata;
- title/abstract polish only if scientifically neutral;
- journal-format/source cleanliness;
- cover letter and concise novelty statement;
- final package inventory and reproducibility check.

Do not use submission packaging as a pretext to reopen frozen research branches.

---

# Frozen branches

- HgCdTe/Kane WP17–24;
- coherent quantum pointers;
- continuous classical/analog detector generalization;
- non-Poisson/nonclassical source extensions.
