# The Universal Photodetection Resource Problem

## Research question

**What physical resources are actually sufficient to bound the rate at which a photodetector can transfer information from an optical field to an electrical record, and which proposed resource sets fail by explicit counterexample?**

The project began by asking for a detector-independent sensitivity--bandwidth--temperature law. The research trail shows that this is too broad unless the detector/output class and hidden dynamical resources are specified.

The mature first-paper result is therefore a **temporal-information resource theory for one precisely defined autonomous photodetection event class**, together with exact operational bounds and no-go results explaining why broader statements fail.

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

For weak sinusoidal Poisson intensity modulation, the ideal source-normalized Fisher-information transfer is
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

## Complete weak-waveform Fisher operator

Rev7 removes the apparent dependence on a sinusoidal probe. For arbitrary finite-dimensional weak temporal flux perturbations
\[
\Phi_{\boldsymbol\theta}(t)
=\Phi_0\left[1+\sum_{a=1}^{p}\theta_a s_a(t)\right],
\qquad
s_a\in L^2(\mathbb R)\cap L^\infty(\mathbb R),
\]
with Plancherel transforms `S_a`, the ideal primary-record Fisher matrix is
\[
\boxed{
[F_{\rm out}]_{ab}
=\frac{\Phi_0}{2\pi}
\int_{-\infty}^{\infty}
G(\omega)S_a^*(\omega)S_b(\omega)d\omega.
}
\]

Thus `G(omega)` is the spectral multiplier of the **complete local weak-waveform Fisher-information operator** for this detector class. Sinusoidal modulation is simply its Fourier-mode specialization.

The transfer spectrum is bounded, even, and continuous:
\[
\boxed{
0\le G(\omega)\le\eta,
\qquad
G(-\omega)=G(\omega),
\qquad
G\in C(\mathbb R).
}
\]

---

## Universal weak-waveform Fisher ordering

For two detectors `A` and `B` in the same theorem class,
\[
\boxed{
G_A(\omega)\ge G_B(\omega)\ \text{for every }\omega
\iff
F_A\succeq F_B
\text{ for every admissible finite weak-waveform task.}
}
\]

So `G` is a complete local Fisher-ordering object for weak temporal waveform estimation in this model. If two spectra cross, neither detector has a task-independent Fisher advantage.

This is **not** a claim of generic Blackwell dominance.

---

## Exact band-subspace guarantee

For a scalar weak perturbation with spectrum supported in `[-Omega,Omega]`, define
\[
\rho_G[s]
=\frac{F_{\rm out}[s]}{F_{\rm in}[s]}
=\frac{\int G(\omega)|S(\omega)|^2d\omega}
{\int |S(\omega)|^2d\omega}.
\]

Rev7 proves
\[
\boxed{
\inf_{s\ne0,\ \operatorname{supp}S\subset[-\Omega,\Omega]}
\rho_G[s]
=
\min_{|\omega|\le\Omega}G(\omega).
}
\]

Therefore preserving at least an absolute Fisher fraction `q` for **every weak temporal waveform in the full band** is equivalent to
\[
\boxed{
G(\omega)\ge q
\qquad\text{for every }|\omega|\le\Omega.
}
\]

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

## Exact Fisher-equivalent bandwidth

For `eta>0`, Rev7 defines the DC-normalized equivalent rectangular Fisher bandwidth
\[
\boxed{
B_{\rm FI}
\equiv
\frac1\eta\int_0^\infty G(2\pi f)df
=
\frac{\mathfrak R_2}{4\eta}.
}
\]

This is an information-area metric, not an electrical amplitude or `-3 dB` bandwidth.

The hazard hierarchy gives
\[
\boxed{
B_{\rm FI}\le\frac{\mathfrak H}{4\eta}.
}
\]

For a common captured-event conditional-hazard ceiling,
\[
\boxed{B_{\rm FI}\le\Lambda/4.}
\]

A single exponential registration delay saturates the common-hazard bound.

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

Rev7 gives the same coefficient a stronger interpretation: these resource lower bounds are also necessary for guaranteeing at least `q` Fisher retention for **every weak waveform** in the entire band.

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

## Independent delay-stage cascade

For serial independent unresolved **unmarked delay-only** stages,
\[
\boxed{G_{12}(\omega)=G_1(\omega)G_2(\omega).}
\]

For `k` serial exponential waiting stages of common rate `lambda`, total capture probability `eta`,
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

This gives a simple architecture-level example of unresolved serial timing stages progressively consuming equivalent temporal Fisher bandwidth.

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
the maximum **total escape rate** from pre-registration states, not merely the successful-registration edge intensity. The manuscript contains the self-contained holding-time proof.

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

The stationary rate bound is connected to the independent-event theorem through an **isolated-event / low-overlap reduction**: stationary thermodynamic quantities constrain baseline microscopic rates, then one conditions on an isolated optical capture and uses the subsequent autonomous CTMC as the per-photon post-capture delay kernel. If occupancy/recovery makes capture history dependent, the independent-event information bound is not claimed.

The rare-fast counterexample proves that stationary aggregate thermodynamic quantities alone do not supply an absolute temporal scale.

---

## Publication state

Active branch:

`agent/uprp-core-theorem-round10`

Current manuscript:

`manuscript/event_resource_theorem_rev7.tex`

Rev7 is the current publication candidate. It inherits the hostile-referee repairs in Rev6 and adds the complete weak-waveform Fisher operator, pointwise detector ordering, exact band-subspace guarantee, exact Fisher-equivalent bandwidth, and independent serial-delay example.

Verification:

- push run `32433326375`: successful generation, full LaTeX compilation, artifact upload, and source persistence;
- independent proof-hardened run `32433375491`: successful generation, full LaTeX compilation, and artifact upload;
- artifact ID `9429898246`;
- verified main TeX blob `f59e36e32a2d6eb36752c847cbdd40b07b241db0`;
- only the inherited approximately `2.45667 pt` appendix overfull warning remains.

Temporary validation PR #13 is closed and unmerged.

Current state files:

- `docs/CURRENT_RESEARCH_STATE.md`
- `notes/RESEARCH_LOG_ROUND16.md`
- `notes/WP36_COMPLETE_WEAK_WAVEFORM_FISHER_OPERATOR.md`
- `notes/WP36A_BAND_SUBSPACE_FISHER_GUARANTEE.md`
- `AGENTS.md`
- `ROADMAP.md`

Steady-state CI has read-only permissions and directly compiles committed Rev7. It has no self-commit/source-generation validation machinery.

The first-paper science is at the **submission-package stage**. Additional foundational derivations are not the default next action.

---

## Novelty posture

Do not claim:

- first information-theoretic detector timing analysis;
- first IRF-information result;
- first generic sensitivity-bandwidth tradeoff;
- generic Fisher-information transfer-function novelty;
- generic Blackwell detector ordering;
- generic finite-frequency response/noise novelty;
- arbitrary fixed-FWHM no-go;
- a universal all-detector speed limit.

The defensible contribution is the combined autonomous marked-event temporal-resource theorem stack and its operational weak-waveform completion.

---

## Frozen branches

Frozen for the first manuscript unless a concrete Rev7 defect requires reopening:

- HgCdTe/Kane material calculations WP17--24;
- coherent quantum-pointer resource theory;
- continuous classical/analog detector generalization;
- non-Poisson/nonclassical source extensions;
- high-flux/history-dependent event-channel extensions.

Failed conjectures and negative results remain in the repository because they establish why the final resource hierarchy has its present form.
