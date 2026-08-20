# AGENTS.md

## Purpose

Durable handoff for **The Universal Photodetection Resource Problem (UPRP)**. The repository, not chat context, is authoritative.

Research is analytical/theoretical only. Numerical algebra/simulation is allowed for validation. Do not make experiments, fabrication, sample procurement, or measurement campaigns necessary next steps.

## Read first

A replacement agent should read in this order:

1. `docs/CURRENT_RESEARCH_STATE.md`
2. `notes/RESEARCH_LOG_ROUND7.md`
3. `notes/WP11_SPATIAL_DELAY_INFORMATION_THEOREM.md`
4. `notes/WP11_DISSIPATIVE_MATCHING_THEOREM.md`
5. `notes/WP11_DISSIPATIVE_DETUNING_EXTENSION.md`
6. `notes/WP11_MINIMAL_FINITE_LEVEL_SEMICONDUCTOR_DETECTOR.md`
7. `notes/WP11_SHOCKLEY_RAMO_KANE_RESOURCE_BOUND.md`
8. `notes/WP12_READOUT_FILTER_INFORMATION_INVARIANCE.md`
9. `notes/WP12_SIMPLE_RC_AMPLIFIER_INFORMATION_BOUND.md`
10. `notes/WP8_UV_NON_GAUSSIAN_INSTABILITY.md`
11. `notes/WP8_GENERAL_FINITE_SUBSPACE_GENERATOR_THEOREM.md`
12. `notes/WP10_TRK_POINTER_RESOURCE_AUDIT.md`
13. `notes/WP5_T_OPERATOR_FINITE_BAND_CAPTURE.md`
14. `notes/WP4_MICROSCOPIC_OPTICAL_COUPLING_NO_GO.md`
15. `notes/WP3_GATEWAY_RESOURCE_THEOREM.md`
16. `docs/LITERATURE_MAP.md`
17. `docs/FORMALISM.md`

Older research logs and WP0–WP9 notes preserve derivations, failed conjectures, corrections, and novelty audits.

---

# Project objective

Determine which physical resources are necessary and/or sufficient for a finite-temperature photodetector to transfer information from an incident optical field into an electrical measurement record with specified sensitivity and temporal information bandwidth.

The project is now a **resource-completeness / no-go + repair program**, not a search for one naive sensitivity-bandwidth-temperature product.

---

# Core information metric

Use

\[
\boxed{\eta_{\mathcal I}=F_{\rm electrical}/F_{\rm incident}^{Q}}
\]

for the same encoded parameter.

For coherent/Poisson weak flux modulation,

\[
\eta_{\mathcal I}(\omega)=\Phi_0|\chi_{Y\Phi}(\omega)|^2/S_Y(\omega).
\]

Use a finite source task

\[
\bar\eta_{\mathcal I}
=\frac{\int(d\omega/2\pi)\mathcal J_{\rm in}\eta_{\mathcal I}}
{\int(d\omega/2\pi)\mathcal J_{\rm in}}
\]

rather than an unweighted all-frequency integral.

---

# Mandatory conceptual distinction — new central result

Do **not** identify conventional detector `-3 dB` bandwidth with UPRP information bandwidth without an explicit observation/noise model.

Three different quantities must be separated:

1. **latency** — deterministic propagation/response delay;
2. **amplitude bandwidth** — attenuation/phase of a waveform or transfer function;
3. **information bandwidth** — degradation of source-normalized Fisher/QFI in the accessible output record.

A deterministic known delay has `|e^{-i omega tau}|=1` and therefore no stationary spectral-FI loss.

A deterministic invertible LTI filter applied to signal and all upstream noise obeys

\[
\boxed{|\chi_Y|^2/S_Y=|\chi_X|^2/S_X}
\]

where the transfer function is nonzero.

Information loss instead requires inaccessible/coarse-grained degrees of freedom, stochastic timing, downstream additive noise, finite sampling/quantization/observation resources, or exact spectral nulls.

This correction supersedes any older wording that treated transit/RC latency as automatically equivalent to information bandwidth.

---

# Established classical/Markov resource result

Exact finite-state response/noise machinery is solved.

Strongest classical no-go:

\[
\boxed{
\{T,\hbar\omega_0,\text{detailed balance},f_*,\mathcal A,\Sigma,\text{edge EPRs},\eta_q\}
\not\Rightarrow\text{finite detector speed}
}
\]

because an explicit reversible family hides diverging absolute rates in rare states while all listed stationary resources remain finite.

**Missing resource:** absolute microscopic coupling/transition scale.

Restricted repair: fixed optical gateway kinetics + finite EPR/activity/throughput gives a finite post-absorption escape-rate and event-record information ceiling. See WP3/WP4.

---

# Passive optical frontend — WP5

For coherent passive capture, QFI data processing plus rigorous T-operator sum rules gives finite-band capture ceilings. In a small reciprocal detector,

\[
\bar\eta_I(\Omega_s)
\le
\min\left[
1,
\frac{\pi}{4cA\Omega_s}
\min(\omega_p^2V,(\omega_0+\Omega_s)^2\alpha_{\rm stat})
\right]
\]

under the stated spatial/channel assumptions.

Optical power-bandwidth/sum-rule theory is prior art; UPRP uses it as one resource layer.

---

# Quantum apparatus resource — WP7/WP8

Finite-hypothesis branch:

\[
D_{\rm elec}/D_{\rm in}\le\min\{1,2G\}
\]

with interaction-action seminorm `G`. Trace-distance contraction does **not** imply SLD-QFI contraction; trine POVM counterexample proves this.

For coherent displacement through passive mixing, directional SLD-Stam gives

\[
\frac1{J_C}\ge\frac\tau{J_A}+\frac{1-\tau}{J_B}.
\]

For coherent input and arbitrary pointer excitation `N`,

\[
\boxed{
F_{\rm elec}/F_{\rm in}
\le\frac\tau{\tau+(1-\tau)\xi(N)},
\quad
\xi(N)=(\sqrt{N+1}-\sqrt N)^2.
}
\]

This is globally tight for the passive-linear single-effective-mode model.

### Critical WP8 UV result

Finite free energy in an unrestricted harmonic pointer is not enough for an exact smooth Gaussian optimum. High-Fock coherences generate a UV instability for every `D0>0`; energy moments/complete diagonal energy data do not remove it.

A finite preparation subspace `S` and bounded signal generator `G` repair the problem exactly:

\[
\boxed{
\sup_{\rho\subset S}F_Q(\rho,G)
=4\inf_c\lambda_{\max}[\Pi_S(G-cI)^2\Pi_S].
}
\]

Finite level count alone is insufficient if the absolute generator scale can diverge.

TRK/f-sum alone also fails for arbitrary excited pointer states because signed upward/downward oscillator strengths can cancel. See WP10.

---

# WP11 — explicit semiconductor detector embedding

## Exact coherent three-node detector

\[
|F\rangle\xleftrightarrow{g}|X\rangle\xleftrightarrow{\kappa}|C\rangle.
\]

For weak single-rail optical encoding and binary charge readout,

\[
\boxed{
\eta_I(t)=
\frac{4g^2\kappa^2}{(g^2+\kappa^2)^2}
\sin^4\left(\frac{\sqrt{g^2+\kappa^2}t}{2}\right).
}
\]

Time-maximized transfer is unity iff `g=kappa`.

With `Q=e|C><C|`,

\[
\boxed{\|I\|=e|\kappa|.}
\]

For finite electrical subspace with Hamiltonian span `W_S` and charge span `Delta Q_S`,

\[
\boxed{\|I\|\le W_S\Delta Q_S/(2\hbar)}
\]

and the bound is tight.

## Shockley–Ramo / band-velocity mapping

For weighting potential `phi_w`,

\[
Q_w=q\phi_w(\hat r),
\qquad I_w=(i/\hbar)[H,Q_w].
\]

With velocity capacity `v_S` and weighting length `ell_w=1/sup|grad phi_w|`,

\[
\boxed{\|I_w\|\le |q|v_S/\ell_w.}
\]

Binary-electron internal coupling therefore satisfies

\[
\boxed{
|\kappa|\le
\min[W_S/(2\hbar),v_S/\ell_w].
}
\]

A HgCdTe Kane velocity near `1.07e6 m/s` is an illustrative ballistic microscopic scale only, not a detector bandwidth.

---

# WP11 spatial-delay information theorem

For independently captured Poisson events with random delay `D`, event-timestamp information is

\[
\boxed{
\eta_I^{\rm timestamp}(\omega)
=\eta_c|\mathbb E e^{-i\omega D}|^2.
}
\]

For unresolved capture-position density `p_abs(r)` and deterministic transport delay `D(r)`,

\[
\boxed{
\eta_I(\omega)=
\eta_c\left|\int p_{\rm abs}(r)e^{-i\omega D(r)}dr\right|^2.
}
\]

If capture position is retained as side information, deterministic geometry delay can be corrected and this loss disappears.

Uniform unresolved depth in a planar layer gives

\[
\boxed{
\eta_I=\eta_c\operatorname{sinc}^2(\omega L/2v),
\quad
f_{1/2}=0.4429464707\ldots\,v/L.
}
\]

This recovers the conventional `~0.44/tau` transit coefficient as **delay dispersion**, not deterministic latency.

With dark counts `d`, flux `Phi0`, and independent delays,

\[
\boxed{
\eta_I
=\frac{\eta_c^2\Phi_0}{\eta_c\Phi_0+d}
\prod_j|H_j(\omega)|^2.
}
\]

---

# WP11 dissipative matching

Minimal coherent capture + irreversible electrical localization:

\[
H=\hbar g(|F\rangle\langle X|+h.c.),
\qquad L=\sqrt\Gamma|C\rangle\langle X|.
\]

At resonance,

\[
\boxed{\langle T\rangle=\Gamma/(4g^2)+2/\Gamma.}
\]

The mean and variance are minimized at

\[
\boxed{\Gamma_{\rm opt}=2\sqrt2\,g}
\]

with `mean=sqrt(2)/g` and `sigma=1/(sqrt(2)g)`.

Too-large `Gamma` enters a quantum-Zeno regime; generic Zeno detector tradeoffs are prior art.

With detuning `Delta`,

\[
\boxed{
\langle T\rangle=
\Gamma/(4g^2)+2/\Gamma+\Delta^2/(\Gamma g^2),
}
\]

\[
\boxed{
\Gamma_{\rm opt}=2\sqrt{\Delta^2+2g^2}.
}
\]

---

# WP12 readout-circuit information

A known deterministic RC pole alone does not destroy FI.

For parallel RC with input-side current noise `S_u` and downstream voltage noise `S_e`,

\[
\boxed{
K_V(\omega)=
\frac{|\chi_I|^2}
{S_u+\frac{S_e}{R^2}[1+(\omega RC)^2]}.
}
\]

For white noise/flat intrinsic response,

\[
\boxed{
f_{1/2}^{I}
=\frac1{2\pi RC}
\sqrt{1+S_uR^2/S_e}.}
\]

Only when downstream voltage noise dominates does the FI half-power point reduce to the conventional RC amplitude pole.

---

# Current resource hierarchy

The strongest structure now supported by explicit no-go/repair pairs is

\[
\boxed{
\text{finite source task}
+\text{finite-band optical capture}
+\text{absolute microscopic coupling}
+\text{finite apparatus preparation/support/generator resource}
+\text{semiconductor transport/current resource}
+\text{optical/electrical geometry and unresolved timing statistics}
+\text{ongoing thermokinetic resources}
+\text{readout noise/sampling resources}
\Longrightarrow
\text{finite information-transfer ceiling}
}
\]

under explicit model assumptions.

The recurring failure mode is **hidden resource in a vanishing-weight or unobserved sector**.

---

# Novelty constraints

Do not claim novelty for:

- generic photodetector gain/speed tradeoffs;
- transit-time `~0.44/tau` scaling;
- RC amplitude bandwidth;
- Shockley–Ramo detector signals;
- Fisher information applied generically to semiconductor detector signals;
- quantum-Zeno/anti-Zeno measurement backaction;
- squeezing/non-Gaussian displacement sensing;
- thermodynamic metrology resources;
- optical sum rules/T-operator bounds.

Current candidate novelty is the **source-normalized photodetection resource-completeness chain**, including explicit demonstrations that deterministic latency/amplitude attenuation need not reduce information and identification of the hidden stochastic/noise/coarse-graining resources that do.

---

# Highest-priority next work

1. Replace flat Markov `Gamma` in WP11 by a structured semiconductor/contact/phonon spectral density and identify Zeno vs anti-Zeno regimes.
2. Compose WP5 finite-band optical capture with WP11 spatial absorption-delay information: determine the resource cost of sharply localizing absorption while maintaining broad optical bandwidth.
3. Extend WP12 to correlated amplifier voltage/current noise and finite ADC/sampling resources.
4. Analyze avalanche/multiplication: deterministic gain is information-invariant; stochastic multiplication/excess noise and bias/pump free energy must be explicit.
5. Continue theorem-level novelty audit.

---

# Recordkeeping

After every substantive result:

- create/update a dedicated derivation note;
- add a numbered research-log checkpoint when direction changes;
- update `AGENTS.md` and `docs/CURRENT_RESEARCH_STATE.md`;
- preserve failed conjectures and corrections.

Status vocabulary: **PROVED**, **VERIFIED**, **CONJECTURE**, **COUNTEREXAMPLE**, **OPEN**, **BLOCKED**, **REJECTED**.
