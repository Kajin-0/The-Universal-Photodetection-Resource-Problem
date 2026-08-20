# Current Research State

**Date:** 2026-08-20

This is the first-stop replacement-agent summary. **The repository, not chat history, is authoritative.**

## Read first
1. `AGENTS.md`
2. `notes/WP32_GENERAL_MARKED_POISSON_EVENT_KERNEL_THEOREM.md`
3. `notes/WP29_THERMODYNAMIC_BRIDGE_TO_REGISTRATION_INTENSITY.md`
4. `notes/WP30_WIENER_ATOMIC_DELAY_INFORMATION_THEOREM.md`
5. `notes/WP31_EVENT_BRANCH_RESOURCE_NECESSITY_MATRIX.md`
6. `notes/WP26_JITTER_MOMENT_NO_GO_AND_COLLISION_INTENSITY_RESOURCE.md`
7. `notes/WP27_SYNCHRONOUS_CONTROL_CLOCK_NO_GO.md`
8. `notes/WP28_ARBITRARY_SOURCE_SPECTRAL_CONCENTRATION_THEOREM.md`
9. `notes/RESEARCH_LOG_ROUND11.md`
10. `docs/ADVERSARIAL_REVIEW_EVENT_THEOREM_STACK.md`
11. `docs/NOVELTY_AUDIT_ROUND5_EVENT_THEOREM_STACK.md`
12. `docs/MANUSCRIPT_SKELETON_EVENT_RESOURCE_THEOREM.md`
13. `notes/WP4_MICROSCOPIC_OPTICAL_COUPLING_NO_GO.md`

Detailed HgCdTe/Kane WP17–24 is frozen.

---

# 1. Central objective
Determine the smallest physical resource set that bounds source-normalized optical-to-electrical temporal information transfer for a precisely defined photodetector class, and prove insufficiency by explicit counterexample when candidate resources are omitted.

Core metric:
\[
\boxed{\eta_I=F_{\rm electrical}/F_{\rm incident}^{Q}.}
\]

Central distinction:
\[
\boxed{\text{latency}\neq\text{amplitude bandwidth}\neq\text{information bandwidth}.}
\]

---

# 2. Mature detector class
The current mature theorem applies to an **autonomous/time-translation-invariant one-primary-event photodetection channel** in the weak coherent/Poisson direct-detection regime.

Every accessible autonomous primary-event mark is retained. Parameter-independent dark/background additions and downstream processing may be present but cannot increase FI.

Externally synchronized clocks/references and coherent continuous pointers are separate resource classes.

---

# 3. WP32 — general marked event kernel
Per incident photon:
\[
K(dm,d\tau)=\kappa(dm)\mu_m(d\tau),
\qquad
\eta=\kappa(\mathsf M)\le1.
\]

Conditional characteristic function:
\[
H_m(\omega)=\int e^{-i\omega\tau}d\mu_m(\tau).
\]

For weak sinusoidal intensity modulation, exact ideal primary-record normalized FI:
\[
\boxed{
G(\omega)=\int|H_m(\omega)|^2\kappa(dm).}
\]
Measured FI satisfies
\[
\eta_I^{\rm measured}(\omega)\le G(\omega).
\]

## Atomic asymptotic
If `p_j(m)` are the conditional delay atoms,
\[
\boxed{
\lim_{\Omega\to\infty}
\frac1{2\Omega}\int_{-\Omega}^{\Omega}G(\omega)d\omega
=
\int\kappa(dm)\sum_jp_j(m)^2.}
\]
Purely non-atomic mark-conditioned delay laws therefore force asymptotic average timing information to vanish.

## Absolute collision intensity
For square-integrable delay densities,
\[
\boxed{
\mathfrak R_2
=2\int\kappa(dm)\int f_m(t)^2dt.}
\]
Parseval gives
\[
\boxed{\int G(\omega)d\omega=\pi\mathfrak R_2.}
\]
Flat-band average:
\[
\boxed{
\bar\eta_I(\Omega)
\le
\min\left[\eta,\frac{\pi\mathfrak R_2}{2\Omega}\right].}
\]

For normalized source FI spectrum `w`, define
\[
\mathcal W(A)=\sup_{E:\,|E|\le A}\int_Ew(\omega)d\omega.
\]
Then
\[
\boxed{
\bar\eta_I[w]
\le
\eta\mathcal W\!\left(\frac{\pi\mathfrak R_2}{\eta}\right).}
\]

## Capture-weighted hazard capacity
If `h_m(t)<=Lambda(m)`, define
\[
\boxed{\mathfrak H=\int\Lambda(m)\kappa(dm).}
\]
Then
\[
\boxed{\mathfrak R_2\le\mathfrak H}
\]
and
\[
\boxed{
\bar\eta_I(\Omega)
\le
\min\left[\eta,\frac{\pi\mathfrak H}{2\Omega}\right].}
\]
A global worst-case hazard is a convenient stronger specialization, not the minimal marked-channel rate resource.

---

# 4. WP26 — conventional jitter no-go
A smooth fast-path / rare-slow-path registration mixture can keep mean/variance finite or fixed while approaching unit information transfer over every fixed finite band.

Therefore mean delay, RMS jitter, FWHM jitter, deterministic transit latency and ordinary `-3 dB` amplitude bandwidth are not resource-complete temporal-information variables.

---

# 5. WP27 — clock/control no-go
An unbounded source-synchronous temporal reference can encode arrival phase into an event mark and report it arbitrarily slowly while preserving the incident timing FI.

Thus the event theorem requires autonomy/time-translation invariance unless reference-clock bandwidth, phase precision, memory and control action are explicitly counted.

---

# 6. WP29 — thermodynamic no-go and conditional repair
For the reversible WP3 gateway
\[
0\xrightleftharpoons[d]{u}1,
\qquad f=u\pi_0\ge f_*,
\]
with total EPR `<=Sigma` and activity `<=A`, define
\[
g(z)=(1-z^{-1})\ln z,
\qquad
Z_*=g^{-1}(\Sigma/f_*).
\]
Then
\[
\pi_1\ge\frac{f_*}{dZ_*},
\qquad
\boxed{\lambda_1\le\Lambda_*={\mathcal A dZ_*}/{f_*}.}
\]
WP29 proves every autonomous downstream marked registration after first gateway exit satisfies
\[
\boxed{h_D(t|M)\le\lambda_1\le\Lambda_*}.
\]
Thus WP32/WP25 supplies a finite thermokinetic temporal-information ceiling.

WP4 provides the complementary impossibility theorem: bounded temperature, detailed-balance ratio, throughput, stationary activity and EPR do **not** bound the absolute microscopic local rate scale.

Current clean answer to original thermodynamic question:
\[
\boxed{\text{stationary thermodynamics alone}\not\Rightarrow\text{finite information bandwidth},}
\]
but in the restricted gateway class
\[
\boxed{\text{thermodynamic budgets}+\text{absolute microscopic rate scale}\Rightarrow\text{finite information bandwidth}.}
\]

---

# 7. Resource classification
Necessary for a well-posed/invariant event theorem:
- normalized source-information task;
- complete accessible primary-event mark;
- autonomy OR explicit clock/reference resources.

Exact high-band obstruction:
- mark-conditioned atomic timing mass.

Quantitative timing resources:
- `mathfrak R2`: exact integrated spectral budget;
- `mathfrak H`: capture-weighted local-hazard sufficient budget;
- uniform `Lambda`: convenient stronger microscopic specialization.

Rejected primitive resources:
- deterministic latency;
- mean delay;
- RMS/FWHM jitter;
- RC amplitude bandwidth;
- stationary EPR/activity without an absolute microscopic rate resource.

Not required for intrinsic upper speed bound:
- parameter-independent dark/background events;
- downstream electronics;
- nontrivial optical capture theorem beyond probability conservation unless stronger sensitivity bounds are desired.

Parallel replication is source-normalized extensive. Multiple independent pre-primary timing copies from one photon are a separate class/resource.

---

# 8. Novelty boundary
Closest prior art:
- Köllner & Wolfrum, *How many photons are necessary for fluorescence-lifetime measurements?* (1992), FI/CRLB photon requirements;
- Talaga, *Information-theoretical analysis of time-correlated single-photon counting measurements of single molecules* (2009), IRF convolution, information loss, detector sensitivity-bandwidth discussion and IRF power spectra;
- later FI/CRLB FLIM/TCSPC work;
- classical hazard/reliability, marked-Poisson/displacement, Wiener/Parseval, first-passage and finite-frequency response theory.

Talaga is especially important: the manuscript cannot claim the general idea that finite detector timing response reduces photon information.

Current potentially distinct contribution is the **resource-completeness theorem stack**:
1. exact marked source-modulation FI transfer;
2. exact atomic high-band residual;
3. quantitative collision/hazard spectral budgets;
4. conventional-jitter no-go;
5. free-clock/control no-go;
6. stationary-thermodynamics no-go and restricted thermokinetic repair.

No equivalent complete stack has been identified in targeted searches. Novelty remains provisional.

---

# 9. Publication state
- manuscript skeleton exists;
- hostile-referee review found no fatal mathematical contradiction under the stated autonomous independent-event assumptions;
- final broad literature audit did not identify a direct theorem collision;
- manuscript should be framed as **resource-completeness**, not invention of timing-information analysis.

## Immediate next step
Draft the first theorem manuscript using WP32 notation and conservative novelty claims. Defer non-Poisson/nonclassical source extension unless manuscript review demonstrates it is necessary.

**Latest durable checkpoint:** `notes/RESEARCH_LOG_ROUND11.md` plus WP32.