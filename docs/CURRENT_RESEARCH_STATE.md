# Current Research State

**Date:** 2026-08-20

This is the first-stop replacement-agent summary. The repository, not chat history, is authoritative.

Read first:

1. `AGENTS.md`
2. `notes/RESEARCH_LOG_ROUND7.md`
3. `notes/WP11_SPATIAL_DELAY_INFORMATION_THEOREM.md`
4. `notes/WP11_DISSIPATIVE_MATCHING_THEOREM.md`
5. `notes/WP11_MINIMAL_FINITE_LEVEL_SEMICONDUCTOR_DETECTOR.md`
6. `notes/WP11_SHOCKLEY_RAMO_KANE_RESOURCE_BOUND.md`
7. `notes/WP12_READOUT_FILTER_INFORMATION_INVARIANCE.md`
8. `notes/WP12_SIMPLE_RC_AMPLIFIER_INFORMATION_BOUND.md`
9. `notes/WP8_UV_NON_GAUSSIAN_INSTABILITY.md`
10. `notes/WP10_TRK_POINTER_RESOURCE_AUDIT.md`
11. WP5/WP4/WP3 core notes.

---

## Central objective

Determine which physical resources are necessary and/or sufficient for a finite-temperature photodetector to transfer information from an incident optical field into an electrical record with specified sensitivity and **information bandwidth**.

The project has converged toward a no-go/repair program: repeatedly show that an apparently sufficient resource set can hide an unbounded degree of freedom, then identify the additional microscopic resource that closes the loophole.

Core metric:

\[
\boxed{\eta_I=F_{\rm electrical}/F_{\rm incident}^Q.}
\]

For weak coherent/Poisson flux modulation,

\[
\eta_I(\omega)=\Phi_0|\chi_{Y\Phi}(\omega)|^2/S_Y(\omega).
\]

---

## Most important conceptual correction

**Latency, amplitude bandwidth, and information bandwidth are different.**

- A deterministic known delay changes phase but not stationary spectral FI.
- A deterministic invertible LTI filter applied to signal and upstream noise leaves `|chi|^2/S` invariant wherever its transfer function is nonzero.
- Information loss requires stochastic/unresolved timing, inaccessible modes/coarse graining, downstream additive noise, finite sampling/quantization/observation resources, or exact spectral nulls.

Therefore conventional `f_tr` or `f_RC` cannot be inserted into a universal information theorem without specifying the accessible output/noise model.

---

## Classical/Markov foundation

Exact finite-state response/noise machinery is solved.

Strongest no-go:

\[
\boxed{
\{T,\hbar\omega_0,\text{detailed balance},f_*,\mathcal A,\Sigma,\text{edge EPRs},\eta_q\}
\not\Rightarrow\text{finite absolute speed}.
}
\]

A reversible rare-fast construction keeps all displayed stationary resources finite while an absolute microscopic rate diverges.

**Necessary resource:** absolute microscopic coupling/rate scale.

Restricted repair: fixed optical gateway kinetics plus throughput/EPR/activity bounds produces a finite event-record timing/information ceiling.

---

## Finite-band optical capture

WP5 uses coherent-state QFI data processing plus rigorous T-operator oscillator/sum-rule bounds. For a small reciprocal detector,

\[
\bar\eta_I(\Omega_s)
\le
\min\left[
1,
\frac{\pi}{4cA\Omega_s}
\min(\omega_p^2V,(\omega_0+\Omega_s)^2\alpha_{\rm stat})
\right]
\]

under stated assumptions.

Optical sum-rule/power-bandwidth theory is prior art; UPRP uses it as the optical resource layer.

---

## Quantum apparatus resource

For coherent displacement through passive mixing, directional SLD-Stam gives

\[
1/J_C\ge\tau/J_A+(1-\tau)/J_B.
\]

For coherent input and arbitrary pointer excitation budget `N`,

\[
\boxed{
F_{\rm elec}/F_{\rm in}
\le\frac\tau{\tau+(1-\tau)\xi(N)},
\quad
\xi(N)=(\sqrt{N+1}-\sqrt N)^2.
}
\]

This is globally tight in the passive-linear single-effective-mode model.

Critical WP8 correction: finite nonequilibrium free energy does not create an exact smooth Gaussian optimum in an unrestricted harmonic pointer. High-Fock coherences create a UV instability for every `D0>0`; diagonal energy moments do not cure it.

Exact finite-support repair for preparation subspace `S` and signal generator `G`:

\[
\boxed{
\sup_{\rho\subset S}F_Q(\rho,G)
=4\inf_c\lambda_{\max}[\Pi_S(G-cI)^2\Pi_S].
}
\]

TRK/f-sum alone does not uniformly bound this pointer resource for excited states because signed upward/downward oscillator strengths cancel.

---

## WP11 finite-level semiconductor embedding

Minimal coherent chain:

\[
|F\rangle\xleftrightarrow{g}|X\rangle\xleftrightarrow{\kappa}|C\rangle.
\]

For weak single-rail optical encoding and binary electrical charge readout,

\[
\boxed{
\eta_I(t)=
\frac{4g^2\kappa^2}{(g^2+\kappa^2)^2}
\sin^4\left(\frac{\sqrt{g^2+\kappa^2}t}{2}\right).
}
\]

Perfect coherent transfer requires `g=kappa`.

With charge observable `Q=e|C><C|`,

\[
\boxed{\|I\|=e|\kappa|.}
\]

General finite electrical subspace:

\[
\boxed{\|I\|\le W_S\Delta Q_S/(2\hbar)}
\]

and the bound is tight.

Shockley–Ramo/band mapping:

\[
Q_w=q\phi_w(\hat r),
\qquad
\boxed{\|I_w\|\le |q|v_S/\ell_w}
\]

with `ell_w^{-1}=sup|grad phi_w|`. Thus a binary-electron internal coupling obeys

\[
\boxed{|\kappa|\le\min[W_S/(2\hbar),v_S/\ell_w].}
\]

The HgCdTe Kane velocity `~1.07e6 m/s` is only an illustrative ballistic microscopic scale; it is not a predicted detector bandwidth.

---

## Spatial transport information theorem

For captured Poisson events with independent delay `D`, timestamp/count readout gives

\[
\boxed{
\eta_I(\omega)=\eta_c|\mathbb E e^{-i\omega D}|^2.
}
\]

For unresolved capture positions,

\[
\boxed{
\eta_I(\omega)=
\eta_c\left|\int p_{\rm abs}(r)e^{-i\omega D(r)}dr\right|^2.
}
\]

If capture position is retained as side information, deterministic geometry delay can be corrected event-by-event.

Uniform unresolved depth in a planar layer:

\[
\boxed{
\eta_I=\eta_c\operatorname{sinc}^2(\omega L/2v),
\quad
f_{1/2}=0.4429464707\ldots\,v/L.
}
\]

Thus the familiar transit coefficient arises from **unresolved delay dispersion**.

With dark counts `d`, signal flux `Phi0`, and independent timing stages,

\[
\boxed{
\eta_I=
\frac{\eta_c^2\Phi_0}{\eta_c\Phi_0+d}
\prod_j|H_j(\omega)|^2.
}
\]

---

## Dissipative capture/readout matching

Minimal irreversible model:

\[
H=\hbar g(|F\rangle\langle X|+h.c.),
\qquad
L=\sqrt\Gamma|C\rangle\langle X|.
\]

At resonance,

\[
\boxed{\langle T\rangle=\Gamma/(4g^2)+2/\Gamma.}
\]

Both mean and variance are minimized at

\[
\boxed{\Gamma_{\rm opt}=2\sqrt2\,g.}
\]

Too-large `Gamma` gives a quantum-Zeno capture penalty. Generic Zeno tradeoffs in photon detection are established prior art.

With detuning `Delta`,

\[
\boxed{
\langle T\rangle=
\Gamma/(4g^2)+2/\Gamma+\Delta^2/(\Gamma g^2),
}
\]

\[
\boxed{\Gamma_{\rm opt}=2\sqrt{\Delta^2+2g^2}.}
\]

---

## WP12 electrical readout information

A deterministic RC pole alone is not an information limit.

For parallel RC with input-side current noise `S_u` and downstream voltage noise `S_e`,

\[
\boxed{
K_V(\omega)=
\frac{|\chi_I|^2}
{S_u+\frac{S_e}{R^2}[1+(\omega RC)^2]}.
}
\]

For white noise and flat intrinsic response,

\[
\boxed{
f_{1/2}^{I}
=\frac1{2\pi RC}
\sqrt{1+S_uR^2/S_e}.}
\]

The conventional RC pole equals the FI half-power point only in the downstream-voltage-noise-dominated limit.

---

## Current resource hierarchy

The best-supported structure is now

\[
\boxed{
\text{finite source task}
+\text{finite-band optical capture}
+\text{absolute microscopic optical/internal coupling}
+\text{finite apparatus preparation/support/generator resource}
+\text{semiconductor current/velocity/energy-span resource}
+\text{optical/electrical geometry}
+\text{unresolved timing/noise/coarse-graining resources}
+\text{ongoing thermokinetic resources}
+\text{readout noise/sampling resources}
\Rightarrow
\text{finite information-transfer ceiling}.
}
\]

Recurring failure mode: an unbounded resource hides in a vanishing-weight, canceling, or unobserved sector.

---

## Novelty boundaries

Do not claim novelty for generic:

- transit-time `~0.44/tau` scaling;
- RC amplitude bandwidth;
- Shockley–Ramo detector signals;
- FI applied to semiconductor detector waveforms/DOI estimation;
- quantum-Zeno/anti-Zeno detector backaction;
- non-Gaussian/squeezing metrology;
- optical sum rules/T-operator bounds.

Candidate novelty remains the **source-normalized photodetection resource-completeness chain**, especially proving which familiar speed metrics do and do not correspond to actual information loss.

---

## Immediate next gates

1. Replace flat Markov `Gamma` with a structured semiconductor/contact/phonon reservoir and derive Zeno/anti-Zeno information effects.
2. Compose WP5 finite-band optical capture with WP11 spatial absorption-delay information to price absorption localization.
3. Extend WP12 to correlated amplifier noise and finite ADC/sampling resources.
4. Analyze avalanche/multiplication: deterministic gain cannot create FI; stochastic multiplication, excess noise, and bias/pump free energy must be explicit.
5. Continue novelty audit and record all failed shortcuts.
