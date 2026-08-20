# Current Research State

**Date:** 2026-08-20

This is the first-stop scientific/publication state for UPRP. The active branch is:

`agent/uprp-core-theorem-round10`

## Current manuscript state

- `manuscript/event_resource_theorem_rev4.tex` is the last fully build-verified committed manuscript source.
- GitHub Actions verified Rev4 generation, full LaTeX compilation, and artifact upload for commit `0acd8ca6304585e44c89130ca6b31826884c85a8`.
- `notes/WP35_MARK_CONDITIONED_MARKOV_RATE_CORRECTION.md` subsequently identified one localized microscopic-rate wording defect in Rev4.
- `manuscript/apply_rev5.py` is the assertion-based Rev4 -> Rev5 editorial transformer.
- `.github/workflows/manuscript-check.yml` now generates and compiles `event_resource_theorem_rev5.tex` and uploads the Rev5 TeX/PDF artifacts.

The WP35 correction does **not** change the central event theorem, Wiener result, Parseval constant, collision resource, capture-weighted hazard theorem, WP33 fixed-jitter no-go, WP34 inverse cost, or WP29 thermodynamic gateway theorem.

---

# Detector class

The mature first-paper theorem is restricted to:

- autonomous/time-translation-invariant processing;
- independent-event/low-overlap operation;
- one primary electrical registration per captured photon;
- complete accessible primary-event marks;
- weak coherent/Poisson direct-detection intensity modulation;
- parameter-independent downstream background/processing for the FI upper-bound step.

It is not a universal speed law for every architecture called a photodetector.

---

# Exact marked-event transfer

Per incident photon,
\[
K(dm,d\tau)=\kappa(dm)\mu_m(d\tau),
\qquad
\eta=\kappa(\mathsf M)\le1.
\]

For sinusoidal source modulation,
\[
\boxed{
G(\omega)=\int_{\mathsf M}|H_m(\omega)|^2\kappa(dm).
}
\]

Any parameter-independent background addition or downstream stochastic map can only reduce FI.

---

# Resource hierarchy

## Exact atomic residue
If `p_j(m)` are the atoms of the mark-conditioned delay measure,
\[
\boxed{
\lim_{\Omega\to\infty}\frac1{2\Omega}
\int_{-\Omega}^{\Omega}G(\omega)d\omega
=
\int\kappa(dm)\sum_j p_j(m)^2.
}
\]

Purely non-atomic conditional timing therefore gives zero asymptotic flat-band **average** transfer. Do not turn this into an unsupported pointwise Fourier-decay claim.

## Timing collision intensity
For square-integrable conditional delay densities,
\[
\boxed{
\mathfrak R_2=2\int\kappa(dm)\int f_m(t)^2dt,
}
\]
with exact Parseval budget
\[
\boxed{
\int G(\omega)d\omega=\pi\mathfrak R_2.
}
\]

Hence
\[
\boxed{
\bar\eta_I(\Omega)
\le
\min\left[\eta,\frac{\pi\mathfrak R_2}{2\Omega}\right].
}
\]

## Capture-weighted local hazard capacity
If `h_m(t)<=Lambda(m)`, define
\[
\boxed{
\mathfrak H=\int\Lambda(m)\kappa(dm).
}
\]
Then
\[
\boxed{
\mathfrak R_2\le\mathfrak H.
}
\]

This weighted resource is preferred to a global worst-case rate because rare fast marks can carry negligible capture weight.

---

# Operational inverse theorem
For a flat task on `|omega|<=Omega`, with ordinary-frequency half-band
\[
B=\frac{\Omega}{2\pi},
\]
a required absolute average information fraction `q` implies
\[
\boxed{
q\le\eta,
\qquad
\mathfrak R_2\ge4Bq,
\qquad
\mathfrak H\ge4Bq.
}
\]

For a common conditional-hazard ceiling,
\[
\boxed{\Lambda\ge\frac{4Bq}{\eta}.}
\]
For relative retention `q=r eta`,
\[
\boxed{\Lambda\ge4Br.}
\]

---

# Exact conventional-jitter no-go
For any prescribed mean `mu0>0` and variance `sigma^2>0`, WP33 constructs smooth delay laws satisfying both exactly for every selected family member while their transfer tends uniformly to the capture ceiling on any prescribed finite band.

Therefore exact mean delay plus exact RMS jitter does not determine a finite temporal information bandwidth.

No theorem is claimed for simultaneously fixing an arbitrary exact FWHM.

---

# WP35 microscopic CTMC correction
Rev4 says that the maximum total intensity of successful first-registration transitions is a generic uniform mark-conditioned hazard bound. That is too weak.

For a pre-registration state `x`, define the total escape rate
\[
q_x=\sum_{y\ne x}W_{yx}
\]
and
\[
\boxed{q_{\max}=\max_{x\in S_{\rm pre}}q_x.}
\]

If the accessible mark does not independently reveal the realized pre-registration holding times, then
\[
\boxed{h_D(t\mid M)\le q_{\max}.}
\]

Competing-exit check: rates `r` (success) and `R` (failure) give
\[
T\mid M=\mathrm{success}\sim\mathrm{Exp}(r+R),
\]
so the conditional hazard is `r+R`, while
\[
P(M=\mathrm{success})(r+R)=r.
\]
This directly illustrates why the capture-weighted hazard capacity remains well behaved.

The generic quantum-jump sentence is removed from Rev5 rather than extending the first paper into quantum-trajectory assumptions.

---

# Thermodynamic bridge
The restricted finite-state time-homogeneous reversible Markov gateway uses the **total first-exit rate** `lambda1` and is already consistent with WP35.

With forward traffic `f>=f_*`, total EPR `<=Sigma`, activity `<=A`, reverse optical rate `d`, and
\[
g(z)=(1-z^{-1})\ln z,
\]
WP29 gives
\[
\boxed{
\lambda_1\le
\Lambda_*
=\frac{\mathcal A d}{f_*}g^{-1}(\Sigma/f_*).
}
\]

The exponential gateway waiting time then gives `h_D(t|M)<=lambda1` under the stated mark restriction.

The absolute microscopic rate `d` cannot be eliminated in favor of stationary thermodynamic aggregates alone; the rare-fast construction is the counterexample.

---

# Scope boundaries

- Free synchronous clock/control defeats a detector-only timing bound unless reference resources are counted.
- Coherent continuous pointers form a separate quantum-resource branch.
- High-flux history-dependent capture/recovery requires trajectory-level treatment.
- Multiple independent pre-primary timing copies are an additional multiplicity resource.
- Nonclassical/phase-sensitive optical source parameters require a different input-information normalization.

---

# Novelty posture
The individual mathematical ingredients are established: marked Poisson processes, Fisher information, Wiener theory, Parseval, survival/hazard calculus, and rearrangement inequalities.

The defensible candidate novelty is the **resource-completeness stack**:

> exact marked source-modulation FI transfer -> atomic timing residue -> collision spectral budget -> capture-weighted local-hazard resource -> inverse timing-resource cost, together with explicit jitter, clock/control, and stationary-thermodynamic no-go/repair results.

Do not claim generic information-theoretic timing analysis or generic response/noise theory as new.

---

# Frozen work
WP17–24 HgCdTe/Kane validation is frozen. The quantum-pointer, continuous-analog, and non-Poisson branches are also frozen for the first manuscript unless a concrete referee-level defect forces reopening them.

---

# Immediate publication gates
1. Observe and inspect the Rev5 CI result.
2. Persist the generated Rev5 source after successful build verification.
3. Run a final line-by-line claim/reference audit on Rev5.
4. If no substantive defect remains, prepare the submission-ready source/package rather than opening another research branch.
