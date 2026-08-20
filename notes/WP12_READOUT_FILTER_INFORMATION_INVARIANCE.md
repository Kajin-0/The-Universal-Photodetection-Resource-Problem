# WP12 — Readout-filter invariance and why RC bandwidth is not automatically information bandwidth

**Date:** 2026-08-20

## Purpose

Conventional photodetector specifications combine intrinsic transit-time and RC-limited `-3 dB` bandwidths. UPRP uses Fisher information / input-referred noise instead of amplitude response, so a deterministic electrical pole must be re-examined.

Main result:

> **A known deterministic invertible linear filter does not reduce Fisher information merely because its amplitude rolls off. An RC pole becomes an information limit only through noninvertibility, downstream/additive noise, finite sampling/quantization, finite observation windows, model uncertainty, or other coarse graining.**

This is the circuit-level analogue of the deterministic transit-delay correction in WP11.

---

# 1. Exact LTI invariance of the information kernel

Let an intrinsic electrical record `X` have linear susceptibility

\[
\chi_X(\omega)
\]

and stationary noise PSD

\[
S_X(\omega).
\]

Pass it through a known deterministic LTI filter

\[
Y(\omega)=H(\omega)X(\omega).
\]

Then

\[
\chi_Y=H\chi_X,
\qquad
S_Y=|H|^2S_X.
\]

Therefore wherever `H(omega) != 0`,

\[
\boxed{
\frac{|\chi_Y(\omega)|^2}{S_Y(\omega)}
=
\frac{|\chi_X(\omega)|^2}{S_X(\omega)}.
}
\]

Thus the Gaussian linear Fisher-information kernel is exactly invariant.

This is also a direct consequence of invariance of Fisher information under invertible deterministic transformations of the observed record.

**Status:** PROVED.

---

# 2. RC pole example

Take a simple low-pass transimpedance

\[
H(\omega)=\frac{R}{1+i\omega RC}.
\]

Its voltage amplitude is down by 3 dB at

\[
\omega=1/RC.
\]

Nevertheless, if all detector signal and detector-originated noise are filtered by the same `H`,

\[
\boxed{K_Y(\omega)=K_X(\omega).}
\]

So

\[
\boxed{
\text{RC amplitude bandwidth}
\not\equiv
\text{information bandwidth}.
}
\]

Do not use `1/(2pi RC)` as a fundamental UPRP limit without specifying the output record and the noise that enters after or inside the filter.

---

# 3. Downstream additive noise creates a genuine information rolloff

Now let the measured output contain additive noise after the intrinsic filter:

\[
Y=HX+N_A,
\]

with PSD

\[
S_A(\omega).
\]

Then

\[
S_Y=|H|^2S_X+S_A
\]

and

\[
\boxed{
K_Y
=\frac{|H|^2|\chi_X|^2}
{|H|^2S_X+S_A}
=\frac{|\chi_X|^2}
{S_X+S_A/|H|^2}.
}
\]

As `|H|` becomes small, downstream noise is referred back to the detector input with the amplified penalty

\[
S_{A,\rm in}=S_A/|H|^2.
\]

This produces a true information-bandwidth ceiling.

Therefore the meaningful resource is not the pole alone but the pair

\[
\boxed{
\text{transfer function}
+
\text{location/spectrum of added noise}.
}
\]

---

# 4. Passive resistor noise does not automatically restore the usual RC cutoff

A resistor at finite temperature brings Johnson-Nyquist noise through fluctuation-dissipation. However, in a simple parallel `R-C` current-readout node, the resistor's equivalent current noise is injected before the same impedance that filters the signal.

Schematically,

\[
V(\omega)=Z(\omega)[I_{\rm sig}(\omega)+I_R(\omega)],
\]

so both signal and resistor-current noise acquire the same `Z`.

The signal-to-resistor-noise Fisher ratio can therefore remain independent of the RC pole.

This is consistent with the fluctuation-dissipation form `S_V proportional Re Z`: for a parallel RC,

\[
{\rm Re}\,Z=|Z|^2/R.
\]

Hence the pole attenuates the resistor voltage noise together with the signal.

Conclusion:

\[
\boxed{
\text{finite-temperature passivity alone does not imply that the amplitude }-3\,\mathrm{dB}\text{ point is the FI }-3\,\mathrm{dB}\text{ point}.
}
\]

The complete circuit topology and measurement-noise placement matter.

---

# 5. Exact spectral zeros are different

If

\[
H(\omega_0)=0,
\]

then the corresponding component is erased and cannot be recovered from that output channel.

Thus deterministic filtering can destroy information through a true null even without additive noise.

For rational RC low-pass filters, there is no finite-frequency exact zero, so the ideal mathematical record remains invertible frequency by frequency.

---

# 6. Finite observation time and unstable inverse

Although a mathematical inverse may exist, practical recovery of heavily attenuated frequencies can fail because of:

- finite observation duration;
- finite ADC range/resolution;
- digitizer/applifier input noise;
- clock jitter;
- model uncertainty in `H`;
- saturation;
- finite numerical precision;
- causal real-time constraints.

These are additional resources/constraints and must be stated explicitly if they are used to turn amplitude attenuation into information loss.

UPRP should not hide them inside a nominal analog bandwidth number.

---

# 7. Output-record hierarchy

The project now needs to distinguish at least:

1. **intrinsic detector state/current record**;
2. **complete analog electrode waveform**;
3. **filtered amplifier output**;
4. **digitized samples**;
5. **thresholded event timestamps/counts**.

Each is a coarse graining of the previous level unless extra side information is retained.

A universal theorem must state which record is accessible.

---

# 8. Relation to conventional detector engineering

Conventional high-speed photodiode design correctly combines transit-time and RC amplitude limitations to predict measured `S21`, impulse rise time, and usable analog voltage response. These engineering metrics remain essential.

UPRP makes a different statement:

\[
\boxed{
\text{measured amplitude bandwidth}
\neq
\text{fundamental information bandwidth}
}
\]

unless the associated noise/coarse-graining model is specified.

This distinction should be emphasized in any eventual paper because otherwise familiar `f_RC` or `f_tr` formulas can be incorrectly interpreted as universal information bounds.

---

# 9. New no-go statement

A finite deterministic analog bandwidth alone is insufficient to bound source-normalized detector FI:

\[
\boxed{
\{H(\omega)\text{ with strong rolloff but }H\ne0\}
\not\Rightarrow
\eta_{\mathcal I}(\omega)\to0.
}
\]

A completion requires at least one of:

- additive/downstream noise;
- random internal timing;
- exact spectral nulls;
- finite sampling/quantization;
- finite observation resources;
- output coarse graining.

---

# 10. Immediate next step

Build the simplest explicit finite-temperature detector + amplifier circuit and derive the exact electrical FI kernel with:

1. detector shot/Johnson/GR noise upstream;
2. passive impedance;
3. resistor fluctuation-dissipation noise;
4. amplifier voltage/current noise downstream;
5. finite sampling bandwidth.

The objective is to identify which circuit resources actually create an information-bandwidth ceiling instead of merely an amplitude rolloff.
