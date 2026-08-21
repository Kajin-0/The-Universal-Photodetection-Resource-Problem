# Paper 2 Research Log — Round 01

**Date:** 2026-08-21

## Trigger

Paper 1 / Rev11 was judged strong enough to freeze. The next objective is a separate paper with substantially greater theoretical scope and breakthrough potential rather than further expansion of Rev11.

The initial candidate directions included quantum FI, universal speed-resource bounds, mark-rate-distortion theory, high-flux memory, and optimal detector design.

The first active route selected is the **general detector-channel / high-flux memory** direction because it can potentially remove one of Paper 1's largest assumptions in a single theorem while preserving an exact temporal ordering theory.

---

## Result 1 — general detector Fisher-retention operator

For a parameter-independent detector Markov channel from complete source record `X` to complete accessible output `Y`, the standard conditional-score identity gives

`score_out = E(score_in | Y)`.

Packaging this on the source score Hilbert space gives

`M_K = T_K^dagger T_K`,

`0 <= M_K <= I`,

and

`[F_out]_{ab} = <S_a, M_K S_b>`.

Universal local Fisher ordering over all admitted tangent tasks is exactly operator order between the corresponding `M_K`.

This is useful infrastructure but **not itself a novelty claim**; its ingredients are classical statistics/sufficiency theory.

Recorded in `WP01_GENERAL_FISHER_CHANNEL_OPERATOR.md`.

---

## Result 2 — candidate arbitrary-memory stationary Fisher-spectrum theorem

For stationary Poisson input of rate `Phi0` with weak waveform perturbation `u(t)`, the source score is

`S_u = int u(t)[N(dt)-Phi0 dt]`

with Poisson isometry

`E[S_u S_v] = Phi0 int u v`.

Thus the scalar temporal source tangent is isometric to `L^2(R)`.

For an **arbitrary autonomous detector channel**, the induced waveform Fisher operator `A_K` is a positive contraction. Time-translation covariance should force

`A_K U_a = U_a A_K`.

Standard harmonic analysis then gives an exact multiplier

`G_{Phi0,K}(omega)` with `0 <= G <= 1` a.e., satisfying

`F_out[u,v] = Phi0/(2*pi) int G(omega) U*(omega)V(omega) d omega`.

If the measure-theoretic proof closes, this means a complete scalar temporal Fisher spectrum survives:

- arbitrary detector memory;
- dead time;
- saturation;
- recovery;
- afterpulsing;
- state-dependent capture;
- multiple registrations;
- arbitrary high-flux history dependence.

No independent-event delay kernel is required.

Candidate conceptual statement:

> **Spectral completeness is symmetry-driven, not independent-event-driven.**

Recorded in `WP02_STATIONARY_POISSON_SPECTRAL_THEOREM.md`.

---

## Prior-art boundary

The proof ingredients are standard and must not be renamed as breakthroughs:

- output score as conditional expectation;
- Fisher monotonicity under Markov processing;
- conditional expectation as an `L^2` contraction;
- translation-invariant `L^2` operators as Fourier multipliers.

High-flux/dead-time FI also has substantial prior art.

Most important close result found:

Frederic J. N. Jorgensen and Steven G. Johnson, *Fundamental Bounds and Efficient Estimation for Dead-Time-Constrained Event Detection, with Application to Single-Photon Lidar*, arXiv:2605.23210 (2026).

They develop LAN/FI theory for discrete periodic **nonparalyzable** dead-time detection with arbitrary causal gating and show that history-dependent gating affects asymptotic information through activation/sampling frequencies.

Therefore simple nonparalyzable live-fraction FI penalties are not our novelty target.

Their paper explicitly leaves **paralyzable/Type-II dead time** as future work.

Updated in `WP03_PRIOR_ART_AND_NOVELTY_AUDIT.md`.

---

## Result 3 — exact nonparalyzable validation

For an ideal continuous-time nonparalyzable detector with deterministic dead time `tau_d`, complete output timestamps, and Poisson input rate `lambda0`, the live indicator is exactly output-predictable.

The output conditional intensity is

`mu_epsilon(t)=lambda_epsilon(t) A_t`.

Point-process martingale FI gives

`F_out[u,v]=lambda0 E[A] int u v`.

The stationary live fraction is

`E[A]=1/(1+lambda0 tau_d)`.

Thus

`G_lambda0(omega)=1/(1+lambda0 tau_d)`

for **every** frequency.

Dead time removes temporal exposure but is not a Fisher low-pass in this ideal complete-record model.

Because of Jorgensen–Johnson, this is retained as an exact continuous-time validation/corollary rather than a central novelty claim.

Recorded in `WP04_NONPARALYZABLE_DEAD_TIME_EXACT_EXAMPLE.md`.

---

## Result 4 — exact paralyzable information-spectral inversion

A discrete one-bin Type-II detector was solved exactly:

`X_n ~ Bernoulli(p_n)` independently,

`Y_n = X_n(1-X_{n-1})`.

Every input event, including a hidden/unrecorded one, suppresses the next bin. The hidden detector state is therefore not reconstructible from the output record.

At baseline `p`, the output is a renewal process whose intervals are sums of a geometric run of ones and a geometric run of zeros.

The exact conditional score given a renewal interval was derived, yielding a convergent exact renewal-series representation of the full Fisher multiplier `G_p(omega)`.

At the symmetric high-flux point `p=1/2`:

### DC

The hidden switch point is uniform conditional on an observed renewal interval. The conditional score for a uniform perturbation cancels **for every interval individually**, giving

`G_{1/2}(0)=0`.

This is complete local DC nonidentifiability, not merely zero slope of the mean count rate.

### Nyquist / alternating mode

For `u_n=(-1)^n`, exact summation gives

`G_{1/2}(pi) = 3/4 + ln(3)/16 = 0.818663268...`.

Therefore the same saturated detector that retains zero DC Fisher information retains more than 81% of the incident information about the fastest alternating modulation.

This is a strong frequency-selective high-flux effect and the first result in the Paper-2 program that is not reproduced by predictable-gating/live-fraction logic.

A numerical evaluation of the exact renewal series gives a high-pass-like curve rising from 0 at DC to `0.818663...` at Nyquist. Monotonicity has not yet been proved.

Recorded in `WP05_PARALYZABLE_ONEBIN_EXACT_SPECTRUM.md`.

Reproduction assets:

- `paper2/numerics/paralyzable_onebin_spectrum.py`
- `paper2/numerics/paralyzable_onebin_spectrum_p_half.csv`

---

## Current interpretation

The emerging organizing distinction is:

1. **Output-predictable memory/gating:** local FI loss can be spectrally flat because the record tells the estimator exactly when the detector was exposed.
2. **Hidden memory:** unobserved input events alter future detector state; the state posterior itself responds dynamically to the source waveform, producing a genuinely frequency-dependent Fisher spectrum.

This may become a resource principle involving **state observability / accessible side information**, linking the general-channel theorem to Paper 1's mark-resource gradient.

---

## Immediate next work

1. Deep prior-art search for paralyzable/Type-II FI and hidden-state waveform information.
2. Prove or disprove monotonicity of `G_{1/2}(omega)`.
3. Generalize the one-bin Type-II model to `d` dead bins and look for exact spectral structure.
4. Attack the continuous-time paralyzable detector.
5. Close theorem-grade DQM/covariance details of WP02.
6. Do not begin a polished Paper-2 manuscript until the central theorem and novelty survive these gates.
