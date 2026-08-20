# WP8 — SLD Stam inequality and globally tight arbitrary-pointer energy theorem

**Date:** 2026-08-19

## Purpose

The published bosonic entropy-power/Stam literature uses a divergence-based Fisher information and therefore does not directly solve the UPRP SLD-QFI problem. However, a separate **directional SLD Stam inequality** follows directly from SLD-QFI data processing, product additivity, and beam-splitter covariance.

This closes a major gap: the WP7 energy-repaired QFI theorem is not merely Gaussian. It is globally valid and tight for **arbitrary detector pointer states** under the passive-linear oscillator model and a total excitation-energy budget.

---

# 1. Directional SLD translation Fisher information

For a bosonic state `rho`, define

\[
J_X(\rho)
\equiv
F_Q\!\left[
D_X(\theta)\rho D_X^\dagger(\theta);
\theta
\right],
\]

where `D_X(theta)=exp(-i theta P)` shifts the conjugate quadrature according to

\[
D_X^\dagger(\theta)XD_X(\theta)=X+\theta.
\]

The normalization is `[X,P]=i`; vacuum/coherent states have

\[
\boxed{J_X(|0\rangle)=2.}
\]

SLD QFI has the two properties needed below:

1. **data processing:** parameter-independent CPTP maps cannot increase QFI;
2. **product additivity:** for product parameter families, QFI adds.

---

# 2. Beam-splitter covariance

Let

\[
\rho_C
=\mathcal B_\lambda(\rho_A\otimes\rho_B)
\]

be one output mode of a beam splitter with

\[
X_C=\sqrt\lambda X_A+\sqrt{1-\lambda}X_B,
\qquad 0<\lambda<1.
\]

Translate the two inputs by `a theta` and `b theta`. The output is translated by

\[
(\sqrt\lambda\,a+\sqrt{1-\lambda}\,b)\theta.
\]

Thus if

\[
\boxed{
\sqrt\lambda\,a+\sqrt{1-\lambda}\,b=1,
}
\]

the resulting output family is exactly the unit-translation family used to define `J_X(rho_C)`.

The input product-family QFI is

\[
a^2J_X(\rho_A)+b^2J_X(\rho_B).
\]

Data processing through the beam splitter plus discarded output therefore gives

\[
J_X(\rho_C)
\le
a^2J_A+b^2J_B
\]

for every `a,b` satisfying the linear constraint.

---

# 3. SLD Stam inequality

Minimize

\[
J_Aa^2+J_Bb^2
\]

subject to

\[
\sqrt\lambda a+\sqrt{1-\lambda}b=1.
\]

The quadratic constrained minimum is

\[
\frac1{\lambda/J_A+(1-\lambda)/J_B}.
\]

Hence

\[
\boxed{
\frac1{J_X(\rho_C)}
\ge
\frac\lambda{J_X(\rho_A)}
+
\frac{1-\lambda}{J_X(\rho_B)}.
}
\]

Equivalently,

\[
\boxed{
J_C
\le
\frac1{\lambda/J_A+(1-\lambda)/J_B}.
}
\]

This proof uses the **SLD/Bures QFI itself** and remains finite on pure coherent, vacuum, and squeezed-vacuum states.

**Status:** PROVED.

Novelty warning: the inequality is a direct consequence of standard SLD-QFI monotonicity/additivity plus displacement covariance and may be known in broader quantum-estimation literature. Do not claim the mathematical inequality itself as novel without citation chaining.

---

# 4. Application to coherent photodetection

Let the optical source port `A` be vacuum after removing the theta-dependent coherent displacement. Let the detector pointer port `B` start in an arbitrary theta-independent state `sigma_D`.

The detector output receives source amplitude probability

\[
\tau
\]

and pointer amplitude probability

\[
1-\tau.
\]

Thus set

\[
\lambda=\tau,
\qquad
J_A=2,
\qquad
J_B=J_X(\sigma_D).
\]

The base detector output state has translation QFI

\[
\boxed{
J_{D,0}
\le
\frac1{\tau/2+(1-\tau)/J_B}.
}
\]

The optical parameter produces only a `sqrt(tau)` displacement at the detector output, so

\[
F_D=\tau J_{D,0}.
\]

The coherent optical input has `F_in=2`. Therefore

\[
\boxed{
\frac{F_D}{F_{\rm in}}
\le
\frac{\tau J_B}
{2(1-\tau)+\tau J_B}.
}
\]

Any electrical measurement is downstream of the detector state, so the same bound holds for `F_elec`.

---

# 5. Total excitation-energy bound for arbitrary pointer states

Let a normalized collective detector mode have quadratures `X,P`, and suppose the complete detector pointer apparatus has total mean excitation budget

\[
N_{\rm tot}\le N.
\]

For any normalized collective mode accessible by passive mixing,

\[
n_c\le N.
\]

After removing theta-independent means,

\[
\operatorname{Var}(X)+\operatorname{Var}(P)
=2n_c+1
\le2N+1.
\]

Robertson gives

\[
\operatorname{Var}(X)\operatorname{Var}(P)
-\operatorname{Cov}(X,P)^2
\ge\frac14.
\]

Maximizing `Var(P)` under these constraints yields

\[
\boxed{
\operatorname{Var}(P)
\le
N+\frac12+\sqrt{N(N+1)}.
}
\]

For any unitary translation family,

\[
J_X(\rho)\le4\operatorname{Var}(P).
\]

Therefore

\[
J_B
\le
4N+2+4\sqrt{N(N+1)}.
\]

Define

\[
\xi(N)
=(\sqrt{N+1}-\sqrt N)^2.
\]

Using

\[
2N+1+2\sqrt{N(N+1)}=1/\xi(N),
\]

we obtain

\[
\boxed{
J_B\le\frac{2}{\xi(N)}.
}
\]

This bound is achieved by a pure squeezed vacuum using all available excitation in the collective mode and aligning the anti-squeezed generator quadrature with the displacement generator.

---

# 6. Globally tight arbitrary-pointer theorem

Substituting `J_B<=2/xi(N)` into the SLD Stam photodetection inequality gives

\[
\boxed{
\frac{F_{\rm elec}}{F_{\rm in}}
\le
\frac{\tau}
{\tau+(1-\tau)\xi(N)}.
}
\]

This is exactly the formula previously derived under a Gaussian-pointer assumption.

It is now valid for **arbitrary, including non-Gaussian, detector pointer states** satisfying the total excitation budget.

The bound is globally tight because it is saturated by:

1. a pure squeezed-vacuum detector pointer with mean excitation `N`;
2. a beam splitter of source-to-detector transfer probability `tau`;
3. coherent source displacement encoding;
4. an aligned homodyne electrical measurement.

Hence

\[
\boxed{
\sup_{\rho_D:\,\langle N_D\rangle\le N}
\frac{F_{\rm elec}}{F_{\rm in}}
=
\frac{\tau}
{\tau+(1-\tau)\xi(N)}
}
\]

within the passive-linear single-collective-mode photodetection model.

**Status:** PROVED and globally saturable under the stated model assumptions.

---

# 7. Coupling-action form

WP7 gives

\[
\tau\le\sin^2\Gamma,
\qquad
\Gamma=\int_0^t\|V(s)\|_2ds.
\]

The right-hand side is increasing in `tau`, so

\[
\boxed{
\frac{F_{\rm elec}}{F_{\rm in}}
\le
\frac{\sin^2\Gamma}
{\sin^2\Gamma+\cos^2\Gamma\,\xi(N)}
}
\]

for `0<=Gamma<=pi/2`.

To transfer fraction `q`, necessarily

\[
\boxed{
\Gamma
\ge
\arctan\sqrt{\frac{q\xi(N)}{1-q}}.
}
\]

This upgrades `WP7_ENERGY_REPAIRED_GAUSSIAN_THEOREM.md`: the theorem is no longer restricted to Gaussian pointer states.

---

# 8. Relation to the published divergence-Fisher Stam literature

`WP8_STAM_METRIC_AUDIT.md` remains correct in its narrow conclusion:

> the **published divergence-based** Fisher-information Stam machinery from the quantum EPI literature cannot simply be identified with SLD QFI.

The present theorem bypasses that problem by deriving a Stam inequality **directly for directional SLD QFI** using only SLD data processing/additivity and beam-splitter displacement covariance.

Thus there is no metric substitution.

---

# 9. Free-energy consequence and remaining gap

A finite excitation budget gives a globally tight theorem because energy directly bounds the maximum translation-generator variance and a pure squeezed state simultaneously saturates the QFI-variance inequality.

A finite-temperature nonequilibrium free-energy budget is subtler. Mixed high-entropy states can have large quadrature variance but low SLD QFI. The crude chain

\[
J_B\le4\operatorname{Var}(P)
\]

therefore yields a rigorous but potentially loose free-energy bound.

The exact Gaussian free-energy theorem in `WP8_FREE_ENERGY_GAUSSIAN_CLOSURE.md` remains stronger within the Gaussian class.

The remaining non-Gaussian problem is now narrower:

> maximize the **pointer's SLD translation QFI** `J_B` subject to `D(rho_D||tau_beta)<=D_0`.

Once that scalar resource frontier `J_F^{max}(D_0,H_D)` is known, the SLD Stam theorem immediately gives the globally optimal photodetection transfer bound

\[
\boxed{
\frac{F_{\rm elec}}{F_{\rm in}}
\le
\frac{\tau J_F^{\max}}
{2(1-\tau)+\tau J_F^{\max}}.
}
\]

This is the exact next mathematical target for WP8.
