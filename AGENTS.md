# AGENTS.md

## Purpose
Durable handoff for **The Universal Photodetection Resource Problem (UPRP)**. The repository, not chat history, is authoritative.

Research is analytical/theoretical only. Numerical work may be used for validation. Do not make experiments, fabrication, procurement, or laboratory campaigns necessary next steps.

## Working branch
`agent/uprp-core-theorem-round10`

## Read first
1. `docs/CURRENT_RESEARCH_STATE.md`
2. `manuscript/event_resource_theorem_rev6.tex`
3. `docs/MANUSCRIPT_REV6_REFEREE_REPAIR_AUDIT.md`
4. `notes/RESEARCH_LOG_ROUND15.md`
5. `notes/WP35_MARK_CONDITIONED_MARKOV_RATE_CORRECTION.md`
6. `notes/WP34_MINIMUM_TIMING_RESOURCE_COST_THEOREM.md`
7. `notes/WP32_GENERAL_MARKED_POISSON_EVENT_KERNEL_THEOREM.md`
8. `notes/WP33_EXACT_FIXED_MEAN_VARIANCE_JITTER_NO_GO.md`
9. `notes/WP29_THERMODYNAMIC_BRIDGE_TO_REGISTRATION_INTENSITY.md`
10. `notes/WP30_WIENER_ATOMIC_DELAY_INFORMATION_THEOREM.md`
11. `docs/NOVELTY_AUDIT_ROUND5_EVENT_THEOREM_STACK.md`

**Freeze:** HgCdTe/Kane WP17–24, coherent-pointer, continuous-analog, and non-Poisson/nonclassical branches unless a concrete referee-level defect in Rev6 requires reopening them.

---

# Publication state

Current first-paper source:

`manuscript/event_resource_theorem_rev6.tex`

Rev6 is the hostile-referee-hardened successor to Rev5. It passed GitHub Actions generation, full LaTeX compilation, artifact upload, and source persistence. The final layout pass also passed and persisted the source.

Steady-state CI:

`.github/workflows/manuscript-check.yml`

It has **read-only contents permission**, compiles committed Rev6 directly, and uploads the Rev6 PDF/TeX plus versioned appendix. There are no self-commit or issue-comment side effects.

Rev5 is historical and should not be edited retroactively.

---

# First-paper theorem class

The theorem concerns autonomous/time-translation-invariant, independent-event, low-overlap, one-primary-registration photodetection under weak coherent/Poisson direct-detection intensity modulation, retaining the complete accessible primary-event mark.

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

At exact DC, Eq. for incident FI rate `Phi_0/2` is not used literally: the DC incident rate is `Phi_0`, with the same factor change in output FI, so normalized transfer remains `G(0)=eta`.

Parameter-independent background/downstream processing cannot increase FI.

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
This is a flat-band **average** asymptotic; do not claim generic pointwise Fourier decay for singular continuous measures.

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

# WP34 inverse resource cost
For ordinary-frequency half-band
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

# WP33 conventional-jitter no-go
For any prescribed mean `mu0>0` and variance `sigma^2>0`, a smooth delay family can satisfy both exactly while `|H_D(omega)|^2 -> 1` uniformly on any prescribed finite band.

Therefore exact mean delay plus exact RMS jitter do not bound information bandwidth.

Rev6 explicitly does **not** claim a fixed-FWHM counterexample. Scalar widths such as FWHM require additional shape assumptions before functioning as resource summaries.

---

# WP35 / finite-state CTMC completion

The successful-registration edge intensity alone does not generically bound the complete-mark-conditioned delay hazard when competing exits exist.

For pre-registration state `x`,
\[
\lambda_x=\sum_{y\ne x}W_{yx},
\qquad
\boxed{q_{\max}=\max_{x\in S_{\rm pre}}\lambda_x.}
\]

Rev6 now contains the self-contained proof: the first holding time is `Exp(lambda_x)` and independent of exit destination/subsequent trajectory; under the mark restriction,
\[
D\mid(M,x)=T_x+Y_{M,x},\qquad Y_{M,x}\ge0,
\]
so `f <= lambda_x S`, hence
\[
\boxed{h_D(t\mid M,x)\le\lambda_x\le q_{\max}.}
\]
Mixing over the initial state preserves the `q_max` ceiling.

The generic quantum-jump operator-norm extension remains deferred.

---

# Rev6 thermodynamic model-class bridge

Use **bidirectionally connected**, not “reversible,” for the nonequilibrium CTMC gateway/counterexample. Here bidirectionally connected means reverse-transition support; it does not mean stationary detailed balance.

The stationary thermodynamic bound is applied to the event theorem only through an explicit isolated-event reduction:

1. stationary baseline EPR/activity/traffic constrain microscopic rates;
2. condition on one isolated optical capture placing the gateway in state 1;
3. the post-capture autonomous CTMC generates the per-photon delay kernel;
4. require low overlap so occupancy/recovery do not make capture or the kernel history dependent.

If capture/recovery is history dependent, the independent-event kernel and thermodynamic information bound are not claimed.

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

The absolute microscopic rate `d` remains indispensable. The rare-fast family shows stationary thermodynamic aggregates alone do not fix the temporal scale.

---

# Other scope/no-go boundaries

- A free source-synchronous clock can preserve arrival-phase FI despite arbitrarily slow final registration; autonomy is a real resource assumption.
- Deterministic latency is not information loss.
- Multiple independent pre-primary timing copies are an additional multiplicity resource.
- High-flux/history-dependent capture requires trajectory-level treatment.
- Nonclassical/phase-sensitive sources need a different input-information treatment.

---

# Novelty posture
Do not claim first information-theoretic detector timing analysis, first IRF-information result, first sensitivity-bandwidth tradeoff, generic finite-frequency response/noise novelty, or a universal all-detector speed limit.

Defensible contribution:

> A resource-completeness theorem for source-modulation information transfer in autonomous marked photodetection event channels, combining exact marked-event transfer, atomic timing residue, collision spectral budget, capture-weighted local-hazard resource, inverse timing-resource cost, and explicit no-go/repair results for low-order timing moments, free synchronous control, and aggregate stationary thermodynamics.

Novelty is strongest in the **combined theorem stack**, not the classical ingredients individually.

---

# Immediate next action
Prepare the submission package / journal-positioning materials from committed Rev6. Do not reopen foundational theory merely to enlarge the paper.

Status vocabulary: **PROVED**, **VERIFIED**, **CONJECTURE**, **COUNTEREXAMPLE**, **OPEN**, **BLOCKED**, **REJECTED**.
