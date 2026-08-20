# WP14 — Intrinsic versus measured information bandwidth

**Date:** 2026-08-20

## Purpose

WP11–WP13 repeatedly show that conventional detector speed metrics depend strongly on which output record is retained:

- deterministic transit delay can be phase-only;
- deterministic RC rolloff can be invertible;
- unresolved transit-position jitter loses timestamp information;
- random avalanche gain can be FI-neutral for resolved marked events but lossy after analog integration;
- downstream amplifier noise converts otherwise invertible attenuation into real information loss.

A resource-complete theory therefore needs an explicit **record hierarchy**.

---

# 1. Quantum detector-output hierarchy

Let the optical input family be

\[
\rho_{\rm in}(\theta).
\]

After physical detector interaction, define an electrical-output subsystem/state

\[
\rho_E(\theta).
\]

All inaccessible internal degrees of freedom have already been traced out at this boundary.

Define intrinsic electrical quantum Fisher information

\[
\boxed{
F_E^Q(\theta)=F_Q[\rho_E(\theta)].
}
\]

and intrinsic information-transfer efficiency

\[
\boxed{
\eta_{\rm int}(\theta)
=\frac{F_E^Q(\theta)}{F_{\rm in}^Q(\theta)}.
}
\]

By quantum data processing,

\[
\boxed{0\le\eta_{\rm int}\le1.}
\]

This is the cleanest detector-intrinsic object when a fully quantum electrical output subsystem can be specified.

---

# 2. Classical complete electrical trajectory

In a semiclassical detector, let `Z` be the complete accessible electrical trajectory before deliberate readout coarse graining, with likelihood

\[
p_Z(z|\theta).
\]

Its path Fisher information is

\[
\boxed{
F_Z(\theta)
=\mathbb E_\theta[(\partial_\theta\ln p_Z)^2].
}
\]

Define

\[
\boxed{
\eta_Z=F_Z/F_{\rm in}^Q.
}
\]

This is the classical analogue of the electrical-output QFI boundary.

---

# 3. Measurement/readout coarse graining

Let the actually recorded data `Y` be generated from `Z` by a parameter-independent Markov kernel

\[
p(y|z).
\]

Examples:

- deterministic analog filtering;
- threshold crossing;
- pulse integration;
- event timestamp extraction;
- digitization;
- finite ADC quantization;
- dead-time logic;
- compression/discarding side information.

Classical FI data processing gives

\[
\boxed{F_Y\le F_Z.}
\]

Thus

\[
\boxed{
\eta_{\rm meas}
\le
\eta_{\rm int/classical\ complete}.
}
\]

Any information-bandwidth theorem must state at which level it is defined.

---

# 4. Invertible transformations preserve FI

If `Y=f(Z)` is a one-to-one deterministic transformation independent of `theta`, then

\[
\boxed{F_Y=F_Z.}
\]

Consequences:

- deterministic known gain is FI-neutral;
- deterministic known delay is FI-neutral;
- an invertible analog filter is FI-neutral in the ideal complete record;
- changing voltage/current units is FI-neutral.

This is why ordinary amplitude rolloff does not automatically define information bandwidth.

---

# 5. Strict information loss requires non-sufficiency

A coarse-grained record loses no FI iff it is sufficient for the parameter under the relevant statistical family.

In general, strict loss arises when distinct microscopic/electrical records with different scores are mapped to the same measured output.

Examples already obtained:

### Unresolved capture depth

Different absorption positions generate different deterministic delays but only a timestamp is retained:

\[
\eta_I=\eta_c|\mathbb E e^{-i\omega D}|^2.
\]

Retaining position side information restores the ideal deterministic-delay information.

### Integrated avalanche charge

Random gain marks are discarded into one integrated analog amplitude; excess-noise statistics can then reduce FI.

Retaining individually resolved event timestamps and marks can preserve primary count FI.

### RC + downstream voltage noise

The noisy channel is not invertible; attenuation amplifies downstream noise when referred back to the detector input.

---

# 6. Two distinct bandwidth definitions

For a frequency-parametrized weak-modulation task, define intrinsic and measured information efficiencies

\[
\eta_{\rm int}(\omega),
\qquad
\eta_{\rm meas}(\omega).
\]

For target fraction `q`, define pointwise information bandwidths

\[
\boxed{
\Omega_q^{\rm int}
=\sup\{\Omega:\eta_{\rm int}(\omega)\ge q\eta_{\rm int}(0)
\;\forall |\omega|\le\Omega\},
}
\]

\[
\boxed{
\Omega_q^{\rm meas}
=\sup\{\Omega:\eta_{\rm meas}(\omega)\ge q\eta_{\rm meas}(0)
\;\forall |\omega|\le\Omega\}.
}
\]

Data processing implies

\[
\eta_{\rm meas}(\omega)\le\eta_{\rm int}(\omega)
\]

pointwise for the same input task, but a simple universal ordering of the **normalized-to-DC bandwidths** need not follow if the readout also changes the DC efficiency. State the chosen normalization explicitly.

A source-QFI-normalized absolute threshold avoids that ambiguity.

---

# 7. Recommended UPRP theorem target

The primary fundamental-detector theorem should target the earliest physically meaningful **electrical output boundary**:

\[
\boxed{
\text{optical input}
\to
\text{electrical subsystem/complete electrical trajectory}.
}
\]

This avoids making arbitrary external filters, amplifiers, ADC choices, or threshold algorithms part of a supposedly material-independent detector law.

Then compose a separate readout theorem:

\[
\boxed{
\text{intrinsic electrical information}
+\text{readout transfer/noise/sampling resources}
\to
\text{measured information}.
}
\]

This separation should become part of the final paper architecture.

---

# 8. Boundary ambiguity is itself physical

The phrase `complete electrical record` must not be interpreted as omniscient access to every microscopic detector coordinate.

For example, an absorption position `r` that is not encoded into any accessible electrode degree of freedom is an internal latent variable and must be traced/coarse-grained before the electrical boundary.

If the device adds a segmented electrode or another channel that reveals `r`, then the physical output subsystem has changed and more information can become electrically accessible.

Thus detector architecture can convert internal side information into accessible electrical information.

This is a real resource, not a bookkeeping trick.

---

# 9. Relation to DQE and NEP

Conventional DQE already embodies a related idea: compare output SNR/information-like performance to incident quanta. UPRP extends the logic temporally and at the trajectory/QFI level.

Do not claim the general principle of information data processing or sufficient statistics as novel.

The project-specific role is to use it to distinguish **intrinsic photodetection information transfer** from conventional amplitude bandwidth and implementation-specific readout losses.

---

# 10. Revised resource hierarchy

The overall chain should now be written as two layers:

## Intrinsic detector layer

\[
\boxed{
\text{source task}
+\text{optical capture resources}
+\text{microscopic coupling}
+\text{apparatus preparation/support}
+\text{transport/geometry/timing resources}
+\text{thermokinetic resources}
\Rightarrow
\eta_{\rm int}(\omega).
}
\]

## Readout layer

\[
\boxed{
\eta_{\rm int}(\omega)
+\text{filter/noise/sampling/quantization/algorithm resources}
\Rightarrow
\eta_{\rm meas}(\omega).
}
\]

---

# 11. Immediate implications for prior WPs

- WP3 event-timestamp bounds are **record-specific**, not automatically complete-analog-record bounds.
- WP11 spatial-delay sinc rolloff is a timestamp/count coarse-graining theorem.
- WP12 RC invariance applies to the ideal complete analog record; the noisy amplifier theorem is a measured-record result.
- WP13 avalanche excess-noise penalty depends on whether individual events/marks are retained or integrated.
- Any final claim must label its output record explicitly.

---

# 12. Next step

Revise `PROBLEM.md` and eventually the paper outline so the intrinsic versus measured distinction is explicit from the start. Then test all future candidate bandwidth limits against the invertible-processing/sufficiency adversarial check before treating them as fundamental.
