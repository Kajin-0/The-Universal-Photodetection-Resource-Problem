# WP04 — Exact Nonparalyzable Dead-Time Example

**Status:** exact continuous-time calculation; retained as a validation/corollary, **not** as the central novelty claim because of close Jorgensen–Johnson 2026 prior art.

## 1. Model

Incident photons form an inhomogeneous Poisson process with weak intensity perturbation

\[
\lambda_\epsilon(t)=\lambda_0[1+\epsilon u(t)].
\]

The detector is an ideal nonparalyzable counter with deterministic dead time `tau_d`:

- when live, the next incident photon is recorded;
- each recorded photon makes the detector dead for exactly `tau_d`;
- photons arriving while dead are ignored and do not extend the dead interval;
- the complete output timestamp record is retained.

Let `A_t` be the predictable live indicator determined from the output history:

\[
A_t=1
\iff
\text{no recorded output occurred in }(t-\tau_d,t).
\]

Because nonrecorded photons do not affect recovery, `A_t` is exactly reconstructible from the observed timestamps.

## 2. Output conditional intensity

Conditional on the output past,

\[
\boxed{
\mu_\epsilon(t|\mathcal Y_{t^-})
=\lambda_\epsilon(t)A_t.
}
\]

The gate `A_t` depends on the output history but not directly on the source perturbation once that history is fixed.

For a point process with predictable conditional intensity `mu_epsilon`, the local likelihood score is

\[
S_u^{\rm out}
=\int
\left.\partial_\epsilon\log\mu_\epsilon(t)\right|_0
[dN_{\rm out}(t)-\mu_0(t)dt].
\]

On live intervals,

\[
\left.\partial_\epsilon\log\mu_\epsilon(t)\right|_0=u(t),
\]

so

\[
\boxed{
S_u^{\rm out}
=\int u(t)[dN_{\rm out}(t)-\lambda_0A_tdt].
}
\]

## 3. Fisher bilinear form

The martingale isometry gives

\[
F_{\rm out}[u,v]
=\mathbb E\int u(t)v(t)\lambda_0A_tdt.
\]

At stationary homogeneous baseline, `E[A_t]=p_live` is constant, hence

\[
\boxed{
F_{\rm out}[u,v]
=\lambda_0p_{\rm live}\int u(t)v(t)dt.
}
\]

The incident Poisson Fisher form is

\[
F_{\rm in}[u,v]
=\lambda_0\int u(t)v(t)dt.
\]

Therefore the waveform retention operator is simply

\[
\boxed{\mathcal A=p_{\rm live}I.}
\]

and the full temporal Fisher spectrum is frequency-flat:

\[
\boxed{G_{\lambda_0}(\omega)=p_{\rm live}\quad\forall\omega.}
\]

## 4. Stationary live fraction

A renewal cycle consists of:

1. a deterministic dead interval `tau_d` after a recorded event;
2. an exponential waiting time of mean `1/lambda_0` until the next incident photon, which is recorded.

Thus

\[
p_{\rm live}
=\frac{1/\lambda_0}{\tau_d+1/\lambda_0}
=\boxed{\frac{1}{1+\lambda_0\tau_d}}.
\]

Hence

\[
\boxed{
G_{\lambda_0}(\omega)
=\frac{1}{1+\lambda_0\tau_d}
\quad\text{for all }\omega.
}
\]

## 5. Independent DC check

For a constant rate parameter, recorded interarrival intervals are

\[
W=\tau_d+E,
\qquad E\sim\operatorname{Exp}(\lambda).
\]

Each interval contains the same rate information as one exponential waiting time. The stationary output event rate is

\[
r_{\rm out}=\frac{1}{\tau_d+1/\lambda}
=\frac{\lambda}{1+\lambda\tau_d}.
\]

For the fractional rate perturbation, FI per recorded renewal interval is 1, so FI rate is `r_out`. Input FI rate is `lambda`. Their ratio is again

\[
\frac{r_{\rm out}}{\lambda}
=\frac{1}{1+\lambda\tau_d}.
\]

This independently verifies the spectral result at DC.

## 6. Interpretation

This ideal detector has memory and operates at arbitrary flux, but its memory is **fully output-predictable**. Dead time removes temporal exposure; it does not smear the timestamps that are recorded.

Therefore deterministic nonparalyzable dead time is not a Fisher low-pass when the complete timestamp record and exact recovery rule are retained. It produces a frequency-independent efficiency penalty equal to the live-time fraction.

This is an important caution:

> a long recovery/dead time does not by itself imply a finite local temporal-information cutoff.

A conventional count-rate bandwidth or recovery time can therefore be very different from the complete-record temporal Fisher spectrum.

## 7. More general predictable-gating corollary

The same calculation extends to a predictable gate or recovery factor `q_t` that is fully reconstructible from the output history and enters multiplicatively:

\[
\mu_\epsilon(t)=\lambda_\epsilon(t)q_t,
\qquad 0\le q_t\le1.
\]

If the stationary baseline gives `E[q_t]=qbar`, then

\[
F_{\rm out}[u,v]
=\lambda_0qbar\int uv,
\]

so

\[
\boxed{G(\omega)=qbar.}
\]

Thus **output-predictable multiplicative exposure loss is spectrally flat** in local FI.

This corollary should be checked against the exact scope of Jorgensen–Johnson's activation-frequency theorem before publication.

## 8. Prior-art boundary

Jorgensen & Johnson, arXiv:2605.23210 (2026), develop LAN and Fisher-information rates for discrete periodic nonparalyzable dead-time event detection with arbitrary causal gating. They show that history-dependent gating affects asymptotic information through limiting activation/sampling frequencies.

Accordingly:

- do **not** claim priority for the live-fraction FI penalty;
- do **not** claim that nonparalyzable dead-time FI is new;
- use this exact continuous-time result as a validation of the Paper-2 operator/spectral framework and as a conceptual bridge to the harder hidden-state case.

Their manuscript explicitly leaves paralyzable/Type-II dead time as future work, making that the next high-value target.

## 9. Why hidden state should change the answer

For paralyzable dead time, an unrecorded photon during the inactive period restarts the dead time. The current live/dead state is therefore **not reconstructible from the output timestamps**: an apparently quiet interval may contain hidden photons that extended recovery.

Then the output conditional intensity has the form

\[
\mu_\epsilon(t|\mathcal Y_{t^-})
=\lambda_\epsilon(t)\,\pi_\epsilon(t),
\]

where `pi_epsilon(t)` is the posterior probability of being live given the output history. Crucially, `pi_epsilon` itself depends on the source perturbation.

Hence

\[
\partial_\epsilon\log\mu_\epsilon
=u(t)+\partial_\epsilon\log\pi_\epsilon(t),
\]

introducing a memory/filter term. This is the mechanism expected to generate genuinely frequency-dependent `G_{lambda0}(omega)`.

That is WP05.
