# WP10 — Measurement-independent quantum random-time mode budget

**Date:** 2026-08-21

## Status

**Strong theorem candidate; currently the highest-ceiling result in the grand-challenge branch.**

WP06--WP08 bound a chosen covariant timestamp layer and then arbitrary downstream classical memory. WP09 showed why a source-only mean-energy bound cannot hold for arbitrary local estimation of a deterministic time shift if a detector is supplied with a free temporal phase reference.

WP10 changes the encoded parameter. Instead of estimating a deterministic global shift, it asks how much information about a **Fourier mode of a random event-time distribution** can be encoded in the quantum excitation itself before any detector is chosen.

For a periodic positive-energy model, the maximal quantum Fisher retention of each temporal mode is computable exactly for pure states, bounded for mixed states by the same population expression, and obeys a sharp mean-excitation mode-sum law. Because the bound is imposed at the quantum-state level, **every parameter-independent quantum detector, coherent memory, adaptive internal processing, and final classical measurement is downstream of it.**

This avoids the external-clock loophole of WP09: an apparatus reference may help attain the QFI, but cannot increase QFI already encoded in the random-time mixture.

---

## 1. Periodic positive-energy model

Let time be periodic with period `T` and fundamental angular frequency

`omega0 = 2*pi/T`.

Let the excitation Hamiltonian, after subtracting an irrelevant lower spectral edge, have nonnegative integer-spaced sectors

`H = hbar*omega0*N`,

`N = sum_{n>=0} n P_n`,

where `P_n` may have arbitrary degeneracy.

Start with a quantum excitation state `sigma`. A latent event center `t in [0,T)` shifts the excitation by

`U_t = exp(-i omega0 N t)`.

The conditional state is

`sigma_t = U_t sigma U_t^*`.

The baseline latent event-time distribution is uniform. Introduce weak real Fourier modulation in mode `k>=1`:

`p_{eps_c,eps_s}(t)`

`= (1/T)[1 + eps_c cos(k omega0 t) + eps_s sin(k omega0 t)]`.

The encoded quantum state is

`rho_{eps_c,eps_s}`

`= int_0^T p_{eps_c,eps_s}(t) sigma_t dt`.

At the baseline,

`rho0 = sum_n P_n sigma P_n`,

the `U(1)`-twirled state.

The latent classical source-label Fisher matrix is

`F_in(k) = (1/2) I_2`

for the cosine/sine quadratures.

This is the quantum analogue of asking how well a detector can retain one temporal waveform mode of a random event-time distribution.

---

## 2. Exact pure-state calculation

First let

`|psi> = sum_{n>=0} |psi_n>`,

where

`|psi_n> = P_n|psi>`,

and define

`q_n = ||psi_n||^2`,

`sum_n q_n=1`.

For each `q_n>0`, let

`|phi_n> = |psi_n>/sqrt(q_n)`.

The vectors `phi_n` lie in orthogonal energy sectors. The uniformly twirled baseline is

`rho0 = sum_n q_n |phi_n><phi_n|`.

The cosine derivative at zero modulation is

`D_c^(k) := partial_{eps_c} rho|_0`

`= (1/2) sum_{n>=0}`

`[ |psi_{n+k}><psi_n| + |psi_n><psi_{n+k}| ]`.

The sine derivative is

`D_s^(k) := partial_{eps_s} rho|_0`

`= (1/(2i)) sum_{n>=0}`

`[ |psi_n><psi_{n+k}| - |psi_{n+k}><psi_n| ]`,

up to an irrelevant overall sign convention.

Thus each temporal Fourier mode couples only energy sectors separated by the corresponding gap `k hbar omega0`. This is exactly the `U(1)` mode-of-asymmetry decomposition; the mode decomposition itself is prior art.

---

## 3. Exact QFI matrix for one mode

For a density matrix with eigenvalues `lambda_i`, the SLD quantum Fisher metric is

`F_Q(D,E)=2 sum_{i,j:lambda_i+lambda_j>0}`

`Re[D_ij E_ji]/(lambda_i+lambda_j)`.

For each unordered pair `(n,n+k)`, the derivative matrix element magnitude is

`|<phi_n|D_c^(k)|phi_{n+k}>|`

`= (1/2) sqrt(q_n q_{n+k})`,

and the sine derivative has the same magnitude with a relative phase of `pi/2`.

Therefore

`F_Q,cc^(k)=F_Q,ss^(k)`

`= sum_{n>=0} q_n q_{n+k}/(q_n+q_{n+k})`,

with the convention that zero-over-zero terms vanish, while

`F_Q,cs^(k)=0`.

Hence the QFI matrix is isotropic in the two real quadratures:

`boxed: F_Q^(k) = S_k I_2`,

where

`S_k = sum_{n>=0} q_n q_{n+k}/(q_n+q_{n+k})`.

Normalizing by the source-label FI `(1/2)I_2`, define the maximal quantum temporal-mode retention

`boxed: G_Q(k) = 2 S_k`

`= 2 sum_{n>=0} q_n q_{n+k}/(q_n+q_{n+k})`.

This formula is exact for a pure excitation, including arbitrary degeneracy of the energy sectors.

---

## 4. Data-processing normalization: `0 <= G_Q(k) <= 1`

The inequality `G_Q(k)<=1` is required by the fact that encoding the classical event-time label into a quantum state is a channel. It also follows directly.

For `a,b>=0`,

`2ab/(a+b) <= (a+b)/2`.

Thus

`G_Q(k)`

`<= (1/2) sum_n [q_n+q_{n+k}]`

`= 1 - (1/2) sum_{j=0}^{k-1}q_j`

`<=1`.

Therefore

`boxed: 0 <= G_Q(k) <=1`.

High temporal harmonics cannot be encoded with greater Fisher information than existed in the latent classical event-time distribution.

---

## 5. Sharp mean-excitation mode-sum law

Sum over all positive temporal modes:

`sum_{k>=1}G_Q(k)`

`=2 sum_{0<=n<m} q_n q_m/(q_n+q_m)`.

For every `n<m`,

`q_n q_m/(q_n+q_m) <= q_m`.

Therefore

`sum_{k>=1}G_Q(k)`

`<=2 sum_m [number of n<m] q_m`

`=2 sum_m m q_m`.

Define the mean excitation number

`nbar = sum_m m q_m`.

Then

`boxed: sum_{k>=1} G_Q(k) <= 2 nbar`.

Because the physical temporal spectrum is even, assigning the same retention to the negative-frequency partner gives

`boxed: sum_{k != 0}G_Q(k) <= 4 nbar`.

In energy units,

`Ebar = hbar omega0 nbar`,

so

`boxed: omega0 sum_{k !=0}G_Q(k) <= 4 Ebar/hbar`.

This is the periodic **measurement-independent quantum temporal Fisher mode-area law**.

---

## 6. Sharpness of the constant

Take the two-sector family

`q_0=1-epsilon`,

`q_1=epsilon`,

with all other populations zero.

Then

`G_Q(1)=2 epsilon(1-epsilon)`,

all higher positive modes vanish, and

`nbar=epsilon`.

Hence

`[sum_{k>=1}G_Q(k)]/(2 nbar)=1-epsilon ->1`

as `epsilon->0`.

Thus the positive-mode constant `2` is sharp as a supremum. Equivalently the two-sided constant `4` is sharp.

The optimum is approached by an arbitrarily weak occupation of the first excited sector rather than by a broad high-energy distribution.

---

## 7. Flat-band inverse law

Suppose the first `K` positive temporal harmonics all satisfy

`G_Q(k) >= q`, `k=1,...,K`.

Then

`Kq <= sum_{k>=1}G_Q(k) <=2nbar`,

so

`boxed: nbar >= Kq/2`.

The ordinary fundamental frequency is

`f0=1/T`,

and a band through harmonic `K` has

`B=K/T=K f0`.

Since

`Ebar = h f0 nbar`,

we obtain

`boxed: Ebar >= (h/2) B q`.

This is the periodic arbitrary-measurement counterpart of the stricter covariant-timestamp result from WP06/WP07,

`E^+ >= h B q`.

The factor-of-two gap is a concrete target for interpretation: arbitrary phase-sensitive quantum readout can in principle retain more random-time waveform information per unit mean excitation than a covariant continuous timestamp readout, but no measurement can beat the WP10 bound.

---

## 8. Mixed states: purification bound

Let `sigma` be an arbitrary mixed excitation state with energy-sector probabilities

`q_n = Tr[P_n sigma]`.

Choose a purification

`|Psi> in H tensor R`

such that

`Tr_R |Psi><Psi| = sigma`,

and let the time shift act only on `H`.

The energy-sector weights of the purification are still exactly `q_n`.

Encode the same random event-time distribution into the purified state. By the pure-state calculation, its mode QFI retention is

`G_Q^pur(k)=2 sum_n q_nq_{n+k}/(q_n+q_{n+k})`.

The physical encoded state is obtained by the parameter-independent channel `Tr_R`. Quantum Fisher information is monotone under parameter-independent CPTP maps. Therefore the mixed-state encoded QFI matrix satisfies

`F_Q^sigma(k) <= F_Q^pur(k)`

in positive-semidefinite matrix order, and in particular

`boxed: G_Q^sigma(k) <= 2 sum_n q_nq_{n+k}/(q_n+q_{n+k})`.

Consequently **all mode-sum and mean-energy bounds above hold unchanged for arbitrary mixed states**.

The population formula is generally an upper bound for mixed states, and is exact for pure states.

---

## 9. Arbitrary quantum detector and coherent memory inheritance

The parameter `eps_c` or `eps_s` is encoded in the quantum state `rho_eps` **before a detector is chosen**.

Let an arbitrary apparatus be initialized in any parameter-independent state `sigma_A`, including a state carrying an external phase/time reference. Let any parameter-independent joint quantum channel act on signal plus apparatus, with arbitrary coherent memory, feedback internal to the channel, hidden degrees of freedom, amplification, saturation, or entangling dynamics. Finally perform any measurement and retain any classical record `Y`.

Appending the parameter-independent apparatus state does not change the signal QFI. CPTP evolution cannot increase QFI, and classical measurement cannot exceed QFI. Therefore for each temporal quadrature,

`F_Y^(k) <= F_Q^sigma(k)`.

Relative to the latent source-label FI `(1/2)`,

`boxed: G_Y(k) <= G_Q^sigma(k)`.

Combining with the population bound,

`boxed: G_Y(k) <= 2 sum_n q_nq_{n+k}/(q_n+q_{n+k})`.

And summing,

`boxed: sum_{k>=1}G_Y(k) <=2nbar`,

`boxed: sum_{k!=0}G_Y(k) <=4nbar`.

This is stronger in detector scope than WP08: **no factorization into a primary timestamp followed by classical memory is required.** Any subsequent quantum detector processing is downstream of the encoded-state QFI.

### Why the WP09 external-clock counterexample does not apply

WP09 concerns estimation of a deterministic global time shift of a coherent quantum state. At fixed mean energy, a sparse arbitrarily high-energy tail can create unbounded shift QFI, and an external phase reference can access it.

WP10 instead estimates the amplitude of a Fourier component in the **probability distribution of a random latent event time**. Uniform randomization at the baseline twirls away inter-energy phase coherence. A rare high-energy component contributes only through the harmonic-mean population overlap with another occupied energy sector. The total mode budget is therefore controlled linearly by the mean excitation number.

An external phase reference may help attain the already-encoded QFI, but cannot create additional information about the random-time distribution parameter.

This distinction is central and should be emphasized in any future manuscript.

---

## 10. Independent multi-event / Poisson extension

For a mathematically clean independent quantum-marked Poisson model, suppose each latent event carries an independent copy of the excitation state encoded by the same periodic event-time law, and the number of events in one period is Poisson with mean `mu` independent of the zero-mean modulation amplitudes.

Represent the pre-detector state as the block-diagonal direct sum

`Rho_eps = directsum_{N>=0} Pois_mu(N) rho_eps^{tensor N}`.

Because the Poisson weights do not depend on `eps`, QFI is additive within each tensor-power block and averages across orthogonal `N` blocks:

`F_Q[Rho_eps] = mu F_Q[rho_eps]`.

The latent classical Poisson event-time experiment has FI `mu/2` per cosine/sine quadrature. Hence the source-normalized retention is **the same `G_Q(k)` as for one event**.

Any joint quantum detector acting coherently on all events and arbitrary internal memory remains downstream of this QFI.

This establishes the mode-budget theorem for an independent quantum-marked Poisson stream at arbitrary mean count, provided the excitation marks are represented as independent tensor factors/direct-sum number sectors.

Do not yet identify this abstract marked-Poisson model with every overlapping indistinguishable-boson field state. A full second-quantized coherent-field formulation is a separate gate.

---

## 11. Continuous-spectrum candidate

Let a pure positive-frequency excitation have normalized spectral probability density `q(w)` on `[0,infinity)` with finite first moment

`wbar = int_0^infinity w q(w)dw`.

The periodic formula suggests, for positive modulation angular frequency `nu`,

`G_Q(nu)`

`=2 int_0^infinity`

`q(w)q(w+nu)/[q(w)+q(w+nu)] dw`.

If this continuum expression is justified as a large-period limit, then Tonelli plus

`q(w)q(w')/[q(w)+q(w')] <= q(w')`

would give

`int_0^infinity G_Q(nu)dnu <=2 wbar`,

and therefore

`boxed: int_R G_Q(nu)dnu <=4 wbar = 4 Ebar^+/hbar`.

This would be the continuous measurement-independent counterpart of WP07's covariant timestamp law

`int G_timestamp <=2E^+/hbar`.

### Current mathematical obstruction

A perfectly uniform random time on the infinite line does not produce a normal trace-class dephased state for an absolutely continuous energy spectrum. Therefore the continuous formula should **not** yet be stated as a theorem by simply writing delta-normalized energy eigenstates.

Safe route:

1. prove the compact periodic theorem exactly;
2. formulate a sequence of periodic boxes with spacing `omega0->0` and controlled probability measures;
3. prove convergence of the mode-retention Riemann sums under finite first moment / regularity assumptions.

Until that limit is written rigorously, the continuous area law is a conjectural continuum limit, not a theorem.

---

## 12. Prior-art boundary

### Direct conceptual collision: modes of asymmetry

Marvian and Spekkens, *Phys. Rev. A* **90**, 062110 (2014), develop the harmonic-analysis decomposition of states, measurements, and channels into `U(1)`/time-translation modes of asymmetry. They prove that covariant operations cannot move information between distinct mode labels and construct mode-specific asymmetry monotones.

Therefore **do not claim novelty** for:

- decomposing temporal information by energy-gap/Fourier mode;
- identifying mode `k` with the `k`-energy-gap block;
- preservation/noncreation of mode labels under time-covariant processing.

### What targeted searches have not yet located

Searches through quantum metrology, phase diffusion, synchronization, and asymmetry literature have not yet located the exact random-time encoding result

`G_Q(k)=2 sum_n q_nq_{n+k}/(q_n+q_{n+k})`,

nor the summed mean-energy theorem

`sum_{k>=1}G_Q(k)<=2 nbar`,

nor the inverse law

`Ebar >= (h/2)Bq`

stated as a maximal **random temporal-distribution Fisher-retention budget**.

The harmonic-mean denominator itself is of course standard in SLD-QFI formulas and related monotone quantum metrics. Novelty cannot be assigned to that algebraic structure alone.

Priority is **not certified**.

---

## 13. Significance if the theorem survives

WP10 is potentially more fundamental than WP06--WP08 because the bound is imposed **before any measurement or detector architecture is selected**.

It says, in the rigorous periodic model:

> A positive-energy quantum excitation with mean excitation number `nbar` can encode only a finite total amount of Fisher information about all Fourier modes of a random event-time distribution; the two-sided source-normalized mode budget is at most `4 nbar`, and no quantum detector with arbitrary coherent memory can increase it.

This is a quantum information-transfer statement, not a property of a particular timestamp POVM.

If the controlled continuous-spectrum limit exists, the candidate universal form becomes

`int G_Q(nu)dnu <=4Ebar^+/hbar`,

with a corresponding flat-band inverse law

`Ebar^+ >= (h/2)Bq`.

That would provide a genuinely measurement-independent Planck-scale resource law for temporal waveform information.

It remains premature to call this Nobel-level; the continuum limit, full optical-field interpretation, and prior-art audit are decisive.

---

## 14. Immediate hostile gates

1. **Independent derivation audit:** rederive every factor of two in the cosine/sine QFI matrix and source-FI normalization.
2. **Mixed-state rigor:** state QFIM monotonicity under purification carefully, including energy degeneracy and zero-population sectors.
3. **Multiparameter caution:** distinguish SLD-QFI matrix upper bounds from simultaneous attainability of cosine and sine quadratures.
4. **Deep collision search:** search asymmetry/phase-diffusion/random-unitary-channel literature for the exact mode-QFI formula or mode-sum mean-energy bound.
5. **Periodic-to-continuum limit:** build a rigorous Riemann-sum theorem under finite first moment and appropriate density regularity.
6. **Second-quantized optical field:** determine whether the independent quantum-marked Poisson extension maps exactly to physically relevant photonic states or whether bosonic overlap modifies the bound.
7. **Factor-of-two interpretation:** determine whether the gap between arbitrary-measurement `4E/hbar` area and covariant-timestamp `2E/hbar` area is fundamental and whether it is saturable in a broadband limit.
8. **Operational equality/sharpness:** identify detector/measurement sequences that approach the sharp mode-sum constant, not merely state distributions.
9. Only after gates 1--8 decide whether WP10 is manuscript-ready.
