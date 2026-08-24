# WP01 — Linear Gaussian detector: exact Fisher/NEP bridge

**Date:** 2026-08-23

**Status:** analytical derivation complete at the stated convention level; prior-art novelty not claimed.

## Question

How does the temporal Fisher information used in the existing resource program reduce to ordinary photodetector quantities for the standard experiment of a weak sinusoidally modulated optical input measured with a linear detector in stationary Gaussian noise?

The objective is not to rename NEP. The objective is to obtain a convention-controlled identity that allows the abstract Fisher resource laws to be tested using measured detector transfer functions and noise spectra.

## Measurement model and convention lock

Let the incident optical-power perturbation be

`delta P(t) = x cos(2 pi f0 t) + y sin(2 pi f0 t)`

on an observation interval of duration `T`, where `x` and `y` are **peak** cosine/sine amplitudes in watts.

Let a linear detector have complex small-signal responsivity `R(f)` in A/W (or V/W), and let its additive zero-mean stationary Gaussian output noise have **one-sided** PSD `S_n(f)` in A^2/Hz (or V^2/Hz).

For a deterministic output waveform `s(t;theta)` in stationary Gaussian noise, define the standard one-sided noise-weighted inner product

`(a|b) = 4 Re integral_0^infinity [a_tilde(f)^* b_tilde(f) / S_n(f)] df`.

The Gaussian Fisher matrix is

`F_ij = (partial_i s | partial_j s)`.

For a long observation of a narrowband sinusoid at `f0`, the two quadratures become orthogonal and the response magnitude may be treated as constant across the Fourier width `~1/T`.

## Result 1 — one-quadrature and two-quadrature Fisher rates

The detector output derivatives are, up to the detector transfer phase,

`partial_x s = R(f0) cos(2 pi f0 t)`

and

`partial_y s = R(f0) sin(2 pi f0 t)`.

Using Parseval and the one-sided PSD convention,

`F_xx = T |R(f0)|^2 / S_n(f0)`

`F_yy = T |R(f0)|^2 / S_n(f0)`

`F_xy -> 0`

as `T f0 >> 1` (or exactly after an integer number of periods in the ideal narrowband/white-local-PSD case).

Therefore

`F_xx/T = F_yy/T = |R(f0)|^2/S_n(f0)`

and

**`Tr F / T = 2 |R(f0)|^2 / S_n(f0)`.**

Units check:

- `R^2/S_n` has units `Hz/W^2 = 1/(s W^2)`;
- multiplying by `T` gives Fisher units `1/W^2`, as required for amplitude parameters in watts.

## Result 2 — exact reduction to frequency-resolved NEP

Under the same linear/Gaussian/small-signal assumptions, conventional frequency-resolved noise-equivalent power is

`NEP(f) = sqrt(S_n(f))/|R(f)|`

with units W/sqrt(Hz).

Hence

**`F_xx/T = 1/NEP(f0)^2`**

and

**`Tr F/T = 2/NEP(f0)^2`.**

Equivalently, if ordinary detectivity is defined as `D(f)=1/NEP(f)`,

**`Tr F/T = 2 D(f0)^2`.**

This is not proposed as a new definition of NEP or detectivity. It is the detector-language bridge needed to connect the existing Fisher-resource theorems to conventional measurements.

## RMS convention

If the modulation parameters are instead RMS quadrature amplitudes `x_rms,y_rms`, with

`delta P(t)=sqrt(2) x_rms cos(...) + sqrt(2) y_rms sin(...)`,

each parameter derivative is larger by `sqrt(2)`. Therefore

`F_xrms,xrms/T = F_yrms,yrms/T = 2/NEP^2`

and

`Tr F_rms/T = 4/NEP^2`.

Any manuscript statement must specify peak or RMS amplitude. The preferred Paper-4 convention is peak quadrature amplitudes because it matches the cosine/sine local-coordinate convention used in the flagship theory.

## Result 3 — arbitrary waveform/basis version

For a linear input perturbation

`delta P(t;theta)=sum_i theta_i q_i(t)`

with Fourier-domain detector response `R(f)`, the Gaussian Fisher matrix is

**`F_ij = 4 Re integral_0^infinity [q_i_tilde(f)^* q_j_tilde(f) |R(f)|^2 / S_n(f)] df`.**

Because `NEP(f)^2=S_n(f)/|R(f)|^2`, this becomes

**`F_ij = 4 Re integral_0^infinity [q_i_tilde(f)^* q_j_tilde(f) / NEP(f)^2] df`.**

Thus `1/NEP(f)^2` is literally the frequency weighting of the Fisher metric for small input-waveform perturbations in the linear stationary Gaussian regime.

This is a highly practical bridge: measured `R(f)` and measured output-noise PSD `S_n(f)` are sufficient to reconstruct the complete local Fisher matrix for any specified weak waveform basis, provided the assumptions hold.

## Result 4 — response bandwidth need not equal information bandwidth

For a narrowband sinusoidal temporal task, define the normalized Fisher-transfer function

`Gamma_F(f) = [|R(f)|^2/S_n(f)] / [|R(f_ref)|^2/S_n(f_ref)]`

for a reference frequency in the low-frequency plateau.

Equivalently,

`Gamma_F(f) = [NEP(f_ref)/NEP(f)]^2`.

A task-specific Fisher 3-dB frequency may be defined, when monotonic and well posed, by

`Gamma_F(f_F,3dB)=1/2`,

or

`NEP(f_F,3dB)=sqrt(2) NEP(f_ref)`.

This generally differs from the conventional responsivity 3-dB frequency defined by

`|R(f_R,3dB)|^2=|R(f_ref)|^2/2`.

They coincide only when the relevant output-noise PSD is effectively flat over the transition.

### Standard-physics example: filtered signal and filtered input noise

Let

`R(f)=R0 H(f)`

and suppose the dominant noise enters before the same linear filter, so

`S_n(f)=|H(f)|^2 S_in`.

Then

`|R(f)|^2/S_n(f)=R0^2/S_in`

wherever `H(f) != 0`.

The responsivity can roll off strongly while the ideal matched-filter Fisher information for estimating a known narrowband input amplitude remains unchanged, because both signal and dominant noise are attenuated by the same invertible linear transformation.

Once additive readout noise `S_ro(f)` is included,

`S_n(f)=|H(f)|^2 S_in + S_ro(f)`

and

`F_xx/T = R0^2 |H(f)|^2 / [|H(f)|^2 S_in + S_ro(f)]`.

Now the information eventually rolls off when the post-filter/readout noise dominates. This gives a direct, conventional explanation for why response bandwidth alone is not a complete temporal-information metric.

## Practical falsification test for WP01

For a detector believed to satisfy the linear stationary Gaussian model:

1. measure small-signal complex responsivity `R(f0)` at the operating point;
2. measure one-sided intrinsic output noise PSD `S_n(f0)` with instrument noise removed or separately modelled;
3. inject many weak known cosine/sine modulation realizations near the same operating point;
4. estimate the empirical likelihood or sample Fisher matrix for `x,y` from the raw output record;
5. compare against

`F_xx/T = F_yy/T = |R|^2/S_n`, `F_xy=0`.

A statistically significant calibrated disagreement after accounting for finite observation time and the actual PSD would falsify the assumed linear stationary Gaussian measurement model or the data-reduction convention. It would not by itself falsify the upstream quantum resource theorem; rather it would invalidate this detector-language reduction for that operating point.

## Why this matters for Paper 4

The identity makes the upstream theory legible in ordinary detector language:

`temporal Fisher-information rate <-> inverse-square NEP`

for the most standard weak-signal detector model.

It also provides the entry point for the practical paper's stronger questions:

- when does conventional NEP cease to represent the actual information in the record?
- can a likelihood-defined input-equivalent information metric extend the comparison to nonlinear, non-Gaussian, memoryful, and timestamp detectors?
- can survival/synthesis inequalities be rewritten directly as bounds on measured `NEP(f)`, sideband curvature, or timestamp Fisher spectra?

## Prior-art status from initial targeted search

No novelty claim is made for Fisher information in optical sensing, NEP, or the idea that detector noise limits Fisher precision.

Relevant current context found in the initial search:

- Pecunia et al., *Nature Photonics* (2025), “Guidelines for accurate evaluation of photodetectors based on emerging semiconductor technologies,” emphasizes measured frequency-dependent responsivity, noise PSD, NEP at specified modulation frequency/bandwidth, and warns against white-noise/`sqrt(B)` normalizations under colored noise. DOI/article page: `https://www.nature.com/articles/s41566-025-01759-1`.
- A 2026 *Optics Express* paper on Fisher-information design of diffuse optical monitoring explicitly combines Gaussian detector noise parameterized by photodiode NEP with Fisher-information calculations; this confirms that NEP/Fisher connections are not generically novel.
- Recent ACS Nano work on multispectral sensing states that Fisher-limited precision can be fundamentally limited by detector NEP, again showing neighboring prior art.

What may still be publishable is the **specific frequency-resolved temporal-information bridge, its convention-controlled waveform form, its integration with timestamp detectors and the survival/synthesis falsification program, and any nontrivial detector-ranking/crossover predictions**. A dedicated prior-art gate is mandatory before novelty language.

## Next

WP02: derive the ideal inhomogeneous-Poisson two-quadrature Fisher rate and exact attenuation under independent timing jitter, including units and finite-time assumptions. Then compare the resulting timestamp-information spectrum to the analog `1/NEP^2` weighting established here.
