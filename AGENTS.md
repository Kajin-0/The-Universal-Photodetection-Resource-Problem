# AGENTS.md

## Purpose

Durable handoff for **The Universal Photodetection Resource Problem (UPRP)**. The repository, not chat history, is authoritative.

Research is analytical/theoretical only. Numerical work is allowed for validation. Do not make experiments, fabrication, procurement, or laboratory campaigns necessary next steps.

## Read first

A replacement agent should read, in order:

1. `docs/CURRENT_RESEARCH_STATE.md`
2. `notes/RESEARCH_LOG_ROUND11.md`
3. `notes/WP29_THERMODYNAMIC_BRIDGE_TO_REGISTRATION_INTENSITY.md`
4. `notes/WP30_WIENER_ATOMIC_DELAY_INFORMATION_THEOREM.md`
5. `notes/WP31_EVENT_BRANCH_RESOURCE_NECESSITY_MATRIX.md`
6. `notes/WP25_REGISTRATION_INTENSITY_INFORMATION_BANDWIDTH_THEOREM.md`
7. `notes/WP26_JITTER_MOMENT_NO_GO_AND_COLLISION_INTENSITY_RESOURCE.md`
8. `notes/WP27_SYNCHRONOUS_CONTROL_CLOCK_NO_GO.md`
9. `notes/WP28_ARBITRARY_SOURCE_SPECTRAL_CONCENTRATION_THEOREM.md`
10. `docs/NOVELTY_AUDIT_ROUND4_EVENT_INFORMATION_THEOREM.md`
11. `docs/DECHANT_WP25_MAPPING.md`
12. `ROADMAP.md`
13. `notes/WP4_MICROSCOPIC_OPTICAL_COUPLING_NO_GO.md`
14. earlier WP0–WP24 notes only as needed.

The detailed HgCdTe/Kane WP17–24 branch is **FROZEN** unless a core theorem later explicitly requires material validation.

---

# Strategic state

The project has returned to the original universal-resource question. The most mature branch is now the **autonomous proper event/counter detector** class.

Do not re-expand the primitive resource list unless a counterexample proves a genuinely missing resource.

Core metric:

\[
\boxed{\eta_I=F_{\rm electrical}/F_{\rm incident}^{Q}.}
\]

Critical distinction:

\[
\boxed{\text{latency}\neq\text{amplitude bandwidth}\neq\text{information bandwidth}.}
\]

Known deterministic delay and invertible deterministic filtering do not by themselves reduce stationary FI.

---

# Event theorem stack

## WP30 — weakest current asymptotic statement

For complete accessible autonomous mark `M`, let the conditional registration-delay measure have atomic masses `p_j(M)`.

Then Wiener theory gives

\[
\boxed{
\lim_{\Omega\to\infty}\bar\eta_I(\Omega)
=\eta_c\,\mathbb E_M\!\left[\sum_jp_j(M)^2\right]
}
\]

in the ideal signal-only event channel.

Therefore purely non-atomic mark-conditioned delay laws force asymptotic flat-band average information to vanish.

This requires neither finite hazard nor finite RMS jitter.

Accessible marks matter: if a mark reveals a deterministic timing branch, conditional atomic mass can become one and timing information can be restored.

## WP26/WP28 — quantitative timing concentration

When conditional delay densities are square-integrable, define

\[
\boxed{
\mathcal R_2
=2\,\mathbb E_M\int f(t|M)^2dt.
}
\]

For arbitrary normalized incident information spectrum `w(omega)`, define

\[
\boxed{
\mathcal W(A)=\sup_{E:\,|E|\le A}\int_Ew(\omega)d\omega.
}
\]

Then

\[
\boxed{
\bar\eta_I[w]\le C\mathcal W(\pi\mathcal R_2).
}
\]

For a flat two-sided band,

\[
\boxed{
\bar\eta_I(\Omega)
\le C\min\left(1,\frac{\pi\mathcal R_2}{2\Omega}\right).
}
\]

Finite mean latency, RMS jitter, and FWHM jitter do **not** control `R2`; WP26 gives explicit smooth counterexamples.

## WP25 — microscopic hazard completion

Let

\[
\Lambda
=\operatorname*{ess\,sup}_{M,t}h(t|M).
\]

Then

\[
\boxed{\mathcal R_2\le\Lambda}
\]

and hence

\[
\boxed{
\bar\eta_I(\Omega)
\le C\min\left(1,\frac{\pi\Lambda}{2\Omega}\right).
}
\]

Constant-hazard exponential registration asymptotically saturates the high-bandwidth coefficient.

Microscopic sufficient realizations:

Classical Markov:

\[
\boxed{\Lambda_{cl}=\max_x\sum_{y\in E_{reg}(x)}W_{yx}.}
\]

Quantum jump:

\[
\boxed{\Lambda_q=\left\|\sum_\alpha L_\alpha^\dagger L_\alpha\right\|_\infty.}
\]

A finite hazard is a physically interpretable sufficient resource, **not** the mathematically weakest condition for qualitative asymptotic decay.

---

# WP29 — thermodynamic bridge

For the reversible single-gateway Markov class of WP3,

\[
0\xrightleftharpoons[d]{u}1,
\qquad f=u\pi_0\ge f_*,
\]

with total EPR `<=Sigma` and total stationary activity `<=A`, define

\[
g(z)=\left(1-\frac1z\right)\ln z,
\qquad
Z_*=g^{-1}(\Sigma/f_*).
\]

WP3 gives

\[
\pi_1\ge\frac{f_*}{dZ_*}
\]

and

\[
\boxed{
\lambda_1\le
\Lambda_*
=\frac{\mathcal A dZ_*}{f_*}.
}
\]

WP29 proves that any autonomous downstream registration delay/mark after the first gateway exit satisfies

\[
\boxed{h_D(t|M)\le\lambda_1\le\Lambda_*}.
\]

Therefore

\[
\boxed{
\bar\eta_I(\Omega)
\le
C\min\left[
1,
\frac{\pi\mathcal A d}{2f_*\Omega}
 g^{-1}(\Sigma/f_*)
\right].
}
\]

For arbitrary source spectrum,

\[
\boxed{
\bar\eta_I[w]
\le
C\mathcal W\!\left(
\pi\frac{\mathcal A d}{f_*}g^{-1}(\Sigma/f_*)
\right).
}
\]

The original gateway structure also yields a stronger Lorentzian pointwise envelope.

## Complementary no-go

WP4 proves that bounded temperature/detailed balance/EPR/activity/throughput do **not** supply the absolute local rate scale. Local microscopic rates can diverge while the stationary thermodynamic quantities remain bounded.

Thus the clean conclusion is

\[
\boxed{
\text{stationary thermodynamics alone}
\not\Rightarrow
\text{finite information bandwidth},
}
\]

but

\[
\boxed{
\text{thermodynamic budgets}
+\text{absolute microscopic rate scale}
\Rightarrow
\text{finite bandwidth}
}
\]

in the restricted gateway class.

---

# WP27 — external clock/control no-go

A free source-synchronous clock can encode arrival phase into an event mark and report it arbitrarily slowly while preserving the incident timing FI.

Therefore WP25–WP31 apply to **autonomous/time-translation-invariant event detectors** unless clock/control bandwidth, phase precision, memory, and control action are explicitly counted as resources.

Do not silently apply the theorem to heterodyne, lock-in, synchronous-gated, or otherwise clocked detection.

---

# Resource necessity matrix — WP31

Current event-branch classification:

### Necessary for well-posedness / invariance

- finite normalized source-information task;
- complete accessible record/mark specification;
- autonomy or explicit accounting of clock/control resources.

### Exact structural timing obstruction

- mark-conditioned atomic timing mass.

### Quantitative timing resources

- finite `R2`: integrated spectral budget;
- finite local `Lambda`: microscopic sufficient bound with `R2<=Lambda`.

### Rejected as primitive universal timing resources

- deterministic latency/transit time;
- mean delay;
- RMS/FWHM jitter;
- RC `-3 dB` amplitude bandwidth;
- stationary EPR/activity without an absolute local rate scale.

### Not required for intrinsic upper speed bound

- dark/background events;
- downstream electronics;
- nontrivial optical capture theorem beyond trivial `C<=1`, unless a stronger sensitivity ceiling is desired.

### Extensivity

Parallel replication passes: total FI and incident FI scale together. If multiple primary registration routes exist for one capture, the relevant microscopic resource is their **total** local intensity.

Multiple independent pre-registration timing copies from one photon define a separate detector class unless explicitly modeled.

---

# Detector-class taxonomy

1. **Autonomous proper event/counter:** WP25–31 central stack.
2. **Actively synchronized event:** explicit clock/control resources; WP27.
3. **Continuous classical/Markov analog:** generic finite-frequency response/noise theory is close prior art; pursue only photodetection-specific additions.
4. **Coherent quantum pointer before irreversible registration:** WP7/WP8 separate apparatus/coupling/support theory.

A single scalar formula covering all classes without assumptions is not currently expected.

---

# Novelty posture

Do not claim novelty for Wiener theory, hazard functions, marked Poisson FI, Parseval, detector jitter metrics, synchronous detection, TUR/KUR/FRI theory, optical sum rules, or first-passage methods individually.

Targeted literature searches found FI-based IRF/jitter analyses, Poisson communication channels, random-delay estimation/channels, and classical hazard/Fisher-information literature, but no equivalent complete WP25–30 photodetection theorem stack has yet been located.

Equation-level comparison shows WP25 is not an obvious direct corollary of Dechant's 2026 finite-frequency FRI.

**Novelty remains provisional.**

---

# Immediate next actions

1. Finish theorem-level novelty audit, especially older first-passage/random-delay communication literature.
2. Build a compact theorem/counterexample manuscript skeleton and adversarially test every headline claim.
3. Decide whether non-Poisson/nonclassical source statistics are required for the first paper or can be deferred.
4. Keep detailed HgCdTe WP17–24 frozen.

---

# Recordkeeping

After every substantive theorem, counterexample, correction, or novelty result:

- create/update a dedicated note;
- add a numbered research-log checkpoint when direction changes;
- keep this file and `docs/CURRENT_RESEARCH_STATE.md` current;
- preserve failed conjectures.

Status vocabulary: **PROVED**, **VERIFIED**, **CONJECTURE**, **COUNTEREXAMPLE**, **OPEN**, **BLOCKED**, **REJECTED**.