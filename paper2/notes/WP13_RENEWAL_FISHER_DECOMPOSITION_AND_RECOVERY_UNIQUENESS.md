# WP13 — Renewal Fisher Decomposition and the Uniqueness of Deterministic Type-II Recovery

**Status:** exact class-wide theorem derived. This upgrades WP12 from a deterministic-vs-exponential counterexample to a general identifiability result for iid Type-II recovery laws. The renewal-Fisher decomposition itself has substantial prior art in renewal/statistical/neural inference and is used here as a proof tool, not a priority claim.

## 1. Generalized Type-II model

Incident events form a homogeneous Poisson process of rate `lambda`.

Each incident event at time `S_i` starts an iid recovery/dead interval

\[
[S_i,S_i+T_i),
\]

where `T_i` has fixed distribution function `F`, survival `\bar F=1-F`, and finite positive mean

\[
\boxed{m=E[T]=\int_0^\infty \bar F(u)du.}
\]

The detector is dead whenever at least one event-generated interval is active. An incident event is recorded iff it arrives when no interval is active. Recorded events are therefore the starts of connected Poisson-Boolean / `M/G/infinity` busy clusters.

By regeneration at empty epochs, the recorded event process is a stationary renewal process.

As in WP12, the stationary recorded-event rate is universal over all recovery distributions with the same mean:

\[
\boxed{r(\lambda)=\lambda e^{-\lambda m}.}
\]

Thus all equal-mean recovery laws have the same conventional paralysis curve and the same maximum at `lambda*m=1`.

---

## 2. Exact renewal density of recorded timestamps

Condition on a recorded event at time `0`. Let

\[
U_\lambda(t)
\]

be the renewal density: `U_lambda(t) dt` is the conditional probability, to first order in `dt`, of a recorded event in `(t,t+dt)` given a recorded event at `0`, allowing any number of intervening recorded events.

An incident Poisson arrival at time `t>0` is recorded iff the recovery interval started by the event at `0` has ended and no later incident event still has an active interval at `t`.

The first condition has probability

\[
F(t).
\]

For incident events in `(0,t)`, Poisson marking/thinning shows that the number whose intervals cover `t` is Poisson with mean

\[
\lambda A(t),
\qquad
A(t)=\int_0^t\bar F(u)du
=E[\min(T,t)].
\]

Hence the probability that no such interval is active is `exp[-lambda A(t)]`.

Multiplying by the incident arrival rate at `t` gives the exact formula

\[
\boxed{
U_\lambda(t)
=\lambda F(t)e^{-\lambda A(t)},
\qquad t>0.
}
\]

This formula is classical `M/G/infinity` / Poisson-Boolean structure; its use below for Fisher identifiability is the new target.

### Consistency check: deterministic recovery

If `T=m` a.s., then

\[
F(t)=\mathbf1_{t\ge m},
\qquad
A(t)=\min(t,m),
\]

so

\[
\boxed{
U_\lambda(t)=r(\lambda)\mathbf1_{t\ge m}.}
\]

Its Laplace transform is `r exp(-sm)/s`, and the ordinary renewal identity

\[
\widetilde U=\frac{\widetilde f_D}{1-\widetilde f_D}
\]

yields

\[
\widetilde f_D(s)
=\frac{r e^{-sm}}{s+r e^{-sm}},
\]

exactly recovering WP07.

### Complete interval law from `U`

For any renewal process,

\[
U=f_D+f_D*f_D+f_D*f_D*f_D+\cdots.
\]

Thus wherever Laplace transforms exist,

\[
\boxed{
\widetilde f_D(s)
=\frac{\widetilde U(s)}{1+\widetilde U(s)}.
}
\]

Therefore the renewal density `U_lambda` and the complete inter-recording law determine each other uniquely. Equality or first-order equality of `U` is equivalent to equality or first-order equality of the complete stationary renewal experiment, apart from negligible observation-window boundary terms.

---

## 3. Complete timestamp Fisher information of a renewal process

Let a scalar local parameter `epsilon` perturb the renewal interval density `f_epsilon(d)` smoothly. At the baseline define the one-interval score

\[
\boxed{
s_D(d)=\left.\partial_\epsilon\log f_\epsilon(d)\right|_{\epsilon=0},}
\]

with

\[
E[s_D(D)]=0,
\qquad
I_D=E[s_D(D)^2].
\]

Let

\[
\mu=E[D]=1/r.
\]

Over a long observation window of duration `L`, there are `L/mu+o_p(L)` complete renewal intervals. Standard renewal-likelihood theory shows that the boundary-censoring terms contribute only `o(L)` Fisher information under the usual regularity conditions. Hence

\[
\boxed{
\lim_{L\to\infty}\frac{F_{\rm out}^{[0,L]}}{L}
=\frac{I_D}{\mu}
=r I_D.
}
\]

For the fractional incident-rate tangent

\[
\lambda_\epsilon=\lambda(1+\epsilon),
\]

the incident Poisson FI rate is `lambda`. Therefore the normalized static Fisher retention is

\[
\boxed{
G(0)=\frac{r}{\lambda}I_D.
}
\]

This exact renewal reduction is standard in statistical inference for renewal processes; see e.g. Basawa (1974) and Zhao & Nagaraja (2011). It is not claimed as novel.

---

## 4. Exact count-rate versus interval-shape decomposition

Let

\[
\dot\mu
=\left.\partial_\epsilon E_\epsilon[D]\right|_0.
\]

By the score identity,

\[
\boxed{\dot\mu=E[(D-\mu)s_D(D)].}
\]

Let

\[
\sigma_D^2=\operatorname{Var}(D).
\]

Project the interval score orthogonally onto the one-dimensional subspace spanned by `D-mu`:

\[
\boxed{
s_D(D)
=\frac{\dot\mu}{\sigma_D^2}(D-\mu)
+s_{\rm shape}(D),}
\]

where

\[
E[s_{\rm shape}]=0,
\qquad
E[(D-\mu)s_{\rm shape}]=0.
\]

Pythagoras gives

\[
\boxed{
I_D
=\frac{\dot\mu^2}{\sigma_D^2}
+I_{\rm shape},
\qquad
I_{\rm shape}=E[s_{\rm shape}^2]\ge0.
}
\]

Thus

\[
\boxed{
G(0)=G_{\rm rate}+G_{\rm shape},}
\]

with

\[
\boxed{
G_{\rm rate}
=\frac r\lambda\frac{\dot\mu^2}{\sigma_D^2},
\qquad
G_{\rm shape}
=\frac r\lambda I_{\rm shape}.}
\]

For the fractional rate parameter,

\[
\dot\mu
=\lambda\frac{d}{d\lambda}\frac1r
=-\frac{\lambda r'}{r^2},
\]

so

\[
\boxed{
G_{\rm rate}
=\frac{\lambda [r'(\lambda)]^2}
{r^3\sigma_D^2}.}
\]

This is precisely the asymptotic Fisher information obtainable from the total renewal count alone: renewal CLT gives

\[
\operatorname{Var}N_L
\sim r^3\sigma_D^2 L,
\]

while the fractional perturbation changes its mean at rate `lambda r'`.

Hence `G_shape` measures the additional static information carried by the detailed inter-recording intervals after the best count/rate statistic has been removed.

### Prior-art boundary

The distinction between firing-rate information and exact spike-timing / interval information is old in neural coding. Toyoizumi, Aihara & Amari, PRL 97, 098102 (2006), DOI `10.1103/PhysRevLett.97.098102`, explicitly compare spike-based and rate-based Fisher information for refractory neurons. Koyama & Kostal, MBE 11, 63--80 (2014), DOI `10.3934/mbe.2014.11.63`, study Fisher information of rate-modulated renewal spike trains and ISI shape.

Therefore the decomposition above is a structural lemma and interpretation tool, **not** a generic novelty claim.

---

## 5. At the universal paralysis maximum all rate information vanishes

For every recovery law of mean `m`,

\[
r(\lambda)=\lambda e^{-\lambda m}.
\]

At

\[
\boxed{\lambda m=1,}
\]

\[
r'(\lambda)=0,
\]

and therefore

\[
\boxed{G_{\rm rate}(0)=0.}
\]

Any complete-record static information that survives the conventional paralysis maximum must come entirely from interval-shape information:

\[
\boxed{
G(0)=G_{\rm shape}(0)
=\frac r\lambda I_{\rm shape}
\quad\text{when }\lambda m=1.}
\]

This turns the qualitative statement “timestamps contain more than counts” into an exact orthogonal decomposition.

---

## 6. Fractional-rate derivative of the complete renewal density

Under

\[
\lambda_\epsilon=\lambda(1+\epsilon),
\]

the recovery law `F` is held fixed. Differentiating

\[
U_\lambda(t)=\lambda F(t)e^{-\lambda A(t)}
\]

gives

\[
\boxed{
\dot U_\lambda(t)
=U_\lambda(t)[1-\lambda A(t)].}
\]

At the common paralysis maximum `lambda=1/m`,

\[
\boxed{
\dot U_*(t)
=U_*(t)\left[1-\frac{A(t)}m\right].}
\]

Since

\[
A(t)=E[\min(T,t)]\le m,
\]

the factor in brackets is nonnegative and is strictly positive exactly when

\[
P(T>t)>0.
\]

Thus random recovery leaves a directly observable first-order signature in the pair/renewal structure even when the mean count-rate derivative is zero.

---

## 7. Deterministic recovery is the unique law with complete DC Fisher blindness

We now obtain the class-wide theorem suggested by WP12.

### Theorem

Assume the generalized iid Type-II model above, finite mean `m`, and regularity sufficient for the stationary renewal experiment to be DQM in the fractional incident-rate parameter. At the universal paralysis maximum

\[
\lambda m=1,
\]

the complete registered-timestamp Fisher information vanishes,

\[
G(0)=0,
\]

**if and only if**

\[
\boxed{T=m\quad\text{almost surely}.}
\]

### Proof: sufficiency

If `T=m` a.s., WP07/WP11 show that the complete renewal law depends on `lambda` only through

\[
r=\lambda e^{-\lambda m}.
\]

At `lambda m=1`, `dr/dlambda=0`, so the complete output score vanishes and `G(0)=0`.

### Proof: necessity

If `G(0)=0`, then by the renewal FI formula

\[
I_D=0,
\]

so the inter-recording score vanishes almost surely. Hence the first-order derivative of the complete renewal density must vanish:

\[
\dot U_*(t)=0
\]

for almost every `t` with `U_*(t)>0`.

But

\[
\dot U_*(t)
=U_*(t)\left[1-\frac{A(t)}m\right].
\]

Thus for every relevant `t` with `F(t)>0`,

\[
A(t)=m.
\]

Now

\[
m-A(t)=E[(T-t)_+].
\]

Therefore `A(t)=m` implies `P(T>t)=0`.

Let

\[
a=\inf\{t:F(t)>0\}
\]

be the essential lower endpoint of the recovery distribution. Since `F(t)=0` for `t<a`, `T>=a` a.s. Taking any sequence `t_n downarrow a` with `F(t_n)>0`, the preceding argument gives `T<=t_n` a.s. for every `n`, hence `T<=a` a.s. Consequently

\[
T=a\quad\text{a.s.}
\]

and its mean forces `a=m`.

Therefore deterministic recovery is necessary.

### Corollary

For every genuinely nondegenerate iid recovery law with finite mean,

\[
\boxed{
G(0)>0
\quad\text{at }\lambda m=1,
}

under the stated DQM regularity, even though

\[
\boxed{r'(\lambda)=0.}
\]

Thus the complete timestamps resolve source-rate changes that the entire conventional mean paralysis curve is locally blind to.

---

## 8. Deterministic recovery is also unique for global Lambert-W branch aliasing

Take two distinct incident rates `lambda_1 != lambda_2` with the same conventional recorded rate:

\[
\lambda_1e^{-\lambda_1m}
=\lambda_2e^{-\lambda_2m}.
\]

For `0<rm<1/e` these are the two Lambert-W branches discussed in WP11.

Suppose the **complete stationary registered-timestamp laws** at `lambda_1` and `lambda_2` are identical. Their renewal densities must be identical:

\[
\lambda_1 F(t)e^{-\lambda_1A(t)}
=
\lambda_2 F(t)e^{-\lambda_2A(t)}.
\]

For every `t` with `F(t)>0`,

\[
\ln\frac{\lambda_1}{\lambda_2}
=(\lambda_1-\lambda_2)A(t).
\]

But equality of the mean rates gives

\[
\ln\frac{\lambda_1}{\lambda_2}
=(\lambda_1-\lambda_2)m.
\]

Therefore

\[
A(t)=m
\]

for every `t` with `F(t)>0`, which by the same support argument forces

\[
\boxed{T=m\quad\text{a.s.}}
\]

Conversely deterministic recovery indeed gives identical complete timestamp laws whenever the two rates have equal `r`.

Hence:

\[
\boxed{
\begin{array}{c}
\text{two distinct equal-mean-output rate branches}\
\text{produce identical complete timestamp experiments}
\end{array}
\iff
T\text{ is deterministic}.}
\]

This upgrades WP11's deterministic branch aliasing from an isolated curiosity to a uniqueness theorem inside the full iid-recovery Type-II class.

---

## 9. Exponential recovery as a transparent check

For

\[
T\sim\operatorname{Exp}(\mu),
\qquad m=1/\mu,
\]

\[
F(t)=1-e^{-\mu t},
\qquad
A(t)=\frac{1-e^{-\mu t}}\mu.
\]

Therefore

\[
\boxed{
U_\lambda(t)
=\lambda(1-e^{-\mu t})
\exp\!\left[-\frac\lambda\mu(1-e^{-\mu t})\right].}
\]

At the shared paralysis maximum `lambda=mu`,

\[
\boxed{
\dot U_*(t)=U_*(t)e^{-\mu t}>0
\quad\text{for every finite }t>0.}
\]

So the complete pair/renewal structure has first-order rate sensitivity everywhere away from the origin even though the mean recorded rate has zero slope. This independently confirms the short-cycle argument of WP12.

---

## 10. Significance

The strongest result is not that random dead time changes interval statistics; that is classical.

It is the exact information/identifiability statement:

\[
\boxed{
\text{all iid Type-II recovery laws with mean }m
\text{ share }r(\lambda)=\lambda e^{-\lambda m},
}
\]

but

\[
\boxed{
G(0)=0\text{ at }\lambda m=1
\iff
T=m\text{ a.s.}}
\]

and, globally,

\[
\boxed{
\text{complete Lambert-W branch aliasing}
\iff
T\text{ is deterministic}.}
\]

Thus deterministic recovery is an **information-singular extremal point** of a whole family of detectors that are indistinguishable by their mean saturation curves.

This is a plausible Paper-2-level theorem because it identifies a structural property of recovery dynamics that cannot be inferred from conventional detector characterization.

---

## 11. Hostile prior-art boundary

The following ingredients are old and must be cited, not claimed:

- Type-II counters with random impulse/recovery durations;
- `M/G/infinity` busy-period / busy-cycle theory;
- hidden service-distribution inference in `M/G/infinity` queues;
- renewal-process Fisher information and MLE asymptotics;
- neural spike-timing versus firing-rate Fisher information;
- the Cramer-Rao inequality `I_D >= dot(mu)^2/sigma_D^2`.

Relevant works found so far include:

- Dvurecenskij & Ososkov, *Aplikace matematiky* 29, 237--249 (1984), DOI `10.21136/AM.1984.104092`.
- Stadje, *J. Appl. Prob.* 22, 697--704 (1985), DOI `10.2307/3213872`.
- George & Agrawal, *Naval Research Logistics Quarterly* 20, 549--555 (1973), DOI `10.1002/nav.3800200314`, hidden `M/G/infinity` service-distribution estimation.
- Zhao & Nagaraja, *Ann. Inst. Stat. Math.* 63, 791--825 (2011), DOI `10.1007/s10463-009-0252-2`, Fisher information in window-censored renewal processes.
- Toyoizumi, Aihara & Amari, *Phys. Rev. Lett.* 97, 098102 (2006), DOI `10.1103/PhysRevLett.97.098102`.
- Koyama & Kostal, *Math. Biosci. Eng.* 11, 63--80 (2014), DOI `10.3934/mbe.2014.11.63`.

The targeted search has **not** yet located the deterministic-recovery uniqueness theorem above. No `first` claim is permitted.

---

## 12. Next gates

1. Search inverse `M/G/infinity` / Type-II literature specifically for conditions under which busy-cycle or cluster-start observations identify a degenerate service law.
2. Derive quantitative lower bounds on `G(0)` for nondegenerate recovery in terms of a recovery-shape functional, not merely strict positivity.
3. Ask whether deterministic recovery minimizes `G(0)` under fixed mean at the paralysis maximum (it is the unique zero, but no monotone variance law is implied).
4. Compute exact/numerical `G(0)` for exponential recovery from the interval transform to calibrate the scale of the effect.
5. Explore whether a similar uniqueness theorem holds at finite temporal frequency or for non-Poisson incident processes.
6. Integrate this theorem with WP10 and WP12 only after the novelty search survives another pass.
