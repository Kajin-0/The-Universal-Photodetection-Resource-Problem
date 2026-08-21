# Current Research State

**Date:** 2026-08-21

Active branch: `agent/uprp-core-theorem-round10`

## Project-level status

The repository has two publication tracks:

1. **Paper 1 / Rev11:** scientifically frozen and technically validated for Physical Review Applied; only factual/personal submission metadata remain.
2. **Paper 2:** active theoretical program on arbitrary autonomous detector channels, high-flux hidden memory, Type-II recovery information singularities, and information-spectral resource structure.

The active scientific frontier is Paper 2.

## Read first

1. `AGENTS.md`
2. `paper2/AGENTS_PAPER2.md`
3. `paper2/notes/WP22_CONDITIONAL_SCORE_ATOM_THEOREM_AND_SELECTOR_COROLLARY.md`
4. `paper2/notes/WP21_HISTORICAL_INVERSE_OUTPUT_IDENTIFIABILITY_AUDIT.md`
5. `paper2/notes/RESEARCH_LOG_ROUND03_WP13_WP20_CHECKPOINT.md`
6. `paper2/notes/WP19_EXACT_VARIANCE_INSUFFICIENCY_COUNTEREXAMPLE.md`
7. `paper2/notes/WP18_LAPLACE_PROOF_REPAIR_FOR_RECOVERY_SINGULARITY.md`
8. `paper2/notes/WP17_PUBLICATION_GRADE_WP10_FORMALIZATION.md`
9. `paper2/notes/WP07_CONTINUOUS_PARALYZABLE_SPECTRAL_SURVIVAL.md`

Paper-1 submission files remain under `submission/` and `manuscript/`; do not infer the active frontier from them.

---

# Paper 1 — frozen Rev11

Preferred submission candidate: **Rev11**.

The first-paper class remains autonomous/time-translation-invariant, independent-event/low-overlap, one-primary-registration photodetection under weak coherent/Poisson direct-detection intensity modulation with complete accessible primary-event marks.

Core transfer:

`G(omega)=int |H_m(omega)|^2 kappa(dm)`.

Complete local weak-waveform Fisher operator:

`[F_out]_{ab}=Phi0/(2*pi) int G(omega)S_a*(omega)S_b(omega)domega`.

For one unresolved mark:

`B_FI=int_0^infty |H(2*pi*f)|^2df=B_ENBW`.

The ENBW identity is conventional prior art. Rev11 remains mechanically validated at 33 pages and should not be reopened absent a concrete defect or referee request.

---

# Paper 2 — active frontier

## 1. WP10/WP17 — general autonomous-channel Fisher spectrum

For homogeneous Poisson baseline flux `Phi0`,

`S_u=int u(t)[N(dt)-Phi0 dt]`.

For any parameter-independent detector channel with complete record `Y`,

`S_u^out=E[S_u|Y]`.

This induces a positive contraction `A_K` on scalar `L2(R)`. Autonomy/time-translation covariance implies `A_K` is a Fourier multiplier:

`F_out[u,v]=Phi0/(2*pi) int G_{Phi0,K}(omega)U*(omega)V(omega)domega`,

with `0<=G<=1` a.e.

WP17 closes the main formal proof gaps using standard-Borel trajectory spaces, kernel randomization, DQM under statistics, the classical translation-invariant `L2` multiplier theorem, and narrowband wavepacket limits.

Current status: proof architecture strong; novelty/positioning still under hostile audit.

## 2. WP07 — deterministic Type-II spectral survival

For deterministic paralyzable dead time `tau`, `rho=lambda*tau`, output rate `r=lambda exp(-rho)`.

At `rho=1`:

`G_1(0)=0`,

`G_1(omega)>0` for every `omega!=0`,

`lim_|omega|->infty G_1(omega)=1/e`.

At `omega=pi/tau`, analytic lower bound is `0.516975...`; exact complete-record Volterra numerics give about `0.52814`.

This remains the strongest concrete physical spectral theorem.

## 3. WP18 — generalized iid Type-II recovery Fisher singularity

For iid recovery duration `T` with mean `m`, all equal-mean recovery laws share the classical mean curve

`r(lambda)=lambda exp(-lambda m)`.

The classical busy-cycle renewal density is

`U_lambda(t)=lambda F(t)exp[-lambda A(t)]`,

`A(t)=E[min(T,t)]`.

These stochastic-process formulas are prior art.

Define static per-time retention `G_DC` separately from WP10's a.e.-defined spectral multiplier.

Under renewal DQM/window regularity,

`G_DC=(r/lambda)I_D`.

At `lambda*m=1`, all count/rate FI vanishes. WP18's bounded-Laplace-statistic proof gives

`G_DC=0 iff T=m almost surely`

under the stated regularity.

The quantitative witness includes

`G_DC >= (4/e) W_s^2/(1+u_s)^4`.

This theorem remains a candidate contribution, but generic output identifiability is classical and must not be used as novelty framing.

## 4. WP19 — exact mean/variance insufficiency no-go

Two recovery laws have identical

`E[T]=1`, `Var(T)=1/4`, `CV=0.5`,

and identical conventional curve `r(lambda)=lambda exp(-lambda)`, but different timestamp information channels.

A common interval coarse-graining has zero FI for one and normalized per-time FI `~0.00443520488427` for the other at `lambda=1`.

Converged full static values differ by about `8.78%`:

`G_DC^A~0.01765400847`,

`G_DC^B~0.01920433799`.

Thus mean + variance/CV + the complete conventional saturation curve are not resource-complete descriptors.

## 5. WP21 — historical inverse-output audit

The historical gate is **closed for manuscript strategy but unresolved for priority certification**.

Established:

- output-flow identifiability was an explicit queueing topic by at least 1965;
- Kovalenko (1965) is described in later Soviet inverse-problem literature as recovering Poisson input rate and service-time distribution from an `M/G/1` output process, with `M/M/1` exceptional;
- Kendall & Lewis, Ivnitskii, Brown, Ross, George & Agrawal, Shanbhag and others occupy adjacent inverse-output territory;
- by 1982 a queueing textbook had a dedicated section on recovering system characteristics from output-flow observations;
- Afanaseva & Mikhailova (1973) is a direct Type-II-lineage blocker whose readable theorem text has not been located.

Therefore do not claim generic identifiability, output reconstruction, or the broad existence of exceptional information-degenerate service laws as new.

No verified predecessor has yet been found for the narrow WP18 static Fisher singularity at the universal Type-II count maximum.

Further historical searching is low priority unless the inaccessible Type-II theorem text becomes realistically obtainable.

## 6. WP22 — conditional-score covariance-atom theorem; supersedes WP20 for manuscript wording

WP22 repairs an overbroad implication in WP20.

### Abstract theorem

Let the complete output score admit a centered stationary random measure `M` with covariance measure

`Gamma_M=a delta_0+nu`,

where `nu` has finite total variation and `nu({0})=0`.

Then

`lambda G(omega)=a+nu_hat(omega)`

in this regularity class, and for every fixed `0<a0<b0`,

`lim_{Omega->infty} 1/[(b0-a0)Omega] int_{a0Omega}^{b0Omega}G(omega)domega = a/lambda`.

Thus the robust high-frequency invariant is

**zero-lag conditional-score covariance atom / incident rate**.

If `nu` is atomless, Wiener gives high-frequency mean-square convergence. If `nu` is Rajchman, e.g. an `L1` covariance density, pointwise convergence follows.

### Regular exact-timestamp-selector corollary

For a stationary simple selector `Y<=N` of visible rate `r`, if the conditional hidden-event mean is diffuse,

`E[H(dt)|Y]=m_Y(t)dt`,

and the posterior field has ordinary Palm/second-order regularity, then

`M(dt)=Y(dt)-r dt+xi_Y(t)dt`.

The simple-point-process term contributes `r delta_0`; distinct-event covariance has no zero-lag atom; point-field cross terms are absolutely continuous in lag by Campbell/Palm reduction; and diffuse-field covariance is also absolutely continuous. Therefore

`Gamma_M({0})=r`,

and under finite-TV correction regularity the Cesaro residue is

`r/lambda`.

### Important withdrawal

The statement

`Y<=N alone => high-frequency residue r/lambda`

is **not justified** and must not be used.

A sufficiently pathological history-dependent selector may encode hidden continuous event-time information nonlocally into the observed record, making the posterior hidden-event conditional measure singular. The universal residue is then `a/lambda`, where `a=Gamma_M({0})`, not necessarily `r/lambda`.

WP22 is now the preferred theorem; WP20 is an intermediate derivation.

A useful finite-band convergence bound is

`|Gbar_Omega-a/lambda| <= lambda^{-1}[|nu|((-delta,delta))+2||nu||_TV/((b0-a0)Omega delta)]`.

All stationary-random-measure, Palm, Fourier-Stieltjes, Wiener, and Rajchman ingredients are standard. Novelty is uncertified.

---

# Current novelty hierarchy

1. **WP10/WP17:** arbitrary-autonomous-channel local Fisher spectrum as a photodetection-channel synthesis.
2. **WP07:** deterministic Type-II static blindness with positive FI at every nonzero temporal frequency and high-frequency residue `1/e`.
3. **WP18:** deterministic recovery as the unique regular static Fisher-singular fixed-mean iid Type-II recovery law at the common mean-rate maximum.
4. **WP22:** conditional-score covariance-atom/Cesaro residue theorem plus regular exact-timestamp-selector corollary.
5. **WP19:** rigorous resource no-go showing recovery mean and variance are insufficient.

Supporting only: WP20 derivation, WP14 witness, rate-vs-shape decomposition, branch aliasing, WP15 pair inversion.

Do not claim novelty for standard conditional-score projection, Fisher data processing, function-valued score/Fisher kernels, Fourier multipliers, point-process covariance/spectral measures, Campbell/Palm formulas, Wiener/Rajchman theory, dead-time counting theory, random Type-II busy-cycle formulas, pair-correlation identities, or generic queue-output identifiability.

---

# Immediate next gates

1. **Targeted novelty audit of WP22** against dependent thinning, missing-event point-process inference, point-process filtering/innovation theory, functional score spectra, neural spike-train FI, and photodetection dead-time information theory.
2. Search for any prior theorem explicitly equating a high-frequency Fisher/score-spectrum residue with the zero-lag **conditional-score covariance atom**.
3. Recheck WP18 renewal-DQM and window-censoring assumptions for atomic and heavy-tailed recovery laws.
4. Then decide whether the combined WP10/WP07/WP18/WP22/WP19 stack has earned Paper-2 manuscript drafting.

---

# Documentation requirement

Material theorem results, proof repairs, prior-art collisions, numerical results used in arguments, and changes in next-gate decisions must be committed as they occur. Do not allow important project state to exist only in chat.

Keep synchronized at minimum:

- relevant `paper2/notes/WP*.md` / research logs;
- `paper2/AGENTS_PAPER2.md` when recovery order/claims/gates change;
- this file when project-level status changes.
