# WP22 — Continuum-limit rigor for the operational survival law

**Date:** 2026-08-22

## Status

**Continuum gate substantially closed.**

WP19 stated the continuum operational survival theorem through a controlled periodic approximation. WP20 repaired the collective proof at finite periodic spacing. This note makes the passage to a general positive excitation-frequency probability measure explicit and removes any need for a smooth density.

Let `mu` be a probability measure on `[0,infinity)` with finite first moment

`omega_bar = int_[0,infinity) omega mu(domega) < infinity`.

For spacing `delta>0`, define the lower-bin quantization

`q_n^(delta) = mu([n delta,(n+1)delta))`, `n=0,1,...`.

Then the periodic random-time model with sector spacing `delta` has exact tail

`T_k^(delta)=sum_{m>=k}q_m^(delta)=mu([k delta,infinity))`

and discrete mean excitation frequency

`omega_bar_delta = delta sum_n n q_n^(delta)`

`= int delta floor(omega/delta) mu(domega)`.

Hence

`0<=omega_bar_delta<=omega_bar`

and

`omega_bar_delta -> omega_bar`

by monotone/dominated convergence as `delta->0`.

WP20 gives for every finite-copy collective detector

`R_delta(k) <= T_k^(delta)`.

The continuum theorem follows from this exact discretization.

---

## 1. Pointwise survival theorem at arbitrary threshold

Fix `nu>0`.

Choose

`k_delta = floor(nu/delta)`

for sufficiently small `delta`, so `k_delta>=1`, and define

`nu_delta=k_delta delta`.

Then

`nu_delta <= nu`,

`nu_delta -> nu`,

and the exact discrete tail is

`T_(k_delta)^(delta)=mu([nu_delta,infinity))`.

As `delta->0`, the sets `[nu_delta,infinity)` decrease to `[nu,infinity)` along any nested sequence of spacings for which `nu_delta` increases to `nu`; more generally the same limit follows by sandwiching thresholds. Continuity from above of finite measures gives

`T_(k_delta)^(delta) -> mu([nu,infinity))`.

Suppose a sequence of physical detector schemes has source-normalized mode-trace retentions satisfying

`R_delta(k_delta) -> R(nu)`

at this target frequency.

Then WP20 implies

`R_delta(k_delta) <= T_(k_delta)^(delta)`

for every `delta`, and therefore

`boxed: R(nu) <= S_mu(nu):=mu([nu,infinity))`.

No continuity of a density is required, and atoms in `mu` are retained correctly by the closed-tail convention.

### Limsup form

If a pointwise detector limit is not assumed, the robust statement is

`boxed: limsup_(delta->0) R_delta(k_delta) <= mu([nu,infinity))`.

Thus every subsequential continuum limit obeys the same survival ceiling.

---

## 2. Threshold-sequence lemma

For completeness, let `a_j -> nu` with `a_j<=nu` and `a_j` tending upward to `nu` after passage to a monotone subsequence. Then

`[a_j,infinity) downarrow [nu,infinity)`

and therefore

`mu([a_j,infinity)) -> mu([nu,infinity))`.

For a general nonmonotone sequence `a_j<=nu`, fix `epsilon>0`. Eventually

`nu-epsilon <= a_j <= nu`,

so

`mu([nu,infinity)) <= mu([a_j,infinity)) <= mu([nu-epsilon,infinity))`.

Letting `epsilon downarrow0` and using continuity from above again proves convergence to `mu([nu,infinity))`.

Hence the floor discretization gives the desired closed-tail limit without an atom-free assumption.

---

## 3. Area theorem from piecewise-constant interpolation

Define the positive-frequency interpolation

`mathcal R_delta(nu)=R_delta(k)`

for

`nu in [k delta,(k+1)delta)`, `k>=1`,

and set `mathcal R_delta(nu)=0` on `[0,delta)`.

Then exactly

`int_0^infinity mathcal R_delta(nu)dnu`

`=delta sum_(k>=1)R_delta(k)`

`<=delta sum_(k>=1)T_k^(delta)`

`=delta sum_n n q_n^(delta)`

`=omega_bar_delta`

`<=omega_bar`.

Thus **every discretized physical detector already obeys the continuum-dimensional area coefficient exactly**, before taking a limit:

`boxed: int_0^infinity mathcal R_delta(nu)dnu <= omega_bar_delta <= omega_bar`.

If `mathcal R_delta_j -> R` almost everywhere along any sequence `delta_j->0`, Fatou gives

`int_0^infinity R(nu)dnu`

`<= liminf_j int_0^infinity mathcal R_delta_j(nu)dnu`

`<=omega_bar`.

Therefore

`boxed: int_0^infinity R(nu)dnu <= omega_bar`.

With even extension,

`boxed: int_R R(nu)dnu <=2omega_bar = 2Ebar^+/hbar`.

This argument needs only finite first moment and nonnegative retentions.

---

## 4. Weak-limit formulation

Pointwise convergence of detector interpolants is stronger than needed for the area theorem.

Because `0<=mathcal R_delta<=1`, the family is bounded in `L^infinity` on every finite frequency interval. Any weak-* accumulation point `R` satisfies, for every finite `L`,

`int_0^L R(nu)dnu`

`=lim_j int_0^L mathcal R_delta_j(nu)dnu`

along the convergent subsequence when tested against the indicator (or continuous approximants to it), and hence

`int_0^L R <= omega_bar`.

Letting `L->infinity` gives the same global area law by monotone convergence.

Thus the operational area theorem is stable under very weak detector convergence.

The pointwise survival law additionally requires modewise convergence (or is stated directly as a limsup bound along lattice frequencies approaching the target).

---

## 5. Pointwise Planck-scale inverse law for general measures

For any probability measure `mu` on `[0,infinity)` with finite first moment,

`omega_bar >= nu mu([nu,infinity))`.

This is simply

`int omega mu(domega) >= int_[nu,infinity) omega mu(domega) >= nu mu([nu,infinity))`.

Combining with the operational survival theorem gives

`boxed: omega_bar >= nu R(nu)`.

In energy units,

`boxed: Ebar^+ >= hbar nu R(nu)`.

At ordinary temporal modulation frequency `f=nu/(2pi)`,

`boxed: Ebar^+ >= h f R(2pi f)`.

If a detector guarantees retention at least `q0` at the top of a band `|f|<=B`, then

`boxed: Ebar^+ >= h B q0`.

No integration over the band is required for this corollary.

---

## 6. Exact equality family under the discretization

Take the exponential continuum law

`mu(domega)=beta exp(-beta omega)domega`.

The lower-bin probabilities are

`q_n^(delta)`

`=exp(-beta n delta)-exp[-beta(n+1)delta]`

`=(1-r)r^n`,

with

`r=exp(-beta delta)`.

Thus the canonical lower-bin discretization of the exponential measure is **exactly** the geometric equality family of WP19 for every `delta`.

Its discrete survival is

`T_k^(delta)=r^k=exp(-beta k delta)`.

The canonical phase POVM saturates

`R_delta(k)=T_k^(delta)`

for every mode and every spacing.

Therefore as `delta->0`,

`R(nu)=exp(-beta nu)=mu([nu,infinity))`

pointwise, and

`int_0^infinity R(nu)dnu=1/beta=omega_bar`.

This shows that the continuum theorem and its constant are attained through an exact discretization sequence, not only through an informal asymptotic analogy.

---

## 7. Relation to continuous-spectrum quantum states

A subtle but important point remains.

A literally uniform random-time distribution on the noncompact real line is not a normalizable probability law, and complete time twirling of a continuous-spectrum pure state generally does not produce an ordinary trace-class diagonal density operator in the same way as periodic `U(1)` twirling.

Therefore the continuum theorem should **not** be presented as though there were a normalized uniform-time baseline state on `R`.

The rigorous physical formulation is instead:

1. work on a periodic observation/time circle of period `T=2pi/delta`;
2. apply the exact finite-copy theorem there;
3. bin the fixed positive excitation-frequency measure as above;
4. take `T->infinity` / `delta->0` while tracking the detector's local mode-retention limit.

This is analogous to the standard box/large-time normalization used for stationary spectral densities.

A future operator-algebraic stationary-process formulation may remove the periodic scaffold, but it is unnecessary for the current resource inequality.

---

## 8. General spectral measures and degeneracy

The measure `mu` need not have a density. It may contain:

- atoms;
- absolutely continuous pieces;
- singular continuous pieces;
- arbitrary mixtures of these.

The discretization uses only bin masses.

Likewise internal degeneracy within an energy bin/sector does not affect the theorem after purification: `q_n^(delta)` is the total participating probability in the corresponding excitation-frequency bin, and the detector is given the most favorable purification/reference access when deriving the upper bound.

Thus the continuum law is naturally a theorem about the **spectral probability measure of the total time-translation generator**, not specifically about a smooth optical spectrum.

---

## 9. Decision

The continuum part of the operational theorem is now sufficiently precise for manuscript development.

Publication-grade statement:

> Let `mu` be the positive excitation-frequency spectral probability measure of a fixed random-time-encoded excitation, with finite first moment. In periodic approximants formed by lower-bin quantization of `mu`, every finite-copy collective measurement obeys `R_delta(k)<=mu([k delta,infinity))`. Consequently every modewise continuum limit obeys `R(nu)<=mu([nu,infinity))`, and every a.e./weak limiting retention spectrum obeys `int_0^infinity R<=int omega mu(domega)`. The exponential spectral law with canonical phase/time readout attains both bounds exactly.

Remaining high-value gate:

- make WP13's independent quantum-marked Poisson-to-physical-bosonic-field map equally explicit;
- then perform a final integrated hostile review and manuscript decision.