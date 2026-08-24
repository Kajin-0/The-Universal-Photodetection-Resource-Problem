# WP02 — Ideal Poisson timestamps and independent timing jitter

**Date:** 2026-08-23

**Status:** analytical derivation complete for ideal Poisson detection, independent timestamp displacement, efficiency, and independent dark counts. Dead time/recovery/memory is deferred to WP03.

## Question

What does the temporal Fisher spectrum become in the most standard event-counting photodetector model, and how is it degraded by ordinary detector timing jitter?

The aim is to obtain formulas directly estimable from timestamp records and to cross-check them against the analog shot-noise/NEP bridge from WP01.

## Model and likelihood

Let detected events form an inhomogeneous Poisson process with rate

`lambda(t;x,y)=lambda_0 [1 + x cos(Omega t) + y sin(Omega t)]`,

where

- `lambda_0` is the baseline detected count rate in s^-1;
- `x,y` are dimensionless **fractional peak modulation quadratures**;
- `x^2+y^2` is small enough that the rate remains nonnegative;
- `Omega=2 pi f`.

For observed event times `{t_k}` in a window `[0,T]`,

`log L = sum_k log lambda(t_k) - integral_0^T lambda(t) dt`.

For an inhomogeneous Poisson process the Fisher matrix is

`F_ij = integral_0^T [partial_i lambda(t) partial_j lambda(t) / lambda(t)] dt`.

At the unmodulated baseline `x=y=0`,

`partial_x lambda=lambda_0 cos(Omega t)`

and

`partial_y lambda=lambda_0 sin(Omega t)`.

## Result 1 — ideal timestamp Fisher information

The exact finite-window entries are

`F_xx = lambda_0 [T/2 + sin(2 Omega T)/(4 Omega)]`,

`F_yy = lambda_0 [T/2 - sin(2 Omega T)/(4 Omega)]`,

`F_xy = lambda_0 [1-cos(2 Omega T)]/(4 Omega)`.

The trace is especially simple because `cos^2+sin^2=1`:

**`Tr F = lambda_0 T`**

for every `T` in the continuously illuminated Poisson model, not only asymptotically.

Hence the exact two-quadrature fractional-modulation Fisher rate is

**`Tr F/T = lambda_0`.**

When the observation spans an integer number of modulation periods, or for `Omega T >> 1`,

`F_xx/T -> lambda_0/2`,

`F_yy/T -> lambda_0/2`,

`F_xy/T -> 0`.

Thus the ideal event stream carries one unit of two-quadrature Fisher information per detected event for fractional modulation coordinates.

## Absolute optical-power coordinates

Let incident optical power be

`P(t)=P_0 + p_x cos(Omega t) + p_y sin(Omega t)`

and let ideal linear photon detection have

`lambda_0 = eta P_0/(hbar omega_opt)`,

where `eta` is total detection efficiency and `hbar omega_opt` is photon energy.

Since

`x=p_x/P_0`, `y=p_y/P_0`,

Fisher information transforms as

`F_pxp_x/T = lambda_0/(2 P_0^2)`

and similarly for `p_y`, so

**`Tr F_P/T = lambda_0/P_0^2 = eta/(hbar omega_opt P_0)`.**

Units are `1/(W^2 s)`, matching WP01.

## Result 2 — exact cross-check against analog shot-noise NEP

For an ideal unity-gain photodiode whose only output noise is Poisson shot noise,

`R_I = eta q/(hbar omega_opt)`

and the one-sided shot-current PSD is

`S_I = 2 q I_0 = 2 q^2 lambda_0`.

WP01 gives one-quadrature optical-power Fisher rate

`F_pxp_x/T = R_I^2/S_I`.

Substituting gives

`R_I^2/S_I = eta/(2 hbar omega_opt P_0)`,

which is exactly the timestamp result above.

Equivalently, the ideal shot-noise-limited NEP satisfies

`NEP_shot^2 = S_I/R_I^2 = 2 hbar omega_opt P_0/eta`,

so

**`Tr F_P/T = 2/NEP_shot^2`.**

This is an important consistency check: ideal analog shot-noise readout and the full Poisson timestamp likelihood carry the same local information about the weak optical-power quadratures when they describe the same physical counting process and no extra information is discarded.

## Result 3 — independent timing jitter

Assume each ideal event time `t_k` is independently displaced by a random jitter `J_k`, giving registered time

`t_k^reg = t_k + J_k`.

Let the jitter density be `g(J)` and characteristic function

`Phi_J(Omega)=E[exp(-i Omega J)]`.

By the displacement theorem for Poisson point processes, independently displaced points remain a Poisson process, with rate equal to the convolution of the ideal rate and `g`.

For a single sinusoidal mode the convolution multiplies the complex modulation amplitude by `Phi_J(Omega)`. In the real cosine/sine coordinates this is a rotation by `arg Phi_J` followed by an amplitude contraction `|Phi_J|`.

At baseline, the two-quadrature Fisher matrix is therefore multiplied by the positive matrix corresponding to that rotation/contraction. Its trace is

**`Tr F_jitter/T = lambda_0 |Phi_J(Omega)|^2`.**

For long/integer-period observations each diagonal becomes

`F_xx/T = F_yy/T = (lambda_0/2)|Phi_J(Omega)|^2`.

A deterministic timing offset has `|Phi_J|=1`: it rotates phase but does not reduce the two-quadrature Fisher trace. Random timing uncertainty reduces information through the modulus of the characteristic function.

### Gaussian timing jitter

For zero-mean Gaussian jitter with standard deviation `sigma_t`,

`Phi_J(Omega)=exp[-Omega^2 sigma_t^2/2]`,

so

**`Tr F_jitter/T = lambda_0 exp[-Omega^2 sigma_t^2]`.**

The Fisher response falls by 3 dB when

`exp[-Omega^2 sigma_t^2]=1/2`,

hence

**`f_F,3dB = sqrt(ln 2)/(2 pi sigma_t) ~= 0.1325/sigma_t`.**

This is a directly measurable timing-jitter information bandwidth.

### Low-frequency expansion

For any jitter distribution with finite variance,

`|Phi_J(Omega)|^2 = 1 - Omega^2 Var(J) + o(Omega^2)`

as `Omega -> 0`.

The mean delay affects only phase to leading order; variance controls the leading two-quadrature information loss.

## Result 4 — efficiency and dark counts

### Detection efficiency

Independent Bernoulli thinning of an incident Poisson photon stream by efficiency `eta` leaves a Poisson process with rate `lambda_s=eta Phi_0`. Therefore fractional-modulation Fisher rate simply scales with detected signal rate:

`Tr F/T = lambda_s`.

### Independent unmodulated dark counts

Let the signal count rate be `lambda_s` and an independent unmodulated dark process have rate `lambda_d`. The observed baseline rate is

`lambda_b=lambda_s+lambda_d`,

but only the signal component carries the modulation derivative. At baseline,

`partial_x lambda=lambda_s cos(Omega t)`,

`partial_y lambda=lambda_s sin(Omega t)`.

Therefore

**`Tr F/T = lambda_s^2/(lambda_s+lambda_d)`.**

With independent timing jitter acting on the signal timestamps,

**`Tr F/T = [lambda_s^2/(lambda_s+lambda_d)] |Phi_J(Omega)|^2`**

provided the dark process itself is unmodulated and the registered process remains the superposition of independent Poisson streams.

This provides a conventional event-detector benchmark incorporating quantum efficiency, dark counts, and timing jitter without invoking any abstract resource language.

## Practical timestamp Fisher estimator

For a parameterized point-process model `lambda(t;theta)`, the score from a timestamp record is

`partial_i log L = sum_k partial_i log lambda(t_k;theta) - integral_0^T partial_i lambda(t;theta) dt`.

The empirical Fisher matrix can therefore be estimated either by

1. repeated-record score covariance,
2. negative expected Hessian of the fitted likelihood, or
3. for a trusted fitted intensity model, direct numerical evaluation of `integral (partial_i lambda partial_j lambda/lambda) dt`.

For jittered records one may fit the convolved intensity or estimate the jitter transfer independently and compare against the predicted `|Phi_J|^2` attenuation.

## Falsification criteria

### Ideal Poisson model

Measured quantities:

- baseline event rate `lambda_0`;
- raw timestamps under weak known sine/cosine modulation;
- observation duration and modulation phase/frequency.

Prediction:

`Tr F/T=lambda_0` for fractional quadratures.

A reproducible statistically significant disagreement after correcting for efficiency definition, finite gating, background counts, and estimator bias falsifies the **ideal inhomogeneous-Poisson detector model** at that operating point.

### Independent-jitter model

Measured quantities:

- independently characterized timing-jitter distribution `g(J)`;
- timestamp Fisher spectrum versus modulation frequency.

Prediction:

`[Tr F(f)/T]/[Tr F(0)/T] = |Phi_J(2 pi f)|^2`

for an otherwise ideal Poisson detector with independent timestamp displacement.

If the measured normalized Fisher spectrum differs from the independently measured jitter characteristic-function modulus after known electronic filtering is removed, then timing jitter is not an independent displacement channel; detector memory, dead time, amplitude-time correlations, or another mechanism is present.

## Connection to standard detector physics

The sequence

`lambda_0 -> shot-noise PSD -> NEP_shot -> Fisher rate`

and the independent sequence

`timestamp likelihood -> Fisher rate`

produce the same result.

This lets Paper 4 compare analog and event detectors in one information language while still using each community's ordinary measurements.

## Scope boundary

WP02 does **not** include dead time, paralysis, recovery, afterpulsing, count-rate saturation, or correlated jitter. Those processes destroy the simple independent-Poisson displacement structure and belong in WP03.

## Prior-art discipline

Poisson-process Fisher information, shot-noise NEP, and characteristic-function attenuation under independent timing displacement are standard ingredients and are not claimed as individually new.

The possible publication value is their integration with the existing temporal spectral-resource program, explicit analog/timestamp equivalence, and the subsequent memory/survival/synthesis falsification tests.

## Next

WP03: derive practical dead-time/recovery benchmarks and identify which features of the **full timestamp Fisher spectrum** are invisible in conventional mean count-rate saturation curves. Reuse the existing random-time theorem rather than re-deriving it from scratch, and express its predictions in measurable detector quantities.
