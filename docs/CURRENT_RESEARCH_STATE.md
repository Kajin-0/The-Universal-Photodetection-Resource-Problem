# Current Research State

**Date:** 2026-08-20

Active branch:

`agent/uprp-core-theorem-round10`

## Publication state

Current first-paper source:

`manuscript/event_resource_theorem_rev5.tex`

Rev5 is now **committed and mechanically verified**. Its committed blob SHA is

`23ad1c27be95bdbf79d88176d438c8a305f844f0`,

which exactly matches the Git blob hash of the TeX source retrieved from the successful GitHub Actions Rev5 artifact.

The final generated Rev5 state passed:

1. assertion-based Rev4 -> Rev5 generation;
2. full LaTeX compilation;
3. artifact upload.

Steady-state CI has been restored to read-only direct compilation of committed Rev5. It has no self-commit or issue-comment side effects.

Final audit:

`docs/MANUSCRIPT_REV5_FINAL_AUDIT.md`

Latest durable research checkpoint:

`notes/RESEARCH_LOG_ROUND14.md`

The first-paper science is at the **submission-package stage**.

---

# Detector class

The mature theorem is restricted to:

- autonomous/time-translation-invariant processing;
- independent-event/low-overlap operation;
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

Exact ideal source-normalized transfer:
\[
\boxed{
G(\omega)=\int_{\mathsf M}|H_m(\omega)|^2\kappa(dm).
}
\]

Parameter-independent background addition or downstream stochastic processing cannot increase FI.

---

# Timing-resource hierarchy

## Exact atomic residue
\[
\boxed{
\lim_{\Omega\to\infty}\frac1{2\Omega}
\int_{-\Omega}^{\Omega}G(\omega)d\omega
=
\int\kappa(dm)\sum_jp_j(m)^2.
}
\]

This is a flat-band **average** result. Purely non-atomic conditional timing gives zero asymptotic average transfer; do not strengthen it to generic pointwise Fourier decay.

## Collision resource
For square-integrable conditional delay densities,
\[
\boxed{
\mathfrak R_2=2\int\kappa(dm)\int f_m(t)^2dt,
\qquad
\int G(\omega)d\omega=\pi\mathfrak R_2.
}
\]

Thus
\[
\boxed{
\bar\eta_I(\Omega)
\le
\min\left[\eta,\frac{\pi\mathfrak R_2}{2\Omega}\right].
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

`mathfrak H` is the preferred microscopic sufficient rate resource; a global worst-case hazard is only a stronger corollary.

---

# WP34 inverse resource cost
For flat ordinary-frequency half-band
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

# WP33 exact jitter no-go
For arbitrary prescribed `mu0>0` and `sigma^2>0`, a smooth delay family can satisfy exactly
\[
\mathbb E D=\mu_0,
\qquad
\operatorname{Var}D=\sigma^2
\]
for every selected family member while source-normalized transfer approaches the capture ceiling uniformly on every prescribed finite band.

Therefore exact mean delay plus exact RMS jitter do not bound temporal information bandwidth.

No arbitrary fixed-exact-FWHM theorem is claimed.

---

# WP35 CTMC correction
The successful-registration edge intensity alone is not a generic complete-mark-conditioned hazard bound.

For finite-state CTMC pre-registration state set `S_pre`,
\[
q_x=\sum_{y\ne x}W_{yx},
\qquad
\boxed{q_{\max}=\max_{x\in S_{\rm pre}}q_x.}
\]

Provided the accessible mark does not independently expose realized pre-registration holding times,
\[
\boxed{h_D(t\mid M)\le q_{\max}.}
\]

Rev5 applies this correction and removes the generic quantum-jump operator-norm sentence. The capture-weighted theorem and all constants are unchanged.

---

# Thermodynamic bridge
The restricted finite-state time-homogeneous reversible gateway already uses the **total first-exit rate** `lambda1`, so WP29 required no repair.

With forward traffic `f>=f_*`, EPR `<=Sigma`, activity `<=A`, reverse rate `d`, and
\[
g(z)=(1-z^{-1})\ln z,
\]
\[
\boxed{
\lambda_1\le
\Lambda_*
=\frac{\mathcal A d}{f_*}g^{-1}(\Sigma/f_*).
}
\]

The absolute microscopic rate `d` cannot be eliminated in favor of stationary thermodynamic aggregates alone; the rare-fast counterexample establishes this.

---

# Final claim/citation posture
Established ingredients are explicitly treated as prior art: marked Poisson processes/FI, Wiener theory, Parseval, survival/hazard calculus, TCSPC/IRF information loss, synchronous references, and generic finite-frequency response/noise inequalities.

The defensible candidate contribution is the **combined resource-completeness stack** and its photodetection-specific no-go/repair structure.

The final audit tightened the Dechant comparison to the claims directly needed from the cited finite-frequency response/fluctuation work.

---

# Frozen work
Keep frozen for the first paper unless a concrete referee-level defect requires reopening:

- HgCdTe/Kane WP17–24;
- coherent quantum pointers;
- continuous analog detectors;
- non-Poisson/nonclassical source extensions.

---

# Next action
Prepare the submission-ready source/package and journal positioning from committed Rev5. Additional foundational research is not the default next step.
