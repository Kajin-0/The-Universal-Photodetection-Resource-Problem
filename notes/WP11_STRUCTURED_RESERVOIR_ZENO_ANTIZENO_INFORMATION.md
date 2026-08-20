# WP11 — Structured-reservoir Zeno/anti-Zeno information theorem

**Date:** 2026-08-20

## Purpose

The earlier dissipative WP11 model uses a flat Markov localization/readout rate `Gamma`. This note replaces that phenomenological constant by the simplest frequency-structured reservoir and asks how measurement/readout broadening changes the effective event rate and timestamp information.

Main conclusion:

> **A single Golden-Rule/Markov rate is not resource-complete once detector backaction broadens the transition. The reservoir spectral density/correlation scale and energetic detuning become independent resources.**

Generic Zeno/anti-Zeno spectral-overlap physics is established prior art. The project-specific result is the closed-form information-resource composition for the detector event stage.

---

# 1. Kofman–Kurizki overlap framework

In weak system-bath coupling, measurement/control-modified decay can be written as a spectral overlap

\[
\boxed{
\Gamma_{\rm eff}
=2\pi\int d\omega\,G(\omega)F(\omega),
}
\]

where

- `G(omega)` is the reservoir coupling spectrum;
- `F(omega)` is the normalized control/measurement-broadening spectrum.

This is the Kofman–Kurizki universal formula. Depending on whether broadening decreases or increases spectral overlap, one obtains quantum-Zeno or anti-Zeno behavior.

Literature anchors:

- A. G. Kofman and G. Kurizki, Nature 405, 546 (2000) and related Zeno/anti-Zeno work;
- Kofman, Kurizki, Opatrny, Phys. Rev. A 63, 042108 (2001);
- Kurizki et al. reviews of universal dynamical control;
- modern experimental/use examples retain the same overlap structure.

Do not claim the spectral-overlap principle as novel.

---

# 2. Lorentzian reservoir and measurement broadening

Define the bath spectrum

\[
\boxed{
G(\omega)
=\frac{\gamma_0}{2\pi}
\frac{\lambda^2}
{(\omega-\omega_c)^2+\lambda^2}.
}
\]

`lambda` is the reservoir half-width/correlation scale, `omega_c` its center, and `gamma_0` sets the coupling strength.

Let the detector transition frequency be `omega_0` and define

\[
\Delta=\omega_0-\omega_c.
\]

Model continuous measurement/dephasing broadening by the normalized Lorentzian

\[
\boxed{
F_\nu(\omega)
=\frac1\pi
\frac{\nu}
{(\omega-\omega_0)^2+\nu^2},
}
\]

with `nu >= 0`; in the `nu -> 0+` limit this tends to `delta(omega-omega_0)`.

The overlap of two normalized Lorentzians is another Lorentzian with summed width. Therefore

\[
\boxed{
\Gamma_{\rm eff}(\nu)
=\gamma_0
\frac{\lambda(\lambda+\nu)}
{\Delta^2+(\lambda+\nu)^2}.
}
\]

At zero measurement broadening,

\[
\boxed{
\Gamma_0^{\rm GR}
=\gamma_0\frac{\lambda^2}{\Delta^2+\lambda^2}.
}
\]

**Status:** PROVED within the weak-coupling spectral-overlap model and stated normalization.

---

# 3. Exact Zeno / anti-Zeno criterion

Let

\[
x=\lambda+\nu.
\]

Then

\[
\Gamma_{\rm eff}=\gamma_0\lambda\frac{x}{\Delta^2+x^2}.
\]

Its derivative has sign

\[
\operatorname{sgn}\frac{d\Gamma_{\rm eff}}{d\nu}
=
\operatorname{sgn}(\Delta^2-x^2).
\]

Therefore:

## Resonant / near-resonant case

If

\[
|\Delta|\le\lambda,
\]

then already at `nu=0`, `x>=|Delta|`, so

\[
\boxed{
\frac{d\Gamma_{\rm eff}}{d\nu}\le0
\quad\forall\nu\ge0.
}
\]

Increasing measurement broadening only suppresses decay: pure Zeno behavior within this model.

At exact resonance,

\[
\boxed{
\Gamma_{\rm eff}(\nu)
=\gamma_0\frac{\lambda}{\lambda+\nu}.
}
\]

## Detuned case

If

\[
|\Delta|>\lambda,
\]

then initially

\[
d\Gamma_{\rm eff}/d\nu>0.
\]

The effective event rate is maximized at

\[
\boxed{
\nu_*^{\rm AZ}
=|\Delta|-\lambda.
}
\]

At this optimum,

\[
\boxed{
\Gamma_{\rm max}
=\gamma_0\frac{\lambda}{2|\Delta|}.
}
\]

The enhancement over the unbroadened Golden-Rule rate is

\[
\boxed{
\frac{\Gamma_{\rm max}}
{\Gamma_0^{\rm GR}}
=
\frac{\Delta^2+\lambda^2}
{2\lambda|\Delta|}
\ge1.
}
\]

For `|Delta| >> lambda`, the enhancement factor is approximately `|Delta|/(2lambda)`.

For still larger `nu`, the rate eventually decreases as

\[
\Gamma_{\rm eff}\sim\gamma_0\lambda/\nu,
\]

so the asymptotic strong-measurement limit is always Zeno-suppressed.

---

# 4. Timestamp information spectrum

Suppose this structured-reservoir decay is the only unresolved stochastic post-capture event stage and is approximately exponential with rate `Gamma_eff(nu)`.

Then

\[
H_T(\Omega)
=\frac{\Gamma_{\rm eff}}
{\Gamma_{\rm eff}+i\Omega}
\]

for modulation angular frequency `Omega`, and

\[
\boxed{
\eta_I(\Omega;\nu)
=\eta_{\rm pre}
\frac{\Gamma_{\rm eff}(\nu)^2}
{\Gamma_{\rm eff}(\nu)^2+\Omega^2}.
}
\]

`eta_pre` collects optical capture efficiency and any preceding independent information penalties.

Thus maximizing event-timestamp information bandwidth with respect to measurement broadening is equivalent, in this single exponential stage, to maximizing `Gamma_eff`.

Consequently:

- `|Delta|<=lambda`: best `nu` is the smallest allowed measurement broadening;
- `|Delta|>lambda`: anti-Zeno optimum `nu=|Delta|-lambda` maximizes the timestamp bandwidth;
- `nu -> infinity`: information bandwidth collapses through Zeno suppression.

The half-information angular frequency of this stage is exactly

\[
\boxed{\Omega_{1/2}=\Gamma_{\rm eff}(\nu).}
\]

---

# 5. New no-go: a scalar Markov rate is insufficient

Two reservoirs can have the same unperturbed local rate

\[
\Gamma_0^{\rm GR}=2\pi G(\omega_0)
\]

but different spectral curvature/width away from `omega_0`.

Under detector-induced broadening they can therefore exhibit different:

- Zeno versus anti-Zeno response;
- optimal measurement strength;
- effective localization speed;
- timestamp information bandwidth.

Hence

\[
\boxed{
\{\Gamma_0^{\rm GR}\}
\not\Rightarrow
\text{backaction-modified detector information speed}.
}
\]

A resource-complete strong-readout model needs at least the relevant **reservoir spectral shape/correlation scale**, not merely its on-shell rate.

---

# 6. Reservoir resource hierarchy

For this detector stage the minimal spectral resource set is

\[
\boxed{
\text{system-bath coupling weight}
+\text{reservoir width/correlation time}
+\text{detuning}
+\text{measurement/control broadening resource}
\Rightarrow
\Gamma_{\rm eff}
\Rightarrow
\eta_I(\Omega).
}
\]

For a general reservoir, replace the Lorentzian parameters by the full relevant `G(omega)` or a mathematically sufficient spectral envelope/smoothness class.

---

# 7. Relation to previous WP11 dissipative matching

`WP11_DISSIPATIVE_MATCHING_THEOREM.md` uses `Gamma` as a flat irreversible registration rate coupled to a coherent optical-capture subsystem. The present `nu` is a measurement/control broadening parameter that modifies an underlying structured reservoir rate.

They must not be silently identified.

A more complete detector can contain both:

1. coherent optical capture `g`;
2. structured reservoir localization `Gamma_eff(nu)`;
3. electrical registration/readout backaction.

In a weak-coupling reduction one may substitute the structured `Gamma_eff(nu)` into a Markov event stage, but only when the reservoir correlation time is short enough relative to subsequent dynamics.

---

# 8. Novelty boundary

The following are prior art:

- quantum Zeno and anti-Zeno effects;
- Kofman–Kurizki spectral-overlap formula;
- measurement-induced level broadening;
- structured-reservoir control of decay.

Do not claim them as new.

The UPRP-specific role is to show that **reservoir spectral structure is another missing resource in a photodetector information-bandwidth theorem**, and to compose it explicitly with source-normalized event-record FI.

---

# 9. Next step

1. Replace the Lorentzian reservoir by semiconductor phonon/contact spectral densities with threshold/band-edge structure.
2. Derive resource bounds using only coarse spectral quantities, e.g. total coupling weight plus bandwidth/Lipschitz constraints, rather than specifying the entire `G(omega)`.
3. Compose structured localization with the coherent capture/readout matching model without double-counting measurement backaction.
4. Search whether a theorem can bound `sup_nu Gamma_eff(nu)` from finite reservoir spectral weight and bandwidth; if not, construct a spectral-spike counterexample.
