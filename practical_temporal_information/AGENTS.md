# AGENTS — Practical Temporal-Information Benchmarks

**Active branch:** `agent/practical-temporal-information-benchmarks`

The repository, not chat history, is authoritative.

## Mission

Create a fourth paper that brings the temporal-information resource program down to standard detector physics and explicit falsifiability. Every central result should identify what is measured, what is predicted, and what observation would contradict it.

Do not modify the frozen scientific theorem/proof layers of the PRXQ flagship, the random-time timestamp paper, or the PRA unitary-coupling paper unless this program exposes a genuine defect.

## Read first

1. `README.md`
2. `notes/WP01_LINEAR_GAUSSIAN_FISHER_NEP_BRIDGE.md`
3. `notes/WP02_POISSON_TIMESTAMPS_AND_JITTER.md`
4. `notes/WP03_DEAD_TIME_RECOVERY_INFORMATION_BENCHMARKS.md`
5. root `docs/CURRENT_RESEARCH_STATE.md`

## Current result stack

### WP01 — linear Gaussian detector

For peak optical-power quadratures and one-sided output PSD,

`F_xx/T=F_yy/T=|R(f)|^2/S_n(f)=1/NEP(f)^2`,

`Tr F/T=2/NEP(f)^2`.

For arbitrary weak waveform coordinates,

`F_ij=4 Re integral_0^infinity q_i*(f)q_j(f)/NEP(f)^2 df`.

The relevant information response is `|R|^2/S_n`, not responsivity alone, so response bandwidth and Fisher-information bandwidth need not coincide.

### WP02 — ideal timestamps and independent jitter

For fractional sinusoidal modulation of an ideal Poisson event rate,

`Tr F/T=lambda_0`.

For optical-power coordinates this exactly matches the analog shot-noise result `2/NEP_shot^2`.

Independent timestamp jitter gives

`Tr F/T=lambda_0 |Phi_J(Omega)|^2`.

Gaussian jitter gives

`Tr F/T=lambda_0 exp[-Omega^2 sigma_t^2]`,

`f_F,3dB=sqrt(ln2)/(2 pi sigma_t)`.

### WP03 — dead time/recovery: conventional saturation is insufficient

Deterministic paralyzable Type-II recovery has

`r(lambda)=lambda exp(-lambda tau)`.

At `lambda tau=1`, the **complete timestamp channel** satisfies

`G(0)=0`

but

`G(omega)>0` for every `omega !=0`.

At `omega tau=pi` (`f=1/(2tau)`),

`G>=0.51697536`,

with exact model value about `0.52814`, and

`G(omega)->1/e` at high frequency.

For `tau=10 ns`, the benchmark point is `lambda=100 MHz`, `r=36.79 MHz`, `f=50 MHz`.

For arbitrary iid recovery `T` with finite mean `m`, every recovery law shares

`r(lambda)=lambda exp(-lambda m)`.

At the common maximum `lambda m=1`,

**`G_DC=0 iff T=m almost surely`.**

Every genuinely random recovery law retains positive timestamp information despite the same zero mean-count slope.

A bounded practical witness uses `Z_s=exp(-sD)` from registered intervals. At the count maximum,

`d E[Z_s]/d epsilon=0` iff recovery is deterministic, and is strictly positive for every nondegenerate finite-mean recovery law.

WP03 also dimensionalizes the exact same-mean/same-variance counterexample to `m=10 ns`:

- Law A: `T=5 ns` or `15 ns`, each probability `1/2`;
- Law B: `T=2.5 ns` with `2/9`, `10 ns` with `5/9`, `17.5 ns` with `2/9`.

Both have mean `10 ns`, variance `25 ns^2`, CV `0.5`, and the entire identical saturation curve. Yet at `lambda=100 MHz` and lag `7.5 ns`,

`g_A^(2)=0.7274957`,

`g_B^(2)=0.3188718`.

The one-bit statistic `1{D<=4 ns}` has zero Fisher information for A but positive Fisher information for B; at the common maximum B has

`P(D<=4 ns)=0.0245029`,

`G_Z=0.00443520`.

This is the first clearly nontrivial practical Paper-4 result: mean dead time, recovery variance/CV, maximum count rate, and even the complete saturation curve do **not** determine temporal information transfer.

## Next work packages

- **WP04:** optical sideband survival-to-synthesis crossover with seeded and empty sidebands.
- **WP05:** textbook resonant-exchange interpretation of exact unitary-coupling cost.
- **WP06:** integrated falsification matrix and minimal practical manuscript theorem stack.
- **WP07:** dedicated prior-art/significance gate before manuscript drafting.

## Publication criterion

WP03 materially strengthens the case for a fourth paper. The likely thesis is no longer merely “Fisher information equals an inverse noise metric,” but:

> standard detector figures of merit can fail to determine temporal-information transfer; full response/noise/timestamp structure supplies falsifiable information benchmarks, and the upstream survival/synthesis laws predict where that information must physically reside.

Do not claim novelty for classical paralyzable count laws, renewal spectra, pair-correlation formulas, NEP, matched filtering, or generic Fisher statistics. Novelty must be assigned only after WP07.

## Documentation rule

After every material advance, update the corresponding note and this handoff. When the frontier changes, also update root `README.md`, `AGENTS.md`, `ROADMAP.md`, and `docs/CURRENT_RESEARCH_STATE.md`.
