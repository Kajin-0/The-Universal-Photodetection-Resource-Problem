# WP11 — Dissipative capture/readout matching theorem

**Date:** 2026-08-20

## Purpose

The closed three-node WP11 model shows coherent optical/internal coupling mismatch. Real photodetectors usually include irreversible localization/readout. This note studies the smallest such model and derives exact detection-time statistics and the corresponding event-timestamp information transfer.

The model also exposes a quantum-Zeno penalty when irreversible readout is made arbitrarily fast relative to coherent optical capture.

Quantum-Zeno backaction in photodetection/continuous measurement is well known; do not claim that general principle as novel. The project-specific value is the exact resource-matching/timing-information result in the UPRP detector chain.

---

# 1. Minimal dissipative detector

Use states

\[
|F\rangle,
\qquad
|X\rangle,
\qquad
|C\rangle.
\]

The optical excitation and captured excitation are coherently coupled:

\[
H=\hbar g
\left(|F\rangle\langle X|+|X\rangle\langle F|\right).
\]

Electrical detection/localization is an irreversible jump

\[
L=\sqrt{\Gamma}|C\rangle\langle X|.
\]

`|C>` is absorbing and represents a registered electrical event.

Start in

\[
|F\rangle.
\]

---

# 2. No-click dynamics

Before the first electrical jump, amplitudes obey

\[
\dot a=-igb,
\]

\[
\dot b=-iga-\frac{\Gamma}{2}b.
\]

The survival probability is

\[
S(t)=|a(t)|^2+|b(t)|^2.
\]

The first-detection-time density is

\[
\boxed{w(t)=\Gamma|b(t)|^2.}
\]

Since there is no other irreversible channel, eventual detection probability is unity for every `g>0`, `Gamma>0`.

---

# 3. Exact Laplace transform of the detection-time density

Solving the no-click density-matrix equations gives the exact Laplace transform

\[
\boxed{
\widetilde w(s)
=\int_0^\infty e^{-st}w(t)dt
=
\frac{4\Gamma g^2}
{(\Gamma+2s)(s^2+\Gamma s+4g^2)}.
}
\]

At `s=0`,

\[
\widetilde w(0)=1,
\]

confirming unit eventual detection probability.

**Status:** PROVED.

---

# 4. Exact mean detection time

Using

\[
\langle T\rangle=-\widetilde w'(0),
\]

one obtains

\[
\boxed{
\langle T\rangle
=
\frac{\Gamma}{4g^2}
+
\frac{2}{\Gamma}.
}
\]

The two terms have clear regimes:

### Slow localization/readout

\[
\Gamma\ll g
\quad\Rightarrow\quad
\langle T\rangle\sim2/\Gamma.
\]

### Quantum-Zeno/overmeasurement regime

\[
\Gamma\gg g
\quad\Rightarrow\quad
\langle T\rangle\sim\Gamma/(4g^2).
\]

The effective capture rate becomes

\[
\sim4g^2/\Gamma
\]

in the strong-measurement limit.

---

# 5. Exact optimal matching

Minimize the mean with respect to `Gamma`:

\[
\frac{d\langle T\rangle}{d\Gamma}
=\frac1{4g^2}-\frac2{\Gamma^2}=0.
\]

Therefore

\[
\boxed{
\Gamma_{\rm opt}=2\sqrt2\,g.
}
\]

At this point

\[
\boxed{
\langle T\rangle_{\min}
=\frac{\sqrt2}{g}.}
\]

Thus an ideal irreversible detector has a finite optimal readout/localization strength. Making the electrical localization rate arbitrarily large is counterproductive because it suppresses optical transfer through Zeno backaction.

**Status:** PROVED.

---

# 6. Exact timing variance

From the Laplace transform,

\[
\langle T^2\rangle
=\widetilde w''(0)
=
\frac{\Gamma^2}{8g^4}
+\frac1{2g^2}
+\frac8{\Gamma^2}.
\]

Therefore

\[
\boxed{
{\rm Var}(T)
=
\frac{\Gamma^2}{16g^4}
-\frac1{2g^2}
+\frac4{\Gamma^2}.
}
\]

Minimizing the variance gives the **same** optimum:

\[
\boxed{
\Gamma_{\rm opt}=2\sqrt2\,g.}
\]

At the optimum,

\[
\boxed{
{\rm Var}(T)=\frac1{2g^2},
\qquad
\sigma_T=\frac1{\sqrt2 g}.}
\]

The coefficient of variation is

\[
\boxed{
\sigma_T/\langle T\rangle=1/2.}
\]

Thus the same matching point simultaneously minimizes latency and rms timing jitter.

**Status:** PROVED.

---

# 7. Exact timestamp information spectrum

For independent photon events passed through this detector, the electrical timestamp is delayed by the first-detection time `T`.

The event-delay theorem of WP11 gives

\[
\eta_{\mathcal I}^{\rm timestamp}(\omega)
=|H_T(\omega)|^2
\]

in the ideal unit-efficiency/no-dark-count case, where

\[
H_T(\omega)=\widetilde w(i\omega).
\]

Therefore

\[
\boxed{
\eta_{\mathcal I}(\omega)
=
\frac{16\Gamma^2g^4}
{(\Gamma^2+4\omega^2)
[(4g^2-\omega^2)^2+\Gamma^2\omega^2]}.
}
\]

This is an exact non-Lorentzian information spectrum for the minimal coherent-capture + irreversible-readout detector.

**Status:** PROVED.

---

# 8. Information spectrum at the optimal matching point

Set

\[
\Gamma=2\sqrt2 g
\]

and define

\[
x=\omega/g.
\]

Then

\[
\boxed{
\eta_{\mathcal I}^{\rm opt}(x)
=
\frac{32}
{(x^2+2)(x^4+16)}.
}
\]

The half-information point solves

\[
\eta_{\mathcal I}^{\rm opt}=1/2
\]

at

\[
\boxed{x_{1/2}=1.2265168396\ldots.}
\]

Hence

\[
\boxed{
\omega_{1/2}^{\mathcal I}
=1.2265168396\ldots\,g,
}
\]

or

\[
\boxed{
f_{1/2}^{\mathcal I}
=0.1952062178\ldots\,g}
\]

when `g` is expressed in inverse seconds in the Hamiltonian `H=hbar g(...)`.

---

# 9. Low-frequency expansion and consistency

For any normalized delay distribution,

\[
|H_T(\omega)|^2
=1-\omega^2{\rm Var}(T)+O(\omega^4).
\]

Using the exact variance above reproduces the Taylor expansion of the rational spectrum in Sec. 7.

Thus the timing-statistics and spectral-FI derivations are mutually consistent.

---

# 10. Resource interpretation

The dissipative model identifies two genuinely different speed resources:

1. coherent optical capture coupling `g`;
2. irreversible electrical localization/readout rate `Gamma`.

Neither should be made arbitrarily large relative to the other while holding the other fixed.

The optimum

\[
\boxed{\Gamma/g=2\sqrt2}
\]

is a **capture/readout matching condition** for this particular minimal model.

Do not claim the numerical factor is universal across detector architectures. Reservoir spectral structure, detuning, multiple levels, phonons, and non-Markovian effects will change it.

---

# 11. Literature overlap

Quantum-Zeno modification of photodetection/continuous-measurement dynamics is established. Relevant prior work includes:

- Koshino and Shimizu reviews/work on quantum Zeno and anti-Zeno effects under realistic/indirect measurements;
- Helmer et al., Phys. Rev. A 79, 052115 (2009), showing detector backaction/continuous measurement can limit photon-detector efficiency through the quantum Zeno effect.

Therefore the generic statement `too-strong measurement can suppress detection` is not novel.

The UPRP novelty question is whether the exact timing/FI resource composition and its connection to semiconductor/thermodynamic bounds produce a distinct photodetection theorem.

---

# 12. Next steps

1. Add detuning between `|F>` and `|X>` and determine the optimal `Gamma(g,Delta)`.
2. Replace the flat Markov jump by a structured phonon/electrical reservoir and test anti-Zeno regimes.
3. Map `Gamma` to semiconductor localization/escape/current resources rather than leaving it phenomenological.
4. Compose this stochastic timing spectrum with the spatial-delay factor and dark-count penalty:

\[
\eta_I
=\frac{\eta_c}{1+d/(\eta_c\Phi_0)}
|H_{\rm geom}|^2|H_T|^2.
\]

5. Compare the optimum with the thermokinetic gateway theorem of WP3 to see whether activity/EPR budgets cap the achievable matching point.
