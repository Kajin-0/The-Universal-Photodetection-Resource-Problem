# WP04 — Optical sideband survival-to-synthesis crossover

**Date:** 2026-08-23

**Status:** analytical practical bridge complete for (i) an exact seeded two-frequency-bin crossover and (ii) ordinary weak phase modulation at an empty-sideband boundary. The externally driven phase-modulator example tests the rank-boundary curvature law, not the autonomous dual-action theorem. Autonomous coupling interpretation is deferred to WP05.

## Purpose

The PRXQ flagship distinguishes two local resource regimes:

1. finite affine physical radius -> information is backed by pre-existing spectral survival;
2. rank-changing zero radius -> baseline-empty population must appear at second order and its positive curvature bounds information.

The goal here is to make that transition visible in ordinary optical sideband physics without treating “zero sideband power” as a loose analogy. The model must reproduce the actual support/positivity transition of the state.

---

# Part I — exact seeded two-frequency-bin crossover

## 1. Minimal frequency-bin state

Use a carrier bin `|c>` and an upper sideband bin `|s>` separated by angular frequency `Omega`.

Take a stationary baseline density operator

`rho_p = (1-p)|c><c| + p |s><s|`,

with

`0 <= p < 1/2`.

The sideband seed `p` is an ordinary pre-existing spectral population. For `p>0`, both bins belong to the support. At `p=0`, the sideband is baseline empty and becomes a kernel direction.

Let a calibrated lossless two-mode frequency converter apply the small complex mixing

`U(x,y)=exp{kappa[(x-iy)|s><c|-(x+iy)|c><s|]}`,

where `x,y` are dimensionless peak control quadratures and `kappa` converts them to a mixing angle. Define

`r=sqrt(x^2+y^2)`.

The exact output state is

`rho_p(x,y)=U(x,y) rho_p U(x,y)^dagger`.

This is standard SU(2) mode mixing (the same mathematics as a beam splitter or ideal two-mode frequency converter).

## 2. Exact sideband population

Direct two-level rotation gives

**`P_s(p;r)=p+(1-2p) sin^2(kappa r)`.**

Therefore near the origin

`P_s=p+(1-2p)kappa^2(x^2+y^2)+O(r^4)`.

At finite seed `p>0`, modulation mostly redistributes pre-existing spectral population/coherence within the supported two-bin state.

At `p=0`,

`P_s(0;r)=sin^2(kappa r)=kappa^2(x^2+y^2)+O(r^4)`,

so the sideband population is generated only at second order.

## 3. Linear tangent and exact affine radius

The first-order density matrix is

`rho_lin = [[1-p, kappa(1-2p)(x+iy)], [kappa(1-2p)(x-iy), p]]`

up to the harmless sign convention for the sine quadrature.

Its determinant is

`p(1-p)-kappa^2(1-2p)^2(x^2+y^2)`.

Hence the exact linear physical tangent radius is

**`R_lin^2 = p(1-p)/[kappa^2(1-2p)^2]`.**

Consequences:

- every `p>0` has a nonzero affine disk;
- `R_lin ->0` as `p->0+`;
- the exact nonlinear unitary family remains physical at `p=0` even though its linearized affine disk collapses.

This is precisely the support transition required by the flagship taxonomy.

## 4. Finite-radius survival bound in directly measured quantities

The complex positive-gap tangent is

`A = 2 kappa(1-2p)|s><c|`.

The pre-existing upper-endpoint population is simply

`U=p`.

The flagship finite-radius survival theorem therefore gives

**`(R_lin^2/4) Tr F <= p`.**

Substituting the exact radius gives the equivalent Fisher ceiling

**`Tr F <= 4 kappa^2(1-2p)^2/(1-p)`.**

No abstract spectral-tail reconstruction is needed in this two-bin realization: `p` is the directly measured sideband population and `R_lin` is fixed by `p` and the calibrated mixing coefficient `kappa`.

## 5. Boundary limit and exact synthesis curvature

At `p=0`, the sideband is baseline empty and

`P_s(x,y)=kappa^2(x^2+y^2)+O(r^4)`.

With

`Delta=partial_x^2+partial_y^2`,

**`Delta P_s(0)=4 kappa^2`.**

The one-sided rank-boundary theorem gives

**`Tr F <= Delta P_s(0)=4 kappa^2`.**

The survival ceiling approaches exactly the same number:

**`lim_(p->0+) 4p/R_lin^2 = 4 kappa^2 = Delta P_s(0)`.**

Equivalently,

`p/R_lin^2 -> kappa^2`.

This is the central practical crossover result:

> as the pre-seeded sideband population tends to zero, the finite-radius survival resource vanishes together with the affine radius, but their ratio approaches the second-order sideband-population curvature that takes over at the rank boundary.

The resource description changes order while the information ceiling has a continuous limit.

## 6. Boundary equality is attainable

At `p=0`, the state is pure and, to first order,

`|psi(x,y)> = |c> + kappa(x-iy)|s> + O(r^2)`

(up to convention).

Use the four-outcome equatorial qubit POVM

`E_(+x)=1/2 |+x><+x|`,

`E_(-x)=1/2 |-x><-x|`,

`E_(+y)=1/2 |+y><+y|`,

`E_(-y)=1/2 |-y><-y|`,

where

`|+/-x>=(|c> +/- |s>)/sqrt(2)`

and

`|+/-y>=(|c> +/- i|s>)/sqrt(2)`.

At the baseline every outcome has probability `1/4`. Direct differentiation gives

`F_xx=2 kappa^2`,

`F_yy=2 kappa^2`,

`F_xy=0`,

so

**`Tr F=4 kappa^2=Delta P_s(0)`.**

Thus the one-sided curvature law is exactly saturated by a fixed common-record measurement.

A practical implementation is a calibrated two-mode interferometric/frequency-bin analyzer followed by photon counting.

---

# Part II — ordinary phase modulation gives a bilateral boundary saturation example

## 7. Standard single-carrier phase modulation

Start with a single-frequency photon in carrier bin `|0>` and apply an ideal phase modulation

`exp{i[x cos(Omega t)+y sin(Omega t)]}`.

Let

`beta=sqrt(x^2+y^2)`.

For weak modulation the first upper/lower sideband amplitudes are linear in `x,y`, while the powers are quadratic. Independently of phase convention,

**`P_+(x,y)=(x^2+y^2)/4 + O(beta^4)`,**

**`P_-(x,y)=(x^2+y^2)/4 + O(beta^4)`.**

Therefore both first sidebands are baseline empty and

**`Delta P_+(0)=Delta P_-(0)=1`.**

This is ordinary sideband generation, but now expressed in exactly the second-order population language required by the rank-boundary theorem.

## 8. Fisher information of the two modulation quadratures

The local derivative states can be chosen as two orthogonal tangent vectors, each of norm squared `1/2` and orthogonal to the carrier. The pure-state SLD-QFI matrix is therefore

`H_xx=2`,

`H_yy=2`,

`H_xy=0`,

so

**`Tr H=4`.**

The tangent inner product is real, so the two-parameter pure-state compatibility obstruction vanishes at the baseline.

A fixed three-outcome real interferometric basis can attain the same classical Fisher matrix. Define normalized tangent basis vectors `|e_x>,|e_y>` and measurement kets

`|m_1>=(1/sqrt(3))|0>+sqrt(2/3)|e_x>`,

`|m_2>=(1/sqrt(3))|0>-(1/sqrt(6))|e_x>+(1/sqrt(2))|e_y>`,

`|m_3>=(1/sqrt(3))|0>-(1/sqrt(6))|e_x>-(1/sqrt(2))|e_y>`.

These are orthonormal, all baseline probabilities equal `1/3`, and direct differentiation gives

`F_xx=2`,

`F_yy=2`,

`F_xy=0`.

Hence

**`Tr F=4`.**

Physically this is a lossless three-mode frequency-bin interferometer followed by ordinary photon counting.

## 9. Exact bilateral curvature saturation

The flagship bilateral boundary law is

`Tr F <= [sqrt(Delta P_+)+sqrt(Delta P_-)]^2`.

For ideal weak phase modulation,

`Delta P_+=Delta P_-=1`,

so

**`Tr F <= (1+1)^2=4`.**

The interferometric measurement above attains

**`Tr F=4`.**

Thus ordinary weak phase modulation of a single-frequency photon is a direct ideal saturation example of the bilateral rank-boundary curvature law.

This is a particularly useful Paper-4 bridge because every ingredient is standard optics:

- an optical carrier;
- an electro-optic phase modulator;
- first-order upper/lower sidebands;
- sideband power versus modulation depth;
- a frequency-bin interferometric analyzer;
- photon counts.

## 10. Important measurement distinction

A spectrum analyzer or direct frequency-bin photon count that measures **only sideband powers** is sufficient to estimate the curvature resource `Delta P_+`, `Delta P_-`, but it does **not** by itself recover both modulation phase quadratures at first order.

The Fisher measurement must be phase sensitive: e.g. a frequency-bin interferometer, coherent sideband/carrier mixing, heterodyne/homodyne equivalent, or another calibrated POVM with nonzero baseline probabilities.

The resource measurement and the Fisher measurement may therefore be performed on identically prepared trials with different analysis settings.

This distinction must be explicit in any practical manuscript.

---

# Part III — experimental/falsification protocol

## 11. Falsification test C — seeded survival-to-synthesis crossover

Use the two-bin converter model.

Measured/calibrated quantities:

1. baseline sideband seed `p` from spectroscopy/photon counting;
2. calibrated local mixing coefficient `kappa` from converter transfer versus drive;
3. local two-quadrature Fisher matrix from a fixed frequency-bin analyzer;
4. at or near `p=0`, sideband population curvature from a quadratic fit of `P_s(x,y)`.

Predictions:

For `p>0`,

`(R_lin^2/4) Tr F <= p`,

with

`R_lin^2=p(1-p)/[kappa^2(1-2p)^2]`.

At `p=0`,

`Tr F <= Delta P_s(0)=4kappa^2`.

Crossover identity:

**`lim_(p->0+) 4p/R_lin^2 = Delta P_s(0)`.**

A calibrated violation of either inequality, or a failure of the limiting relation in a device accurately described by the two-mode unitary model, would contradict the assumed model/resource law.

## 12. Falsification test D — ordinary empty-sideband phase modulation

Measured/calibrated quantities:

1. modulation quadratures `x,y` or equivalent calibrated modulation index;
2. upper/lower first-sideband probabilities near zero modulation;
3. their Hessian/Laplacian at the origin;
4. classical Fisher matrix of an independent phase-sensitive frequency-bin measurement.

Prediction:

**`Tr F <= [sqrt(Delta P_+)+sqrt(Delta P_-)]^2`.**

Ideal phase modulation predicts

`Delta P_+=Delta P_-=1`,

`Tr F=4`,

with equality.

If measured Fisher information exceeds the independently measured curvature RHS beyond calibration/statistical uncertainty, then at least one assumption—state model, parameter normalization, measurement model, or boundary theorem application—is wrong.

---

# Part IV — relation to autonomous action and Paper 3

## 13. Do not overinterpret an externally driven EOM

The examples above directly instantiate the **state-family support geometry and boundary curvature**. A laboratory electro-optic modulator is normally driven by an external classical RF source. That setup is not, by itself, the globally stationary autonomous clock-signal exchange of the PRXQ dual-action theorem.

Therefore WP04 does **not** claim that the electrical RF energy consumed by an EOM equals the flagship synthesis action.

The verified flagship normalization is

`A_S^(2)=(hbar nu/4)(Delta T_S,+ + Delta T_S,-)`,

`A_C^(2)=(hbar nu/4)(Delta T_C,+ + Delta T_C,-)`,

and, in the clean companion implementation problem,

`A_ex^(2)=hbar nu V_min`.

To connect the sideband curvature to that autonomous implementation statement, the controller/clock must be included explicitly in an energy-conserving exchange model. That is WP05.

---

# Part V — significance and manuscript role

## 14. Why WP04 is more than an analogy

The seeded two-bin model exhibits the exact mathematical transition:

- `p>0`: sideband is in support, `R_lin>0`, finite-radius survival applies;
- `p->0+`: both the seed and affine radius collapse;
- `p=0`: sideband is in the kernel, exact nonlinear unitary family remains physical, and second-order population curvature takes over;
- the survival Fisher ceiling tends continuously to the boundary curvature ceiling.

The phase-modulation model then shows the boundary law in perhaps the most familiar possible optics setting and saturates it exactly.

This gives a concrete physical picture for the flagship's central conceptual distinction without importing its full operator machinery into Paper 4.

## 15. Paper-4 significance after WP04

WP03 and WP04 now provide two complementary practical cores:

1. **detector memory:** conventional saturation and low-order dead-time statistics can fail to determine temporal-information transfer;
2. **spectral support:** a pre-existing sideband supports finite-radius information, while an empty sideband moves the resource to measurable second-order sideband generation.

Together with WP01/WP02, this is beginning to look like a coherent practical paper rather than a collection of examples.

## 16. Claim discipline

Do not claim novelty for:

- electro-optic phase modulation or Bessel sideband generation;
- SU(2) frequency conversion/beam-splitter mathematics;
- standard frequency-bin interferometry;
- QFI of pure optical states as such.

The candidate new content is the explicit detector/optics realization of the survival-to-synthesis resource transition, the limiting identity linking finite-radius survival to boundary curvature, and its integration with the broader falsification framework. Prior-art novelty remains to be audited in WP07.

## Next

WP05: include a controller/clock explicitly and reduce the PRA theorem to a textbook resonant exchange Hamiltonian. The target is to show exactly what `V_impl` becomes in a simple beam-splitter/frequency-conversion interaction, and to distinguish that calibrated quadratic coupling from work, RF power consumption, or peak Hamiltonian norm.
