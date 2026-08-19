# WP0 Correction — Unbounded Information Bandwidth and the Proper Task-Normalized Objective

**Date:** 2026-08-19

## Executive correction

The candidate

\[
B_{\mathcal I}
=\int_{-\infty}^{\infty}\frac{d\omega}{2\pi}\eta_{\mathcal I}(\omega)
\]

is useful for comparing finite-response models, but **it is not generically finite and cannot itself be the left-hand side of a universal photodetection theorem without an optical signal-bandwidth or microscopic-dynamics constraint**.

The simplest counterexample is an ideal continuous-time photon counter. For a coherent/Poisson input, it has

\[
\eta_{\mathcal I}(\omega)=1
\]

at every modulation frequency in the white-Poisson point-process model, and therefore

\[
B_{\mathcal I}=\infty.
\]

This is not a detector pathology. It means the mathematical input model itself permits arbitrarily rapid independent intensity modulation and an ideal instantaneous counting measurement.

**Status:** PROVED conceptual correction.

---

# 1. Exact Poisson Fisher-information calculation

Let an inhomogeneous Poisson photon stream have rate

\[
\lambda(t;\epsilon)
=\Phi_0[1+\epsilon s(t)],
\qquad |\epsilon|\ll1.
\]

For an observed Poisson trajectory over \([0,T]\), the Fisher information for \(\epsilon\) is

\[
F_\epsilon(T)
=\int_0^Tdt\,
\frac{[\partial_\epsilon\lambda(t;\epsilon)]^2}{\lambda(t;\epsilon)}.
\]

At \(\epsilon=0\),

\[
\boxed{
F_\epsilon(T)
=\Phi_0\int_0^Tdt\,s^2(t).
}
\]

For a sinusoidal modulation

\[
s(t)=\cos\Omega t,
\]

and an observation interval containing many periods,

\[
\boxed{
\dot F_\epsilon
=\lim_{T\to\infty}\frac{F_\epsilon(T)}{T}
=\frac{\Phi_0}{2},
}
\]

independent of \(\Omega\).

An ideal photon counter reproduces the incident point process, so

\[
F_{\rm out}=F_{\rm in}
\]

for every \(\Omega\), giving

\[
\boxed{
\eta_{\mathcal I}(\Omega)=1\quad\forall\Omega.
}
\]

Thus the unweighted integral over all baseband frequencies diverges.

---

# 2. What went wrong with the original bandwidth integral

The original integral implicitly treated every temporal Fourier mode as an independently available signal mode extending to infinite frequency while assigning no additional source resource to widening that mode family.

In a physical optical field, arbitrarily fast envelope/intensity variation generally requires one or more of:

- increasing optical spectral bandwidth;
- sidebands farther from the carrier;
- shorter wave packets / broader temporal-mode support;
- additional field energy or altered photon-frequency distribution;
- a detector-field coupling capable of resolving the corresponding temporal structure.

Therefore an ultimate theorem cannot silently allow an infinite-bandwidth optical source and then attribute the resulting infinite information bandwidth to the detector.

This is exactly the source/detector resource leakage that `AGENTS.md` warned against.

---

# 3. Correct primary objective: task-weighted information efficiency

Let \(\mathcal J_{\rm in}(\omega)\ge0\) denote the incident optical QFI spectral density for the parameter-estimation task being considered. Let

\[
\eta_{\mathcal I}(\omega)
=\frac{\mathcal J_{\rm out}(\omega)}{\mathcal J_{\rm in}(\omega)}
\]

where defined.

Then define the total task efficiency

\[
\boxed{
\bar\eta_{\mathcal I}[\mathcal J_{\rm in}]
=
\frac{
\int\frac{d\omega}{2\pi}\,
\mathcal J_{\rm in}(\omega)\eta_{\mathcal I}(\omega)
}{
\int\frac{d\omega}{2\pi}\,
\mathcal J_{\rm in}(\omega)
}
=
\frac{F_{\rm out}}{F_{\rm in}^{Q}}.
}
\]

This is dimensionless and obeys

\[
0\le\bar\eta_{\mathcal I}\le1.
\]

It is the correct information-transfer objective for a specified optical task/mode family.

**Status:** DEFINITION / preferred WP0 objective.

---

# 4. Flat finite-band specialization

For a task with equal incident information weight over

\[
|\omega|\le\Omega_s
\]

and zero weight outside, define

\[
\boxed{
\bar\eta_{\mathcal I}(\Omega_s)
=
\frac{1}{2\Omega_s}
\int_{-\Omega_s}^{\Omega_s}d\omega\,
\eta_{\mathcal I}(\omega).
}
\]

An ideal detector gives

\[
\bar\eta_{\mathcal I}(\Omega_s)=1
\]

for every finite \(\Omega_s\).

This does not assert infinite detector resources. It simply says that an idealized zero-latency detector is perfect on any prescribed finite task band.

The nontrivial research question is therefore inverted:

> **What detector resources are necessary to maintain \(\bar\eta_{\mathcal I}(\Omega_s)\ge\eta_*\) as the required signal bandwidth \(\Omega_s\) increases?**

This is a better-posed sensitivity-speed-resource problem.

---

# 5. Revised theorem form

Instead of seeking

\[
B_{\mathcal I}\le f(T,\Phi,\sigma,\mathcal A,\ldots),
\]

seek a resource requirement of the form

\[
\boxed{
\mathcal R_{\rm det}
\ge
G(\Omega_s,\eta_*,T,\hbar\omega_{\rm opt},\Phi_0,\ldots),
}
\]

where \(\mathcal R_{\rm det}\) is a detector-internal kinetic/energetic/coupling resource and

\[
\bar\eta_{\mathcal I}(\Omega_s)\ge\eta_*.
\]

Equivalently one may maximize

\[
\bar\eta_{\mathcal I}(\Omega_s)
\]

subject to a fixed resource budget.

This formulation cleanly separates:

1. **source task:** which temporal optical modes must be estimated;
2. **available optical information:** \(F_{\rm in}^{Q}\);
3. **detector transfer:** \(\eta_{\mathcal I}(\omega)\);
4. **detector resource budget:** the object still to be identified.

---

# 6. Why thermodynamics alone cannot set a speed scale

A response bandwidth has dimensions of inverse time. Steady entropy production and activity are rates, so dimensionally they can enter a bound, but the rare-fast-state construction shows that stationary averages need not detect large latent transition rates.

More fundamentally, quantum dynamics can be made arbitrarily fast if the relevant Hamiltonian/coupling norm is allowed to grow without bound. Classical Markov dynamics has the analogous freedom in kinetic prefactors/escape rates.

Therefore the project should now distinguish:

- **thermodynamic resources:** fluxes, affinities, heat/work, EPR;
- **kinetic resources:** transition-rate scales, escape rates, generator norms;
- **quantum dynamical resources:** Hamiltonian norm/variance, coupling strength, bath spectral density;
- **optical resources:** photon flux, carrier energy, spectral bandwidth, mode count.

A universal detector-speed theorem that omits all kinetic/coupling scales is now strongly disfavored.

**Status:** CONJECTURE supported by explicit Markov counterexamples; rigorous general no-go theorem remains to be written.

---

# 7. Direct-feedthrough issue

For a Markov readout whose counted electrical edge is directly modulated by the optical input, the susceptibility contains a frequency-independent term

\[
\chi_{I\Phi}(\omega)
\supset
\mathbf 1^T\mathcal J_{\Phi}^{(1)}\pi.
\]

Such an idealized model can retain nonzero response as \(|\omega|\to\infty\), making any all-frequency bandwidth integral divergent even with finite internal relaxation rates.

To study a finite **transduction** bandwidth, one should either:

1. use a finite source task band; or
2. restrict to **proper transducers** in which optical input and electrical output are distinct channels and

\[
\boxed{
\mathcal J_{\Phi}^{(1)}=0,
}
\]

so that response reaches the electrical output only through internal dynamics.

This restriction must be explicit, not silently assumed.

---

# 8. Revised WP0 status

### Solved

- coordinate-invariant information normalization;
- source QFI normalization;
- relation to temporal DQE;
- proof that unweighted infinite-band integration is ill posed;
- task-weighted finite-band efficiency definition.

### Still open

- exact optical QFI spectral density for general quantum states;
- best definition of a detector-internal kinetic/coupling resource;
- whether a universal lower resource requirement exists for proper transducers;
- whether microscopic optical sum rules or quantum speed limits provide the needed rate scale.

---

# 9. Immediate research target

The project should now attempt a **no-go theorem**:

> No finite upper bound on photodetector temporal information transfer can depend only on stationary thermodynamic observables \(\{T,\Phi_0,\sigma,\mathcal A,\eta\}\) without a source-bandwidth constraint and/or a microscopic detector kinetic/coupling resource.

The three-state rare-fast counterexample supplies the first constructive proof component. The ideal Poisson counter supplies the source-bandwidth obstruction.

The next task is to determine the weakest additional resource that repairs the theorem.