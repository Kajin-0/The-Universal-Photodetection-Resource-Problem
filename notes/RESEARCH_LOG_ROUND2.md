# Research Log — Round 2

**Date:** 2026-08-19

This file records the second major research round. Read it together with `notes/RESEARCH_LOG.md`.

---

## 1. Microscopic optical-reservoir mapping

For a weak-coupling bosonic optical transition,

\[
\Gamma_\uparrow=\gamma(\omega_0)n(\omega_0),
\qquad
\Gamma_\downarrow=\gamma(\omega_0)[n(\omega_0)+1].
\]

At thermal equilibrium,

\[
\Gamma_\uparrow/\Gamma_\downarrow=e^{-\beta\hbar\omega_0}.
\]

Therefore fixed photon energy and temperature constrain the **ratio** of optical rates but not the absolute coupling scale `gamma(omega_0)`.

**Status:** standard microscopic mapping / VERIFIED.

---

## 2. Stronger detailed-balance-preserving counterexample

Constructed the reversible three-state family

\[
0\xrightleftharpoons[bR]{aR}1,
\qquad
1\xrightleftharpoons[q]{cR}2,
\qquad
2\xrightleftharpoons[sR]{p}0.
\]

The optical ratio `a/b` is independent of `R` and can be fixed to `exp(-beta hbar omega_0)`.

Exact stationary probabilities are

\[
\pi_0=\frac{x}{R+x+y},\qquad
\pi_1=\frac{y}{R+x+y},\qquad
\pi_2=\frac{R}{R+x+y},
\]

with

\[
\Delta=ac+s(b+c),
\]

\[
x=\frac{p(b+c)+bq}{\Delta},
\qquad
y=\frac{(a+s)q+ap}{\Delta}.
\]

Consequences as `R -> infinity`:

- optical forward throughput `aR pi_0 -> ax > 0`;
- total stationary activity remains finite;
- every edge's forward and reverse stationary traffic remains finite;
- every edge EPR remains finite;
- cycle affinity `ln(acp/bqs)` remains fixed;
- successful first-exit detection branch probability `c/(b+c)` remains finite and nonzero;
- post-absorption first-exit rate `(b+c)R` diverges;
- timing jitter scales as `1/R` and timing bandwidth scales as `R`.

Therefore fixing temperature, photon energy, optical detailed balance, useful throughput, total stationary activity, total EPR, and even all edge EPRs is **not sufficient** to bound detector speed.

The only diverging resource is the absolute microscopic rate scale / light–matter coupling.

**Status:** PROVED for the stated finite-state reversible Markov event-detector class.

Full derivation: `notes/WP4_MICROSCOPIC_OPTICAL_COUPLING_NO_GO.md`.

---

## 3. Revised no-go theorem

A finite universal photodetection speed limit cannot depend only on thermodynamic ratios and stationary traffic/cost observables. At least one resource that constrains an **absolute microscopic transition scale** is necessary.

Candidate minimal resources:

- optical spectral coupling `gamma(omega)`;
- bath spectral density `J_EM(omega)`;
- projected LDOS times transition dipole strength;
- system-field interaction Hamiltonian norm or variance;
- a finite-band electromagnetic response functional;
- an optical oscillator-strength + photonic-environment resource pair.

**Status:** PROVED necessity within the Markov class; quantum-general necessity remains OPEN.

---

## 4. Microscopic repair of the WP3 gateway theorem

If a separate physical constraint supplies

\[
\gamma(\omega_0)\le\gamma_{\max},
\]

then

\[
d\le\gamma_{\max}[n(\omega_0)+1].
\]

The WP3 gateway theorem becomes

\[
\Lambda_{\rm micro}
=
\frac{\mathcal A\gamma_{\max}[n+1]}{f_*}
\,g^{-1}(\Sigma/f_*),
\]

and

\[
\eta_{\mathcal I}(\omega)
\le
\eta_q\frac{\Lambda_{\rm micro}^2}
{\Lambda_{\rm micro}^2+\omega^2}.
\]

Thus the abstract rate `d` has been replaced by an explicit microscopic optical-coupling cap.

**Status:** PROVED conditional completion for the restricted event-detector class.

---

## 5. Free-space TRK corollary

For a free-space electric-dipole transition,

\[
\Gamma_0=\frac{\omega_0^3|\mathbf d|^2}
{3\pi\epsilon_0\hbar c^3}.
\]

Using

\[
f_{01}=\frac{2m_e\omega_0}{3\hbar e^2}|\mathbf d|^2
\]

and `sum_f f_0f = N_e`, a single positive transition satisfies

\[
\Gamma_0\le
\frac{N_e e^2\omega_0^2}{2\pi\epsilon_0m_ec^3}
=2N_e\alpha\frac{\hbar\omega_0}{m_ec^2}\omega_0.
\]

Illustrative one-electron values:

- `lambda=10 um`: `Gamma_max ~= 6.67e5 s^-1` (`1/Gamma ~= 1.50 us`);
- `lambda=1.55 um`: `2.78e7 s^-1` (`36 ns`);
- `lambda=500 nm`: `2.67e8 s^-1` (`3.75 ns`).

This is **not** a universal photodetector bound because `N_e` is extensive and photonic environments can modify the LDOS/Purcell factor.

**Status:** DERIVED free-space corollary; physical scope deliberately narrow.

---

## 6. Electromagnetic-environment obstruction

Matter oscillator strength alone cannot close the theorem. Spontaneous emission is controlled by the electromagnetic Green tensor / LDOS, and photonic structuring can strongly enhance it. Therefore a complete bound needs both:

1. a **matter-side** oscillator-strength/electron-number resource; and
2. an **electromagnetic-side** LDOS/mode-volume/material-susceptibility/bandwidth resource.

Relevant existing work includes arbitrary-bandwidth LDOS and optical power-bandwidth bounds (Shim, Fan, Johnson, Miller, PRX 9, 011043 (2019)) and later LDOS optimization/bounds.

The crucial opportunity is that baseband photodetection of modulation up to `Omega_s` requires the optical frontend to accept carrier sidebands over a corresponding optical bandwidth. Thus a narrow, arbitrarily strong Purcell resonance cannot automatically provide arbitrarily high **information bandwidth**: optical power-bandwidth limits may constrain the required sideband coupling.

**Status:** promising composition route; not yet a proved UPRP theorem.

---

## 7. Important connection to Young–Sarovar–Léonard

The 2018 fully quantum photodetector model explicitly reports that in its dark-state configuration, near-perfect detection can be obtained as the optical coupling `gamma` and localization rate are made arbitrarily large compared with the photon-wavepacket timescale. This is precisely the degree of freedom isolated by the present no-go theorem.

Their result should be interpreted as demonstrating that photodetector tradeoffs can disappear when the absolute light–matter coupling scale is unconstrained. The missing-resource problem is therefore not artificial; it is already latent in the canonical fully quantum photodetector model.

**Status:** VERIFIED literature connection.

---

## 8. Current strongest research question

The project is now focused on:

> What is the weakest architecture-independent microscopic light–matter resource that, together with a finite optical task bandwidth and thermodynamic/kinetic budgets, yields a finite upper bound on optical-to-electrical information transfer speed?

The leading candidate is not a scalar temperature or entropy-production quantity. It is likely a coupling functional involving one or more of:

\[
\operatorname{Var}(H_{\rm int}),
\quad
\|H_{\rm int}\|,
\quad
|d|^2\rho_{\rm EM},
\quad
\text{TRK/f-sum budget},
\quad
\text{finite-band LDOS/absorption bound}.
\]

---

## 9. Next work

1. Derive a rigorous optical-side finite-band coupling bound by combining TRK with Green-tensor/LDOS power-bandwidth inequalities.
2. Translate baseband modulation bandwidth into required optical sideband bandwidth without assuming a single-mode cavity.
3. Attempt an implicit bound of the form

\[
\bar\eta_{\mathcal I}(\Omega_s)\ge r
\Rightarrow
\Omega_s\le F(\Sigma,\mathcal A,f_*,C_{\rm matter},C_{\rm EM}).
\]

4. Map the coupling resource to the input-output quantum photodetector formalism of Young–Sarovar–Léonard.
5. Compare with Nishiyama–Hasegawa temporal-FI speed limits, whose quantum resource involves interaction-Hamiltonian fluctuations.
6. Preserve the Markov no-go theorem even if the positive universal completion fails.
