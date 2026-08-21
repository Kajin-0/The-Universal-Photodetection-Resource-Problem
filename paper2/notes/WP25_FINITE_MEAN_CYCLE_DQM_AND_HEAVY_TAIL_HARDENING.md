# WP25 — Finite-mean cycle DQM, Hellinger separation, and heavy-tail hardening of the Type-II recovery theorem

**Status:** major proof hardening of WP18. The one-cycle deterministic-recovery information-singularity theorem does not require finite recovery variance and does not need to assume finite interval Fisher information separately. Finite positive mean recovery is enough for the latent regenerative-cycle experiment to have finite Fisher information. A bounded Laplace statistic also yields a distribution-level local-separation theorem without DQM at all. The remaining separate regularity issue is the identification of the Palm-cycle information rate with the Fisher information rate of a **stationary fixed observation window**, especially under very heavy tails.

**Date:** 2026-08-21

---

## 1. Model and notation

Incident events form a homogeneous Poisson process of rate

`lambda>0`.

Each incident event independently receives a recovery mark `T` with arbitrary probability law on `[0,infinity)` and finite positive mean

`m=E[T] in (0,infinity)`.

The detector is dead whenever at least one event-generated recovery interval remains active. Registered events are starts of `M/G/infinity` busy clusters and form a renewal process.

Classical formulas:

`r(lambda)=lambda exp(-lambda m)`,

`E[D]=1/r(lambda)`,

where `D` is a Palm inter-registration interval.

The common count-rate maximum is

`lambda_*=1/m`,

`r_*=1/(em)`.

The classical registered-event renewal density is

`U_lambda(t)=lambda F(t)exp[-lambda A(t)]`,

with

`A(t)=E[min(T,t)]`,

and residual/stop-loss function

`R(t)=m-A(t)=E[(T-t)_+]`.

These queueing formulas are prior art.

---

# Part I — regularity-free local separation of the interval law

## 2. Exact bounded-Laplace sensitivity requires only finite mean

For `s>0`, define

`u_s(lambda)=int_0^infinity exp(-s t)U_lambda(t)dt`,

and the Palm interval Laplace transform

`phi_s(lambda)=E_lambda[exp(-sD)]`.

Renewal theory gives

`phi_s=u_s/(1+u_s)`.

Use the fractional source-rate perturbation

`lambda_epsilon=lambda(1+epsilon)`.

At `lambda_*=1/m`, dominated differentiation gives

`dot U_*(t)=U_*(t)R(t)/m`.

The domination is elementary and uses only finite mean:

- `0<=A(t)<=m`;
- locally in `lambda`, `U_lambda(t)<=C`;
- `|1-lambda A(t)|<=C`;
- `exp(-st)` is integrable.

Therefore

`dot u_s=W_s`,

where

`W_s=int_0^infinity exp(-st)U_*(t)R(t)/m dt`,

and

`boxed: dot phi_s = W_s/(1+u_s)^2`.

No interval density, finite `Var(T)`, finite `Var(D)`, DQM, or Fisher-information assumption enters this calculation.

---

## 3. Exact first-order singularity criterion for the Laplace family

If `T` is nondegenerate, choose `a<b` such that

`P(T<=a)>0`,

`P(T>b)>0`.

For every `t in [a,b]`:

`F(t)>0`,

`R(t)>0`.

Hence

`U_*(t)>0`

and the integrand defining `W_s` is strictly positive on a set of positive Lebesgue measure. Thus

`boxed: T nondegenerate => W_s>0 for every s>0`.

If `T=m` almost surely, then `F(t)=0` below `m` and `R(t)=0` at and above `m`, so

`W_s=0` for every `s>0`.

Consequently, with only `0<m<infinity`,

`boxed:`

`T=m a.s.`

`iff`

`d/d epsilon E_{lambda_*(1+epsilon)}[exp(-sD)]|_0 = 0`

for one/every `s>0`.

Equivalently, every genuinely random recovery law has a bounded observable of a **single registered interval** that responds linearly to source rate at the count-rate maximum, whereas deterministic recovery is first-order blind in the entire interval-Laplace family.

This is the broadest regularity-free statement currently justified.

---

## 4. Total-variation and Hellinger separation without DQM

Let `P_epsilon` be the law of one Palm interval `D` at rate `lambda_*(1+epsilon)`, and define

`Z_s=exp(-sD) in [0,1]`.

Set

`c_s=W_s/(1+u_s)^2`.

For nondegenerate recovery,

`c_s>0`

and

`E_epsilon[Z_s]-E_0[Z_s]=c_s epsilon+o(epsilon)`.

Using the variational characterization

`d_TV(P,Q)=sup_{0<=f<=1}|E_P f-E_Q f|`,

we obtain

`boxed:`

`d_TV(P_epsilon,P_0)>=c_s |epsilon|+o(|epsilon|)`.

Thus the interval experiment is **first-order statistically separated in total variation** for every nondegenerate finite-mean recovery law.

Use the Hellinger convention

`H^2(P,Q)=1-int sqrt(dP dQ)`.

The standard inequality

`d_TV(P,Q)<=sqrt(2) H(P,Q)`

gives

`boxed:`

`liminf_{epsilon->0} H^2(P_epsilon,P_0)/epsilon^2 >= c_s^2/2 >0`.

This remains meaningful if ordinary Fisher information is infinite or if a classical density-score representation is inconvenient.

Under ordinary DQM,

`H^2(P_epsilon,P_0)=I_D epsilon^2/8+o(epsilon^2)`,

so the regularity-free Hellinger bound implies

`I_D>=4c_s^2`,

consistent with the sharper bounded-statistic Cramer-Rao/projection inequality below.

---

# Part II — finite one-cycle Fisher information from the stopped latent Poisson cycle

## 5. Palm regenerative-cycle construction

Condition on a registered cluster start at time `0` (Palm initialization).

The recovery mark `T_0` of that event has the original law `F` and is independent of the future incident process because marks are iid and independent of the Poisson arrivals.

Let the future marked Poisson process be

`Pi=sum_i delta_(X_i,T_i)`

on `(0,infinity) x [0,infinity)` with intensity measure

`lambda dt F(dT)`.

Let `D` be the time of the next registered cluster start.

With respect to the filtration generated by `T_0` and the future marked Poisson process, `D` is a stopping time: at time `t`, whether the initial busy cluster has ended and whether the next cluster start has occurred is determined by incident events and their recovery marks observed up to `t`.

Classical renewal theory gives

`E_lambda[D]=1/r(lambda)=exp(lambda m)/lambda<infinity`.

No second moment is needed.

---

## 6. Stopped latent-cycle likelihood and score

Compare baseline rate `lambda` with

`lambda_epsilon=lambda(1+epsilon)`.

Recovery marks are parameter-independent. The likelihood-ratio process of the future marked Poisson input up to deterministic time `t` is

`L_epsilon(t)=(1+epsilon)^{N_t} exp(-lambda epsilon t)`.

Stopped at the next-cluster-start time `D`, the latent-cycle likelihood is

`boxed:`

`L_epsilon(D)=(1+epsilon)^{N_D} exp(-lambda epsilon D)`.

Its fractional-rate score is

`boxed: S_cyc=N_D-lambda D`.

Here `N_D` counts future incident events through the terminal arrival at `D`.

The compensated Poisson martingale

`M_t=N_t-lambda t`

has predictable quadratic variation `lambda t`. Localization at `D wedge K` and monotone convergence give the stopped martingale isometry

`boxed:`

`E[S_cyc^2]=lambda E[D]=lambda/r`.

Therefore the complete latent regenerative cycle has finite Fisher information whenever `m<infinity`.

This remains true when:

- `T` is discrete/atomic;
- `T` is singular continuous;
- `Var(T)=infinity`;
- the busy-cycle/registered-interval variance is infinite;
- the recovery density does not exist.

Only the finite cycle mean `E[D]` is used.

---

## 7. DQM of the stopped latent-cycle experiment by localization

For bounded stopping time

`D_K=D wedge K`,

the Poisson likelihood family stopped at `D_K` is the standard regular one-parameter counting-process experiment and is DQM with score

`S_K=N_{D_K}-lambda D_K`.

Moreover,

`E[(S_cyc-S_K)^2]=lambda E[D-D_K] ->0`

because `E[D]<infinity`.

The square-root likelihoods can be localized in the same way. Writing

`a_epsilon=sqrt(1+epsilon)-1=epsilon/2+O(epsilon^2)`,

the square-root likelihood satisfies a stochastic-integral representation whose first-order term is

`(epsilon/2)M_{D_K}`

and whose remainder is `o_L2(epsilon)` for each fixed `K`. The tail from replacing `D` by `D_K` is controlled by

`lambda E[D-D_K]`,

uniformly at first order for rates in a small neighborhood because

`E_{lambda'}[D]=exp(lambda' m)/lambda'`

is locally finite.

Hence the unbounded stopped-cycle experiment is DQM with score

`S_cyc=N_D-lambda D`

and Fisher information

`lambda/r`.

### Reference posture

This is standard stopped counting-process likelihood / martingale localization rather than a new statistical theorem. A manuscript should cite standard counting-process likelihood theory (e.g. Andersen–Borgan–Gill–Keiding / Jacobsen) rather than present the DQM machinery as novel.

---

## 8. The observed interval is a statistic: automatic finite `I_D`

The registered interval `D` is a measurable statistic of the latent stopped cycle.

DQM is preserved under parameter-independent statistics, with output score equal to the conditional expectation of the latent score. Therefore

`boxed:`

`a(D)=E[S_cyc|D]`

is the one-interval score and

`boxed:`

`I_D=E[a(D)^2] <= E[S_cyc^2]=lambda/r`.

Thus **finite interval Fisher information is automatic** for every arbitrary recovery law with finite positive mean.

This removes the separate WP18 assumption `I_D<infinity` at the Palm-cycle level.

Define the cycle-normalized retention

`boxed: G_cyc=(r/lambda)I_D`.

Then universally in the finite-mean iid-recovery Type-II class,

`boxed: 0<=G_cyc<=1`.

This is exactly the data-processing normalization expected relative to the source Poisson information accumulated over one mean cycle.

---

## 9. Deterministic recovery is the unique zero of cycle-normalized FI

At the count-rate maximum `lambda_*=1/m`, take

`Z_s=e^{-sD}`.

DQM gives the score identity

`dot phi_s=E[Z_s a(D)]`.

Because `E[a(D)]=0`, Cauchy-Schwarz yields

`dot phi_s^2 <= Var(Z_s) I_D`.

Therefore

`boxed:`

`I_D >= c_s^2/Var(e^{-sD})`,

where

`c_s=W_s/(1+u_s)^2`.

For nondegenerate recovery, `c_s>0`, hence

`I_D>0`

and

`G_cyc>0`.

For deterministic recovery, the entire Palm interval law depends on `lambda` only through

`r(lambda)=lambda exp(-lambda m)`,

whose fractional first derivative vanishes at `lambda m=1`. Thus the interval score is zero and

`I_D=0`.

Consequently the cycle theorem can be stated with only finite positive mean recovery:

`boxed:`

`G_cyc=0 at lambda m=1`

`iff`

`T=m almost surely`.

No finite variance, smooth recovery density, or separate finite-FI assumption is required.

Using `Var(Z_s)<=1/4`,

`G_cyc >= (4/e) W_s^2/(1+u_s)^4`

at the common maximum, exactly matching the WP14/WP18 simple witness.

---

# Part III — what remains delicate: stationary fixed-window FI rate

## 10. Cycle information versus window information

The Palm cycle theorem above is now very broad.

However, WP18 previously defined the static detector retention as the stationary long-window limit

`G_DC=lim_{L->infinity} F_out^[0,L]/(lambda L)`.

Identifying this with

`(r/lambda)I_D=G_cyc`

is a **separate renewal-window theorem**.

For regular parametric renewal families, window-censored renewal likelihood theory gives exactly this bulk behavior: complete inter-renewal intervals contribute asymptotically at rate `r`, while initial/final censoring terms are lower order. Zhao & Nagaraja (2011), *Fisher information in window censored renewal process data and its applications*, derive exact and asymptotic FI for random-origin/window-censored renewal observations.

But their standard setting and many classical renewal-likelihood arguments impose regularity conditions that should not silently be extended to every singular/atomic/heavy-tailed interval family.

Therefore distinguish two quantities:

1. **Palm-cycle retention**
   
   `G_cyc=(r/lambda)I_D`,
   
   now established for all finite-mean recovery laws;
2. **stationary fixed-window retention**
   
   `G_DC`,
   
   identified with `G_cyc` only when renewal-window boundary/censoring Fisher terms are `o(L)` and the asymptotic FI-rate theorem applies.

This is the cleanest way to avoid hiding a heavy-tail boundary assumption inside the core singularity theorem.

---

## 11. Why heavy tails specifically affect the window issue, not the cycle theorem

Finite `m=E[T]` guarantees

`E[D]=1/r<infinity`.

It does **not** guarantee:

- `Var(T)<infinity`;
- `Var(D)<infinity`;
- finite mean forward-recurrence time;
- rapid mixing of the stationary detector state;
- small Fisher information in the random-origin boundary state under every parametrization.

For a stationary renewal observation window, the left boundary samples a size-biased/forward-recurrence structure. If `E[D^2]=infinity`, ordinary boundary-moment arguments can fail even though the number of complete cycles still grows linearly.

Thus the safe manuscript theorem should not claim, without proof, that finite `E[T]` alone implies

`F_window(L)=rI_D L+o(L)`.

This boundary issue is orthogonal to the one-cycle deterministic-recovery uniqueness result.

---

## 12. Recommended theorem hierarchy after WP25

### Theorem 1 — regularity-free interval sensitivity

For every iid recovery law with `0<E[T]<infinity`, at `lambda=1/E[T]`:

`T` is nondegenerate iff, for every `s>0`,

`d/d epsilon E[exp(-sD)]|_0 >0`.

For nondegenerate `T`, the interval laws obey linear total-variation separation and positive Hellinger curvature lower bound.

### Theorem 2 — universal finite-mean Palm-cycle Fisher theorem

For every iid recovery law with `0<E[T]<infinity`, the Palm interval experiment is DQM in fractional incident rate and

`0<=I_D<=lambda/r`.

Define

`G_cyc=(r/lambda)I_D`.

At the common count-rate maximum:

`boxed: G_cyc=0 iff T=E[T] a.s.`

and every nondegenerate law has the explicit positive Laplace-statistic witness.

### Corollary 3 — stationary fixed-window FI rate

Under standard window-censored renewal regularity sufficient for

`F_window(L)=rI_D L+o(L)`,

`G_DC=G_cyc`.

Then the same zero-iff-deterministic result holds for the stationary per-time detector FI.

This three-level statement is stronger and more honest than WP18's earlier single regularity-qualified theorem.

---

## 13. Novelty posture

The following are standard and must be credited:

- stopped Poisson/counting-process likelihood ratios;
- compensated-counting-process martingales;
- optional stopping/isometry;
- DQM localization;
- DQM under statistics / score projection;
- renewal Palm intervals;
- asymptotic Fisher information in window-censored renewal processes;
- total variation and Hellinger inequalities.

The candidate contribution is their use to remove unnecessary smoothness/moment restrictions from the **specific generalized Type-II recovery information-singularity theorem**.

No priority claim is certified.

---

## 14. Decision impact

WP25 materially strengthens WP18:

- `Var(T)<infinity` is unnecessary;
- atomic and singular recovery laws are included;
- heavy-tailed recovery with finite mean is included at the Palm-cycle level;
- finite `I_D` need not be separately assumed;
- a regularity-free bounded-statistic / TV / Hellinger separation theorem survives even if one does not want to invoke DQM;
- the only remaining significant technical qualification is the **stationary fixed-window FI-rate equivalence** under pathological heavy-tail/boundary behavior.

This makes the deterministic-recovery singularity result substantially more robust and suitable as a central Paper-2 theorem candidate.

## 15. Next gate

The next highest-value task is to determine whether the fixed-window equality

`G_DC=G_cyc`

can be proved under merely finite mean `D`, or whether a mild extra condition such as finite second moment / finite boundary Fisher information is genuinely necessary.

Do not force a universal statement. If the clean theorem naturally needs one additional renewal-window hypothesis, state it and keep the universal Palm-cycle theorem as the core result.
