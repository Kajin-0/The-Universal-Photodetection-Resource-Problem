# WP20 — Cesàro Visible-Event Fisher Residue from the Zero-Lag Covariance Atom

**Status:** rigorous replacement/hardening of WP08 under weaker second-order assumptions. The pointwise limit `G(omega)->r/lambda` requires a Rajchman/Riemann–Lebesgue condition on the non-shot-noise covariance. The robust theorem is instead a high-frequency **band-average** law: the visible exact-timestamp fraction is the coefficient of the unique zero-lag covariance atom and therefore survives every expanding high-frequency Cesàro average. If the correction covariance measure is atomless, Wiener's theorem upgrades the result to high-frequency mean-square convergence.

This work package is a proof/statement improvement. It does not claim novelty for stationary random-measure spectral theory or Wiener's theorem.

---

## 1. Event-selector model

Let `N` be a homogeneous Poisson input on `R` of rate

\[
\lambda>0.
\]

Let an autonomous detector produce a stationary simple output point process `Y` satisfying

\[
\boxed{Y\le N}
\]

as counting measures: every registered output event is an incident event and preserves its **exact incident timestamp**. The history-dependent selection rule may otherwise be arbitrary.

Let

\[
r=E[Y([0,1])]
\]

be the stationary visible-event rate.

Write the hidden incident process as

\[
H=N-Y.
\]

Assume, as in WP08, that the conditional hidden-event mean given the complete output record is diffuse:

\[
E[H(dt)\mid Y]=m_Y(t)dt,
\]

with stationary locally square-integrable density. Since

\[
E[m_Y(t)]=\lambda-r,
\]

define

\[
\xi_Y(t)=m_Y(t)-(\lambda-r).
\]

For a source waveform `u`, the exact output score is

\[
\boxed{
S_u^{out}
=\int u(t)[Y(dt)-r\,dt]
+\int u(t)\xi_Y(t)dt.}
\]

Define the centered **conditional-score random measure**

\[
\boxed{
M(dt)=Y(dt)-r\,dt+\xi_Y(t)dt.}
\]

Then

\[
S_u^{out}=\int u(t)M(dt).
\]

---

## 2. Second-order covariance-measure assumption

Assume the stationary second-order covariance measure of `M` exists and has the form

\[
\boxed{
\Gamma_M(dt)=r\,\delta_0(dt)+\nu(dt),}
\]

where

1. `nu` is a finite signed/complex measure of finite total variation;
2. `nu({0})=0`.

This is the key regularity class.

### Why the `r delta_0` term is structural

Because `Y` is a **simple exact-timestamp** point process, its ordinary covariance measure contains the familiar diagonal shot-noise contribution

\[
r\delta_0.
\]

The posterior hidden-intensity correction `xi_Y(t)dt` is diffuse in time. Therefore it cannot itself create a counting-measure diagonal atom. Cross terms with a diffuse measure likewise do not create another point mass on the exact diagonal under the stated ordinary second-order regularity.

The remaining reduced output covariance, hidden-intensity covariance, and cross covariance are collected into `nu`.

The condition

\[
\|\nu\|_{TV}<\infty
\]

is a standard short-range second-order mixing condition. In point-process language, finiteness of reduced covariance/factorial cumulant total variation is the second-order part of Brillinger-type mixing. It is **weaker than assuming an integrable covariance density**: `nu` may contain singular-continuous structure or atoms at nonzero lags.

Relevant background includes the stationary random-measure spectral theory in Daley & Vere-Jones and the Brillinger-mixing literature; finite total variation of reduced covariance measures is a standard sufficient condition for continuous spectral densities of ordinary stationary point processes.

---

## 3. Fisher spectrum from the score covariance measure

For compactly supported square-integrable source waveforms,

\[
F_{out}[u,v]
=E\left[\int u(t)M(dt)\int v(s)M(ds)\right].
\]

Stationarity and the covariance measure give

\[
F_{out}[u,v]
=\frac1{2\pi}
\int_{\mathbb R}
S_M(\omega)U^*(\omega)V(\omega)d\omega,
\]

where, under the finite-measure assumption,

\[
\boxed{
S_M(\omega)
=r+\widehat\nu(\omega).}
\]

The incident Poisson Fisher form is

\[
F_{in}[u,v]
=\frac{\lambda}{2\pi}
\int U^*V.
\]

Therefore the general WP10 multiplier has the continuous representative

\[
\boxed{
\lambda G(\omega)
=r+\widehat\nu(\omega).}
\]

In particular,

\[
\boxed{
G(\omega)-\frac r\lambda
=\frac1\lambda\widehat\nu(\omega).}
\]

The question of high-frequency residue is exactly the Fourier–Stieltjes behavior of the non-diagonal covariance measure `nu`.

---

## 4. Pointwise convergence is not implied by finite covariance measure

A finite measure need not have Fourier transform tending to zero at infinity. Continuous singular measures and atomic measures can have nonvanishing Fourier–Stieltjes transforms along unbounded frequency sequences.

Therefore the WP08 statement

\[
G(\omega)\to r/\lambda
\]

is **not** a consequence of finite covariance-measure memory alone.

Pointwise convergence requires the stronger property

\[
\boxed{\widehat\nu(\omega)\to0,}
\]

i.e. that `nu` is a Rajchman measure. An `L1` covariance density is a familiar sufficient condition by the Riemann–Lebesgue lemma, which is essentially the route used in WP08.

This distinction matters because it prevents an overbroad claim that “short memory” in an arbitrary measure-theoretic sense forces pointwise convergence.

---

## 5. Robust theorem: moving high-frequency band average

For `Omega>0`, define the one-octave high-frequency average

\[
\boxed{
\overline G_{[\Omega,2\Omega]}
=\frac1\Omega\int_\Omega^{2\Omega}G(\omega)d\omega.}
\]

Then

\[
\overline G_{[\Omega,2\Omega]}-\frac r\lambda
=\frac1\lambda
\int K_\Omega(t)\nu(dt),
\]

where

\[
K_\Omega(t)
=\frac1\Omega\int_\Omega^{2\Omega}e^{-i\omega t}d\omega.
\]

For `t=0`,

\[
K_\Omega(0)=1.
\]

For `t\ne0`,

\[
K_\Omega(t)
=e^{-3i\Omega t/2}
\frac{2\sin(\Omega t/2)}{\Omega t}
\longrightarrow0.
\]

Also

\[
|K_\Omega(t)|\le1
\]

for every `t`.

Since `nu` has finite total variation, dominated convergence gives

\[
\lim_{\Omega\to\infty}
\int K_\Omega(t)\nu(dt)
=\nu(\{0\}).
\]

By assumption `nu({0})=0`. Therefore

\[
\boxed{
\lim_{\Omega\to\infty}
\frac1\Omega\int_\Omega^{2\Omega}G(\omega)d\omega
=\frac r\lambda.}
\]

This is a **genuine high-frequency tail-band theorem**: the averaging window itself moves to infinity.

The same proof works for any fixed `0<a<b<infinity`:

\[
\boxed{
\lim_{\Omega\to\infty}
\frac1{(b-a)\Omega}
\int_{a\Omega}^{b\Omega}G(\omega)d\omega
=\frac r\lambda.}
\]

Because `G` is even, the corresponding negative-frequency or symmetric two-sided versions are identical.

---

## 6. Expanding flat-band average

The simpler origin-centered average also follows:

\[
\boxed{
\lim_{\Omega\to\infty}
\frac1{2\Omega}
\int_{-\Omega}^{\Omega}G(\omega)d\omega
=\frac r\lambda.}
\]

Indeed,

\[
\frac1{2\Omega}\int_{-\Omega}^{\Omega}e^{-i\omega t}d\omega
=\frac{\sin(\Omega t)}{\Omega t}
\to\mathbf1_{\{0\}}(t),
\]

bounded by one, so finite-measure dominated convergence again extracts exactly the zero-lag atom.

This is the direct random-measure analogue of the atomic-residue logic used in Paper 1.

---

## 7. Interpretation: exact timestamp visibility is a diagonal Fisher atom

The result can be stated without invoking a detector recovery time:

\[
\boxed{
\text{high-frequency Cesàro Fisher residue}
=\text{zero-lag score-covariance atom}/\lambda
= r/\lambda.}
\]

The visible registered timestamps contribute an irreducible singular covariance term `r delta_0`. Any finite non-diagonal covariance correction averages away over an expanding high-frequency band.

Thus the invariant is not “dead time” or “recovery speed.” It is **atomic exact-timestamp visibility in the conditional source score**.

This is stronger conceptually than WP08's initial proof because it identifies the precise mathematical object responsible for the residue.

---

## 8. Mean-square strengthening when the correction measure is atomless

The band-average theorem above permits `nu` to have atoms at nonzero lags. Such atoms produce persistent oscillations in `G(omega)` and can prevent pointwise convergence.

If `nu` is instead **atomless everywhere**, Wiener's classical theorem for Fourier–Stieltjes transforms gives

\[
\boxed{
\lim_{\Omega\to\infty}
\frac1{2\Omega}
\int_{-\Omega}^{\Omega}
|\widehat\nu(\omega)|^2d\omega
=0.}
\]

Equivalently,

\[
\boxed{
\lim_{\Omega\to\infty}
\frac1{2\Omega}
\int_{-\Omega}^{\Omega}
\left|G(\omega)-\frac r\lambda\right|^2d\omega
=0.}
\]

The same follows on moving proportional bands such as `[Omega,2 Omega]` because the difference of two cumulative Cesàro integrals has the same zero limit.

Thus an atomless finite correction measure yields **mean-square high-frequency convergence** even if it is singular continuous and Riemann–Lebesgue pointwise decay is unavailable.

More generally, Wiener's atom formula gives

\[
\lim_{\Omega\to\infty}
\frac1{2\Omega}
\int_{-\Omega}^{\Omega}
|\widehat\nu(\omega)|^2d\omega
=\sum_{t\in\mathbb R}|\nu(\{t\})|^2.
\]

So persistent high-frequency mean-square oscillation is itself controlled exactly by the **nonzero-lag atomic part** of the correction covariance measure.

---

## 9. Three-level residue hierarchy

WP08/WP20 should therefore be organized as follows.

### Level I — finite correction covariance measure

Assume

\[
\|\nu\|_{TV}<\infty,
\qquad
\nu(\{0\})=0.
\]

Then the moving-band and flat-band Cesàro laws are exact:

\[
\boxed{\langle G\rangle_{high\ band}\to r/\lambda.}
\]

No pointwise limit is claimed.

### Level II — atomless finite correction measure

If in addition `nu` has no atoms at any lag, then

\[
\boxed{
\left\langle
|G-r/\lambda|^2
\right\rangle_{high\ band}
\to0.}
\]

Thus `G` converges to `r/lambda` in high-frequency mean square / density, though not necessarily pointwise.

### Level III — Rajchman correction measure

If

\[
\widehat\nu(\omega)\to0,
\]

for example because `nu` has an `L1` density, then

\[
\boxed{G(\omega)\to r/\lambda}
\]

pointwise.

WP08's original theorem belongs at Level III. WP20 supplies the more robust Levels I and II.

---

## 10. Checks against solved detector models

### Independent exact-timestamp thinning

There is no correction covariance:

\[
\nu=0.
\]

Hence

\[
G(\omega)=r/\lambda=\eta
\]

at every frequency.

### Ideal nonparalyzable dead time

WP04 gives the exact flat spectrum

\[
G(\omega)=r/\lambda=\frac1{1+\lambda\tau_d}.
\]

Again every level of the hierarchy is satisfied trivially.

### Deterministic paralyzable dead time

WP07 proves independently

\[
G(\omega)\to r/\lambda=e^{-\lambda\tau}
\]

pointwise, so this model lies in Level III.

At the paralysis maximum,

\[
G(0)=0,
\qquad
G(\infty)=1/e.
\]

WP20 explains the asymptotic constant structurally as the exact-timestamp score-covariance atom of the visible cluster starts.

---

## 11. Why WP20 is preferable to simply strengthening WP08's covariance-density assumptions

The earlier route required each reduced/cross covariance to possess an integrable density so that the Riemann–Lebesgue lemma could be applied term by term.

WP20 instead packages the complete conditional score into one stationary random measure and asks only for a finite-total-variation **correction covariance measure**.

Advantages:

1. it allows singular covariance structure;
2. it allows nonzero-lag covariance atoms;
3. it makes clear exactly why pointwise convergence may fail;
4. it still yields an exact high-frequency band-average law;
5. it identifies `r/lambda` as the coefficient of the zero-lag Fisher atom;
6. it aligns naturally with Paper 1's atomic timing/Wiener viewpoint.

This is the recommended theorem for a manuscript. The pointwise version should appear only as a stronger corollary under Rajchman/L1 regularity.

---

## 12. Prior-art boundary

The following are standard and must not be claimed as new:

- covariance and spectral measures of stationary random measures/point processes;
- the diagonal shot-noise atom of a simple point process;
- Fourier transforms of finite measures;
- dominated-convergence extraction of an atom by expanding Fourier averages;
- Wiener's theorem detecting atoms of finite measures from Cesàro averages of squared Fourier transforms;
- Brillinger-type mixing conditions expressed through finite total variation of reduced cumulant/covariance measures.

The candidate detector-specific contribution is their synthesis with the conditional-score/Fisher-channel construction:

> for a history-dependent exact-timestamp selector, the visible-event fraction is the coefficient of a singular zero-lag component of the **conditional source-score covariance**, and therefore fixes the high-frequency Cesàro Fisher residue independently of the detailed detector memory.

No priority claim has been audited specifically for this covariance-atom formulation.

---

## 13. Recommended theorem wording

> **Visible-event Cesàro residue theorem.** Consider an autonomous exact-timestamp event-selector channel `Y<=N` driven by a homogeneous Poisson input of rate `lambda`, with visible output rate `r`. Suppose the conditional mean of hidden incident events is diffuse and the stationary conditional-score random measure has covariance measure `r delta_0 + nu`, where `nu` has finite total variation and no atom at zero. Then the complete local Fisher-retention spectrum satisfies, for every fixed `0<a<b`,
> \[
> \lim_{\Omega\to\infty}
> \frac1{(b-a)\Omega}
> \int_{a\Omega}^{b\Omega}G(\omega)d\omega
> =\frac r\lambda.
> \]
> If `nu` is atomless, the high-frequency mean-square deviation from `r/lambda` vanishes. If `nu` is Rajchman—for example if it has an `L1` density—then the pointwise limit `G(omega)->r/lambda` follows.

This theorem is strictly safer and more general than the original WP08 pointwise formulation.

---

## 14. Research decision

WP08 should be **demoted/replaced** by WP20 in the candidate manuscript stack.

The remaining questions are no longer whether a residue law exists, but:

1. whether the conditional-score covariance decomposition `r delta_0+nu` can be shown automatically for a broad named detector class rather than assumed;
2. whether finite total variation of `nu` follows from a convenient physical detector mixing condition (finite-state Markov, geometrically ergodic hidden state, finite-memory selector, etc.);
3. whether the covariance-atom Fisher interpretation has direct prior art in stationary observation-channel/statistical-experiment literature.

The theorem itself is now rigorous under explicit assumptions and does not require pointwise spectral convergence.
