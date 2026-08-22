# WP11 — WP10 factor audit, QFIM compatibility, and targeted prior-art check

**Date:** 2026-08-21

## Status

**WP10 survives the first independent algebra/prior-art audit.**

The pure-state cosine/sine QFI constants were independently rederived and numerically checked in finite dimensions. The sharp positive-mode sum constant `2` and two-sided constant `4` are correct. A multiparameter caveat was identified: cosine and sine SLDs are generally not jointly compatible, so the QFIM is an upper-bound matrix and should not be described as simultaneously attainable by one measurement without an additional compatibility condition.

Targeted searches found the expected neighboring literature on `U(1)` modes of asymmetry, phase diffusion, random-unitary channels, and Fisher/asymmetry monotones, but did not locate the exact WP10 random-time mode-retention formula or summed mean-energy theorem.

Priority remains uncertified.

---

## 1. Independent QFI calculation

For a pure periodic excitation

`|psi>=sum_n c_n|n>`, `q_n=|c_n|^2`,

with random event-time modulation in mode `k`, the uniformly twirled baseline is

`rho0=sum_n q_n|n><n|`

in the nondegenerate notation.

The cosine derivative has pairwise matrix elements

`D_c[n+k,n]=(1/2)c_{n+k}c_n^*`,

and the sine derivative has the same magnitude with relative phase `pi/2`.

Using the SLD metric

`F_ab=2 sum_{i,j} Re[D_a,ij D_b,ji]/(q_i+q_j)`,

one unordered pair `(n,n+k)` contributes

`q_n q_{n+k}/(q_n+q_{n+k})`

to each diagonal quadrature entry. Therefore

`boxed: F_cc^(k)=F_ss^(k)=sum_n q_nq_{n+k}/(q_n+q_{n+k})`,

`boxed: F_cs^(k)=0`.

The latent classical event-time label has

`F_in=(1/2)I_2`,

so

`boxed: G_Q(k)=2 sum_n q_nq_{n+k}/(q_n+q_{n+k})`.

Direct finite-dimensional numerical evaluation of the SLD formula for random complex states reproduced these expressions to floating-point precision.

---

## 2. Source-FI normalization audit

For

`p_eps(t)=(1/T)[1+eps cos(k omega0 t)]`,

at `eps=0`,

`partial_eps log p = cos(k omega0 t)`.

Thus

`F_in = (1/T)int_0^T cos^2(k omega0 t)dt =1/2`.

The same holds for the sine quadrature and the cross term vanishes.

Therefore the factor of `2` converting QFI to source-normalized retention is correct.

---

## 3. Mode-sum constant audit

For positive modes,

`sum_{k>=1}G_Q(k)`

`=2 sum_{0<=n<m} q_nq_m/(q_n+q_m)`.

Since

`q_nq_m/(q_n+q_m)<=q_m`,

`sum_{k>=1}G_Q(k)<=2 sum_m m q_m=2 nbar`.

The two-sector sequence

`q_0=1-epsilon`, `q_1=epsilon`

gives

`G_Q(1)=2epsilon(1-epsilon)`, `nbar=epsilon`,

hence

`G_Q(1)/(2nbar)=1-epsilon ->1`.

Thus the positive-side constant `2` is sharp as a supremum. Counting the even negative-frequency partner gives sharp two-sided constant `4`.

---

## 4. Per-mode `G_Q<=1` audit

Using

`2ab/(a+b)<=(a+b)/2`,

`G_Q(k)`

`<= (1/2)sum_n(q_n+q_{n+k})`

`=1-(1/2)sum_{j=0}^{k-1}q_j`

`<=1`.

This agrees with data processing from the latent classical event-time label into the quantum excitation.

---

## 5. Multiparameter compatibility caveat

Although

`F_Q^(k)=S_k I_2`

for cosine/sine quadratures, the corresponding SLDs are generally **not weakly commuting**:

`Tr[rho0 [L_c,L_s]]` need not vanish.

Finite-dimensional numerical tests give nonzero imaginary commutator expectation for generic population profiles.

Therefore:

- the SLD-QFIM is a valid matrix upper bound on every classical Fisher matrix;
- each scalar quadrature bound is individually valid;
- a single fixed measurement need not simultaneously attain both QFI diagonal entries;
- WP10 should not claim simultaneous attainability of the full two-parameter SLD bound absent an additional Holevo/compatibility analysis.

This caveat does **not** weaken the mode-budget theorem because every final detector's classical FI for each quadrature is bounded by the same `G_Q(k)`, and the summed upper bound is derived before any attainability claim.

For an autonomous/covariant final detector, phase symmetry would normally force equal classical retention for the two quadratures; nevertheless the quantum upper bound remains the same.

---

## 6. Mixed-state audit

For arbitrary mixed `sigma`, choose a purification with the time generator acting only on the system. The energy-sector probabilities of the purification are

`q_n=Tr[P_n sigma]`.

The pure-state calculation on the purification gives exactly the WP10 population expression. Partial trace is a parameter-independent CPTP map, so the physical QFIM is bounded in PSD order by the purification QFIM.

Hence

`G_Q^mixed(k) <= 2 sum_n q_nq_{n+k}/(q_n+q_{n+k})`

and all sum/energy bounds survive degeneracy and mixedness.

This route avoids needing a detailed operator inequality for arbitrary coherence blocks inside degenerate energy sectors.

---

## 7. External reference / arbitrary detector audit

Appending a parameter-independent apparatus state, even one with strong time-translation asymmetry, leaves the QFI with respect to the random-time modulation parameter unchanged:

`F_Q[rho_eps tensor sigma_A]=F_Q[rho_eps]`.

Any parameter-independent joint signal-apparatus channel is QFI monotone. Therefore an external clock can help implement an optimal measurement but **cannot exceed the WP10 encoded-state QFI**.

This is the crucial distinction from WP09's deterministic global-shift counterexample.

---

## 8. Prior-art audit

### Established and directly relevant

Marvian and Spekkens, *Phys. Rev. A* 90, 062110 (2014), develop `U(1)` modes of asymmetry. For a pure state they explicitly quantify a mode using sums such as

`sum_n |psi_{n+k}||psi_n|`,

and show mode labels cannot be mixed by covariant processing. Their framework is a direct conceptual ancestor of the energy-gap/Fourier decomposition used in WP10.

Later asymmetry/coherence work constructs mode-resolved norms, Hellinger/skew-information quantities, and QFI-type asymmetry monotones.

Standard SLD-QFI formulas of course contain denominators `p_i+p_j`, and harmonic-mean structures also appear in local quantum Fisher information and monotone-metric literature.

### Not located in targeted search

Searches across:

- modes of asymmetry;
- phase-distribution metrology;
- phase diffusion;
- random-unitary noise;
- synchronization FI/QFI;
- mean-photon-number metrology bounds;

have not located the exact random-time encoding formula

`G_Q(k)=2 sum_n q_nq_{n+k}/(q_n+q_{n+k})`

interpreted as maximal Fisher retention of a Fourier mode of a latent event-time distribution.

Nor was the sharp sum rule

`sum_{k>=1}G_Q(k)<=2nbar`

or inverse bandwidth law

`Ebar >= (h/2)Bq`

located in this form.

This absence is **not priority certification**. The result could exist under another language such as phase-covariant randomization, group-parameter distribution estimation, or monotone quantum metrics.

---

## 9. Current assessment

No factor-of-two error or immediate prior-art preemption has been found.

WP10 is stronger than WP08 in detector scope because it bounds the parameter information in the premeasurement quantum state itself. The main remaining risks are:

1. an equivalent theorem hidden in group-distribution/phase-noise estimation literature;
2. failure or nonphysicality of the continuous-spectrum limit;
3. mismatch between the abstract independent quantum-marked Poisson model and a genuine overlapping bosonic optical field;
4. overinterpreting the SLD-QFIM as jointly attainable.

Next gate: controlled periodic-to-continuum limit and a deeper search in group-distribution/random-unitary-channel estimation.
