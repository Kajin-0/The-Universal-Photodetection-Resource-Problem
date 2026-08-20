# WP25 — Registration-Intensity Information-Bandwidth Theorem

**Date:** 2026-08-20

## Purpose

Return from the HgCdTe material-validation branch to the central Universal Photodetection Resource Problem (UPRP).

This note asks for the smallest resource set that is sufficient to produce a rigorous finite information-bandwidth ceiling in a broad but explicit detector class.

Main result:

> For a proper event photodetector driven by weak coherent/Poisson optical flux, a finite upper bound on the **post-capture electrical registration hazard** is enough to force a finite average information bandwidth. Capture efficiency and dark counts set the DC information ceiling; arbitrary downstream electronics can only reduce Fisher information and therefore need not appear in the intrinsic upper bound.

This sharply compresses the earlier long resource list for the event-detector branch.

---

# 1. Detector class

Consider a **proper primary-event photodetector** with the following structure.

1. Incident photons form an inhomogeneous Poisson process with weak modulation

\[
\Phi_\theta(t)=\Phi_0[1+\theta s(t)],
\qquad |\theta|\ll1.
\]

The same formulas describe the direct-detection statistics of weak modulation of a coherent optical state.

2. Each incident signal photon is captured independently with probability `eta`, with

\[
0\le\eta\le C\le1.
\]

3. Conditional on successful capture, one primary intrinsic electrical registration occurs after a nonnegative random delay `D` with normalized density `f_D(t)`.

4. The delay law is independent of the small signal parameter `theta`.

5. Independent dark registrations form a homogeneous Poisson process of rate `d`, with

\[
d\ge d_0\ge0.
\]

6. Any amplifier, filter, threshold, ADC, multiplication stage, or other downstream processing is a parameter-independent stochastic channel acting on the intrinsic primary electrical record.

The theorem concerns source information that reaches the **intrinsic primary electrical event record**. By Fisher-information data processing, the same result is automatically an upper bound for every downstream measured record.

The theorem does not claim to cover arbitrary continuous analog detectors, coherent unitary pointers before registration, or detector classes in which one absorbed photon produces an unresolved parameter-dependent many-event process. Those require separate branches already developed elsewhere in the repository.

---

# 2. Exact frequency-resolved Fisher-information transfer

Let

\[
H_D(\omega)=\mathbb E[e^{-i\omega D}]
=\int_0^\infty f_D(t)e^{-i\omega t}dt
\]

be the delay characteristic function.

Poisson thinning and the Poisson displacement theorem give the intrinsic signal-event intensity

\[
\lambda_{\rm sig,\theta}(t)
=\eta\int_0^\infty f_D(u)\Phi_\theta(t-u)du.
\]

Adding dark events,

\[
\lambda_{\rm out,\theta}(t)
=\lambda_{\rm sig,\theta}(t)+d.
\]

For an infinitesimal sinusoidal modulation at angular frequency `omega`, the incident Poisson Fisher-information rate is proportional to `Phi_0`, while the output rate has modulation amplitude multiplied by `eta H_D(omega)` and baseline `eta Phi_0+d`.

Therefore the exact source-normalized intrinsic Fisher-information transfer is

\[
\boxed{
\eta_I(\omega)
=
\frac{\eta^2\Phi_0}
{\eta\Phi_0+d}
|H_D(\omega)|^2.
}
\]

Define the DC information factor

\[
\boxed{
A(\eta,d;\Phi_0)
=\frac{\eta^2\Phi_0}{\eta\Phi_0+d}.
}
\]

At zero frequency `H_D(0)=1`, so

\[
\eta_I(0)=A.
\]

This separates static sensitivity/information efficiency from temporal information loss.

---

# 3. Capture/dark resource ceiling

For positive `Phi_0`,

\[
\frac{\partial A}{\partial\eta}>0,
\qquad
\frac{\partial A}{\partial d}<0.
\]

Thus, if

\[
\eta\le C,
\qquad d\ge d_0,
\]

then

\[
\boxed{
A\le A_*
\equiv
\frac{C^2\Phi_0}{C\Phi_0+d_0}.
}
\]

Special cases:

- no proven dark floor: `d_0=0`, hence `A_* = C`;
- no optical capture information beyond probability conservation: `C=1`, hence `A_* = Phi_0/(Phi_0+d_0)`;
- neither resource bounded beyond trivial physics: `C=1,d_0=0`, hence `A_*=1`.

Thus a finite timing theorem can exist even without a dark-floor theorem, but temperature-dependent **sensitivity** requires a separate microscopic relation that maps temperature and detector resources into `C` and/or `d_0`.

---

# 4. Registration-hazard resource

Let

\[
S(t)=\Pr[D>t]
\]

be the survival probability and

\[
\boxed{
h(t)=\frac{f_D(t)}{S(t)}}
\]

the conditional registration hazard where `S(t)>0`.

Assume the physical registration process obeys

\[
\boxed{h(t)\le\Lambda}
\]

for all relevant times.

`Lambda` has dimensions of inverse time and is an **absolute local electrical-registration intensity resource**.

This is fundamentally different from stationary dynamical activity. A rare state can have an arbitrarily large local event rate while contributing negligibly to stationary activity; the WP4 rare-fast counterexample exploits exactly that distinction.

---

# 5. Hazard ceiling implies an L2 timing-density ceiling

Write the cumulative hazard

\[
u(t)=\int_0^t h(s)ds,
\]

so

\[
S(t)=e^{-u(t)},
\qquad
f_D(t)=h(t)e^{-u(t)}.
\]

Then

\[
\int_0^\infty f_D(t)^2dt
=\int_0^\infty h(t)^2e^{-2u(t)}dt.
\]

On intervals where `h>0`, use `du=h dt`:

\[
\int f_D^2dt
=\int_0^\infty h(u)e^{-2u}du.
\]

Since `h<=Lambda`,

\[
\boxed{
\int_0^\infty f_D(t)^2dt
\le
\frac{\Lambda}{2}.
}
\]

Zero-hazard intervals simply contribute nothing and do not alter the inequality.

Equality is attained by a constant-hazard exponential delay

\[
f_D(t)=\Lambda e^{-\Lambda t}.
\]

**Status:** PROVED.

---

# 6. Parseval information-bandwidth theorem

Using the Fourier convention above, Parseval gives

\[
\int_{-\infty}^{\infty}
\frac{d\omega}{2\pi}
|H_D(\omega)|^2
=
\int_0^\infty f_D(t)^2dt.
\]

Therefore

\[
\boxed{
\int_{-\infty}^{\infty}
\frac{d\omega}{2\pi}
|H_D(\omega)|^2
\le\frac{\Lambda}{2}.
}
\]

Define the flat two-sided source-information task

\[
\boxed{
\bar\eta_I(\Omega_s)
=\frac{1}{2\Omega_s}
\int_{-\Omega_s}^{\Omega_s}
\eta_I(\omega)d\omega.
}
\]

Since `|H_D|<=1`,

\[
\frac{1}{2\Omega_s}
\int_{-\Omega_s}^{\Omega_s}|H_D|^2d\omega
\le
\min\left[
1,
\frac{\pi\Lambda}{2\Omega_s}
\right].
\]

Combining with Sec. 3 yields the central theorem:

\[
\boxed{
\bar\eta_I(\Omega_s)
\le
A_*
\min\left[
1,
\frac{\pi\Lambda}{2\Omega_s}
\right],
}
\]

where

\[
\boxed{
A_*
=\frac{C^2\Phi_0}{C\Phi_0+d_0}.
}
\]

Because any downstream parameter-independent readout is a stochastic map of the primary event record, Fisher-information data processing gives

\[
\boxed{
\bar\eta_I^{\rm measured}
\le
\bar\eta_I^{\rm intrinsic}
\le
A_*
\min\left[
1,
\frac{\pi\Lambda}{2\Omega_s}
\right].
}
\]

This automatically includes arbitrary RC filtering, deterministic gain, thresholding, ADC, unresolved avalanche marks, etc. as downstream processes: they may tighten the bound but can never invalidate it upward.

**Status:** PROVED for the stated proper-event class.

---

# 7. Required bandwidth for a target information fraction

Suppose the task requires

\[
\bar\eta_I(\Omega_s)\ge q>0.
\]

A necessary DC condition is

\[
\boxed{q\le A_*.}
\]

In addition, the theorem implies

\[
\boxed{
\Omega_s
\le
\frac{\pi\Lambda A_*}{2q}.
}
\]

Writing the two-sided half-band in ordinary frequency as

\[
\Omega_s=2\pi B,
\]

one obtains

\[
\boxed{
B
\le
\frac{\Lambda A_*}{4q}.
}
\]

This is a source-information bandwidth ceiling, not a conventional electrical `-3 dB` amplitude bandwidth.

---

# 8. Asymptotic tightness

For constant hazard `Lambda`,

\[
f_D(t)=\Lambda e^{-\Lambda t},
\qquad
H_D(\omega)=\frac{\Lambda}{\Lambda+i\omega}.
\]

Then exactly

\[
\boxed{
\frac{1}{2\Omega_s}
\int_{-\Omega_s}^{\Omega_s}|H_D|^2d\omega
=
\frac{\Lambda}{\Omega_s}
\tan^{-1}\left(\frac{\Omega_s}{\Lambda}\right).
}
\]

For

\[
\Omega_s\gg\Lambda,
\]

\[
\frac{\Lambda}{\Omega_s}
\tan^{-1}(\Omega_s/\Lambda)
\sim
\frac{\pi\Lambda}{2\Omega_s}.
\]

Thus the theorem's high-bandwidth prefactor is asymptotically saturated by the simplest memoryless registration process.

The `1/Omega_s` scaling and coefficient are therefore not merely loose consequences of Parseval.

---

# 9. Necessity of an absolute registration-intensity resource

If no finite `Lambda` is supplied, hold capture and dark resources fixed and consider

\[
f_n(t)=n e^{-nt}.
\]

Then

\[
H_n(\omega)=\frac{n}{n+i\omega}.
\]

For every fixed finite source band `Omega_s`,

\[
\lim_{n\to\infty}
\frac{1}{2\Omega_s}
\int_{-\Omega_s}^{\Omega_s}|H_n|^2d\omega
=1.
\]

Hence

\[
\boxed{
\text{capture efficiency + dark rate + temperature labels alone}
\not\Rightarrow
\text{finite event-detector information bandwidth}
}
\]

unless those resources themselves imply a finite absolute registration intensity.

This is the event-record analogue of WP4's rare-fast-state no-go.

**Status:** PROVED explicit counterexample family.

---

# 10. Microscopic interpretation of Lambda

## 10.1 Classical Markov jump detector

Let `E_reg` be the set of transitions that create the first primary electrical registration. For internal state `x`, define the instantaneous registration escape rate

\[
r_{\rm reg}(x)
=\sum_{y:(x\to y)\in E_{\rm reg}}W_{yx}.
\]

Conditioned on no registration yet,

\[
h(t)=\mathbb E[r_{\rm reg}(X_t)\mid D>t].
\]

Therefore

\[
\boxed{
\Lambda_{\rm cl}
=\max_x r_{\rm reg}(x)
}
\]

is a sufficient microscopic hazard ceiling.

This makes explicit why stationary activity does not generally replace `Lambda_cl`: activity weights rates by state occupation; `Lambda_cl` is a local operator/rate norm.

## 10.2 Quantum-jump detector

For electrical-registration jump operators `L_alpha`, the no-jump conditional hazard is

\[
h(t)=
\sum_\alpha
\langle L_\alpha^\dagger L_\alpha\rangle_{\rm cond}(t).
\]

Thus

\[
\boxed{
\Lambda_{\rm q}
=
\left\|
\sum_\alpha L_\alpha^\dagger L_\alpha
\right\|_\infty
}
\]

is a sufficient hazard ceiling.

This provides a direct quantum-event interpretation of the same resource without invoking a classical master equation.

## 10.3 Structured/non-Markovian registration

The theorem itself does not require Markovianity. It only requires a first-registration delay distribution with bounded conditional hazard. Structured reservoirs, memory, anti-Zeno effects, etc. are allowed provided they do not violate the stated finite `Lambda`.

The WP11 structured-reservoir work should therefore be reinterpreted as one possible microscopic route to bounding or violating `Lambda`, rather than as a separate primitive theorem resource.

---

# 11. What happened to temperature?

Temperature does **not** appear explicitly in the abstract event theorem.

This is a feature, not an omission.

At the theorem level, temperature can affect photodetection information only through a microscopic relation that maps `T` and other physical resources into quantities such as

\[
C(T,\ldots),
\qquad
d_0(T,\ldots),
\qquad
\Lambda(T,\ldots).
\]

Temperature by itself does not specify optical coupling, dark-event channels, local registration rates, detector Hamiltonians, or reservoir spectra.

Therefore any claimed universal sensitivity-bandwidth-temperature law must separately prove how finite-temperature physics constrains `C`, `d_0`, and/or `Lambda` in the detector class under consideration.

This is consistent with the earlier Markov no-go results showing that temperature, detailed balance, stationary EPR, and stationary activity do not determine an absolute microscopic speed scale.

---

# 12. Minimal-resource interpretation for the proper-event branch

The earlier project-wide resource hierarchy mixed resources needed by different detector classes.

For the **proper-event branch**, the core theorem reduces to:

\[
\boxed{
\text{finite source information band}
+
\text{finite DC information ceiling }A_*
+
\text{finite primary-registration hazard }\Lambda
\Longrightarrow
\text{finite average information bandwidth}.
}
\]

`A_*` can be resolved physically into capture and dark resources. `Lambda` can be resolved physically into local transition/jump/operator or reservoir resources.

External readout resources are **not required for an intrinsic upper bound**, because downstream processing cannot increase FI.

Preloaded squeezing/apparatus QFI is also not an independent primitive in this event theorem because the output class has already been restricted to a first primary registration process with bounded hazard. It remains essential in the separate coherent continuous-pointer branch of WP7/WP8.

This is the first major compression of the UPRP resource list.

---

# 13. Detector-class taxonomy implied by the result

A single minimal resource set should no longer be expected to cover all photodetectors without qualification.

At least three branches are now distinguished:

1. **proper event/counter detectors** — WP25 theorem; core timing resource is a bounded primary-registration hazard;
2. **continuous classical/Markov analog detectors** — finite-frequency fluctuation-response/response-uncertainty theory is already close prior art; photodetection-specific source/capture mapping is the remaining layer;
3. **coherent quantum pointer detectors before irreversible registration** — WP7/WP8 show that interaction action alone is insufficient and preloaded apparatus/generator resources must be bounded.

This taxonomy is more precise than one overgrown universal resource list.

---

# 14. Novelty posture

The mathematical ingredients used here are standard individually:

- Poisson thinning/displacement;
- Fisher information of an inhomogeneous Poisson process;
- survival/hazard representation;
- Parseval/Plancherel;
- Fisher-information data processing.

Do **not** claim those ingredients as new.

The candidate contribution is their **photodetection-specific resource-completeness composition**:

- identify local primary registration intensity, not conventional transit/RC bandwidth or stationary activity, as the minimal event-detector timing resource;
- prove a finite source-information bandwidth bound from that resource;
- show the bound is asymptotically tight;
- prove that omission of the local rate norm removes any finite bandwidth ceiling;
- separate intrinsic event information from arbitrary downstream electronics;
- clarify that temperature requires a separate microscopic map rather than appearing automatically in the universal theorem.

A theorem-level literature audit is still required before publication-level novelty claims.

---

# 15. Next steps

1. Audit the literature specifically for any prior photodetection theorem equivalent to the `hazard -> Parseval -> source-FI bandwidth` result.
2. Determine whether the proper-event assumptions can be weakened to marked point processes and multiple registration channels without changing the bound.
3. Test parallel replication/channel-count scaling and ensure `Lambda` is defined per incident optical channel or normalized extensive resource.
4. Compose existing WP3/WP4 microscopic rate results into explicit bounds on `Lambda` rather than maintaining them as separate primitive resources.
5. Decide whether WP25 plus the no-go taxonomy is the central theorem of a first UPRP manuscript.

---

# Status

**PROVED for the stated proper-event photodetector class.**

This work package returns the project to the original universal-resource question and materially compresses the event-detector resource set.