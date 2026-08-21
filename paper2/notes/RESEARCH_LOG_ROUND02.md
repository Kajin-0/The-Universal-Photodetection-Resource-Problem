# Paper 2 Research Log — Round 02

**Scope:** continuous Type-II/paralyzable high-flux information, general-channel proof hardening, visible-event high-frequency residue, static branch aliasing, and random-recovery counterexample.

Paper 1 / Rev11 remained untouched.

## 1. Continuous deterministic Type-II theorem closed

For Poisson input rate `lambda`, deterministic paralyzable dead time `tau`, `rho=lambda*tau`, the recorded events are cluster starts and form a renewal process.

Classical interval transform:

`psi(s)=lambda exp[-(lambda+s)tau] / [s+lambda exp[-(lambda+s)tau]]`

or with `r=lambda exp(-rho)`,

`psi(s)=r exp(-s tau)/[s+r exp(-s tau)]`.

At `rho=1`, the entire homogeneous output law is locally insensitive to uniform incident flux because it depends on `lambda` only through `r` and `dr/dlambda=0`.

Exact result:

`G_1(0)=0`.

For temporal mode `y=omega*tau`, the exact first-order mean-response multiplier is

`M_rho(y)=1-rho(1-exp(-iy))/(iy)`.

The baseline renewal PSD is

`S_Y(omega)=r[1-2 rho exp(-rho) sin(y)/y]`.

A single optimally phased Fourier statistic therefore yields the rigorous lower bound

`G_rho(omega) >= exp(-rho)|M_rho(y)|^2/[1-2 rho exp(-rho) sin(y)/y]`.

At `rho=1`, the bound is positive for every nonzero frequency. In particular,

`G_1(pi/tau) >= exp(-1)(1+4/pi^2)=0.516975...`.

The exact renewal-transition score gives

`G_rho(omega)=exp(-rho) E|A_D(omega)|^2`

and the high-frequency limit

`lim_|omega|->infty G_rho(omega)=exp(-rho)`.

Thus at the paralysis maximum:

`G_1(0)=0`, `G_1(omega)>0` for every nonzero `omega`, and `G_1(infty)=1/e`.

Recorded in `WP07_CONTINUOUS_PARALYZABLE_SPECTRAL_SURVIVAL.md`.

## 2. Independent Volterra numerical validation

A second calculation was implemented from the exact causal Volterra equations for the baseline interval density `k0` and its complex-mode derivative `k1`.

Files:

- `paper2/numerics/continuous_paralyzable_volterra_exact.py`
- `paper2/numerics/continuous_paralyzable_volterra_convergence.csv`
- `paper2/numerics/continuous_paralyzable_volterra_spectrum_snapshot.csv`

At `lambda=tau=1`, grid refinement at `omega*tau=pi` gives:

- h=0.02: `G=0.52689237`
- h=0.01: `G=0.52752096`
- h=0.005: `G=0.52783253`
- h=0.0025: `G=0.52798759`

First-order extrapolation gives approximately `G(pi/tau)~0.52814`, safely above the rigorous lower bound `0.516975`.

The spectrum rises from zero, peaks around `omega*tau~3.3`, then shows damped oscillation toward `1/e`; unlike the discrete one-bin model, the physical continuous model is not strictly monotone high-pass.

## 3. General visible-event high-frequency residue

For an autonomous exact-timestamp event selector `Y<=N` acting on a stationary Poisson input of rate `lambda`, output rate `r`, decompose the conditional source score into

- directly visible timestamp shot noise;
- posterior hidden-event intensity correction.

Under explicit diffuse-posterior and short-memory covariance assumptions, the smooth posterior/correlation spectra vanish at high frequency while the visible-event shot-noise atom remains.

Candidate theorem:

`lim_|omega|->infty G(omega)=r/lambda`.

This unifies independent exact-timestamp thinning, nonparalyzable dead time, and deterministic paralyzable dead time.

Recorded in `WP08_VISIBLE_EVENT_HIGH_FREQUENCY_RESIDUE.md`.

## 4. Targeted novelty audit

Important old results explicitly conceded:

- Teich & Vannucci (1978), DOI `10.1364/JOSA.68.001338`: modulated laser photocounting with paralyzable dead time.
- Teich & Cantor (1978), DOI `10.1109/JQE.1978.1069731`: likelihood/error/mutual-information/channel-capacity work with dead time.
- Jorgensen & Johnson (2026), arXiv:2605.23210: LAN/FI for nonparalyzable dead-time detection; paralyzable Type-II left open.
- Clark (2026), DOI `10.1016/j.spl.2026.110779`: function-valued Fisher operators for point processes.
- Dvurecenskij & Ososkov (1984), DOI `10.21136/AM.1984.104092`: general Type-II counter with random impulse durations.
- classical Takacs/Pyke/Muller Type-II interval/busy-period theory.

Therefore Paper 2 cannot claim novelty for dead-time modulation, generic Fisher operators, random dead time, renewal transforms, or dead-time information theory itself.

No predecessor was found in this search for the combined complete-record temporal Fisher-spectrum results of WP06/WP07 or the visible-event residue theorem. No priority language is allowed yet.

## 5. General autonomous-channel theorem hardened

`WP10_GENERAL_AUTONOMOUS_CHANNEL_THEOREM_HARDENED.md` replaces the earlier increasing-window-first approach.

Primitive tangents are bounded compactly supported `u in L2 cap Linfinity` on the whole line.

Poisson DQM gives

`S_u=int u(t)[N(dt)-Phi0 dt]`

and `E[S_u S_v]=Phi0<u,v>`.

A parameter-independent detector Markov kernel preserves DQM with output score `E[S_u|Y]`. The resulting bounded Fisher quadratic form extends uniquely to a positive contraction `A_K` on all `L2(R)`.

Autonomy gives exact commutation with translations; the standard multiplier theorem yields

`F_out[u,v]=Phi0/(2pi) int G(omega) U*(omega)V(omega)domega`, `0<=G<=1` a.e.

Real preservation + self-adjointness gives even real `G` a.e.

Long sinusoidal performance is recovered afterward with normalized narrowband packets at Lebesgue points of `G`; pure infinite sinusoids are not primitive admissible perturbations.

Paper 1 is recovered exactly as the marked-Poisson special case.

The main remaining theorem issues are publication-grade citations and trajectory-space measurability wording, not the core argument.

## 6. Global static nonidentifiability of deterministic Type II

Because the deterministic Type-II inter-recording transform depends on `lambda` only through

`r=lambda exp(-lambda tau)`,

two incident rates on opposite Lambert-W branches with the same `r` generate **identical complete stationary timestamp laws**.

For `0<r tau<1/e`:

`lambda_-=-W_0(-r tau)/tau`,
`lambda_+=-W_{-1}(-r tau)/tau`.

Thus the familiar mean-rate ambiguity is actually a complete timestamp-experiment ambiguity in the ideal deterministic Type-II model.

At `lambda tau=1` the two branches coalesce and the local Fisher tangent vanishes, explaining `G(0)=0` geometrically.

Temporal modulation breaks the static equivalence; WP07 proves every nonzero frequency retains information.

Recorded in `WP11_GLOBAL_STATIC_NONIDENTIFIABILITY_PARALYZABLE.md`.

## 7. Random recovery disproves any saturation-curve-only information theory

Generalize Type II: every incident event starts an iid dead interval `T`; detector is dead while any event-generated interval is active. This is the `M/G/infinity` cluster-start model.

For any recovery distribution with mean `m`, stationarity/PASTA gives the same conventional output-rate curve:

`r(lambda)=lambda exp(-lambda m)`.

Therefore all distributions with equal mean have the same paralysis maximum at `lambda m=1`.

But complete-record FI differs.

### Deterministic recovery

At `T=m` a.s.:

`G(0)=0` at `lambda m=1`.

### Exponential recovery

For `T~Exp(mu)`, `m=1/mu`, a short-cycle event from one observed renewal interval satisfies

`P(D<=delta)=lambda mu delta^2/2 + O(delta^3)`.

Under fractional flux perturbation `lambda_epsilon=lambda(1+epsilon)`, its derivative is nonzero. The binary statistic `1{D<=delta}` alone therefore gives

`G_exp(0) >= r mu delta^2/2 + O(delta^3)`.

At the shared rate maximum `lambda=mu`,

`G_exp(0) >= (mu delta)^2/(2e)+O((mu delta)^3)>0`

for sufficiently small `delta`.

Hence two Type-II detectors can have the **identical mean saturation curve** but qualitatively different complete-record identifiability:

`G_deterministic(0)=0` versus `G_exponential(0)>0`.

Recovery-law shape is therefore an information resource invisible to the mean count-rate characteristic.

Recorded in `WP12_RANDOM_RECOVERY_BREAKS_STATIC_FISHER_ZERO.md`.

## 8. Current research thesis

The strongest emerging Paper-2 thesis is no longer simply “extend Paper 1 to dead time.” It is:

> Temporal Fisher transfer for autonomous detectors is a property of the full trajectory channel, not of a scalar timing or saturation summary. Time-translation symmetry gives a complete Fisher spectrum even with arbitrary memory; hidden Type-II dynamics can erase static information while retaining dynamic information; exact timestamp visibility fixes a broad high-frequency residue; and recovery-law shape can change identifiability even when the conventional paralysis curve is unchanged.

This is materially broader than Paper 1 if novelty survives.

## 9. Immediate next gates

1. Derive the exact renewal-output DC Fisher formula and use it to formalize “rate information vs interval-shape information.”
2. Quantify exponential-recovery DC FI more sharply, possibly with M/M/infinity busy-cycle transforms.
3. Determine conditions under which deterministic recovery is the unique Type-II law with complete static branch aliasing.
4. Harden WP08 with random-measure language or a weaker Cesaro/Wiener residue theorem.
5. Continue dependent-thinning / refractory-neuron / point-process LAN novelty searches.
6. Add theorem-grade citations for DQM under Markov maps and translation-invariant multipliers.
7. Do not draft a manuscript until the organizing theorem and at least one of WP07/WP08/WP12 survive another hostile review.
