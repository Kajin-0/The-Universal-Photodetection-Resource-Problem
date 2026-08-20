# WP12 — Exact RC + amplifier-noise information bound

**Date:** 2026-08-20

## Purpose

`WP12_READOUT_FILTER_INFORMATION_INVARIANCE.md` proves that a deterministic RC pole alone does not reduce the Gaussian Fisher-information kernel. This note adds the minimal realistic asymmetry: current-like noise before the RC impedance and voltage noise after it.

The resulting information bandwidth can be solved exactly and is generally **not equal** to the conventional RC amplitude bandwidth.

---

# 1. Circuit model

Let the intrinsic detector produce current susceptibility

\[
\chi_I(\omega)
\]

for the optical parameter of interest.

Use the parallel-RC transimpedance

\[
\boxed{
Z(\omega)=\frac{R}{1+i\omega\tau},
\qquad
\tau=RC.
}
\]

Collect all noise that is naturally referred to the current-source/input side into

\[
S_u(\omega),
\]

including, as appropriate:

- detector shot/GR/Johnson-equivalent current noise;
- resistor Norton noise;
- amplifier input-current noise.

Let an amplifier/input voltage-noise source be added **after** the transimpedance with PSD

\[
S_e(\omega).
\]

Then

\[
V=Z[I_{\rm sig}+n_u]+e_n.
\]

---

# 2. Exact output information kernel

The voltage susceptibility is

\[
\chi_V=Z\chi_I.
\]

The output voltage-noise PSD is

\[
S_V=|Z|^2S_u+S_e.
\]

Therefore

\[
\boxed{
K_V(\omega)
=\frac{|Z|^2|\chi_I|^2}
{|Z|^2S_u+S_e}
=\frac{|\chi_I|^2}
{S_u+S_e/|Z|^2}.
}
\]

For the RC impedance,

\[
\frac1{|Z|^2}
=\frac{1+(\omega\tau)^2}{R^2}.
\]

Hence

\[
\boxed{
K_V(\omega)
=\frac{|\chi_I|^2}
{S_u(\omega)+
\frac{S_e(\omega)}{R^2}[1+(\omega\tau)^2]}.
}
\]

This is the exact linear-Gaussian information kernel for the stated circuit model.

---

# 3. White-noise closed form

Assume over the band of interest

\[
S_u(\omega)=S_u,
\qquad
S_e(\omega)=S_e,
\]

and take intrinsic `chi_I` locally flat so that only the circuit/noise contribution is being examined.

Define

\[
B\equiv S_e/R^2.
\]

Then

\[
K_V(0)=\frac{|\chi_I|^2}{S_u+B}.
\]

The normalized information response is

\[
\boxed{
\frac{K_V(\omega)}{K_V(0)}
=
\frac{1}
{1+\beta(\omega\tau)^2},
}
\]

where

\[
\boxed{
\beta=\frac{B}{S_u+B}
=\frac{S_e/R^2}{S_u+S_e/R^2}.
}
\]

Thus the information kernel has a Lorentzian rolloff only to the extent that **post-impedance voltage noise** is present.

---

# 4. Half-information frequency

Set

\[
K_V(\omega_{1/2})=K_V(0)/2.
\]

Then

\[
\beta(\omega_{1/2}\tau)^2=1
\]

and therefore

\[
\boxed{
\omega_{1/2}^{\mathcal I}
=
\frac{1}{RC}
\sqrt{1+\frac{S_uR^2}{S_e}}.
}
\]

Equivalently in ordinary frequency,

\[
\boxed{
f_{1/2}^{\mathcal I}
=
\frac{1}{2\pi RC}
\sqrt{1+\frac{S_uR^2}{S_e}}.}
\]

Compare the conventional amplitude `-3 dB` frequency

\[
f_{RC}=1/(2\pi RC).
\]

Therefore

\[
\boxed{
\frac{f_{1/2}^{\mathcal I}}{f_{RC}}
=
\sqrt{1+\frac{S_uR^2}{S_e}}.
}
\]

The information bandwidth can be much larger than the amplitude bandwidth when downstream voltage noise is small.

---

# 5. Important limits

## Downstream voltage-noise dominated

If

\[
S_e/R^2\gg S_u,
\]

then

\[
\beta\to1
\]

and

\[
\boxed{f_{1/2}^{\mathcal I}\to f_{RC}.}
\]

In this regime the usual RC bandwidth acquires a direct information interpretation.

## Upstream-noise dominated

If

\[
S_e/R^2\ll S_u,
\]

then

\[
\beta\ll1
\]

and

\[
f_{1/2}^{\mathcal I}\gg f_{RC}.
\]

In the formal limit `S_e -> 0`,

\[
\boxed{f_{1/2}^{\mathcal I}\to\infty}
\]

within this idealized model, reproducing the deterministic-filter invariance theorem.

---

# 6. Johnson-Nyquist noise placement

For a resistor in the parallel-RC node, its thermal noise can be represented in Norton form as a current source before the same impedance `Z` that filters the detector current. It therefore contributes to `S_u`, not to the post-filter `S_e` term.

Consequently the resistor's own Johnson noise does **not by itself** force the FI half-power point to coincide with the RC amplitude pole.

The exact finite-temperature result in a specific circuit must use the full fluctuation-dissipation spectrum and circuit topology, but the structural conclusion is already clear:

\[
\boxed{
\text{noise location relative to attenuation matters.}
}
\]

---

# 7. Relation to detector engineering

Ordinary photodiode `f_RC` remains a valid and important voltage-response specification. The present theorem does not dispute that.

It states that for optimal estimation from a known noisy waveform,

\[
\boxed{
\text{recoverable information bandwidth}
\text{ depends on both }Z(\omega)\text{ and the noise partition.}
}
\]

A universal photodetection theorem cannot infer FI bandwidth from `R` and `C` alone.

---

# 8. New resource pair

The external electrical-readout layer requires at minimum

\[
\boxed{
\text{transfer/impedance function}
+
\text{input-referred vs downstream noise resources}.
}
\]

If digitization is included, sampling rate, quantization, clock jitter, and ADC noise become additional explicit resources.

---

# 9. Next step

Extend this exact two-noise-source model to:

1. quantum fluctuation-dissipation spectra;
2. amplifier voltage-current noise correlation;
3. finite input impedance and detector capacitance;
4. finite sampling/ADC precision;
5. an optimized impedance/noise matching theorem analogous to the optical/internal matching result of WP11.
