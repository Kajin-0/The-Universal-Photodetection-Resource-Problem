# AGENTS.md

## Purpose
Durable handoff for **The Universal Photodetection Resource Problem (UPRP)**. The repository, not chat history, is authoritative.

Research is analytical/theoretical only. Numerical work may be used for validation. Do not make experiments, fabrication, procurement, or laboratory campaigns necessary next steps.

## Working branch
`agent/uprp-core-theorem-round10`

## Read first
1. `docs/CURRENT_RESEARCH_STATE.md`
2. `manuscript/event_resource_theorem_rev7.tex`
3. `notes/RESEARCH_LOG_ROUND16.md`
4. `notes/WP36_COMPLETE_WEAK_WAVEFORM_FISHER_OPERATOR.md`
5. `notes/WP36A_BAND_SUBSPACE_FISHER_GUARANTEE.md`
6. `docs/MANUSCRIPT_REV6_REFEREE_REPAIR_AUDIT.md`
7. `notes/RESEARCH_LOG_ROUND15.md`
8. `notes/WP35_MARK_CONDITIONED_MARKOV_RATE_CORRECTION.md`
9. `notes/WP34_MINIMUM_TIMING_RESOURCE_COST_THEOREM.md`
10. `notes/WP32_GENERAL_MARKED_POISSON_EVENT_KERNEL_THEOREM.md`
11. `notes/WP33_EXACT_FIXED_MEAN_VARIANCE_JITTER_NO_GO.md`
12. `notes/WP29_THERMODYNAMIC_BRIDGE_TO_REGISTRATION_INTENSITY.md`
13. `notes/WP30_WIENER_ATOMIC_DELAY_INFORMATION_THEOREM.md`
14. `docs/NOVELTY_AUDIT_ROUND5_EVENT_THEOREM_STACK.md`

**Freeze:** HgCdTe/Kane WP17–24, coherent-pointer, continuous-analog, non-Poisson/nonclassical, and high-flux/history-dependent branches unless a concrete referee-level defect in Rev7 requires reopening them.

---

# Publication state

Current first-paper source:

`manuscript/event_resource_theorem_rev7.tex`

Rev7 is the **current publication/submission candidate**. Rev6 remains the frozen hostile-referee-hardened predecessor and must not be edited retroactively.

Rev7 adds a significance layer without broadening the detector model class:

1. complete local weak-waveform Fisher operator;
2. pointwise necessary-and-sufficient weak-waveform detector ordering;
3. exact band-subspace worst-case Fisher retention;
4. exact DC-normalized Fisher-equivalent bandwidth;
5. independent delay-stage cascade law and serial-Erlang example.

Canonical source blob for the verified main TeX:
`f59e36e32a2d6eb36752c847cbdd40b07b241db0`

Verification records:
- canonical push run `32433326375`: generation, full LaTeX compile, artifact upload, and persistence succeeded;
- independent proof-hardened PR run `32433375491`: generation, full LaTeX compile, and artifact upload succeeded;
- independent artifact ID `9429898246`, ZIP SHA-256 `733262dc3b07b6959c175bbddb5ee1185016500b276dd932061342c75199f276`;
- final proof-hardened PDF: 24 pages, 360775 bytes in the independent run;
- only material typesetting warning is the inherited approximately `2.45667 pt` appendix overfull box around “timing-concentration”; no new Rev7 layout failure.

Temporary validation PR `#13` is closed and was never intended for merge.

Steady-state CI:
`.github/workflows/manuscript-check.yml`

It was restored in commit `8b9118bd7ae428dd51952853c1571624356fdc94` to:
- `permissions: contents: read`;
- direct compilation of committed `event_resource_theorem_rev7.tex`;
- artifact upload only;
- no source generation, self-commit, or PR-validation side effects.

---

# First-paper theorem class

The theorem concerns autonomous/time-translation-invariant, independent-event / low-overlap, one-primary-registration photodetection under weak coherent/Poisson direct-detection intensity modulation, retaining the complete accessible primary-event mark.

Do **not** describe it as a universal all-detector speed limit.

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

At exact DC the incident FI rate is `Phi_0`, not `Phi_0/2`; the same factor changes in the output, so normalized transfer remains
\[
\boxed{G(0)=\eta.}
\]

Parameter-independent background/downstream processing cannot increase FI.

---

# Rev7 complete weak-waveform Fisher operator

For finite-dimensional real weak temporal perturbations
\[
\Phi_{\boldsymbol\theta}(t)
=\Phi_0\left[1+\sum_{a=1}^p\theta_a s_a(t)\right],
\qquad s_a\in L^2(\mathbb R)\cap L^\infty(\mathbb R),
\]
with Plancherel transforms `S_a`, Rev7 proves
\[
\boxed{
[F_{\rm out}]_{ab}
=\frac{\Phi_0}{2\pi}
\int_{-\infty}^{\infty}
G(\omega)S_a^*(\omega)S_b(\omega)d\omega.
}
\]

Thus multiplication by `G(omega)` is the complete local Fisher-information transfer operator for weak temporal waveform perturbations in this detector class. The sinusoidal theorem is its Fourier-mode specialization.

The transfer spectrum is real, bounded, even, and continuous:
\[
\boxed{
0\le G(\omega)\le\eta,
\qquad G(-\omega)=G(\omega),
\qquad G\in C(\mathbb R).
}
\]

## Universal weak-waveform Fisher ordering
For two detectors in the same class,
\[
\boxed{
G_A(\omega)\ge G_B(\omega)\ \forall\omega
\iff
F_A\succeq F_B
\text{ for every admissible finite weak-waveform task.}
}
\]

Do not call this generic Blackwell dominance. It is local Fisher ordering for the stated weak-waveform family.

If spectra cross, there is no task-independent Fisher ranking within this model.

## Exact band-subspace guarantee
For a scalar perturbation spectrally supported in `[-Omega,Omega]`,
\[
\rho_G[s]
=\frac{F_{\rm out}[s]}{F_{\rm in}[s]}
=\frac{\int G|S|^2}{\int|S|^2}.
\]
Continuity gives
\[
\boxed{
\inf_{s\ne0,\ \operatorname{supp}S\subset[-\Omega,\Omega]}
\rho_G[s]
=
\min_{|\omega|\le\Omega}G(\omega).
}
\]
Therefore retaining at least absolute Fisher fraction `q` for **every** weak waveform in the band is equivalent to
\[
\boxed{G(\omega)\ge q\quad\forall |\omega|\le\Omega.}
\]

---

# Timing-resource hierarchy

## Atomic timing residue
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

The capture-weighted `mathfrak H` is preferred to a global worst-case rate.

---

# Rev7 exact Fisher-equivalent bandwidth

For `eta>0`, define the ordinary-frequency DC-normalized equivalent rectangular Fisher bandwidth
\[
\boxed{
B_{\rm FI}
\equiv
\frac1\eta\int_0^\infty G(2\pi f)df
=
\frac{\mathfrak R_2}{4\eta}.
}
\]

This is an information-area metric, **not** an electrical amplitude or `-3 dB` bandwidth.

Using `mathfrak R_2<=mathfrak H`,
\[
\boxed{B_{\rm FI}\le\frac{\mathfrak H}{4\eta}.}
\]
For a common conditional-hazard ceiling `Lambda`,
\[
\boxed{B_{\rm FI}\le\frac{\Lambda}{4}.}
\]
The single exponential delay saturates this bound.

---

# Inverse timing-resource cost

For ordinary-frequency half-band
\[
B=\frac{\Omega}{2\pi},
\]
a target absolute flat-average transfer `q` requires
\[
\boxed{
q\le\eta,
\qquad
\mathfrak R_2\ge4Bq,
\qquad
\mathfrak H\ge4Bq.
}
\]

Rev7 gives the same coefficient a stronger interpretation: it is also a necessary cost for guaranteeing at least `q` retention for **every weak waveform** in the full band.

For a common markwise hazard ceiling,
\[
\boxed{\Lambda\ge\frac{4Bq}{\eta}.}
\]
For `q=r eta`,
\[
\boxed{\Lambda\ge4Br.}
\]

---

# Independent cascade example

For independent unresolved unmarked delay-only stages,
\[
\boxed{G_{12}(\omega)=G_1(\omega)G_2(\omega).}
\]
Do not extend this scalar product law to arbitrary retained marks or history-dependent stages.

For `k` serial exponential stages of common rate `lambda`, total capture probability `eta`,
\[
G_k(\omega)=\eta\left(\frac{\lambda^2}{\lambda^2+\omega^2}\right)^k,
\]
and
\[
\boxed{
B_{\rm FI}
=\frac{\lambda}{4}
\frac{\binom{2k-2}{k-1}}{4^{k-1}}
\sim\frac{\lambda}{4\sqrt{\pi(k-1)}}.
}
\]

---

# Conventional-jitter no-go

For any prescribed mean `mu0>0` and variance `sigma^2>0`, a smooth delay family can satisfy both exactly while `|H_D(omega)|^2 -> 1` uniformly on any prescribed finite band.

Therefore exact mean delay plus exact RMS jitter do not bound information bandwidth.

Rev7, like Rev6, explicitly does **not** claim a fixed-FWHM counterexample. Scalar widths such as FWHM require additional shape assumptions before functioning as resource summaries.

---

# Finite-state CTMC completion

The successful-registration edge intensity alone does not generically bound the complete-mark-conditioned delay hazard when competing exits exist.

For pre-registration state `x`,
\[
\lambda_x=\sum_{y\ne x}W_{yx},
\qquad
\boxed{q_{\max}=\max_{x\in S_{\rm pre}}\lambda_x.}
\]

The first holding time is `Exp(lambda_x)` and independent of exit destination/subsequent trajectory; under the mark restriction,
\[
D\mid(M,x)=T_x+Y_{M,x},\qquad Y_{M,x}\ge0,
\]
so
\[
\boxed{h_D(t\mid M,x)\le\lambda_x\le q_{\max}.}
\]
Mixing over the initial state preserves the `q_max` ceiling.

The generic quantum-jump operator-norm extension remains deferred.

---

# Thermodynamic model-class bridge

Use **bidirectionally connected**, not “reversible,” for the nonequilibrium CTMC gateway/counterexample. Reverse-transition support does not mean stationary detailed balance.

The stationary thermodynamic bound is applied to the event theorem only through the explicit isolated-event reduction:

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

Do not claim:
- first information-theoretic detector timing analysis;
- first IRF-information result;
- first sensitivity-bandwidth tradeoff;
- generic finite-frequency response/noise novelty;
- generic Fisher-information transfer-function novelty;
- Blackwell ordering;
- arbitrary fixed-FWHM no-go;
- universal all-detector speed limit.

Defensible Rev7 contribution:

> A temporal-information resource theory for autonomous marked photodetection event channels in which the exact marked-delay spectrum is the complete local weak-waveform Fisher multiplier; pointwise spectral ordering is necessary and sufficient for universal local weak-waveform Fisher dominance; atomic timing, collision concentration, and capture-weighted hazard provide a resource hierarchy; the exact Fisher-equivalent bandwidth and inverse band-resource costs make that hierarchy operational; and explicit no-go/repair results show why low-order jitter metrics, free synchronous control, and aggregate stationary thermodynamics are incomplete resources.

Novelty is strongest in the **combined theorem stack**, not the classical ingredients individually.

---

# Immediate next action

**Stop foundational expansion of the first paper unless a concrete defect is found.**

Proceed to submission packaging / journal positioning from committed Rev7:
- target-journal fit and current submission requirements;
- author/affiliation metadata when supplied;
- final source/package inventory;
- cover letter;
- concise significance/novelty statement;
- title/abstract polish only if scientifically neutral.

Potential capacity/QFI/high-flux-memory generalizations belong to a second-paper program unless needed to repair a specific Rev7 flaw.

Status vocabulary: **PROVED**, **VERIFIED**, **CONJECTURE**, **COUNTEREXAMPLE**, **OPEN**, **BLOCKED**, **REJECTED**.
