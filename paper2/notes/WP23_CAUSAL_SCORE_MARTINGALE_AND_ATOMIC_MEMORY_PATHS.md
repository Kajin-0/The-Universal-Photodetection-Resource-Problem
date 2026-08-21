# WP23 — Causal counting-process score martingale and atomic memory paths

**Status:** adversarial extension of WP22; prevents an overbroad causal-selector theorem and sharpens the physical meaning of the covariance atom.

**Date:** 2026-08-21

The central lesson is:

> Causality alone does **not** make the high-frequency Fisher residue equal to the immediately visible event fraction. A perfectly sharp delayed memory response can contribute additional zero-lag Fisher covariance through its self-correlation. The robust invariant is the total atomic timing content of the conditional score.

This work package uses standard counting-process likelihood/martingale theory. No novelty is claimed for the score-martingale representation itself.

---

## 1. Standard causal counting-process likelihood representation

Let an observed simple counting process `Y` have predictable intensity `q_t^epsilon` under a local source perturbation parameter `epsilon`. Under the standard multiplicative-intensity likelihood regularity, the local score is

`S_u^Y = int dot(log q_t)[u] [dY_t-q_t dt]`,

where

`q_t=q_t^0`

and

`dot(log q_t)[u] = d/d epsilon log q_t^epsilon |_{epsilon=0}`.

Writing the output innovation martingale as

`dM_t^Y=dY_t-q_tdt`,

we have

`S_u^Y=int h_t[u] dM_t^Y`,

with

`h_t[u]=dot(log q_t)[u]`.

The Fisher bilinear form follows from the counting-process martingale isometry:

`boxed:`

`F_Y[u,v]=E int q_t h_t[u] h_t[v] dt`.

This is standard Aalen/Andersen-Gill counting-process likelihood theory and must be credited as such.

---

## 2. Causal exact-timestamp selector factorization

Suppose the incident process is Poisson with deterministic local intensity

`lambda_epsilon(t)=lambda[1+epsilon u(t)]`,

and the detector is a causal parameter-independent exact-timestamp selector: every observed event is an incident event and the keep/drop decision is made causally from detector state/history plus parameter-independent internal randomness.

With respect to the observed filtration, the output intensity has the natural factorization

`q_t^epsilon=lambda_epsilon(t) alpha_t^epsilon`,

where `alpha_t^epsilon` is the predictable posterior probability/acceptance factor that an incident event at `t` will be registered given the observed past.

At baseline,

`q_t=lambda alpha_t`,

and stationarity gives

`E[q_t]=r`,

the registered output rate.

If the acceptance factor is DQM-differentiable with respect to the source waveform, write

`B_t[u]=d/d epsilon log alpha_t^epsilon |_{0}`.

Because the source intensity contributes multiplicatively and instantaneously,

`boxed: h_t[u]=u(t)+B_t[u]`.

For a genuinely causal detector, `B_t[u]` depends only on source perturbations before `t` (modulo a zero-measure convention at the endpoint). Thus the score splits into an immediate source term plus a causal detector-memory term.

Substitution into the martingale Fisher form gives

`F_Y[u,v]`

`=E int q_t [u(t)+B_t[u]][v(t)+B_t[v]]dt`.

The first term alone is

`r int u(t)v(t)dt`,

which corresponds to an `r delta_0` Fisher-covariance atom.

The crucial question is whether the memory terms can add additional zero-lag atoms.

---

## 3. Causality alone is insufficient: exact delayed memory counterexample

Consider the abstract stationary causal score response

`B_t[u]=c u(t-tau)`,

with fixed `tau>0` and real constant `c`.

For simplicity take `q_t=r` deterministic. Then

`h_t[u]=u(t)+c u(t-tau)`

and

`F_Y[u,v]=r int [u(t)+c u(t-tau)][v(t)+c v(t-tau)]dt`.

For Fourier mode `omega`, the normalized multiplier is proportional to

`|1+c exp(-i omega tau)|^2`

`=1+c^2+2c cos(omega tau)`.

Therefore the proportional high-frequency band average obeys

`boxed:`

`<G>_high -> (r/lambda)(1+c^2)`,

not `r/lambda`.

The cross terms generate covariance atoms at lags `+/-tau`, which oscillate and average to zero. But the self-correlation of the delayed atomic path produces another **zero-lag atom** of weight `r c^2`.

Thus a strictly causal exact-delay memory path survives high-frequency averaging.

### Important scope note

This algebraic counterexample is a legitimate causal counting-process score response. It is not yet asserted that every such `B_t` can be realized by a physically ordinary `Y<=N` event-selector whose only internal dynamics are event-triggered recovery intervals. In many physical selector models, memory kernels are ordinary functions over nonzero time intervals rather than delta delays, and the extra atomic term is absent.

The counterexample is sufficient for the logical point:

`causality by itself does not imply residue = r/lambda`.

Additional **non-atomic/diffuse memory-response regularity** is required.

---

## 4. General atomic memory decomposition

The preceding example suggests a sharper resource decomposition.

Suppose, in a stationary scalar idealization, the score-response operator has impulse representation

`h = k*u`,

with atomic-plus-diffuse timing response

`k(dt)=sum_j c_j delta_{tau_j}(dt)+k_c(t)dt`,

where the delays `tau_j` are distinct and the diffuse component is sufficiently regular that its Fourier transform vanishes in high-frequency Cesaro mean (for example `k_c in L2`, with corresponding finite-energy assumptions).

For deterministic stationary innovation rate `r`,

`G(omega)=(r/lambda)|k_hat(omega)|^2`.

The high-frequency Cesaro average of cross terms between distinct atomic delays vanishes, as do atomic-diffuse and diffuse-diffuse contributions under the stated regularity. The surviving constant is

`boxed:`

`lim <G>_high = (r/lambda) sum_j |c_j|^2`.

For an exact-timestamp selector, the immediate path has

`tau_0=0`, `c_0=1`.

Therefore

`r/lambda`

is the **minimum atomic-path contribution** in this idealized causal representation; any additional perfectly sharp delayed score path adds positive high-frequency Cesaro retention.

This is the direct analogue of the atomic timing residue in Paper 1, but now applied to the **conditional score response** rather than an independent-event registration kernel.

---

## 5. Diffuse causal memory recovers the WP22 selector corollary

If the causal memory response `B` has no atomic timing component and its induced Fisher correction is represented by a finite lag measure with no zero-lag atom, then the only atomic score path is the direct coefficient `1` multiplying `u(t)`.

In that case

`a=r`

and WP22 gives

`boxed: <G>_high -> r/lambda`.

Thus the physically useful selector theorem should be stated as:

> **For a causal exact-timestamp selector whose hidden-state/source-response memory is non-atomic in timing and satisfies the stated finite-covariance regularity, the high-frequency Cesaro Fisher residue equals the registered-event fraction `r/lambda`.**

The non-atomic-memory qualification is substantive, not cosmetic.

WP22's diffuse-posterior/Palm conditions are one sufficient route to this conclusion. The causal score-martingale formulation supplies another route if the acceptance-response operator can be shown to have no atomic delay components.

---

## 6. Interpretation: the resource is atomic timing-path energy

The correct physical invariant is stronger than “visible events.”

A detector can retain high-frequency local Fisher information through any part of the complete output record that carries **perfectly sharp timing relative to the source perturbation**, whether that timing appears as:

1. an immediately visible incident-event timestamp;
2. a deterministic delayed registration path;
3. a perfectly sharp internal timing mark or memory path that later modulates an observable event process;
4. any other atomic component of the conditional-score timing response.

Diffuse recovery memory, ordinary jitter distributions, and smooth posterior-memory responses contribute continuous timing structure whose high-frequency Cesaro energy vanishes under finite-energy/mixing assumptions.

Therefore the robust resource statement is:

`boxed:`

`high-frequency Cesaro Fisher retention = atomic timing energy in the conditional score / source Fisher normalization`.

WP22 expresses the same fact invariantly through the zero-lag covariance atom `a=Gamma_M({0})`.

---

## 7. Connection to Paper 1

Paper 1 already distinguishes atomic and diffuse timing components.

For an independent-event delay law with an atomic deterministic latency, the transfer magnitude does not decay at high frequency. A diffuse timing density does decay under ordinary regularity.

WP23 shows the analogous phenomenon survives in the arbitrary-memory setting at the level of the **conditional score**:

- exact timing atoms generate nonzero asymptotic/Cesaro residue;
- diffuse timing response washes out at high frequency;
- memory need not be absent; what matters is whether the memory timing is atomic or diffuse.

This gives a potentially useful unifying message across Paper 1 and Paper 2 without claiming that the harmonic-analysis fact itself is novel.

---

## 8. Prior-art boundary

The following are standard:

- counting-process likelihoods written as stochastic integrals against innovation martingales;
- martingale isometry for Fisher information;
- multiplicative-intensity models;
- causal linear response and delay operators;
- Fourier spectra of discrete delays;
- Cesaro averaging of oscillatory cross terms;
- spectral decompositions of point-process innovations;
- atomic/diffuse decomposition of measures.

The candidate detector-specific contribution is only the synthesis with the UPRP Fisher-channel framework:

> the atomic part of the **conditional source-score timing response**, not dead time or recovery duration, controls the robust high-frequency information residue of a causal detector.

No priority claim is certified.

---

## 9. Consequence for WP22 and manuscript wording

WP22 remains correct as an abstract covariance-atom theorem.

Its regular exact-timestamp-selector corollary remains correct under its explicit diffuse-posterior/Palm assumptions.

WP23 adds two restrictions/interpretations:

1. **do not replace those assumptions merely by “causal selector”; causality is too weak in abstract score space;**
2. interpret `a` as total atomic timing-path energy of the conditional score, of which immediate visible events are only one possible contribution.

Recommended manuscript hierarchy:

- universal theorem: residue `a/lambda`, where `a` is the zero-lag conditional-score covariance atom;
- causal/diffuse selector corollary: `a=r` and residue `r/lambda`;
- atomic-memory extension: additional exact-delay score paths add to `a` rather than averaging away.

---

## 10. Next proof question

The highest-value remaining structural question is now:

> For physically ordinary causal event-selector channels `Y<=N` generated by event-driven hidden states with no free source-synchronous clock, what minimal conditions guarantee that the acceptance-response memory is non-atomic, so that `a=r`?

A theorem here would convert the current sufficient diffuse-posterior assumption into a more microscopic detector-model condition.

Do not force such a theorem if the necessary assumptions simply restate non-atomic memory. The abstract WP22 theorem is already rigorous and sufficient for a manuscript if novelty survives.
