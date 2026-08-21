# AGENTS — Paper 2 General-Channel Program

## Scope

Durable handoff for the **second paper** in The Universal Photodetection Resource Problem repository.

Paper 1 / Rev11 is scientifically frozen by default. Do not alter it while working on Paper 2 unless a concrete Paper-1 defect is identified.

Research remains analytical/theoretical. Numerical work may validate derivations or analyze published data. Do not make new experiments, fabrication, procurement, or laboratory campaigns required next steps.

Active repository branch: `agent/uprp-core-theorem-round10`.

## Read first — current order

1. `paper2/notes/WP17_PUBLICATION_GRADE_WP10_FORMALIZATION.md`
2. `paper2/notes/WP16_HOSTILE_RANDOM_TYPEII_PRIOR_ART_AUDIT.md`
3. `paper2/notes/WP13_RENEWAL_FISHER_DECOMPOSITION_AND_RECOVERY_UNIQUENESS.md`
4. `paper2/notes/WP14_RECOVERY_SHAPE_FISHER_WITNESS.md`
5. `paper2/notes/WP15_PAIR_CORRELATION_RATE_IDENTIFIABILITY.md` — **read with WP16; its pair-correlation identity is prior art**
6. `paper2/notes/WP10_GENERAL_AUTONOMOUS_CHANNEL_THEOREM_HARDENED.md`
7. `paper2/notes/WP07_CONTINUOUS_PARALYZABLE_SPECTRAL_SURVIVAL.md`
8. `paper2/notes/WP08_VISIBLE_EVENT_HIGH_FREQUENCY_RESIDUE.md` — provisional
9. `paper2/notes/WP09_TYPEII_AND_FISHER_OPERATOR_PRIOR_ART_AUDIT.md`
10. `paper2/notes/WP06_CLOSED_FORM_HIGH_PASS_THEOREM.md`
11. `paper2/notes/WP11_GLOBAL_STATIC_NONIDENTIFIABILITY_PARALYZABLE.md`
12. `paper2/notes/WP12_RANDOM_RECOVERY_BREAKS_STATIC_FISHER_ZERO.md`
13. `paper2/README.md`

## Central theorem candidate — proof architecture now publication-grade

For a stationary Poisson source of baseline flux `Phi0`, use primitive tangents

`u in C_c^infty(R)`

and

`lambda_epsilon(t)=Phi0[1+epsilon u(t)]`.

The source score is

`S_u = int u(t)[N(dt)-Phi0 dt]`,

with

`E[S_u S_v]=Phi0 <u,v>_{L2}`.

For any parameter-independent stochastic detector channel `K`, with complete accessible record `Y`,

`S_u^out=E[S_u|Y]`.

WP17 closes the stochastic-kernel DQM gap rigorously:

1. take the incident configuration space as the standard Polish space of locally finite counting measures on `R` with vague topology;
2. require only that the output record space is standard Borel with a measurable time-shift action;
3. use Kallenberg's kernel-randomization lemma to realize `K` as a measurable function of `(N,Z)` with one independent `Z~Unif[0,1]`;
4. the enlarged experiment has the same score `S_u(N)`;
5. Pollard's DQM-under-statistics theorem gives `S_u^out=E[S_u|Y]` exactly.

This induces a unique positive contraction `A_K` on scalar `L2(R)`:

`F_out[u,v]=Phi0 <u,A_K v>`, `0<=A_K<=I`.

Autonomy/time-translation covariance gives exact commutation with waveform translations. Stein's classical `L2` translation-invariant-operator theorem then yields a Fourier multiplier:

`F_out[u,v] = Phi0/(2*pi) int G_{Phi0,K}(omega) U*(omega)V(omega)domega`,

with

`0<=G_{Phi0,K}(omega)<=1` a.e.,

and `G(-omega)=G(omega)` a.e.

No independent-event delay kernel, finite detector state, low-flux approximation, one-output-per-photon assumption, renewal property, or causal-state reconstructibility is required.

The detector may contain arbitrary dead time, saturation, recovery, afterpulsing, hidden-state memory, state-dependent capture, multiple output events, analog marks, and high-flux nonlinear history dependence.

Long sinusoidal performance is a narrowband wavepacket/Lebesgue-point corollary. Pure infinite sinusoids are not primitive admissible `L2` tangents.

Paper 1 is recovered exactly as the marked-Poisson special case:

`G(omega)=int |H_m(omega)|^2 kappa(dm)`.

Candidate conceptual message:

> **Spectral completeness is symmetry-driven, not independent-event-driven.**

The conditional-score identity, Fisher monotonicity, kernel randomization, function-valued Fisher operators, Riesz representation, translation-invariant multiplier theorem, and approximate-identity arguments are standard and must not be claimed as new.

## Exact discrete hidden-memory theorem

One-bin Type-II detector:

`Y_n=X_n(1-X_{n-1})`, `X_n~Bernoulli(p_n)`.

At `p=1/2`, let `x=1-cos(omega)`. The complete local Fisher spectrum is

`G(omega)=1-1/(2x)+ln(1+4x)/(8x^2)`, with `G(0)=0`.

It is strictly increasing for `0<omega<pi` and

`G(pi)=3/4+ln(3)/16=0.818663268...`.

This is an exact saturation-induced information-high-pass theorem.

## Continuous deterministic Type-II theorem — strongest physical spectral result

Poisson rate `lambda`, deterministic paralyzable dead time `tau`, `rho=lambda*tau`.

Recorded timestamps are renewal cluster starts with

`r=lambda exp(-rho)`.

At the classical paralysis maximum `rho=1`,

`G_1(0)=0`.

For `y=omega*tau`,

`M_rho(y)=1-rho(1-exp(-iy))/(iy)`.

A single optimally phased Fourier statistic gives

`G_rho(omega)>=exp(-rho)|M_rho(y)|^2/[1-2 rho exp(-rho) sin(y)/y]`.

At `rho=1`, this is positive for every `omega!=0`, and

`G_1(pi/tau)>=exp(-1)(1+4/pi^2)=0.516975...`.

The exact complete-record renewal score gives

`lim_|omega|->infty G_rho(omega)=exp(-rho)`.

Hence at paralysis:

`G_1(0)=0`, `G_1(omega)>0` for every nonzero frequency, `G_1(infty)=1/e`.

Independent Volterra numerics give

`G_1(pi/tau) ~ 0.52814`,

with the spectrum peaking near `omega*tau~3.3` and oscillating toward `1/e`.

## General iid Type-II recovery — strongest current class-wide physical theorem candidate

Every incident Poisson event starts an iid recovery interval `T` of fixed distribution `F` and finite mean

`m=E[T]`.

The detector is dead whenever at least one event-generated interval remains active. Registered events are starts of `M/G/infinity` busy clusters.

Classical counter/queueing theory gives the universal mean output curve

`r(lambda)=lambda exp(-lambda m)`

for every recovery law of the same mean.

It also gives the busy-cycle renewal density

`U_lambda(t)=lambda F(t) exp[-lambda A(t)]`,

where

`A(t)=E[min(T,t)]`.

**WP16 establishes that this formula is classical prior art and must not be claimed.**

For a fractional source-rate tangent, the renewal-output Fisher rate is

`Fdot_out=r I_D`,

so

`G(0)=(r/lambda) I_D`.

The interval score decomposes orthogonally into rate and shape components:

`I_D=dot(mu)^2/sigma_D^2 + I_shape`,

and therefore

`G(0)=G_rate+G_shape`,

with

`G_rate=lambda [r'(lambda)]^2/[r^3 sigma_D^2]`.

At the common paralysis maximum

`lambda*m=1`,

`r'(lambda)=0`, hence all surviving static information is interval-shape information.

Differentiating the classical renewal density gives

`dot U_*(t)=U_*(t)[1-A(t)/m]`.

Using `m-A(t)=E[(T-t)_+]` gives the current class-wide theorem candidate:

`G_*(0)=0  iff  T=m almost surely`,

under the stated renewal DQM regularity.

Thus deterministic recovery is the unique fixed-mean iid Type-II law that is completely DC Fisher-blind at the common mean-rate maximum.

### Global branch-aliasing uniqueness

For two distinct incident rates satisfying

`lambda_1 exp(-lambda_1 m)=lambda_2 exp(-lambda_2 m)`,

identical complete stationary registered-timestamp laws imply

`A(t)=m` wherever `F(t)>0`, which forces `T=m` a.s.

Conversely deterministic recovery gives the usual complete Lambert-W branch aliasing.

Therefore, for fixed known recovery law:

`distinct equal-output-rate branches give identical complete timestamp experiments iff T is deterministic`.

No exact historical statement of these two **iff** information/identifiability characterizations has yet been found. No priority claim is certified.

## Quantitative recovery-shape Fisher witness

At `lambda*m=1`, define

`g(t)=1-A(t)/m=E[(T-t)_+]/m`.

For `s>0`,

`u_s=int exp(-s t) U_*(t) dt`,

`W_s=int exp(-s t) U_*(t) g(t) dt`.

A single bounded interval statistic `exp(-sD)` gives

`G_*(0)>=e^{-1} W_s^2 / [(1+u_s)^4 (phi_{2s}-phi_s^2)]`,

and the simpler rigorous bound

`G_*(0)>=(4/e) W_s^2/(1+u_s)^4`.

`W_s=0` for all `s>0` iff recovery is deterministic; `W_s>0` for every `s>0` for any genuinely nondegenerate recovery law.

Therefore deterministic recovery is the unique zero/minimizer of complete-record DC FI under fixed mean, within the regular iid-recovery Type-II class.

Do not paraphrase this as “noise helps.” It is symmetry breaking at the common paralysis maximum.

## Numerical calibration

At mean recovery `m=1` and the common maximum `lambda=1`:

### Exponential recovery

Converged Volterra result:

`I_D ~ 0.18798493`,

`G_exp(0) ~ 0.06915579`.

Fine stored grid:

`G_exp(0)=0.06915576364565855`,

interval mass `0.9999998146`,

mean interval `2.7182749269 ~ e`.

### Mean-one gamma recovery family

| shape k | CV | G(0) |
|---:|---:|---:|
| 0.5 | 1.4142 | 0.10843945 |
| 1 | 1.0000 | 0.06915542 |
| 2 | 0.7071 | 0.03534347 |
| 4 | 0.5000 | 0.01412083 |
| 8 | 0.3536 | 0.00474035 |
| 16 | 0.2500 | 0.00147512 |
| 32 | 0.1768 | 0.000454385 |
| 64 | 0.1250 | 0.000142552 |

This monotonicity is **gamma-family-specific numerical evidence only**. No universal variance ordering is proved.

The handoff-only gamma-vs-lognormal same-CV comparison is **not currently durable in the repository** and must not be treated as verified until reproduced and committed.

## Pair correlation — major WP16 prior-art correction

WP15 derived

`g_Y^(2)(t)=F(t) exp[lambda E[(T-t)_+]]`.

WP16 found that this exact identity is already contained in the random-paralyzable photon-correlation theory of Apanasovich & Paltsev, JOSA B 12, 1550–1554 (1995), DOI `10.1364/JOSAB.12.001550`. Their second-order product-density formula, specialized to stationary Poisson input and normalized by `r^2`, gives exactly the WP15 expression.

Therefore **do not claim novelty for the pair-correlation identity**.

The rearrangement

`lambda=ln[g_Y^(2)(t)/F(t)] / E[(T-t)_+]`

at a lag where both factors are nonzero remains a useful operational corollary, but because it follows algebraically from an old formula it should not be a lead novelty theorem.

Larsen & Kostinski (2009) independently establish pair-correlation dead-time correction/inversion as prior art.

## Visible-event high-frequency residue — still provisional

For an autonomous exact-timestamp selector `Y<=N`, input rate `lambda`, output rate `r`, under explicit diffuse-posterior and integrable short-memory covariance assumptions,

`lim_|omega|->infty G(omega)=r/lambda`.

Checks:

- independent exact-timestamp thinning: `G=eta=r/lambda`;
- nonparalyzable dead time: flat `G=r/lambda=1/(1+lambda tau)`;
- deterministic paralyzable dead time: `G(infty)=r/lambda=exp(-rho)`.

Treat WP08 as provisional. Autonomy alone does **not** imply the present mixing hypotheses.

## Hostile novelty state after WP16

Classical / must be credited:

- generalized random Type-II/paralyzable recovery;
- `M/G/infinity` representation and busy-cycle theory;
- `U_lambda(t)=lambda F(t)exp[-lambda A(t)]`;
- random-paralyzable pair-correlation formulas, including the normalized WP15 identity;
- pair-correlation dead-time inversion in general;
- hidden service/recovery-distribution inference in `M/G/infinity` systems;
- renewal FI and count-vs-interval-shape FI ideas;
- score projection / Fisher data processing / translation-invariant multiplier mathematics;
- dead-time information theory generally;
- modulated paralyzable photocounting generally.

### Critical unresolved historical blocker

Afanaseva & Mikhailova (1973), approximately **“On recovering characteristics of some queueing systems from the output flow,”** is cited in the classical Type-II literature. A readable full text was not located in WP16.

Because its title directly concerns inverse recovery from output flow, it must be checked before any priority language for the deterministic full-law uniqueness theorem.

Absence of online full text is not evidence of novelty.

## Current novelty hierarchy

### Strongest organizing candidate

1. **WP10/WP17 general autonomous-channel Fisher-spectrum theorem** as a photodetection-channel synthesis, with arbitrary hidden detector memory/high-flux dynamics and exact pointwise local Fisher ordering/data processing.

### Strong physical theorem candidates

2. **WP07 continuous deterministic Type-II spectral survival**:
   `G_1(0)=0`, every nonzero frequency positive, `G_1(infty)=1/e`.
3. **WP13 deterministic-recovery information singularity in the iid Type-II class**:
   `G_*(0)=0 iff T deterministic`, plus full-law branch-aliasing iff deterministic.

### Supporting results, not lead novelty claims

4. rate-versus-shape Fisher decomposition;
5. `W_s` recovery-shape witness;
6. pair-correlation inversion/interpretation.

## Mandatory novelty boundaries

Do **not** claim:

- first conditional-score / Fisher data-processing theorem;
- first Fisher operator for function-valued parameters;
- first translation-invariant Fourier-multiplier representation in mathematics;
- first dead-time FI or dead-time information theory;
- first modulated paralyzable photon counting;
- first random Type-II / `M/G/infinity` model;
- novelty of the classical busy-cycle renewal density;
- novelty of the random-paralyzable pair-correlation identity;
- first pair-correlation dead-time inversion;
- generic Blackwell dominance;
- a theorem for nonclassical optical states;
- a universal scalar speed limit for every photodetector.

Close literature includes Teich & Vannucci (1978), Teich & Cantor (1978), Dvurecenskij & Ososkov (1984), Apanasovich & Paltsev (1995), Larsen & Kostinski (2009), Mandalapu & Jagannathan (2021), Jorgensen & Johnson (2026), Clark (2026), and classical Takacs/Pyke `M/G/infinity` work.

## Current research thesis

> Temporal Fisher transfer for an autonomous detector is a property of its complete trajectory channel, not of a scalar timing width or saturation curve. Time-translation symmetry yields a complete local Fisher spectrum even with arbitrary detector memory; hidden Type-II dynamics can erase a static tangent while retaining dynamic information; and within generalized iid Type-II recovery, deterministic recovery is an information-singular boundary despite all equal-mean recovery laws sharing the same conventional paralysis curve.

This remains materially broader than Paper 1 if the remaining novelty audit survives.

## Next decisive gates

1. **Finish historical inverse-output audit**, especially Afanaseva–Mikhailova (1973), before assigning novelty confidence to WP13's full-law uniqueness result.
2. Independently scrutinize the DQM regularity step in WP13's implication `G(0)=0 -> dot U=0`, including boundary/censoring conditions for the stationary renewal experiment.
3. Decide whether to prove a rigorous **variance-insufficiency no-go** with a durable same-mean/same-variance counterexample. If no clean theorem emerges quickly, drop the branch.
4. Harden WP08 or replace it with a weaker Cesaro/Wiener high-frequency residue theorem under weaker assumptions.
5. Only after these gates decide whether Paper 2 has earned manuscript drafting.

## Breakthrough criterion

Proceed to a manuscript only if the combined stack survives hostile review:

- WP10/WP17 is not merely standard stationary-channel statistics in photodetection notation;
- WP07 remains unpreempted as a complete-record Type-II Fisher-spectrum phenomenon;
- WP13's deterministic-recovery Fisher/full-law uniqueness is not already contained in inverse Type-II/`M/G/infinity` literature.

Current status: **scientifically strong and increasingly focused; not yet ready for priority language or manuscript drafting.**
