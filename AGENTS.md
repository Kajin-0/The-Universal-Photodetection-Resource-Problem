# AGENTS.md

## Purpose
Durable handoff for **The Universal Photodetection Resource Problem (UPRP)**. The repository, not chat history, is authoritative.

Research is analytical/theoretical only. Numerical work is allowed for validation. Do not make experiments, fabrication, procurement, or laboratory campaigns necessary next steps.

## Working branch
`agent/uprp-core-theorem-round10`

## Read first
1. `docs/CURRENT_RESEARCH_STATE.md`
2. `notes/WP35_MARK_CONDITIONED_MARKOV_RATE_CORRECTION.md`
3. `docs/MANUSCRIPT_REV4_INTEGRATION_AUDIT.md`
4. `manuscript/event_resource_theorem_rev4.tex`
5. `manuscript/apply_rev5.py`
6. `notes/WP34_MINIMUM_TIMING_RESOURCE_COST_THEOREM.md`
7. `notes/WP32_GENERAL_MARKED_POISSON_EVENT_KERNEL_THEOREM.md`
8. `notes/WP33_EXACT_FIXED_MEAN_VARIANCE_JITTER_NO_GO.md`
9. `notes/WP29_THERMODYNAMIC_BRIDGE_TO_REGISTRATION_INTENSITY.md`
10. `notes/WP30_WIENER_ATOMIC_DELAY_INFORMATION_THEOREM.md`
11. `notes/WP31_EVENT_BRANCH_RESOURCE_NECESSITY_MATRIX.md`
12. `docs/NOVELTY_AUDIT_ROUND5_EVENT_THEOREM_STACK.md`

**Freeze:** detailed HgCdTe/Kane WP17–24, the coherent-pointer branch, analog-detector generalization, and non-Poisson/nonclassical extensions unless a referee-level defect in the first manuscript requires reopening them.

---

# Strategic state
The first-paper target is the **autonomous/time-translation-invariant, independent-event, one-primary-registration photodetection event channel** driven by weak coherent/Poisson direct-detection intensity modulation.

Do not describe it as a universal speed limit for every photodetector architecture.

Rev4 is a fully build-verified historical manuscript source. GitHub Actions verified deterministic Rev4 generation, LaTeX compilation, and artifact upload for commit `0acd8ca6304585e44c89130ca6b31826884c85a8`.

WP35 subsequently found one localized microscopic-rate wording defect in Rev4. The main event theorem, constants, WP34 inverse theorem, WP33 jitter no-go, Wiener result, and WP29 thermodynamic gateway theorem are unchanged.

`manuscript/apply_rev5.py` is the assertion-based editorial transformer from Rev4 to Rev5. It:

1. replaces the obsolete registration-edge/quantum-jump sentence with the WP35 total-escape-rate CTMC statement;
2. removes the generic quantum-jump claim from the first manuscript;
3. adds explicit prose callouts to both theorem figures;
4. switches the hierarchy graphic to the Rev5 wording `microscopic sufficient local-rate resource`.

The CI workflow now generates and compiles `event_resource_theorem_rev5.tex` and uploads its TeX/PDF artifacts.

---

# Exact marked-event theorem
Per incident photon,
\[
K(dm,d\tau)=\kappa(dm)\mu_m(d\tau),
\qquad
\eta=\kappa(\mathsf M)\le1.
\]

The kernel is independent of the small source parameter and translation-covariant in time. `M` is the complete accessible primary-event mark.

For weak sinusoidal Poisson intensity modulation,
\[
\boxed{
G(\omega)=\int_{\mathsf M}|H_m(\omega)|^2\kappa(dm).
}
\]

Parameter-independent background or downstream processing cannot increase source FI.

---

# Timing-resource hierarchy

## Atomic timing
If `p_j(m)` are atoms of the mark-conditioned delay law,
\[
\boxed{
\lim_{\Omega\to\infty}
\frac1{2\Omega}\int_{-\Omega}^{\Omega}G(\omega)d\omega
=
\int\kappa(dm)\sum_jp_j(m)^2.
}
\]
This is a flat-band **average** asymptotic. Do not claim pointwise Fourier decay for arbitrary non-atomic singular measures.

## Collision intensity
For square-integrable conditional delay densities,
\[
\boxed{
\mathfrak R_2=2\int\kappa(dm)\int f_m(t)^2dt,
}
\]
and Parseval gives
\[
\boxed{
\int_{-\infty}^{\infty}G(\omega)d\omega=\pi\mathfrak R_2.
}
\]
Therefore
\[
\boxed{
\bar\eta_I(\Omega)\le
\min\left[\eta,\frac{\pi\mathfrak R_2}{2\Omega}\right].
}
\]

## Capture-weighted local hazard capacity
If `h_m(t)<=Lambda(m)`, define
\[
\boxed{
\mathfrak H=\int\Lambda(m)\kappa(dm).
}
\]
Then
\[
\boxed{\mathfrak R_2\le\mathfrak H.}
\]

This capture-weighted quantity is the preferred microscopic sufficient rate resource. A global worst-case hazard is a stronger corollary, not the fundamental marked-channel primitive.

---

# WP34 inverse resource-cost theorem
For a flat two-sided task with ordinary-frequency half-band
\[
B=\frac{\Omega}{2\pi},
\]
a required absolute average transfer `q` implies
\[
\boxed{
q\le\eta,
\qquad
\mathfrak R_2\ge4Bq,
\qquad
\mathfrak H\ge4Bq.
}
\]

For a common markwise hazard ceiling,
\[
\boxed{\Lambda\ge\frac{4Bq}{\eta}.}
\]
For retention `q=r eta` relative to captured DC information,
\[
\boxed{\Lambda\ge4Br.}
\]

This is the cleanest operational headline equation currently supported.

---

# WP33 exact jitter no-go
For any prescribed `mu0>0` and `sigma^2>0`, a smooth two-exponential-plus-shift family can satisfy exactly
\[
\mathbb E D=\mu_0,
\qquad
\operatorname{Var}D=\sigma^2
\]
for every selected family member while `|H_D(omega)|^2 -> 1` uniformly on every prescribed finite band.

Therefore exact mean delay and exact RMS jitter do not bound information bandwidth.

Do not claim an arbitrary fixed-exact-FWHM theorem.

---

# WP35 Markov-rate correction
Rev4's generic statement that the maximum successful-registration edge intensity bounds the complete mark-conditioned delay hazard is false when registration competes with other exits.

For a finite-state CTMC define, for every pre-registration state,
\[
q_x=\sum_{y\ne x}W_{yx},
\qquad
q_{\max}=\max_{x\in S_{\rm pre}}q_x.
\]

Provided the accessible mark does not independently record the realized pre-registration holding times,
\[
\boxed{h_D(t\mid M)\le q_{\max}.}
\]

Example: competing exits `r` (success) and `R` (failure) give
\[
T\mid M=\text{success}\sim\mathrm{Exp}(r+R),
\]
so the conditional hazard is `r+R`, not `r`.

This does **not** damage the capture-weighted theorem. In the same example,
\[
P(M=\text{success})\Lambda(M=\text{success})
=\frac{r}{r+R}(r+R)=r.
\]

WP29 is already consistent because it uses the gateway's **total first-exit rate** `lambda1`.

The generic quantum-jump operator-norm sentence is intentionally removed from the first manuscript; a trajectory-level quantum completion is a separate future branch.

---

# External clock/control no-go
A free source-synchronous temporal reference can store arrival phase in a mark and report it after arbitrarily slow registration while preserving source timing FI.

Therefore autonomy is a genuine scope/resource assumption. Clocked/gated/heterodyne/lock-in architectures require explicit temporal-reference resources.

---

# Thermodynamic bridge
For the restricted finite-state, time-homogeneous reversible Markov optical gateway
\[
0\xrightleftharpoons[d]{u}1,
\qquad
f=u\pi_0\ge f_*,
\]
with total dimensionless steady EPR `<=Sigma` and stationary one-way activity `<=A`, define
\[
g(z)=(1-z^{-1})\ln z.
\]
Then
\[
\boxed{
\lambda_1\le
\Lambda_*
=\frac{\mathcal A d}{f_*}g^{-1}(\Sigma/f_*).
}
\]

Because `lambda1` is the total first-exit rate from the gateway state and the holding time is exponential and independent of exit destination,
\[
\boxed{h_D(t\mid M)\le\lambda_1.}
\]

Stationary EPR/activity/throughput alone do not supply an absolute time scale; the microscopic rate `d` is indispensable in this restricted bridge.

---

# Novelty posture
Do not claim first information-theoretic timing analysis, first IRF-information result, first sensitivity-bandwidth tradeoff, generic finite-frequency response/noise novelty, or an all-detector universal speed limit.

Defensible candidate contribution:

> A resource-completeness theorem for source-modulation information transfer in autonomous marked photodetection event channels, with exact atomic and collision-intensity timing resources, a capture-weighted local-hazard budget and inverse timing-resource cost, plus explicit no-go/repair results for low-order jitter moments, free synchronous control, and aggregate stationary thermodynamics.

Novelty is strongest in the **combined theorem/resource-completeness stack**, not in Poisson marking, Wiener theory, Parseval, or hazard calculus individually.

---

# Immediate next actions
1. Observe the Rev5 CI result and inspect any failure at the first fatal line.
2. Persist the generated Rev5 source after successful verification without reintroducing self-commit/issue-comment behavior into steady-state CI.
3. Perform one final claim/reference audit of Rev5.
4. Prepare a submission-ready source/package if that audit finds no substantive defect.
5. Do not reopen frozen research branches merely to enlarge the first paper.

Status vocabulary: **PROVED**, **VERIFIED**, **CONJECTURE**, **COUNTEREXAMPLE**, **OPEN**, **BLOCKED**, **REJECTED**.
