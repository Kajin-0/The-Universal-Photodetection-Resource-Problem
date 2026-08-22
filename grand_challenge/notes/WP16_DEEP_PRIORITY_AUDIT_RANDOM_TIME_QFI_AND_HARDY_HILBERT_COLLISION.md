# WP16 — Deep priority audit: random-time QFI and Hardy–Hilbert collision

**Date:** 2026-08-21

## Status

**Material prior-art correction; core physics theorem survives.**

The first deep-priority pass produces a split result.

1. The sharp Mellin/operator inequality used in WP15 is not a plausible standalone mathematical novelty claim. It is an explicit specialization of classical parameterized Hardy–Hilbert integral inequalities with best Beta-function constants.
2. The targeted quantum-information search still has not located an exact predecessor for the **random latent-time distribution Fourier-mode estimation problem**, the exact source-normalized mode formula

   `G_Q(k)=2 sum_n q_n q_{n+k}/(q_n+q_{n+k})`,

   the positive-mode budget

   `sum_{k>=1} G_Q(k)<=2 nbar`,

   or the resulting random-time temporal-information interpretation of the continuum area law.
3. Priority is therefore **not certified**, but the candidate novelty has been narrowed materially: it must lie in the quantum statistical experiment, the mode-budget theorem, and the source-to-record temporal-information interpretation—not in the sharp Hilbert/Mellin constant itself.

No theorem coefficient changes.

---

## 1. Exact Hardy–Hilbert specialization behind the WP15 operator norm

WP15 reduces the density functional to

`A[q]=<r,Tr>`,

with

`(Tr)(s)=int_0^infinity [2st/(s+t)^3] r(t)dt`.

The current proof diagonalizes this positive homogeneous operator by Mellin transform and obtains

`||T||=pi/4`.

Classical Hardy–Hilbert theory already contains the relevant sharp weighted inequality. A standard parameterized form is

`iint f(x)g(y)/(x+y)^lambda dxdy`

`<= B(lambda/2,lambda/2)`

`   * [int x^(1-lambda)f(x)^2 dx]^(1/2)`

`   * [int y^(1-lambda)g(y)^2 dy]^(1/2)`,

for `lambda>0`, with the Beta-function constant best possible.

Set

`lambda=3`,

`f(x)=x r(x)`,

`g(y)=y r(y)`.

Then the weighted norms collapse exactly:

`int x^(-2) f(x)^2 dx = int r(x)^2 dx`,

and likewise for `g`.

Moreover

`B(3/2,3/2)`

`=Gamma(3/2)^2/Gamma(3)`

`=pi/8`.

Therefore the classical inequality gives

`iint [xy/(x+y)^3] r(x)r(y)dxdy <= (pi/8)||r||_2^2`.

Multiplying by the factor `2` in the WP15 kernel gives immediately

`boxed: <r,Tr> <= (pi/4)||r||_2^2`.

Thus the exact WP15 operator norm

`boxed: ||T||=pi/4`

is a direct Hardy–Hilbert best-constant specialization.

### Consequence

Do **not** claim mathematical novelty for:

- the operator norm `pi/4`;
- the Beta/Gamma constant;
- Mellin diagonalization of this homogeneous kernel;
- the sharpness mechanism at the operator level.

The WP15 layer-cake/Tonelli reduction remains a clean and useful proof route from the density functional to the classical operator inequality, but the final sharp analytic inequality belongs to established Hilbert-type inequality theory.

Primary literature identified in this pass includes:

- B. Yang, *On the norm of an integral operator and applications*, J. Math. Anal. Appl. **321**, 182–192 (2006), DOI `10.1016/j.jmaa.2005.07.071`;
- the broader Hardy–Hilbert survey literature documenting the parameterized best-constant formula with `B(lambda/2,lambda/2)` for `lambda>0`.

The exact density-functional statement

`iint q(x)q(y)/(q(x)+q(y)) dxdy <= (pi/2) int xq(x)dx`

may or may not have appeared verbatim, but after WP15's rearrangement/layer-cake identity it is an immediate corollary of established sharp Hardy–Hilbert theory. It should therefore not be advertised as a new theorem of classical analysis absent much stronger evidence.

---

## 2. Quantum prior-art families examined

The search was deliberately phrased in several neighboring languages because an equivalent result need not use the words “random time”.

### 2.1 U(1)/time-translation modes of asymmetry

Marvian–Spekkens and subsequent resource-theory work establish decomposition into `U(1)`/energy-gap modes, mode-preserving constraints under covariant processing, and mode-resolved asymmetry monotones.

This directly preempts novelty for the **mode decomposition itself**.

No located source in this family, however, treats a weak Fourier coefficient of a latent random group-translation distribution as the unknown parameter and derives the WP10 SLD-QFI retention formula normalized by the classical label Fisher information.

### 2.2 Phase diffusion / dephasing estimation

A large literature computes QFI for phase estimation in the presence of phase diffusion, jointly estimates phase and a diffusion-strength parameter, or treats estimation of dephasing/noise strength.

These models typically parameterize a low-dimensional family such as a Gaussian phase distribution through its variance or a channel strength. They are close in channel structure but are not, in the sources located so far, the same statistical problem as independently perturbing a Fourier coefficient of an otherwise uniform random phase/time distribution.

### 2.3 Random-unitary and noise-channel estimation

General quantum-channel estimation and adaptive noise-estimation work treats parameters of random-unitary/noisy channels and supplies powerful QFI/data-processing machinery.

The search did not locate the exact pure-state expression

`2 sum_n q_n q_{n+k}/(q_n+q_{n+k})`

as Fisher retention of the `k`th Fourier coefficient of the mixing distribution, nor a summed mean-generator theorem equivalent to `2 nbar`.

### 2.4 Quantum noise spectroscopy / characteristic-function methods

Quantum dephasing spectroscopy often reconstructs noise correlation functions, spectra, or characteristic functions from probe coherence. This is conceptually adjacent, but the retrieved work focuses on estimating properties of environmental stochastic processes from controlled probe dynamics rather than the WP10 random-translation mixture geometry and its all-mode energy budget.

---

## 3. Why the WP10 formula is still a priority risk

The absence of an exact match in this pass is not strong priority evidence.

Once the baseline random-time distribution is uniform, the state is `U(1)`-twirled. A Fourier perturbation of order `k` creates only off-diagonal blocks between energy sectors separated by `k`. Inserting those blocks into the standard SLD metric automatically produces the harmonic denominator `q_n+q_{n+k}`.

Therefore the exact mode formula is structurally natural from established QFI plus representation theory. A specialist paper on estimation of mixing weights/distributions of random-unitary channels could contain the same expression without using photodetection or temporal-information language.

The next priority search must therefore target **statistical estimation of group-distribution parameters**, not merely phase estimation under noise.

High-risk search languages include:

- estimation/tomography of probability measures on compact groups from quantum probes;
- local estimation of random-unitary mixing weights;
- Fourier/characteristic coefficients of phase-noise distributions;
- nonparametric quantum channel estimation for dephasing channels;
- quantum statistical inference for convolution/randomization channels;
- local asymptotic geometry of twirling channels.

---

## 4. Refined novelty candidate

After this audit, the defensible candidate contribution is the **combined physical/information-theoretic theorem stack**, not its classical analytic ingredients.

Potentially distinctive components are:

1. formulate temporal waveform information as estimation of Fourier modes of a **latent random event-time distribution** encoded by translations of a fixed semibounded-energy excitation;
2. derive the exact source-normalized quantum retention

   `G_Q(k)=2 sum_n q_n q_{n+k}/(q_n+q_{n+k})`;

3. prove the all-positive-mode resource budget

   `sum_{k>=1}G_Q(k)<=2 nbar`;

4. take the physically controlled continuum limit and identify the sharp integrated temporal-information consequence

   `int_R G_Q(nu)dnu<=pi Ebar^+/hbar`;

5. convert that area theorem into the Planck-scale flat-band inverse law

   `Ebar^+ >= (2/pi)hBq0`;

6. place the result between the stricter covariant-timestamp subclass and the WP14 arbitrary-waveform no-go;
7. interpret the bound as an upstream encoded-state limit inherited by arbitrary parameter-independent quantum detector processing.

The mathematical `pi` coefficient is important physically, but it must be presented as arising from a classical sharp Hardy–Hilbert inequality after the quantum-information reduction.

---

## 5. The theorem itself is unchanged

Nothing in this prior-art collision changes the validity or constants of WP12/WP15.

For finite-first-moment normalized positive-frequency density `q(w)`,

`boxed: int_0^infinity G_Q(nu)dnu <= (pi/2)wbar`,

`boxed: int_R G_Q(nu)dnu <= pi Ebar^+/hbar`,

and a flat guaranteed ordinary-frequency band obeys

`boxed: Ebar^+ >= (2/pi)hBq0`.

The change is solely one of **priority attribution and manuscript positioning**.

---

## 6. Revised hostile gates

### Gate 1A — deeper quantum-statistics priority search

Search specifically for estimation of Fourier coefficients/mixing weights of `U(1)` random-unitary channels and probability measures on groups. This is now more important than further generic QFI or phase-diffusion searches.

### Gate 1B — exact density-functional provenance

Determine whether the harmonic-mean density inequality itself has appeared explicitly, rather than merely as an immediate corollary after layer cake. This affects mathematical citation style, not theorem validity.

### Gate 2 — operational attainability

Determine whether one physical measurement family can approach the integrated `pi` QFI-area coefficient. Per-mode SLD optima are generally incompatible, so the operational classical-FI area may have a smaller universal constant.

### Gate 3 — optical-source embedding

Strengthen the independent quantum-marked Poisson/event construction into publication-grade incoherent bosonic-field language.

---

## Decision

The first deep-priority pass **does not preempt the Grand Challenge result**, but it removes any remaining basis for marketing the sharp `pi/4` Mellin/operator constant as new mathematics.

The physics priority question remains open and has become more sharply posed:

> Has quantum estimation theory already derived the Fisher geometry and mean-generator mode budget for Fourier perturbations of a random `U(1)` translation distribution?

Until that question is answered, do not draft the foundational manuscript and do not make a strong priority claim.