# Current Research State

**Date:** 2026-08-20

This is the first-stop replacement-agent summary. **The repository, not chat history, is authoritative.**

## Read first

1. `AGENTS.md`
2. `notes/RESEARCH_LOG_ROUND10.md`
3. `notes/WP25_REGISTRATION_INTENSITY_INFORMATION_BANDWIDTH_THEOREM.md`
4. `notes/WP26_JITTER_MOMENT_NO_GO_AND_COLLISION_INTENSITY_RESOURCE.md`
5. `notes/WP27_SYNCHRONOUS_CONTROL_CLOCK_NO_GO.md`
6. `notes/WP28_ARBITRARY_SOURCE_SPECTRAL_CONCENTRATION_THEOREM.md`
7. `docs/DECHANT_WP25_MAPPING.md`
8. `docs/NOVELTY_AUDIT_ROUND4_EVENT_INFORMATION_THEOREM.md`
9. `ROADMAP.md`
10. `notes/WP4_MICROSCOPIC_OPTICAL_COUPLING_NO_GO.md`

The detailed HgCdTe/Kane WP17–24 branch is frozen unless a core theorem later requires it.

---

# 1. Central objective

Determine the smallest physical resource set that bounds source-normalized optical-to-electrical information acquisition for a precisely defined photodetector class, and prove necessity of resources by explicit counterexamples when omitted.

Core metric:

\[
\boxed{\eta_I=F_{\rm electrical}/F_{\rm incident}^{Q}.}
\]

The project is no longer seeking one naive sensitivity-bandwidth-temperature product across every detector architecture.

---

# 2. Most important conceptual distinction

\[
\boxed{\text{latency}\neq\text{amplitude bandwidth}\neq\text{information bandwidth}.}
\]

A known deterministic delay changes phase but not stationary spectral FI. An invertible deterministic filter applied to signal and all upstream noise does not change `|chi|^2/S` wherever the transfer function is nonzero.

Information loss requires unresolved stochasticity, inaccessible/coarse-grained variables, downstream noise, finite observation/sampling/quantization, exact nulls, or an explicitly bounded control/reference resource.

---

# 3. Current central theorem — autonomous proper marked-event detectors

WP25 now provides the strongest direct answer to the original UPRP for the event/counter class.

Assume:

- weak coherent/Poisson optical modulation;
- independent capture probability `eta<=C`;
- one primary intrinsic electrical registration per captured photon;
- every accessible event mark `M` retained;
- autonomous/time-translation-invariant optical-to-event processing; no free source-synchronous clock encodes arrival time into the mark.

For conditional delay density `f(t|m)`, survival `S(t|m)`, and hazard

\[
h(t|m)=f(t|m)/S(t|m),
\]

define

\[
\boxed{\Lambda=\operatorname*{ess\,sup}_{m,t}h(t|m).}
\]

Then

\[
\int f(t|m)^2dt\le\Lambda/2
\]

and, for a flat two-sided information band `|omega|<=Omega_s`,

\[
\boxed{
\bar\eta_I
\le
C\min\left(1,\frac{\pi\Lambda}{2\Omega_s}\right).}
\]

Target average information fraction `q` therefore requires

\[
\boxed{q\le C}
\]

and

\[
\boxed{B\le\Lambda C/(4q),
\qquad B=\Omega_s/(2\pi).}
\]

Constant-hazard exponential registration asymptotically saturates the high-bandwidth coefficient.

Microscopic sufficient resources:

\[
\boxed{\Lambda_{cl}=\max_x\sum_{y\in E_{reg}(x)}W_{yx}}
\]

for classical Markov registration, and

\[
\boxed{\Lambda_q=\left\|\sum_\alpha L_\alpha^\dagger L_\alpha\right\|_\infty}
\]

for quantum-jump registration.

---

# 4. Why stationary thermodynamics does not replace Lambda

WP4 provides explicit rare-fast reversible Markov families with bounded stationary activity/EPR and fixed thermodynamic labels while local bare rates diverge.

Thus

\[
\boxed{
\{T,\text{detailed balance},\Sigma,\mathcal A,\ldots\}
\not\Rightarrow
\Lambda<\infty.}
\]

The local registration-rate/operator norm is a distinct microscopic resource.

---

# 5. WP26 — collision intensity and the jitter no-go

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
\qquad
\mathcal R_2\le\Lambda.}
\]

`R2` is the mathematically minimal timing-concentration object used by the Parseval proof; `Lambda` is a local physical sufficient condition.

Explicit smooth two-exponential families prove:

\[
\boxed{
\text{finite/fixed mean latency + RMS jitter}
\not\Rightarrow
\text{finite information bandwidth}.}
\]

A dominant prompt peak can become arbitrarily narrow while a vanishing long-delay tail carries the moment constraint.

FWHM is likewise not resource-complete.

---

# 6. WP27 — reference-clock/control no-go

An unrestricted synchronous detector can store the optical arrival phase in an event mark and report it arbitrarily slowly.

For

\[
\Phi_\theta(t)=\Phi_0[1+\theta\cos\omega t],
\]

a phase mark

\[
M=\omega t\pmod{2\pi}
\]

retains the full incident timing FI per captured photon.

Therefore

\[
\boxed{
\text{finite registration hazard alone does not bound actively synchronized detector bandwidth if clock/control resources are free}.}
\]

Repair: either restrict WP25 to autonomous/time-translation-invariant processing, or count control bandwidth, clock frequency/phase precision, Hamiltonian/action, memory, etc.

---

# 7. WP28 — arbitrary source information spectrum

Normalize the incident information spectrum:

\[
w(\omega)=\mathcal J_{in}(\omega)/\int\mathcal J_{in}d\omega.
\]

Define its spectral concentration function

\[
\boxed{
\mathcal W(A)
=\sup_{|E|\le A}\int_Ew(\omega)d\omega.}
\]

Then for the autonomous proper marked-event class,

\[
\boxed{
\bar\eta_I[w]
\le
C\mathcal W(\pi\mathcal R_2)
\le
C\mathcal W(\pi\Lambda).}
\]

This removes the arbitrary flat-band convention and is the preferred source-side statement.

For a flat band, it reduces exactly to WP25.

Interpretation:

> finite timing concentration allows substantial information transfer over only finite total spectral measure; the source task determines how much information is concentrated in that measure.

---

# 8. Dark counts, readout, and temperature

Parameter-independent dark/background additions and downstream processing cannot increase source FI, so they are not required in the universal mark-robust upper bound.

If dark events are signal-indistinguishable, a sharper unmarked Poisson corollary includes the usual dark dilution factor.

Temperature is **not by itself** an information-performance resource. A genuine sensitivity-bandwidth-temperature theorem needs a microscopic relation from `T` and other bounded physical resources to at least one of:

- capture;
- signal-indistinguishable background;
- local registration intensity/timing concentration.

Do not substitute an empirical material dark-current law for a universal theorem.

---

# 9. Detector-class taxonomy

Current classes:

1. **Autonomous proper event/counter detectors** — WP25–28 central result.
2. **Actively synchronized event detectors** — explicit control/reference resources required; WP27.
3. **Continuous classical/Markov analog detectors** — general finite-frequency response/noise theory is close prior art; pursue only distinct photodetection-specific composition.
4. **Coherent quantum pointers before irreversible registration** — WP7/WP8 separate apparatus/coupling/support resource theory.

This taxonomy is currently a more accurate answer than one universal scalar product law.

---

# 10. Novelty status

Known prior art covers individually:

- single-photon efficiency/dark/dead-time/jitter metrics;
- timing distributions and IRFs;
- marked Poisson Fisher information;
- survival/hazard theory;
- Parseval/Plancherel and rearrangement inequalities;
- synchronous/heterodyne/lock-in detection;
- general finite-frequency fluctuation-response bounds.

Equation-level audit of Dechant 2026 shows WP25 is **not an obvious direct algebraic corollary** of the published finite-frequency FRI. Dechant gives a pointwise `R^†S^-1R<=A` bound and a different broadband response/static-variance integral. WP25 adds first-registration timing concentration and local hazard.

No equivalent complete photodetection theorem has yet been located, but novelty remains provisional.

---

# 11. Frozen material-validation branch

WP15–24 contain useful physical examples and should remain available, but detailed HgCdTe/Kane work is frozen.

Key lessons already extracted:

- total optical volume is not localized capture capacity;
- generic `alpha_abs v` bandwidth-efficiency is prior art;
- carrier statistics/Pauli blocking can dominate material-specific corrections;
- material parameters do not determine universal information performance without source, geometry, dark, and record assumptions.

Do not resume the unresolved 6↔8-band HgCdTe renormalization audit unless a core theorem explicitly requires it.

---

# 12. Immediate next gates

1. Search first-passage, reliability, queueing, random-delay Poisson-channel, and communication literature for an equivalent hazard/collision-intensity information theorem.
2. Rewrite WP3/WP4 directly in `Lambda` language and remove redundant event-branch resource entries.
3. Finish only assumption tests that can alter the theorem: dead time, multiple primary channels/photon-number resolution, parallel replication, and non-Poisson/nonclassical inputs.
4. Decide whether WP25–28 plus the necessity matrix forms a publication-worthy first theorem.

**Latest durable checkpoint:** `notes/RESEARCH_LOG_ROUND10.md`.