# Research Log — Round 7

**Date:** 2026-08-20

## Purpose

Durable checkpoint for the transition from abstract quantum-apparatus resource theory to explicit semiconductor transport/readout physics. This round also contains a critical conceptual correction: conventional latency and amplitude bandwidth are not automatically Fisher-information bandwidth.

---

## 1. WP8 housekeeping correction

Issue #8 has been rewritten. The correct result is:

- squeezed-thermal Gaussian states are asymptotically optimal in the regular/BKM expansion as `D0 -> 0`;
- in the unrestricted ideal harmonic oscillator they are **not exact local optima for any D0>0** because arbitrarily high-Fock centered coherences produce a UV instability;
- energy moments/diagonal energy data do not cure that loophole;
- finite support plus bounded generator matrix elements gives an exact repair.

This correction is now explicit in Issue #8 and the dedicated WP8 notes.

---

## 2. Minimal finite-level semiconductor detector

Constructed the exact one-excitation chain

\[
|F\rangle\xleftrightarrow{g}|X\rangle\xleftrightarrow{\kappa}|C\rangle.
\]

For weak single-rail optical parameter encoding and binary charge readout,

\[
\boxed{
\eta_I(t)
=\frac{4g^2\kappa^2}{(g^2+\kappa^2)^2}
\sin^4\left(\frac{\sqrt{g^2+\kappa^2}t}{2}\right).
}
\]

Thus

\[
\boxed{
\eta_{\max}=\frac{4g^2\kappa^2}{(g^2+\kappa^2)^2}
}
\]

and perfect coherent transfer requires `g=kappa`.

Electrical charge observable `Q=e|C><C|` gives

\[
\boxed{\|I\|=e|\kappa|.}
\]

For arbitrary finite electrical subspace with Hamiltonian span `W_S` and charge span `DeltaQ_S`,

\[
\boxed{\|I\|\le W_S\Delta Q_S/(2\hbar)}
\]

and the inequality is tight.

Primary note: `WP11_MINIMAL_FINITE_LEVEL_SEMICONDUCTOR_DETECTOR.md`.

---

## 3. Shockley–Ramo / band-velocity mapping

For weighting potential `phi_w`,

\[
Q_w=q\phi_w(\hat r),
\qquad
I_w=(i/\hbar)[H,Q_w].
\]

With accessible velocity capacity `v_S` and weighting length

\[
\ell_w^{-1}=\sup|\nabla\phi_w|,
\]

\[
\boxed{\|I_w\|\le |q|v_S/\ell_w.}
\]

For a binary electron pointer,

\[
\boxed{|\kappa|\le v_S/\ell_w.}
\]

Combined finite-level cap:

\[
\boxed{
|\kappa|\le
\min[W_S/(2\hbar),v_S/\ell_w].
}
\]

A narrow-gap HgCdTe Kane velocity near `1.07e6 m/s` is a useful illustrative ballistic microscopic scale, not a detector bandwidth.

Primary note: `WP11_SHOCKLEY_RAMO_KANE_RESOURCE_BOUND.md`.

---

## 4. Weighting geometry is an independent resource

Finite carrier velocity alone does not bound the sharpness of the induced-current pulse if the weighting-potential swing is allowed to collapse into an arbitrarily small spatial region.

A finite weighting length regularizes current slew and signal-formation latency:

\[
|d\langle Q\rangle/dt|\le |q|v_{\max}/\ell_w.
\]

But this is **latency/slew**, not automatically information bandwidth.

The earlier transport-chain note has been corrected explicitly.

---

## 5. Critical distinction: latency, amplitude bandwidth, information bandwidth

A deterministic known delay

\[
D=\tau
\]

has transfer function

\[
H=e^{-i\omega\tau},
\qquad |H|=1.
\]

Therefore it changes phase/latency but not stationary spectral FI.

Likewise, a deterministic invertible LTI filter applied to signal and upstream noise gives

\[
\boxed{|\chi_Y|^2/S_Y=|\chi_X|^2/S_X}
\]

where its transfer function is nonzero.

Thus conventional `-3 dB` transit/RC amplitude bandwidth cannot be inserted directly as a fundamental information-bandwidth bound.

Information loss requires inaccessible/coarse-grained modes, stochastic timing, downstream additive noise, sampling/quantization, finite observation resources, or exact spectral zeros.

Primary notes:
- `WP11_SPATIAL_DELAY_INFORMATION_THEOREM.md`
- `WP12_READOUT_FILTER_INFORMATION_INVARIANCE.md`.

---

## 6. Exact spatial-delay information theorem

For Poisson/coherent photon events captured with probability `eta_c` and independently delayed by random variable `D`, event-timestamp readout obeys

\[
\boxed{
\eta_I^{\rm timestamp}(\omega)
=\eta_c|\mathbb E e^{-i\omega D}|^2.
}
\]

For unresolved spatial capture density `p_abs(r)` and deterministic geometry delay `D(r)`,

\[
\boxed{
\eta_I(\omega)
=\eta_c\left|\int p_{\rm abs}(r)e^{-i\omega D(r)}dr\right|^2.
}
\]

If the capture coordinate is retained as side information, deterministic geometry delay can be corrected event-by-event and this loss disappears.

Uniform unresolved absorption depth in a planar layer gives

\[
D\sim\mathrm{Uniform}(0,L/v),
\]

\[
\boxed{
\eta_I(\omega)=\eta_c\operatorname{sinc}^2(\omega L/2v).
}
\]

The half-information point is

\[
\boxed{f_{1/2}=0.4429464707\ldots\,v/L.}
\]

This recovers the familiar photodiode `~0.44/tau` transit coefficient as **unresolved delay dispersion**, not deterministic latency.

For Beer–Lambert conditional absorption depth, exact `H(omega)` was also derived.

---

## 7. Dark counts and stochastic timing compose cleanly

With incident flux `Phi0`, capture `eta_c`, dark rate `d`, and total independent delay characteristic `H`,

\[
\boxed{
\eta_I(\omega)
=\frac{\eta_c^2\Phi_0}{\eta_c\Phi_0+d}|H(\omega)|^2.
}
\]

Independent geometry/scattering/localization delays multiply in characteristic-function magnitude.

Primary note: `WP11_SPATIAL_DELAY_NOISE_EXTENSION.md`.

---

## 8. Exact readout-circuit information theorem

For parallel RC transimpedance

\[
Z=R/(1+i\omega RC),
\]

input-side current noise `S_u`, and downstream voltage noise `S_e`,

\[
\boxed{
K_V(\omega)
=\frac{|\chi_I|^2}
{S_u+\frac{S_e}{R^2}[1+(\omega RC)^2]}.
}
\]

For white noises and flat intrinsic response,

\[
\boxed{
\frac{K(\omega)}{K(0)}
=\frac1{1+\beta(\omega RC)^2},
\quad
\beta=\frac{S_e/R^2}{S_u+S_e/R^2}.
}
\]

Hence

\[
\boxed{
f_{1/2}^{I}
=\frac1{2\pi RC}
\sqrt{1+S_uR^2/S_e}.}
\]

Only in the downstream-voltage-noise-dominated limit does the FI half-power point coincide with the conventional RC amplitude pole.

Primary notes:
- `WP12_READOUT_FILTER_INFORMATION_INVARIANCE.md`
- `WP12_SIMPLE_RC_AMPLIFIER_INFORMATION_BOUND.md`.

---

## 9. Dissipative capture/readout matching theorem

Minimal coherent capture + irreversible electrical localization:

\[
H=\hbar g(|F\rangle\langle X|+h.c.),
\qquad
L=\sqrt\Gamma|C\rangle\langle X|.
\]

Exact mean detection time:

\[
\boxed{\langle T\rangle=\Gamma/(4g^2)+2/\Gamma.}
\]

Too-small `Gamma` gives slow localization; too-large `Gamma` suppresses capture by quantum-Zeno backaction.

The mean and timing variance are both minimized at resonance by

\[
\boxed{\Gamma_{\rm opt}=2\sqrt2\,g}
\]

with

\[
\boxed{\langle T\rangle_{\min}=\sqrt2/g,\quad
\sigma_T=1/(\sqrt2 g).}
\]

The exact event-timestamp information spectrum is

\[
\boxed{
\eta_I(\omega)
=\frac{16\Gamma^2g^4}
{(\Gamma^2+4\omega^2)[(4g^2-\omega^2)^2+\Gamma^2\omega^2]}.
}
\]

At optimal matching,

\[
\eta_I=32/[(x^2+2)(x^4+16)],
\quad x=\omega/g,
\]

with half-information `x=1.2265168396...`.

Quantum-Zeno tradeoffs in photon detectors are prior art; the exact factor is model specific.

Primary note: `WP11_DISSIPATIVE_MATCHING_THEOREM.md`.

---

## 10. Detuning extension

With optical/electronic detuning `Delta`,

\[
\boxed{
\langle T\rangle
=\Gamma/(4g^2)+2/\Gamma+\Delta^2/(\Gamma g^2).
}
\]

Mean-optimal readout rate:

\[
\boxed{\Gamma_{\rm opt}=2\sqrt{\Delta^2+2g^2}.}
\]

Minimum mean:

\[
\boxed{\langle T\rangle_{\min}=\sqrt{\Delta^2+2g^2}/g^2.}
\]

Primary note: `WP11_DISSIPATIVE_DETUNING_EXTENSION.md`.

---

## 11. Novelty boundaries added this round

- Helmer et al., PRA 79, 052115 (2009): photon-detector continuous-measurement backaction can produce a Zeno efficiency optimum at intermediate coupling. Generic Zeno matching is prior art.
- Salcin et al., IEEE TNS 61, 1243–1251 (2014): Fisher information + Shockley–Ramo semiconductor signals already used for depth-of-interaction estimation in CdTe/CdZnTe. Generic FI + Shockley–Ramo is prior art.
- Conventional photodiode transit-time `~0.44-0.45/tau` scaling is prior art.

The potentially distinct UPRP contribution is the **source-normalized optical-to-electrical information-transfer resource chain**, especially the proof that deterministic latency/amplitude attenuation need not reduce information and the identification of which hidden randomness/noise/coarse-graining resources actually do.

---

## 12. Exact next actions

1. Map the dissipative readout rate `Gamma` into a structured semiconductor reservoir/contact/phonon spectral density and identify when Zeno vs anti-Zeno behavior occurs.
2. Compose WP5 finite-band optical capture constraints with the spatial absorption-delay kernel; determine whether optical localization itself has a finite-band resource cost.
3. Extend the RC theorem to correlated amplifier voltage/current noise and finite sampling/ADC resources.
4. Analyze avalanche/multiplication detectors: deterministic gain is information-invariant, while stochastic multiplication/excess noise and bias free energy must enter explicitly.
5. Refresh `AGENTS.md` and `CURRENT_RESEARCH_STATE.md` whenever the next gate changes.
