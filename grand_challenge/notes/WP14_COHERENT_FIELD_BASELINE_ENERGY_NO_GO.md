# WP14 — Coherent-field no-go for arbitrary waveform bounds based only on baseline energy

**Date:** 2026-08-21

## Status

**Decisive scope no-go.**

WP12's mean-energy temporal Fisher-area law does **not** extend to an arbitrary family of quantum optical states whose waveform parameter may alter the field state in an unconstrained way. A coherent optical carrier can acquire an infinitesimal arbitrarily high-frequency sideband at first order in the parameter while the sideband contributes energy only at second order. Hence the baseline mean energy alone cannot bound the QFI of arbitrary waveform tangents.

This does not weaken WP10/WP12. It identifies their essential physical encoding assumption: the temporal waveform modulates the probability distribution of **pre-existing time translations/random event centers** of a fixed excitation, rather than synthesizing new high-energy spectral components as the parameter changes.

A broader quantum-waveform resource theorem would have to include a tangent/control resource such as second-order energy injection, modulation bandwidth, or generator cost.

---

## 1. Periodic positive-frequency coherent field

Consider bosonic frequency modes `a_n` on a period `T`, with

`omega0=2*pi/T`,

and Hamiltonian

`H=hbar*omega0 sum_{n>=0} n a_n^dagger a_n`.

Take a baseline coherent state occupying carrier mode `n0>0` with amplitude `A`:

`alpha_n(0)=A delta_{n,n0}`.

Let

`Nbar=|A|^2`.

The baseline temporal field amplitude is

`beta_0(t)=A/sqrt(T) exp(-i n0 omega0 t)`,

and its direct-detection intensity is constant,

`lambda_0(t)=Nbar/T`.

Baseline mean energy is

`E0=hbar*omega0*n0*Nbar`.

---

## 2. One-upper-sideband encoding of an intensity mode

For any positive integer `k`, define a local waveform family by adding an upper sideband:

`alpha_{n0+k}(epsilon)=epsilon A/2`,

with the carrier unchanged.

Then

`beta_epsilon(t)`

`=A/sqrt(T) exp(-i n0 omega0 t)`

` + epsilon A/(2sqrt(T)) exp[-i(n0+k)omega0t]`.

Its intensity is

`lambda_epsilon(t)=|beta_epsilon(t)|^2`

`= (Nbar/T)[1+epsilon cos(k omega0 t)+epsilon^2/4]`.

Therefore at `epsilon=0` the **fractional intensity tangent is exactly**

`u_k(t)=cos(k omega0 t)`.

The corresponding ideal classical Poisson direct-detection FI is

`F_Poisson = int_0^T [partial_epsilon lambda]^2/lambda_0 dt`

`=Nbar/2`.

---

## 3. Coherent-state QFI is independent of sideband frequency

For a multimode coherent state whose amplitude vector depends smoothly on a real parameter, the pure-state QFI is

`F_Q=4 ||partial_epsilon alpha||^2`

when the irrelevant global phase convention is fixed in the usual coherent-state representation.

Here

`||partial_epsilon alpha||^2=Nbar/4`,

so

`boxed: F_Q=Nbar`.

Relative to the ideal Poisson intensity FI,

`boxed: F_Q/F_Poisson=2`.

Crucially, this QFI is **independent of `k`**.

For every arbitrarily high positive sideband mode `n0+k`, the same baseline carrier state can therefore be embedded in a parameter family with the same first-order intensity modulation amplitude and the same local QFI.

---

## 4. Baseline-energy area law fails for unrestricted state families

The baseline state and its mean energy `E0` are identical for every choice of `k`.

Yet for each `k`, the family can encode finite QFI about the `k`th temporal intensity harmonic. If one attempted to assign a universal per-mode retention spectrum to *all possible independently chosen source-state tangents* and sum it over arbitrarily many `k`, no finite bound depending only on `E0` could hold.

The reason is transparent from the energy expansion. The new sideband occupation is quadratic:

`<n_{n0+k}>=epsilon^2 Nbar/4`.

Thus

`E(epsilon)=E0`

`+epsilon^2 [Nbar/4] hbar*omega0(n0+k)`.

The high-frequency energetic cost enters at **second order in the parameter**, whereas QFI is itself a second-order distinguishability quantity built from the first derivative of the state.

A theorem using only the zeroth-order baseline energy misses the resource supplied by the parameter-dependent modulation operation.

---

## 5. Same intensity tangent does not specify a unique quantum encoding

For `k<=n0`, one may instead distribute the amplitude tangent symmetrically over upper and lower sidebands:

`partial_epsilon alpha_{n0+k}=A/4`,

`partial_epsilon alpha_{n0-k}=A/4`.

The two carrier--sideband interference terms add to the same unit fractional intensity tangent `cos(k omega0 t)`.

Now

`||partial_epsilon alpha||^2=Nbar/8`,

so

`F_Q=Nbar/2`,

exactly equal to the ideal Poisson direct-detection FI.

Thus two quantum state families can have the **same first-order intensity waveform** but different QFI:

- symmetric sidebands: `F_Q=Nbar/2`;
- one upper sideband: `F_Q=Nbar`.

This is a concrete demonstration that an intensity waveform does not by itself specify the full quantum statistical experiment.

The one-sided family contains additional phase-sensitive distinguishability invisible to direct intensity detection.

---

## 6. Why WP10/WP12 survive

WP10/WP12 impose a much more specific encoding:

`rho_epsilon = int p_epsilon(t) U_t sigma U_t^dagger dt`,

where `sigma` is fixed and only the **probability distribution of latent event time** changes.

No new high-energy sector is introduced as `epsilon` changes. All temporal modes must be constructed from overlaps between energy sectors already populated in the baseline excitation. That is why the mean baseline energy controls the total random-time mode budget.

The coherent-sideband counterexample changes the quantum state family itself in a way that injects arbitrarily high-frequency support at first order in amplitude.

Therefore there is no contradiction.

---

## 7. Implication for classical Poisson direct-detection physics

Paper 2's source model is a classical Poisson **intensity** process. A quantum realization as independent incoherent event marks naturally belongs to the WP10/WP12 random-event class.

A phase-coherent laser field can have the same Poisson photocount statistics under direct detection while carrying additional phase-sensitive quantum information. Hence Poisson counting statistics alone do not define the quantum source.

Any manuscript connecting WP12 to photodetection must state which source class is meant:

- independent random quantum events / phase-insensitive direct-detection source: WP12 applies;
- arbitrary coherent state engineering with phase-sensitive measurements: WP14 shows baseline energy alone is insufficient.

---

## 8. Candidate broader resource

The counterexample suggests what a more general waveform theorem would need to count.

For the one-sideband family,

`E''(0)= (Nbar/2) hbar*omega0(n0+k)`.

The local QFI is `Nbar`. Thus the high-frequency sideband resource is visible in the **curvature of energy with respect to the waveform parameter**, even though it is absent from the baseline energy.

Possible future resources include:

- `partial_epsilon^2 <H>|_0`;
- norm/energy of the state tangent `|dot psi>`;
- control Hamiltonian bandwidth or action required to synthesize the tangent;
- a joint baseline-state + encoding-map resource.

No universal theorem in these terms is yet claimed.

---

## 9. Decision

Do **not** attempt to state WP12 as a bound for arbitrary quantum waveform encodings.

Current high-confidence scope remains:

> **random temporal-distribution encoding by a fixed semibounded-energy quantum excitation**, followed by arbitrary parameter-independent quantum detector processing.

Within that scope, WP12 is measurement-independent and survives coherent detector memory.

WP14 identifies the next conceptual fork:

1. publish the random-time resource theorem as a sharp foundational result if priority survives; or
2. seek a still broader theorem by explicitly including the energetic/control cost of the parameter-dependent source encoding.
