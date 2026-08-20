# The Universal Photodetection Resource Problem

## Research question

**What physical resources are actually sufficient to bound the rate at which a photodetector can transfer information from an optical field to an electrical record, and which proposed resource sets fail by explicit counterexample?**

The project began by asking for a detector-independent sensitivity--bandwidth--temperature law. The research trail shows that this question is too broad unless the detector/output class and hidden dynamical resources are specified.

The mature first-paper result is therefore a **resource-completeness theorem for one precisely defined detector class**, together with no-go results explaining why broader statements fail.

This repository is theoretical/analytical. Numerical calculations are used for validation; experiments, fabrication, procurement, and laboratory campaigns are not required next steps.

---

## First-paper theorem class

The current manuscript concerns:

- autonomous/time-translation-invariant photodetection;
- weak coherent/Poisson direct-detection intensity modulation;
- independent-event/low-overlap operation;
- one primary electrical registration per captured photon;
- retention of the complete accessible primary-event mark.

It does **not** claim a speed limit for coherent continuous pointers, externally synchronized detectors, arbitrary high-flux/history-dependent counters, nonclassical optical inputs, or every architecture called a photodetector.

---

## Exact marked-event information transfer

Per incident photon, write the primary-event channel as the subprobability kernel

\[
K(dm,d\tau)=\kappa(dm)\mu_m(d\tau),
\qquad
\eta=\kappa(\mathsf M)\le1,
\]

where `m` is the complete accessible event mark and `tau` is registration delay.

For weak sinusoidal Poisson intensity modulation, the ideal source-normalized Fisher-information transfer is

\[
\boxed{
G(\omega)=\int_{\mathsf M}|H_m(\omega)|^2\kappa(dm).
}
\]

Parameter-independent background addition and downstream stochastic processing cannot increase this FI.

---

## Timing-resource hierarchy

### Atomic timing

Wiener's classical theorem gives the exact high-band flat-average residue

\[
\boxed{
\lim_{\Omega\to\infty}
\frac{1}{2\Omega}
\int_{-\Omega}^{\Omega}G(\omega)d\omega
=
\int\kappa(dm)\sum_j p_j(m)^2.
}
\]

Thus deterministic/discrete timing branches are the exact asymptotic obstruction; purely non-atomic conditional timing forces the flat-band **average** transfer to vanish.

### Collision resource

For square-integrable conditional delay densities,

\[
\boxed{
\mathfrak R_2
=2\int\kappa(dm)\int f_m(t)^2dt,
}
\]

and Parseval gives

\[
\boxed{
\int_{-\infty}^{\infty}G(\omega)d\omega
=\pi\mathfrak R_2.
}
\]

### Capture-weighted local hazard capacity

If `h_m(t)<=Lambda(m)`, define

\[
\boxed{
\mathfrak H=\int\Lambda(m)\kappa(dm).
}
\]

Then

\[
\boxed{\mathfrak R_2\le\mathfrak H.}
\]

The capture-weighted resource is sharper than a global worst-case rate: a very fast branch can be harmless when its event weight is sufficiently small.

---

## Operational inverse theorem

For a flat source-information task on ordinary-frequency half-band

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

If `q=r eta` is retention relative to captured DC information,

\[
\boxed{\Lambda\ge4Br.}
\]

This is the cleanest current operational resource-cost statement.

---

## Main no-go results

The repository contains explicit counterexamples showing that the following are not resource-complete substitutes for the timing resources above:

- deterministic latency;
- exact mean delay plus exact RMS timing jitter;
- stationary entropy production/activity/throughput without an absolute microscopic rate scale;
- detector-only timing resources when an unbounded source-synchronous clock/reference is supplied for free.

For finite-state CTMC detectors, complete mark conditioning also requires care: the safe generic uniform microscopic rate bound is the maximum **total escape rate** from any pre-registration state,

\[
q_{\max}=\max_{x\in S_{\rm pre}}\sum_{y\ne x}W_{yx},
\]

not merely the successful-registration edge intensity. This is the WP35 correction.

---

## Thermodynamic bridge

For the restricted reversible finite-state Markov optical gateway, stationary EPR, activity, and minimum throughput can bound temporal information only after an absolute microscopic rate is supplied.

With reverse gateway rate `d`,

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

The gateway's total first-exit rate `lambda_1` bounds the relevant conditional hazard under the stated mark restriction. The rare-fast counterexample proves that stationary aggregate thermodynamic quantities alone do not create the missing absolute time scale.

---

## Publication state

Active branch:

`agent/uprp-core-theorem-round10`

Rev4 was fully build verified. WP35 then identified one localized microscopic-rate wording correction.

Rev5 applies that correction, removes the unneeded generic quantum-jump sentence, explicitly references both theorem figures, and tightens the finite-frequency prior-work wording. The final generated Rev5 state has passed GitHub Actions generation, full LaTeX compilation, and artifact upload.

Current audit/checkpoint files:

- `docs/CURRENT_RESEARCH_STATE.md`
- `docs/MANUSCRIPT_REV5_FINAL_AUDIT.md`
- `notes/RESEARCH_LOG_ROUND14.md`
- `notes/WP35_MARK_CONDITIONED_MARKOV_RATE_CORRECTION.md`
- `AGENTS.md`
- `ROADMAP.md`

The first-paper science is at the **submission-package stage**. Additional foundational derivations are not the default next action.

---

## Frozen branches

The following remain scientifically useful but are frozen for the first manuscript unless a concrete review objection requires them:

- HgCdTe/Kane material calculations WP17--24;
- coherent quantum-pointer resource theory;
- continuous classical/analog detector generalization;
- non-Poisson/nonclassical source extensions.

Failed conjectures and negative results are intentionally retained in the repository because they establish why the final resource hierarchy has its present form.
