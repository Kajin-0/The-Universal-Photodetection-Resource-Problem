# WP36 — Complete Weak-Waveform Fisher Operator and Universal Fisher Ordering

**Date:** 2026-08-20  
**Status:** Rev7 theorem-grade result; proof-hardened after first successful integration compile.

## Purpose

Raise the significance of the first autonomous-event paper without broadening its physical detector class. Rev6 derives the exact source-normalized Fisher-information transfer for sinusoidal modulation. WP36 proves that the same scalar spectrum `G(omega)` is the spectral multiplier of the **entire local Fisher-information operator for arbitrary finite-dimensional weak temporal waveform perturbations**.

The extension stays inside autonomous, time-translation-invariant, independent-event, weak coherent/direct-detection photodetection. It does not add high-flux history dependence, nonclassical light, coherent pointers, or free source-synchronous timing references.

---

# 1. Source class and Fourier convention

Let

\[
\Phi_{\boldsymbol\theta}(t)
=\Phi_0\left[1+\sum_{a=1}^{p}\theta_a s_a(t)\right],
\]

with real

\[
s_a\in L^2(\mathbb R)\cap L^\infty(\mathbb R),
\]

and sufficiently small `theta` so the intensity is nonnegative.

Because `L2 cap L-infinity` does not imply `L1`, define

\[
S_a=\mathcal F s_a
\]

as the **Plancherel `L2` Fourier transform**. When `s_a in L1 cap L2`, this agrees with

\[
S_a(\omega)=\int e^{-i\omega t}s_a(t)dt.
\]

The incident Poisson Fisher matrix is

\[
\boxed{
[F_{\rm in}]_{ab}
=\Phi_0\int s_a(t)s_b(t)dt
=\frac{\Phi_0}{2\pi}
\int S_a^*(\omega)S_b(\omega)d\omega.
}
\]

---

# 2. Complete weak-waveform Fisher operator

Keep the Rev6 marked subprobability kernel

\[
K(dm,d\tau)=\kappa(dm)\mu_m(d\tau),
\qquad
\eta=\kappa(\mathsf M)\le1.
\]

For mark `m`, define

\[
g_{a,m}(t)=\int s_a(t-\tau)\mu_m(d\tau).
\]

Convolution by the probability measure `mu_m` is contractive on `L2` and `L-infinity`, so `g_{a,m}` remains bounded and square-integrable. In the Plancherel sense,

\[
\widehat g_{a,m}(\omega)=S_a(\omega)H_m(\omega),
\qquad
H_m(\omega)=\int e^{-i\omega\tau}\mu_m(d\tau).
\]

The marked Poisson Fisher matrix is therefore

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

Hence multiplication by `G` is the complete local weak-temporal-waveform Fisher-information transfer operator for this theorem class. Parameter-independent downstream processing satisfies

\[
F_{\rm measured}\preceq F_{\rm out}.
\]

The Rev6 sinusoidal theorem is recovered as the long-window limit of square-integrable windowed sinusoids. In the translation-invariant limit, Fourier modes diagonalize the local Fisher operator with multiplier `G(omega)`.

---

# 3. Regularity of `G`

For every mark, `H_m` is a characteristic function. Therefore it is continuous, obeys

\[
H_m(-\omega)=H_m(\omega)^*,
\]

and satisfies `|H_m| <= 1`. Since `kappa` is finite, dominated convergence gives

\[
\boxed{
0\le G(\omega)\le\eta,
\qquad
G(-\omega)=G(\omega),
\qquad
G\in C(\mathbb R).
}
\]

This continuity matters: universal Fisher ordering can be stated **pointwise everywhere**, not merely almost everywhere.

---

# 4. Universal weak-waveform Fisher ordering

For two autonomous independent-event detectors `A` and `B`, the following are equivalent:

1. \(G_A(\omega)\ge G_B(\omega)\) for **every** real `omega`;
2. for every finite admissible real perturbation family `{s_a}`, the ideal primary-record Fisher matrices obey
   \[
   F_A\succeq F_B.
   \]

The forward implication follows from

\[
c^T(F_A-F_B)c
=\frac{\Phi_0}{2\pi}
\int [G_A-G_B]|S_c|^2d\omega\ge0.
\]

For the converse, if pointwise ordering fails at `omega_0`, continuity and evenness provide a symmetric finite-measure neighborhood `E` and `delta>0` with

\[
G_A-G_B\le-\delta
\]

on `E`. Choose a nonzero real-even `S in L1 cap L2` supported in `E`, for example an indicator of a finite-measure symmetric subset. Its inverse Fourier transform is real, bounded, and square-integrable, hence admissible. Then

\[
\int(G_A-G_B)|S|^2d\omega<0,
\]

contradicting universal Fisher dominance.

Therefore

\[
\boxed{
G_A(\omega)\ge G_B(\omega)\ \forall\omega
\iff
F_A\succeq F_B\ \text{for every admissible local weak temporal task}.
}
\]

Interpretation:

- `G_A = G_B` everywhere means Fisher-equivalence for every admissible weak temporal waveform task in this model;
- crossing spectra imply no task-independent Fisher ranking exists.

This is a Fisher-ordering theorem within the stated local waveform class, **not** a claim of Blackwell/statistical-experiment dominance.

---

# 5. Exact band-subspace guarantee

For scalar perturbation `s`,

\[
\rho_G[s]
=\frac{F_{\rm out}[s]}{F_{\rm in}[s]}
=\frac{\int G|S|^2}{\int|S|^2}.
\]

For spectra supported in a symmetric measurable set `E`, this is the Rayleigh quotient of the multiplication operator, so

\[
\operatorname*{ess\,inf}_{E}G
\le\rho_G[s]\le
\operatorname*{ess\,sup}_{E}G,
\]

and both bounds are sharp over admissible perturbations.

For the compact band `[-Omega,Omega]`, continuity upgrades the exact worst-case retention to

\[
\boxed{
\inf_{\operatorname{supp}S\subset[-\Omega,\Omega]}\rho_G[s]
=
\min_{|\omega|\le\Omega}G(\omega).
}
\]

Hence preserving at least absolute Fisher fraction `q` for **every** weak waveform in the band is equivalent to

\[
\boxed{
G(\omega)\ge q
\qquad\forall |\omega|\le\Omega.
}
\]

With Parseval,

\[
\int Gd\omega=\pi\mathfrak R_2,
\]

this universal band guarantee requires

\[
\boxed{
\mathfrak R_2\ge4Bq,
\qquad
\mathfrak H\ge4Bq,
\qquad B=\Omega/(2\pi).
}
\]

Thus the Rev6 `4Bq` coefficient is not only a flat-average necessary cost: it is also the necessary resource cost of a uniform Fisher guarantee over a full weak-waveform band-limited subspace.

---

# 6. Exact Fisher-equivalent bandwidth

For square-integrable conditional delay densities,

\[
\int G(\omega)d\omega=\pi\mathfrak R_2.
\]

Define

\[
\boxed{
B_{\rm FI}
\equiv
\frac1\eta\int_0^\infty G(2\pi f)df
=\frac{\mathfrak R_2}{4\eta},
\qquad \eta>0.
}
\]

Then

\[
\boxed{
B_{\rm FI}\le\frac{\mathfrak H}{4\eta}.
}
\]

For a common conditional-hazard ceiling `Lambda`,

\[
\boxed{B_{\rm FI}\le\Lambda/4.}
\]

A single exponential delay saturates the last bound. `B_FI` is an equivalent-rectangular **information-area bandwidth**, not a relabeled `-3 dB` bandwidth.

---

# 7. Independent delay-stage cascade and serial exponential example

For independent unmarked autonomous delay-only stages,

\[
\boxed{G_{12}(\omega)=G_1(\omega)G_2(\omega).}
\]

This scalar product law is intentionally restricted to independent unmarked delay stages; general retained marks remain governed by the full marked kernel.

For `k` serial exponential waiting stages of common rate `lambda`, with total capture probability `eta`,

\[
G_k(\omega)
=\eta\left(\frac{\lambda^2}{\lambda^2+\omega^2}\right)^k,
\]

\[
\boxed{
\frac{\mathfrak R_2}{\eta}
=\lambda\frac{(2k-2)!}{4^{k-1}[(k-1)!]^2},
}
\]

and

\[
\boxed{
B_{\rm FI}
=\frac{\lambda}{4}
\frac{\binom{2k-2}{k-1}}{4^{k-1}}
\sim\frac{\lambda}{4\sqrt{\pi(k-1)}}.
}
\]

This supplies an architecture-level interpretation: accumulated unresolved stochastic registration stages consume temporal Fisher bandwidth even when each stage has the same fast bare microscopic rate.

---

# 8. Novelty posture

Do **not** claim Fisher-information transfer functions generically new. Koppell and Kasevich (Optica 2021, DOI `10.1364/OPTICA.412129`) use a Fisher-information-based information transfer function for phase imaging.

The defensible Rev7 claim is:

> For the autonomous independent-event photodetection kernel, the exact marked-delay spectrum `G(omega)` is the complete local weak-temporal-waveform Fisher multiplier; its pointwise ordering is necessary and sufficient for universal Fisher dominance within that waveform class, while the atomic/collision/hazard hierarchy constrains its high-frequency residue, total spectral area, equivalent information bandwidth, and uniform band-limited retention.

Recent photodetector metrology showing non-equivalence of pulse, transient, and `-3 dB` response-time measurements (Deng, Van Thourhout, and Hens, ACS Photonics 2026, DOI `10.1021/acsphotonics.6c00438`) strengthens the motivation but does not itself establish these theorems.

---

# 9. Manuscript recommendation

Rev7 hierarchy:

1. retain the exact sinusoidal theorem as the shortest entry point;
2. promote it immediately to the complete weak-waveform Fisher operator;
3. prove continuity/evenness of `G`;
4. state universal pointwise weak-waveform Fisher ordering;
5. state exact compact-band worst-case retention;
6. retain Wiener atomic residue and Parseval collision resource;
7. define exact `B_FI = mathfrak R_2/(4 eta)`;
8. connect `B_FI` and uniform band guarantees to local hazard capacity;
9. give the independent-cascade / serial-Erlang example;
10. retain the three no-go constructions and restricted thermodynamic repair.

This materially increases conceptual and operational significance without weakening the clean Rev6 model-class boundary.
