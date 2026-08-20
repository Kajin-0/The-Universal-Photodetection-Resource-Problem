# The Universal Photodetection Resource Problem

## Research question

**What physical resources are actually sufficient to bound the rate at which a photodetector can transfer information from an optical field to an electrical record, and which proposed resource sets fail by explicit counterexample?**

The project began by asking for a detector-independent sensitivity--bandwidth--temperature law. The research trail shows that this is too broad unless the detector/output class and hidden dynamical resources are specified.

The mature first-paper result is therefore a **resource-completeness theorem for one precisely defined detector class**, together with no-go results explaining why broader statements fail.

This repository is theoretical/analytical. Numerical calculations are used for validation; experiments, fabrication, procurement, and laboratory campaigns are not required next steps.

---

## First-paper theorem class

The current manuscript concerns:

- autonomous/time-translation-invariant photodetection;
- weak coherent/Poisson direct-detection intensity modulation;
- independent-event / low-overlap operation;
- one primary electrical registration per captured photon;
- retention of the complete accessible primary-event mark.

It does **not** claim a speed limit for coherent continuous pointers, externally synchronized detectors, arbitrary high-flux/history-dependent counters, nonclassical optical inputs, or every architecture called a photodetector.

---

## Exact marked-event information transfer

Per incident photon,
\[
K(dm,d\tau)=\kappa(dm)\mu_m(d\tau),
\qquad
\eta=\kappa(\mathsf M)\le1.
\]

For weak nonzero-frequency sinusoidal Poisson intensity modulation, the ideal source-normalized Fisher-information transfer is
\[
\boxed{
G(\omega)=\int_{\mathsf M}|H_m(\omega)|^2\kappa(dm).
}
\]

At exact DC the incident FI rate changes from `Phi_0/2` to `Phi_0`; the same factor changes in the output FI, so normalized transfer remains
\[
\boxed{G(0)=\eta.}
\]

Parameter-independent background addition and downstream stochastic processing cannot increase FI.

---

## Timing-resource hierarchy

### Atomic timing

Wiener's classical theorem gives
\[
\boxed{
\lim_{\Omega\to\infty}
\frac{1}{2\Omega}
\int_{-\Omega}^{\Omega}G(\omega)d\omega
=
\int\kappa(dm)\sum_j p_j(m)^2.
}
\]

This is a flat-band **average** asymptotic.

### Collision resource

For square-integrable conditional delay densities,
\[
\boxed{
\mathfrak R_2
=2\int\kappa(dm)\int f_m(t)^2dt,
\qquad
\int G(\omega)d\omega=\pi\mathfrak R_2.
}
\]

### Capture-weighted local hazard capacity

If `h_m(t)<=Lambda(m)`, define
\[
\boxed{
\mathfrak H=\int\Lambda(m)\kappa(dm),
\qquad
\mathfrak R_2\le\mathfrak H.
}
\]

A very fast branch can be negligible if its event weight is correspondingly small, so the capture-weighted resource is more informative than a global worst-case rate.

---

## Operational inverse theorem

For ordinary-frequency half-band
\[
B=\frac{\Omega}{2\pi},
\]
preserving absolute average incident-information fraction `q` requires
\[
\boxed{
q\le\eta,
\qquad
\mathfrak R_2\ge4Bq,
\qquad
\mathfrak H\ge4Bq.
}
\]

For a common per-captured-event conditional-hazard ceiling,
\[
\boxed{
\Lambda\ge\frac{4Bq}{\eta}.
}
\]

If `q=r eta`,
\[
\boxed{\Lambda\ge4Br.}
\]

---

## Main no-go results

Explicit counterexamples show that the following are not resource-complete substitutes for the timing resources above:

- deterministic latency;
- exact mean delay plus exact RMS timing jitter;
- stationary entropy production/activity/throughput without an absolute microscopic rate scale;
- detector-only timing resources when an unbounded source-synchronous clock/reference is supplied for free.

No fixed-FWHM counterexample is claimed; scalar widths such as FWHM require additional shape assumptions.

For finite-state CTMC detectors, the safe generic complete-mark-conditioned microscopic rate bound is
\[
\boxed{
q_{\max}=\max_{x\in S_{\rm pre}}
\sum_{y\ne x}W_{yx},
}
\]
the maximum **total escape rate** from pre-registration states, not merely the successful-registration edge intensity. Rev6 contains the self-contained holding-time proof of this statement.

---

## Thermodynamic bridge

The nonequilibrium gateway is described as **bidirectionally connected**, not “reversible” in the standard detailed-balance Markov-chain sense. Bidirectional support allows nonzero stationary currents and entropy production.

For the restricted finite-state gateway,
\[
\boxed{
\lambda_1
\le
\frac{\mathcal A d}{f_*}
 g^{-1}(\Sigma/f_*),
\qquad
g(z)=(1-z^{-1})\ln z.
}
\]

Rev6 explicitly connects this stationary rate bound to the independent-event theorem through an **isolated-event / low-overlap reduction**: stationary thermodynamic quantities constrain baseline microscopic rates, then one conditions on an isolated optical capture and uses the subsequent autonomous CTMC as the per-photon post-capture delay kernel. If occupancy/recovery makes capture history dependent, the independent-event information bound is not claimed.

The rare-fast counterexample proves that stationary aggregate thermodynamic quantities alone do not supply an absolute temporal scale.

---

## Publication state

Active branch:

`agent/uprp-core-theorem-round10`

Current manuscript:

`manuscript/event_resource_theorem_rev6.tex`

Rev6 is the publication candidate produced after an independent extreme adversarial review of Rev5. The review found no collapse of the core event-channel theorem stack but identified four publication-level repairs: the isolated-event thermodynamic bridge, correct nonequilibrium CTMC terminology, exact-DC normalization, and a self-contained `q_max` proof. All are now implemented.

Rev6 passed GitHub Actions generation, full LaTeX compilation, artifact upload, and source persistence. A final layout-only pass also succeeded and removed the previous large thermodynamic overfull box.

Current state/audit files:

- `docs/CURRENT_RESEARCH_STATE.md`
- `docs/MANUSCRIPT_REV6_REFEREE_REPAIR_AUDIT.md`
- `notes/RESEARCH_LOG_ROUND15.md`
- `AGENTS.md`
- `ROADMAP.md`

Steady-state CI has read-only permissions and directly compiles committed Rev6.

The first-paper science is at the **submission-package stage**. Additional foundational derivations are not the default next action.

---

## Frozen branches

Frozen for the first manuscript unless a concrete Rev6 defect requires reopening:

- HgCdTe/Kane material calculations WP17--24;
- coherent quantum-pointer resource theory;
- continuous classical/analog detector generalization;
- non-Poisson/nonclassical source extensions.

Failed conjectures and negative results remain in the repository because they establish why the final resource hierarchy has its present form.
