# WP25 — Registration-Intensity Information-Bandwidth Theorem

**Date:** 2026-08-20

## Purpose

Return from the HgCdTe material-validation branch to the central Universal Photodetection Resource Problem (UPRP), and identify the smallest sufficient timing resource for an explicit detector class.

Main result:

> For a proper event photodetector driven by weak coherent/Poisson optical flux, a finite bound on the **primary electrical registration hazard after conditioning on all accessible event marks** forces a finite average source-information bandwidth. Capture probability sets the universal DC ceiling. Dark/background events and arbitrary downstream electronics need not appear in the universal upper bound because adding parameter-independent noise or coarse graining cannot increase Fisher information.

This is a substantial compression of the earlier project-wide resource list for the event-detector branch.

---

# 1. Detector class and record definition

Consider a **proper primary-event photodetector**.

1. Incident photons form an inhomogeneous Poisson process

\[
\Phi_\theta(t)=\Phi_0[1+\theta s(t)],
\qquad |\theta|\ll1.
\]

The same direct-detection statistics arise from weak flux modulation of a coherent optical state.

2. Each incident signal photon is captured independently with probability `eta`,

\[
0\le\eta\le C\le1.
\]

3. Conditional on successful capture, one primary intrinsic electrical registration occurs. The accessible primary event may contain an arbitrary mark `M=m` such as pulse amplitude, channel identity, or other side information.

4. Conditional on mark `m`, the electrical registration delay `D` has normalized density

\[
f(t\mid m),\qquad t\ge0,
\]

and characteristic function

\[
H_m(\omega)=\int_0^\infty f(t\mid m)e^{-i\omega t}dt.
\]

The mark law `p(m)` and the conditional delay laws are independent of the small signal parameter `theta`.

5. Arbitrary parameter-independent dark/background records may be added after the signal-event channel.

6. Arbitrary parameter-independent downstream processing—gain, filtering, thresholding, ADC, multiplication, etc.—may act on the intrinsic primary record.

By Fisher-information data processing, neither independent parameter-free noise addition nor downstream coarse graining can increase source FI. Therefore it is sufficient to bound the ideal marked signal record.

The theorem does not claim to cover arbitrary continuous analog detectors, coherent unitary pointers before registration, or source-dependent many-event gain dynamics. Those remain separate detector classes.

---

# 2. Exact marked-record Fisher-information transfer

For a sinusoidal infinitesimal modulation at angular frequency `omega`, the signal-event intensity in mark-time space has baseline

\[
\lambda_0(m)=\eta\Phi_0 p(m)
\]

and modulation amplitude multiplied by `H_m(omega)`.

The Fisher-information rate of a marked Poisson process is the integral of `(partial_theta lambda)^2/lambda` over mark and time. Therefore, with no extra background/coarse graining, the exact source-normalized transfer is

\[
\boxed{
\eta_I^{\rm mark}(\omega)
=
\eta\int p(m)|H_m(\omega)|^2dm.
}
\]

For a discrete mark set, replace the integral by a sum.

Any independent parameter-free dark/background process or downstream stochastic processing gives

\[
\boxed{
\eta_I^{\rm measured}(\omega)
\le
\eta_I^{\rm mark}(\omega).
}
\]

This fixes an important issue in earlier timing arguments: a mark that reveals capture position or deterministic delay can restore timing information that would be lost after marginalizing the mark. The correct timing resource must therefore be conditioned on **all accessible side information**.

---

# 3. Conditional registration-hazard resource

For each accessible mark `m`, let

\[
S(t\mid m)=\Pr[D>t\mid M=m]
\]

and

\[
\boxed{
h(t\mid m)=\frac{f(t\mid m)}{S(t\mid m)}}
\]

where the survival probability is nonzero.

Define the uniform conditional registration-intensity resource

\[
\boxed{
\Lambda
=
\operatorname*{ess\,sup}_{m,t} h(t\mid m).
}
\]

Assume `Lambda<infinity`.

A deterministic delay revealed perfectly by a mark corresponds to a delta-distributed conditional delay and therefore to an infinite conditional hazard. This is exactly as required: known latency by itself is not an information-bandwidth limit.

---

# 4. Hazard ceiling implies an L2 timing-density ceiling

For fixed `m`, define cumulative hazard

\[
u_m(t)=\int_0^t h(s\mid m)ds.
\]

Then

\[
S(t\mid m)=e^{-u_m(t)},
\qquad
f(t\mid m)=h(t\mid m)e^{-u_m(t)}.
\]

Thus

\[
\int_0^\infty f(t\mid m)^2dt
=
\int_0^\infty h(t\mid m)^2e^{-2u_m(t)}dt.
\]

Using `du_m=h dt` on positive-hazard intervals,

\[
\int f^2dt
=
\int_0^\infty h(u\mid m)e^{-2u}du
\le
\frac{\Lambda}{2}.
\]

Therefore, uniformly in every accessible mark,

\[
\boxed{
\|f(\cdot\mid m)\|_2^2\le\Lambda/2.
}
\]

The constant-hazard exponential law

\[
f(t\mid m)=\Lambda e^{-\Lambda t}
\]

saturates this inequality.

**Status:** PROVED.

---

# 5. Parseval information-bandwidth theorem

Parseval gives, for every mark,

\[
\int_{-\infty}^{\infty}
\frac{d\omega}{2\pi}|H_m(\omega)|^2
=
\int_0^\infty f(t\mid m)^2dt
\le\frac{\Lambda}{2}.
\]

Define the flat two-sided source-information task

\[
\boxed{
\bar\eta_I(\Omega_s)
=
\frac{1}{2\Omega_s}
\int_{-\Omega_s}^{\Omega_s}
\eta_I(\omega)d\omega.
}
\]

Since `|H_m|<=1`, averaging first over frequency and then over marks gives

\[
\frac{1}{2\Omega_s}
\int_{-\Omega_s}^{\Omega_s}
\int p(m)|H_m(\omega)|^2dm\,d\omega
\le
\min\left[
1,
\frac{\pi\Lambda}{2\Omega_s}
\right].
\]

Using `eta<=C`,

\[
\boxed{
\bar\eta_I^{\rm measured}(\Omega_s)
\le
C
\min\left[
1,
\frac{\pi\Lambda}{2\Omega_s}
\right].
}
\]

This is the **mark-robust Registration-Intensity Information-Bandwidth Theorem**.

With no optical resource beyond probability conservation, `C<=1` gives the universal proper-event form

\[
\boxed{
\bar\eta_I^{\rm measured}(\Omega_s)
\le
\min\left[
1,
\frac{\pi\Lambda}{2\Omega_s}
\right].
}
\]

**Status:** PROVED for the stated proper-event class.

---

# 6. Target-bandwidth consequence

If the task requires

\[
\bar\eta_I(\Omega_s)\ge q>0,
\]

then necessarily

\[
\boxed{q\le C}
\]

and

\[
\boxed{
\Omega_s
\le
\frac{\pi\Lambda C}{2q}.
}
\]

Writing

\[
\Omega_s=2\pi B,
\]

where `B` is the ordinary-frequency two-sided half-band,

\[
\boxed{
B\le\frac{\Lambda C}{4q}.
}
\]

This is an information-bandwidth ceiling, not an amplitude `-3 dB` bandwidth.

---

# 7. Asymptotic tightness

Take one mark and a constant-hazard delay

\[
f_D(t)=\Lambda e^{-\Lambda t},
\qquad
H_D(\omega)=\frac{\Lambda}{\Lambda+i\omega}.
\]

Then

\[
\frac{1}{2\Omega_s}
\int_{-\Omega_s}^{\Omega_s}|H_D|^2d\omega
=
\frac{\Lambda}{\Omega_s}
\tan^{-1}\left(\frac{\Omega_s}{\Lambda}\right).
\]

For `Omega_s >> Lambda`,

\[
\frac{\Lambda}{\Omega_s}
\tan^{-1}(\Omega_s/\Lambda)
\sim
\frac{\pi\Lambda}{2\Omega_s}.
\]

Therefore the theorem's high-bandwidth prefactor is asymptotically saturated.

---

# 8. Necessity of the local registration-intensity resource

If no finite `Lambda` is supplied, fix capture at any nonzero `eta` and take

\[
f_n(t)=n e^{-nt}.
\]

Then

\[
H_n(\omega)=\frac{n}{n+i\omega}.
\]

For every fixed finite source band,

\[
\lim_{n\to\infty}
\frac{1}{2\Omega_s}
\int_{-\Omega_s}^{\Omega_s}|H_n|^2d\omega
=1.
\]

Thus no finite event-detector information-bandwidth ceiling follows from capture probability, temperature labels, stationary EPR, stationary activity, or other resources **unless those resources imply a finite local primary-registration intensity**.

This is the direct event-record version of the WP4 rare-fast-state no-go.

**Status:** PROVED explicit counterexample family.

---

# 9. Microscopic interpretation of Lambda

## 9.1 Classical Markov detector

Let `E_reg` be transitions producing first primary registration. For internal state `x`,

\[
r_{\rm reg}(x)
=
\sum_{y:(x\to y)\in E_{\rm reg}}W_{yx}.
\]

Conditioned on no event yet,

\[
h(t)=\mathbb E[r_{\rm reg}(X_t)\mid D>t].
\]

Hence

\[
\boxed{
\Lambda_{\rm cl}=\max_x r_{\rm reg}(x)
}
\]

is sufficient.

Stationary activity does not replace this local norm because activity weights rates by occupation. Rare states can have arbitrarily large `r_reg` while contributing little to stationary activity.

## 9.2 Quantum-jump detector

For electrical-registration jump operators `L_alpha`,

\[
h(t)=
\sum_\alpha
\langle L_\alpha^\dagger L_\alpha\rangle_{\rm cond}(t).
\]

Therefore

\[
\boxed{
\Lambda_q
=
\left\|
\sum_\alpha L_\alpha^\dagger L_\alpha
\right\|_\infty
}
\]

is sufficient.

The same event theorem therefore spans classical Markov and monitored quantum-jump detectors.

## 9.3 Non-Markovian registration

No Markov assumption is needed in the theorem itself. Any structured-reservoir or memory model is allowed if its full accessible marked first-registration process has finite conditional hazard `Lambda`.

---

# 10. Dark counts and temperature: what can and cannot be universal

Dark/background events do not appear in the mark-robust **upper** bound because parameter-independent extra noise cannot increase source FI.

If dark events are known to be **indistinguishable from signal events in the accessible record**, an unmarked Poisson corollary gives the sharper DC factor

\[
A(\eta,d)=
\frac{\eta^2\Phi_0}{\eta\Phi_0+d},
\]

and hence, for `eta<=C` and `d>=d_0`,

\[
\boxed{
\bar\eta_I
\le
\frac{C^2\Phi_0}{C\Phi_0+d_0}
\min\left[
1,
\frac{\pi\Lambda}{2\Omega_s}
\right].
}
\]

But a scalar dark rate cannot universally tighten the marked-record theorem: if signal and dark marks have disjoint support, the dark events are perfectly identifiable and cause no FI dilution.

Therefore any universal temperature-dependent sensitivity law needs an additional microscopic theorem connecting temperature to **signal-indistinguishable background**, capture, or registration intensity.

Temperature itself does not specify those quantities.

This is a central UPRP conclusion:

\[
\boxed{
T\text{ is not by itself an information-performance resource; it enters through a detector/bath coupling model.}
}
\]

---

# 11. Parallel replication and channel count

The theorem is normalized per incident optical information and is therefore invariant under ordinary parallel replication when each photon is routed to one primary detector channel.

If several marked subchannels have conditional hazards individually bounded by the same `Lambda`, their mixture also obeys the same hazard ceiling:

\[
f=\sum_jp_j f_j,
\qquad
S=\sum_jp_jS_j,
\]

and

\[
f\le\Lambda S.
\]

Thus merely adding more marked channels does not evade the per-photon theorem.

A separate optical channel-count/area resource is still required when asking about **total information rate for increasing incident mode number or detector area**, rather than source-normalized information per incident photon/task.

---

# 12. Minimal-resource interpretation

The earlier project-wide resource hierarchy mixed resources belonging to different output classes.

For the **proper primary-event branch**, the core sufficient set is now

\[
\boxed{
\text{finite source information band}
+
\text{finite conditional primary-registration intensity }\Lambda
}
\]

with the universal probability bound `C<=1` already giving a finite ceiling.

A nontrivial capture bound `C<1` tightens sensitivity. A signal-indistinguishable thermal/dark floor can tighten it further. Neither is required merely to prove finite average bandwidth once `Lambda` is finite.

External readout resources are not primitive for the intrinsic upper bound because of data processing.

Preloaded squeezing/apparatus QFI is not an independent primitive in this event theorem because the detector class has already been restricted to a first primary registration process with bounded conditional hazard. It remains essential in the separate coherent continuous-pointer branch of WP7/WP8.

This is the strongest resource compression obtained so far.

---

# 13. Detector-class taxonomy

A single minimal resource set should no longer be expected to cover every object called a photodetector.

At least three branches are distinct:

1. **proper event/counter detectors** — WP25; local conditional registration intensity is the core timing resource;
2. **continuous classical/Markov analog detectors** — finite-frequency fluctuation-response/response-uncertainty theory is already close prior art; the photodetection-specific source/capture map is the remaining layer;
3. **coherent quantum pointer detectors before irreversible registration** — WP7/WP8 prove interaction action alone is insufficient and apparatus preparation/generator resources must be bounded.

This taxonomy is a more precise answer to the UPRP than one overgrown universal scalar formula.

---

# 14. Novelty posture

The mathematical ingredients are standard individually:

- Poisson mapping/thinning;
- FI of marked Poisson processes;
- survival/hazard representation;
- Parseval/Plancherel;
- information data processing.

Do not claim these ingredients as new.

Candidate contribution:

- identify **conditional local primary-registration intensity**, after all accessible side information, as the minimal event-detector timing resource;
- prove a finite average source-information bandwidth from it;
- show asymptotic tightness;
- prove that omitting the local rate norm destroys any finite bandwidth ceiling;
- separate event/counter detectors from coherent and continuous-analog detector classes;
- show why temperature requires a detector/bath coupling theorem rather than entering automatically.

Targeted search on 2026-08-20 did not identify an equivalent photodetection theorem, but novelty remains provisional pending a theorem-level audit.

---

# 15. Next steps

1. Audit specifically for prior marked-point-process photodetection results equivalent to the conditional-hazard/Parseval bound.
2. Determine the weakest replacement for a uniform hazard norm: e.g. an integrated local-rate moment or registration operator norm that still forces finite bandwidth.
3. Compose WP3/WP4 microscopic rate results directly into `Lambda` and eliminate redundant resource language.
4. Rewrite the project roadmap around the detector-class taxonomy and mark WP17–24 as a frozen validation/example branch.
5. Decide whether WP25 plus the no-go taxonomy is the central theorem of the first UPRP manuscript.

---

# Status

**PROVED for the stated proper marked-event photodetector class.**

This work package returns the project to the original universal-resource question and materially compresses the event-detector resource set.