# Research Roadmap — Rev6 Submission Package Phase

**Updated:** 2026-08-20

## Guiding principle

The autonomous marked-event branch has passed its theorem, hostile-review, and manuscript-hardening gates. The first-paper task is now **submission packaging and journal positioning**, not additional foundational derivation.

Do not reopen material-specific, coherent-pointer, analog-detector, or non-Poisson branches unless a concrete defect in Rev6 requires it.

---

# Closed theorem stack

## E0 — Exact marked-event kernel
**PROVED**

\[
K(dm,d\tau)=\kappa(dm)\mu_m(d\tau),
\qquad
G(\omega)=\int_{\mathsf M}|H_m(\omega)|^2\kappa(dm).
\]

Exact DC is handled separately in Rev6; normalized transfer remains `G(0)=eta`.

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
**PROVED; WP35 + REV6 SELF-CONTAINED CTMC COMPLETION**

\[
\boxed{
\mathfrak H=\int\Lambda(m)\kappa(dm),
\qquad
\mathfrak R_2\le\mathfrak H.
}
\]

For finite-state CTMC pre-registration states,
\[
\boxed{
q_{\max}=\max_{x\in S_{\rm pre}}
\sum_{y\ne x}W_{yx}.
}
\]

Rev6 proves that `q_max` bounds the complete-mark-conditioned hazard under the stated holding-time mark restriction. The old successful-registration-edge-only statement is rejected. The generic quantum-jump extension remains deferred.

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
- no fixed-FWHM counterexample is claimed;
- free synchronous temporal reference defeats detector-only timing bounds;
- stationary EPR/activity/throughput do not provide an absolute microscopic time scale;
- deterministic latency is not information loss;
- parameter-independent downstream processing cannot improve primary-record FI.

---

# Thermodynamic completion

**PROVED FOR THE RESTRICTED BIDIRECTIONALLY CONNECTED GATEWAY CLASS, WITH EXPLICIT LOW-OVERLAP BRIDGE**

Use **bidirectionally connected**, not “reversible,” for the nonequilibrium CTMC network. Reverse-transition support does not imply detailed balance.

For the restricted gateway,
\[
\boxed{
\lambda_1\le
\Lambda_*
=\frac{\mathcal A d}{f_*}g^{-1}(\Sigma/f_*),
\qquad
g(z)=(1-z^{-1})\ln z.
}
\]

Rev6 explicitly states that stationary baseline thermodynamic quantities constrain microscopic rates, while application to Theorem 1 conditions on an isolated capture and requires the low-overlap regime so capture/recovery do not become history dependent.

If capture/recovery is history dependent, the independent-event theorem is not applied.

The absolute reverse rate `d` remains indispensable.

---

# Publication state

## Rev4
Historical build-verified revision; contains later-corrected WP35 wording.

## Rev5
Historical WP35-corrected manuscript; passed final claim/citation audit but was superseded by hostile-review Rev6.

## Rev6
`manuscript/event_resource_theorem_rev6.tex`

**CURRENT FIRST-PAPER SOURCE — HOSTILE-REVIEW REPAIRED + BUILD VERIFIED + PERSISTED.**

Rev6 adds only publication-hardening changes:

1. exact-DC source-FI clarification;
2. self-contained `q_max` CTMC hazard proof;
3. conservative FWHM wording;
4. “bidirectionally connected” terminology replacing probabilistic “reversible” language;
5. explicit isolated-event/low-overlap bridge between stationary thermodynamic accounting and the independent-event theorem;
6. versioned rare-fast appendix terminology;
7. layout-only split of the long thermodynamic boxed conclusion.

No central theorem or numerical coefficient changed.

Key verification records:

- `docs/MANUSCRIPT_REV6_REFEREE_REPAIR_AUDIT.md`
- `notes/RESEARCH_LOG_ROUND15.md`

Steady-state CI has read-only permissions and directly compiles committed Rev6.

---

# Closed publication gates

## P1 — Core theorem audit
**PASSED.** Independent hostile review found no collapse of the exact event-transfer, Wiener, Parseval, hazard-collision, jitter no-go, clock no-go, thermodynamic algebra, or rare-fast results.

## P2 — Referee model-class/terminology repairs
**PASSED.** All four targeted corrections are present in Rev6.

## P3 — Rev6 mechanical verification
**PASSED.** Full LaTeX compilation and artifact upload succeeded; final layout source persisted successfully.

## P4 — Clean CI
**PASSED.** Read-only direct compilation; no self-commit or issue-comment side effects.

---

# Next gate — Submission package

Prepare the submission-ready package and journal positioning. This may include:

- final author/affiliation metadata;
- journal-format/source cleanup;
- cover letter and concise novelty statement;
- final package inventory / reproducibility check;
- title/abstract polish only if scientifically neutral.

Do not use submission packaging as a pretext to reopen frozen research branches.

---

# Frozen branches

- HgCdTe/Kane WP17–24;
- coherent quantum pointers;
- continuous classical/analog detector generalization;
- non-Poisson/nonclassical source extensions.
