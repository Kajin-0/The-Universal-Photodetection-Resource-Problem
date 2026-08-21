# WP22 — Conditional-score covariance-atom theorem and exact-timestamp-selector corollary

**Status:** adversarial proof repair / strengthening of WP20.

**Date:** 2026-08-21

This work package separates two statements that WP20 had partially conflated:

1. an **abstract stationary Fisher-covariance theorem**: the high-frequency Cesaro Fisher residue is the zero-lag atom of the conditional-score covariance measure divided by the incident Poisson rate;
2. an **exact-timestamp-selector corollary**: that atom equals the visible event rate `r` only under explicit diffuse-posterior / Palm second-order regularity.

The distinction is necessary. Exact timestamp selection `Y<=N` by itself does not logically prevent the complete keep/drop pattern from encoding singular information about hidden incident events. The universal invariant is therefore the **conditional-score covariance atom**, not automatically the visible-event fraction.

---

## 1. General stationary conditional-score random measure

Let the incident source be a homogeneous Poisson process on `R` of rate

`lambda>0`.

For a compactly supported waveform tangent `u`, the incident score is

`S_u = int u(t)[N(dt)-lambda dt]`.

Let `Y` denote the complete accessible record of an autonomous, parameter-independent detector channel. Assume the output score can be represented by integration against a centered stationary second-order random measure `M`:

`S_u^out = int u(t) M(dt)`.

Let `Gamma_M` be the reduced stationary covariance measure of `M`, defined so that

`E[int u(t)M(dt) int v(s)M(ds)]`

has spectral density/measure induced by `Gamma_M`.

Assume the covariance measure decomposes as

`Gamma_M = a delta_0 + nu`,

where

- `a>=0` is the zero-lag atomic mass;
- `nu` is a finite signed/Hermitian measure of finite total variation;
- `nu({0})=0`.

Then the WP10 Fisher multiplier admits the continuous Fourier-Stieltjes representative

`lambda G(omega) = a + nu_hat(omega)`.

The data-processing bound still implies `0<=G<=1` wherever this representative is used.

---

## 2. Abstract covariance-atom Cesaro theorem

For fixed `0<a0<b0<infinity`, define the proportional high-frequency band average

`Gbar_Omega = 1/[(b0-a0)Omega] int_{a0 Omega}^{b0 Omega} G(omega) d omega`.

Then

`Gbar_Omega - a/lambda`

`= (1/lambda) int K_Omega(t) nu(dt)`,

with

`K_Omega(t)`

`= 1/[(b0-a0)Omega] int_{a0 Omega}^{b0 Omega} exp(-i omega t)domega`.

For `t!=0`,

`K_Omega(t) -> 0`,

while

`K_Omega(0)=1`,

and for all `t`

`|K_Omega(t)|<=1`.

Finite total variation plus dominated convergence therefore gives

`lim_{Omega->infinity} int K_Omega(t)nu(dt)=nu({0})=0`.

Hence

`boxed: lim_{Omega->infinity} Gbar_Omega = a/lambda`.

The same proof gives the origin-centered average

`lim_{Omega->infinity} 1/(2Omega) int_{-Omega}^{Omega} G(omega)domega = a/lambda`.

### Interpretation

The robust high-frequency Cesaro invariant is

`boxed: high-frequency Fisher residue = zero-lag conditional-score covariance atom / incident rate`.

This statement does not refer to dead time, a recovery constant, or even event selection. It is a property of the complete conditional source score.

---

## 3. Wiener and Rajchman refinements

If `nu` is atomless everywhere, Wiener's theorem gives

`lim_{Omega->infinity} 1/(2Omega) int_{-Omega}^{Omega} |nu_hat(omega)|^2 d omega = 0`,

hence

`boxed: <|G-a/lambda|^2>_high band -> 0`.

If `nu` is Rajchman,

`nu_hat(omega)->0`,

then

`boxed: G(omega)->a/lambda` pointwise.

An `L1` covariance density is a familiar sufficient condition for the Rajchman property.

Thus the correct hierarchy is:

1. finite correction covariance measure -> Cesaro residue `a/lambda`;
2. atomless correction -> high-frequency mean-square convergence;
3. Rajchman correction -> pointwise convergence.

All of the harmonic-analysis statements above are standard and carry no novelty claim.

---

## 4. Quantitative finite-band error bound

For the proportional-band kernel,

`|K_Omega(t)| <= min(1, 2/[(b0-a0)Omega |t|])`.

Therefore

`|Gbar_Omega-a/lambda|`

`<= (1/lambda) int min(1,2/[(b0-a0)Omega |t|]) |nu|(dt)`.

For every `delta>0`,

`boxed:`

`|Gbar_Omega-a/lambda|`

`<= (1/lambda)[ |nu|((-delta,delta)) + 2 ||nu||_TV / ((b0-a0)Omega delta) ]`.

This gives a direct convergence-control formula from the amount of correction covariance concentrated near zero lag plus total correction covariance.

If `nu` has a locally bounded density near zero, choosing `delta` of order `Omega^{-1/2}` gives an `O(Omega^{-1/2})` generic bound. Stronger inverse-lag integrability can improve the rate to `O(Omega^{-1})`.

This quantitative estimate is useful operationally but is standard Fourier-measure analysis, not a novelty claim.

---

## 5. Exact-timestamp event-selector model

Now specialize to an autonomous detector whose observed event process is a history-dependent subset of incident Poisson events:

`Y<=N`

as simple counting measures, with selected timestamps preserved exactly.

Let the stationary observed rate be

`r = E[Y([0,1])]`.

Write hidden incident events as

`H=N-Y`.

Assume the conditional mean hidden-event measure given the **complete** observed record is diffuse:

`E[H(dt)|Y] = m_Y(t) dt`,

with stationary locally square-integrable density `m_Y(t)`.

Since

`E[m_Y(t)] = lambda-r`,

define the centered posterior hidden-intensity field

`xi_Y(t)=m_Y(t)-(lambda-r)`.

Then

`E[N(dt)-lambda dt | Y]`

`=Y(dt)-r dt + xi_Y(t)dt`.

Therefore the exact output score is

`S_u^out`

`= int u(t)[Y(dt)-r dt] + int u(t)xi_Y(t)dt`.

Define

`M(dt)=Y(dt)-r dt + xi_Y(t)dt`.

This is the conditional-score random measure to which the abstract theorem applies.

---

## 6. Why the zero-lag atom is `r` under explicit regularity

The equality

`Gamma_M({0})=r`

must be **derived under assumptions**, not declared universal from `Y<=N` alone.

Assume:

1. `Y` is stationary and simple with finite second moments on bounded windows;
2. its reduced covariance measure can be written
   
   `Gamma_Y = r delta_0 + gamma_Y^red`,
   
   with
   
   `gamma_Y^red({0})=0`;
3. `xi_Y` is an ordinary locally-square-integrable stationary random field;
4. the Palm first moments `E^0[xi_Y(h)]` exist as locally integrable functions of lag;
5. the stationary field covariance
   
   `c_xi(h)=E[xi_Y(0)xi_Y(h)]`
   
   exists as a locally integrable function;
6. the total reduced correction assembled below has finite total variation when the Cesaro theorem is invoked.

### 6.1 Point-process term

For a stationary simple point process,

`Cov[Y-rdt]`

contains the structural diagonal shot-noise atom

`r delta_0`.

The reduced distinct-event term has no atom at zero because simplicity excludes two distinct registered events at exactly the same time.

### 6.2 Point-field cross terms

Campbell/Palm reduction gives, schematically,

`E[Y(dt) xi_Y(s) ds]`

`= r dt E^0[xi_Y(s-t)] ds`.

After stationary reduction to lag `h=s-t`, the cross-covariance contribution therefore has density

`r E^0[xi_Y(h)] dh`.

The reverse cross term has density

`r E^0[xi_Y(-h)] dh`.

These terms are absolutely continuous in lag and therefore have no zero-lag atom.

### 6.3 Diffuse-field term

The covariance of `xi_Y(t)dt` is

`c_xi(h) dh`

after stationary reduction. This is also absolutely continuous and has no zero-lag atom.

### 6.4 Combined covariance decomposition

Under the assumptions above,

`boxed:`

`Gamma_M(dh)`

`= r delta_0(dh) + gamma_Y^red(dh)`

`+ [ r E^0[xi_Y(h)] + r E^0[xi_Y(-h)] + c_xi(h) ] dh`.

Consequently

`boxed: Gamma_M({0})=r`.

If the non-diagonal correction

`nu(dh)=gamma_Y^red(dh)`

`+[ r E^0[xi_Y(h)] + r E^0[xi_Y(-h)] + c_xi(h)]dh`

has finite total variation, the abstract theorem yields

`boxed:`

`lim_{Omega->infinity} 1/[(b0-a0)Omega] int_{a0 Omega}^{b0 Omega} G(omega)domega = r/lambda`.

This is the rigorous **exact-timestamp-selector corollary**.

---

## 7. Why diffuseness is a real assumption, not bookkeeping

It is tempting to argue:

`Y<=N` and selected timestamps are exact, therefore the high-frequency atom must always be exactly `r`.

That is too broad.

The complete future keep/drop pattern can, in principle, encode additional information about hidden incident-event times. For a sufficiently pathological history-dependent selector, the posterior conditional measure

`E[H(dt)|Y]`

need not remain diffuse with respect to Lebesgue measure. It can develop singular or atomic components tied to information encoded nonlocally into the observed record.

If the hidden posterior contains a singular component, then the conditional-score random measure contains more singular structure than

`Y-rdt + xi(t)dt`,

and cross/hidden terms can contribute additional zero-lag covariance atoms. In that case the abstract residue remains

`a/lambda`,

where

`a=Gamma_M({0})`,

but one may no longer identify `a` with `r`.

Therefore:

> **Exact visible timestamps guarantee an observed shot-noise contribution `r delta_0`; they do not, without posterior regularity, prove that this is the entire conditional-score zero-lag atom.**

This is the principal adversarial correction to WP20.

---

## 8. Relation to solved detector models

### Independent exact-timestamp thinning

The hidden posterior is diffuse and no memory correction remains. Then

`a=r=eta lambda`,

so

`G(omega)=eta`

at every frequency.

### Ideal nonparalyzable dead time

WP04 gives exactly

`G(omega)=r/lambda=1/(1+lambda tau_d)`.

Again the conditional-score atom exhausts the spectrum.

### Deterministic paralyzable Type II

WP07 independently proves

`G(omega)->r/lambda=exp(-lambda tau)`

pointwise, so it lies in the strongest Rajchman level. At paralysis,

`r/lambda=1/e`.

WP22 interprets this asymptotic constant as the zero-lag conditional-score covariance atom under the regular selector representation.

---

## 9. Prior-art / novelty boundary

The following ingredients are standard and must not be claimed as new:

- stationary random-measure covariance and spectral measures;
- shot-noise/diagonal atoms of simple point processes;
- Campbell and Palm formulas;
- Fourier transforms of finite measures;
- extraction of an atom by expanding Fourier averages;
- Wiener's theorem for Fourier-Stieltjes transforms;
- Rajchman/Riemann-Lebesgue decay conditions;
- Brillinger-type mixing / finite reduced-covariance measures;
- conditional expectation of scores and Fisher data processing;
- function-valued score covariance / Fisher kernels.

Close modern statistical prior art includes Daniel E. Clark (2026) on Bartlett identities and Fisher-information kernels for point processes. Neural spike-train literature also studies temporal Fisher information in dynamical point-process records. These literatures prevent any claim that score-covariance kernels or timing Fisher spectra are new mathematical objects.

The candidate detector-specific contribution, if novelty survives targeted audit, is the synthesis:

> For an autonomous photodetection channel, the high-frequency Cesaro retention of weak temporal Poisson-source Fisher information is controlled by the singular zero-lag component of the **conditional source-score covariance**. For regular exact-timestamp selectors with diffuse posterior hidden events, that atom is exactly the visible registered-event rate, giving residue `r/lambda` independent of the detailed memory dynamics.

No priority claim is certified.

---

## 10. Recommended theorem wording

### Theorem A — conditional-score covariance-atom residue

> Let a stationary Poisson-source detector channel admit a centered stationary conditional-score random measure `M` whose covariance measure is `Gamma_M=a delta_0+nu`, with `nu` finite in total variation and `nu({0})=0`. Then for every fixed `0<a0<b0`, the complete local Fisher-retention multiplier obeys
> 
> `lim_{Omega->infinity} [(b0-a0)Omega]^{-1} int_{a0Omega}^{b0Omega} G(omega)domega = a/lambda`.
> 
> If `nu` is atomless, convergence also holds in high-frequency mean square; if `nu` is Rajchman, `G(omega)->a/lambda` pointwise.

### Corollary B — regular exact-timestamp selector

> If, in addition, the detector output is a stationary simple exact-timestamp subset `Y<=N` of rate `r`, the posterior hidden-event conditional mean is diffuse, and the Palm/field second-order regularity of Section 6 holds, then `a=r`. Consequently the high-frequency Cesaro Fisher residue is `r/lambda`.

This is safer and stronger than the original WP08/WP20 wording because it makes the true invariant and the selector-specific assumptions explicit.

---

## 11. Decision impact

WP20 is **not invalidated**. Its harmonic-analysis core is correct, but its manuscript formulation should be replaced by the two-level WP22 statement.

Current status:

- abstract covariance-atom theorem: **rigorous under stated finite-measure assumptions**;
- selector identification `a=r`: **rigorous under explicit diffuse posterior + Palm/field regularity**;
- universal claim `a=r` from `Y<=N` alone: **withdrawn / not justified**;
- pointwise limit from finite covariance measure alone: already withdrawn in WP20;
- novelty: **uncertified**, requires targeted point-process information / dependent-thinning audit.

The key conceptual invariant is now cleaner:

`boxed: zero-lag conditional-score atom, not dead time, controls the robust high-frequency Fisher residue.`
