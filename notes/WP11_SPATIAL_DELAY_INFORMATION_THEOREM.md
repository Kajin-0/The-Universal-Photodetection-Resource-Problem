# WP11 — Spatial transport-delay information theorem

**Date:** 2026-08-20

## Purpose

A conventional photodiode transit time `L/v` is often treated as a detector bandwidth. Under the UPRP information metric this requires care:

- a **deterministic known delay** changes only phase and does not reduce Fisher information;
- unresolved **event-to-event delay dispersion** does reduce timestamp/count-record information;
- deterministic noiseless analog filtering can preserve `|chi|^2/S` because signal and upstream noise are filtered together;
- downstream additive noise, sampling, finite windows, or transfer-function zeros create genuine information loss.

This note derives the exact point-process theorem and shows that the familiar `~0.44 v/L` transit-time coefficient arises from **uniform unresolved transit-delay dispersion**.

---

# 1. Independent displacement theorem for Poisson photon events

Let incident photon events form an inhomogeneous Poisson process with intensity

\[
\Phi(t;\theta).
\]

Assume each captured event is independently:

1. retained with probability `eta_cap`;
2. assigned a transport delay `D` drawn independently from density `h(D)`;
3. recorded electrically only by its delayed event timestamp.

The displacement theorem for Poisson processes implies that the electrical event process is again Poisson with intensity

\[
\boxed{
\lambda_{\rm out}(t;\theta)
=\eta_{\rm cap}\int h(D)\Phi(t-D;\theta)dD.
}
\]

For weak sinusoidal modulation at angular frequency `omega`, the modulation amplitude is multiplied by the delay characteristic function

\[
\boxed{
H_D(\omega)=\mathbb E[e^{-i\omega D}].
}
\]

The Poisson output noise remains white at the output mean rate; it is not multiplied by `|H_D|^2` as it would be for a deterministic analog convolution of an already-realized waveform.

Therefore, in the absence of dark counts or other noise,

\[
\boxed{
\eta_{\mathcal I}^{\rm timestamp}(\omega)
=\eta_{\rm cap}|H_D(\omega)|^2.
}
\]

**Status:** PROVED for independent thinning + independent event-delay displacement of a Poisson/coherent source and a timestamp/count output record.

This is the geometric/event-delay version of the random-delay theorem used earlier in WP3.

---

# 2. Deterministic delay is not an information-bandwidth limit

If

\[
D=\tau
\]

is deterministic,

\[
H_D(\omega)=e^{-i\omega\tau}
\]

and therefore

\[
\boxed{|H_D(\omega)|^2=1.}
\]

Thus

\[
\boxed{
\eta_{\mathcal I}^{\rm timestamp}(\omega)=\eta_{\rm cap}
}
\]

at every frequency in the ideal point-process model.

A known fixed propagation/transit delay is a **latency**, not a loss of spectral information.

This distinction is mandatory in UPRP. Do not equate a deterministic carrier flight time directly with information bandwidth.

---

# 3. General small-frequency expansion: delay variance is the first information penalty

Write

\[
D=\bar D+\delta D,
\qquad
\mathbb E[\delta D]=0.
\]

Then

\[
H_D(\omega)
=e^{-i\omega\bar D}
\left[1-\frac{\omega^2}{2}{\rm Var}(D)+O(\omega^3)\right].
\]

Therefore

\[
\boxed{
|H_D(\omega)|^2
=1-\omega^2{\rm Var}(D)+O(\omega^4).
}
\]

The mean delay affects only phase; the leading information-bandwidth penalty is the **delay variance/jitter**.

Variance alone does not give a global all-frequency bound because characteristic functions can have revivals; distributional structure matters away from low frequency.

---

# 4. Joint optical/electrical geometry theorem

Let an absorbed photon be created at position `r` with normalized conditional capture density

\[
p_{\rm abs}(\mathbf r).
\]

Suppose the electrical timestamp delay is a deterministic function of the capture point,

\[
D=D(\mathbf r),
\]

but the capture position is **not** included in the electrical record.

Then the unresolved delay characteristic function is

\[
\boxed{
H_{\rm geom}(\omega)
=\int d^3r\,
p_{\rm abs}(\mathbf r)
e^{-i\omega D(\mathbf r)}.
}
\]

Hence

\[
\boxed{
\eta_{\mathcal I}^{\rm timestamp}(\omega)
=\eta_{\rm cap}
\left|
\int d^3r\,p_{\rm abs}(\mathbf r)e^{-i\omega D(\mathbf r)}
\right|^2.
}
\]

This is the first explicit UPRP formula that composes:

1. the **spatial optical capture distribution**;
2. semiconductor transport;
3. electrical event timing;
4. source-normalized information transfer.

The optical and electrical geometries enter through the distribution of `D(r)`, not through detector thickness alone.

**Status:** PROVED for the stated Poisson/timestamp model.

---

# 5. Side-information recovery theorem

If the capture coordinate `r` (or any variable sufficient to determine `D(r)`) is recorded together with the electrical timestamp, the deterministic delay can be subtracted event by event:

\[
t_{\rm corrected}=t_{\rm out}-D(\mathbf r).
\]

Therefore the geometry-induced information loss above is a **coarse-graining loss** caused by unresolved latent transport position.

In the ideal model,

\[
\boxed{
\eta_{\mathcal I}^{\rm timestamp+position}(\omega)
=\eta_{\rm cap}.
}
\]

This is another mandatory output-record distinction for UPRP.

---

# 6. Uniform absorption-depth model

Consider a planar layer `0<=x<=L`, collection at `x=L`, constant deterministic carrier velocity `v`, and unresolved absorption depth uniformly distributed over the layer:

\[
p_{\rm abs}(x)=1/L.
\]

The delay is

\[
D(x)=\frac{L-x}{v}.
\]

Thus

\[
D\sim{\rm Uniform}(0,\tau),
\qquad
\tau=L/v.
\]

The characteristic function is

\[
H_D(\omega)
=e^{-i\omega\tau/2}
\operatorname{sinc}\!\left(\frac{\omega\tau}{2}\right),
\]

where `sinc z = sin(z)/z`.

Therefore

\[
\boxed{
\eta_{\mathcal I}(\omega)
=\eta_{\rm cap}
\operatorname{sinc}^2\!\left(\frac{\omega\tau}{2}\right).
}
\]

The half-information point solves

\[
\operatorname{sinc}^2 z=1/2
\]

at

\[
z=1.391557378\ldots
\]

so

\[
\boxed{
f_{1/2}
=\frac{z}{\pi\tau}
=\frac{0.4429464707\ldots}{\tau}
=0.4429464707\ldots\frac{v}{L}.}
\]

This is essentially the familiar conventional photodiode transit-time coefficient near `0.44-0.45/tau`, now derived as an **information loss from unresolved transit-delay dispersion**.

Conventional UTC/MUTC photodiode literature uses transit-time bandwidth relations proportional to `1/tau_tr`; this scaling itself is not novel.

**Status:** PROVED exact coefficient for the uniform-depth timestamp model.

---

# 7. Beer-Lambert absorption-depth model

For one-sided illumination with absorption coefficient `alpha`, let

\[
p_{\rm abs}(x)
=\frac{\alpha e^{-\alpha x}}
{1-e^{-\alpha L}},
\qquad 0\le x\le L.
\]

Again let

\[
D(x)=(L-x)/v.
\]

Define dimensionless optical depth and modulation frequency

\[
A=\alpha L,
\qquad
z=\omega L/v.
\]

Direct integration gives

\[
\boxed{
H_D(z)
=e^{-iz}
\frac{A}{A-iz}
\frac{1-e^{-A+iz}}{1-e^{-A}}.
}
\]

Hence

\[
\boxed{
|H_D(z)|^2
=
\frac{A^2}{A^2+z^2}
\frac{1+e^{-2A}-2e^{-A}\cos z}
{(1-e^{-A})^2}.
}
\]

Therefore

\[
\boxed{
\eta_{\mathcal I}(z)
=\eta_{\rm cap}|H_D(z)|^2.
}
\]

Limits:

### Weak absorption `A -> 0`

Conditional on capture, absorption depth approaches uniform over the layer, and

\[
|H_D|^2
\to
\operatorname{sinc}^2(z/2).
\]

### Strong absorption `A >> 1`

Absorption is tightly localized near the illuminated surface. The mean carrier flight time may remain approximately `L/v`, but its **spread** becomes small. At fixed `z`,

\[
|H_D|^2\to1.
\]

Thus a long deterministic flight time can coexist with high timestamp information bandwidth if the absorption position is sharply localized.

This proves that detector thickness or mean transit time alone is not an information-bandwidth resource.

---

# 8. Relation to Shockley-Ramo weighting geometry

For a collection-timestamp record, `D(r)` is determined by carrier trajectories to the event-definition surface.

For a thresholded induced-charge record, `D(r)` instead depends on when the Shockley-Ramo weighting potential has changed by the threshold amount. Thus the same theorem applies with

\[
D(\mathbf r)
=\text{first time the trajectory reaches the specified weighting-potential change}.
\]

This is where the electrical weighting geometry from `WP11_FINITE_TRANSPORT_CHAIN_AND_GEOMETRY_NO_GO.md` enters directly.

The relevant geometric resource is the **distribution of capture-to-readout delays**, not merely a scalar detector thickness.

---

# 9. Full analog current record is different

If each event produces a deterministic current waveform `p(t)` and the complete analog superposition is observed with only upstream Poisson shot noise, then deterministic convolution gives

\[
\chi_Y=P(\omega)\chi_X,
\qquad
S_Y=|P(\omega)|^2S_X,
\]

and therefore

\[
\boxed{
|\chi_Y|^2/S_Y
=|\chi_X|^2/S_X
}
\]

where `P(omega) != 0`.

Thus the timestamp theorem must **not** be silently applied to a complete noiseless analog waveform record.

Information loss then requires downstream noise, unresolved internal randomness, finite sampling, quantization, finite observation windows, exact spectral zeros, or other coarse graining.

---

# 10. Conventional transit-time bandwidth reinterpreted

The standard architecture-level statement

\[
f_{\rm tr}\sim0.44/\tau_{\rm tr}
\]

can now be separated into two concepts:

1. **kinematic latency:** carriers require time to propagate;
2. **information rolloff:** unresolved event-to-event variation of that propagation delay attenuates modulation by `|H_D|^2`.

The first alone does not reduce stationary spectral FI. The second does.

This distinction is likely important for any publication-level UPRP theorem.

---

# 11. New resource statement

For event-timestamp photodetection, the semiconductor transport layer requires

\[
\boxed{
\text{capture probability}
+
\text{distribution of capture positions}
+
\text{transport/weighting geometry}
+
\text{carrier dynamical law}
\Rightarrow
\text{delay characteristic function}
\Rightarrow
\eta_{\mathcal I}(\omega).
}
\]

A single scalar transit time is generally insufficient.

---

# 12. Next steps

1. Add dark counts and derive the exact degradation factor.
2. Add stochastic velocity/scattering on top of spatial absorption dispersion.
3. Use WP5 electromagnetic constraints to bound how sharply `p_abs(r)` can be localized over a finite optical bandwidth.
4. Determine whether a finite-band optical absorption sum rule plus `v_max` and weighting geometry yields a nontrivial joint information-bandwidth theorem.
5. Compare timestamp, threshold-crossing, and full analog current records explicitly so no output coarse graining is hidden.
