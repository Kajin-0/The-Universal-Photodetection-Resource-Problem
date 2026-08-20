# AGENTS.md

## Purpose

Durable handoff for **The Universal Photodetection Resource Problem (UPRP)**. The repository, not chat history, is authoritative.

Research is analytical/theoretical only. Numerical work is allowed for validation. Do not make experiments, fabrication, procurement, or laboratory campaigns necessary next steps.

## Read first

A replacement agent should read, in order:

1. `docs/CURRENT_RESEARCH_STATE.md`
2. `notes/RESEARCH_LOG_ROUND10.md`
3. `notes/WP25_REGISTRATION_INTENSITY_INFORMATION_BANDWIDTH_THEOREM.md`
4. `notes/WP26_JITTER_MOMENT_NO_GO_AND_COLLISION_INTENSITY_RESOURCE.md`
5. `notes/WP27_SYNCHRONOUS_CONTROL_CLOCK_NO_GO.md`
6. `notes/WP28_ARBITRARY_SOURCE_SPECTRAL_CONCENTRATION_THEOREM.md`
7. `docs/DECHANT_WP25_MAPPING.md`
8. `docs/NOVELTY_AUDIT_ROUND4_EVENT_INFORMATION_THEOREM.md`
9. `ROADMAP.md`
10. `notes/WP4_MICROSCOPIC_OPTICAL_COUPLING_NO_GO.md`
11. earlier WP0–WP24 notes only as needed.

---

# Strategic state

The detailed HgCdTe/Kane WP17–24 branch is **FROZEN** unless a core theorem later requires quantitative material validation. Do not resume 6↔8-band renormalization, heavy-hole refinements, or detailed HgCdTe modeling merely because those questions remain open.

The project has returned to the original universal-resource question and now uses a detector-class taxonomy rather than one oversized resource list.

---

# Core metric

Use source-normalized information transfer

\[
\boxed{\eta_I=F_{\rm electrical}/F_{\rm incident}^{Q}}
\]

for the same optical parameter.

Critical distinction:

\[
\boxed{\text{latency}\neq\text{amplitude bandwidth}\neq\text{information bandwidth}.}
\]

Known deterministic delays and invertible deterministic filtering do not by themselves reduce stationary FI.

---

# Current central theorem — autonomous proper event detectors

WP25 applies to an **autonomous/time-translation-invariant proper primary-event detector**:

- weak coherent/Poisson optical flux;
- each captured signal photon produces one primary intrinsic electrical registration;
- every accessible event mark is retained;
- no unbounded external clock/control is allowed to encode arrival time into a mark before registration.

For mark `M=m`, let `f(t|m)` be the conditional first-registration delay density and

\[
h(t|m)=f(t|m)/S(t|m).
\]

Define

\[
\boxed{\Lambda=\operatorname*{ess\,sup}_{m,t}h(t|m).}
\]

If capture probability `eta<=C`, then for a flat two-sided source-information band `|omega|<=Omega_s`,

\[
\boxed{
\bar\eta_I
\le
C\min\left(1,\frac{\pi\Lambda}{2\Omega_s}\right).
}
\]

For target `q`, ordinary-frequency half-band `B=Omega_s/(2pi)` must satisfy

\[
\boxed{B\le\Lambda C/(4q).}
\]

Constant-hazard exponential registration asymptotically saturates the high-bandwidth coefficient.

Microscopic sufficient bounds:

Classical Markov:

\[
\boxed{\Lambda_{cl}=\max_x\sum_{y\in E_{reg}(x)}W_{yx}.}
\]

Quantum jumps:

\[
\boxed{\Lambda_q=\left\|\sum_\alpha L_\alpha^\dagger L_\alpha\right\|_\infty.}
\]

This local rate/operator norm is distinct from stationary activity.

---

# WP26 — mathematically minimal timing-concentration resource

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
\le
C\min\left(1,\frac{\pi\mathcal R_2}{2\Omega_s}\right),
\qquad \mathcal R_2\le\Lambda.}
\]

Finite mean latency, RMS jitter, or FWHM jitter do **not** imply finite information bandwidth. WP26 contains an explicit smooth prompt-spike/long-tail counterexample at fixed variance.

Do not replace `R2`/`Lambda` by conventional jitter without proof.

---

# WP27 — external clock/control is a resource

An unrestricted synchronous detector can store optical arrival phase in an event mark and report it arbitrarily slowly while preserving the incident FI.

Therefore

\[
\boxed{
\text{finite registration hazard alone does not bound an actively synchronized detector if clock/control bandwidth is free.}
}
\]

Either:

- keep WP25 autonomous/time-translation invariant; or
- explicitly bound clock frequency/phase precision, control Hamiltonian/action, memory, and related reference resources.

Do not silently apply WP25 to heterodyne, lock-in, synchronous-gated, or externally clocked architectures.

---

# WP28 — arbitrary source spectrum

For normalized incident information spectrum

\[
w(\omega)=\mathcal J_{in}(\omega)/\int\mathcal J_{in}d\omega,
\]

define source spectral concentration

\[
\boxed{
\mathcal W(A)=\sup_{|E|\le A}\int_Ew(\omega)d\omega.}
\]

Then

\[
\boxed{
\bar\eta_I[w]
\le
C\mathcal W(\pi\mathcal R_2)
\le
C\mathcal W(\pi\Lambda).}
\]

This is preferred to inventing an arbitrary scalar bandwidth for multi-band or colored source tasks.

Flat-band WP25 is recovered exactly.

---

# Important no-go results that remain central

1. **Stationary thermodynamics is insufficient.** WP4 gives rare-fast Markov families with bounded EPR/activity but diverging bare/local speed. Therefore stationary activity/EPR cannot replace `Lambda`.
2. **RC amplitude bandwidth is not intrinsic FI bandwidth.** Deterministic filters preserve FI before downstream noise/coarse graining.
3. **Deterministic transit latency is not intrinsic FI loss.** Unresolved timing dispersion is.
4. **Conventional jitter moments are insufficient.** WP26.
5. **Free synchronous control defeats detector-only timing bounds.** WP27.
6. **Coherent-pointer branch needs separate apparatus resources.** WP7/WP8 squeezing and UV counterexamples remain valid but are not primitive resources in the proper-event theorem.

---

# Temperature

Temperature is **not by itself** an information-performance resource in the autonomous event theorem.

A genuine temperature-dependent sensitivity/bandwidth law requires a separate microscopic theorem mapping `T` plus bounded physical resources into one or more of:

- capture ceiling;
- signal-indistinguishable background;
- local conditional registration intensity/timing concentration.

Do not substitute a material-specific empirical dark-current formula for a universal theorem.

---

# Detector-class taxonomy

1. **Autonomous proper event/counter:** WP25–28 central theorem.
2. **Actively synchronized event:** clock/control resources required; WP27.
3. **Continuous classical/Markov analog:** general finite-frequency response/noise theory is close prior art; pursue only photodetection-specific additions.
4. **Coherent quantum pointer before irreversible registration:** WP7/WP8 separate resource theory.

A single resource formula covering all four without class assumptions is not currently expected.

---

# Novelty posture

Do not claim novelty for marked Poisson FI, hazard functions, Parseval, rearrangement inequalities, jitter distributions, synchronous detection, TUR/KUR/FRI theory, optical sum rules, or detector timing metrics individually.

Equation-level comparison shows WP25 is **not an obvious direct algebraic corollary** of Dechant's 2026 finite-frequency FRI, but novelty remains provisional.

Current candidate contribution:

> A photodetection-specific no-go/repair theorem identifying conditional local first-registration intensity / timing-density concentration as the resource controlling source-normalized information bandwidth in autonomous proper event detectors, together with explicit counterexamples showing why stationary activity, conventional jitter, deterministic latency, and free clock/control cannot substitute for it.

---

# Immediate next actions

1. Complete novelty audit in first-passage, reliability, queueing, random-delay Poisson-channel, and communication literature.
2. Rewrite WP3/WP4 directly as attempted microscopic bounds/no-go results for `Lambda`.
3. Finish only high-value assumption tests: dead time, multiple primary channels/photon-number resolution, and non-Poisson inputs.
4. Decide whether WP25–28 plus the necessity matrix supports a first manuscript.

Do **not** return to detailed HgCdTe modeling unless one of these gates explicitly requires it.

---

# Recordkeeping

After every substantive theorem, counterexample, correction, or novelty result:

- create/update a dedicated note;
- add a numbered research-log checkpoint when project direction changes;
- keep this file and `docs/CURRENT_RESEARCH_STATE.md` current;
- preserve failed conjectures.

Status vocabulary: **PROVED**, **VERIFIED**, **CONJECTURE**, **COUNTEREXAMPLE**, **OPEN**, **BLOCKED**, **REJECTED**.