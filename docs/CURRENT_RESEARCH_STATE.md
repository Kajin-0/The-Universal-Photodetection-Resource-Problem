# Current Research State

**Date:** 2026-08-20

Active branch:

`agent/uprp-core-theorem-round10`

## Publication state

Current first-paper source:

`manuscript/event_resource_theorem_rev6.tex`

Rev6 is the current **submission candidate**. It is the targeted hostile-referee repair of Rev5 and does not change the central theorem stack or any headline numerical coefficient.

Supporting records:

- `docs/MANUSCRIPT_REV6_REFEREE_REPAIR_AUDIT.md`
- `notes/RESEARCH_LOG_ROUND15.md`
- `notes/WP35_MARK_CONDITIONED_MARKOV_RATE_CORRECTION.md`

Rev6 passed GitHub Actions generation, full LaTeX compilation, artifact upload, and source persistence. The final layout pass for trigger commit `4009049562838ee33ff8c9c18fdbe072b933ff57` also succeeded and persisted the two-line thermodynamic box.

Steady-state CI is read-only and compiles committed Rev6 directly. It has no self-commit or issue-comment behavior.

---

# Detector class

The first-paper theorem is restricted to:

- autonomous/time-translation-invariant processing;
- independent-event / low-overlap operation;
- one primary electrical registration per captured photon;
- complete accessible primary-event marks;
- weak coherent/Poisson direct-detection intensity modulation;
- parameter-independent downstream background/processing for the FI upper-bound step.

It is not a universal speed law for every photodetector architecture.

---

# Exact marked-event transfer

Per incident photon,
\[
K(dm,d\tau)=\kappa(dm)\mu_m(d\tau),
\qquad
\eta=\kappa(\mathsf M)\le1.
\]

For nonzero sinusoidal modulation frequency,
\[
\boxed{G(\omega)=\int_{\mathsf M}|H_m(\omega)|^2\kappa(dm).}
\]

At exact DC the incident FI rate is `Phi_0`, rather than `Phi_0/2`; the same factor changes in the output FI and the normalized transfer remains
\[
\boxed{G(0)=\eta.}
\]

Parameter-independent downstream processing cannot increase FI.

---

# Timing-resource hierarchy

## Atomic residue
\[
\boxed{
\lim_{\Omega\to\infty}\frac1{2\Omega}
\int_{-\Omega}^{\Omega}G(\omega)d\omega
=
\int\kappa(dm)\sum_jp_j(m)^2.
}
\]

This is a flat-band average asymptotic, not a generic pointwise Fourier-decay claim.

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

The capture-weighted resource is preferred to a global worst-case rate.

---

# Operational inverse theorem

For ordinary-frequency half-band
\[
B=\frac{\Omega}{2\pi},
\]
a required absolute average information fraction `q` implies
\[
\boxed{
q\le\eta,
\qquad
\mathfrak R_2\ge4Bq,
\qquad
\mathfrak H\ge4Bq.
}
\]

For a common conditional-hazard ceiling,
\[
\boxed{\Lambda\ge\frac{4Bq}{\eta}.}
\]
For `q=r eta`,
\[
\boxed{\Lambda\ge4Br.}
\]

---

# Exact conventional-jitter no-go

For arbitrary prescribed mean `mu0>0` and variance `sigma^2>0`, a smooth delay family can satisfy both exactly while its transfer approaches the capture ceiling uniformly on every prescribed finite band.

Therefore exact mean delay plus exact RMS jitter does not determine a finite temporal information bandwidth.

Rev6 explicitly claims **no fixed-FWHM counterexample**; FWHM requires additional shape assumptions.

---

# Finite-state CTMC hazard completion

For pre-registration state `x`, define
\[
\lambda_x=\sum_{y\ne x}W_{yx},
\qquad
\boxed{q_{\max}=\max_{x\in S_{\rm pre}}\lambda_x.}
\]

Rev6 now proves the uniform conditional-hazard bound. The first holding time is `Exp(lambda_x)` and independent of exit destination/subsequent trajectory. Under the mark restriction,
\[
D\mid(M,x)=T_x+Y_{M,x},\quad Y_{M,x}\ge0,
\]
so
\[
\boxed{h_D(t\mid M,x)\le\lambda_x\le q_{\max}.}
\]
Mixing over the initial pre-registration state preserves the `q_max` ceiling.

The successful-registration edge rate alone is insufficient when exits compete.

---

# Rev6 thermodynamic closure

Do **not** call the nonequilibrium CTMC gateway/counterexample “reversible” in the standard Markov-chain sense. Rev6 uses **bidirectionally connected**, meaning reverse-transition support, while allowing nonzero stationary currents and entropy production.

The restricted thermodynamic bridge is now explicitly connected to the event theorem through an isolated-event / low-overlap reduction:

1. stationary baseline EPR/activity/traffic constrain microscopic rates;
2. condition on one isolated optical capture into gateway state 1;
3. the post-capture autonomous CTMC generates the per-photon delay kernel;
4. require sufficiently separated source events that occupancy/recovery do not make capture or the kernel history dependent.

If capture/recovery is history dependent, the independent-event kernel and thermodynamic information bound are not claimed.

For the restricted bidirectionally connected gateway,
\[
\boxed{
\lambda_1\le
\Lambda_*
=\frac{\mathcal A d}{f_*}g^{-1}(\Sigma/f_*),
\qquad
g(z)=(1-z^{-1})\ln z.
}
\]

The absolute microscopic reverse rate `d` remains indispensable. The rare-fast counterexample proves stationary aggregate thermodynamic quantities alone do not set the missing temporal scale.

---

# Scope boundaries

- Free source-synchronous clock/control defeats detector-only timing bounds unless reference resources are counted.
- Coherent continuous pointers are a separate quantum-resource branch.
- High-flux history-dependent capture/recovery requires trajectory-level treatment.
- Multiple independent pre-primary timing records are an additional multiplicity resource.
- Nonclassical/phase-sensitive source parameters require a different input-information normalization.

---

# Novelty posture

Established mathematical ingredients are treated as prior art: marked Poisson processes/FI, Wiener theory, Parseval, survival/hazard calculus, TCSPC/IRF information loss, synchronous references, and generic finite-frequency response/noise inequalities.

The defensible candidate novelty is the **combined photodetection resource-completeness stack** and its explicit no-go/repair structure.

---

# Frozen work

Keep frozen unless a concrete Rev6 referee-level defect forces reopening:

- HgCdTe/Kane WP17–24;
- coherent quantum pointers;
- continuous analog detectors;
- non-Poisson/nonclassical source extensions.

---

# Next action

Prepare the submission-ready package and journal positioning from committed Rev6. Additional foundational research is not the default next step.
