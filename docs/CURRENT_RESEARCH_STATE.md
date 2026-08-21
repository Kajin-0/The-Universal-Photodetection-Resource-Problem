# Current Research State

**Date:** 2026-08-20

Active branch:

`agent/uprp-core-theorem-round10`

## Publication state

Current first-paper source:

`manuscript/event_resource_theorem_rev7.tex`

Rev7 is the current **submission candidate**. It preserves Rev6's hostile-referee repairs and adds a significance layer that remains inside the same autonomous independent-event detector class.

Primary new records:

- `notes/WP36_COMPLETE_WEAK_WAVEFORM_FISHER_OPERATOR.md`
- `notes/WP36A_BAND_SUBSPACE_FISHER_GUARANTEE.md`
- `notes/RESEARCH_LOG_ROUND16.md`

Rev6 records remain relevant for the model-class and referee repairs:

- `docs/MANUSCRIPT_REV6_REFEREE_REPAIR_AUDIT.md`
- `notes/RESEARCH_LOG_ROUND15.md`
- `notes/WP35_MARK_CONDITIONED_MARKOV_RATE_CORRECTION.md`

## Verification

Canonical Rev7 source blob:

`f59e36e32a2d6eb36752c847cbdd40b07b241db0`

Validation:

- push run `32433326375`: generation, full LaTeX compilation, artifact upload, and source persistence **SUCCESS**;
- independent proof-hardened PR run `32433375491`: generation, full LaTeX compilation, artifact upload **SUCCESS**;
- independent artifact ID `9429898246`;
- artifact ZIP SHA-256 `733262dc3b07b6959c175bbddb5ee1185016500b276dd932061342c75199f276`;
- final independent build: 24 pages, 360775 bytes;
- only nontrivial layout warning is the inherited approximately `2.45667 pt` overfull appendix line involving “timing-concentration.”

Temporary validation PR `#13` is closed and unmerged.

Steady-state CI was restored in commit

`8b9118bd7ae428dd51952853c1571624356fdc94`

to read-only direct compilation of committed Rev7. It performs no source generation, self-commit, or PR-validation mutation.

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

For sinusoidal modulation,
\[
\boxed{G(\omega)=\int_{\mathsf M}|H_m(\omega)|^2\kappa(dm).}
\]

At exact DC the incident FI rate is `Phi_0`, rather than `Phi_0/2`; the same factor changes in the output FI and normalized transfer remains
\[
\boxed{G(0)=\eta.}
\]

Parameter-independent downstream processing cannot increase FI.

---

# Rev7 complete weak-waveform Fisher operator

For
\[
\Phi_{\boldsymbol\theta}(t)
=\Phi_0\left[1+\sum_{a=1}^{p}\theta_a s_a(t)\right],
\qquad
s_a\in L^2(\mathbb R)\cap L^\infty(\mathbb R),
\]
with Plancherel transforms `S_a`, Rev7 proves
\[
\boxed{
[F_{\rm out}]_{ab}
=\frac{\Phi_0}{2\pi}
\int G(\omega)S_a^*(\omega)S_b(\omega)d\omega.
}
\]

Thus `G` is the spectral multiplier of the complete local weak-waveform Fisher operator for this detector class. Sinusoidal modulation is a Fourier-mode specialization, not a fundamental restriction.

The spectrum obeys
\[
\boxed{
0\le G(\omega)\le\eta,
\qquad
G(-\omega)=G(\omega),
\qquad
G\in C(\mathbb R).
}
\]

## Necessary-and-sufficient detector ordering

For two detectors in the same theorem class,
\[
\boxed{
G_A(\omega)\ge G_B(\omega)\ \forall\omega
\iff
F_A\succeq F_B
\text{ for every admissible finite weak-waveform task.}
}
\]

This is local Fisher ordering, not a claim of generic Blackwell dominance.

If `G_A` and `G_B` cross, there is no task-independent Fisher ranking within this model.

---

# Exact band-subspace guarantee

For a nonzero scalar weak perturbation,
\[
\rho_G[s]
=\frac{F_{\rm out}[s]}{F_{\rm in}[s]}
=\frac{\int G(\omega)|S(\omega)|^2d\omega}
{\int |S(\omega)|^2d\omega}.
\]

For the compact band `[-Omega,Omega]`, continuity gives
\[
\boxed{
\inf_{s\ne0,\ \operatorname{supp}S\subset[-\Omega,\Omega]}
\rho_G[s]
=
\min_{|\omega|\le\Omega}G(\omega).
}
\]

Therefore retaining at least absolute Fisher fraction `q` for **every** admissible weak temporal waveform in the band is equivalent to
\[
\boxed{G(\omega)\ge q\quad\forall |\omega|\le\Omega.}
\]

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
\int_{-\infty}^{\infty}G(\omega)d\omega=\pi\mathfrak R_2.
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

# Exact Fisher-equivalent bandwidth

For `eta>0`, Rev7 defines
\[
\boxed{
B_{\rm FI}
=\frac1\eta\int_0^\infty G(2\pi f)df
=\frac{\mathfrak R_2}{4\eta}.
}
\]

This is a DC-normalized equivalent rectangular **Fisher-information area bandwidth**, not an electrical amplitude or `-3 dB` bandwidth.

The hierarchy gives
\[
\boxed{B_{\rm FI}\le\frac{\mathfrak H}{4\eta}.}
\]
If all captured-event conditional hazards share a common ceiling `Lambda`,
\[
\boxed{B_{\rm FI}\le\frac{\Lambda}{4}.}
\]
The single exponential delay saturates this inequality.

---

# Operational inverse theorem

For ordinary-frequency half-band
\[
B=\frac{\Omega}{2\pi},
\]
a required absolute flat-average information fraction `q` implies
\[
\boxed{
q\le\eta,
\qquad
\mathfrak R_2\ge4Bq,
\qquad
\mathfrak H\ge4Bq.
}
\]

Rev7 strengthens the operational interpretation: the same `4Bq` lower bound is also necessary to guarantee at least `q` retention for **every weak waveform** in the entire band.

For a common conditional-hazard ceiling,
\[
\boxed{\Lambda\ge\frac{4Bq}{\eta}.}
\]
For `q=r eta`,
\[
\boxed{\Lambda\ge4Br.}
\]

---

# Independent-stage cascade example

For serial independent unresolved unmarked delay-only stages,
\[
\boxed{G_{12}(\omega)=G_1(\omega)G_2(\omega).}
\]

For `k` independent serial exponential waits of common rate `lambda`,
\[
G_k(\omega)
=\eta\left(\frac{\lambda^2}{\lambda^2+\omega^2}\right)^k,
\]
and
\[
\boxed{
B_{\rm FI}
=\frac{\lambda}{4}
\frac{\binom{2k-2}{k-1}}{4^{k-1}}
\sim
\frac{\lambda}{4\sqrt{\pi(k-1)}}.
}
\]

This provides an architecture-level example of accumulated unresolved timing consuming temporal Fisher bandwidth.

---

# Exact conventional-jitter no-go

For arbitrary prescribed mean `mu0>0` and variance `sigma^2>0`, a smooth delay family can satisfy both exactly while its transfer approaches the capture ceiling uniformly on every prescribed finite band.

Therefore exact mean delay plus exact RMS jitter does not determine a finite temporal information bandwidth.

Rev7 explicitly claims **no fixed-FWHM counterexample**; FWHM requires additional shape assumptions.

---

# Finite-state CTMC hazard completion

For pre-registration state `x`, define
\[
\lambda_x=\sum_{y\ne x}W_{yx},
\qquad
\boxed{q_{\max}=\max_{x\in S_{\rm pre}}\lambda_x.}
\]

The self-contained holding-time proof inherited from Rev6 gives
\[
D\mid(M,x)=T_x+Y_{M,x},\quad Y_{M,x}\ge0,
\]
with `T_x~Exp(lambda_x)`, hence
\[
\boxed{h_D(t\mid M,x)\le\lambda_x\le q_{\max}.}
\]
Mixing over the initial pre-registration state preserves the ceiling.

The successful-registration edge rate alone is insufficient when exits compete.

---

# Thermodynamic closure

Use **bidirectionally connected**, not “reversible,” for the nonequilibrium CTMC gateway/counterexample. Reverse-transition support does not imply detailed balance.

The restricted thermodynamic bridge is connected to the event theorem through the isolated-event / low-overlap reduction:

1. stationary baseline EPR/activity/traffic constrain microscopic rates;
2. condition on one isolated optical capture into gateway state 1;
3. the post-capture autonomous CTMC generates the per-photon delay kernel;
4. require sufficiently separated source events that occupancy/recovery do not make capture or the kernel history dependent.

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

Established ingredients are treated as prior art: marked Poisson processes/FI, Wiener theory, Parseval, survival/hazard calculus, TCSPC/IRF information loss, synchronous references, generic Fisher-information transfer functions in other optical contexts, and generic finite-frequency response/noise inequalities.

The defensible novelty is the **combined autonomous-photodetection temporal-resource theorem stack**, now strengthened by the complete weak-waveform Fisher operator, necessary-and-sufficient spectral ordering, exact band-subspace guarantee, and exact Fisher-equivalent bandwidth.

Do not claim generic Blackwell dominance, generic FI-transfer-function novelty, a fixed-FWHM no-go, or a universal all-detector speed limit.

---

# Frozen work

Keep frozen unless a concrete Rev7 referee-level defect forces reopening:

- HgCdTe/Kane WP17–24;
- coherent quantum pointers;
- continuous analog detectors;
- non-Poisson/nonclassical source extensions;
- high-flux/history-dependent event channels.

---

# Next action

The first-paper foundational research phase is closed by default.

Prepare the submission-ready package and journal positioning from committed Rev7. Potential capacity/QFI/high-flux-memory extensions should be treated as second-paper work unless they are required to repair a specific Rev7 defect.
