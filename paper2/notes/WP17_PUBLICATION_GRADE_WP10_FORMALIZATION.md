# WP17 — Publication-Grade Formalization of the General Autonomous-Channel Fisher Spectrum

**Status:** the main measure-theoretic gaps in WP10 have a clean theorem-grade closure route. In particular, an arbitrary parameter-independent stochastic detector kernel can be reduced to an ordinary statistic by standard-Borel kernel randomization, after which the standard DQM-under-statistics theorem gives the exact conditional-score formula. The source configuration space, detector output assumptions, shift covariance, operator extension, Fourier diagonalization, and narrowband interpretation can all be stated without an increasing-window construction.

This work package is a **rigor/citation hardening pass**, not a new novelty claim.

---

## 1. Recommended theorem setup

### Input trajectory space

Let

\[
\mathsf X=\mathcal N_{\mathrm{lf}}(\mathbb R)
\]

be the space of locally finite integer-valued Radon measures on `R`, equipped with the vague topology and its Borel sigma-field.

Because `R` is locally compact, second countable, and Polish, the locally finite configuration space with the vague topology is itself a standard Borel/Polish point-process state space. This is the conventional state space used in point-process theory.

An incident photon trajectory is

\[
N\in\mathsf X.
\]

Define the time-shift action on configurations by

\[
(\Theta_a^{\mathsf X}n)(B)=n(B-a).
\]

Thus every point is shifted forward by `a`.

### Output trajectory space

Do **not** force every detector architecture into a particular path topology.

Assume only that the complete accessible detector record takes values in a **standard Borel space**

\[
(\mathsf Y,\mathcal Y)
\]

with a measurable time-shift action

\[
\Theta_a^{\mathsf Y}:\mathsf Y\to\mathsf Y,
\qquad a\in\mathbb R,
\]

satisfying the group law.

This is broad enough for:

- point-process timestamps;
- marked point processes;
- finite/countable digital event streams;
- finite-dimensional analog marks;
- standard Skorokhod/path-space records when desired;
- hidden-state, dead-time, afterpulse, and saturation models after inaccessible variables are integrated out.

The theorem does not require a universal topology for all analog detector records; standard-Borel measurability is enough for the stochastic-channel argument.

### Detector channel

Let

\[
K(dy\mid n)
\]

be a probability kernel from `X` to `Y`, independent of the optical perturbation parameter.

Assume **autonomy / time-translation covariance** in the kernel sense:

\[
\boxed{
K(\Theta_a^{\mathsf Y}B\mid \Theta_a^{\mathsf X}n)
=K(B\mid n)
}
\]

for every `a`, every measurable `B`, and all `n` outside any fixed kernel-null exceptional set allowed by the chosen version.

No causality assumption is needed for the spectral theorem itself. Physical causal detector models can of course satisfy the stronger property.

---

## 2. Dense source tangent class

For the cleanest primitive proof use

\[
\boxed{
\mathcal D=C_c^\infty(\mathbb R;\mathbb R),
}
\]

which is dense in real `L^2(R)`.

For `u in D`, define a local Poisson intensity family

\[
\lambda_{\epsilon,u}(t)
=\Phi_0[1+\epsilon u(t)].
\]

Because `u` is bounded and compactly supported, this is positive for all sufficiently small `|epsilon|`.

The larger bounded compact-support class used in WP10 is also valid, but `C_c^infty` makes density and admissibility immediate and loses nothing after the bounded Fisher form is extended to all `L^2`.

For a finite tangent family one may equivalently use

\[
\lambda_{\boldsymbol\theta}(t)
=\Phi_0\left[1+\sum_{j=1}^p\theta_j u_j(t)\right].
\]

---

## 3. Source Poisson DQM is explicit

Let `P_{epsilon,u}` be the law on `X` of the Poisson process with the intensity above and let `P_0` be homogeneous Poisson of rate `Phi0`.

Since the intensity perturbation has compact support, the likelihood ratio relative to `P_0` is

\[
\boxed{
\log\frac{dP_{\epsilon,u}}{dP_0}(N)
=
\int \log[1+\epsilon u(t)]N(dt)
-\Phi_0\epsilon\int u(t)dt.
}
\]

Differentiating at zero gives

\[
\boxed{
S_u(N)
=
\int u(t)[N(dt)-\Phi_0dt].
}
\]

For bounded compact support, the ordinary Poisson exponential-moment bounds control the Taylor remainder and yield differentiability in quadratic mean. Equivalently, this is a direct special case of classical Poisson-process LAN/DQM theory.

Poisson isometry/Campbell covariance gives

\[
\boxed{
E_0[S_uS_v]
=\Phi_0\int u(t)v(t)dt.
}
\]

Thus the normalized source score map

\[
u\mapsto S_u/\sqrt{\Phi_0}
\]

is an isometry of the dense temporal tangent class into `L_0^2(P_0)`.

### Suitable references

- F. Liese and U. Lorz, **“Contiguity and LAN-property of sequences of Poisson processes,”** *Kybernetika* **35**, 281–308 (1999). They formulate Poisson likelihood/Hellinger/LAN conditions on arbitrary state spaces.
- A. F. Karr, *Point Processes and Their Statistical Inference*, Marcel Dekker (1986), for standard point-process likelihood/statistical foundations.
- L. Leskelä, **“Information divergences and likelihood ratios of Poisson processes and point patterns,”** *IEEE Trans. Inf. Theory* (2024), DOI `10.1109/TIT.2024.3472448`, for modern general-measurable-space likelihood-ratio and divergence formulas.

The manuscript can keep the displayed elementary likelihood and score derivation self-contained and cite one of these for the standard general theory.

---

## 4. Stochastic detector kernels: rigorous DQM route

WP10 previously invoked a standard “DQM under parameter-independent Markov maps” result. There is a particularly transparent proof route that avoids needing a separate specialized theorem for randomized channels.

### 4.1 Kernel randomization

Because `Y` is standard Borel, the kernel-randomization lemma gives a jointly measurable function

\[
F:\mathsf X\times[0,1]\to\mathsf Y
\]

such that if

\[
Z\sim\operatorname{Unif}[0,1]
\]

is independent of `N`, then

\[
F(n,Z)\sim K(\cdot\mid n)
\]

for every input trajectory `n`.

A publication-grade reference is:

- O. Kallenberg, *Foundations of Modern Probability*, 3rd ed., Springer (2021), **Lemma 4.22, kernels and randomization**: a probability kernel from an arbitrary measurable space into a Borel space can be represented by a measurable function of the source point and one independent uniform random variable.

This is precisely why the standard-Borel output assumption is useful.

### 4.2 Enlarge the source experiment

Consider

\[
\widetilde P_{\epsilon,u}
=P_{\epsilon,u}\otimes\operatorname{Unif}[0,1]
\]

on `X x [0,1]`.

The auxiliary randomizer is parameter independent, so the enlarged experiment is DQM with the **same score**

\[
\widetilde S_u(N,Z)=S_u(N).
\]

Now the detector output is simply the ordinary measurable statistic

\[
Y=F(N,Z).
\]

### 4.3 Apply the standard DQM-under-statistics theorem

Pollard's Theorem 7 states that if an experiment is DQM with score `Delta` and one retains a measurable statistic `S`, then the induced experiment is DQM with score equal to the conditional expectation of the original score given that statistic.

Reference:

- D. Pollard, **“A note on insufficiency and the preservation of Fisher information,”** in *From Probability to Statistics and Back: High-Dimensional Models and Processes*, IMS Collections **9**, 266–275 (2013), DOI `10.1214/12-IMSCOLL919`, **Theorem 7**.

Applying it to the enlarged experiment gives

\[
\boxed{
S_u^{\rm out}(Y)
=E_0[S_u(N)\mid Y].
}
\]

This proves the Markov-kernel score identity rigorously for the theorem class, with no deterministic-channel restriction.

### Important novelty boundary

Neither kernel randomization nor the conditional-score identity is new. They are proof tools only.

---

## 5. Fisher-retention form and bounded extension

Define on `D`

\[
\mathcal F_K[u,v]
=E_0[S_u^{\rm out}S_v^{\rm out}].
\]

Conditional expectation is an orthogonal contraction in `L^2`, hence

\[
\|S_u^{\rm out}\|_2
\le\|S_u\|_2
=\sqrt{\Phi_0}\|u\|_2.
\]

Consequently

\[
|\mathcal F_K[u,v]|
\le
\Phi_0\|u\|_2\|v\|_2.
\]

The bilinear form therefore extends uniquely and continuously from the dense class `D` to all real `L^2(R)`.

By Riesz representation there is a unique bounded self-adjoint operator

\[
\boxed{
A_K:L^2(\mathbb R)\to L^2(\mathbb R)
}
\]

such that

\[
\boxed{
\mathcal F_K[u,v]
=\Phi_0\langle u,A_Kv\rangle.
}
\]

For every `u`,

\[
0\le\mathcal F_K[u,u]
\le\Phi_0\|u\|_2^2,
\]

so

\[
\boxed{0\preceq A_K\preceq I.}
\]

No integral kernel for `A_K` is assumed or needed.

---

## 6. Autonomy implies exact commutation with shifts

Let waveform translation be

\[
(U_au)(t)=u(t-a).
\]

With the trajectory-shift convention above,

\[
\boxed{
S_{U_au}(n)=S_u(\Theta_{-a}^{\mathsf X}n).
}
\]

At baseline, `P_0` is stationary. Kernel covariance implies the joint baseline law

\[
J_0(dn,dy)=P_0(dn)K(dy\mid n)
\]

is invariant under the diagonal action

\[
(n,y)\mapsto
(\Theta_a^{\mathsf X}n,\Theta_a^{\mathsf Y}y).
\]

The conditional-score version can therefore be chosen covariantly in `L^2(Q_0)`:

\[
S_{U_au}^{\rm out}(y)
=
S_u^{\rm out}(\Theta_{-a}^{\mathsf Y}y)
\quad Q_0\text{-a.s.}
\]

One can verify this without choosing pointwise conditional-probability versions: test both sides against arbitrary bounded measurable functions of `Y` and use diagonal stationarity of `J_0`.

Hence

\[
\mathcal F_K[U_au,U_av]
=\mathcal F_K[u,v].
\]

Since `U_a` is unitary on `L^2`,

\[
U_a^*A_KU_a=A_K,
\]

or equivalently

\[
\boxed{
A_KU_a=U_aA_K
\qquad\forall a\in\mathbb R.
}
\]

This is the only structural detector property needed for frequency diagonalization.

---

## 7. Exact Fourier-multiplier theorem

The harmonic-analysis step has an exact classical reference, stronger than an informal appeal to stationarity.

E. M. Stein, *Singular Integrals and Differentiability Properties of Functions*, Princeton University Press (1970), Chapter II, Section 1.4, Proposition 2 states that a bounded linear transformation on `L^2(R^n)` commutes with translations **iff** there exists a bounded measurable multiplier `m` such that

\[
\widehat{Tf}(\xi)=m(\xi)\widehat f(\xi).
\]

Applying this with `n=1` gives an essentially bounded measurable

\[
G_{\Phi_0,K}\in L^\infty(\mathbb R)
\]

such that after complexification

\[
\boxed{
\widehat{A_Ku}(\omega)
=G_{\Phi_0,K}(\omega)\widehat u(\omega)
\quad\text{a.e.}
}
\]

Because `A_K` is self-adjoint, positive, and contractive,

\[
\boxed{
0\le G_{\Phi_0,K}(\omega)\le1
\quad\text{a.e.}
}
\]

and `G` is real a.e.

Because `A_K` maps real waveforms to real waveforms,

\[
G(-\omega)=\overline{G(\omega)}.
\]

Combining with reality yields

\[
\boxed{G(-\omega)=G(\omega)\quad\text{a.e.}}
\]

No continuity is implied by the universal theorem.

---

## 8. Publication-grade theorem statement

> **Theorem (autonomous-channel temporal Fisher spectrum).** Let `N` be a homogeneous Poisson point process of rate `Phi0>0` on the standard configuration space of locally finite counting measures on `R`. Let local source perturbations be generated initially by real `C_c^infty(R)` intensity waveforms. Let `K` be a parameter-independent probability kernel from the incident configuration to a standard-Borel accessible output-record space, and assume the input and output record spaces carry measurable time-shift actions under which `K` is covariant. Then the local output experiment is DQM in every admitted waveform direction. Its Fisher bilinear form extends uniquely to all `L^2(R)` and there is an even measurable function
> \[
> 0\le G_{\Phi_0,K}(\omega)\le1
> \]
> a.e. such that for every `u,v in L^2(R)`,
> \[
> \boxed{
> F_{\rm out}[u,v]
> =\frac{\Phi_0}{2\pi}
> \int_{\mathbb R}
> G_{\Phi_0,K}(\omega)
> U^*(\omega)V(\omega)d\omega.
> }
> \]
> The detector channel may have arbitrary hidden state, dead time, saturation, recovery, afterpulsing, multiple output events, analog marks, and nonlinear history dependence; no independent-event delay kernel is assumed.

### Scope sentence that should accompany it

The theorem is for local classical Poisson **intensity** perturbations and autonomous parameter-independent observation channels. It is not a theorem for arbitrary quantum optical inputs or arbitrary phase-sensitive optical measurements.

---

## 9. Narrowband operational meaning without illegal infinite sinusoids

The universal theorem gives `G` only as an `L^infty` equivalence class, so a pure infinite sinusoid should not be treated as the primitive statistical perturbation.

Choose a nonzero

\[
w\in C_c^\infty(\mathbb R)
\]

and define a normalized complex wavepacket

\[
u_T(t)=T^{-1/2}w(t/T)e^{i\omega_0t}.
\]

Then

\[
\|u_T\|_2=\|w\|_2
\]

and

\[
|U_T(\omega)|^2
=T|W(T(\omega-\omega_0))|^2.
\]

Therefore

\[
\frac{F_{\rm out}[u_T,u_T]}
{F_{\rm in}[u_T,u_T]}
=
\frac{\int G(\omega)T|W(T(\omega-\omega_0))|^2d\omega}
{\int T|W(T(\omega-\omega_0))|^2d\omega}.
\]

The normalized spectral weight is an approximate identity. Hence at every Lebesgue point of `G`,

\[
\boxed{
\lim_{T\to\infty}
\frac{F_{\rm out}[u_T,u_T]}
{F_{\rm in}[u_T,u_T]}
=G(\omega_0).
}
\]

For real cosine packets the spectral mass splits between `+omega0` and `-omega0`; evenness gives the same value.

Thus the ordinary “performance at frequency `omega0`” language is a rigorous narrowband corollary, not an assumption involving a non-`L^2` infinite sinusoid.

---

## 10. Frequency-by-frequency data processing

Suppose an accessible fine record `Y` is degraded by another parameter-independent autonomous kernel to `Z`.

The score projections obey the tower property:

\[
E[S_u\mid Z]
=E[E[S_u\mid Y]\mid Z].
\]

Therefore

\[
F_Y[u,u]\ge F_Z[u,u]
\quad\forall u,
\]

so

\[
A_Y\succeq A_Z.
\]

Both commute with translations, hence their difference is also a translation-invariant positive operator. Its Fourier multiplier is nonnegative a.e., giving

\[
\boxed{
G_Y(\omega)\ge G_Z(\omega)
\quad\text{a.e.}
}
\]

This is the exact general-channel frequency-resolved data-processing law.

Again, it is a consequence of standard Fisher data processing plus the autonomous spectral representation; do not present generic data processing as new mathematics.

---

## 11. What has now been closed

WP10 listed six formal issues. This work package closes or sharply localizes them:

1. **DQM under stochastic detector kernels:** closed by Kallenberg randomization + Pollard Theorem 7.
2. **Trajectory-space measurability:** use standard point-process configuration space for input and arbitrary standard-Borel output record with measurable shifts.
3. **Translation-invariant multiplier citation:** Stein 1970, Ch. II, §1.4, Prop. 2.
4. **Dense perturbation class:** use `C_c^infty`, then extend the bounded Fisher form uniquely to `L^2`.
5. **Sinusoidal interpretation:** narrowband wavepacket/Lebesgue-point corollary.
6. **Continuity of G:** deliberately **not** part of the general theorem; prove only in model-specific mixing classes if needed.

The remaining work is editorial theorem packaging and checking exact bibliographic formatting, not a conceptual proof gap.

---

## 12. Novelty consequence

This hardening strengthens the organizing theorem but does **not** enlarge the safe novelty claim.

The following are classical:

- Poisson likelihood/DQM;
- kernel randomization;
- DQM under measurable statistics;
- conditional expectation of the score;
- Fisher data processing;
- Riesz representation;
- translation-invariant `L^2` operators as Fourier multipliers;
- Lebesgue differentiation/approximate identities.

The possible Paper-2 contribution remains the **photodetection-channel synthesis and consequences**:

> the complete local temporal Fisher metric of an arbitrary autonomous classical photodetection channel is forced by time-translation symmetry to be frequency diagonal on the multiplicity-one Poisson intensity tangent, even when detector dynamics have arbitrary hidden memory and high-flux nonlinear history dependence.

That claim derives its publication value from the exact Type-II phenomena (WP06/WP07/WP13), not from inventing any of the functional-analytic ingredients.

---

## 13. Immediate next gate

With the WP10 proof architecture now formalized, the highest-value remaining theorem work is no longer basic measure theory.

Priority order:

1. finish the historical inverse-output audit flagged in WP16, especially Afanaseva–Mikhailova (1973);
2. decide whether WP13's deterministic-recovery Fisher singularity survives enough novelty pressure to be a principal theorem rather than a corollary;
3. either build a rigorous same-mean/same-variance recovery counterexample proving variance insufficiency, or abandon that branch;
4. keep WP08 provisional until its high-frequency residue proof is strengthened beyond the present sufficient mixing assumptions;
5. only then decide whether Paper 2 has earned manuscript drafting.
