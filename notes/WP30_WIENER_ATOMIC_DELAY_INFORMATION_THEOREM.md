# WP30 — Wiener Atomic-Delay Information Theorem

**Date:** 2026-08-20

## Purpose

Adversarially test whether the WP25 finite conditional-hazard resource is truly the weakest condition needed for a finite average information bandwidth.

It is not.

A finite hazard (or finite collision-intensity resource `R2`) gives a strong quantitative `1/Omega` ceiling, but a much weaker and more structural statement follows from classical harmonic analysis:

> The asymptotic flat-band source-information retention of an autonomous proper event detector is determined by the **atomic part of its conditional registration-delay distribution**.

Purely non-atomic timing noise forces the average retained information to vanish at arbitrarily high modulation bandwidth even if the delay density is not bounded and not square-integrable.

The underlying Fourier theorem is classical Wiener theory; the photodetection interpretation is the project-specific contribution.

---

# 1. Unmarked event detector

Let `mu_D` be the probability measure of the post-capture primary electrical registration delay `D>=0`. It need not possess a density.

Define its characteristic function

\[
H_D(\omega)=\int e^{-i\omega t}\,d\mu_D(t).
\]

For a weak coherent/Poisson modulation and no parameter-dependent downstream processing, the source-normalized signal-event Fisher-information transfer is

\[
\eta_I(\omega)=\eta_c |H_D(\omega)|^2
\]

in the no-background upper-envelope case. Any independent background or downstream coarse graining only reduces FI.

For a flat two-sided source-information band,

\[
\bar\eta_I(\Omega)
=\frac{\eta_c}{2\Omega}
\int_{-\Omega}^{\Omega}|H_D(\omega)|^2d\omega.
\]

---

# 2. Wiener theorem

Decompose the delay measure into its atomic and non-atomic parts. Let the point masses be

\[
p_j=\mu_D(\{t_j\}).
\]

Wiener's theorem for the Fourier transform of a finite measure gives

\[
\boxed{
\lim_{\Omega\to\infty}
\frac{1}{2\Omega}
\int_{-\Omega}^{\Omega}|H_D(\omega)|^2d\omega
=
\sum_j p_j^2.
}
\]

Therefore

\[
\boxed{
\lim_{\Omega\to\infty}\bar\eta_I(\Omega)
=
\eta_c\sum_jp_j^2.
}
\]

With capture ceiling `eta_c<=C`,

\[
\boxed{
\limsup_{\Omega\to\infty}\bar\eta_I(\Omega)
\le
C\sum_jp_j^2.
}
\]

---

# 3. Purely non-atomic timing implies vanishing average information

If the conditional delay law has no atoms,

\[
p_j=0\quad\forall j,
\]

then

\[
\boxed{
\lim_{\Omega\to\infty}\bar\eta_I(\Omega)=0.
}
\]

This requires neither:

- a bounded hazard;
- a bounded delay density;
- finite `R2=2 int f^2`;
- finite mean delay;
- finite variance/RMS jitter.

Thus **non-atomicity alone** is sufficient for qualitative high-bandwidth information loss in the flat-band average sense.

However, Wiener theory supplies no universal decay rate. The approach to zero can be arbitrarily slow.

---

# 4. Atoms are the exact asymptotic obstruction

If a fraction `p` of detections occurs at an exactly deterministic delay `tau_0`, with the remainder non-atomic,

\[
\mu_D=p\delta_{\tau_0}+(1-p)\mu_c,
\]

then

\[
\boxed{
\lim_{\Omega\to\infty}\bar\eta_I(\Omega)
=\eta_c p^2.
}
\]

More generally, for finitely or countably many deterministic-delay branches,

\[
\boxed{
\bar\eta_I(\infty)=
\eta_c\sum_jp_j^2.
}
\]

Hence exact prompt/feedthrough branches leave a nonzero high-bandwidth information residue even when all continuous timing components are arbitrarily slow or noisy.

This gives a precise interpretation of the direct-feedthrough loophole that appeared repeatedly in earlier work packages.

---

# 5. Why conventional jitter resources fail

WP26 constructed smooth prompt-plus-tail families with fixed finite RMS variance but increasingly narrow prompt mass. The Wiener theorem explains the limiting structure.

If the prompt component becomes an actual atom of mass `p`, the asymptotic retained fraction tends to `p^2` when the branch identity is unresolved. If the prompt peak only becomes increasingly narrow but remains continuous, the ultimate `Omega->infinity` limit remains zero, but the crossover bandwidth can diverge without any bound from the first two timing moments.

Thus:

\[
\boxed{
\text{finite mean/RMS/FWHM jitter}
\not\Rightarrow
\text{a quantitative information-bandwidth ceiling}.
}
\]

The first moments do not control either the atomic content or the concentration scale of the non-atomic part.

---

# 6. Mark-resolved theorem

Let `M` be the complete accessible autonomous event mark. Conditional on `M=m`, let the delay probability measure be `mu_m` with characteristic function

\[
H_m(\omega)=\int e^{-i\omega t}\,d\mu_m(t).
\]

For a signal event channel whose mark distribution is parameter-independent apart from the arrival-time translation, the marked-record FI transfer is

\[
\boxed{
\eta_I(\omega)
=
\eta_c\,\mathbb E_M[|H_M(\omega)|^2]
}
\]

in the ideal no-background upper-envelope case.

For each mark, let

\[
a(m)=\sum_j p_j(m)^2
\]

be the squared atomic mass of the conditional delay measure.

By Wiener theorem for each conditional measure and dominated convergence (`|H_M|^2<=1`),

\[
\boxed{
\lim_{\Omega\to\infty}
\bar\eta_I(\Omega)
=
\eta_c\,\mathbb E_M[a(M)].
}
\]

Therefore with `eta_c<=C`,

\[
\boxed{
\limsup_{\Omega\to\infty}
\bar\eta_I(\Omega)
\le
C\,\mathbb E_M[a(M)].
}
\]

This is the correct mark-robust atomic obstruction.

---

# 7. Accessible marks can restore atomic timing

Suppose an unresolved detector has two deterministic delay branches

\[
D\in\{\tau_1,\tau_2\}
\]

with probabilities `p` and `1-p`.

Without branch identity in the record,

\[
\bar\eta_I(\infty)
=\eta_c[p^2+(1-p)^2].
\]

If the electrical mark `M` reveals which branch occurred, then each conditional delay law is deterministic:

\[
a(M)=1.
\]

Hence

\[
\boxed{
\bar\eta_I(\infty)=\eta_c.
}
\]

This reproduces the earlier result that capture-position or path side information can remove deterministic transit dispersion.

The theorem therefore must always be formulated **after conditioning on every accessible event mark**.

---

# 8. Relation to WP25 hazard theorem

A finite conditional hazard ceiling

\[
h(t\mid M)\le\Lambda<\infty
\]

implies that each conditional delay law is absolutely continuous and therefore non-atomic.

More strongly, WP25 proves

\[
2\int f(t\mid M)^2dt\le\Lambda
\]

and hence the quantitative flat-band bound

\[
\boxed{
\bar\eta_I(\Omega)
\le
C\min\left[1,\frac{\pi\Lambda}{2\Omega}\right].
}
\]

Thus the hierarchy is

\[
\boxed{
\text{finite conditional hazard}
\Rightarrow
\text{finite }R_2
\Rightarrow
\text{non-atomic conditional delay}
\Rightarrow
\bar\eta_I(\Omega)\to0.
}
\]

The converses are false in general.

Interpretation:

- **non-atomicity** is the weakest structural condition currently identified for qualitative asymptotic information loss;
- **finite `R2`** gives an integrated spectral budget;
- **finite local hazard `Lambda`** gives a microscopic, physically interpretable sufficient resource and the explicit `1/Omega` coefficient.

---

# 9. Relation to WP29 thermodynamic bridge

WP29's Markov gateway contains an independent exponential first-exit stage

\[
T_1\sim\mathrm{Exp}(\lambda_1).
\]

Convolution with this continuous distribution removes atomic timing even if all downstream delays are deterministic. Thus WP3 already guarantees qualitative asymptotic decay once the proper-gateway/no-bypass assumption is imposed.

The EPR/activity/throughput plus absolute-rate argument further gives

\[
\lambda_1\le\Lambda_*,
\]

which upgrades qualitative Wiener decay to the quantitative WP25/WP29 bound.

So the old thermodynamic theorem now has a clean two-level interpretation:

1. the gateway enforces a non-atomic timing stage;
2. thermokinetic resources plus an absolute microscopic rate bound control how concentrated that stage can be.

---

# 10. Free-clock caveat

WP27 remains outside this theorem. A synchronous detector with an unbounded external clock may encode arrival phase into a mark before slow registration. Such a mark is not generated by a time-translation-invariant delay channel `mu_m(t-t_arrival)` and therefore violates the autonomous marked-event assumption.

A clocked detector requires clock/control bandwidth and phase memory to be counted as explicit resources.

---

# 11. Minimality conclusion

For the autonomous proper-event branch, the project should distinguish three questions.

### Does information necessarily vanish at arbitrarily high flat-bandwidth?

Sufficient and essentially structural answer:

\[
\boxed{\text{all mark-conditioned delay laws are non-atomic}.}
\]

### Can one bound the total available timing spectrum?

Sufficient answer:

\[
\boxed{R_2=2\mathbb E_M\int f(t\mid M)^2dt<\infty.}
\]

### Can one express that timing resource in microscopic detector dynamics?

Sufficient answer:

\[
\boxed{\operatorname*{ess\,sup}_{M,t}h(t\mid M)\le\Lambda<\infty.}
\]

WP25/WP29 then map `Lambda` to local Markov or quantum-jump rate/operator norms and, in restricted thermodynamic classes, to EPR/activity/throughput plus an absolute microscopic coupling scale.

This is a more precise resource hierarchy than calling `Lambda` the mathematically minimal timing resource.

---

# 12. Status

**PROVED/APPLIED:** Wiener asymptotic theorem to unmarked and mark-resolved proper-event photodetection records.

**PROVED CORRECTION:** finite hazard/R2 is sufficient for a quantitative rate but is not the weakest condition for qualitative finite information bandwidth.

**OPEN:** rate bounds under weaker regularity classes than `L2`; extension to non-Poisson/nonclassical incident statistics; theorem-level novelty audit for the photodetection interpretation.