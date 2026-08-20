# Research Log — Round 10: Return to the Universal Theorem

**Date:** 2026-08-20

## Purpose

Durable checkpoint after deliberately freezing the detailed HgCdTe/Kane WP17–24 branch and returning to the original Universal Photodetection Resource Problem.

The central objective is again theorem closure: identify the smallest noncircular resources that bound source-normalized optical-to-electrical information transfer, and prove necessity by explicit counterexamples when a resource is omitted.

---

# 1. Strategic pivot

The detailed HgCdTe material branch was useful as a validation/example layer but had begun to consume effort on 6↔8-band renormalization, heavy-hole DOS refinements, and other material-specific details.

Decision:

\[
\boxed{\text{WP17--24 frozen unless a core theorem later requires them.}}
\]

The universal problem now uses a detector-class taxonomy rather than one oversized resource list.

---

# 2. Central detector-class taxonomy

At least four classes must be distinguished.

1. **Autonomous proper event/counter detectors.** One captured photon produces one primary electrical registration; all accessible event marks are retained. WP25–28 apply.
2. **Actively synchronized event detectors.** External clocks/control can down-convert timing information; control/reference resources must be counted. WP27 no-go.
3. **Continuous classical/Markov analog detectors.** General finite-frequency fluctuation-response theory is already close prior art; only a genuinely photodetection-specific source/capture composition is worth pursuing.
4. **Coherent quantum pointers before irreversible registration.** WP7/WP8 show interaction action alone is insufficient; apparatus preparation/support/generator resources matter.

A single scalar resource set should not be expected to cover these classes without qualification.

---

# 3. WP25 — local registration-intensity theorem

For the autonomous proper marked-event class, condition on every accessible mark `M=m` and let `f(t|m)` be the conditional first-registration delay density.

Define conditional hazard

\[
h(t|m)=f(t|m)/S(t|m)
\]

and local resource

\[
\boxed{\Lambda=\operatorname*{ess\,sup}_{m,t}h(t|m).}
\]

A hazard ceiling implies

\[
\boxed{\int f(t|m)^2dt\le\Lambda/2.}
\]

Parseval then gives a flat two-sided source-band theorem

\[
\boxed{
\bar\eta_I(\Omega_s)
\le C\min\left(1,\frac{\pi\Lambda}{2\Omega_s}\right).
}
\]

For target average information fraction `q`, ordinary-frequency half-band `B=Omega_s/(2pi)` obeys

\[
\boxed{B\le\Lambda C/(4q).}
\]

Constant-hazard exponential registration asymptotically saturates the high-bandwidth coefficient.

Microscopic sufficient resources:

Classical Markov:

\[
\Lambda_{cl}=\max_x\sum_{y\in E_{reg}(x)}W_{yx}.
\]

Quantum jumps:

\[
\Lambda_q=\left\|\sum_\alpha L_\alpha^\dagger L_\alpha\right\|_\infty.
\]

This identifies a local rate/operator norm, not stationary activity.

---

# 4. Mark correction

Marginal delay jitter is insufficient if the primary record contains side information that identifies the delay.

Therefore WP25 must condition on **all accessible parameter-independent event marks**.

The ideal marked-record transfer is

\[
\boxed{
\eta_I^{mark}(\omega)
=\eta\,\mathbb E_M|H_M(\omega)|^2.
}
\]

Dark/background addition and downstream electronics are parameter-independent channels and cannot increase FI.

A scalar dark rate only sharpens the theorem if dark events are signal-indistinguishable in the accessible record.

---

# 5. WP26 — timing-jitter no-go

Define

\[
\boxed{
\mathcal R_2
=2\,\mathbb E_M\int f(t|M)^2dt.}
\]

Then

\[
\boxed{
\bar\eta_I
\le C\min\left(1,\frac{\pi\mathcal R_2}{2\Omega_s}\right),
\qquad \mathcal R_2\le\Lambda.}
\]

`R2` is the mathematically minimal timing-concentration quantity used by the Parseval proof; `Lambda` is the stronger local microscopic sufficient resource.

Explicit smooth two-timescale mixtures prove that fixed finite mean/RMS timing jitter does **not** imply finite information bandwidth. A dominant prompt component can become arbitrarily narrow while a vanishing long tail carries the prescribed variance.

Therefore conventional mean latency, RMS jitter, and FWHM jitter are not resource-complete theorem variables.

---

# 6. WP27 — synchronous-control / clock no-go

A free high-frequency temporal reference defeats a detector-only timing theorem.

For

\[
\Phi_\theta(t)=\Phi_0[1+\theta\cos\omega t],
\]

an ideal synchronous detector can store the arrival phase

\[
M=\omega t\pmod{2\pi}
\]

and report it arbitrarily slowly. The phase mark carries exactly the incident Poisson FI per captured photon.

Even binary synchronous gating preserves a nonzero frequency-independent fraction of FI.

Hence

\[
\boxed{
\text{finite registration hazard alone does not bound an unrestricted actively synchronized detector.}
}
\]

Repair:

- restrict WP25 to autonomous/time-translation-invariant detection; or
- include reference-clock/control bandwidth, action, phase precision, memory, etc. as explicit resources.

---

# 7. WP28 — arbitrary source spectral-concentration theorem

The flat-band convention is not fundamental.

Normalize the incident Fisher-information spectrum:

\[
w(\omega)=\mathcal J_{in}(\omega)/\int\mathcal J_{in}d\omega,
\qquad \int w d\omega=1.
\]

Define spectral concentration function

\[
\boxed{
\mathcal W(A)
=\sup_{|E|\le A}\int_Ew(\omega)d\omega.}
\]

For an autonomous proper marked-event detector,

\[
\boxed{
\bar\eta_I[w]
\le C\,\mathcal W(\pi\mathcal R_2)
\le C\,\mathcal W(\pi\Lambda).}
\]

This follows from

\[
0\le G(\omega)=\mathbb E|H_M(\omega)|^2\le1,
\qquad
\int Gd\omega=\pi\mathcal R_2,
\]

and the bathtub/Hardy-Littlewood rearrangement principle.

For a flat band, `W(A)=min[1,A/(2Omega_s)]`, reproducing WP25 exactly.

Thus the source side is best described by **information spectral concentration**, not by an arbitrary `-3 dB` or RMS bandwidth.

---

# 8. Temperature conclusion

Temperature does not appear automatically in the mark-robust autonomous event theorem.

A genuine sensitivity-bandwidth-temperature law requires a separate microscopic theorem mapping `T` and other bounded resources into one or more of:

- capture ceiling;
- signal-indistinguishable background;
- conditional registration intensity/timing concentration.

This is consistent with WP4's rare-fast counterexample showing stationary EPR/activity and detailed-balance labels do not determine an absolute local speed scale.

---

# 9. Dechant 2026 equation-level audit

Dechant's finite-frequency FRI proves

\[
R^\dagger S^{-1}R\le A.
\]

This gives a pointwise response/noise ceiling. Its published broadband corollary integrates response magnitude normalized by **static variance**, not the UPRP source-FI kernel `|R|^2/S(omega)`.

WP25's additional physical ingredient is a bounded first-registration timing concentration, which makes

\[
\int |H(\omega)|^2d\omega
\]

finite.

Current conclusion:

\[
\boxed{\text{WP25 is not an obvious direct algebraic corollary of Dechant's displayed FRI.}}
\]

This does not prove novelty.

Primary audit: `docs/DECHANT_WP25_MAPPING.md`.

---

# 10. Novelty posture

Prior art includes:

- detector efficiency/dark/dead-time/jitter metrics;
- full detector timing distributions;
- marked Poisson FI;
- hazard/survival mathematics;
- Parseval and rearrangement inequalities;
- synchronous/heterodyne/lock-in detection;
- general finite-frequency fluctuation-response bounds.

Targeted search has not yet identified an equivalent complete theorem combining **autonomous marked photodetection + conditional local registration intensity + source-normalized FI bandwidth**.

Novelty remains provisional.

---

# 11. Immediate next gates

1. Search first-passage, reliability, queueing, random-delay Poisson-channel, and communication literature for equivalent hazard/characteristic-function information bounds.
2. Integrate WP3/WP4 explicitly into `Lambda`; stop listing stationary EPR/activity as independent event-theorem primitives.
3. Finish assumption audit: dead time, photon-number resolution, multiple primary channels, parallel replication, and non-Poisson inputs. Only pursue cases that change the theorem.
4. Decide whether WP25/WP26/WP27/WP28 plus the resource-necessity matrix forms a publication-worthy first theorem.

---

# Status

The project is now back on the original universal question. The current strongest answer is a **class-conditional resource theorem plus explicit no-go results**, rather than a universal material-specific sensitivity-bandwidth product.