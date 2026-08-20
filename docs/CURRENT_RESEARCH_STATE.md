# Current Research State

**Date:** 2026-08-20

This is the first-stop replacement-agent summary. **The repository, not chat history, is authoritative.**

## Read first

1. `AGENTS.md`
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

The detailed HgCdTe/Kane WP17–24 branch is **frozen** unless a core theorem explicitly needs it.

---

# 1. Central objective

Determine the smallest resource set that bounds source-normalized optical-to-electrical information acquisition for a precisely stated photodetector class, and prove necessity by counterexample whenever a proposed resource is omitted.

Core metric:

\[
\boxed{\eta_I=F_{\rm electrical}/F_{\rm incident}^{Q}.}
\]

The project no longer assumes one sensitivity-bandwidth-temperature product for all detector architectures.

---

# 2. Central conceptual distinction

\[
\boxed{\text{latency}\neq\text{amplitude bandwidth}\neq\text{information bandwidth}.}
\]

Known deterministic delay and invertible deterministic filtering do not by themselves reduce stationary FI. Information loss comes from unresolved timing structure, inaccessible/coarse-grained variables, downstream noise, finite observation/sampling, exact nulls, or explicitly bounded control/reference resources.

---

# 3. Autonomous proper event-detector theorem hierarchy

The most mature branch is now the **autonomous/time-translation-invariant proper marked-event detector** with weak coherent/Poisson optical modulation.

Every accessible autonomous event mark `M` must be retained.

## 3.1 WP30 — exact asymptotic atomic-timing theorem

Let the conditional registration-delay measure at mark `M=m` have atomic masses `p_j(m)`.

Then

\[
\boxed{
\lim_{\Omega\to\infty}\bar\eta_I(\Omega)
=
\eta_c\,\mathbb E_M\left[\sum_jp_j(M)^2\right]
}
\]

for the ideal signal-only marked event channel.

Consequences:

- purely non-atomic conditional delays imply asymptotic average information loss;
- deterministic/discrete delay branches leave an exact high-frequency information residue;
- if a mark reveals a deterministic branch, conditional timing can become atomic and high-frequency information can be restored.

This is the weakest structural timing statement currently identified.

## 3.2 WP26/WP28 — quantitative timing collision resource

When conditional delay densities are square-integrable, define

\[
\boxed{
\mathcal R_2
=2\,\mathbb E_M\int f(t|M)^2dt.
}
\]

For normalized source-information spectrum `w(omega)`, define

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

Fixed mean delay, RMS jitter, or FWHM jitter do **not** control `R2`; WP26 contains explicit smooth counterexamples.

Finite `R2` is sufficient for a quantitative integrated spectral budget but is not necessary for qualitative asymptotic decay.

## 3.3 WP25 — microscopic local-hazard completion

Let

\[
\boxed{
\Lambda
=\operatorname*{ess\,sup}_{M,t}h(t|M).
}
\]

Then

\[
\boxed{\mathcal R_2\le\Lambda}
\]

and therefore

\[
\boxed{
\bar\eta_I(\Omega)
\le C\min\left(1,\frac{\pi\Lambda}{2\Omega}\right).
}
\]

Constant-hazard exponential registration asymptotically saturates the high-bandwidth coefficient.

Microscopic sufficient forms:

\[
\boxed{\Lambda_{cl}=\max_x\sum_{y\in E_{reg}(x)}W_{yx}}
\]

for a classical Markov detector and

\[
\boxed{\Lambda_q=\left\|\sum_\alpha L_\alpha^\dagger L_\alpha\right\|_\infty}
\]

for quantum-jump registration.

Thus `Lambda` is the physically useful local rate/operator resource, not the mathematically weakest timing condition.

---

# 4. WP29 — thermodynamic no-go + conditional repair

For the reversible WP3 optical gateway

\[
0\xrightleftharpoons[d]{u}1,
\qquad f=u\pi_0\ge f_*,
\]

with total EPR `<=Sigma` and stationary activity `<=A`, define

\[
g(z)=\left(1-\frac1z\right)\ln z,
\qquad
Z_*=g^{-1}(\Sigma/f_*).
\]

WP3 proves

\[
\pi_1\ge\frac{f_*}{dZ_*}
\]

and therefore

\[
\boxed{
\lambda_1\le
\Lambda_*
=\frac{\mathcal A dZ_*}{f_*}.
}
\]

WP29 proves the new mark-robust bridge:

\[
\boxed{h_D(t|M)\le\lambda_1\le\Lambda_*}
\]

for any autonomous downstream delay/mark after the first gateway exit.

Hence

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

The arbitrary-source form is

\[
\boxed{
\bar\eta_I[w]
\le
C\mathcal W\!\left(
\pi\frac{\mathcal A d}{f_*}
 g^{-1}(\Sigma/f_*)
\right).
}
\]

### Complementary impossibility theorem

WP4 shows that temperature/detailed balance/EPR/activity/throughput alone do **not** bound the absolute local rate scale. Local microscopic rates can diverge in rare states while all listed stationary resources remain finite.

Therefore:

\[
\boxed{
\text{stationary thermodynamics alone}
\not\Rightarrow
\text{finite information bandwidth}.
}
\]

But in the restricted gateway class,

\[
\boxed{
\text{thermodynamic budgets}
+\text{absolute microscopic rate}
\Rightarrow
\Lambda_*
\Rightarrow
\text{finite information bandwidth}.
}
\]

This is currently the cleanest direct answer to the original thermodynamic UPRP question.

---

# 5. WP27 — free clock/control no-go

A source-synchronous detector with an unbounded external temporal reference can store arrival phase in a mark and report it arbitrarily slowly while retaining the incident timing FI.

Therefore WP25–WP31 require autonomy/time-translation invariance unless clock/control bandwidth, phase precision, memory, and control action are explicitly counted.

Do not apply the autonomous theorem silently to heterodyne, lock-in, gated, or externally clocked architectures.

---

# 6. Resource necessity matrix — WP31

### Necessary for well-posedness / invariant statement

- normalized finite source-information task;
- complete accessible record/mark specification;
- autonomous processing or explicit control/reference resources.

### Exact asymptotic obstruction

- mark-conditioned atomic timing mass.

### Quantitative timing resources

- `R2`: finite integrated timing spectrum;
- `Lambda`: microscopic local rate/operator sufficient condition, with `R2<=Lambda`.

### Rejected as primitive universal timing resources

- deterministic latency/transit time;
- mean delay;
- RMS/FWHM jitter;
- RC `-3 dB` amplitude bandwidth;
- stationary EPR/activity without an absolute local rate scale.

### Not required for intrinsic upper speed bound

- dark/background events;
- downstream electronics;
- nontrivial optical capture theorem beyond the trivial `C<=1`, unless a stronger sensitivity ceiling is desired.

### Parallel replication

Source-normalized performance passes extensivity: identical independent replication increases total incident and output FI by the same factor. Multiple primary routes must be bounded through their total local intensity.

### Multiple-event/gain caveat

Post-primary offspring are downstream processing. Multiple independent **pre-primary** timing records from one captured photon define a separate detector class unless their combined timing resource is modeled explicitly.

---

# 7. Novelty status

Targeted searches now include:

- first-passage/reliability/hazard theory;
- Poisson communication channels;
- random-delay communication and remote estimation;
- detector IRF/jitter literature;
- FI-based TCSPC/FLIM analysis;
- Dechant's 2026 finite-frequency FRI.

All ingredients are individually standard. FI-based FLIM work explicitly treats Poisson counts convolved with finite IRFs and background, but no equivalent theorem to the WP25–30 source-information/hazard/atomic-timing stack has yet been located.

An older Efron–Johnstone report titled *Fisher's Information in Terms of the Hazard Rate* exists, but it concerns statistical Fisher information of lifetime distributions; it is not currently identified as the same source-to-detector spectral transfer theorem.

Dechant's FRI gives a pointwise response/noise inequality and a different broadband response/static-variance integral; WP25 is not an obvious direct algebraic corollary.

**Novelty remains provisional.**

---

# 8. Frozen material branch

WP15–24 remain useful examples, but detailed HgCdTe/Kane work is frozen. Do not resume 6↔8-band downfolding, heavy-hole refinements, or detailed dark-current modeling unless a core theorem explicitly requires them.

---

# 9. Immediate next gates

1. Finish theorem-level novelty audit in older first-passage/random-delay channel literature.
2. Build a compact theorem/counterexample manuscript skeleton and adversarially test every headline claim.
3. Decide whether non-Poisson/nonclassical source statistics must be included in a first paper or can be deferred as a separate source-statistics branch.

**Latest durable checkpoint:** `notes/RESEARCH_LOG_ROUND11.md`.