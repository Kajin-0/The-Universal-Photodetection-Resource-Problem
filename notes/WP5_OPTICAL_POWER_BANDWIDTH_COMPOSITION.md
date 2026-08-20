# WP5 — Optical Power-Bandwidth Composition Target

**Date:** 2026-08-19

## Purpose

WP4 proves that an absolute microscopic light–matter coupling scale is necessary. WP5 asks whether existing optical response bounds can supply a physically meaningful, architecture-independent cap on that coupling over the optical bandwidth required by a photodetection task.

This note does **not** yet claim a completed theorem. It fixes the composition problem precisely enough to attack.

---

# 1. Why a single-frequency coupling cap is insufficient

Suppose a resonant optical environment produces an extremely large spontaneous-emission/absorption coupling at carrier frequency `omega_0`. A single-frequency quantity such as

\[
\gamma(\omega_0)
\]

can be made very large in idealized high-Q or strongly confined structures.

However, a detector required to recover temporal modulation at baseband frequency `Omega` does not interact with a perfectly monochromatic optical field. Amplitude/phase modulation of a carrier produces sidebands near

\[
\omega_0\pm\Omega.
\]

Therefore a detector that preserves optical information over

\[
|\Omega|\le\Omega_s
\]

must possess adequate optical coupling over a **nonzero optical frequency interval** around the carrier.

This immediately suggests that arbitrary-bandwidth LDOS / absorption bounds are the relevant electromagnetic resource, not a pointwise Purcell factor.

---

# 2. Generic optical coupling spectrum

For weak electric-dipole coupling in a passive linear environment, write the local spectral rate schematically as

\[
\gamma(\omega)
=\frac{2}{\hbar}
\mathbf d^*\cdot
\operatorname{Im}\mathbf G(\mathbf r_0,\mathbf r_0;\omega)
\cdot\mathbf d
\times C(\omega),
\]

where `G` is the appropriate electromagnetic Green tensor and `C(omega)` collects the conventional frequency/unit prefactor.

The exact normalization must be fixed before publication. The important structure is

\[
\gamma(\omega)\propto
|d|^2\rho_{\rm proj}(\omega).
\]

Thus the microscopic coupling decomposes into

\[
\boxed{
\text{matter oscillator strength}
\times
\text{photonic LDOS/environment response}.
}
\]

---

# 3. Matter-side budget

TRK/f-sum rules constrain integrated transition strength. For a single free-space electric-dipole transition from a stable initial manifold,

\[
|d|^2\le\frac{3\hbar e^2N_e}{2m_e\omega_0}.
\]

This supplies a matter-side resource `C_matter`, but it is extensive in participating electron number and is not sufficient by itself.

---

# 4. Electromagnetic-side finite-band budget

Shim, Fan, Johnson, and Miller (PRX 9, 011043 (2019)) prove:

- an all-frequency LDOS sum rule;
- geometry/material upper bounds on the sum-rule constant;
- arbitrary-bandwidth LDOS power-bandwidth bounds from causality and energy conservation.

In their notation, the scattered LDOS obeys an all-frequency sum rule of the form

\[
\int_0^\infty \rho_{\rm scat}(\omega)d\omega
=\alpha_{\rm LDOS},
\]

where `alpha_LDOS` is an electrostatic constant determined by geometry/material response. Their finite-band theory provides stronger bounds for a chosen nonzero bandwidth and introduces material susceptibility and geometric resources.

For UPRP, abstract this as a positive functional bound

\[
\boxed{
\int d\omega\,W_{\Omega_s}(\omega-\omega_0)
\rho_{\rm proj}(\omega)
\le
C_{\rm EM}(\omega_0,\Omega_s;\chi,\mathcal G),
}
\]

where

- `W_Omega` is a specified normalized optical-band window;
- `chi` denotes material susceptibility information;
- `G` denotes allowed geometry/footprint/separation resources.

The task is to extract the tightest usable `C_EM` from existing optical-bound literature rather than rederive those results unnecessarily.

---

# 5. Desired coupling bound

Combining matter and electromagnetic resources should yield

\[
\boxed{
\int d\omega\,W_{\Omega_s}(\omega-\omega_0)
\gamma(\omega)
\le
C_{LM}(\omega_0,\Omega_s;C_{\rm matter},C_{\rm EM}).
}
\]

This `C_LM` is the candidate missing absolute coupling resource.

A pointwise cap need not exist for arbitrarily narrow resonances. A finite-band average is both physically meaningful and consistent with known optical power-bandwidth theory.

---

# 6. Carrier-sideband to baseband lemma — target

Let an optical temporal mode be a narrowband carrier with envelope `a(t)`:

\[
E^{(+)}(t)=a(t)e^{-i\omega_0t}.
\]

If the envelope contains Fourier components only for

\[
|\Omega|\le\Omega_s,
\]

then the physical optical spectrum lies in

\[
\omega\in[\omega_0-\Omega_s,\omega_0+\Omega_s].
\]

A necessary condition for high information-transfer efficiency over the baseband is therefore that the optical absorption/coupling map preserve the relevant field-state distinguishability across that sideband interval.

The theorem target is an inequality of the form

\[
\bar\eta_{\mathcal I}^{\rm optical}(\Omega_s)
\le
\mathcal B_{\rm opt}
[C_{LM}(\omega_0,\Omega_s)],
\]

with no single-mode-cavity assumption.

This is the missing bridge between existing optical power-bandwidth theory and UPRP.

**Status:** OPEN.

---

# 7. Composition with WP3

Suppose the optical-side theorem supplies an effective cap

\[
\gamma_{\rm eff}(\Omega_s)\le\gamma_{\max}(\Omega_s).
\]

The restricted Markov gateway theorem then gives

\[
\Lambda_{\rm micro}(\Omega_s)
=
\frac{\mathcal A\gamma_{\max}(\Omega_s)[n+1]}{f_*}
\,g^{-1}(\Sigma/f_*).
\]

For a flat baseband information task,

\[
\bar\eta_{\mathcal I}^{\rm transducer}(\Omega_s)
\le
\eta_q
\frac{\Lambda_{\rm micro}(\Omega_s)}{\Omega_s}
\arctan\frac{\Omega_s}{\Lambda_{\rm micro}(\Omega_s)}.
\]

If the optical frontend itself has efficiency ceiling

\[
\bar\eta_{\mathcal I}^{\rm optical}(\Omega_s)
\le B_{\rm opt}(\Omega_s),
\]

data processing implies the total efficiency cannot exceed either stage:

\[
\boxed{
\bar\eta_{\mathcal I}^{\rm total}(\Omega_s)
\le
\min\!\left[
B_{\rm opt}(\Omega_s),
B_{\rm trans}(\Omega_s)
\right].
}
\]

For cascaded conditionally independent channels, stronger multiplicative bounds may exist, but `min` is always the safe data-processing ceiling.

A target requirement

\[
\bar\eta_{\mathcal I}^{\rm total}(\Omega_s)\ge r
\]

then implies two simultaneous necessary conditions:

\[
B_{\rm opt}(\Omega_s)\ge r,
\qquad
B_{\rm trans}(\Omega_s)\ge r.
\]

This is the clean composition architecture.

---

# 8. Important distinction from known optical bounds

The optical literature already proves limits on LDOS, absorption, scattering, and external coupling. UPRP should **not** rebrand those limits as new detector theorems.

The potentially new step is to turn them into a bound on

\[
\frac{F_{\rm electrical\ output}}
{F_{\rm incident\ optical\ field}}
\]

over a specified temporal-information band, and then combine that with the thermokinetic transducer bound.

---

# 9. Passive versus active optical environments

Initial composition theorem should restrict to passive linear optical environments.

Reason: in gain media, simple spontaneous-emission formulas based only on passive LDOS can fail and extra quantum pumping/noise channels appear. Franke et al., PRL 127, 013602 (2021), explicitly demonstrate this issue.

An active/nonreciprocal extension would need to count the pump/free-energy and quantum-noise resources explicitly.

---

# 10. Single-mode sanity check

For a simple cavity mode,

\[
F_P\propto Q/V_{\rm eff},
\qquad
\kappa\sim\omega_0/Q.
\]

Thus

\[
F_P\kappa\propto\omega_0/V_{\rm eff}.
\]

This illustrates the expected structure: arbitrarily large peak Purcell enhancement obtained by increasing `Q` simultaneously narrows the optical bandwidth. A finite modulation task cannot exploit infinite `Q` at fixed bandwidth.

This is only a sanity check, not the general theorem.

---

# 11. Strongest current conjecture

There exists a passive-linear, finite-resource detector theorem of the schematic form

\[
\boxed{
\bar\eta_{\mathcal I}(\Omega_s)\ge r
\Longrightarrow
\Omega_s
\le
F\!\left(
C_{\rm TRK},
C_{\rm EM},
\mathcal A,
\Sigma,
f_*,
T,
\omega_0,
r
\right),
}
\]

where `C_TRK` controls matter oscillator strength and `C_EM` controls finite-band electromagnetic response.

The exact functional form is OPEN.

---

# 12. Falsification tests

Before accepting any composition theorem, test:

1. lossless high-Q cavity (`Q -> infinity`);
2. mode volume `V_eff -> 0`;
3. large participating electron number `N_e -> infinity`;
4. parallel detector replication;
5. slow-light waveguide LDOS singularity;
6. plasmonic near-field separation `d -> 0`;
7. nonlocal/material-dispersion regularization;
8. active/gain optical environment;
9. coherent drive versus incoherent/thermal light;
10. direct optical-to-electrical feedthrough;
11. broadband ideal photon counter;
12. strong/ultrastrong coupling where golden-rule rates cease to be valid.

Each diverging limit must either be excluded by an explicit resource or shown not to increase the task-normalized information efficiency.

---

# 13. Immediate next derivation

Extract from the optical-bound literature an explicit finite-band inequality for the projected LDOS or absorption relevant to a localized detector, then combine it with the TRK matter bound. The result should be expressed as a bound on a physically normalized optical coupling functional rather than on `gamma(omega_0)` alone.
