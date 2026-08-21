# WP08 — Visible-Event High-Frequency Fisher Residue for History-Dependent Event Selectors

**Status:** provisional general theorem with an explicit sufficient regularity class. Derived from the general score-projection framework and motivated by WP04/WP07. Requires hostile prior-art and measure-theoretic review before manuscript use.

## 1. Motivation

Three apparently different detector classes show the same high-frequency behavior when they preserve selected incident timestamps exactly:

1. independent thinning with exact timestamps: `G(omega)=eta`;
2. ideal nonparalyzable dead time with complete timestamps: `G(omega)=r/lambda` at every frequency;
3. continuous paralyzable dead time: WP07 gives

\[
\lim_{|\omega|\to\infty}G(\omega)=r/\lambda=e^{-\lambda\tau}.
\]

This suggests that the high-frequency residue is not a peculiarity of a particular dead-time law. It is tied to the fraction of incident events whose **original timestamps remain visible as atoms in the accessible record**.

The goal of this work package is to formulate a history-dependent extension of Paper 1's atomic-timing residue idea.

---

## 2. Event-selector class

Let `N` be a homogeneous Poisson point process on `R` of rate `lambda`.

Let an autonomous causal detector produce an accessible simple point process `Y` satisfying

\[
\boxed{Y\le N}
\]

as counting measures almost surely: every output event is an incident event at the **same timestamp**, but the detector may hide any subset of incident events according to an arbitrary history-dependent stochastic rule.

Examples include idealized

- independent efficiency thinning;
- nonparalyzable dead time;
- paralyzable / retriggered dead time;
- state-dependent event acceptance;
- history-dependent veto/gating generated internally by the detector.

Let the stationary output rate be

\[
r=E[Y([0,1])].
\]

No independent thinning or renewal property is assumed in the general statement.

---

## 3. Conditional-score decomposition

For a weak source waveform `u`, the incident Poisson score is

\[
S_u=\int u(t)[N(dt)-\lambda dt].
\]

Let `H=N-Y` be the hidden incident-event process.

Because the output record `Y` reveals the selected events exactly,

\[
E[N(dt)|Y]=Y(dt)+E[H(dt)|Y].
\]

Assume the conditional mean hidden measure is diffuse:

\[
E[H(dt)|Y]=m_Y(t)dt
\]

for a stationary square-integrable random field `m_Y(t)` with

\[
E[m_Y(t)]=\lambda-r.
\]

Then the exact output score becomes

\[
\boxed{
E[S_u|Y]
=\int u(t)[Y(dt)-r\,dt]
+\int u(t)\xi_Y(t)dt,
}
\]

where

\[
\boxed{
\xi_Y(t)=m_Y(t)-(\lambda-r).
}
\]

The first term is the directly visible timestamp shot-noise contribution. The second is a posterior correction carried by what the observed event pattern tells us about the hidden incident events.

This decomposition is exact under the diffuse conditional-mean hypothesis.

---

## 4. Sufficient high-frequency regularity conditions

Assume:

1. the centered output point process `Y-r dt` has an absolutely continuous covariance density away from its shot-noise atom, with integrable reduced covariance;
2. `xi_Y(t)` has an integrable covariance function;
3. the cross-covariance between `Y-r dt` and `xi_Y(t)dt` has an integrable density.

These are mixing/short-memory conditions. They hold for the explicit renewal dead-time examples studied so far and are expected for a broad class of finite-memory stable detector dynamics, but they are **assumptions**, not consequences of autonomy alone.

Let the corresponding spectral densities be

- `S_Y(omega)` for the centered output point process;
- `S_xi(omega)` for the posterior hidden-intensity field;
- `S_Yxi(omega)` for their cross spectrum.

Riemann--Lebesgue gives

\[
\boxed{S_Y(\omega)\to r}
\]

because the point process retains a white shot-noise atom of weight `r`, while

\[
\boxed{S_\xi(\omega)\to0,\qquad S_{Y\xi}(\omega)\to0.}
\]

---

## 5. Fisher-spectrum consequence

The complete output Fisher metric is the variance of the conditional score. For a complex Fourier mode, the exact source-normalized multiplier therefore has the spectral decomposition

\[
\boxed{
\lambda G(\omega)
=S_Y(\omega)
+S_\xi(\omega)
+2\operatorname{Re}S_{Y\xi}(\omega).
}
\]

Under the assumptions above,

\[
\boxed{
\lim_{|\omega|\to\infty}\lambda G(\omega)=r.
}
\]

Hence

\[
\boxed{
\lim_{|\omega|\to\infty}G(\omega)=\frac{r}{\lambda}.
}
\]

### Candidate theorem wording

> **Visible-event high-frequency residue theorem.** For an autonomous exact-timestamp event-selector channel acting on a stationary Poisson input, if the posterior hidden-event intensity and the reduced output/cross covariances are diffuse and sufficiently mixing, then the complete local temporal Fisher-retention spectrum converges at high frequency to the stationary visible-event fraction `r/lambda`, regardless of the detector's history-dependent selection rule.

This is a sufficient-condition theorem, not a claim for every possible event selector.

---

## 6. Interpretation

At very high source-modulation frequency, any smooth inference about hidden events from neighboring output history averages away. What remains is the singular information carried by event timestamps that are known **exactly** to coincide with incident arrivals.

Thus

\[
\boxed{
\text{high-frequency Fisher residue}
=\text{fraction of incident timestamps remaining directly visible}.
}
\]

The resource is not dead time itself. It is **atomic timestamp visibility**.

This gives an information-theoretic distinction between:

- **event erasure with exact timestamps retained for survivors**, which has a nonzero high-frequency residue;
- **continuous timing smearing**, whose high-frequency characteristic function can vanish;
- **accessible side information / marks**, which can restore otherwise hidden timing information.

---

## 7. Checks against solved examples

### Independent exact-timestamp thinning

If each incident event is retained independently with probability `eta`, then `r/lambda=eta` and

\[
G(\omega)=\eta
\]

for every frequency. The theorem recovers the exact result.

### Ideal nonparalyzable dead time

WP04 gives

\[
G(\omega)=\frac{1}{1+\lambda\tau_d}
\]

for every frequency, while

\[
\frac r\lambda=\frac{1}{1+\lambda\tau_d}.
\]

Again the limit is exact at all frequencies.

### Continuous paralyzable dead time

WP07 gives

\[
r/\lambda=e^{-\lambda\tau}
\]

and independently derives

\[
\lim_{|\omega|\to\infty}G(\omega)=e^{-\lambda\tau}.
\]

Thus the general decomposition reproduces the model-specific renewal-score proof.

---

## 8. Relation to Paper 1

Paper 1's independent-event theorem permits atomic and continuous delay components. Exact unshifted registration corresponds to an atom at zero latency and therefore leaves a nonvanishing high-frequency component.

WP08 extends the organizing idea in a different direction:

- Paper 1 allows arbitrary per-event latency but assumes independent low-overlap events;
- WP08 allows arbitrary history-dependent event selection but assumes the timestamps of selected events are exact incident timestamps.

The two are complementary slices of a more general theory of **singular versus diffuse timing information**.

A later theorem may combine both history-dependent selection and marked stochastic latency, but that should not be attempted until the present result is hardened.

---

## 9. Why this could matter

If the theorem survives prior-art review, it gives a resource law that is genuinely architecture independent within a broad event-selector class:

\[
\boxed{
G_\infty=r/\lambda.
}
\]

This says that detector memory can radically reshape low and intermediate frequencies while leaving the asymptotic information residue fixed by a simple physical quantity: the fraction of photons whose arrival times remain explicitly represented in the output record.

In particular, WP07's striking saturation behavior

\[
G(0)=0,
\qquad
G(\infty)=e^{-1}
\]

is no longer an isolated curiosity. It is an example of a more general visibility law.

---

## 10. Novelty boundary and prior art

Known prior art already covers:

- Fisher-information loss under thinning and stochastic processing;
- stationary point-process spectra and shot-noise limits;
- dead-time count statistics and power spectra;
- independent thinning of point processes;
- high-rate dead-time inference.

An initial search did **not** locate the combined statement that the **complete local waveform Fisher spectrum** of a history-dependent exact-timestamp selector has high-frequency residue equal to its stationary visible-event fraction.

This is not a priority certification. Search specifically for:

1. high-frequency local asymptotic experiments for thinned/history-dependent point processes;
2. score spectra of stationary point-process observation channels;
3. information rates under dependent thinning;
4. neural refractory-process Fisher spectra;
5. missing-event point-process inference with exact survivor times.

Do not use `first` until that search is complete.

---

## 11. Open proof gates

1. Put the conditional hidden-intensity field on a rigorous stationary random-distribution footing.
2. State minimal covariance/mixing hypotheses; the present `L^1` assumptions are sufficient but may be stronger than necessary.
3. Determine whether a Cesaro/Wiener version survives without pointwise spectral convergence.
4. Extend from unmarked event selectors to exact-timestamp events carrying marks.
5. Determine what replaces `r/lambda` when one incident event may generate multiple exact-timestamp output records or when false output events occur.
6. Check whether the visible-event residue can be formulated directly as an atomic component of the general Fisher-retention operator without explicit covariance densities.
