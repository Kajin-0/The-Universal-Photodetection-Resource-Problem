# WP5 — Incident-Channel QFI Capture Bound

**Date:** 2026-08-19

## Purpose

This note replaces an emitter-centered LDOS-first formulation by a more natural incident-channel statement for photodetection. It derives a rigorous information-theoretic reduction for a passive linear optical frontend and then examines what electromagnetic/matter sum rule is actually safe to use.

**Status:**

- QFI/data-processing capture lemma: **PROVED** for coherent-state modulation through a passive frequency-preserving linear optical frontend.
- Microscopic electric-dipole/TRK integrated-capture corollary: **PROVED within the dipole/oscillator-strength model**.
- Arbitrary macroscopic scatterer/device cross-section version: **NOT YET PROVED**; do not use a blanket extinction-cross-section sum rule without a rigorous T-operator derivation.

---

# 1. Optical input and task

Represent a narrowband incident coherent field by continuous spectral modes with coherent amplitudes

\[
\alpha(\omega;\theta),
\]

where `theta` is the encoded optical parameter.

Use the mode normalization

\[
\langle a^\dagger(\omega)a(\omega')\rangle
=2\pi |\alpha(\omega)|^2\delta(\omega-\omega')
\]

schematically; exact finite-time normalization can be fixed by box normalization and then taking the continuum limit.

For a pure multimode coherent-state family, the quantum Fisher information is proportional to the squared displacement derivative,

\[
F_{\rm in}^{Q}
=4\int\frac{d\omega}{2\pi}
|\partial_\theta\alpha(\omega;\theta)|^2,
\]

for the usual real-parameter coherent-state convention. Any common convention factor cancels in the information-transfer ratio.

Define the input QFI spectral density

\[
\mathcal J_{\rm in}(\omega)
=4|\partial_\theta\alpha(\omega;\theta)|^2.
\]

---

# 2. Passive capture channel

A passive, linear, time-invariant, frequency-preserving optical frontend admits a Stinespring/unitary scattering representation at each frequency. For one selected incident mode, the input coherent amplitude is distributed among:

- reflected/transmitted/radiated optical output modes;
- internal absorptive bath/capture modes.

Let

\[
0\le\tau(\omega)\le1
\]

be the total probability/power fraction sent into the internal capture subspace for that normalized incident channel.

Because coherent states remain product coherent states under passive linear mode mixing, the total QFI residing in the capture subspace is

\[
\boxed{
F_{\rm cap}^{Q}
=\int\frac{d\omega}{2\pi}
\tau(\omega)\mathcal J_{\rm in}(\omega).
}
\]

This is exact for coherent displacement encoding in the stated passive-linear model.

---

# 3. Electrical-record data-processing bound

The electrical photodetector record is downstream of the captured optical/material degrees of freedom. Hence by monotonicity of quantum Fisher information under parameter-independent quantum channels, followed by the classical-measurement data-processing inequality,

\[
F_{\rm elec}
\le F_{\rm cap}^{Q}
\le F_{\rm in}^{Q}.
\]

Therefore

\[
\boxed{
\eta_{\mathcal I}
\equiv\frac{F_{\rm elec}}{F_{\rm in}^{Q}}
\le
\frac{\int\frac{d\omega}{2\pi}
\tau(\omega)\mathcal J_{\rm in}(\omega)}
{\int\frac{d\omega}{2\pi}\mathcal J_{\rm in}(\omega)}.
}
\]

This is the **incident optical capture ceiling**. It is independent of the downstream detector mechanism.

For a flat coherent-state QFI task over the optical sideband interval

\[
\omega\in[\omega_0-\Omega_s,\omega_0+\Omega_s],
\]

one obtains

\[
\boxed{
\bar\eta_{\mathcal I}(\Omega_s)
\le
\frac{1}{2\Omega_s}
\int_{\omega_0-\Omega_s}^{\omega_0+\Omega_s}
\tau(\omega)d\omega.
}
\]

Thus a photodetector cannot retain more information than the sideband-averaged optical capture probability.

**Status:** PROVED under the stated coherent/passive/frequency-preserving assumptions.

---

# 4. Why this is preferable to LDOS as the primary frontend quantity

LDOS is naturally emitter-centered: it bounds spontaneous-emission coupling of a local source into its environment. Photodetection is incident-channel driven.

The capture coefficient `tau(omega)` is operationally aligned with the detector problem:

\[
\text{incident optical channel}
\to
\text{absorbed/internal degrees of freedom}
\to
\text{electrical record}.
\]

LDOS remains useful for reciprocal/localized gateway models, but should be treated as a special-case way to constrain the microscopic coupling, not as the universal optical performance variable.

---

# 5. Microscopic electric-dipole/TRK corollary

For a finite microscopic absorber in the electric-dipole/oscillator-strength regime, the integrated photoabsorption strength is constrained by the Thomas–Reiche–Kuhn sum rule.

For one polarization and the conventional oscillator-strength normalization, a transition of oscillator strength `f_j` has integrated absorption strength proportional to `f_j`, and

\[
\sum_j f_j=N_e.
\]

The standard angular-frequency integrated dipole cross-section scale is

\[
\boxed{
\int_0^\infty\sigma_{\rm abs}(\omega)d\omega
\le
C_e N_e,
\qquad
C_e\equiv
\frac{\pi e^2}{2\epsilon_0m_ec}.
}
\]

Numerically,

\[
\boxed{
C_e=1.66756\times10^{-5}\ {m m^2\,s^{-1}}
}
\]

per electron.

The inequality allows oscillator strength to go into nonabsorptive/radiative channels; equality is a model-dependent idealization.

For a planar/beam-normalized detector in which

\[
\tau(\omega)=\sigma_{\rm abs}(\omega)/A
\]

is valid for illuminated area `A`, the flat-sideband QFI bound gives

\[
\boxed{
\bar\eta_{\mathcal I}
\le
\min\left[
1,
\frac{\pi e^2}{4\epsilon_0m_ec}
\frac{N_e/A}{\Omega_s}
\right].
}
\]

Therefore a target

\[
\bar\eta_{\mathcal I}\ge r
\]

requires

\[
\boxed{
\Omega_s
\le
\frac{\pi e^2}{4\epsilon_0m_ec}
\frac{N_e/A}{r}.
}
\]

In ordinary baseband frequency `f_s=Omega_s/(2pi)`,

\[
\boxed{
f_s
\le
\frac{e^2}{8\epsilon_0m_ec}
\frac{N_e/A}{r},
}
\]

with numerical coefficient

\[
\boxed{
\frac{e^2}{8\epsilon_0m_ec}
=1.32700\times10^{-6}\ {m m^2\,s^{-1}}.
}
\]

Example: for areal participating-electron density

\[
N_e/A=10^{21}\ {m m^{-2}}
\]

and `r=0.9`, this ceiling is

\[
f_s\lesssim1.47\times10^{15}\ {m Hz}.
\]

This is finite but extraordinarily loose for infrared detector engineering.

## Interpretation

Electron number / total oscillator strength alone is sufficient to prevent a mathematically infinite integrated capture bandwidth in this microscopic dipole class, but it is far too coarse to give a technologically meaningful bound. A useful theorem must constrain how much oscillator strength can reside near the specified optical carrier and over the required sideband interval.

---

# 6. Critical macroscopic-sum-rule caveat

Do **not** promote the preceding microscopic dipole formula to an arbitrary macroscopic photonic scatterer by assertion.

Mishchenko, *Broadband electromagnetic scattering by particles*, JOSA A 25, 2893 (2008), explicitly criticized commonly invoked extinction-cross-section sum rules when they are justified only by heuristic causality arguments rather than a first-principles scattering derivation.

The rigorous arbitrary-scatterer route should instead use the modern matrix-valued `T`-operator representation of Zhang, Monticone, and Miller, *Nature Communications* 14, 7724 (2023). Their passive-scattering result gives

\[
\int_{-\infty}^{\infty}
\omega\,\operatorname{Im}\mathbb T(\omega)d\omega
=
\pi\omega_p^2\mathbb I_V,
\]

along with a low-frequency sum rule and a bounded matrix-oscillator representation.

The next task is to project those operator constraints onto a normalized incident optical channel and derive a rigorous finite-band bound on **absorbed/captured QFI**, not merely on an assumed scalar cross section.

**Status:** OPEN.

---

# 7. Relation to 2026 maximum-capacity work

Amaolo et al., *Maximum Shannon capacity of photonic structures*, npj Nanophotonics 3, 14 (2026), already combine information theory, electromagnetic Green functions, structural optimization, and power constraints to bound Shannon capacity of arbitrarily structured photonic environments.

This creates a major novelty constraint:

- `information theory + Maxwell bounds` is already occupied;
- a generic maximum-capacity claim would be redundant.

However, that paper explicitly states that its current results are **single-frequency** and identifies finite-band generalization via spectral sum rules/delay-bandwidth products and macroscopic-QED extensions as future work. It also treats receiver-field communication with externally specified noise models, rather than a finite-temperature photodetector's endogenous optical-to-electrical conversion noise.

The surviving UPRP target is therefore specifically:

\[
\boxed{
\text{finite-band incident optical QFI}
\to
\text{physical optical capture}
\to
\text{finite-temperature electrical detector record},
}
\]

with both electromagnetic and internal detector resources counted.

---

# 8. Composition with the thermokinetic transducer theorem

Let

\[
B_{\rm opt}(\Omega_s)
\]

be any rigorous optical capture ceiling obtained from the incident-channel problem, and let

\[
B_{\rm trans}(\Omega_s)
\]

be the WP3/WP4 downstream thermokinetic ceiling once a microscopic coupling cap has been supplied.

Data processing yields the safe composite bound

\[
\boxed{
\bar\eta_{\mathcal I}^{\rm total}(\Omega_s)
\le
\min\{B_{\rm opt}(\Omega_s),B_{\rm trans}(\Omega_s)\}.
}
\]

Therefore achieving

\[
\bar\eta_{\mathcal I}^{\rm total}\ge r
\]

requires simultaneously

\[
B_{\rm opt}\ge r,
\qquad
B_{\rm trans}\ge r.
\]

If these imply separate bandwidth ceilings `Omega_opt,max` and `Omega_trans,max`, then

\[
\boxed{
\Omega_s
\le
\min\{\Omega_{\rm opt,max},\Omega_{\rm trans,max}\}.
}
\]

This is currently the cleanest architecture for a final UPRP completion theorem.

---

# 9. What remains to tighten the optical bound

The all-frequency TRK budget is far too loose. Candidate tightening mechanisms:

1. **High + low frequency T-operator sum rules.** The 2023 matrix-oscillator representation constrains both total oscillator weight and inverse-frequency-weighted oscillator weight.
2. **Finite-band material susceptibility bounds.** Restrict permitted `chi(omega)` in the carrier band rather than allowing all electron oscillator strength to be concentrated there.
3. **Finite spatial resources.** Bound footprint, volume, separation, aperture, or material electron density.
4. **Passivity/energy-conservation constraints at complex frequency.** Use the Shim–Fan–Johnson–Miller power-bandwidth machinery where a local/near-field gateway is appropriate.
5. **Channel singular-value bounds.** Project the T-operator onto incident and absorbing channels, closer in spirit to Amaolo et al.'s Maxwell-constrained channel matrices.

The desired next theorem is a finite-band operator inequality on capture QFI that is both rigorous and meaningfully tighter than total electron count.

---

# 10. Immediate next derivation target

Starting from the matrix oscillator representation

\[
\mathbb T(\omega)
=
\lim_{\gamma\to0}
\int_0^\infty
\frac{
\mathbb X(\omega_i)+\frac{\omega_i}{\omega}\mathbb Y(\omega_i)
}{
\omega_i^2-\omega^2-i\gamma\omega
}
d\omega_i,
\]

with

\[
\mathbb X(\omega_i)\succeq0,
\]

\[
\frac1{\omega_p^2}\int_0^\infty\mathbb X(\omega_i)d\omega_i
\preceq\mathbb I_D,
\]

\[
\int_0^\infty\frac{\mathbb X(\omega_i)}{\omega_i^2}d\omega_i
\preceq\mathbb T_{0,D},
\]

derive the tightest bound possible on a normalized incident-channel absorptive functional over

\[
\omega\in[\omega_0-\Omega_s,\omega_0+\Omega_s].
\]

This is the highest-priority WP5 mathematical target.
