# AGENTS.md

## Purpose
Durable handoff for **The Universal Photodetection Resource Problem (UPRP)**. The repository, not chat history, is authoritative.

Research is analytical/theoretical only. Numerical work is allowed for validation. Do not make experiments, fabrication, procurement, or laboratory campaigns necessary next steps.

## Working branch
`agent/uprp-core-theorem-round10`

## Read first
1. `docs/CURRENT_RESEARCH_STATE.md`
2. `manuscript/event_resource_theorem_rev5.tex`
3. `docs/MANUSCRIPT_REV5_FINAL_AUDIT.md`
4. `notes/RESEARCH_LOG_ROUND14.md`
5. `notes/WP35_MARK_CONDITIONED_MARKOV_RATE_CORRECTION.md`
6. `notes/WP34_MINIMUM_TIMING_RESOURCE_COST_THEOREM.md`
7. `notes/WP32_GENERAL_MARKED_POISSON_EVENT_KERNEL_THEOREM.md`
8. `notes/WP33_EXACT_FIXED_MEAN_VARIANCE_JITTER_NO_GO.md`
9. `notes/WP29_THERMODYNAMIC_BRIDGE_TO_REGISTRATION_INTENSITY.md`
10. `notes/WP30_WIENER_ATOMIC_DELAY_INFORMATION_THEOREM.md`
11. `docs/NOVELTY_AUDIT_ROUND5_EVENT_THEOREM_STACK.md`

**Freeze:** HgCdTe/Kane WP17–24, coherent-pointer, continuous-analog, and non-Poisson/nonclassical branches unless a concrete referee-level defect requires reopening them.

---

# Publication state

The current first-paper source is

`manuscript/event_resource_theorem_rev5.tex`.

Rev5 is the WP35-corrected successor to fully verified Rev4. The final generated Rev5 source passed GitHub Actions generation, full LaTeX compilation, and artifact upload. The committed Rev5 blob is byte-for-byte identical to the CI artifact (`git blob SHA 23ad1c27be95bdbf79d88176d438c8a305f844f0`).

Steady-state CI is clean and read-only:

`.github/workflows/manuscript-check.yml`

It compiles the **committed Rev5 directly** and uploads TeX/PDF artifacts. There are no self-commit or issue-comment side effects.

The final claim/citation audit passed after tightening the Dechant comparison and applying WP35. The project is at the **submission-package stage**.

---

# First-paper theorem class

The theorem concerns autonomous/time-translation-invariant, independent-event, one-primary-registration photodetection under weak coherent/Poisson direct-detection intensity modulation, retaining the complete accessible primary-event mark.

Do not describe it as a universal all-detector speed limit.

Per incident photon,
\[
K(dm,d\tau)=\kappa(dm)\mu_m(d\tau),
\qquad
\eta=\kappa(\mathsf M)\le1.
\]

Exact ideal source-normalized FI transfer:
\[
\boxed{G(\omega)=\int_{\mathsf M}|H_m(\omega)|^2\kappa(dm).}
\]

Parameter-independent background/downstream processing cannot increase this FI.

---

# Timing-resource hierarchy

## Atomic timing
\[
\boxed{
\lim_{\Omega\to\infty}\frac1{2\Omega}
\int_{-\Omega}^{\Omega}G(\omega)d\omega
=
\int\kappa(dm)\sum_jp_j(m)^2.
}
\]
This is a flat-band **average** asymptotic; do not claim general pointwise decay for singular continuous delay measures.

## Collision resource
\[
\boxed{
\mathfrak R_2=2\int\kappa(dm)\int f_m(t)^2dt,
\qquad
\int G(\omega)d\omega=\pi\mathfrak R_2.
}
\]

## Capture-weighted local hazard capacity
If `h_m(t)<=Lambda(m)`,
\[
\boxed{
\mathfrak H=\int\Lambda(m)\kappa(dm),
\qquad
\mathfrak R_2\le\mathfrak H.
}
\]

The capture-weighted `mathfrak H` is preferred to a global worst-case rate.

---

# WP34 inverse cost
For a flat task with ordinary-frequency half-band
\[
B=\frac{\Omega}{2\pi},
\]
a target absolute average transfer `q` requires
\[
\boxed{
q\le\eta,
\qquad
\mathfrak R_2\ge4Bq,
\qquad
\mathfrak H\ge4Bq.
}
\]

For a common markwise hazard ceiling,
\[
\boxed{\Lambda\ge\frac{4Bq}{\eta}.}
\]
For `q=r eta`,
\[
\boxed{\Lambda\ge4Br.}
\]

---

# WP33 exact jitter no-go
For any prescribed mean `mu0>0` and variance `sigma^2>0`, there is a smooth delay family satisfying both exactly for every selected family member while `|H_D(omega)|^2 -> 1` uniformly on any prescribed finite band.

Therefore exact mean delay plus exact RMS jitter do not bound information bandwidth.

Do not claim an arbitrary fixed-exact-FWHM theorem.

---

# WP35 Markov-rate correction
The successful-registration edge intensity alone does not generically bound the complete mark-conditioned delay hazard when other exits compete.

For finite-state CTMC pre-registration state set `S_pre`, define
\[
q_x=\sum_{y\ne x}W_{yx},
\qquad
\boxed{q_{\max}=\max_{x\in S_{\rm pre}}q_x.}
\]

Provided the accessible mark does not independently expose realized pre-registration holding times,
\[
\boxed{h_D(t\mid M)\le q_{\max}.}
\]

The generic quantum-jump operator-norm sentence was removed from Rev5 and is deferred to a separate quantum-trajectory branch.

WP29 is already consistent because it uses the gateway's **total first-exit rate** `lambda1`.

---

# Other no-go/scope boundaries

- A free source-synchronous temporal reference can preserve arrival-phase FI despite slow final registration; autonomy is therefore a real resource assumption.
- Stationary EPR/activity/throughput do not supply an absolute microscopic time scale without a local rate/coupling resource.
- Deterministic latency is not information loss.
- Multiple independent pre-primary timing copies are an additional multiplicity resource.
- High-flux/history-dependent capture requires trajectory-level treatment.

---

# Novelty posture
Do not claim first information-theoretic detector timing analysis, first IRF-information result, first sensitivity-bandwidth tradeoff, generic finite-frequency response/noise novelty, or a universal all-detector speed limit.

Defensible contribution:

> A resource-completeness theorem for source-modulation information transfer in autonomous marked photodetection event channels, combining the exact marked-event transfer, atomic timing residue, collision spectral budget, capture-weighted local-hazard resource, inverse timing-resource cost, and explicit no-go/repair results for low-order jitter moments, free synchronous control, and aggregate stationary thermodynamics.

Novelty is strongest in the **combined theorem stack**, not the classical mathematical ingredients individually.

---

# Immediate next action
Prepare the submission package / journal-positioning materials from committed Rev5. Do not reopen foundational theory merely to enlarge the first paper.

Status vocabulary: **PROVED**, **VERIFIED**, **CONJECTURE**, **COUNTEREXAMPLE**, **OPEN**, **BLOCKED**, **REJECTED**.
