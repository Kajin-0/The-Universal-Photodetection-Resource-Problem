# Manuscript Skeleton — Autonomous Photodetection Event Resource Theorem

**Date:** 2026-08-20

## Publication purpose

Test whether the mature WP25–WP32 autonomous event-detector branch can support a focused first paper without relying on the frozen HgCdTe material side branch.

This is a **skeleton and claim audit**, not a finished manuscript.

---

# Candidate title

**Resource bounds on temporal information transfer in photodetection event channels**

Alternatives:

- **What limits photodetector information bandwidth? Timing concentration and thermodynamic resource bounds**
- **Temporal information bandwidth of autonomous photodetection events**
- **No-go and resource theorems for photodetector information bandwidth**

Avoid titles suggesting that hazard theory, Fisher information, or Wiener theory themselves are new.

---

# One-sentence claim

For autonomous direct-detection event channels, source-normalized temporal information is controlled by the spectral concentration of the **mark-resolved registration-delay law**; deterministic timing atoms give an exact high-bandwidth residue, finite timing-collision intensity gives a quantitative spectral budget, and a bounded local registration rate gives a microscopic completion, while stationary thermodynamic quantities and conventional jitter metrics do not supply that rate scale by themselves.

---

# Proposed abstract logic

1. Conventional photodetector bandwidth mixes latency, waveform attenuation, timing jitter, and readout filtering, none of which are individually equivalent to loss of source information.
2. Model a captured photon as producing a marked primary electrical event through an autonomous random-delay kernel.
3. Derive the exact source-normalized Fisher-information transfer for weak coherent/Poisson flux modulation.
4. Use classical Wiener theory to show that the asymptotic high-bandwidth information residue is exactly the squared atomic mass of the mark-conditioned delay distribution.
5. For square-integrable delay densities, use Parseval to define a timing-collision resource and derive a finite spectral budget; show bounded local registration hazard/jump intensity is a microscopic sufficient condition.
6. Give explicit no-go constructions showing that mean/RMS/FWHM jitter and stationary EPR/activity do not replace this local timing resource.
7. In a reversible Markov optical-gateway class, combine throughput, EPR, activity, and a bounded absolute microscopic rate to obtain an explicit thermokinetic information-bandwidth ceiling.
8. Show that a free synchronous clock defeats detector-only timing bounds, identifying autonomy/reference-frame resources as an essential scope condition.

---

# Detector class

The paper should state the class before any theorem.

- weak intensity modulation of coherent light, equivalently an inhomogeneous Poisson photon process for direct detection;
- autonomous/time-translation-invariant detector;
- one primary electrical registration event per successfully captured photon;
- arbitrary accessible autonomous event mark retained;
- parameter-independent dark/background and downstream processing allowed but not needed in the upper bound;
- no free source-synchronous temporal reference;
- no coherent continuous pointer carrying phase before irreversible registration;
- multiple independent pre-primary timing copies from one photon are a separate class.

This narrow statement is a strength. Do not sell the paper as covering every photodetector architecture.

---

# Theorem 1 — exact marked event-kernel information transfer

Let

\[
K(dm,d\tau)=\kappa(dm)\mu_m(d\tau)
\]

be the autonomous marked registration kernel per incident photon, with total primary-event probability

\[
\eta=\kappa(\mathsf M)\le1.
\]

For weak sinusoidal flux modulation at `omega`, define

\[
H_m(\omega)=\int e^{-i\omega\tau}d\mu_m(\tau).
\]

Then the ideal marked primary-record source-normalized FI is

\[
\boxed{
\eta_I(\omega)
=G(\omega)
=\int|H_m(\omega)|^2\kappa(dm).
}
\]

Any parameter-independent background or downstream processing satisfies

\[
\eta_I^{measured}(\omega)\le G(\omega).
\]

### Importance

This establishes the exact object that later theorems bound and automatically handles parallel mark channels.

### Prior-art posture

Marked-Poisson FI and displacement/marking theorems are standard. Claim only the detector-channel specialization and subsequent resource consequences.

---

# Theorem 2 — exact atomic high-bandwidth residue

For each mark, let `p_j(m)` be atomic masses of the conditional delay measure.

Wiener's classical theorem gives

\[
\boxed{
\lim_{\Omega\to\infty}
\frac1{2\Omega}
\int_{-\Omega}^{\Omega}G(\omega)d\omega
=
\int\kappa(dm)\sum_jp_j(m)^2.
}
\]

### Consequences

- purely non-atomic mark-conditioned timing forces asymptotic average information to vanish;
- exact deterministic delay branches leave a nonzero residue;
- accessible side information can reveal a deterministic branch and restore timing information.

### Physical interpretation

The fundamental asymptotic obstruction is not `RMS jitter`; it is **atomic timing information after conditioning on the full accessible event record**.

### Prior-art posture

Wiener's theorem is classical. The paper derives a photodetection information corollary.

---

# Theorem 3 — timing-collision spectral budget

When each `mu_m` has square-integrable density `f_m`, define

\[
\boxed{
\mathfrak R_2
=2\int\kappa(dm)\int f_m(t)^2dt.
}
\]

Then

\[
\boxed{
\int_{-\infty}^{\infty}G(\omega)d\omega
=\pi\mathfrak R_2.
}
\]

For a flat band,

\[
\boxed{
\bar\eta_I(\Omega)
\le
\min\left[
\eta,
\frac{\pi\mathfrak R_2}{2\Omega}
\right].
}
\]

For arbitrary normalized source-information spectrum `w`, with spectral concentration function `W(A)`, the conditional form is

\[
\boxed{
\bar\eta_I[w]
\le
\eta\mathcal W\!\left(
\pi\mathfrak R_2/\eta
\right).
}
\]

### Importance

This is the quantitative information-bandwidth theorem independent of an arbitrary scalar bandwidth convention.

---

# Corollary 3A — local hazard / registration-intensity completion

If

\[
h_m(t)\le\Lambda(m),
\]

then

\[
2\int f_m^2dt\le\Lambda(m).
\]

Define capture-weighted hazard capacity

\[
\boxed{
\mathfrak H
=\int\Lambda(m)\kappa(dm).
}
\]

Then

\[
\boxed{\mathfrak R_2\le\mathfrak H}
\]

and

\[
\boxed{
\bar\eta_I(\Omega)
\le
\min\left[
\eta,
\frac{\pi\mathfrak H}{2\Omega}
\right].
}
\]

A uniform local ceiling `Lambda(m)<=Lambda` gives

\[
\bar\eta_I\le\eta\min(1,\pi\Lambda/(2\Omega)).
\]

Classical Markov and quantum-jump operator norms provide microscopic sufficient realizations.

### Tightness

Constant-hazard exponential registration asymptotically saturates the uniform-hazard high-band coefficient.

---

# Counterexample 1 — conventional jitter moments are not resource-complete

Use WP26 smooth prompt-spike/long-tail family.

Fix finite mean/variance while making a dominant prompt timing component arbitrarily narrow.

For every fixed finite source band,

\[
\eta_I(\omega)\to\eta
\]

while the moment constraint remains fixed.

### Claim

Mean latency, RMS jitter, FWHM jitter, and related conventional scalar timing metrics cannot furnish a universal source-information bandwidth bound.

This is one of the strongest practical messages in the paper.

---

# Counterexample 2 — stationary thermodynamics is insufficient

Use WP4 rare-fast reversible Markov family.

Hold fixed/bounded:

- temperature / optical detailed-balance ratio;
- useful throughput;
- stationary activity;
- stationary EPR.

Allow an absolute microscopic local rate to diverge while the fast state becomes rare.

The detector timing resource and information bandwidth diverge.

### Claim

\[
\boxed{
(T,\Sigma,\mathcal A,\text{detailed balance},f_*)
\not\Rightarrow
\text{finite information bandwidth}.
}
\]

This is the thermodynamic no-go result.

---

# Theorem 4 — restricted thermokinetic completion

Use WP3/WP29 reversible single-gateway class.

With fixed reverse optical rate `d`, throughput `f>=f_*`, EPR `<=Sigma`, and activity `<=A`,

\[
Z_*=g^{-1}(\Sigma/f_*),
\qquad
g(z)=(1-z^{-1})\ln z,
\]

and

\[
\boxed{
\Lambda_*
=\frac{\mathcal A dZ_*}{f_*}.
}
\]

WP29 proves the full mark-conditioned registration hazard satisfies

\[
\boxed{h_D(t|M)\le\Lambda_*}.
\]

Therefore

\[
\boxed{
\bar\eta_I(\Omega)
\le
C\min\left[
1,
\frac{\pi\mathcal A d}{2f_*\Omega}
 g^{-1}(\Sigma/f_*)
\right].
}
\]

The gateway's exponential first stage also gives a stronger Lorentzian envelope.

### Interpretation

Thermodynamics constrains speed only **conditional on an absolute microscopic rate scale**. Temperature and stationary dissipation do not create that scale.

This theorem reconnects the paper directly to the original UPRP motivation.

---

# Counterexample 3 — free temporal reference

Use WP27.

A source-synchronous clock records arrival phase

\[
M=\omega t\pmod{2\pi}
\]

and reports the mark arbitrarily slowly.

The captured photon retains its full source timing FI despite slow registration.

### Claim

Autonomy/time-translation invariance is a necessary scope assumption unless clock/control bandwidth and phase-memory resources are counted explicitly.

---

# Figure plan

## Figure 1 — information-bandwidth concept

Compare:

- deterministic delay: phase only, no FI loss;
- continuous random delay: characteristic-function attenuation;
- deterministic atomic branch + continuous tail: nonzero asymptotic residual.

This visually establishes why conventional `-3 dB` latency language is inadequate.

## Figure 2 — timing-resource hierarchy

Diagram:

`local hazard/operator rate -> R2 collision intensity -> spectral budget -> source information ceiling`

with a separate branch

`atomic timing mass -> asymptotic residual`.

## Figure 3 — counterexample to RMS jitter

Plot prompt-spike/long-tail distributions with fixed variance and their information transfer spectra.

## Figure 4 — thermodynamic no-go/repair

Two panels:

- WP4 rare-fast family: bounded `A,Sigma` but diverging local rate;
- WP29 gateway repair: adding absolute microscopic rate closes the loophole.

No material-specific HgCdTe figure is necessary for the first paper.

---

# Suggested paper structure

1. Introduction: conventional bandwidth vs information bandwidth.
2. Source-normalized temporal FI and autonomous marked event channel.
3. Exact event-kernel transfer theorem.
4. Atomic timing theorem and information residue.
5. Collision-intensity / hazard quantitative bounds.
6. Why conventional jitter metrics fail.
7. Thermodynamic impossibility theorem.
8. Restricted thermokinetic completion.
9. External-clock/reference-frame loophole.
10. Discussion: detector-class taxonomy and implications.
11. Appendices: Poisson FI derivation, Wiener corollary, hazard `L2` lemma, Markov gateway proof, counterexample algebra.

---

# Claims to avoid

Do not write:

- "first Fisher-information treatment of detector jitter";
- "first relation between Fisher information and hazard rate";
- "first thermodynamic detector speed limit";
- "universal for all photodetectors";
- "RMS jitter does not matter";
- "RC bandwidth is meaningless";
- "temperature does not matter".

Correct statements are narrower:

- conventional scalar jitter moments are not resource-complete for source-information bandwidth;
- deterministic filtering/latency need not reduce intrinsic FI;
- temperature affects the bound only through microscopic resources in the stated theorem class;
- the central theorem applies to autonomous proper event detectors.

---

# Publication-readiness assessment

## Mathematical coherence

**Strong.** The theorem chain is now logically ordered and the main inequalities have independent interpretations/tightness checks.

## Physical scope

**Clear but restricted.** This is acceptable if stated prominently.

## Novelty

**Promising but provisional.** No equivalent complete theorem stack found, but many ingredients are classical and close timing/FI literature exists.

## Significance

Likely depends less on algebraic difficulty and more on whether reviewers view the resource-completeness synthesis as changing how detector speed limits should be formulated.

The strongest significance points are:

1. exact separation of latency/amplitude response from information loss;
2. exact atomic timing residual;
3. conventional-jitter no-go;
4. thermodynamic no-go + conditional repair;
5. explicit clock/reference resource boundary.

## Recommendation

The event branch is now mature enough to justify drafting a first theorem manuscript **after one final targeted novelty/citation-chain audit**. Do not reopen the HgCdTe material branch before that decision.