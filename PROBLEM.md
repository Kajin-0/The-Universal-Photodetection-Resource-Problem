# Formal Problem Statement

**Updated:** 2026-08-20

## 1. Scientific objective

Determine which finite physical resources are necessary and/or sufficient for a finite-temperature photodetector to transfer information from an incident optical field into an **accessible electrical record** with specified efficiency and temporal information bandwidth.

The project is explicitly agnostic between:

- a universal bound;
- a no-go theorem for an incomplete resource set;
- a hierarchy of restricted theorems;
- a resource-completeness result identifying what must be specified before a finite bound exists.

The project no longer assumes that a simple sensitivity-bandwidth-temperature product exists.

---

## 2. Core information normalization

For an optical parameter `theta`, define

\[
\boxed{
\eta_{\mathcal I}
=\frac{F_{\rm electrical}}
{F_{\rm incident}^{Q}}
}
\]

for the same encoded parameter.

For coherent/Poisson weak photon-flux modulation in a stationary Gaussian/linear record,

\[
\boxed{
\eta_{\mathcal I}(\omega)
=\Phi_0\frac{|\chi_{Y\Phi}(\omega)|^2}{S_Y(\omega)}.
}
\]

This is the temporal analogue of DQE and is not itself a novelty claim.

A finite optical information task must be specified. If `J_in(omega)` is the incident QFI spectral density,

\[
\boxed{
\bar\eta_{\mathcal I}
=
\frac{\int(d\omega/2\pi)\mathcal J_{\rm in}(\omega)\eta_{\mathcal I}(\omega)}
{\int(d\omega/2\pi)\mathcal J_{\rm in}(\omega)}.
}
\]

Do not use an unqualified all-frequency integral as a universal finite objective; an ideal continuous-time photon counter can have flat information efficiency in an ideal white point-process model.

---

## 3. Intrinsic versus measured electrical information

A central project correction is that **latency, amplitude bandwidth, and information bandwidth are not identical**.

### Intrinsic electrical boundary

Let the detector produce an electrical subsystem/state `rho_E(theta)` after inaccessible internal degrees are traced out. Define

\[
\boxed{
\eta_{\rm int}
=F_Q[\rho_E(\theta)]/F_{\rm incident}^{Q}.
}
\]

In a classical detector, replace `rho_E` by the complete accessible electrical trajectory `Z` and use path Fisher information.

### Measured record

Let a practical record `Y` be obtained from the intrinsic electrical record by a parameter-independent readout/coarse-graining channel:

\[
Z\to Y.
\]

Then

\[
\boxed{F_Y\le F_Z.}
\]

A one-to-one deterministic transformation preserves FI exactly.

Consequences:

- a deterministic known delay can be latency-only;
- deterministic known gain is FI-neutral;
- a deterministic invertible RC/LTI filter can preserve FI if signal and upstream noise are transformed together;
- timing dispersion, inaccessible latent variables, downstream noise, thresholding, dead time, quantization, finite sampling, or exact spectral nulls can destroy information.

Therefore every bandwidth theorem must state which electrical output record is accessible.

Primary framework: `notes/WP14_INTRINSIC_VS_MEASURED_INFORMATION_BANDWIDTH.md`.

---

## 4. Candidate universal/resource statement

Seek conditions under which

\[
\boxed{
\bar\eta_{\mathcal I}(\Omega_s)\ge q
\quad\Longrightarrow\quad
\Omega_s\le
\mathcal B(R_1,\ldots,R_n;q)
}
\]

or an equivalent pointwise/integrated information inequality, for all detectors in a precisely specified class.

The resource set is itself part of the problem.

Resources already shown to matter in explicit models include:

### Source/task resources

- finite optical temporal-mode/information task;
- incident photon flux/energy;
- optical carrier frequency.

### Optical frontend resources

- material oscillator-strength/plasma-frequency budget;
- static electromagnetic response;
- device volume/area/footprint;
- finite-band capture/channel resources.

### Microscopic coupling resources

- absolute light-matter coupling/rate scale;
- structured-reservoir spectral density/correlation time;
- energetic detuning.

### Apparatus/preparation resources

- pointer excitation/free energy;
- finite preparation support or equivalent UV regularizer;
- bounded signal-generator matrix elements.

### Semiconductor transport/electrical resources

- accessible electrical energy span;
- charge span;
- band/velocity scale;
- Shockley-Ramo weighting geometry;
- optical capture-position distribution;
- stochastic timing/localization statistics.

### Thermokinetic resources

- entropy-production rate;
- dynamical activity;
- throughput;
- bias/pump free-energy or power throughput.

### Readout resources

- downstream voltage/current noise;
- impedance/filter topology;
- sampling rate;
- quantization/ADC precision;
- dead time/threshold logic.

A central research goal is to identify which of these can be eliminated, combined, or replaced by weaker invariant resources.

---

## 5. Established no-go results

The following resource sets are already known to be incomplete within explicit model classes.

### 5.1 Stationary thermodynamics alone

There is a reversible finite-state family with fixed optical detailed balance, finite useful throughput, bounded activity, bounded total and edge entropy production, and finite efficiency while an absolute kinetic scale diverges.

Thus

\[
\boxed{
\{T,\hbar\omega_0,\text{detailed balance},f_*,\mathcal A,\Sigma,\eta_q\}
\not\Rightarrow
\text{finite absolute speed}.
}
\]

### 5.2 Coupling action alone in the quantum QFI branch

An arbitrarily pre-squeezed detector pointer can transfer nearly all coherent-state QFI at arbitrarily weak nonzero passive coupling. A preparation/metrological resource is necessary.

### 5.3 Free energy alone in an unrestricted ideal harmonic pointer

High-Fock coherences create a UV instability for every nonzero free-energy budget. Energy moments/diagonal energy data do not uniformly regularize it. A support/coherence/matrix-element-sensitive resource is needed.

### 5.4 TRK/f-sum alone for an excited pointer

Signed upward/downward oscillator strengths can cancel while individual transition strengths grow. A spectral/support/sign constraint is required.

### 5.5 Carrier velocity alone

An arbitrarily localized weighting field can generate arbitrarily sharp current pulses at fixed carrier speed. Electrical geometry must be specified.

### 5.6 Transit time or RC pole alone

A deterministic known delay or invertible filter need not reduce FI. Randomness/noise/coarse graining must be specified before conventional amplitude bandwidth becomes information bandwidth.

### 5.7 Integrated reservoir coupling weight alone

Arbitrarily narrow spectral features can evade coarse overlap-rate bounds. A reservoir spectral-regularity/correlation-time resource is required.

---

## 6. Established positive/repaired results

### 6.1 Finite-state Markov response/noise

Exact counted-current susceptibility and finite-frequency PSD formulas are solved for finite-state stationary Markov jump detectors.

### 6.2 Fixed optical-gateway thermokinetic theorem

For a reversible optical gateway with fixed reverse kinetics, nonzero throughput, bounded EPR, and bounded activity, the post-absorption escape rate is finite and an event-timestamp information rolloff follows.

### 6.3 Passive finite-band optical capture

For coherent passive frontend capture, rigorous T-operator sum rules give a finite-band optical-information ceiling under specified material/geometry assumptions.

### 6.4 Finite-support quantum pointer theorem

For preparation subspace `S` and generator `G`,

\[
\boxed{
\sup_{\rho\subset S}F_Q(\rho,G)
=4\inf_c\lambda_{\max}[\Pi_S(G-cI)^2\Pi_S].
}
\]

### 6.5 Minimal finite-level semiconductor theorem

For the coherent one-excitation chain

\[
|F\rangle\xleftrightarrow{g}|X\rangle\xleftrightarrow{\kappa}|C\rangle,
\]

weak single-rail optical encoding and binary charge readout give

\[
\boxed{
\eta_I(t)=
\frac{4g^2\kappa^2}{(g^2+\kappa^2)^2}
\sin^4\left(\frac{\sqrt{g^2+\kappa^2}t}{2}\right).
}
\]

The internal electrical coupling satisfies

\[
\|I\|=e|\kappa|
\]

and, in a finite electrical subspace,

\[
\|I\|\le W_S\Delta Q_S/(2\hbar).
\]

### 6.6 Shockley-Ramo transport resource

With velocity capacity `v_S` and weighting length `ell_w`,

\[
\boxed{\|I_w\|\le |q|v_S/\ell_w.}
\]

### 6.7 Spatial delay information theorem

For captured Poisson events delayed by random `D`,

\[
\boxed{
\eta_I^{\rm timestamp}(\omega)
=\eta_c|\mathbb E e^{-i\omega D}|^2.
}
\]

Uniform unresolved transit delays recover the conventional `0.442946... v/L` half-information coefficient.

### 6.8 Readout-noise composition

For parallel RC with input-side current noise `S_u` and downstream voltage noise `S_e`,

\[
\boxed{
f_{1/2}^{I}
=\frac1{2\pi RC}
\sqrt{1+S_uR^2/S_e}}
\]

under the white-noise/flat-intrinsic-response approximation.

---

## 7. Model hierarchy

The current research hierarchy is

\[
\text{finite-state Markov}
\subset
\text{finite-level coherent/dissipative detector}
\subset
\text{semiconductor transport + structured reservoirs}
\subset
\text{passive/active quantum input-output detector}
\subset
\text{general open quantum detector}.
\]

A sequence of rigorously stated restricted results is preferred over an overbroad false universal theorem.

---

## 8. Mandatory adversarial tests

Every proposed bound must survive or explicitly exclude:

1. output-unit/gain changes;
2. deterministic invertible filtering;
3. direct optical-to-electrical feedthrough;
4. source bandwidth/energy scaling;
5. parallel replication/extensivity;
6. rare-fast internal states;
7. fixed detailed balance with divergent bare coupling;
8. preloaded squeezing/metrological resource;
9. UV coherence tails/increasing support;
10. signed sum-rule cancellations;
11. arbitrarily sharp weighting geometry;
12. unresolved versus observed transport side information;
13. structured-reservoir spectral spikes;
14. active gain/pump resources;
15. downstream noise placement;
16. sampling/quantization/dead time;
17. whether the proposed resource merely renames the bandwidth being bounded.

---

## 9. Novelty discipline

Do not claim novelty for generic:

- detector sensitivity-speed/gain-bandwidth tradeoffs;
- transit-time `~0.44/tau` scaling;
- RC amplitude bandwidth;
- Shockley-Ramo signals;
- Fisher information applied generally to semiconductor detector waveforms;
- quantum Zeno/anti-Zeno control;
- non-Gaussian/squeezed metrology;
- thermodynamic metrology resources;
- TRK/f-sum rules;
- electromagnetic/T-operator power-bandwidth limits.

The surviving candidate novelty is the **photodetection-specific source-information resource-completeness program**: explicit no-go constructions showing why common resource sets and conventional speed metrics are insufficient, together with repaired information-transfer theorems once the missing microscopic resources and output record are specified.

---

## 10. Current next gates

1. Structured semiconductor phonon/contact reservoirs: derive coarse material spectral bounds rather than requiring the full `G(omega)`.
2. Joint finite-band optical capture + spatial localization: price how sharply absorption can be localized while retaining broadband capture.
3. Active multiplication: distinguish resolved-event FI from analog excess-noise penalties and include bias/free-energy resources.
4. Readout: correlated voltage/current noise and finite sampling/quantization.
5. Only after the general structure stabilizes, evaluate nontrivial MWIR/LWIR/room-temperature consequences.

---

## 11. Current status

The project now has multiple proved no-go/repair pairs and several restricted completion theorems. The exact fully universal theorem remains OPEN; the original statement that there was “no theorem/no impossibility proof” is obsolete.
