# Research Roadmap — Resource-Completeness Phase

**Updated:** 2026-08-20

## Guiding principle

The project is no longer a broad search for arbitrary detector tradeoffs. It has converged to a **no-go + repair / detector-class taxonomy**.

The central question is:

> For each well-defined class of photodetector output record, what is the smallest noncircular physical resource set that is sufficient to bound source-normalized optical-to-electrical information transfer, and which resources are provably necessary because their omission permits explicit counterexamples?

Do not add new material-specific calculations unless they close a missing map from a theorem resource to real detector physics.

---

# Core metric — settled

Use

\[
\boxed{\eta_I=F_{\rm electrical}/F_{\rm incident}^{Q}}
\]

for the same encoded optical parameter.

For stationary weak coherent/Poisson modulation, use frequency-resolved or finite-source-task averages. Do **not** use an unweighted all-frequency integral.

Critical distinction:

\[
\boxed{\text{latency}\neq\text{amplitude bandwidth}\neq\text{information bandwidth}.}
\]

Known deterministic delay and invertible deterministic filtering do not by themselves reduce stationary FI.

---

# Branch E — proper event/counter detectors

## E0 — Exact event mapping

**Status: SOLVED**

For captured Poisson/coherent events with conditional electrical delay `D`, event-timestamp FI is controlled by the characteristic function of the delay law. Dark/background addition and downstream processing are information-degrading channels.

Primary notes:

- `notes/WP11_SPATIAL_DELAY_INFORMATION_THEOREM.md`
- `notes/WP14_INTRINSIC_VS_MEASURED_INFORMATION_BANDWIDTH.md`

## E1 — Minimal registration-intensity theorem

**Status: PROVED; current central theorem**

For a proper marked primary-event detector, condition on **all accessible event marks** `M`. Let

\[
\Lambda=\operatorname*{ess\,sup}_{m,t}h(t\mid m)
\]

be the conditional first-registration hazard ceiling and let `C` bound capture probability.

Then for a flat two-sided source-information band `|omega|<=Omega_s`,

\[
\boxed{
\bar\eta_I
\le
C\min\left(1,\frac{\pi\Lambda}{2\Omega_s}\right).
}
\]

Target `q` therefore requires

\[
\boxed{q\le C,\qquad B\le\Lambda C/(4q)}
\]

with `B=Omega_s/(2pi)`.

The high-bandwidth prefactor is asymptotically saturated by constant-hazard exponential registration.

Primary note:

- `notes/WP25_REGISTRATION_INTENSITY_INFORMATION_BANDWIDTH_THEOREM.md`

## E2 — Weakest timing-concentration resource

**Status: PROVED**

Define

\[
\mathcal R_2
=2\,\mathbb E_M\int f(t\mid M)^2dt.
\]

Then

\[
\bar\eta_I
\le
C\min\left(1,\frac{\pi\mathcal R_2}{2\Omega_s}\right),
\]

and a hazard ceiling implies `R2<=Lambda`.

Finite mean latency, FWHM jitter, and finite RMS jitter do **not** imply finite information bandwidth; explicit smooth counterexamples exist.

Primary note:

- `notes/WP26_JITTER_MOMENT_NO_GO_AND_COLLISION_INTENSITY_RESOURCE.md`

## E3 — Microscopic map to Lambda

**Status: PARTLY SOLVED**

Classical Markov primary-registration transitions:

\[
\Lambda_{cl}=\max_x\sum_{y\in E_{reg}(x)}W_{yx}.
\]

Quantum-jump primary registration:

\[
\Lambda_q=\left\|\sum_\alpha L_\alpha^\dagger L_\alpha\right\|_\infty.
\]

WP4 already proves that stationary EPR/activity cannot generally replace this local rate/operator norm because rare states can hide arbitrarily fast transitions.

### Remaining E3 work

1. Rewrite WP3/WP4 explicitly as bounds/no-go results for `Lambda`.
2. Audit structured-reservoir models only insofar as they bound or violate conditional `Lambda`.
3. Test dead time and multiple-primary-event models; do not let avalanche side branches obscure the first-event theorem.

## E4 — Temperature/sensitivity map

**Status: OPEN and conceptually isolated**

Temperature is not a primitive variable in the mark-robust event upper bound.

To obtain a genuine sensitivity–bandwidth–temperature theorem, prove a microscopic relation from `T` and other bounded resources to at least one of:

- capture ceiling `C(T,...)`;
- unavoidable **signal-indistinguishable** background;
- registration intensity `Lambda(T,...)`.

A scalar dark rate is not sufficient when dark and signal marks are distinguishable.

Do not insert empirical HgCdTe dark-current formulas as if they were universal.

---

# Branch A — continuous classical/Markov analog detectors

**Status: GENERAL THEORY CLOSE TO PRIOR ART; photodetection specialization OPEN**

Andreas Dechant's 2026 finite-frequency fluctuation-response inequality already gives general Markovian finite-frequency response/noise and broadband SNR constraints. TUR/KUR/RKUR literature further constrains precision using activity and quantum response resources.

UPRP should not attempt to rediscover these results.

### Remaining high-value question

Can optical-input normalization and explicit optical capture be composed with those general inequalities to produce a genuinely photodetection-specific theorem not already a direct corollary?

If not, Branch A should be treated as literature-covered background rather than a standalone paper result.

---

# Branch Q — coherent quantum pointers before irreversible registration

## Q0 — Trace-distance branch

**Status: PROVED restricted theorem**

Finite-hypothesis distinguishability transfer is bounded by nonlocal interaction action. This does not automatically imply an SLD-QFI bound.

## Q1 — QFI apparatus resource

**Status: PROVED for passive-linear coherent-displacement class**

Directional SLD-Stam plus detector excitation budget gives

\[
\frac{F_{elec}}{F_{in}}
\le
\frac\tau{\tau+(1-\tau)\xi(N)},
\qquad
\xi(N)=(\sqrt{N+1}-\sqrt N)^2.
\]

Pre-squeezing proves interaction action alone is insufficient.

## Q2 — UV/support no-go

**Status: PROVED**

Finite free energy in an unrestricted harmonic pointer does not control high-Fock coherence. Finite support plus bounded generator repairs the problem:

\[
\sup_{\rho\subset S}F_Q(\rho,G)
=4\inf_c\lambda_{max}[\Pi_S(G-cI)^2\Pi_S].
\]

### Remaining Branch Q work

Only continue if needed to compare the event theorem with a coherent detector that genuinely lies outside Branch E. Do not chase the exact unrestricted oscillator frontier unless publication value becomes clear.

---

# Resource-necessity matrix — current answer structure

| Candidate resource/metric | Sufficient by itself? | Current result |
|---|---|---|
| Temperature `T` | No | Needs a detector/bath coupling map |
| Stationary EPR/activity | No | Rare-fast Markov counterexample |
| Conventional RC bandwidth | No | Deterministic filtering is FI-invariant before downstream noise |
| Deterministic transit time | No | Latency alone preserves FI |
| RMS/FWHM timing jitter | No | WP26 prompt-spike/tail counterexample |
| Marginal delay distribution | No for full marked record | Accessible marks can undo delay |
| Conditional delay `L2` concentration `R2` | Yes for Branch E average bandwidth | WP26 |
| Conditional local hazard/rate norm `Lambda` | Yes; physical sufficient resource for Branch E | WP25 |
| Interaction action alone in coherent QFI branch | No | Squeezed-pointer counterexample |
| Finite apparatus excitation/support + coupling | Yes in stated passive-linear QFI class | WP7/WP8 |
| Total optical volume alone | No | Localized-capture geometry obstruction |
| Optical capture probability `C` | Tightens DC sensitivity but does not by itself bound speed | WP25 |
| Downstream readout bandwidth | Not needed for intrinsic upper bound | FI data processing |

This table should drive the paper logic.

---

# Frozen validation/example branch — WP15 through WP24

**Status: FROZEN unless needed by a core theorem**

This branch established useful physical examples:

- localized capture in delay space matters more than total optical volume;
- generic `alpha_abs v` bandwidth-efficiency physics is prior art;
- simplified Kane optical conductivity has the known `13/12` coefficient;
- finite-gap Kane composition plus radiative detailed balance gives a task-dependent phase diagram;
- self-consistent heavy-hole DOS/charge neutrality changes that phase diagram substantially;
- realistic heavy-hole DOS mass is near `0.53–0.54 m0` in the examined HgCdTe range;
- Pauli blocking is an order-unity correction while quadratic six-band optical curvature is only a few-percent correction in the tested model.

The unresolved 6↔8-band renormalization/`Gamma7` audit is recorded but **deprioritized**. Do not continue it unless a later theorem requires quantitative HgCdTe validation.

Primary checkpoint:

- `notes/RESEARCH_LOG_ROUND9.md`

---

# Immediate project gates

## Gate 1 — WP25 theorem-level novelty audit

Search specifically for prior results equivalent to:

\[
\text{conditional event hazard/rate norm}
\Rightarrow
\text{finite source-FI bandwidth via Parseval}.
\]

Marked Poisson FI, timing-jitter theory, and Parseval separately are prior art; the question is whether the **photodetection resource theorem** already exists.

## Gate 2 — Minimality/assumption audit

Stress-test WP25 against:

- accessible side information;
- multiple primary output channels;
- parallel replication;
- dead time;
- photon-number resolution;
- time-dependent/synchronous detector control;
- nonstationary source tasks;
- non-Poisson/nonclassical optical inputs.

Every failure must either tighten the class definition or expose a missing resource.

## Gate 3 — Integrate WP3/WP4 into Lambda

Stop treating EPR/activity/coupling as separate primitive entries in the event theorem. Express them as attempted microscopic bounds on `Lambda`, and retain the rare-fast result as the proof that stationary resources alone cannot supply such a bound.

## Gate 4 — Manuscript decision

After Gates 1–3, decide whether the first paper is centered on:

> **A no-free-lunch theorem for photodetection timing: local registration intensity, not conventional jitter or thermodynamic activity, is the resource controlling source-information bandwidth in proper event detectors.**

Do not draft a publication before the novelty and assumption audits pass.

---

# Publication logic

A plausible publication hierarchy is now:

1. **Proper-event photodetection resource theorem** — WP25/WP26 + necessity matrix.
2. **Coherent quantum detector resource theorem** — only if WP7/WP8 proves distinct enough after audit.
3. **Infrared/HgCdTe illustration** — use frozen WP17–24 only as an example or consequence, not as the universal theorem itself.

The project should now optimize for theorem closure, not calculation count.