# WP07 — Gauge-invariant energy edge and covariant sub-POVM proof repair

**Date:** 2026-08-21

## Status

Proof/physical-interpretation hardening of WP06. The main area law survives, but the correct resource is **detected energy above the lower spectral edge actually participating in the detected state**, not an absolute Hamiltonian energy origin.

The Kiukas--Ruschhaupt--Werner covariant-arrival-time construction also closes the main intertwining concern: for subnormalized covariant observables the dilation map is a contraction that is fiberwise in the same energy variable, so the click probability and detected first energy moment are represented exactly in the dilation.

---

## 1. Why the energy origin must be gauge invariant

The time-shift state orbit is

`rho_theta = exp(-i H theta/hbar) rho exp(+i H theta/hbar)`.

Replacing

`H -> H+c I`

changes each unitary by a global phase and therefore leaves the density-operator orbit exactly unchanged.

Likewise, covariance of a POVM under `H` is unchanged by adding `cI`.

Therefore **no physical timing bound may depend on an arbitrary additive energy origin**.

The crude WP06 notation `H-E0` is correct only when `E0` is chosen as the largest shift that leaves the detected spectral amplitude one-sided.

---

## 2. Detected spectral measure and optimal lower edge

Let `F(dt)` be a time-covariant subnormalized event POVM and

`Q=F(R)<=I`.

Covariance implies

`[Q,H]=0`.

For state `rho`, define the finite detected spectral measure

`mu_det(A) = Tr[rho Q P_H(A)]`,

where `P_H` is the spectral measure of `H`.

Its total mass is

`eta = mu_det(R)=Tr[rho Q]`.

Assume `eta>0` and that the detected spectral measure is bounded below. Define

`E_* = ess inf supp(mu_det)`

(the lower spectral edge of the detected energy distribution).

Then

`mu_det((-∞,E_*))=0`,

and `E_*` is the largest additive shift for which the detected spectral amplitude remains supported on nonnegative excitation energy.

Define the **detected excess-energy moment**

`E_det^+ = int (E-E_*) mu_det(dE)`

`= Tr[rho Q(H-E_*)]`

whenever finite.

This quantity is invariant under `H -> H+cI` because `E_* -> E_*+c`.

In angular-frequency units,

`omega_det^+ = E_det^+/hbar`.

This is the resource that should appear in the sharp area law.

---

## 3. Primary covariant-POVM structure from Kiukas--Ruschhaupt--Werner

Kiukas, Ruschhaupt, and Werner, *J. Math. Phys.* **54**, 042109 (2013), Sec. II C, give the general time-covariant arrival-observable dilation for an absolutely continuous Hamiltonian.

In direct-integral energy representation,

`H = int^⊕ dE H_E`,

`(H psi)(E)=E psi(E)`.

For a normalized covariant time observable there is an energy-independent multiplicity space `K` and measurable energy-fiber isometries

`V_E: H_E -> K`

such that the dilation map

`V: H -> L2(R,dE;K)`

acts fiberwise:

`(V psi)(E)=V_E psi(E)`.

Fourier transformation in the same energy variable produces the time representation in `L2(R,dt;K)`.

Crucially, Kiukas et al. explicitly allow **subnormalized** observables `F(1)<=I`: then `V` is a contraction rather than an isometry. The total effect is

`Q=F(1)=V^*V`,

which commutes with `H`.

Because `V` acts at each energy without changing the energy coordinate, the detected spectral norm and first moment are carried into the dilation exactly.

---

## 4. Pure-state proof with exact first moment

Let `rho=|psi><psi|` and set

`a(E)=V_E psi(E)`.

Then

`int ||a(E)||_K^2 dE = <psi|V^*V|psi> = eta`.

Because the dilation retains the energy coordinate,

`int (E-E_*) ||a(E)||_K^2 dE`

`= <psi|Q(H-E_*)|psi>`

`= E_det^+`.

Introduce excitation angular frequency

`w=(E-E_*)/hbar >=0`

and absorb the Jacobian into the normalized Fourier-domain amplitude. Multiplying the time amplitude by the carrier phase `exp(+i E_* t/hbar)` does not change the observed time density.

With the unitary Fourier convention, obtain a positive-frequency vector amplitude `u(t)` satisfying

`p(t)=||u(t)||_K^2`,

`||u||_2^2=eta`,

`||u||_{Hdot_+^{1/2}}^2 = E_det^+/hbar = omega_det^+`.

Thus the moment identity assumed in WP06 is exact under these hypotheses, not merely an upper bound.

---

## 5. Mixed-state proof by purification

Let `rho` be any normal state with finite `E_det^+`.

Choose a purification

`|Psi> in H tensor R`

with

`Tr_R |Psi><Psi| = rho`.

Use generator

`H tensor I_R`

and extended dilation

`V tensor I_R`.

The time POVM acts trivially on the purifier. The resulting time amplitude is vector valued in

`K tensor R`.

Its norm-square is exactly the observed click-time subdensity because

`p(t)dt = Tr[rho F(dt)]`

is unchanged by purification.

Likewise,

`||(V tensor I_R)Psi||_2^2 = Tr[rho Q]=eta`,

and the positive excitation first moment is

`<Psi|Q(H-E_*) tensor I_R|Psi>`

`= Tr[rho Q(H-E_*)]`

`= E_det^+`.

Therefore the vector-valued Hardy inequality from WP06 applies directly to arbitrary mixed states with **no loss in the energy moment**.

This purification route is cleaner than introducing the pseudoinverse-normalized POVM `Q^{-1/2}FQ^{-1/2}` and avoids domain problems when `Q` has a kernel.

---

## 6. Publication-grade theorem candidate

### Theorem — gauge-invariant positive-energy temporal Fisher-area bound

Let `H` be self-adjoint and let the portion of its spectrum participating in a time-covariant event sub-POVM be absolutely continuous. Let `F(dt)` be a time-translation-covariant subnormalized POVM on `R`,

`e^{iHs/hbar} F(A) e^{-iHs/hbar}=F(A-s)`,

with total event effect

`Q=F(R)<=I`.

Let `rho` be a normal input state with event probability

`eta=Tr[rho Q]>0`.

Let `mu_det(A)=Tr[rho QP_H(A)]` be the detected spectral measure and suppose it is bounded below with lower edge `E_*` and finite excess mean

`E_det^+=Tr[rho Q(H-E_*)]<infinity`.

Assume the event-time law has conditional density `f(t)` given an event. Define its source-normalized independent-event Fisher transfer

`G(nu)=eta |int exp(-i nu t) f(t)dt|^2`.

Then

`boxed: int_R G(nu)dnu <= 2 E_det^+/hbar`.

Equivalently,

`boxed: eta B_FI <= E_det^+/h`,

where

`B_FI=(1/2)int f(t)^2dt`.

If `G(2*pi*f)>=q` for every ordinary frequency `|f|<=B`, then

`boxed: E_det^+ >= h B q`.

### Proof skeleton

1. Kiukas--Ruschhaupt--Werner generalized imprimitivity dilation gives a vector amplitude with Fourier support in the detected energy spectrum and preserves the detected spectral measure.
2. Shift by `E_*`; this changes only an unobservable carrier phase and places the Fourier support in `[0,infinity)`.
3. The amplitude has `L2` norm squared `eta` and `Hdot_+^{1/2}` norm squared `E_det^+/hbar`.
4. Apply the sharp vector-valued Pocovnicu inequality:

   `int p^2 <= eta E_det^+/(pi hbar)`.

5. Since `f=p/eta`, Parseval yields

   `int G = 2*pi*eta*int f^2 = (2*pi/eta)int p^2 <= 2E_det^+/hbar`.

6. Integrating a flat lower bound over `|nu|<=2*pi B` yields `E_det^+>=hBq`.

---

## 7. Absolutely continuous spectrum is a real hypothesis

A normalized covariant time POVM on the real line requires an absolutely continuous translation representation in the generalized imprimitivity construction. Kiukas et al. explicitly make absolute continuity of `H` a standing assumption for this arrival-time setting.

Therefore WP07 is presently a theorem for **continuous arrival-time observables associated with absolutely continuous detected energy spectrum**.

Discrete or periodic spectra lead instead to phase/periodic/almost-periodic time observables and require a separate circle/Besicovitch formulation. Hall's Rényi energy--time work is particularly relevant there.

Do not state WP07 as covering arbitrary discrete Hamiltonians without modification.

---

## 8. Optical carrier interpretation

The gauge-invariant edge `E_*` resolves a central physical issue.

For a detected wavepacket with strict spectral support

`E in [E_min,infinity)`,

the timing law is unchanged by demodulating the time amplitude by `E_min/hbar`. The resource in WP07 is therefore

`E_det^+ = detected mean energy above E_min`,

not the absolute optical carrier energy measured relative to an arbitrary laboratory zero.

For a narrow optical band centered near a large carrier frequency, this correctly makes temporal localization depend on the **available spectral extent above the participating lower edge**, rather than on the carrier offset itself.

If the detected spectrum has nonzero tails all the way down to the physical lower edge (e.g. zero photon frequency), then `E_*` is that lower edge and the exact bound may be numerically loose. One may later seek robust quantile/truncated-spectrum refinements, but the exact theorem should use the true essential lower edge.

Do not casually replace `E_det^+` by optical carrier energy in manuscript prose.

---

## 9. Constant efficiency and energy-selective detection

### Energy-independent loss

If

`Q=eta I`

on the participating state support, then the detected spectral distribution is simply a scaled copy of the source distribution and has the same lower edge `E_*`.

Hence

`E_det^+=eta E_src^+`.

The area law becomes

`int G <= 2 eta E_src^+/hbar`,

and the conditional bandwidth bound is

`boxed: B_FI <= E_src^+/h`.

### Energy-selective detection

If `Q` depends on energy, the detected lower edge and mean excess must be computed **after selection**:

`mu_det(dE)=Tr[rho QP_H(dE)]`.

This is essential. An energy filter can alter both efficiency and the conditional timing law. The theorem tracks that exactly through `E_*` and `E_det^+`.

---

## 10. Direct normalization audit

Use

`F_timing(nu)=int exp(-inu t) f(t)dt`.

With the Fourier convention

`F(nu)=int exp(-inu t)f(t)dt`,

Parseval is

`int_{R}|F(nu)|^2 dnu = 2*pi int_R f(t)^2dt`.

Therefore

`int G(nu)dnu`

`=eta int |F(nu)|^2dnu`

`=2*pi eta int f^2dt`.

Since

`B_FI=(1/2)int f^2dt`,

`boxed: int G(nu)dnu = 4*pi eta B_FI`.

For a flat ordinary-frequency band `|f_mod|<=B`, angular frequency is `nu=2*pi f_mod`; the interval width in `nu` is `4*pi B`. Therefore

`int Gdnu >= 4*pi B q`.

Combining with `int G<=2E_det^+/hbar` gives

`E_det^+ >= 2*pi hbar Bq = hBq`.

All factors of `2`, `pi`, `hbar`, and `h` are therefore consistent.

---

## 11. Equality-family constant audit

Let

`f_a(t)=a/[pi(t^2+a^2)]`.

Then

`int f_a^2dt = 1/(2*pi*a)`,

so

`B_FI=1/(4*pi*a)`.

Its characteristic function is

`F_a(nu)=exp(-a|nu|)`,

therefore

`G_a(nu)=eta exp(-2a|nu|)`

for constant efficiency and

`int G_a dnu = eta/a`.

A positive-frequency one-pole amplitude has exponential excitation-frequency probability density with mean

`omega_bar^+=1/(2a)`.

Thus

`2 eta omega_bar^+=eta/a=int G_a`,

and

`E_src^+/h = [hbar/(2a)]/[2*pi hbar]=1/(4*pi a)=B_FI`.

The sharp constants in WP06/WP07 are internally consistent.

---

## 12. Prior-art update

Kiukas--Ruschhaupt--Werner directly support the general dilation/fiberwise energy structure required by the theorem, including subnormalized observables:

- normalized case: energy-fiber isometries `V_E` into an energy-independent multiplicity space;
- subnormalized case: replace the isometry by a contraction `V`, with `F(1)<=I` commuting with `H`.

Hall (Entropy 24, 1679, 2022) develops strong Rényi/mean-resource Heisenberg bounds and discrete/almost-periodic time--energy uncertainty relations. His discussion explicitly identifies continuous-spectrum displacement generators as an extension direction, so the audited paper does not directly supply the continuous arrival-time `L2` density bound used here.

Targeted searches still have not located the exact covariant arrival-time statements

`int Gdnu <= 2E_det^+/hbar`,

`eta B_FI <= E_det^+/h`,

or

`E_det^+ >= hBq`.

Priority remains uncertified.

---

## 13. Remaining gates after WP07

1. Replace the finite/countable mark extension by a fully general direct-integral measurable-mark proof.
2. Search harder for continuous-spectrum Rényi-2/collision-entropy time--energy inequalities equivalent to `int f^2 <= E^+/(pi hbar)`.
3. Check exact equality characterization for general subnormalized/multiplicity POVMs.
4. Decide whether state-dependent `E_*` is the best publication form or whether a fixed apparatus/source spectral threshold should be stated first with `E_*` as a sharpening.
5. Explore robust bounds when the spectrum has arbitrarily small low-energy tails, where the essential-infimum theorem can be loose.
6. Only after these: test whether an area-law analogue survives memory-bearing trajectory channels.

## Decision

WP06's main theorem survives and is strengthened conceptually: the correct resource is **gauge-invariant detected excess energy above the detected spectral edge**. The covariant POVM dilation preserves the needed first moment exactly under the absolutely-continuous-spectrum hypotheses.
