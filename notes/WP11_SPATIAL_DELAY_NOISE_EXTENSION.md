# WP11 — Dark-count and stochastic-delay extension

**Date:** 2026-08-20

## Purpose

Extend `WP11_SPATIAL_DELAY_INFORMATION_THEOREM.md` to include dark counts and independent stochastic transport/localization delays.

---

# 1. Fractional sinusoidal modulation

Let the incident coherent/Poisson photon flux be

\[
\Phi(t)=\Phi_0[1+\epsilon\cos(\omega t)].
\]

The incident Poisson Fisher-information rate for `epsilon`, averaged over many periods and evaluated at `epsilon=0`, is

\[
\dot F_{\rm in}=\Phi_0/2.
\]

Let signal photons be captured with probability `eta_c`, independently delayed with characteristic function

\[
H(\omega)=\mathbb E[e^{-i\omega D}],
\]

and add a stationary unmodulated dark-count rate `d`.

The mean output rate is

\[
\lambda_0=\eta_c\Phi_0+d,
\]

while the modulation amplitude is

\[
\eta_c\Phi_0|H(\omega)|.
\]

Therefore

\[
\dot F_{\rm out}
=\frac{\eta_c^2\Phi_0^2|H|^2}
{2(\eta_c\Phi_0+d)}.
\]

The source-normalized information-transfer efficiency is

\[
\boxed{
\eta_{\mathcal I}(\omega)
=\frac{\eta_c^2\Phi_0}{\eta_c\Phi_0+d}|H(\omega)|^2
=\frac{\eta_c}{1+d/(\eta_c\Phi_0)}|H(\omega)|^2.
}
\]

**Status:** PROVED for the stated Poisson event-record model.

---

# 2. Independent delay mechanisms multiply

Suppose

\[
D=D_1+D_2+\cdots+D_m
\]

with independent components. Then characteristic functions multiply:

\[
H(\omega)=\prod_jH_j(\omega).
\]

Hence

\[
\boxed{
|H(\omega)|^2
=\prod_j|H_j(\omega)|^2.
}
\]

Therefore independent timing penalties compose multiplicatively in event-timestamp FI.

For example,

\[
D=D_{\rm geom}+D_{\rm sc}+D_{\rm loc}
\]

gives

\[
\boxed{
\eta_{\mathcal I}
=\frac{\eta_c}{1+d/(\eta_c\Phi_0)}
|H_{\rm geom}|^2
|H_{\rm sc}|^2
|H_{\rm loc}|^2.
}
\]

---

# 3. Exponential localization/scattering delay

If an independent delay is exponential,

\[
D_{\rm exp}\sim{\rm Exp}(\gamma),
\]

then

\[
H_{\rm exp}(\omega)
=\frac{\gamma}{\gamma+i\omega}
\]

and

\[
\boxed{
|H_{\rm exp}(\omega)|^2
=\frac{\gamma^2}{\gamma^2+\omega^2}.
}
\]

This recovers the Lorentzian first-passage factor used in WP3 and shows how it composes with spatial absorption-depth dispersion.

---

# 4. Gamma/Erlang multi-stage delay

For `n` independent exponential stages of equal rate `gamma`,

\[
D\sim{\rm Erlang}(n,\gamma),
\]

\[
H(\omega)=\left(\frac{\gamma}{\gamma+i\omega}\right)^n,
\]

so

\[
\boxed{
|H(\omega)|^2
=\left(\frac{\gamma^2}{\gamma^2+\omega^2}\right)^n.
}
\]

Thus sequential unresolved stochastic stages steepen the information rolloff.

---

# 5. Background photon flux

If an unmodulated optical background `Phi_b` enters the same capture channel, the stationary output baseline becomes

\[
\lambda_0=\eta_c(\Phi_0+\Phi_b)+d.
\]

Only the signal flux `Phi_0` is modulated, so

\[
\boxed{
\eta_{\mathcal I}(\omega)
=\frac{\eta_c^2\Phi_0}
{\eta_c(\Phi_0+\Phi_b)+d}
|H(\omega)|^2.
}
\]

This is the event-record analogue of background-limited detection.

---

# 6. Interpretation

For the ideal timestamp/count record, distinct physical penalties separate cleanly:

\[
\boxed{
\text{capture thinning}
\times
\text{dark/background dilution}
\times
\text{geometry jitter}
\times
\text{stochastic internal jitter}.
}
\]

This is substantially more informative than assigning one scalar `response time` to the detector.

---

# 7. Limitation

The multiplication law applies to **independent random event delays** and an event-timestamp/count output. It does not apply unchanged when:

- delays are correlated with signal amplitude or each other;
- carrier trajectories modify capture probability;
- the complete analog current waveform is retained;
- events overlap nonlinearly/saturate;
- active gain introduces branching and excess noise.

Those require separate channel models.
