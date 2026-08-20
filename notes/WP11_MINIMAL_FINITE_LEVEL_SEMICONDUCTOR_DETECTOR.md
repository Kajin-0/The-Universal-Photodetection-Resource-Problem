# WP11 — Minimal finite-level semiconductor photodetector resource theorem

**Date:** 2026-08-20

## Purpose

WP10 established that the optical-capture operator, internal transduction dynamics, and electrical pointer/readout operator must be kept distinct. This note builds the smallest coherent finite-level detector in which all three are explicit and derives an exact optical-information-to-electrical-record transfer law.

The model is intentionally minimal. It is not a complete semiconductor device model. Its role is to identify which microscopic quantities survive after removing arbitrary rates and abstract pointer generators.

---

# 1. Three-node single-excitation detector

Work in the one-excitation sector with basis

\[
|F\rangle,\qquad |X\rangle,\qquad |C\rangle,
\]

where

- `|F>` is one excitation in the incident optical mode;
- `|X>` is a captured electronic excitation;
- `|C>` is an electrically distinguishable charge-separated/readout state.

The resonant ideal Hamiltonian is

\[
\boxed{
\frac{H_1}{\hbar}
=
\begin{pmatrix}
0 & g & 0\\
g & 0 & \kappa\\
0 & \kappa & 0
\end{pmatrix}.
}
\]

`g` is the optical capture coupling and `kappa` is the internal electrical/transduction coupling.

The three stages are now operator-distinct:

\[
\text{optical field}
\xrightarrow{g}
\text{captured excitation}
\xrightarrow{\kappa}
\text{charge pointer}.
\]

---

# 2. Exact transfer amplitude

Let

\[
\Omega=\sqrt{g^2+\kappa^2}.
\]

Starting in `|F>`, direct exponentiation gives

\[
\boxed{
A_{F\to C}(t)
=-\frac{2g\kappa}{g^2+\kappa^2}
\sin^2\!\left(\frac{\Omega t}{2}\right).
}
\]

Hence

\[
\boxed{
P_C(t)
=\frac{4g^2\kappa^2}{(g^2+\kappa^2)^2}
\sin^4\!\left(\frac{\Omega t}{2}\right).
}
\]

The maximum over time is

\[
\boxed{
P_C^{\max}
=\frac{4g^2\kappa^2}{(g^2+\kappa^2)^2}.
}
\]

**Status:** PROVED.

---

# 3. Exact information-transfer interpretation

Encode a weak optical parameter in the single-rail family

\[
|\psi_\theta\rangle
=\cos\theta|0\rangle+\sin\theta|1_F\rangle.
\]

Its input QFI is

\[
\boxed{F_{\rm in}^Q=4.}
\]

Assume the optical vacuum leaves the detector in its electrical zero state. At time `t`, perform the binary electrical measurement

\[
Y=1 \iff |C\rangle\text{ occupied}.
\]

Then

\[
p_1(\theta,t)=\sin^2\theta\,P_C(t).
\]

The Bernoulli Fisher information obeys

\[
\lim_{\theta\to0}
F_Y(\theta,t)
=4P_C(t).
\]

Therefore the source-normalized information-transfer efficiency is exactly

\[
\boxed{
\eta_{\mathcal I}(t)
=\frac{F_Y}{F_{\rm in}^Q}
=P_C(t).
}
\]

Thus

\[
\boxed{
\eta_{\mathcal I}(t)
=\frac{4g^2\kappa^2}{(g^2+\kappa^2)^2}
\sin^4\!\left(\frac{\sqrt{g^2+\kappa^2}\,t}{2}\right).
}
\]

This is an exact optical-input-to-electrical-record FI law for the model, not merely a population-transfer analogy.

**Status:** PROVED.

---

# 4. Resource matching / coherent impedance matching

The time-maximized information fraction is

\[
\eta_{\max}
=\frac{4r^2}{(1+r^2)^2},
\qquad
r=\frac{\kappa}{g}.
\]

Therefore

\[
\boxed{\eta_{\max}=1\iff \kappa=g.}
\]

At fixed `g`, taking the internal readout arbitrarily fast does not produce an ideal coherent detector:

\[
\kappa/g\to\infty
\quad\Rightarrow\quad
\eta_{\max}\sim4g^2/\kappa^2\to0.
\]

Similarly, `g/kappa -> infinity` also kills transfer.

A target fraction `eta_*` is possible only if

\[
\frac{4r^2}{(1+r^2)^2}\ge\eta_*.
\]

Writing

\[
s=\sqrt{1-\eta_*},
\]

this is equivalent to the exact matching window

\[
\boxed{
\sqrt{\frac{1-s}{1+s}}
\le
\frac{\kappa}{g}
\le
\sqrt{\frac{1+s}{1-s}}.
}
\]

Thus high information efficiency requires increasingly precise matching of optical capture and internal transduction scales.

This is the closed coherent model's version of impedance matching. Do not claim the generic impedance-matching principle as novel.

---

# 5. First-hit time

If `eta_* <= eta_max`, the first time at which the target is reached is

\[
\boxed{
t_{\eta_*}
=\frac{2}{\sqrt{g^2+\kappa^2}}
\arcsin\!\left[
\left(\frac{\eta_*}{\eta_{\max}}\right)^{1/4}
\right].
}
\]

For perfect matching `g=kappa=gamma`,

\[
\eta_{\mathcal I}(t)
=\sin^4\!\left(\frac{\sqrt2\gamma t}{2}\right),
\]

and perfect transfer first occurs at

\[
\boxed{
t_{1}=\frac{\pi}{\sqrt2\gamma}.}
\]

---

# 6. Electrical current operator identifies kappa physically

Let the electrical charge pointer be

\[
Q=e|C\rangle\langle C|.
\]

The electrical current operator is

\[
\hat I
=\frac{i}{\hbar}[H_1,Q]
=i e\kappa
\left(|X\rangle\langle C|-|C\rangle\langle X|\right).
\]

Its nonzero eigenvalues are `+e kappa` and `-e kappa`, so

\[
\boxed{\|\hat I\|=e|\kappa|.}
\]

Therefore the internal rate is exactly an electrical current-matrix-element capacity:

\[
\boxed{|\kappa|=\|\hat I\|/e.}
\]

This removes one abstract rate from the theorem.

---

# 7. General finite-level current-capacity theorem

Let `H_S` and charge observable `Q_S` act on any finite accessible electrical subspace `S`. Define their spectral spans

\[
W_S=\lambda_{\max}(H_S)-\lambda_{\min}(H_S),
\]

\[
\Delta Q_S=\lambda_{\max}(Q_S)-\lambda_{\min}(Q_S).
\]

With

\[
I_S=\frac{i}{\hbar}[H_S,Q_S],
\]

center both operators at the midpoints of their spectra. The commutator norm inequality gives

\[
\|[H_S,Q_S]\|
\le
2\frac{W_S}{2}\frac{\Delta Q_S}{2}.
\]

Hence

\[
\boxed{
\|I_S\|
\le
\frac{W_S\Delta Q_S}{2\hbar}.
}
\]

The result is tight. A two-level realization

\[
H_S=(W_S/2)\sigma_x,
\qquad
Q_S=(\Delta Q_S/2)\sigma_z
\]

saturates it.

For a binary one-electron pointer, `Delta Q_S=e`, so

\[
\boxed{|\kappa|\le W_S/(2\hbar).}
\]

Thus a finite electrical energy span supplies an absolute transduction-rate cap without calling the cap itself a bandwidth.

**Status:** PROVED and tight.

---

# 8. Sequential cut bounds

Even outside the exactly resonant constant-coupling chain, the source/capture and capture/charge cuts give separate subspace-flow constraints.

Let

\[
G(t)=\int_0^t|g(s)|ds,
\qquad
K(t)=\int_0^t|\kappa(s)|ds.
\]

Starting with the excitation on the optical side and no charge occupation,

\[
\boxed{
\eta_{\mathcal I}(t)
\le
\min\left[
\sin^2(\min\{G(t),\pi/2\}),
\sin^2(\min\{K(t),\pi/2\})
\right]
}
\]

for any binary charge measurement whose FI cannot exceed the excitation probability delivered across either cut.

For constant couplings and target `eta_*`, a necessary condition is therefore

\[
\boxed{
t\ge
\max\left[
\frac{\arcsin\sqrt{\eta_*}}{|g|},
\frac{\arcsin\sqrt{\eta_*}}{|\kappa|}
\right].}
\]

The exact three-node result is generally stronger because it also captures coherent matching/interference.

---

# 9. What this model resolves

The minimal detector explicitly distinguishes:

1. **optical capture resource** `g`;
2. **internal/electrical transduction resource** `kappa` or equivalently `||I||/e`;
3. **electrical state capacity** through the finite charge/energy subspace.

The next step is to map `||I||` to actual semiconductor transport and electrode geometry using Shockley-Ramo and band-structure velocity operators.

---

# 10. Limitations

The exact transfer formula assumes:

- one coherent excitation;
- a closed resonant three-node chain;
- no irreversible localization, phonons, traps, recombination, dark counts, or amplifier dynamics;
- a binary charge readout;
- no many-carrier gain.

It is therefore an ideal upper-envelope model. Adding uncontrolled loss/noise cannot increase electrical FI by data processing, but adding engineered reservoirs can change the coherent matching law and must be treated as a distinct model.

Do not extrapolate the `kappa -> infinity` coherent mismatch result to every dissipative photodetector architecture.

---

# 11. Status

- Exact three-node optical-to-charge FI law: **PROVED**.
- Current-operator identification `||I||=e|kappa|`: **PROVED**.
- General finite-level current-capacity theorem: **PROVED and tight**.
- Semiconductor microscopic mapping: moved to the companion WP11 Shockley-Ramo/Kane note.
