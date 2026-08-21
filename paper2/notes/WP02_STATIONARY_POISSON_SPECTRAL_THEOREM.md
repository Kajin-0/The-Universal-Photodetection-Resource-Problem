# WP02 — Stationary Poisson Spectral Theorem Beyond Independent Events

**Status:** central candidate breakthrough theorem. Formal proof architecture is complete; measure-theoretic hypotheses and hostile prior-art review remain open.

## 1. Target

Show that Paper 1's existence of a complete scalar temporal Fisher spectrum does **not** fundamentally require an independent-event delay kernel.

The proposed theorem covers a stationary Poisson optical input and an **arbitrary autonomous detector channel**, including high-flux history dependence.

The detector may contain:

- dead time;
- saturation;
- recovery;
- afterpulsing;
- hidden-state memory;
- state-dependent efficiency;
- multiple registrations;
- stochastic gain;
- analog output marks;
- arbitrary nonlinear dependence on the previous input/output history.

The only structural requirements are that the detector acts as a parameter-independent stochastic channel and is covariant under global time translations at the operating point.

---

## 2. Poisson weak-waveform tangent space

Let `N` be a homogeneous Poisson point process on `R` of rate `Phi0>0`.

For a real temporal perturbation `u` in a dense admissible class such as

\[
u\in L^2(\mathbb R)\cap L^\infty(\mathbb R),
\]

consider the local source family

\[
\Phi_\epsilon(t)=\Phi_0[1+\epsilon u(t)]
\]

for sufficiently small `epsilon`.

At `epsilon=0`, the score is

\[
\boxed{
S_u(N)=\int_{\mathbb R}u(t)\,[N(dt)-\Phi_0dt].
}
\]

Poisson isometry gives

\[
\boxed{
\mathbb E_0[S_uS_v]
=\Phi_0\int_{\mathbb R}u(t)v(t)dt.
}
\]

Thus, after normalization by `sqrt(Phi0)`, the source waveform tangent space is isometric to scalar `L^2(R)`.

This **multiplicity-one temporal tangent representation** is the key reason a scalar spectrum may exist even when the detector itself has arbitrarily complicated memory.

---

## 3. Arbitrary detector channel

Let `K(dy|n)` be a parameter-independent Markov kernel from the complete incident photon trajectory `N` to a complete accessible detector record `Y`.

No low-overlap or independent-registration factorization is assumed.

By WP01, the output score for waveform `u` is

\[
S_u^{\rm out}(Y)
=\mathbb E_0[S_u(N)|Y].
\]

Define a bilinear form on waveforms by

\[
\mathcal F_K[u,v]
=\mathbb E_0[S_u^{\rm out}S_v^{\rm out}].
\]

Data processing gives

\[
|\mathcal F_K[u,v]|
\le \Phi_0\|u\|_2\|v\|_2.
\]

Therefore there is a unique bounded self-adjoint positive contraction

\[
\boxed{
\mathcal A_K:L^2(\mathbb R)\to L^2(\mathbb R)
}
\]

such that

\[
\boxed{
\mathcal F_K[u,v]
=\Phi_0\langle u,\mathcal A_Kv\rangle_{L^2}.
}
\]

and

\[
0\preceq\mathcal A_K\preceq I.
\]

`A_K` is the waveform-space version of WP01's score-space retention operator.

---

## 4. Autonomy / time-translation covariance

Let `Theta_a` shift an entire input or output trajectory by `a`, and let

\[
(U_au)(t)=u(t-a)
\]

be the unitary translation on the source waveform space.

Assume the detector is autonomous in the strong stochastic-channel sense

\[
K(\Theta_a B\mid \Theta_a n)=K(B\mid n)
\]

for all relevant measurable output events `B`, input trajectories `n`, and shifts `a` (or an equivalent almost-sure/covariant formulation sufficient for the proof).

Because the baseline Poisson process is stationary and the detector channel is covariant, the joint baseline law of `(N,Y)` is stationary.

The score transforms covariantly:

\[
S_{U_au}(N)=S_u(\Theta_{-a}N)
\]

up to the selected sign convention for trajectory shifts.

Conditional expectation therefore transforms covariantly as well. Consequently

\[
\boxed{
\mathcal A_KU_a=U_a\mathcal A_K
\qquad\forall a\in\mathbb R.
}
\]

This is the crucial structural step.

---

## 5. Fourier-multiplier theorem

A standard harmonic-analysis theorem says that a bounded operator on scalar `L^2(R)` that commutes with all translations is a Fourier multiplier.

Therefore there exists an essentially bounded measurable function

\[
G_{\Phi_0,K}(\omega)
\]

such that

\[
\boxed{
\widehat{\mathcal A_Ku}(\omega)
=G_{\Phi_0,K}(\omega)\,\widehat u(\omega)
\quad\text{a.e.}
}
\]

Since `A_K` is positive and contractive,

\[
\boxed{
0\le G_{\Phi_0,K}(\omega)\le1
\quad\text{for a.e. }\omega.
}
\]

Because the physical operator preserves real waveforms and is self-adjoint, one expects

\[
G_{\Phi_0,K}(-\omega)=G_{\Phi_0,K}(\omega)
\]

a.e.; this should be stated only after the real/complexification proof is written carefully.

---

## 6. Complete arbitrary-waveform Fisher formula

With Fourier convention

\[
U(\omega)=\int_{\mathbb R}u(t)e^{-i\omega t}dt,
\]

Parseval gives

\[
\boxed{
\mathcal F_K[u,v]
=\frac{\Phi_0}{2\pi}
\int_{\mathbb R}
G_{\Phi_0,K}(\omega)
U^*(\omega)V(\omega)d\omega.
}
\]

For a finite waveform family `{u_a}`,

\[
\boxed{
[F_{\rm out}]_{ab}
=\frac{\Phi_0}{2\pi}
\int
G_{\Phi_0,K}(\omega)
U_a^*(\omega)U_b(\omega)d\omega.
}
\]

This is structurally identical to Paper 1's complete weak-waveform theorem, but the derivation no longer uses independent registered events, a delay distribution, a primary-event kernel, or low-overlap capture.

The entire detector's nonlinear high-flux dynamics are compressed, at the local Fisher level, into a baseline-flux-dependent spectrum `G_{Phi0,K}`.

---

## 7. Candidate main theorem statement

> **General autonomous photodetection Fisher-spectrum theorem.**  Consider weak deterministic intensity perturbations of a stationary Poisson optical input at baseline flux `Phi0`. For any parameter-independent autonomous stochastic detector channel whose output experiment is DQM for the admitted perturbations, there exists a measurable source-normalized Fisher-retention spectrum `G_{Phi0}(omega)` with `0<=G_{Phi0}<=1` a.e. such that the complete local Fisher matrix for every finite family of square-integrable temporal waveforms is obtained by multiplication by `G_{Phi0}` in frequency space.

This theorem would apply at arbitrary baseline flux and with arbitrary detector memory.

### Critical wording

Do **not** call this a generic theorem for all optical measurements. The source class is still classical Poisson intensity modulation. The detector output may be arbitrary, but the scalarization relies on the multiplicity-one temporal tangent representation and stationarity.

---

## 8. Universal detector ordering survives high flux

For two autonomous detector channels A and B at the same baseline source flux,

\[
\mathcal A_A\succeq\mathcal A_B
\iff
G_A(\omega)\ge G_B(\omega)\quad\text{a.e.}
\]

Hence

\[
\boxed{
G_A\ge G_B\ \text{a.e.}
\iff
A\text{ locally Fisher-dominates }B
\text{ for every admitted weak temporal waveform task.}
}
\]

This extends Paper 1's ordering theorem from independent low-overlap event channels to arbitrary autonomous history-dependent detectors.

---

## 9. Pointwise data processing under record degradation

If an autonomous detector record is subsequently coarse-grained through a parameter-independent autonomous channel,

\[
\mathcal A_{\rm fine}\succeq\mathcal A_{\rm coarse}.
\]

Because both operators are Fourier multipliers,

\[
\boxed{
G_{\rm fine}(\omega)
\ge G_{\rm coarse}(\omega)
\quad\text{a.e.}
}
\]

Thus the mark-refinement result of Paper 1 becomes a general **frequency-by-frequency data-processing law**, not merely an event-kernel Jensen inequality.

This should be one of the strongest corollaries if the proof survives.

---

## 10. General cascade: no universal product law

For two autonomous stochastic stages in cascade, the overall detector still has a scalar `G_total(omega)` by the theorem. Data processing gives

\[
G_{\rm total}(\omega)\le G_1(\omega)
\quad\text{a.e.}
\]

but in general

\[
G_{\rm total}\ne G_1G_2.
\]

Paper 1's product law is therefore recognized as a special factorization arising from independent unresolved stochastic displacements, not a generic property of detector cascades.

---

## 11. Recovery of Paper 1

In Paper 1's autonomous low-overlap one-primary-registration model,

\[
K(dm,d\tau)=\kappa(dm)\mu_m(d\tau),
\]

with retained mark `m` and conditional delay characteristic function `H_m(omega)`.

The new general spectrum must reduce to

\[
\boxed{
G_{\Phi_0,K}(\omega)
=\int|H_m(\omega)|^2\kappa(dm)
}
\]

in the independent-event regime and become independent of `Phi0` there.

This recovery theorem is essential: Paper 2 must contain Paper 1 as an exact special case, not merely an analogy.

---

## 12. What changes at high flux

For history-dependent detectors, `G` should generally depend on the operating flux:

\[
G=G_{\Phi_0}(\omega).
\]

Dead time, saturation, recovery, and afterpulsing alter the conditional expectation of the input score given the complete detector record. Therefore they alter the Fisher spectrum even if no single-event IRF exists.

This gives a clean distinction:

- **Paper 1:** timing loss represented by a per-photon marked-delay law;
- **Paper 2:** information loss represented by projection of the full source score through an arbitrary trajectory channel.

A major next goal is an explicit `G_{Phi0}` for at least one nontrivial dead-time/recovery model.

---

## 13. Multimode extension: matrix-valued Fisher spectrum

If the source has `d` independently controllable temporal tangent components (e.g. wavelength/polarization/spatial channels), the source tangent space becomes

\[
L^2(\mathbb R;\mathbb C^d).
\]

A bounded positive translation-invariant contraction is then represented by an operator-valued/matrix multiplier

\[
\boxed{\mathbf G(\omega),\qquad
0\preceq\mathbf G(\omega)\preceq I_d.}
\]

The Fisher metric becomes

\[
F_{\rm out}[u,v]
=\frac{\Phi_0}{2\pi}
\int U(\omega)^\dagger
\mathbf G(\omega)
V(\omega)d\omega.
\]

This supplies the rigorous route to the operator-valued spectrum suggested informally before Paper 2 began.

The scalar Paper-1 spectrum is the `d=1` case.

---

## 14. Nonautonomous detector

Without time-translation covariance, `A_K` remains a positive contraction but need not be diagonal in frequency. The correct primitive object is then the full Fisher-retention operator.

One may write a two-frequency kernel `G(omega,omega')` **only if** additional regularity makes the operator kernel-representable. Do not assume every bounded operator has such a kernel.

Thus the hierarchy is:

\[
\text{general detector}
\to \mathcal A_K
\]

\[
\text{autonomous scalar temporal source}
\to G(\omega)
\]

\[
\text{autonomous multimode temporal source}
\to \mathbf G(\omega).
\]

---

## 15. Potential breakthrough significance

If novel in photodetection, this result would establish that:

1. a complete temporal Fisher transfer spectrum survives arbitrary detector memory and high flux;
2. independent events are not required for spectral completeness;
3. the spectrum is forced by time-translation symmetry and source tangent multiplicity;
4. universal local detector ordering remains pointwise in frequency;
5. accessible-record coarse graining obeys pointwise spectral data processing;
6. Paper 1 is an explicit solvable special case of a much larger channel theory.

This is materially more fundamental than adding dead time to the old delay kernel.

---

## 16. Open proof gates

1. Put the Poisson DQM score formula on a rigorous whole-line or increasing-window footing.
2. Prove covariance of the conditional-score operator under trajectory shifts without hidden measurability gaps.
3. State the translation-invariant multiplier theorem with a citable theorem-grade reference.
4. Prove the evenness/reality properties of `G` under the real-waveform formulation.
5. Establish Paper-1 recovery explicitly from the general conditional-score formula.
6. Determine conditions for continuity of `G`; the general theorem gives only an `L^infty` multiplier a.e.
7. Derive at least one genuinely history-dependent example analytically or semi-analytically.
8. Complete an adversarial novelty audit against statistical experiment theory, stationary-process FI, high-flux TCSPC/LiDAR, and hidden-Markov sensing.
