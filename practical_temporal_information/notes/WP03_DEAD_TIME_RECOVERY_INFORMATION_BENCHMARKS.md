# WP03 — Dead time, recovery randomness, and practical timestamp-information benchmarks

**Date:** 2026-08-23

**Status:** practical translation of frozen Paper-2 theorems complete. No new upstream theorem is claimed here. The contribution is a detector-characterization/falsification formulation using ordinary count-rate, modulation-transfer, noise-spectrum, pair-correlation, and interval-statistic measurements.

## Purpose

WP01 showed that ordinary linear Gaussian photodetector information is weighted by `1/NEP(f)^2`.

WP02 showed that ideal photon timestamps carry

`Tr F/T=lambda_0`

for fractional two-quadrature modulation and that independent timing jitter multiplies the spectrum by `|Phi_J|^2`.

WP03 asks what happens when the detector has **memory** from paralyzable dead time or random recovery.

The key practical result inherited from the frozen random-time program is:

> a detector's conventional count-rate saturation curve can be completely insufficient to determine its temporal information channel.

The strongest tests below require only timestamp records and standard modulation/noise measurements.

---

# Part I — deterministic paralyzable detector: paralysis is frequency selective

## 1. Standard Type-II model

Incident events form a Poisson process with rate

`lambda_epsilon(t)=lambda[1+epsilon u(t)]`.

A deterministic paralyzable detector has dead/recovery time `tau`: an event at time `t` is registered only if no incident event occurred in `(t-tau,t)`, and every incident event restarts the dead interval.

The homogeneous registered count rate is the textbook relation

**`r(lambda)=lambda exp(-lambda tau)`.**

Its maximum occurs at

`rho=lambda tau=1`,

so

`lambda_*=1/tau`,

`r_*=1/(e tau)`.

At this operating point the conventional mean count curve has zero slope:

`dr/dlambda=0`.

The frozen random-time theorem is stronger: the **complete stationary timestamp record** is locally blind to a uniform/DC fractional rate perturbation,

**`G(0)=0`.**

Here `G(omega)` is the output Fisher-information retention relative to the incident Poisson source for a weak temporal mode.

## 2. Every nonzero temporal frequency survives

For deterministic Type-II recovery at `rho=1`, the frozen theorem gives

**`G(omega)>0` for every `omega != 0`.**

Thus exact DC blindness is an isolated information singularity, not total paralysis of the timestamp channel.

A rigorous lower bound obtainable from a single optimally phased Fourier statistic of the registered events is

`G_1(omega) >= L_1(y)`, `y=omega tau`,

with

`L_1(y)=e^-1 [1-2 sin(y)/y + 2(1-cos y)/y^2] / [1-(2/e) sin(y)/y]`.

Near DC,

`L_1(y)=y^2/[4(e-2)] + O(y^4)`.

At

`omega tau=pi`, i.e.

**`f=1/(2 tau)`,**

one has the rigorous bound

**`G(pi/tau) >= e^-1(1+4/pi^2) = 0.51697536...`.**

The frozen exact Volterra calculation gives approximately

`G(pi/tau) ~= 0.52814`.

The exact high-frequency limit is

**`lim_|omega|->infinity G(omega)=1/e ~= 0.367879`.**

### Dimensional benchmark

For a detector with deterministic `tau=10 ns`:

- paralysis maximum incident rate: `lambda_*=100 MHz`;
- mean registered rate there: `r_*=100/e MHz ~=36.79 MHz`;
- DC timestamp Fisher retention: `G(0)=0`;
- test frequency `f=1/(2tau)=50 MHz`;
- guaranteed retained fractional-modulation FI: `G>=0.516975`;
- exact model value: about `0.52814`.

So the same detector can be completely first-order blind to a uniform rate change at the saturation maximum while retaining **more than half** of the source Fisher information for a 50 MHz modulation.

This is a highly concrete falsification target.

## 3. It can be tested without reconstructing the full likelihood

For sinusoidal modulation, the ordinary first-harmonic registered-rate transfer is

`delta r/r = epsilon exp(i omega t) M_rho(y)`

with

`M_rho(y)=1-rho(1-exp(-iy))/(iy)`.

The baseline registered-event Bartlett noise spectrum is

`S_Y(omega)=r[1-2 rho exp(-rho) sin(y)/y]`.

The optimally phased Fourier statistic therefore gives the measurable information lower bound

`G_rho(omega) >= exp(-rho)|M_rho(y)|^2/[1-2rho exp(-rho)sin(y)/y]`.

Everything on the right can be obtained from standard detector characterization:

1. baseline incident rate `lambda`;
2. dead time `tau`;
3. measured first-harmonic response of the registered count stream;
4. registered-event noise/Bartlett spectrum at the modulation frequency.

Thus Paper 4 does not need to ask an experimentalist to compute a sophisticated point-process likelihood before obtaining a nonzero Fisher-information witness.

## 4. Falsification test A — deterministic Type-II spectral escape

At calibrated `lambda tau=1`:

1. verify the mean count-rate derivative is zero near DC;
2. apply a weak sinusoidal fractional intensity modulation;
3. measure registered-event first-harmonic response and timestamp Fourier-noise spectrum;
4. form the information lower bound above.

Predictions of the ideal deterministic Type-II model:

- `G(0)=0`;
- any nonzero frequency gives positive information;
- at `f=1/(2tau)`, `G>=0.516975`;
- at high frequency, full-record `G ->1/e`.

A calibrated violation would falsify the ideal deterministic paralyzable model or the theorem assumptions, not merely a fitted time constant.

---

# Part II — random recovery: identical saturation curve, different information

## 5. General iid Type-II recovery class

Now every incident Poisson event starts an iid recovery interval `T>=0` with finite positive mean

`m=E[T]`.

Registered events are starts of the resulting busy clusters.

A classical and crucial fact is

**`r(lambda)=lambda exp(-lambda m)`**

for **every** recovery distribution having the same mean `m`.

Therefore the complete conventional homogeneous saturation curve depends only on mean recovery.

The common maximum is

`lambda_*=1/m`,

`r_*=1/(em)`.

The frozen Paper-2 theorem proves that the stationary complete timestamp Fisher retention at this common maximum satisfies

**`G_DC=0 iff T=m almost surely`.**

Thus deterministic recovery is the **unique** finite-mean iid recovery law that becomes completely DC-information blind at the common count maximum.

Every genuinely random recovery law has positive timestamp Fisher information there, even though the mean count-rate slope is zero for all of them.

This is a much stronger practical statement than ordinary saturation characterization.

## 6. Simple bounded interval witness — no full FI fit required

Let `D` be one registered inter-event interval at the count maximum and choose any `s>0`.

Define the bounded statistic

**`Z_s=exp(-sD)`**, `0<Z_s<=1`.

Under a fractional source-rate perturbation

`lambda_epsilon=lambda_*(1+epsilon)`,

the frozen theorem gives

**`d/d epsilon E[Z_s]|_0 = 0` iff recovery is deterministic**, and

**`d/d epsilon E[Z_s]|_0 >0` for every nondegenerate finite-mean recovery law.**

This is a particularly practical test because it requires only registered intervals and a small incident-rate dither around the saturation maximum.

A convenient dimensionless choice is `s=1/m`, giving `Z=exp(-D/m)`.

### Falsification test B — recovery-randomness witness

1. determine mean recovery `m` and operate at `lambda=1/m`;
2. acquire timestamp records at `lambda(1+epsilon)` and `lambda(1-epsilon)` for small `epsilon`;
3. compute the sample mean of `exp(-D/m)` from registered intervals;
4. estimate the symmetric finite-difference derivative.

Ideal generalized-Type-II prediction:

- deterministic recovery: derivative tends to zero;
- any nondegenerate iid recovery with finite mean: derivative is strictly positive.

A nondegenerate recovery distribution together with a zero derivative in the asymptotic small-dither limit would contradict the generalized iid-Type-II model/theorem assumptions.

This test is stronger operationally than merely estimating the recovery variance because it is sensitive to the full recovery law.

---

# Part III — exact same-mean/same-variance practical counterexample

## 7. Two detectors conventional characterization cannot distinguish

Scale the frozen WP19 construction to an ordinary mean recovery

**`m=10 ns`.**

### Recovery law A

`P(T=5 ns)=1/2`,

`P(T=15 ns)=1/2`.

### Recovery law B

`P(T=2.5 ns)=2/9`,

`P(T=10 ns)=5/9`,

`P(T=17.5 ns)=2/9`.

Both have exactly

- mean recovery `10 ns`;
- variance `25 ns^2`;
- standard deviation `5 ns`;
- coefficient of variation `0.5`;
- the entire same conventional saturation curve

`r(lambda)=lambda exp[-lambda(10 ns)]`.

Therefore they share the same count maximum:

`lambda_*=100 MHz`,

`r_*=36.79 MHz`,

and the same zero slope there.

A characterization consisting of mean dead time, recovery variance/CV, and the complete mean input-output count curve cannot distinguish them.

## 8. Yet their registered-event pair correlations are very different

At the shared maximum `lambda m=1`, evaluate the normalized pair correlation at lag

`t=0.75m=7.5 ns`.

The exact frozen formulas give

**Law A:** `g_A^(2)(7.5 ns)=0.7274957073...`

**Law B:** `g_B^(2)(7.5 ns)=0.3188717529...`

The values differ by more than a factor of two despite identical mean, variance/CV, and saturation curve.

Their local fractional-rate derivatives at the same operating point and lag are also different:

`dot g_A^(2)=0.2728108902...`,

`dot g_B^(2)=0.1151481330...`.

A standard histogram of registered-event pair delays therefore reveals recovery information that conventional saturation measurements discard.

## 9. One-bit interval statistic gives an exact information separation

Use only the binary statistic

`Z=1{D<=0.4m}`.

For `m=10 ns`, the threshold is

**`D<=4 ns`.**

### Law A

Since every recovery duration is at least `5 ns`,

`P(D<=4 ns)=0`

for every incident rate, so this statistic carries exactly zero Fisher information.

### Law B

At `lambda m=1`, the exact result is

**`P(D<=4 ns)=0.024502903710...`**

and its derivative with respect to fractional incident-rate perturbation is

**`dot p=0.016975628075...`.**

The Bernoulli Fisher information per registered cycle is

`I_Z=0.0120561368424...`,

and the source-normalized per-time witness is

**`G_Z=0.00443520488427... >0`.**

Thus even **one bit per registered interval** distinguishes the information channels of two detectors that are identical under the standard mean/variance/saturation summary.

This is a strong practical illustration for Paper 4 because no full timestamp likelihood reconstruction is required.

## 10. Full timestamp FI also differs numerically

The frozen converged Volterra calculation gives at `lambda m=1`:

Law A:

`G_DC ~=0.01765400847`.

Law B:

`G_DC ~=0.01920433799`.

The difference is about `8.78%`.

This scalar difference is a highly converged numerical calibration; the stronger exact theorem is the difference of the accessible timestamp experiment/statistics above.

---

# Part IV — what this means for standard photodetector characterization

## 11. Count-rate saturation is not an information-transfer curve

For generalized Type-II detectors, the conventional relation

`r(lambda)=lambda exp(-lambda m)`

can be identical while

- pair correlation differs;
- interval statistics differ;
- local timestamp response differs;
- Fisher information differs;
- one detector can be information-singular while another is not.

Therefore standard reporting of

- mean dead/recovery time;
- recovery CV;
- maximum count rate;
- homogeneous saturation curve;

is insufficient to determine temporal information transfer.

A practical characterization aimed at temporal estimation should additionally report at least one of:

1. registered inter-event distribution under controlled illumination;
2. pair-correlation function;
3. frequency-resolved timestamp response/noise spectrum;
4. likelihood/Fisher spectrum or a certified lower-bound witness.

## 12. Connection to WP01/WP02

The practical hierarchy now becomes:

- **linear analog detector:** `Tr F/T=2/NEP^2`;
- **ideal event detector:** `Tr F/T=lambda_0`;
- **independent timing jitter:** multiply by `|Phi_J|^2`;
- **memoryful Type-II detector:** no scalar NEP/count-rate factor is generally sufficient; the information resides in the trajectory statistics and is frequency dependent.

This is exactly where a likelihood-defined information benchmark becomes useful rather than cosmetic.

## 13. Candidate Paper-4 figure set from WP03

A strong practical manuscript could use three figures:

1. **Information high-pass at paralysis:** plot conventional mean-count slope versus timestamp `G(f)` for deterministic Type-II at `lambda tau=1`, marking `G(0)=0`, `f=1/(2tau)`, and the `1/e` high-frequency asymptote.
2. **Same saturation, different timestamps:** overlay identical `r(lambda)` for laws A/B, then show their pair-correlation curves or the single lag `7.5 ns` contrast.
3. **One-bit falsification statistic:** probability `P(D<=4 ns)` versus incident rate for laws A/B, showing identically zero versus positive/locally responsive behavior.

These are standard detector plots rather than abstract resource diagrams.

## 14. Publication significance assessment after WP03

WP03 materially strengthens the case for a fourth paper.

WP01–WP02 alone could be viewed as tutorial translation. WP03 supplies a nontrivial practical message:

> **conventional count-rate/dead-time characterization can provably fail to determine a detector's temporal information transfer, even after mean recovery, variance/CV, and the full saturation curve are fixed.**

Moreover, the theory supplies simple observable witnesses and quantitative tests.

This is potentially publishable if prior-art review confirms that the specific integrated benchmarking/falsification framing and the exact same-curve information counterexamples are not already standard in detector characterization literature.

## 15. Claim discipline

Do not claim novelty for:

- the classical paralyzable count-rate law;
- modulated paralyzable mean response;
- renewal/Bartlett spectra;
- random-dead-time pair-correlation formulas as such;
- generic point-process likelihood theory.

The candidate contribution is the temporal-information consequence and practical falsification/benchmarking framework built from the frozen exact results.

## Next

WP04: construct an equally standard optical experiment for the **survival-to-synthesis transition** by comparing pre-seeded optical sidebands with baseline-empty sidebands under weak modulation. The target is an experimentally legible second-order curvature law, not another density-operator abstraction.
