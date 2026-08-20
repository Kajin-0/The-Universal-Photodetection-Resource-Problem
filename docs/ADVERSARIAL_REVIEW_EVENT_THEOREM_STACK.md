# Adversarial Review — Autonomous Event Information-Bandwidth Theorem Stack

**Date:** 2026-08-20

## Purpose

Attack the proposed first-paper theorem stack as a hostile expert referee. Distinguish fatal issues from scope limitations and presentation risks before drafting a manuscript.

---

# Overall verdict

**Technically promising and internally coherent, but the paper will fail if it is sold as “timing jitter reduces information” or “a new Fisher-information/hazard theorem.”** Those themes have substantial prior art.

The defensible paper is narrower:

> a source-normalized resource hierarchy for autonomous photodetection event channels, including an exact mark-resolved atomic high-bandwidth residue, a quantitative timing-collision/hazard spectral budget, conventional-jitter and free-clock counterexamples, and a thermodynamic no-go/conditional-repair theorem.

The mathematics is relatively elementary in places. Significance must therefore come from the **correct resource identification and no-go/repair structure**, not technical complexity.

---

# Objection 1 — “This is just the Fourier transform of an instrument response function.”

### Attack

Random timing jitter convolves the event stream; Fourier transformation multiplies the modulation by the IRF transfer function. This is standard signal processing and appears explicitly in TCSPC literature.

### Assessment

**Valid against any broad novelty claim. Not fatal to the resource theorem.**

### Required response

Do not claim novelty for the exact convolution/characteristic-function response alone. The paper must move quickly from the exact event-kernel transfer identity to:

- atomic timing residual;
- `R2` spectral budget;
- local-hazard completion;
- moment-jitter no-go;
- thermodynamic no-go/repair;
- clock/control no-go.

The transfer identity is setup, not the headline discovery.

---

# Objection 2 — “Wiener's theorem is classical.”

### Attack

The asymptotic formula

\[
\lim\frac1{2\Omega}\int|H|^2=
\sum p_j^2
\]

is a standard theorem of harmonic analysis.

### Assessment

**Correct.**

### Required response

State explicitly that Wiener theory is classical. Claim only the derived photodetection consequence:

> the high-bandwidth source-information residue of an autonomous marked event detector equals the mark-conditioned atomic timing collision mass.

Whether that application is publication-worthy depends on its integration with the rest of the resource story.

---

# Objection 3 — “The hazard-to-L2 inequality is elementary.”

### Attack

From `f=hS`, bounded hazard immediately yields `int f^2 <= Lambda/2`. This is not deep mathematics.

### Assessment

**Correct but not fatal.**

### Required response

The paper should emphasize why `Lambda` is physically nontrivial:

- it is a local conditional registration intensity;
- it maps to total Markov registration escape rate or quantum jump-operator norm;
- stationary activity does not control it;
- WP4 supplies an explicit thermodynamic counterexample;
- WP29 shows the conditions under which EPR/activity/throughput can control it.

The conceptual resource map is the contribution.

---

# Objection 4 — “RMS jitter already characterizes timing resolution.”

### Attack

Detector communities commonly use FWHM or RMS timing jitter. Why introduce `R2` or hazard?

### Assessment

**Strong opportunity for the paper.**

### Response

WP26 gives a smooth, physically realizable two-path Markov family:

\[
f_{\epsilon,n}(t)
=(1-\epsilon)n e^{-nt}
+\epsilon\lambda_\epsilon e^{-\lambda_\epsilon t}.
\]

Choose

\[
\boxed{
\lambda_\epsilon
=\frac{\sqrt{\epsilon(2-\epsilon)}}{\sigma}
}
\]

in the `n->infinity` limit. Then

\[
\operatorname{Var}D\to\sigma^2
\]

while for every fixed finite frequency band

\[
H_{\epsilon,n}(\omega)\to1
\]

as `n->infinity`, `epsilon->0`.

This is not merely a pathological PDF: it is realizable as a captured photon selecting a fast or rare slow exponential registration pathway.

Thus a fixed RMS jitter can coexist with arbitrarily large information bandwidth.

This counterexample should be central.

---

# Objection 5 — “Atomic deterministic timing is unphysical.”

### Attack

Real detectors always have thermal, quantum, electronic, or geometric noise, so exact delta-function timing atoms do not exist.

### Assessment

**Not fatal.**

### Response

WP30 uses atoms to characterize the exact mathematical obstruction and singular limit. In any real system, arbitrarily small broadening converts the atom into a narrow continuous peak, making the ultimate Wiener residual zero but allowing the crossover bandwidth to become arbitrarily large.

Thus the atomic theorem explains the same prompt-spike loophole seen in WP26 and direct-feedthrough limits.

The paper should present atoms as the limiting structure, not claim macroscopic detectors literally have perfect delta timing.

---

# Objection 6 — “Why average over a frequency band instead of use ordinary -3 dB bandwidth?”

### Attack

Detector engineers use pointwise amplitude response and `-3 dB` bandwidth.

### Assessment

**The project has a strong answer.**

### Response

- deterministic invertible filtering can attenuate both signal and upstream noise without losing FI;
- pointwise characteristic functions may have zeros/ripples unrelated to a monotone speed scale;
- the left side should be source-information weighted rather than an arbitrary response threshold;
- WP28 supports arbitrary source information spectra via the concentration function `W(A)`.

The paper should explicitly distinguish **amplitude bandwidth** from **information bandwidth** rather than attacking conventional bandwidth as useless.

---

# Objection 7 — “The detector class is too narrow.”

### Attack

The theorem assumes weak coherent/Poisson flux, independent events, one primary electrical registration per captured photon, and autonomy.

### Assessment

**Real limitation, but acceptable if explicit.**

### Response

This class includes a broad family of autonomous photon-counting/event detectors in the low-overlap regime. It intentionally excludes:

- coherent continuous pointers;
- high-flux saturation/memory unless treated as downstream thinning;
- nonclassical source statistics;
- externally clocked/gated/heterodyne architectures;
- multiple independent pre-registration timing copies per photon.

The manuscript should call itself a theorem for **autonomous photodetection event channels**, not universal for all detectors.

---

# Objection 8 — “A synchronous detector trivially beats the timing bound.”

### Attack

Use a local oscillator or clock to record source phase immediately, then read out slowly.

### Assessment

**Already solved by WP27.**

### Response

This is an explicit no-go demonstrating that a temporal reference is itself a physical resource. The theorem either:

- assumes time-translation-invariant autonomous processing; or
- must count clock/control bandwidth, phase precision, memory, Hamiltonian/action, etc.

This should be presented as a strength of the resource-completeness framework.

---

# Objection 9 — “Stationary activity should already bound speed.”

### Attack

Kinetic uncertainty relations use dynamical activity as a speed/precision resource.

### Assessment

**WP4 is essential.**

### Response

Stationary activity weights rates by stationary occupation. A fast state can become correspondingly rare. WP4 constructs reversible families with bounded activity/EPR but diverging local microscopic rates and detector timing speed.

The event theorem needs a post-capture local timing resource, not only a stationary average.

This distinction from KUR/TUR literature must be explicit.

---

# Objection 10 — “WP29 cheats by putting the speed back in through d.”

### Attack

The thermodynamic completion contains an absolute reverse optical rate `d`, so of course it produces a finite speed.

### Assessment

**The objection is conceptually correct and is exactly the paper's no-go message.**

### Response

Do not market WP29 as deriving speed from thermodynamics alone.

The result is:

\[
\boxed{
\text{thermodynamic budgets}
+\text{absolute microscopic rate scale}
\Rightarrow
\text{finite information bandwidth},
}
\]

while WP4 proves the absolute scale cannot be removed in the stated generality.

The scientific statement is that thermodynamics constrains how a microscopic rate resource can be used; it does not create the rate scale.

---

# Objection 11 — “Capture efficiency is trivial.”

### Attack

`eta<=1` is probability conservation. The theorem might reduce to a timing inequality with no sensitivity physics.

### Assessment

**Partly correct.**

### Response

For the core speed theorem, a nontrivial optical capture bound is optional. This is why detailed EM/HgCdTe work was frozen.

A stronger sensitivity-speed theorem can later compose WP5 optical resources, but the first paper should not pretend that `C` alone is a new sensitivity bound.

---

# Objection 12 — “Dark counts and temperature are absent.”

### Attack

A detector speed/sensitivity theorem without dark noise or temperature does not answer the practical detector problem.

### Assessment

**Presentation risk, not logical defect.**

### Response

Parameter-independent backgrounds can only reduce source FI and therefore are unnecessary in an intrinsic upper bound.

The thermodynamic conclusion is deliberately negative:

\[
T\text{ alone does not specify }C,\Lambda,\text{ or unavoidable background}.
\]

A temperature-dependent sensitivity theorem requires additional microscopic assumptions. WP29 gives one restricted route; the paper should say this clearly.

---

# Objection 13 — “Parallel replication beats any fixed resource bound.”

### Attack

Use `N` detectors in parallel.

### Assessment

**Passes.**

### Response

Source-normalized FI is extensive:

\[
\eta_{tot}=\sum_jw_j\eta_j.
\]

Identical replication scales output FI and incident FI equally. The marked-kernel resources are additive. No superlinear normalized gain appears.

---

# Objection 14 — “Avalanche gain gives many timestamps per photon.”

### Attack

Multiple offspring could average away timing noise.

### Assessment

**Scope boundary must remain explicit.**

### Response

- offspring produced after a sufficient primary event are downstream processing;
- multiple independent **pre-primary** timing records from one photon are a different channel class and represent an additional timing/multiplicity resource.

Do not claim WP25–32 covers arbitrary branching cluster detectors.

---

# Objection 15 — “The source is only sinusoidal amplitude modulation.”

### Attack

A universal information theorem should handle arbitrary optical waveforms and nonclassical states.

### Assessment

**Acceptable first-paper limitation.**

### Response

The theorem is local/spectral: weak sinusoidal modes diagonalize a stationary linearized direct-detection problem, and WP28 integrates arbitrary source spectral FI weights.

For coherent states with real amplitude/intensity modulation, direct photon counting attains the relevant incident QFI. Phase modulation/nonclassical source statistics require a separate extension.

Do not overstate this as all coherent-state QFI.

---

# Objection 16 — “The independent-event assumption excludes dead time and high-flux operation.”

### Attack

Real counters saturate and have history dependence.

### Assessment

**Scope limitation.**

### Response

The first theorem is a low-overlap/independent-primary-event result. Parameter-independent dead time applied after an ideal latent primary record is data processing and cannot improve FI, but arbitrary history-dependent capture dynamics are not represented by a one-photon displacement kernel.

The manuscript should say this rather than hide it.

---

# Objection 17 — “The theorem may already exist in TCSPC information theory.”

### Attack

Talaga (2009) explicitly discusses instrument-response information loss and bandwidth; later FLIM papers compute Fisher-information degradation from finite IRFs.

### Assessment

**Serious novelty constraint.**

### Response

Those works must be central citations. Based on current equation-level inspection:

- Talaga uses Shannon/mutual-information loss for lifetime-state inference and IRF convolution/power spectra;
- later FLIM work uses FI/CRLB for lifetime parameter estimation under specified IRFs;
- none of the inspected works states the WP25–32 local registration-intensity / atomic timing / thermodynamic resource theorem.

The manuscript must claim only the latter.

---

# Objection 18 — “The weighted-hazard refinement undermines the claim that a local max rate is necessary.”

### Attack

WP32 shows a capture-weighted hazard budget `mathfrak H` suffices; a global worst-case `Lambda` can diverge in a negligible branch.

### Assessment

**Valid correction already incorporated.**

### Response

Do not call the global maximum hazard mathematically minimal.

Current hierarchy:

\[
\text{atomic mass}
\rightarrow
\text{asymptotic residual},
\]

\[
\mathfrak R_2
\rightarrow
\text{quantitative spectral budget},
\]

\[
\mathfrak H
\rightarrow
\mathfrak R_2,
\]

with uniform `Lambda` as a convenient microscopic specialization.

WP4's no-go concerns the absence of **any adequate absolute local-rate budget**, not specifically the necessity of a worst-case sup norm.

---

# Fatal-issue check

No fatal mathematical contradiction has been identified in the theorem stack under its stated independent-event/autonomous assumptions.

The main publication risks are:

1. **novelty compression:** many pieces are classical/known;
2. **scope:** event-channel theorem, not all photodetectors;
3. **significance:** must demonstrate why the resource hierarchy changes how detector limits are formulated;
4. **wording:** must not oversell elementary Fourier/hazard ingredients.

---

# Recommended manuscript center of gravity

Do not center the paper on the inequality

\[
\bar\eta_I\le C\pi\Lambda/(2\Omega).
\]

Center it on the **hierarchy and no-go structure**:

1. exact marked event-kernel source FI;
2. deterministic/atomic timing is the exact asymptotic obstruction;
3. conventional timing moments are not resource-complete;
4. collision intensity / weighted local hazard are quantitative timing resources;
5. stationary thermodynamic resources do not supply the absolute timing scale;
6. a restricted thermokinetic completion exists once that microscopic scale is bounded;
7. free temporal references are an independent resource.

That story is substantially stronger than presenting one simple bound.

---

# Verdict

**Proceed to manuscript drafting only after the final citation-chain audit, but do not reopen material-specific physics.**

The current event theorem stack is scientifically coherent enough for a paper attempt. Its publishability will turn on disciplined novelty framing and the value reviewers assign to the resource-completeness synthesis.