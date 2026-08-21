# Paper 2 Research Log — Round 04 checkpoint (WP21–WP26)

**Date:** 2026-08-21

**Purpose:** durable recovery checkpoint after the historical-identifiability audit, conditional-score residue hardening, prior-art demotion, heavy-tail proof repair, and final closure of the stationary fixed-window Fisher-rate gate.

The repository, not chat history, is authoritative.

---

## 1. Executive state

The active Paper-2 core is now:

1. `WP10/WP17` — general autonomous-channel local Fisher-spectrum synthesis;
2. `WP07` — deterministic continuous Type-II static blindness with nonzero-frequency information survival;
3. `WP25/WP26` — finite-mean class-wide random-recovery singularity theorem, now valid both per Palm cycle and per stationary long window;
4. `WP19` — exact resource no-go: recovery mean + variance/CV + conventional saturation curve are insufficient;
5. `WP22/WP23` — conditional-score atomic timing-path bridge theory, retained but novelty-downgraded by `WP24`.

The major mathematical regularity gate around heavy-tailed recovery is now **closed**.

The next action is not another example or another generalization. It is one integrated hostile proof/novelty review deciding whether this stack has earned a manuscript.

---

## 2. WP21 — inverse-output historical audit

Generic queue-output identifiability is old prior art.

Key conclusions:

- output-flow reconstruction/identifiability was an explicit queueing topic by at least 1965;
- Kovalenko (1965), Kendall–Lewis (1965), Ivnitskii (1969/1977), Brown (1970), Ross (1970), George–Agrawal (1973), Shanbhag (1973), and others occupy the surrounding territory;
- by 1982, output-flow reconstruction was textbook material;
- Afanaseva & Mikhailova (1973) remains an inaccessible direct Type-II-lineage blocker.

Therefore:

- do **not** claim generic output identifiability as new;
- do **not** claim hidden-recovery/service reconstruction as new;
- do **not** claim the broad existence of exceptional information-degenerate service laws as new.

The defensible candidate is much narrower:

`deterministic recovery = unique zero-static-Fisher boundary at the universal Type-II count maximum`.

---

## 3. WP22/WP23 — covariance atoms and exact delayed score paths

WP22 repaired the old visible-event residue theorem.

The robust abstract object is the zero-lag atom of the **conditional-source-score covariance**, not output rate by itself:

`Gamma_M=a delta_0+nu`

implies, under finite-TV nonzero-lag correction,

`high-frequency Cesaro Fisher residue = a/lambda`.

WP23 then found an adversarial counterexample to the simpler physical interpretation:

- causality alone does not imply `a=r`;
- an exact delayed score path `c u(t-tau)` adds atomic timing energy;
- high-frequency averaged retention therefore measures total **atomic timing-path energy** in the conditional score.

Immediate visible timestamps are one atomic path; perfectly sharp delayed memory paths can add others.

---

## 4. WP24 — atomic-residue novelty audit

The mathematics behind WP22/WP23 is heavily classical:

- score covariance / Bartlett identities;
- counting-process innovation-martingale likelihoods;
- point-process Fisher kernels;
- Bartlett spectra and high-frequency shot-noise plateaus;
- Fourier-Stieltjes atom extraction, Wiener and Rajchman theory;
- frequency-domain Fisher information in system identification;
- neural/spike-train frequency-resolved information.

No exact predecessor was located for the full UPRP **conditional incident-source score after arbitrary detector processing** construction.

Nevertheless, because the ingredients are standard, WP22/WP23 are now positioned as **bridge/structural theory**, not a standalone novelty pillar.

---

## 5. WP25 — finite-mean Palm-cycle theorem

This was the main heavy-tail proof breakthrough.

For arbitrary iid recovery law with

`0<m=E[T]<infinity`,

at the common count maximum `lambda_*=1/m`, the bounded statistic

`Z_s=exp(-sD)`

has exact derivative

`dot phi_s=W_s/(1+u_s)^2`.

For every nondegenerate recovery law,

`W_s>0` for every `s>0`.

Thus nondegenerate recovery is first-order statistically separated from the deterministic singular case in total variation/Hellinger **without requiring DQM, a density, finite variance, or finite Fisher information**.

### Stopped latent cycle

Palm-initialize at a registered cluster start and stop at the next registered event.

The future marked-Poisson cycle has score

`S_cyc=N_D-lambda D`

and exact FI

`E[S_cyc^2]=lambda E[D]=lambda/r`.

Localization at `D wedge K` uses only `E[D]<infinity`, so the stopped cycle is DQM.

The observed interval is a statistic, hence

`I_D<=lambda/r`.

Define

`G_cyc=(r/lambda)I_D`.

Then for every finite-mean recovery law:

`0<=G_cyc<=1`,

and at `lambda*m=1`,

`G_cyc=0 iff T=m a.s.`.

This covers atomic, singular, infinite-variance, and heavy-tailed recovery laws.

---

## 6. WP26 — stationary fixed-window gate closed

WP25 left open whether the stationary random-origin window FI rate equals the Palm-cycle rate under only finite mean.

Zhao & Nagaraja (2011) prove for generic continuous renewal families that

`I_window(L)/L -> I_D/E[D]`

under regularity conditions including finite Fisher information in the forward recurrence time. Therefore their theorem alone cannot justify the arbitrary finite-mean heavy-tail case.

WP26 closes the gap using Type-II-specific latent structure.

### 6.1 Ordinary renewal started at a renewal

For a DQM interval law with finite `I_D`, progressively right-censor one next interval at horizon `t`.

Its censored FI `J(t)` is

`J(t)=Var(E[a(D)|C_t(D)])`,

so

`J(t) increases to I_D`.

Sequentially generating intervals until the deterministic horizon gives

`I_ord(t)=E[sum stages J(remaining horizon)]`.

Using `J(t)<=I_D`, `J(t)->I_D`, and the elementary renewal theorem:

`boxed: I_ord(t)/t -> I_D/E[D]=rI_D`.

Only finite `E[D]` and finite `I_D` are needed.

### 6.2 Stationary Type-II left boundary

At time zero, the only old incident events relevant to future detector state are recoveries still active at zero.

Their marked-Poisson region has total intensity

`lambda E[T]=lambda m`.

Thus the entire stationary boundary state is a **finite Poisson cloud** with fractional-rate FI `lambda m`.

Let `Y` be the forward recurrence to the first registered event and `tau_L=min(Y,L)`.

Future input up to `tau_L` contributes latent stopped-Poisson FI

`lambda E[tau_L]`.

Therefore the censored first-event observation satisfies

`I(C_L(Y)) <= lambda m + lambda E[min(Y,L)]`.

Since `Y<infinity` a.s.,

`E[min(Y,L)]/L ->0`

by bounded convergence of `min(Y,L)/L`.

Hence

`I(C_L(Y))/L ->0`

even if `E[Y]=infinity`.

### 6.3 Chain rule

Conditional on a first registered event at `Y=y<L`, the remainder is a fresh ordinary renewal experiment of duration `L-y`.

Thus

`I_stat(L)=I(C_L(Y))+E[1{Y<L}I_ord(L-Y)]`.

The first term is `o(L)`. The second has limit `rI_D L` because `I_ord(t)/t->rI_D`, while the probability of `Y` occupying a fixed fraction of an expanding window vanishes.

Therefore

`boxed: lim I_stat(L)/L = rI_D`.

Equivalently:

`boxed: G_DC=G_cyc=(r/lambda)I_D`.

### 6.4 Final class-wide theorem

At `lambda*m=1`, with only

`0<E[T]<infinity`,

`boxed: G_DC=0 iff T=E[T] a.s.`.

No density, finite variance, finite forward-recurrence mean, or separate FRT-FI assumption remains.

---

## 7. Exact resource no-go retained — WP19

Two explicit recovery laws have identical

`E[T]=1`, `Var(T)=1/4`, `CV=0.5`,

and identical conventional curve

`r(lambda)=lambda exp(-lambda)`,

but different registered timestamp experiments.

A common coarse-graining has zero FI for one and normalized FI about

`0.00443520488427`

for the other at `lambda=1`.

Full static values differ by about `8.78%`.

Therefore mean + variance/CV + the complete conventional mean saturation curve are not resource-complete descriptors.

---

## 8. Current safest novelty hierarchy

### Organizing theorem

1. `WP10/WP17` — arbitrary-autonomous-channel local Fisher spectrum as a photodetection-channel synthesis.

### Strong physical novelty candidates

2. `WP07` — deterministic continuous Type-II static blindness with positive information at every nonzero temporal frequency and high-frequency residue `1/e`.
3. `WP25/WP26` — arbitrary finite-mean random recovery: deterministic recovery is the unique zero of complete stationary static Fisher retention at the universal Type-II count maximum.

### Strong resource no-go

4. `WP19` — even recovery mean + variance/CV + complete mean saturation curve do not determine the information channel.

### Structural bridge only

5. `WP22/WP23` — atomic conditional-score timing paths and high-frequency Cesaro residue.

---

## 9. Mandatory claim boundaries

Do not claim novelty for:

- generic Fisher data processing / conditional scores;
- function-valued Fisher operators;
- translation-invariant Fourier multipliers;
- renewal-process FI in general;
- window-censored renewal FI in general;
- random Type-II / `M/G/infinity` modeling;
- busy-cycle renewal formulas;
- generic queue-output identifiability;
- random-paralyzable pair-correlation identities;
- Bartlett spectra / point-process shot-noise plateaus;
- Wiener/Rajchman atom theory;
- dead-time information theory generally;
- modulated paralyzable photocounting generally.

No priority claim is certified for the candidate UPRP-specific synthesis/results.

---

## 10. Next gate

The heavy-tail/fixed-window proof program is complete unless a concrete flaw is discovered.

**Next action:** one integrated hostile review of the complete candidate manuscript stack:

1. theorem correctness and hidden assumptions;
2. internal consistency between WP10 spectral notation and WP25/WP26 static-rate notation;
3. novelty collision search focused on WP07 and the exact WP25/WP26 zero-IFF-deterministic theorem;
4. significance: whether WP19 plus WP07 plus WP25/WP26 form one coherent resource-theory story rather than disconnected dead-time facts;
5. manuscript threshold decision.

Do not begin manuscript drafting before that integrated review is completed.
