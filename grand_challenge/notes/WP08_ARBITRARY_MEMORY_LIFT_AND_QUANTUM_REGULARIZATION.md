# WP08 — Arbitrary-memory lift and quantum regularization of classical timing plateaus

**Date:** 2026-08-21

## Status

**Strong theorem candidate; major scope extension of WP06/WP07.**

The positive-energy Fisher spectral-area law is not restricted to a final independent-event detector record. It survives **arbitrary subsequent parameter-independent autonomous classical detector memory** by Fisher-information data processing.

This produces a sharp conceptual consequence for Paper 2: a nonzero infinite-frequency plateau such as the ideal deterministic Type-II limit `G -> 1/e` cannot persist once the latent event times entering the memory stage are themselves produced by a finite-excess-energy covariant quantum timing layer.

The result is exact for the factorized architecture stated below and does not require low flux after the quantum timing layer.

---

## 1. Factorized physical architecture

Consider a homogeneous Poisson source of incident excitation centers with baseline rate `Phi0` and weak fractional waveform tangent `u(t)`.

Each incident center at physical time `s` independently carries a quantum excitation whose arrival-time parameter enters by covariant translation. A fixed covariant quantum event-time measurement produces either:

- no event; or
- a classical primary event with timestamp `t=s+Delta` and optional accessible mark `m`.

For one unmarked branch, the event probability is `eta` and the conditional delay density is `f(Delta)`.

For a marked measurement, write the one-event kernel as

`kappa(dm) f_m(Delta) dDelta`,

with total event probability

`eta = int kappa(dm)`.

The complete primary timestamp/mark stream is denoted `Z`.

After `Z` is created, allow an **arbitrary parameter-independent autonomous stochastic channel**

`K: Z -> Y`

whose output `Y` is the accessible detector record. This downstream channel may contain arbitrary classical memory, including:

- deterministic or random dead time;
- paralyzable or nonparalyzable logic;
- saturation;
- state-dependent capture;
- afterpulsing;
- hidden finite or infinite state;
- nonlinear history dependence;
- analog or marked outputs;
- deliberate coarse graining of primary timestamps.

The only crucial structural assumption is the factorization: the quantum timing event `Z` is formed first, and the subsequent memory channel acts on that classical trajectory. A detector whose quantum memory is coherently intertwined with event formation is outside WP08.

---

## 2. The primary timing stream remains Poisson at arbitrary flux

Independent thinning, marking, and iid displacement of a Poisson point process produce a marked Poisson point process.

Therefore, under an incident intensity

`Phi_epsilon(t)=Phi0 [1+epsilon u(t)]`,

the primary timing stream `Z` is a marked Poisson process with mark-resolved output intensity obtained by convolution with the one-event timing kernel.

For the unmarked case,

`lambda_Z(t)=eta Phi0 [1+epsilon (f*u)(t)]`.

The local source-normalized Fisher multiplier of the **complete primary stream** is therefore exactly

`G_Z(nu)=eta |F(nu)|^2`,

where

`F(nu)=int exp(-i nu t) f(t)dt`.

For accessible marks,

`G_Z(nu)=int kappa(dm) |F_m(nu)|^2`.

This is exact for arbitrary incident rate because the primary map is independent marking/displacement of a Poisson process. No low-overlap approximation is used at this stage.

---

## 3. Fisher-operator data processing through arbitrary memory

Let the source Poisson score for tangent `u` be

`S_u`.

For the primary record `Z`,

`S_u^Z = E[S_u | Z]`.

For the final record `Y` obtained from a parameter-independent channel `K(dy|z)`,

`S_u^Y = E[S_u | Y]`

`       = E[ E[S_u|Z] | Y ]`

`       = E[S_u^Z | Y]`.

Conditional expectation is an orthogonal contraction in `L2`, so for every finite-energy source tangent `u`,

`F_Y[u,u] <= F_Z[u,u]`.

Equivalently, for the corresponding Fisher operators,

`boxed: A_Y <= A_Z`

in Loewner order.

Both the primary timing channel and the final factorized detector are autonomous, hence both Fisher operators commute with temporal translations and admit Fourier multipliers `G_Z` and `G_Y`.

For bounded translation-invariant self-adjoint operators, Loewner ordering is equivalent to pointwise multiplier ordering almost everywhere. Therefore

`boxed: 0 <= G_Y(nu) <= G_Z(nu)  a.e.`

This is the central arbitrary-memory lift.

---

## 4. Positive-energy area law survives arbitrary downstream memory

WP07 proves for the covariant primary timing layer

`int_R G_Z(nu)dnu <= 2 E_det^+ / hbar`,

where `E_det^+` is the gauge-invariant detected excess-energy moment above the lower spectral edge of the detected participating state.

Since `G_Y<=G_Z` a.e.,

`boxed: int_R G_Y(nu)dnu <= 2 E_det^+ / hbar`.

Thus **arbitrary downstream classical detector memory cannot increase the total temporal Fisher-transfer spectral area beyond the positive-energy quantum timing resource available at the primary event layer.**

The corresponding flat-band inverse law also survives unchanged. If

`G_Y(2*pi*f) >= q`

for every `|f|<=B`, then

`boxed: E_det^+ >= h B q`.

No property of the downstream dead-time/recovery/saturation model enters this inequality.

---

## 5. General measurable marks

The finite/countable-mark argument of WP06 extends naturally by direct-integral disintegration.

Let the covariant primary event POVM have outcome space `R_t x M`, where `(M,Mcal)` is standard Borel and time translations act only on `t`.

Choose a sigma-finite reference measure `mu(dm)` for the mark marginal in a Naimark/direct-integral realization and write the joint timing subdensity as

`p(t,m)=||u_m(t)||^2`,

with measurable positive-frequency vector amplitudes `u_m`.

Define

`kappa(m)=int p(t,m)dt`

and, where `kappa(m)>0`,

`f_m(t)=p(t,m)/kappa(m)`.

Let the mark-resolved detected excess-frequency moment be

`e(m)=int_0^infinity w ||u_hat_m(w)||^2 dw`.

The vector Hardy inequality applies fiberwise:

`int p(t,m)^2 dt <= kappa(m) e(m)/pi`.

Therefore

`kappa(m) int f_m(t)^2dt`

`= [1/kappa(m)] int p(t,m)^2dt`

`<= e(m)/pi`.

Integrating over marks and using Tonelli,

`int mu(dm) kappa(m) int f_m^2dt <= [1/pi] int mu(dm)e(m)`.

The right side is the total detected excess-frequency moment. Parseval then yields

`boxed: int G_Z(nu)dnu <= 2 E_det^+/hbar`

for a general measurable accessible mark space.

Technical publication version should formulate the mark amplitudes as a measurable field in a direct-integral Hilbert space and treat zero-mass fibers by the convention `kappa int f^2=0`.

Thus arbitrary mark resolution also cannot evade the area law.

---

## 6. Quantum regularization of the Paper-2 Type-II plateau

Paper 2's ideal deterministic Type-II model takes mathematically exact incident point events as primitive. At the classical paralysis maximum it has

`G_TypeII(0)=0`,

`G_TypeII(nu)>0` for every `nu!=0`,

and

`lim_|nu|->infinity G_TypeII(nu)=1/e`.

That nonzero asymptotic plateau implies infinite spectral area:

`int_R G_TypeII(nu)dnu = infinity`.

WP08 shows that such a plateau cannot be the literal infinite-frequency behavior of a factorized finite-energy physical detector whose latent event times first arise from a covariant quantum timing layer with finite `E_det^+`.

Indeed the primary quantum timing multiplier has finite area and, because its conditional timing density is an `L1` probability density,

`G_Z(nu) -> 0`

by the Riemann--Lebesgue lemma.

Since

`0<=G_Y(nu)<=G_Z(nu)` a.e.,

the final arbitrary-memory detector is forced into the same vanishing high-frequency envelope in the essential sense.

### Physical interpretation

The ideal classical `1/e` plateau can remain an excellent **intermediate-frequency asymptote** whenever the quantum timing scale is much faster than the dead-time scale. But at sufficiently high modulation frequency the finite-energy quantum localization layer must regularize it and drive the physically accessible Fisher transfer toward zero.

This is a concrete bridge between:

- Paper 2's classical arbitrary-memory Fisher spectrum; and
- the positive-energy quantum timing resource law of WP06/WP07.

It converts the grand-challenge theorem from a one-event statement into a broad **high-flux arbitrary-memory detector theorem**.

---

## 7. Example with the sharp Cauchy timing layer

For the sharp ideal covariant timing family

`f_a(t)=a/[pi(t^2+a^2)]`,

with constant efficiency `eta`,

`G_Z(nu)=eta exp(-2a|nu|)`.

For **any** downstream autonomous memory channel in the factorized class,

`boxed: G_Y(nu) <= eta exp(-2a|nu|)  a.e.`

and

`int G_Y <= eta/a`.

If the downstream memory is deterministic Type II, its ideal-classical tendency toward `1/e` cannot continue past the quantum envelope. The exact cascade need not equal a product of the two individual multipliers because the downstream channel is nonlinear/history dependent; the theorem requires only data-processing domination.

---

## 8. What WP08 does NOT prove

WP08 is not yet a theorem for every conceivable quantum detector with memory.

It does **not** cover a detector in which:

- coherent quantum memory interacts with later photons before any classical primary event is formed;
- the apparatus supplies an independent time reference/asymmetry resource that is not included in `E_det^+`;
- active feedback changes the quantum measurement itself based on earlier outcomes;
- event formation and dead-time dynamics are inseparable at the quantum level.

In such systems a source-only energy bound can fail because timing resource may be supplied by the apparatus or clock. A genuinely universal theorem would have to include the relevant apparatus time-asymmetry/energy resource in the bookkeeping.

Therefore the correct current claim is:

> **Finite positive energy bounds the temporal Fisher spectral area for a covariant primary timing measurement, and that bound is inherited unchanged by any subsequent autonomous classical detector memory.**

This is already substantially broader than the independent-event endpoint of WP07, but it is not the final arbitrary-quantum-memory theorem.

---

## 9. Prior-art position

The separate ingredients are classical/established:

- Poisson thinning/marking/displacement theorem;
- Fisher-information data processing / conditional-score projection;
- translation-invariant Fisher multipliers;
- covariant time POVM dilation;
- sharp positive-frequency Hardy inequality.

The candidate contribution is the synthesis into the end-to-end statement

`boxed: int G_final <= 2 E_det^+/hbar`

for a finite-energy covariant primary timing layer followed by arbitrary high-flux detector memory, together with the physical consequence that ideal nonzero infinite-frequency classical dead-time plateaus are quantum-regularized.

Targeted searches to date have not located this combined result. This is not priority certification.

---

## 10. Significance assessment

WP08 materially raises the ceiling of the positive-energy area law because it eliminates the most obvious objection that WP07 applies only to a memoryless timing detector.

It now covers a broad architecture class containing arbitrary **classical** detector memory after event formation, including the high-flux dead-time/saturation models central to Paper 2.

The strongest conceptual statement is:

`finite positive-energy temporal localization`

`+ arbitrary downstream autonomous memory`

`=> finite total temporal Fisher-transfer area`.

Equivalently, exact infinite-frequency information plateaus require an idealization with unbounded timing resource somewhere upstream.

This is potentially paper-level and more fundamental than Paper 2, but it remains inappropriate to call it Nobel-level unless the result can be broadened further and survives a much deeper priority/physics audit.

---

## 11. Next gates

1. **Deep prior-art audit** for the exact end-to-end area law and quantum regularization interpretation.
2. **Quantum-intertwined-memory counterexample search:** determine whether a source-only area law fails once event formation and detector memory are coherently inseparable.
3. If it fails, formulate the minimal additional apparatus time-asymmetry resource needed to restore a universal bound.
4. Derive quantitative crossover implications for an ideal Type-II memory stage preceded by a finite-energy timing kernel, without pretending the nonlinear cascade multiplier factorizes.
5. Decide whether WP06--WP08 have crossed the threshold for a standalone theorem paper or still need a genuinely quantum-memory extension.
