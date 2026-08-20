# WP32 — General Marked-Poisson Event-Kernel Theorem

**Date:** 2026-08-20

## Purpose

Place WP25–WP30 on one rigorous measure-theoretic event-channel foundation. This removes unnecessary assumptions of a single capture efficiency plus a separately normalized mark distribution and automatically covers:

- unequal parallel primary channels;
- mark-dependent capture probabilities;
- arbitrary continuous/discrete mark spaces;
- arbitrary conditional registration-delay probability measures;
- parameter-independent background as a monotone FI penalty.

The theorem remains restricted to an **autonomous/time-translation-invariant one-primary-event channel** driven by weak coherent/Poisson optical flux.

---

# 1. Detector kernel

Let `M` be the accessible primary-event mark space.

For each incident signal photon, define a subprobability kernel on mark and nonnegative registration delay:

\[
\boxed{
K(dm,d\tau).
}
\]

Its total mass is the primary-event capture/registration probability

\[
\boxed{
\eta=K(\mathsf M\times[0,\infty))\le1.
}
\]

Disintegrate

\[
K(dm,d\tau)=\kappa(dm)\,\mu_m(d\tau),
\]

where

\[
\kappa(dm)=K(dm,[0,\infty))
\]

is a finite mark measure with total mass `eta`, and `mu_m` is a probability measure for `kappa`-almost every mark.

Define the conditional characteristic function

\[
H_m(\omega)=\int e^{-i\omega\tau}\,d\mu_m(\tau).
\]

The autonomous assumption means that the kernel depends only on elapsed delay from photon arrival, not on absolute source phase or an external clock.

---

# 2. Weak sinusoidal Poisson source

Take incident intensity

\[
\Phi_\theta(t)
=\Phi_0[1+\theta\cos(\omega t)],
\qquad |\theta|\ll1.
\]

At `theta=0`, the incident Poisson Fisher-information rate is

\[
\boxed{
\dot F_{in}=\Phi_0/2.
}
\]

By the independent marking/displacement theorem for Poisson processes, the signal output is a marked Poisson process.

At mark `m`, its stationary baseline intensity measure is

\[
\Phi_0\kappa(dm),
\]

and its harmonic modulation amplitude is multiplied by `H_m(omega)`.

Therefore the ideal signal-only marked output FI rate is

\[
\boxed{
\dot F_{out}(\omega)
=
\frac{\Phi_0}{2}
\int_{\mathsf M}|H_m(\omega)|^2\,\kappa(dm).
}
\]

Thus the exact source-normalized transfer is

\[
\boxed{
\eta_I(\omega)
=
G(\omega)
\equiv
\int_{\mathsf M}|H_m(\omega)|^2\,\kappa(dm).
}
\]

At zero frequency,

\[
\boxed{G(0)=\eta.}
\]

This is the general event-kernel version of the earlier `eta_c E_M |H_M|^2` formula.

**Status:** PROVED from marked Poisson FI.

---

# 3. Parameter-independent background and downstream processing

Add any parameter-independent marked background process, including dark counts. For a Poisson background, it adds baseline intensity without adding signal derivative and therefore decreases FI.

More generally, any parameter-independent stochastic processing of the ideal primary record obeys Fisher-information data processing.

Hence

\[
\boxed{
\eta_I^{measured}(\omega)
\le
G(\omega).
}
\]

All subsequent upper bounds may therefore be proved for `G` without explicitly carrying dark/readout terms.

---

# 4. Exact mark-resolved atomic asymptotic

For each mark `m`, let the atomic masses of `mu_m` be

\[
p_j(m)=\mu_m(\{\tau_j(m)\}).
\]

Wiener's theorem gives

\[
\lim_{\Omega\to\infty}
\frac1{2\Omega}
\int_{-\Omega}^{\Omega}|H_m(\omega)|^2d\omega
=
\sum_jp_j(m)^2.
\]

Since `|H_m|^2<=1` and `kappa` is finite, dominated convergence gives

\[
\boxed{
\lim_{\Omega\to\infty}
\frac1{2\Omega}
\int_{-\Omega}^{\Omega}G(\omega)d\omega
=
\int_{\mathsf M}
\left[\sum_jp_j(m)^2\right]\kappa(dm).
}
\]

This is the exact absolute captured-information residual; no separate `eta` factor is needed because `kappa` already carries capture probability.

If every mark-conditioned delay law is non-atomic, the right side is zero.

---

# 5. Absolute timing-collision resource

When `mu_m` has square-integrable density `f_m(t)`, define the **absolute captured timing-collision intensity**

\[
\boxed{
\mathfrak R_2
=2\int_{\mathsf M}\kappa(dm)
\int_0^\infty f_m(t)^2dt.
}
\]

This quantity has units of inverse time and already includes capture/branch weights.

Parseval gives

\[
\int_{-\infty}^{\infty}
\frac{d\omega}{2\pi}
G(\omega)
=
\frac{\mathfrak R_2}{2}.
\]

Equivalently,

\[
\boxed{
\int_{-\infty}^{\infty}G(\omega)d\omega
=
\pi\mathfrak R_2.
}
\]

Therefore for a flat two-sided band,

\[
\boxed{
\bar\eta_I(\Omega)
\le
\min\left[
\eta,
\frac{\pi\mathfrak R_2}{2\Omega}
\right].
}
\]

If `eta>0`, define the capture-conditioned collision intensity

\[
\mathcal R_2=\mathfrak R_2/\eta.
\]

Then this becomes

\[
\bar\eta_I
\le
\eta\min\left(1,\frac{\pi\mathcal R_2}{2\Omega}\right),
\]

recovering WP26 exactly.

---

# 6. Mark-dependent hazard bounds

Suppose each conditional density has hazard `h_m(t)` bounded by a mark-dependent constant

\[
h_m(t)\le\Lambda(m).
\]

The WP25 hazard lemma applies mark by mark:

\[
2\int f_m(t)^2dt\le\Lambda(m).
\]

Hence

\[
\boxed{
\mathfrak R_2
\le
\int_{\mathsf M}\Lambda(m)\,\kappa(dm).
}
\]

This is sharper than requiring a single worst-case hazard.

Define the capture-weighted hazard capacity

\[
\boxed{
\mathfrak H
\equiv
\int_{\mathsf M}\Lambda(m)\,\kappa(dm).
}
\]

Then

\[
\boxed{
\bar\eta_I(\Omega)
\le
\min\left[
\eta,
\frac{\pi\mathfrak H}{2\Omega}
\right].
}
\]

If a uniform bound `Lambda(m)<=Lambda` and capture ceiling `eta<=C` are known,

\[
\mathfrak H\le\eta\Lambda\le C\Lambda,
\]

which yields the earlier WP25 theorem

\[
\bar\eta_I
\le
C\min\left(1,\frac{\pi\Lambda}{2\Omega}\right).
\]

### Important refinement

The **worst-case hazard `Lambda` is not mathematically necessary even for the quantitative `1/Omega` theorem**. A capture-weighted integrated local-hazard budget `mathfrak H` is sufficient.

A rare ultra-fast mark branch is harmless if its capture weight shrinks fast enough that `mathfrak H` remains finite.

This is the correct general marked-channel resource.

---

# 7. Parallel replication

Let detector branches `j` be retained as marks. Then

\[
\kappa=\sum_j\kappa_j,
\]

and

\[
G(\omega)=\sum_jG_j(\omega).
\]

For independent source channels, dividing by total incident source FI gives the corresponding source-weighted average.

Thus identical parallel replication scales total incident FI and total output FI equally; source-normalized performance is unchanged.

The absolute timing-collision resource and capture-weighted hazard are additive:

\[
\mathfrak R_2=\sum_j\mathfrak R_{2,j},
\qquad
\mathfrak H=\sum_j\mathfrak H_j.
\]

This gives the correct extensivity structure.

---

# 8. Arbitrary source spectrum

Let `w(omega)` be normalized incident spectral FI.

The measured average transfer obeys

\[
\bar\eta_I[w]
\le
\int w(\omega)G(\omega)d\omega.
\]

Since

\[
0\le G(\omega)\le\eta
\]

and

\[
\int G(\omega)d\omega\le\pi\mathfrak R_2,
\]

the bathtub/rearrangement principle gives, for `eta>0`,

\[
\boxed{
\bar\eta_I[w]
\le
\eta\,
\mathcal W\!\left(
\frac{\pi\mathfrak R_2}{\eta}
\right)
=
\eta\mathcal W(\pi\mathcal R_2).
}
\]

Similarly, with capture-weighted hazard capacity,

\[
\boxed{
\bar\eta_I[w]
\le
\eta\,
\mathcal W\!\left(
\frac{\pi\mathfrak H}{\eta}
\right).
}
\]

A uniform `Lambda` reduces this to

\[
\bar\eta_I[w]\le\eta\mathcal W(\pi\Lambda)\le C\mathcal W(\pi\Lambda).
\]

---

# 9. Relation to stationary thermodynamics

The refinement from worst-case `Lambda` to capture-weighted `mathfrak H` does **not** make stationary activity/EPR automatically sufficient.

Stationary activity weights local rates by stationary state occupation. `mathfrak H` weights post-capture registration hazards by **signal-event branch probability**. These weights can differ parametrically; WP4's rare-fast constructions exploit this mismatch.

WP29 remains a valid sufficient bridge because it establishes a uniform gateway rate bound `lambda_1<=Lambda_*`, which immediately implies

\[
\mathfrak H\le\eta\Lambda_*.
\]

A more general thermodynamic theorem might one day bound `mathfrak H` directly without a uniform local maximum, but that is not currently proved.

---

# 10. Resource hierarchy refinement

For the general autonomous marked one-event channel, the most economical current quantities are:

### Exact DC captured information ceiling

\[
\eta=\kappa(\mathsf M).
\]

### Exact asymptotic high-band residual

\[
\mathfrak A
=
\int\kappa(dm)\sum_jp_j(m)^2.
\]

### Quantitative integrated timing spectrum

\[
\mathfrak R_2
=2\int\kappa(dm)\int f_m^2dt.
\]

### Microscopic sufficient rate resource

\[
\mathfrak H
=\int\kappa(dm)\Lambda(m),
\qquad
\mathfrak R_2\le\mathfrak H.
\]

A uniform local hazard is a convenient stronger specialization, not the minimal marked-channel rate resource.

---

# 11. Status

**PROVED:** general marked subprobability-kernel FI formula, atomic asymptotic, absolute collision-intensity theorem, mark-weighted hazard bound, and extensivity structure.

**CORRECTION/REFINEMENT:** a global worst-case `Lambda` is sufficient but not necessary for the quantitative marked-channel theorem; the capture-weighted hazard capacity `mathfrak H` is sharper.

**OPEN:** whether a broadly applicable microscopic thermodynamic inequality can bound `mathfrak H` directly without first producing a uniform local-rate bound.