# AGENTS.md

## Purpose
Durable handoff for **The Universal Photodetection Resource Problem (UPRP)**. The repository, not chat history, is authoritative.

Research is analytical/theoretical only. Numerical work is allowed for validation. Do not make experiments, fabrication, procurement, or laboratory campaigns necessary next steps.

## Read first
1. `docs/CURRENT_RESEARCH_STATE.md`
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
14. earlier WP0–WP24 only as needed.

**Freeze:** detailed HgCdTe/Kane WP17–24 unless a core theorem explicitly requires material validation.

---

# Strategic state
The mature core is the **autonomous proper event/counter detector** branch. The project is no longer seeking one scalar sensitivity-bandwidth-temperature law valid for every detector architecture.

Core metric:
\[
\boxed{\eta_I=F_{\rm electrical}/F_{\rm incident}^{Q}}.
\]

Critical distinction:
\[
\boxed{\text{latency}\neq\text{amplitude bandwidth}\neq\text{information bandwidth}.}
\]
Known deterministic delay and invertible deterministic filtering do not by themselves reduce stationary FI.

---

# Strongest event-channel formulation — WP32
For each incident signal photon, use the autonomous marked subprobability kernel
\[
K(dm,d\tau)=\kappa(dm)\mu_m(d\tau),
\]
where `m` is the complete accessible primary-event mark, `tau>=0` is registration delay, and
\[
\eta=\kappa(\mathsf M)\le1
\]
is total primary-event probability.

Define
\[
H_m(\omega)=\int e^{-i\omega\tau}\,d\mu_m(\tau).
\]
For weak coherent/Poisson sinusoidal intensity modulation, the exact ideal primary-record source-normalized FI is
\[
\boxed{G(\omega)=\int |H_m(\omega)|^2\kappa(dm).}
\]
Any parameter-independent background or downstream processing obeys
\[
\eta_I^{\rm measured}(\omega)\le G(\omega).
\]

## Exact asymptotic timing obstruction — WP30/WP32
If `p_j(m)` are the atomic masses of `mu_m`, Wiener theory gives
\[
\boxed{
\lim_{\Omega\to\infty}\frac1{2\Omega}\int_{-\Omega}^{\Omega}G(\omega)d\omega
=\int\kappa(dm)\sum_jp_j(m)^2.}
\]
Thus mark-conditioned deterministic/discrete timing atoms are the exact high-band residual; purely non-atomic conditional delays force the flat-band average to zero.

## Quantitative timing-collision resource
If conditional delays have square-integrable densities `f_m`, define the **absolute captured collision intensity**
\[
\boxed{
\mathfrak R_2=2\int\kappa(dm)\int f_m(t)^2dt.}
\]
Then
\[
\boxed{\int_{-\infty}^{\infty}G(\omega)d\omega=\pi\mathfrak R_2}
\]
and for flat band
\[
\boxed{\bar\eta_I(\Omega)\le\min\left[\eta,\frac{\pi\mathfrak R_2}{2\Omega}\right].}
\]

For normalized source spectral FI `w(omega)`, define
\[
\mathcal W(A)=\sup_{E:\,|E|\le A}\int_Ew(\omega)d\omega.
\]
Then, for `eta>0`,
\[
\boxed{
\bar\eta_I[w]
\le\eta\,\mathcal W\!\left(\frac{\pi\mathfrak R_2}{\eta}\right).}
\]

## Capture-weighted local hazard resource
If mark-conditioned hazard satisfies
\[
h_m(t)\le\Lambda(m),
\]
define
\[
\boxed{\mathfrak H=\int\Lambda(m)\kappa(dm).}
\]
Then
\[
\boxed{\mathfrak R_2\le\mathfrak H}
\]
and hence
\[
\boxed{\bar\eta_I(\Omega)\le\min\left[\eta,\frac{\pi\mathfrak H}{2\Omega}\right].}
\]
A uniform worst-case `Lambda` is a convenient stronger specialization, **not the minimal marked-channel rate resource**.

Microscopic uniform sufficient forms remain useful:
\[
\Lambda_{cl}=\max_x\sum_{y\in E_{reg}(x)}W_{yx},
\]
\[
\Lambda_q=\left\|\sum_\alpha L_\alpha^\dagger L_\alpha\right\|_\infty.
\]

---

# Conventional jitter no-go — WP26
A smooth fast-path/rare-slow-path mixture can keep finite/fixed variance while its prompt component becomes arbitrarily fast. Thus mean latency, RMS jitter, FWHM jitter, deterministic transit time, and ordinary `-3 dB` amplitude bandwidth are not resource-complete information-bandwidth variables.

---

# Free clock/control no-go — WP27
A free source-synchronous clock can encode arrival phase into an event mark and report it arbitrarily slowly while preserving incident timing FI.

Therefore WP25–32 apply to **autonomous/time-translation-invariant event detectors** unless clock/control bandwidth, phase precision, memory/reference resources and control action are explicitly counted.

---

# Thermodynamic bridge — WP29
Restricted reversible optical gateway:
\[
0\xrightleftharpoons[d]{u}1,
\qquad f=u\pi_0\ge f_*.
\]
With total EPR `<=Sigma` and stationary activity `<=A`, define
\[
g(z)=(1-z^{-1})\ln z,
\qquad Z_*=g^{-1}(\Sigma/f_*).
\]
WP3 proves
\[
\pi_1\ge\frac{f_*}{dZ_*},
\qquad
\boxed{\lambda_1\le\Lambda_*={\mathcal A dZ_*}/{f_*}.}
\]
WP29 proves any autonomous downstream marked registration after the first gateway exit obeys
\[
\boxed{h_D(t|M)\le\lambda_1\le\Lambda_*}.
\]
Therefore the event theorem yields a finite thermokinetic information-bandwidth ceiling.

### Complementary no-go
WP4 proves temperature/detailed balance/EPR/activity/throughput alone do **not** bound the absolute microscopic rate scale. Rare-fast states can keep stationary resources bounded while local rates diverge.

Clean original-question answer:
\[
\boxed{\text{stationary thermodynamics alone}\not\Rightarrow\text{finite information bandwidth},}
\]
but, in the restricted gateway class,
\[
\boxed{\text{thermodynamic budgets}+\text{absolute microscopic rate scale}\Rightarrow\text{finite bandwidth}.}
\]

---

# Resource necessity matrix
Necessary for a well-posed invariant event theorem:
- normalized finite source-information task;
- complete accessible primary-event mark specification;
- autonomy OR explicit temporal-reference/control resources.

Exact asymptotic timing obstruction:
- mark-conditioned atomic timing mass.

Quantitative timing resources:
- `mathfrak R2`: integrated timing spectrum;
- `mathfrak H`: capture-weighted local hazard sufficient resource;
- uniform `Lambda`: convenient stronger specialization.

Rejected as primitive universal resources:
- deterministic latency/transit time;
- mean delay;
- RMS/FWHM jitter;
- RC `-3 dB` amplitude bandwidth;
- stationary EPR/activity without an absolute rate resource.

Not required for intrinsic upper speed bound:
- parameter-independent dark/background events;
- downstream electronics;
- nontrivial optical capture theorem beyond `eta<=1`, unless a stronger sensitivity ceiling is desired.

Parallel replication passes source-normalized extensivity. Multiple independent **pre-primary** timing copies from one photon define a separate resource/class.

---

# Detector-class taxonomy
1. **Autonomous proper event/counter:** WP25–32 mature theorem stack.
2. **Actively synchronized event:** explicit clock/control/reference resources; WP27.
3. **Continuous classical/Markov analog:** generic finite-frequency response/noise bounds are close prior art; pursue only distinct additions.
4. **Coherent quantum pointer before irreversible registration:** separate WP7/WP8 apparatus/coupling/support theory.

Do not claim one formula covers all four.

---

# Novelty posture
Closest prior art now explicitly includes:
- Köllner & Wolfrum (1992), FI/CRLB photon requirements for fluorescence lifetime;
- Talaga (2009), information-theoretical TCSPC analysis with IRF convolution, information loss, sensitivity-bandwidth discussion and IRF power spectra;
- later FLIM/TCSPC FI/CRLB work;
- classical hazard/reliability theory;
- Wiener theorem;
- Poisson displacement/marking theory;
- Dechant 2026 finite-frequency FRI.

Do **not** claim novelty for “timing response limits information,” Fisher+hazard, IRF convolution, Wiener/Parseval, marked-Poisson FI, or detector jitter theory.

Current defensible candidate contribution:
> a photodetection-specific **resource-completeness theorem stack**: exact source-modulation FI for autonomous marked event channels; exact atomic timing residual; quantitative collision/hazard spectral budgets; conventional-jitter and free-clock no-go results; and a thermodynamic no-go/conditional-repair theorem.

No equivalent complete stack has been identified in targeted searches. Novelty remains provisional.

---

# Publication state
- `docs/MANUSCRIPT_SKELETON_EVENT_RESOURCE_THEOREM.md`
- `docs/ADVERSARIAL_REVIEW_EVENT_THEOREM_STACK.md`
- `docs/NOVELTY_AUDIT_ROUND5_EVENT_THEOREM_STACK.md`

Hostile review found no fatal mathematical contradiction under stated low-overlap/autonomous assumptions. Main risks: novelty compression and scope, not an identified theorem error.

## Immediate next action
Begin a carefully scoped first manuscript using **WP32 notation** and conservative novelty framing. Defer non-Poisson/nonclassical source extension unless manuscript review proves it necessary.

Do not reopen HgCdTe WP17–24.