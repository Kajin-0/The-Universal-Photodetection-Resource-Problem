# Research Log — Round 18: Rev9 translational grounding

**Date:** 2026-08-20

## Trigger

A translational review judged the Rev8 theorem stack mathematically strong but too abstract for device physicists and experimentalists. It proposed a canonical IRF library, a direct histogram estimator, support-based bounds, mark-resource examples, a circuit analogy, a preamplifier cascade application, and a clearer DC explanation.

The review direction was valuable, but several proposed formulas/interpretations were mathematically incorrect. Rev9 implements the useful grounding only after correcting those points.

## What Rev9 changes

Rev9 does **not** broaden the theorem class or alter the Rev8 theorem stack. It adds an operational-translation section plus two short interpretive notes.

### Canonical timing-law library

For a single unresolved mark,

`G(omega)=eta |H(omega)|^2`,

and

`B_FI = (1/2) int f(t)^2 dt`.

Closed forms are now given for:

- Gaussian timing-error idealization: `G/eta = exp(-sigma^2 omega^2)`, `B_FI = 1/(4 sqrt(pi) sigma)`;
- exponential wait: `G/eta = Lambda^2/(Lambda^2+omega^2)`, `B_FI=Lambda/4`;
- uniform delay on `[0,T]`: `G/eta=sinc^2(omega T/2)`, `B_FI=1/(2T)`;
- `k` serial exponential waits: existing Erlang result carried into the table;
- Gaussian timing error convolved with an exponential wait:
  `G/eta = exp(-sigma^2 omega^2) Lambda^2/(Lambda^2+omega^2)` and
  `B_FI=(Lambda/4) exp(Lambda^2 sigma^2) erfc(Lambda sigma)`.

For the exponential model,

`B_FI/f_3dB = pi/2`.

For the Gaussian--exponential convolution,

`B_FI <= min(Lambda/4, 1/(4 sqrt(pi) sigma))`.

The Gaussian row is explicitly labeled as the usual two-sided timing-error idealization after subtracting a known latency, not as a strictly causal nonnegative delay density.

### Direct estimator from a digitized IRF histogram

The proposed review formula contained an incorrect efficiency prefactor. For a **single mark** with normalized conditional timing density, capture efficiency cancels from the DC-normalized equivalent bandwidth:

`B_FI = (1/2) int f^2`.

For equal-width bins `Delta t` with conditional-on-capture probabilities `p_i`, the piecewise-constant binned bandwidth is

`B_FI^(Delta t) = [sum_i p_i^2]/(2 Delta t)`.

For empirical counts `n_i`, `N=sum_i n_i`, the naive plug-in estimator is

`[sum_i (n_i/N)^2]/(2 Delta t)`.

Its self-collision bias is removed exactly, conditional on `N>1`, by the U-statistic

`Bhat_FI,U^(Delta t) = [sum_i n_i(n_i-1)]/[2 Delta t N(N-1)]`.

This is unbiased for the **binned** collision quantity.

Cauchy--Schwarz on each bin gives

`B_FI^(Delta t) <= B_FI`,

so finite timing bins hide timing concentration. Under refining partitions with maximum bin width tending to zero, the binned quantity converges to `B_FI` for `f in L2`.

### Finite-support correction

The proposed review had the support inequality in the wrong direction. If a normalized density is supported on an interval of length `T`, then

`1=(int f)^2 <= T int f^2`,

hence

`B_FI >= 1/(2T)`.

The uniform density saturates this lower bound.

There is **no support-only upper bound** on `B_FI`: a density can concentrate on an arbitrarily narrow subinterval while remaining inside the same outer support.

An actual concentration ceiling is a separate resource. If `||f||_infty <= M`, then

`B_FI <= M/2`.

A geometric device length or maximum drift time does not by itself imply such an `M`.

### Mark as an information-resource gradient

For discrete fine marks,

`G_fine = sum_m kappa_m |H_m|^2`.

Discarding the mark gives

`H_no-mark = (1/eta) sum_m kappa_m H_m`,

and Jensen gives

`G_no-mark = eta |H_no-mark|^2 <= G_fine`.

If an accessible primary-event mark identifies the realized latency exactly, then each conditional delay is atomic and `G=eta` for all frequency.

A key correction to the translational review is made explicit: a downstream TDC does **not** create missing pre-registration information merely by digitizing the same delayed event more finely. The perfect-mark limit requires additional primary-event side information predictive of the otherwise unresolved latency.

### Cascade / preamplifier correction

The requested statement that a deterministic TIA RC pole simply multiplies the detector Fisher transfer would conflict with the manuscript's data-processing logic.

The exact product law applies to independent unresolved **stochastic delay stages**. A unit-efficiency stage with characteristic function `H_a` gives

`G_total = G_det |H_a|^2`.

A known, noiseless, invertible deterministic TIA filter does not by itself reduce Fisher information. It becomes an information bottleneck only after additive noise, finite sampling/bandwidth, saturation, thresholding, noninvertibility, or unresolved stochastic latency is included. The measured-record FI is then below ideal `G`, but not generically equal to `G |H_TIA|^2`.

### DC normalization clarification

The translational review suggested describing `G(0)=eta` as AC-normalized and multiplying by two for DC. That would be incorrect.

Rev9 now states explicitly:

- absolute incident FI rate is `Phi_0/2` for nonzero sinusoidal modulation under the paper's parameterization;
- exact DC absolute incident FI rate is `Phi_0`;
- `G` is a ratio, so `G(0)=eta` already uses the correct DC normalization;
- the factor of two matters only when converting normalized transfer back to an absolute FI rate.

### Thermodynamic engineering interpretation

The rare-fast family is translated as a hidden fast local mode with vanishing stationary duty cycle:

`lambda_1 ~ R`, `pi_1 ~ 1/R`,

so stationary traffic can remain `O(1)` while the conditional transient rate diverges. This is described as analogous to a fast trap, avalanche substate, or other internal transient that is rarely occupied. The paper deliberately avoids the review's misleading “hidden high-pass cutoff” phrasing; `lambda_1` is a local stochastic escape/pole scale, not generically a circuit high-pass cutoff.

## Verification

Canonical generated Rev9 source:

- `event_resource_theorem_rev9.tex` SHA-256:
  `79d0da661ba394b6064a73103cce4db157f634d2d4b5d47a674c7cd1552af6fc`
- `section_practical_grounding_rev9.tex` SHA-256:
  `b4702642705b01ef811e95f5a3d2d0686bb951122c337fd438d0b53fa0a18c3f`

Full canonical Rev9 build:

- 30 pages;
- PDF SHA-256 `2d8c93a98840d303a1f32cc3c67cd4c2c6d46a4010e440317691cae09df1f0cc`;
- no undefined citations or cross-references;
- only inherited overfull box: approximately `2.45667 pt` around `timing-concentration` in the rare-fast Appendix;
- one harmless underfull table cell warning.

The new pages were visually inspected: DC note, canonical IRF table, estimator, finite-support result, mark hierarchy, preamplifier caveat, thermodynamic interpretation, and PRApplied Data Availability/Appendix transition.

PRApplied submission build:

- 30 pages;
- PDF SHA-256 `5e4c17e7a7e3a8f26172e770b43d9391f88d20e0252cfdc9425e530cbfec9111`;
- submission TeX SHA-256 `b097f8763c25928cdd771b49d257a377980f9e883596b2a41826b69ff86c4ad2`;
- final package ZIP SHA-256 recorded externally as `c612899d536f4653e872f179f8b9fbea61264ed37e3120ac68fb1813ac5b913d`.

## Publication posture

Rev9 is now the preferred submission candidate because it preserves the airtight theorem stack while materially lowering the abstraction barrier for detector physicists.

Do not add additional “grounding” that silently changes the observation model. In particular:

- do not treat a deterministic RC/TIA pole as stochastic timing loss without an explicit noise/coarse-graining model;
- do not claim finite support upper-bounds `B_FI`;
- do not claim a downstream digitizer can recover information that was already lost before the primary record;
- do not reintroduce an incorrect factor-of-two into `G(0)`.

Further additions should be accepted only if they are equally operational and equally exact.
