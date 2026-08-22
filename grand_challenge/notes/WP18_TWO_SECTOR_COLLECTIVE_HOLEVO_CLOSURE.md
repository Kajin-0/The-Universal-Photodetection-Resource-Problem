# WP18 — Two-sector collective Holevo closure of the random-time resource law

**Date:** 2026-08-21

## Status

**Collective-measurement gate passed exactly for the minimal two-sector model.**

WP17 proved the sharp operational mode budget for one fixed POVM and adaptive/separable measurement of independent event excitations, while leaving arbitrary entangled collective measurements across multiple mixed twirled copies open.

WP18 solves that loophole exactly for the smallest nontrivial random-time model: one occupied lower energy sector and one upper sector separated by one temporal harmonic.

For sector probabilities

`q_0=1-p`,

`q_1=p`, `0<p<1`,

the asymptotically attainable Holevo limit for simultaneous estimation of the cosine and sine amplitudes of the random-time mode yields the maximal isotropic source-normalized collective retention

`boxed: q_coll = min(p,1-p)`.

For the resource-relevant branch `p<=1/2`,

`boxed: q_coll=p=nbar`.

Thus arbitrary collective measurements can improve over separable readout, but **cannot exceed the WP17 energy budget** in this minimal model. In fact the collective optimum exactly saturates that budget for `p<=1/2`.

For a gap of `k` energy sectors rather than one,

`nbar=k p`,

and the same qubit estimation geometry gives

`q_coll<=p=nbar/k` for `p<=1/2`.

Equivalently, for target ordinary frequency `f_k=k/T`,

`boxed: Ebar^+ >= h f_k q_coll`.

This does not yet prove the full multimode collective area law. It is a strong positive result for the first hostile collective test.

---

## 1. Two-sector random-time local model

Take the periodic WP10 excitation

`|psi>=sqrt(1-p)|0>+sqrt(p)|1>`

on two participating energy sectors separated by `hbar omega0`.

At uniform random-time baseline the state is twirled to

`rho0=diag(1-p,p)`.

Define

`j=p(1-p)`.

For the cosine/sine random-time modulation parameters `(epsilon_c,epsilon_s)`, the first derivatives are

`D_c=(sqrt(j)/2) sigma_x`,

`D_s=(sqrt(j)/2) sigma_y`

up to the irrelevant sign convention of the sine parameter.

The SLDs are

`L_c=sqrt(j) sigma_x`,

`L_s=sqrt(j) sigma_y`,

so the SLD QFI matrix is

`boxed: J=j I_2`.

The latent source-label Fisher matrix is

`F_in=(1/2)I_2`.

Therefore the separately optimized scalar QFI retention of either quadrature is

`G_Q=2j=2p(1-p)`.

---

## 2. Direct Holevo optimization

Let

`r=1-2p`,

so

`rho0=(I+r sigma_z)/2`.

For unit weight matrix `W=I_2`, the Holevo bound minimizes

`Tr Re Z + ||Im Z||_1`

over Hermitian estimator operators `X_c,X_s` satisfying local unbiasedness.

The constraints are

`Tr[rho0 X_i]=0`,

`Tr[D_j X_i]=delta_ij`.

Every admissible pair can be written as

`X_c=(1/sqrt(j))sigma_x + z_c(sigma_z-rI)`,

`X_s=(1/sqrt(j))sigma_y + z_s(sigma_z-rI)`,

with real `z_c,z_s`.

For

`Z_ij=Tr[rho0 X_i X_j]`,

direct Pauli algebra gives

`Tr Re Z = 2/j + 4j(z_c^2+z_s^2)`.

The imaginary off-diagonal component is independent of the free longitudinal terms:

`Im Z_cs = r/j`,

so

`||Im Z||_1=2|r|/j`.

Therefore the Holevo objective is

`C_H(I)`

`=2/j + 4j(z_c^2+z_s^2) + 2|r|/j`.

It is minimized at

`z_c=z_s=0`.

Hence

`boxed: C_H(I)=2(1+|r|)/j`.

Equivalently,

`boxed: C_H(I)=2[1+|1-2p|]/[p(1-p)]`.

This is the exact asymptotic collective two-parameter precision bound.

---

## 3. Literature cross-check

The result is not a new generic Holevo calculation.

Two-parameter mixed-qubit Holevo bounds are established, including Jun Suzuki's explicit general formula for two-parameter qubit models and modern work on collective estimation of two transverse qubit rotations.

Conlon et al., *Nature Physics* **19**, 351–357 (2023), analyze a diagonal decohered qubit with two small orthogonal rotations and obtain

`v_x+v_y >= (4-2 epsilon)/(1-epsilon)^2`

for asymptotically collective measurements.

Their baseline Bloch length is `r=1-epsilon` and their SLD QFI per parameter is `j=(1-epsilon)^2`, so their formula is precisely

`2(1+r)/j`,

the `r>=0` branch of the expression above after accounting for parameter normalization.

Thus WP18's contribution is the **mapping to the random-time distribution Fourier-mode problem and its energy-resource implication**, not the generic mixed-qubit Holevo mathematics.

---

## 4. Asymptotically attainable isotropic precision

The local model is rotationally symmetric in the cosine/sine plane. The Holevo optimum can therefore be taken isotropic:

`Var(epsilon_c)=Var(epsilon_s)`.

For `N` independently prepared twirled excitations and asymptotically optimal collective measurement,

`N[Var(epsilon_c)+Var(epsilon_s)] -> C_H(I)`.

Thus each variance approaches

`Var(epsilon_c)=Var(epsilon_s)`

`~ (1+|r|)/(jN)`.

It is convenient to express the same precision as a Fisher-equivalent isotropic classical information per copy,

`F_coll = f_coll I_2`,

with

`f_coll=j/(1+|r|)`.

Relative to the source Fisher block `(1/2)I_2`, the source-normalized retention of each quadrature is

`q_coll=2 f_coll`.

Therefore

`q_coll=2j/(1+|r|)`

`=2p(1-p)/[1+|1-2p|]`.

Since

`1+|1-2p|=2 max(p,1-p)`,

we obtain the compact exact result

`boxed: q_coll=min(p,1-p)`.

---

## 5. Resource consequence

For the lower-excitation branch

`0<p<=1/2`,

we have

`q_coll=p`.

But for the two-sector gap-one model

`nbar=p`.

Hence

`boxed: q_coll=nbar`, `p<=1/2`.

Thus the collective optimum reaches—but does not cross—the WP17 one-mode resource ceiling.

For `p>1/2`,

`q_coll=1-p<nbar=p`,

so the mean-excitation bound is loose rather than violated.

### General gap `k`

If the occupied sectors are `0` and `k`, the same two-dimensional density matrix and estimation geometry apply to temporal mode `k`, while

`nbar=k p`.

For `p<=1/2`,

`q_coll=p=nbar/k`.

With

`f_k=k/T`,

`Ebar^+=h f0 nbar=h f_k p`,

we obtain

`boxed: Ebar^+ = h f_k q_coll`

at the collective optimum for the lower-excitation branch.

This is an exact Planck-scale mode-resource equality in the minimal collective model.

---

## 6. Collective advantage versus separable readout

WP17 plus the qubit Gill–Massar/Nagaoka tradeoff gives the optimal single-copy/separable isotropic retention

`q_sep=j=p(1-p)`.

The collective optimum is

`q_coll=min(p,1-p)`.

Therefore the collective gain factor is

`q_coll/q_sep = 1/max(p,1-p)`.

It ranges from approximately `1` in the rare-upper-sector sharpness limit `p->0` to a maximum factor

`boxed: 2`

at `p=1/2`.

At `p=1/2`, the SLD commutator expectation vanishes and collective estimation reaches the full per-quadrature QFI retention:

`q_coll=G_Q=1/2`.

For `p->0`,

`q_coll~p`,

while

`G_Q~2p`.

Thus even asymptotically collective readout retains only about half of the separately optimized SLD envelope in the resource-sharp low-energy limit.

This is exactly the regime relevant to sharpness of the WP17 mean-energy coefficient.

---

## 7. Interpretation

WP18 clarifies the hierarchy of three quantities for the minimal model:

1. **separately optimized scalar QFI** per quadrature:

   `G_Q=2p(1-p)`;

2. **best separable simultaneous retention**:

   `q_sep=p(1-p)`;

3. **best asymptotically collective simultaneous retention**:

   `q_coll=min(p,1-p)`.

For `p<=1/2`,

`q_sep <= q_coll = nbar <= G_Q`,

with the final inequality becoming approximately a factor two in the `p->0` sharpness limit.

Collective measurements recover part of the incompatibility loss but do not create temporal information beyond the mean-excitation resource in the two-sector model.

---

## 8. What is and is not closed

### Closed

For one random-time mode supported by two energy sectors, arbitrary asymptotic collective measurement cannot violate the energy-normalized full-quadrature bound.

The result is exact and Holevo-optimal.

### Still open

WP18 does **not** prove

`sum_{k>=1} R_coll(k) <= nbar`

for a general multilevel excitation under one collective measurement across many copies.

The multimode model has nontrivial cross-mode incompatibility and a much larger tangent space. Collective measurements may redistribute information among modes in ways not visible in the two-sector reduction.

The next theorem target is therefore a **multimode collective Holevo/resource inequality**, not another two-level calculation.

---

## 9. Next routes

1. Test three-sector states numerically with finite-copy collective POVM optimization or Holevo SDP for modes `k=1,2`.
2. Search for a direct Holevo-dual inequality weighted by total generator excitation that could imply

   `sum_k R_coll(k)<=nbar`

   asymptotically.
3. Investigate whether the random-time tangent model is D-invariant or decomposes into D-invariant blocks in a way that makes the Holevo functional analytically summable.
4. Use quantum local asymptotic normality to identify the Gaussian limit of the energy-gap coherences and ask whether the mean-excitation budget becomes a canonical heterodyne-type information constraint.
5. Keep generic qubit Holevo theory explicitly credited; novelty, if any, lies in the temporal random-distribution/resource theorem.

## Decision

The first collective-measurement hostile test **passes**.

Collective entangled readout gives a real advantage over separable measurement, but in the minimal two-sector random-time model its exact Holevo optimum still satisfies—and for low upper-sector occupation saturates—the Planck-scale energy-information resource coefficient implied by WP17.