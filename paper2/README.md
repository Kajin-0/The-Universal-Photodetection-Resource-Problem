# Paper 2 — General Fisher-Channel Resource Theory for Photodetection

## Status

**Active research program.** Paper 1 / Rev11 is scientifically frozen by default and remains the preferred first-paper submission candidate. This directory is a separate second-paper program.

The ambition is deliberately higher than Paper 1: remove the independent-event / one-primary-registration restriction without giving up an exact universal local-information ordering theorem, and identify genuinely new high-flux information phenomena that appear only when detector memory is allowed.

## Central research question

> For an arbitrary photodetector viewed as a parameter-independent stochastic channel from the complete incident optical record to the complete accessible detector record, what operator exactly describes the local temporal Fisher information retained by the detector, and what does time-translation symmetry force that operator to look like?

## Candidate organizing theorem

Let a stationary Poisson optical input of baseline flux `Phi0` be weakly modulated by arbitrary square-integrable temporal waveforms. Let the detector be **any autonomous stochastic channel** from the entire incident photon trajectory to an accessible output record. The detector may have dead time, saturation, recovery, afterpulsing, hidden-state memory, state-dependent capture, multiple output events, analog marks, and arbitrary high-flux history dependence.

Under differentiability/regularity assumptions, the complete output local Fisher metric should be representable as

\[
F_{\rm out}[u,v]
=\frac{\Phi_0}{2\pi}\int_{\mathbb R}
G_{\Phi_0}(\omega)U^*(\omega)V(\omega)d\omega,
\]

with

\[
0\le G_{\Phi_0}(\omega)\le1\quad\text{a.e.}
\]

**without any independent-event delay kernel.**

Proof route:

1. output score = conditional expectation of the source score;
2. package this as a positive contraction on the Poisson waveform tangent space;
3. autonomy makes that operator commute with temporal translations;
4. scalar `L^2(R)` multiplicity plus the Fourier-multiplier theorem gives `G_Phi0(omega)`;
5. Paper 1's marked-delay spectrum must emerge as an exact low-overlap special case.

Candidate conceptual message:

> **Spectral completeness is symmetry-driven, not independent-event-driven.**

The statistical/operator ingredients are standard. Novelty, if any, lies in the photodetection specialization and its nontrivial consequences.

---

# Strongest current new results

## 1. Discrete Type-II information high-pass

For the one-bin paralyzable detector

\[
Y_n=X_n(1-X_{n-1}),
\qquad X_n\sim\operatorname{Bernoulli}(p_n),
\]

at the symmetric high-flux point `p=1/2`, define

\[
x=1-\cos\omega.
\]

The complete source-normalized Fisher spectrum is exactly

\[
\boxed{
G_{1/2}(\omega)
=1-\frac{1}{2x}
+\frac{\ln(1+4x)}{8x^2},
}
\]

with continuous extension `G(0)=0`.

It is strictly increasing over `0<omega<pi` and reaches

\[
\boxed{G(\pi)=\frac34+\frac{\ln3}{16}=0.818663268\ldots}
\]

Thus hidden Type-II memory can turn saturation into a **Fisher-information high-pass**: complete DC blindness but strong high-frequency information.

See `notes/WP05_*` and `notes/WP06_*`.

## 2. Continuous-time paralyzable spectral survival

For a Poisson input of rate `lambda` and deterministic paralyzable dead time `tau`, let

\[
\rho=\lambda\tau.
\]

The baseline output is a renewal process of rate

\[
r=\lambda e^{-\rho}.
\]

At the classical paralysis maximum `rho=1`, the **entire homogeneous output timestamp law**, not just its mean rate, is locally insensitive to uniform intensity:

\[
\boxed{G_1(0)=0.}
\]

For `y=omega*tau`, a single Fourier statistic gives the rigorous complete-record lower bound

\[
\boxed{
G_\rho(\omega)
\ge
e^{-\rho}
\frac{
1-2\rho\sin y/y+2\rho^2(1-\cos y)/y^2
}
{1-2\rho e^{-\rho}\sin y/y}.
}
\]

At `rho=1`, this is strictly positive for **every nonzero frequency**. In particular,

\[
\boxed{
G_1(\pi/\tau)
\ge\frac1e\left(1+\frac4{\pi^2}\right)
\approx0.516975.
}
\]

The exact complete-record renewal-score representation further gives

\[
\boxed{
\lim_{|\omega|\to\infty}G_\rho(\omega)=e^{-\rho}.
}
\]

Therefore at the paralysis maximum

\[
\boxed{
G_1(0)=0,
\quad
G_1(\omega)>0\ \forall\omega\ne0,
\quad
G_1(\infty)=e^{-1}.
}
\]

This is the strongest current physical high-flux theorem. See `notes/WP07_CONTINUOUS_PARALYZABLE_SPECTRAL_SURVIVAL.md`.

## 3. Visible-event high-frequency residue — provisional general theorem

For an autonomous detector that selects a history-dependent subset `Y<=N` of incident Poisson events but preserves selected timestamps exactly, let `r` and `lambda` be output and input rates.

Under explicit diffuse-posterior and short-memory covariance assumptions,

\[
\boxed{
\lim_{|\omega|\to\infty}G(\omega)=\frac r\lambda.
}
\]

Thus the high-frequency Fisher residue is controlled by **atomic timestamp visibility**, not by a recovery time constant.

This unifies independent exact-timestamp thinning, nonparalyzable dead time, and the continuous paralyzable limit. See `notes/WP08_VISIBLE_EVENT_HIGH_FREQUENCY_RESIDUE.md`.

---

# Why this could be substantially broader than Paper 1

Paper 1 assumes autonomous low-overlap independent primary events and obtains

\[
G(\omega)=\int|H_m(\omega)|^2\kappa(dm).
\]

Paper 2 asks whether the same spectral completeness survives when that explicit kernel representation disappears. The target class includes, in principle:

- SPAD dead time and pile-up;
- SNSPD recovery and history-dependent efficiency;
- afterpulsing and trap memory;
- state-dependent capture;
- high-flux saturation;
- multiple primary registrations;
- arbitrary hidden Markov / semi-Markov detector dynamics;
- complete analog or digital output records.

The spectrum generally depends on baseline flux: `G=G_Phi0(omega)`.

---

# Novelty discipline

Known ingredients that must **not** be claimed as new:

- Fisher-information monotonicity under Markov kernels;
- output-score identity `score_out=E(score_in|output)`;
- conditional expectation as an `L^2` contraction;
- translation-invariant bounded operators being Fourier multipliers;
- generic function-valued Fisher-information operators for point processes;
- modulated paralyzable photon counting;
- dead-time count-rate, renewal, moment, correlation, or PSD theory;
- information-theoretic analysis of detector dead time in general.

Important close references include:

- Teich & Vannucci, JOSA 68, 1338 (1978), DOI `10.1364/JOSA.68.001338`;
- Teich & Cantor, IEEE JQE 14, 993 (1978), DOI `10.1109/JQE.1978.1069731`;
- Jorgensen & Johnson, arXiv:2605.23210 (2026), nonparalyzable LAN/FI theory;
- Clark, Statistics & Probability Letters 236, 110779 (2026), DOI `10.1016/j.spl.2026.110779`, functional Fisher operators for point processes.

The current targeted searches have **not** found the exact complete-record Type-II Fisher-spectrum phenomena above or the visible-event residue theorem, but priority is not certified.

---

# Current work packages

1. `notes/WP01_GENERAL_FISHER_CHANNEL_OPERATOR.md`
2. `notes/WP02_STATIONARY_POISSON_SPECTRAL_THEOREM.md`
3. `notes/WP03_PRIOR_ART_AND_NOVELTY_AUDIT.md`
4. `notes/WP04_NONPARALYZABLE_DEAD_TIME_EXACT_EXAMPLE.md`
5. `notes/WP05_PARALYZABLE_ONEBIN_EXACT_SPECTRUM.md`
6. `notes/WP06_CLOSED_FORM_HIGH_PASS_THEOREM.md`
7. `notes/WP07_CONTINUOUS_PARALYZABLE_SPECTRAL_SURVIVAL.md`
8. `notes/WP08_VISIBLE_EVENT_HIGH_FREQUENCY_RESIDUE.md`
9. `notes/WP09_TYPEII_AND_FISHER_OPERATOR_PRIOR_ART_AUDIT.md`
10. `notes/RESEARCH_LOG_*.md`

Numerical/reproduction assets are under `paper2/numerics/`.

---

# Immediate research priorities

1. Harden the general autonomous-channel theorem (DQM/increasing-window/translation covariance/Paper-1 recovery).
2. Independently validate the continuous Type-II exact-spectrum Volterra calculation.
3. Harden the visible-event residue theorem and seek weaker assumptions/Cesaro variants.
4. Search dependent-thinning, refractory-neuron, spike-train, stationary-channel LAN, and system-identification literatures.
5. Generalize deterministic Type-II dead time to random recovery and identify which information-spectral features are invariant.
6. Only then decide whether the result is strong enough for a Paper-2 manuscript.

## Research rule

Do not manufacture a "breakthrough" by renaming standard statistics. Paper 2 is worth writing only if the organizing theorem plus the hidden-memory consequences survive adversarial proof and prior-art review.
