# Manuscript Hostile Proof Audit — Round 2

**Date:** 2026-08-20

## Scope

Adversarial audit of `manuscript/event_resource_theorem_rev2.tex` and the WP25–33 theorem stack. The purpose is to identify theorem-breaking assumptions, overclaims, normalization errors, or claims that are only true in a narrower class than the prose suggests.

This audit is deliberately hostile. Findings are classified as:

- **PASS** — proof/claim survives as written or with minor wording;
- **TIGHTEN** — mathematically correct but assumptions should be made more explicit;
- **CORRECTED** — earlier wording was too strong and has been repaired;
- **DEFER** — outside the first-paper theorem class and should not be generalized implicitly.

---

# 1. Exact marked-event Fisher-information theorem

## Claim

For weak sinusoidal modulation of an inhomogeneous Poisson photon stream and an autonomous one-primary-event subprobability kernel

\[
K(dm,d\tau)=\kappa(dm)\mu_m(d\tau),
\]

the ideal marked-record source-normalized FI transfer is

\[
G(\omega)=\int |H_m(\omega)|^2\kappa(dm).
\]

## Audit

**PASS, with explicit assumptions.**

The result follows from standard Poisson marking/displacement and the Poisson FI formula.

Required assumptions that must remain explicit:

1. `kappa` and `mu_m` are independent of the small parameter `theta`; the source parameter modulates arrival intensity, not the per-photon detector kernel.
2. The detector channel is time-translation covariant/autonomous: the kernel depends on elapsed delay, not absolute source phase.
3. One incident photon produces at most one sufficient **primary** event in the theorem class.
4. The low-overlap/independent-event approximation holds.
5. The output mark space includes every accessible primary-event mark used by the estimator.
6. The FI rate is the asymptotic long-time rate for sinusoidal modulation.

If any of these are dropped, Eq. `G(omega)` need not remain the correct complete record FI.

---

# 2. Input normalization

At `theta=0`,

\[
\dot F_{in}=\Phi_0/2
\]

for `Phi=Phi0[1+theta cos(omega t)]` after long-time averaging.

**PASS.**

No missing factor of two was found. The paper should describe this as the incident Poisson/direct-detection FI for the chosen source task. A broader incident-field QFI statement is unnecessary for the first manuscript and would enlarge the scope without helping the theorem.

---

# 3. Complete accessible marks

**PASS and essential.**

The theorem must condition on every mark available to the final estimator. Marginalizing a mark can reduce FI and can convert deterministic conditional delays into an apparently broad marginal delay law.

This is not a cosmetic issue. The atomic-residue theorem and the clock/control no-go both depend on this distinction.

Recommended wording:

> `M` is the complete accessible mark of the ideal primary electrical record; any mark intentionally discarded is part of a downstream coarse graining and is therefore treated by data processing.

---

# 4. Background events and downstream electronics

**PASS for an upper bound.**

Adding a parameter-independent background process to the ideal primary signal record and then forgetting the decomposition is a parameter-independent stochastic channel. Therefore it cannot increase source FI.

Likewise, thresholding, deterministic gain, ordinary RC filtering, ADC quantization, or dead-time processing applied after a sufficient latent primary record cannot violate the intrinsic upper bound.

Important limitation:

History-dependent capture or dead time that alters whether future incident photons generate latent primary events is not a downstream map of an already-defined independent-event record. That regime is outside the theorem.

---

# 5. Wiener atomic timing theorem

For each conditional delay measure with atoms `p_j(m)`,

\[
\lim_{\Omega\to\infty}\frac1{2\Omega}
\int_{-\Omega}^{\Omega}|H_m(\omega)|^2d\omega
=\sum_j p_j(m)^2.
\]

**PASS.**

Dominated convergence through the finite capture measure `kappa` is justified by `|H_m|<=1`.

Interpretation must remain precise:

- non-atomic timing implies vanishing *flat-band average* transfer as the averaging band grows without bound;
- it does **not** imply pointwise `H(omega)->0` for every non-atomic singular measure;
- a narrow continuous prompt component can have zero Wiener residue yet retain near-unit information over an arbitrarily large but finite band.

The manuscript currently respects this distinction.

---

# 6. Parseval / timing-collision resource

Define

\[
\mathfrak R_2=2\int\kappa(dm)\int f_m^2dt.
\]

Then

\[
\int G(\omega)d\omega=\pi\mathfrak R_2.
\]

**PASS.**

Fourier convention check:

\[
H(\omega)=\int f(t)e^{-i\omega t}dt,
\qquad
\int |H|^2\frac{d\omega}{2\pi}=\int f^2dt.
\]

Thus

\[
\int Gd\omega=2\pi\int\kappa\int f^2
=\pi\mathfrak R_2.
\]

The flat-band coefficient

\[
\pi\mathfrak R_2/(2\Omega)
\]

is correct.

---

# 7. Arbitrary spectral-information weight

The bathtub/rearrangement bound

\[
\int wG
\le
\eta\,\mathcal W(\pi\mathfrak R_2/\eta)
\]

is **PASS** under the stated interpretation.

**TIGHTEN:** `w(omega)` should be described as a normalized weighting of independent frequency-resolved source-FI tasks, or an already-defined scalar task with additive spectral FI density. It is not a theorem for arbitrary correlated multiparameter quantum estimation across frequency.

The first manuscript should avoid language such as “arbitrary optical waveform QFI” here.

---

# 8. Hazard-to-collision inequality

Claim:

\[
2\int f_m^2dt\le\Lambda(m)
\]

when `h_m(t)<=Lambda(m)`.

**PASS.**

A cleaner proof than the original variable substitution is

\[
\int f^2dt
=\int h^2S^2dt
\le\Lambda\int hS^2dt.
\]

Since

\[
\frac{d}{dt}S^2=-2hS^2,
\]

for a normalized continuous registration law with `S(0)=1`, `S(infinity)=0`,

\[
\int hS^2dt=1/2.
\]

Therefore

\[
\int f^2dt\le\Lambda/2.
\]

This proof is recommended for the next manuscript revision because it avoids any concern about zero-hazard intervals or the invertibility of cumulative hazard.

---

# 9. Weighted hazard capacity versus worst-case hazard

**PASS and an important refinement.**

The strongest quantitative event theorem should use

\[
\mathfrak H=\int\Lambda(m)\kappa(dm),
\qquad
\mathfrak R_2\le\mathfrak H.
\]

A global `sup_m Lambda(m)` is merely a convenient sufficient corollary.

This prevents the paper from making the false statement that an infinitely fast but vanishingly improbable branch necessarily makes information bandwidth unbounded.

---

# 10. Constant-hazard asymptotic saturation

For

\[
f(t)=\Lambda e^{-\Lambda t},
\]

\[
\frac1{2\Omega}\int_{-\Omega}^{\Omega}|H|^2d\omega
=\frac{\Lambda}{\Omega}\arctan(\Omega/\Lambda)
\sim\frac{\pi\Lambda}{2\Omega}.
\]

**PASS.**

This validates both the `1/Omega` scaling and the numerical prefactor of the uniform-hazard high-band ceiling.

The original draft contained a LaTeX typo (`rac`); Rev2 corrected it.

---

# 11. Timing-jitter no-go

The earlier WP26 family fixed variance asymptotically but did not keep an arbitrary nonzero mean exactly fixed.

**CORRECTED by WP33.**

WP33 solves the variance equation exactly for every family member, then applies a nonnegative deterministic shift to impose any prescribed mean `mu0`. The shift leaves `|H|` unchanged.

Therefore the manuscript may safely claim:

\[
\boxed{
\{\mathbb E D=\mu_0,\operatorname{Var}D=\sigma^2\}
\not\Rightarrow
\text{finite information bandwidth}.
}
\]

Do **not** claim that an arbitrary exact FWHM can simultaneously be fixed by this same construction. The supported statement is that FWHM or another scalar width is not a complete distributional resource without shape assumptions.

---

# 12. Synchronous-control / temporal-reference no-go

**PASS conceptually.**

A source-synchronous detector can map arrival phase into an internal mark before slow final registration. The information survives because the high-frequency temporal reference and memory are themselves resources.

The counterexample does not say a real clock is free. Its purpose is exactly the opposite: a theorem stated only in terms of final registration delay is incomplete for actively synchronized architectures.

The first paper should therefore keep the word **autonomous** in the title, abstract, theorem assumptions, and conclusions.

---

# 13. Thermodynamic gateway bridge

For WP3's finite-state continuous-time Markov gateway, the first holding time

\[
T_1\sim\mathrm{Exp}(\lambda_1)
\]

is independent of exit destination. If the accessible mark is generated from the exit destination and subsequent autonomous Markov path, the downstream process has no memory of the realized holding time. Thus

\[
D|M=T_1+Y_M
\]

with `T1` independent of `(M,Y_M)`.

The resulting survival/density formula gives

\[
h_D(t|M)\le\lambda_1.
\]

**PASS for this memoryless Markov class.**

**TIGHTEN:** the paper should not imply this mark-robust independence for arbitrary semi-Markov or age-dependent downstream detectors. If a state explicitly stores the elapsed gateway holding time, that stored clock/age variable is an additional timing resource and the finite-state memoryless proof no longer applies directly.

---

# 14. Thermodynamic rate bound

From

\[
\sigma_{opt}=f(1-1/z)\ln z,
\quad f\ge f_*,
\quad \sigma_{opt}\le\Sigma,
\]

one obtains

\[
z\le g^{-1}(\Sigma/f_*).
\]

Since `r=f/z=d pi1`,

\[
\pi_1\ge f_*/[d g^{-1}(\Sigma/f_*)].
\]

Activity then gives

\[
\lambda_1\le
\frac{\mathcal A d}{f_*}
 g^{-1}(\Sigma/f_*).
\]

**PASS.**

Dimensions are correct and no factor error was found.

---

# 15. Rare-fast thermodynamic counterexample

The appendix family

\[
0\rightleftarrows1\rightleftarrows2\rightleftarrows0
\]

with selected rates scaling as `R` has the exact stationary distribution recorded in the appendix. Symbolic re-derivation confirms those probabilities.

As `R->infinity`:

- useful optical traffic remains finite and nonzero;
- stationary one-way activity remains finite;
- total steady EPR remains finite;
- the fixed optical forward/reverse rate ratio `a/b` is independent of `R`;
- post-capture local holding rate `(b+c)R` diverges;
- conditional successful-registration probability `c/(b+c)` remains nonzero;
- conditional successful-registration delay becomes `Exp[(b+c)R]`.

**PASS for the intended aggregate-resource no-go.**

Important limitation that should be acknowledged rather than hidden:

The nonoptical bare rate ratios `cR/q` and `sR/p` are not held fixed. Therefore the counterexample proves that **aggregate stationary EPR/activity plus the fixed optical detailed-balance ratio** do not control the local speed scale. It does not prove insufficiency after every edge-resolved energetic affinity and every microscopic prefactor is separately bounded.

That limitation is consistent with the paper's conclusion: an absolute microscopic local scale or equivalent edge-resolved resource is required.

---

# 16. Pointwise Lorentzian corollary

For the single-gateway Markov repair, the independent exponential factor yields

\[
|H_D(\omega)|^2
\le\lambda_1^2/(\lambda_1^2+\omega^2).
\]

**PASS.**

This pointwise result is stronger than the generic hazard/Parseval theorem but belongs only to the specific gateway structure. It must not be presented as a consequence of bounded hazard alone.

---

# 17. Parallel replication

**PASS.**

Independent parallel detector replication does not violate the source-normalized theorem because both incident FI and output FI are extensive. For unequal branches, WP32's capture-weighted kernel already gives the correct aggregate.

Multiple independent **pre-primary** timing copies from one captured photon are a different resource class and are correctly excluded.

---

# 18. Non-Poisson/nonclassical sources

**DEFER.**

The first paper does not need to solve this branch to make a correct theorem. Extending the exact transfer law to antibunched, bunched, entangled, or phase-sensitive sources would require a different input-information calculation and could obscure the closed event result.

Recommended publication posture:

> The present theorem is for weak coherent/direct-detection intensity modulation; extension to non-Poisson or quantum-correlated sources is left open.

---

# 19. Novelty-sensitive wording

The following claims should **not** appear:

- “first information-theoretic analysis of detector timing”;
- “first proof that jitter limits photon information”;
- “first detector bandwidth--sensitivity tradeoff”;
- “universal photodetector speed limit” without the autonomous event-class qualifier;
- “thermodynamics alone limits detector speed.”

Defensible wording:

> We derive a resource-completeness theorem for source-modulation information transfer in autonomous marked photodetection event channels, identify exact atomic and collision-intensity timing resources, and provide explicit no-go/repair results showing why low-order jitter moments, stationary thermodynamic aggregates, and unaccounted synchronous control do not substitute for those resources.

---

# Overall judgment

**Scientific status: STRONG RESTRICTED THEOREM, not yet a universal all-detector theorem.**

No fatal mathematical defect was found in WP32/WP33 or the thermodynamic bridge under their stated assumptions. The largest remaining risks are publication positioning and readers overlooking the independence/autonomy/one-primary-event restrictions.

Before submission:

1. replace the hazard proof with the direct `d(S^2)/dt` proof;
2. use the exact WP33 fixed-mean/fixed-variance family in the manuscript;
3. explicitly state parameter independence of `kappa` and `mu_m` under source-amplitude modulation;
4. make the Markov memorylessness assumption explicit in the thermodynamic bridge;
5. keep non-Poisson sources out of the main theorem;
6. retain conservative novelty language relative to TCSPC/IRF and finite-frequency response literature.
