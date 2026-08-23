# WP08 — Quadratic spectral-synthesis sum law and coherent-sideband energy budget

**Date:** 2026-08-22

**Branch:** `agent/autonomous-temporal-information-law`

**Status:** analytic PASS for a discrete family of mutually orthogonal baseline-empty endpoint sectors, arbitrary finite-copy collective POVMs, and the multimode coherent-state construction. The theorem is a direct modewise extension of WP07 and therefore mathematically elementary once WP07 is available, but it closes the earlier coherent-waveform baseline-energy loophole in the natural resource variable: **second-order spectral synthesis**. Coherent-state displacement/Holevo/heterodyne mathematics is prior art. Candidate novelty is the frequency-resolved resource sum/energy law and its placement alongside the pre-existing-population survival law. Priority remains **unverified, not certified**.

## 1. Motivation

The inherited coherent-sideband no-go showed that baseline mean energy cannot constrain arbitrary waveform synthesis. A fixed carrier can acquire an arbitrarily high-frequency infinitesimal sideband with finite local information because the new sideband population enters only at second order in modulation amplitude.

WP07 repaired one mode:

`Tr F_N/N <= Delta T_U(0)`

for a two-quadrature tangent that enters a previously empty endpoint sector.

The immediate question is whether an entire collection of new temporal/spectral modes obeys a global budget analogous to the earlier survival-function sum law.

It does.

## 2. Multimode boundary-synthesis model

Let

`theta=(x_1,y_1,...,x_K,y_K)`

parameterize a `C^2` family of density operators `rho(theta)` near `theta=0`, with baseline

`rho0=rho(0)`

and support projector

`P=supp(rho0)`.

Let `P_k`, `k=1,...,K`, be mutually orthogonal projectors satisfying

`P_k P=0`.

Thus every `P_k` is an endpoint sector absent from the baseline.

For mode `k`, let the two first derivatives be represented by a complex tangent `A_k`:

`D_(k,c)=(A_k+A_k^dagger)/2`,

`D_(k,s)=(A_k-A_k^dagger)/(2i)`.

Assume

`A_k=P_k A_k P`.

Define the population synthesized into sector `k`:

`T_k(theta)=Tr[P_k rho(theta)]`.

At the baseline,

`T_k(0)=0`,

`grad T_k(0)=0`.

Let

`Delta_k T_k(0)=partial_(x_k)^2 T_k(0)+partial_(y_k)^2 T_k(0)`.

The parameter normalizations are physical conventions and must be kept fixed when comparing Fisher information with curvature.

## 3. Same-record modewise theorem

Fix **one POVM** on `N` independently encoded copies. It may be arbitrary and entangled across all copies.

Let `F_(N,k)` denote the `2 x 2` classical Fisher block for parameters `(x_k,y_k)` extracted from that same measurement record.

WP07 applies separately to every mode without changing the POVM:

`Tr F_(N,k)/N <= J_k`,

where

`J_k=Tr(A_k rho0^+ A_k^dagger)`.

Second-order positivity gives

`J_k <= Delta_k T_k(0)`.

Therefore, simultaneously for all modes,

> **Modewise quadratic synthesis law**
>
> `boxed: Tr F_(N,k)/N <= Delta_k T_k(0)`.

This is not a set of separately optimized measurement bounds. Every inequality can be applied to the blocks of one fixed physical measurement.

## 4. Arbitrary weighted sum law

Let `w_k>=0` be arbitrary fixed resource weights. Multiplying each modewise inequality and summing gives

> **Weighted spectral-synthesis sum law**
>
> `boxed: sum_k w_k [Tr F_(N,k)/N] <= sum_k w_k Delta_k T_k(0)`.

No measurement incompatibility correction is required on the right-hand side because incompatibility can only reduce the classical Fisher information obtainable from one common record.

The mutual orthogonality of the `P_k` sectors ensures that the synthesized populations represent distinct resource sectors and are not double counted.

For unit weights,

`sum_k Tr F_(N,k)/N <= sum_k Delta_k T_k(0)`.

Define the dimensionless quadratic synthesis budget

`S_syn^(2):=(1/4)sum_k Delta_k T_k(0)`.

Then

> `sum_k [Tr F_(N,k)/(4N)] <= S_syn^(2)`.

This is the natural boundary-synthesis counterpart of a survival-population mode budget.

## 5. Frequency-weighted energy law

Associate mode `k` with a requested temporal frequency/gap `nu_k>0`.

Define the **gap-weighted quadratic spectral-synthesis energy**

`E_gap,syn^(2):=(hbar/4) sum_k nu_k Delta_k T_k(0)`.

Then

> **Quadratic temporal-information energy law**
>
> `boxed: sum_k hbar nu_k [Tr F_(N,k)/(4N)] <= E_gap,syn^(2)`.

Equivalently, every unit of two-quadrature local Fisher information synthesized at a larger temporal gap carries proportionally larger quadratic spectral cost.

This is a curvature/synthesis resource, not the baseline mean energy.

### Important distinction from total mean-energy curvature

`E_gap,syn^(2)` counts only the newly synthesized endpoint populations with their specified gap weights. It is **not** automatically equal to

`(1/4) Delta_theta Tr(H rho(theta))|_0`.

Other sectors may lose population at second order, and their energy changes can cancel part of the total mean-energy Hessian. A universal theorem must therefore retain the positive frequency-resolved synthesis contribution rather than replace it by an unrestricted signed total-energy curvature.

If each `P_k` lies in a physical energy sector whose excess energy above the chosen resource reference is at least `hbar nu_k`, then the positive projected physical synthesis-energy curvature dominates `E_gap,syn^(2)`.

## 6. Exact multimode coherent-state realization

Consider mutually orthogonal bosonic sideband modes `a_k`, all in vacuum at the baseline, and let the parameter-dependent coherent amplitudes be

`alpha_k(theta)=g_k(x_k+i y_k)`.

All other baseline carrier/reference amplitudes may be arbitrary but parameter independent.

The sideband occupations are

`n_k(theta)=|g_k|^2(x_k^2+y_k^2)`.

Hence

`Delta_k n_k(0)=4|g_k|^2`.

A multimode heterodyne measurement has outcome density, mode by mode,

`p(beta_k|alpha_k)=pi^(-1) exp[-|beta_k-alpha_k|^2]`.

Its Fisher information for the two real displacement coordinates is

`F_(k,xx)=2|g_k|^2`,

`F_(k,yy)=2|g_k|^2`,

so

`Tr F_(k)=4|g_k|^2`.

Therefore

> `boxed: Tr F_(k)=Delta_k n_k(0)`

for every mode simultaneously.

Multimode heterodyne thus saturates the entire unweighted and weighted WP08 sum law:

> `boxed: sum_k w_k Tr F_(k)=sum_k w_k Delta_k n_k(0)`.

The equality is one-copy and uses one fixed simultaneous measurement of all sideband quadratures.

## 7. Physical sideband-energy equality

Let sideband mode `k` have physical photon energy `hbar omega_k`.

Its positive synthesized energy is

`E_k(theta)=hbar omega_k n_k(theta)`.

Hence

`(1/4)Delta_k E_k(0)=hbar omega_k |g_k|^2`.

The heterodyne Fisher block obeys

`(hbar omega_k/4) Tr F_(k)=hbar omega_k |g_k|^2`.

Thus, if the weights are chosen as the **actual sideband photon energies**, the coherent-state family exactly saturates the physical positive synthesis-energy identity

> `boxed: sum_k (hbar omega_k/4) Tr F_(k)`
>
> `= (1/4)sum_k Delta_k E_k(0)`.

For a temporal modulation gap `nu_k` relative to a carrier/reference, one usually has a weaker gap-weighted statement with `nu_k` in place of `omega_k`; the actual physical sideband energy is at least as costly whenever the chosen reference makes `omega_k>=nu_k`.

## 8. Recovery of the original one-sideband counterexample

The inherited WP14 family used

`alpha_sb(epsilon)=epsilon A/2`,

`Nbar=|A|^2`.

Promote it to two quadratures:

`alpha_sb(x,y)=(A/2)(x+i y)`.

Then

`Delta n_sb(0)=Nbar`.

The heterodyne Fisher trace is

`Tr F_het=Nbar`.

Therefore the exact family that invalidated a baseline-energy-only waveform theorem **saturates WP08**.

The loophole has not disappeared by assumption. It has been converted into the correct resource statement:

> baseline energy does not pay for a newly synthesized sideband; quadratic sideband population/energy does.

## 9. Controlled continuum form

Suppose a sequence of finite orthogonal mode decompositions converges to a continuum of baseline-empty spectral sectors labelled by `nu`, with well-defined nonnegative Fisher density `f_N(nu)` and quadratic synthesis-population density `c(nu)` such that

`f_N(nu)/N <= c(nu)`

almost everywhere in the limit.

Whenever the weighted integrals exist, monotone/dominated convergence gives

> `integral hbar nu [f_N(nu)/(4N)] dnu`
>
> `<= (hbar/4) integral nu c(nu) dnu`.

This should be treated as a controlled limit theorem, not asserted for arbitrary operator-valued continua without regularity assumptions.

It implies that maintaining a nonvanishing two-quadrature Fisher density to arbitrarily high frequencies requires divergent quadratic spectral-synthesis energy unless the information spectrum decays sufficiently fast.

## 10. Relation to known displacement and waveform metrology

The following are prior art and are not novelty claims:

- coherent-state displacement estimation;
- simultaneous estimation of conjugate quadratures;
- heterodyne/double-homodyne measurement;
- Holevo/RLD bounds for Gaussian displacement models;
- multimode Gaussian multiparameter metrology;
- linear quantum waveform-estimation Holevo bounds.

Recent Gaussian-metrology work continues to treat complex displacement estimation and explicitly notes the role of the Holevo bound when the SLD directions are incompatible. Linear waveform-estimation literature likewise derives ultimate Holevo limits and implementable quadrature measurements.

WP08 does not compete with those precision bounds. Its candidate contribution is a different statement:

> **the local information spectrum itself is bounded by the second-order spectrum of newly synthesized physical population, with a sharp frequency-weighted sum law valid for arbitrary finite-copy POVMs.**

For coherent states the standard heterodyne displacement model supplies the exact extremizer.

Priority remains unverified.

## 11. Significance for the autonomous program

WP02--WP06 showed that temporal information already present as a robust tangent is constrained by **pre-existing spectral survival**.

WP07--WP08 show that information created through a zero-radius boundary tangent is constrained instead by **quadratic spectral synthesis**.

The two regimes now have parallel resource laws:

### Pre-existing-resource regime

`robust Fisher spectrum <= zeroth-order spectral population`.

### Newly synthesized-resource regime

`Fisher spectrum <= second-order spectral population creation`.

And both admit frequency weighting by `hbar nu`.

This is a substantially cleaner resolution of the coherent-waveform loophole than merely saying that a control Hamiltonian must have some unspecified cost.

## 12. What remains open

WP08 does not solve the mixed case where one exact-gap tangent contains both pre-existing-support and newly synthesized endpoint components.

The main unresolved problem remains:

> find the sharp arbitrary-POVM resource geometry when temporal information is partly carried by pre-existing spectral support and partly generated by support-changing synthesis.

The operator-score cross terms may prevent a simple additive scalar law.

Additional open directions:

1. characterize the exact mixed-endpoint geometry or prove scalar additivity impossible;
2. extend the synthesis sum law to Gaussian families whose covariance, not only displacement, changes;
3. formulate the autonomous clock--signal version when new exchange sectors are synthesized on one or both sides;
4. determine the correct positive control/action accounting when the synthesis is generated dynamically;
5. deepen the priority audit against Gaussian displacement/waveform estimation and second-order resource theories.
