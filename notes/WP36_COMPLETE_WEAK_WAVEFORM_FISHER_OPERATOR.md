# WP36 — Complete Weak-Waveform Fisher Operator and Detector Ordering

**Date:** 2026-08-20

## Purpose

Raise the significance of the first autonomous-event paper without broadening its detector class. Rev6 derives the exact source-normalized Fisher-information transfer for a sinusoidal modulation. The result below shows that the same scalar spectrum `G(omega)` is in fact the spectral multiplier of the **entire local Fisher-information operator for arbitrary finite-dimensional weak temporal waveform perturbations**.

This turns the sinusoidal theorem into a Fourier-mode corollary and yields a necessary-and-sufficient detector ordering for every weak temporal estimation task within the same independent-event model.

The extension does **not** add high-flux history dependence, nonclassical light, coherent pointers, or external timing references.

---

# 1. Source class

Let

\[
\Phi_{\boldsymbol\theta}(t)
=\Phi_0\left[1+\sum_{a=1}^{p}\theta_a s_a(t)\right],
\]

where the perturbation modes are real-valued

\[
s_a\in L^2(\mathbb R)\cap L^\infty(\mathbb R),
\]

and `theta` is restricted to a sufficiently small neighborhood of zero so that the intensity is nonnegative.

Define the Fourier transform convention

\[
S_a(\omega)=\int_{-\infty}^{\infty}e^{-i\omega t}s_a(t)dt.
\]

At `theta=0`, the incident Poisson Fisher matrix is

\[
\boxed{
[F_{\rm in}]_{ab}
=\Phi_0\int s_a(t)s_b(t)dt
=\frac{\Phi_0}{2\pi}
\int S_a^*(\omega)S_b(\omega)d\omega.
}
\]

The finite-energy perturbation makes this matrix finite even though the stationary baseline process is defined on the full time axis.

---

# 2. Output Fisher matrix through the marked delay kernel

Keep exactly the Rev6 autonomous subprobability kernel

\[
K(dm,d\tau)=\kappa(dm)\mu_m(d\tau),
\qquad
\eta=\kappa(\mathsf M)\le1.
\]

For mark `m`, define

\[
g_{a,m}(t)
=\int s_a(t-\tau)\mu_m(d\tau).
\]

The marked output intensity measure is

\[
\lambda_{\boldsymbol\theta}(t,dm)
=\Phi_0\left[1+\sum_a\theta_a g_{a,m}(t)\right]\kappa(dm).
\]

At the baseline,

\[
\partial_{\theta_a}\lambda(t,dm)|_0
=\Phi_0 g_{a,m}(t)\kappa(dm).
\]

Therefore the Poisson Fisher matrix is

\[
[F_{\rm out}]_{ab}
=\Phi_0\int_{\mathsf M}\kappa(dm)
\int g_{a,m}(t)g_{b,m}(t)dt.
\]

Because

\[
\widehat g_{a,m}(\omega)=S_a(\omega)H_m(\omega),
\qquad
H_m(\omega)=\int e^{-i\omega\tau}\mu_m(d\tau),
\]

Parseval gives

\[
\boxed{
[F_{\rm out}]_{ab}
=\frac{\Phi_0}{2\pi}
\int_{-\infty}^{\infty}
G(\omega)S_a^*(\omega)S_b(\omega)d\omega,
}
\]

with exactly the Rev6 spectrum

\[
\boxed{
G(\omega)=\int_{\mathsf M}|H_m(\omega)|^2\kappa(dm).
}
\]

Thus the multiplication operator

\[
\mathcal T_G:S(\omega)\mapsto G(\omega)S(\omega)
\]

is the complete local weak-waveform Fisher-information transfer operator for the theorem class.

Parameter-independent downstream processing obeys the matrix data-processing inequality

\[
F_{\rm measured}\preceq F_{\rm out}.
\]

---

# 3. Single-tone theorem becomes a corollary

The Rev6 sinusoidal result is the long-observation periodic/Fourier-eigenmode specialization of the operator theorem. A perturbation concentrated at `+/- omega_0` is multiplied by `G(omega_0)`.

This removes the main possible conceptual objection that the theorem is intrinsically tied to the choice of a sinusoidal test signal. The sinusoid is a diagonalizing mode, not the fundamental source class.

---

# 4. Complete detector ordering theorem

Consider two autonomous independent-event detectors `A` and `B` with transfer spectra `G_A` and `G_B`.

## Theorem

The following are equivalent:

1. `G_A(omega) >= G_B(omega)` for almost every `omega`;
2. for every finite `p` and every admissible real perturbation family `{s_a}`, the ideal primary-record Fisher matrices satisfy
   \[
   F_A\succeq F_B.
   \]

### Forward implication

For every vector `c`, let

\[
S_c(\omega)=\sum_a c_a S_a(\omega).
\]

Then

\[
c^T(F_A-F_B)c
=\frac{\Phi_0}{2\pi}
\int [G_A(\omega)-G_B(\omega)]|S_c(\omega)|^2d\omega\ge0.
\]

Hence `F_A-F_B` is positive semidefinite.

### Converse

If `G_A<G_B` on a set of nonzero measure, then because the difference is bounded, measurable, and even, there exists a finite symmetric frequency region on which the deficit is separated from zero on a subset of positive measure. By regularity of Lebesgue measure, choose a real even smooth compactly supported spectrum `S` concentrated sufficiently strongly on that set. Its inverse Fourier transform is a real Schwartz function, hence admissible (`L2` and bounded), and

\[
\int [G_A-G_B]|S|^2d\omega<0.
\]

The scalar (`p=1`) Fisher information of detector `A` is then smaller than that of `B`, contradicting universal Fisher dominance.

Therefore pointwise almost-everywhere ordering of `G` is **necessary and sufficient** for universal local temporal-information ordering in this detector class.

## Interpretation

`G` is not merely one performance curve. It is a complete order parameter for all weak temporal waveform-estimation tasks in the model.

If

\[
G_A(\omega)=G_B(\omega)\quad\text{a.e.},
\]

then the two detectors are Fisher-equivalent for every admissible weak temporal perturbation despite possibly having different internal mechanisms, latency, rise-time descriptions, or delay decompositions.

Crossing spectra imply there is no task-independent ranking: each detector is better for some weak temporal waveform tasks.

---

# 5. Exact Fisher-equivalent bandwidth

For square-integrable conditional delay densities, Rev6 proves

\[
\int_{-\infty}^{\infty}G(\omega)d\omega=\pi\mathfrak R_2.
\]

Since `G` is even and `G(0)=eta`, define the ordinary-frequency **DC-normalized Fisher-equivalent bandwidth**

\[
\boxed{
B_{\rm FI}
\equiv
\frac1\eta\int_0^\infty G(2\pi f)df,
\qquad \eta>0.
}
\]

Changing variables gives the exact identity

\[
\boxed{
B_{\rm FI}=\frac{\mathfrak R_2}{4\eta}.
}
\]

This is an equivalent-rectangular bandwidth for source-normalized Fisher transfer, not an electrical amplitude bandwidth.

Using the hazard--collision inequality

\[
\mathfrak R_2\le\mathfrak H
\]

gives

\[
\boxed{
B_{\rm FI}\le\frac{\mathfrak H}{4\eta}.
}
\]

If all captured-event conditional hazards obey a common ceiling `Lambda`, then `mathfrak H <= eta Lambda`, so

\[
\boxed{
B_{\rm FI}\le\frac{\Lambda}{4}.
}
\]

For a single exponential delay with rate `Lambda`, equality holds:

\[
G(\omega)=\eta\frac{\Lambda^2}{\Lambda^2+\omega^2},
\qquad
B_{\rm FI}=\frac{\Lambda}{4}.
\]

Its electrical-style half-power frequency would be `Lambda/(2 pi)`, confirming that `B_FI` is a distinct area metric rather than a relabeled `-3 dB` bandwidth.

---

# 6. Independent delay-stage cascade law

For an unmarked autonomous delay-only stage `j` with capture probability `eta_j` and independent delay law with characteristic function `H_j`,

\[
G_j(\omega)=\eta_j|H_j(\omega)|^2.
\]

For two serial independent stages, capture probabilities multiply and delays add. Hence

\[
H_{12}=H_1H_2,
\qquad
\eta_{12}=\eta_1\eta_2,
\]

so

\[
\boxed{
G_{12}(\omega)=G_1(\omega)G_2(\omega).
}
\]

Thus independent unresolved timing stages multiply Fisher transfer. Equivalently, where `G_j>0`,

\[
-\ln G_{12}=-\ln G_1-\ln G_2.
\]

The simple product law is intentionally limited to independent unmarked delay-only stages. General retained marks or history-dependent stages remain governed by the full marked kernel rather than this scalar factorization.

---

# 7. Serial exponential example

For `k` independent serial exponential waiting stages of common rate `lambda`, with total capture probability `eta`, the total delay is Erlang/Gamma with integer shape `k`:

\[
f_k(t)=\frac{\lambda^k t^{k-1}e^{-\lambda t}}{(k-1)!}.
\]

Then

\[
H_k(\omega)=\left(\frac{\lambda}{\lambda+i\omega}\right)^k,
\]

and

\[
\boxed{
G_k(\omega)
=\eta\left(\frac{\lambda^2}{\lambda^2+\omega^2}\right)^k.
}
\]

Direct integration gives

\[
\boxed{
\frac{\mathfrak R_2}{\eta}
=\lambda\frac{(2k-2)!}{4^{k-1}[(k-1)!]^2}.
}
\]

Therefore

\[
\boxed{
B_{\rm FI}
=\frac{\lambda}{4}
\frac{\binom{2k-2}{k-1}}{4^{k-1}}.
}
\]

Using the central-binomial asymptotic,

\[
\boxed{
B_{\rm FI}\sim\frac{\lambda}{4\sqrt{\pi(k-1)}}
\qquad(k\to\infty).
}
\]

This gives an architecture-level interpretation: even if every microscopic serial registration step has the same fast bare rate, accumulated unresolved stochastic timing progressively consumes equivalent temporal Fisher bandwidth.

The exact formula was independently checked symbolically for integer `k=1,...,5` and reduces to `eta lambda`, `eta lambda/2`, `3 eta lambda/8`, `5 eta lambda/16`, ... for `mathfrak R_2`.

---

# 8. Novelty positioning

Do **not** claim that Fisher-information transfer functions are generically new. Koppell and Kasevich (Optica 2021, DOI `10.1364/OPTICA.412129`) use a Fisher-information-based information transfer function for phase imaging.

The defensible claim is narrower and stronger:

> For the autonomous independent-event photodetection kernel, the same exact marked-delay spectrum `G(omega)` is the complete spectral multiplier of the local temporal-waveform Fisher operator, and pointwise ordering of `G` is necessary and sufficient for one detector to Fisher-dominate another over every admissible weak temporal waveform task.

Recent photodetector metrology work also explicitly emphasizes that pulse response, ultrafast transient response, and `-3 dB` bandwidth need not measure the same underlying detector dynamics (Deng, Van Thourhout, and Hens, ACS Photonics 2026, DOI `10.1021/acsphotonics.6c00438`). This strengthens the motivation for an information-based performance object, but does not itself establish the theorem above.

---

# 9. Manuscript recommendation

This WP is strong enough to justify a Rev7 significance pass.

Recommended Rev7 hierarchy:

1. exact sinusoidal marked-event transfer retained as the shortest entry point;
2. immediately promote it to the complete weak-waveform Fisher operator;
3. state the universal detector-ordering theorem;
4. retain Wiener atomic residue;
5. retain Parseval collision resource;
6. define exact `B_FI = mathfrak R_2/(4 eta)`;
7. connect `B_FI` to local hazard capacity;
8. give the independent-cascade / serial-Erlang example;
9. retain the three no-go constructions and restricted thermodynamic repair.

This increases conceptual and operational significance without weakening the clean model-class boundary of Rev6.
