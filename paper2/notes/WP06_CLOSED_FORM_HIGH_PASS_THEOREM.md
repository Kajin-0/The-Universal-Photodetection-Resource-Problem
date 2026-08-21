# WP06 — Closed-Form Information High-Pass Theorem at Type-II Saturation

**Status:** exact closed form derived from WP05 renewal representation; strict monotonicity proved analytically.

This strengthens WP05 from two endpoint values plus a convergent series to a complete closed-form theorem for the entire temporal Fisher spectrum at the symmetric saturation point.

## 1. Starting point

For the one-bin paralyzable detector

\[
Y_n=X_n(1-X_{n-1}),
\qquad X_n\sim\operatorname{Bernoulli}(p_n),
\]

WP05 derived the exact renewal-interval score representation.

At baseline

\[
p=q=\frac12,
\]

renewal intervals satisfy

\[
P(D=d)=\frac{d-1}{2^d},
\qquad d\ge2,
\]

and the exact interval score response to a complex mode `z=e^{i omega}` is

\[
A_d(z)
=\sum_{n=1}^{d-1}
\left(1-\frac{2n}{d-1}\right)z^n+z^d.
\]

The general renewal formula in WP05 contains a same-interval term plus cross-interval terms through

\[
\alpha(z)=E[A_D(z)].
\]

## 2. Exact cancellation of cross-interval correlations

At `p=1/2`, the expectation of the interval response vanishes for **every** frequency:

\[
\boxed{E[A_D(z)]=0,
\qquad |z|=1.}
\]

### Proof

Write `m=d-1>=1`. Then

\[
P(D=m+1)=\frac{m}{2^{m+1}},
\]

and

\[
A_{m+1}(z)
=\sum_{n=1}^{m}\left(1-\frac{2n}{m}\right)z^n+z^{m+1}.
\]

Let `y=z/2`. Interchanging absolutely convergent sums gives

\[
E[A_D(z)]
=\sum_{n\ge1}(n+1)y^n
-2\sum_{n\ge1}ny^n
+\frac z2\sum_{m\ge1}m y^m.
\]

Using

\[
\sum_{n\ge1}y^n=\frac{y}{1-y},
\qquad
\sum_{n\ge1}ny^n=\frac{y}{(1-y)^2},
\]

and `y=z/2`, the terms cancel exactly:

\[
\boxed{E[A_D(z)]=0.}
\]

Therefore distinct renewal-interval score rewards are uncorrelated for every Fourier mode, not only at DC or Nyquist.

Because `E[D]=4` and the incident complex-mode FI rate at `p=1/2` is 1,

\[
\boxed{
G_{1/2}(\omega)=\frac14 E|A_D(e^{i\omega})|^2.
}
\]

This removes the cross-renewal term from WP05 completely.

---

## 3. Summation of the exact spectral series

Again let `m=d-1` and define

\[
B_m(z)=mA_{m+1}(z).
\]

Direct finite summation gives

\[
B_m(z)
=\frac{z}{(z-1)^2}
\left[
 z^m\{m(z-1)(z-2)+2\}
-m(z-1)-2
\right].
\]

Since

\[
P(D=m+1)=\frac{m}{2^{m+1}},
\]

we need

\[
E|A_D(z)|^2
=\frac12\sum_{m\ge1}rac{2^{-m}}{m}|B_m(z)|^2.
\]

Expanding the square reduces the infinite series to the standard sums

\[
\sum_{m\ge1}r^m,
\quad
\sum_{m\ge1}mr^m,
\quad
\sum_{m\ge1}\frac{r^m}{m},
\]

and their versions with `r=z/2`. The logarithmic term comes from

\[
\sum_{m\ge1}\frac{(z/2)^m}{m}
=-\ln(1-z/2).
\]

On the unit circle, set

\[
c=\cos\omega,
\qquad
x=1-c=2\sin^2(\omega/2).
\]

After exact algebraic simplification,

\[
E|A_D(e^{i\omega})|^2
=
\frac{
2(1-c)(1-2c)+\frac12\ln(5-4c)
}{(1-c)^2}.
\]

Therefore

\[
\boxed{
G_{1/2}(\omega)
=\frac{4(1-c)(1-2c)+\ln(5-4c)}{8(1-c)^2},
\qquad c=\cos\omega,
}
\]

for `omega` not congruent to zero modulo `2*pi`, with the continuous extension at zero.

Equivalently, in the cleaner variable

\[
x=1-\cos\omega,
\]

\[
\boxed{
G_{1/2}(\omega)
=1-\frac{1}{2x}
+\frac{\ln(1+4x)}{8x^2},
\qquad x=1-\cos\omega.
}
\]

This is the complete closed-form source-normalized Fisher spectrum.

---

## 4. DC limit

Using

\[
\ln(1+4x)
=4x-8x^2+\frac{64}{3}x^3+O(x^4),
\]

we obtain

\[
G_{1/2}
=\frac{8}{3}x+O(x^2).
\]

Since

\[
x=\frac{\omega^2}{2}+O(\omega^4),
\]

\[
\boxed{
G_{1/2}(\omega)
=\frac{4}{3}\omega^2+O(\omega^4)
\quad\text{as }\omega\to0.
}
\]

Hence

\[
\boxed{G_{1/2}(0)=0.}
\]

The information zero is quadratic in frequency.

---

## 5. Strict high-pass monotonicity

Differentiate with respect to `x`:

\[
\frac{dG}{dx}
=\frac{
2x+\frac{2x}{1+4x}-\ln(1+4x)
}{4x^3}.
\]

Set

\[
y=4x\ge0.
\]

The numerator has the same sign as

\[
h(y)
=\frac{y(y+2)}{2(y+1)}-\ln(1+y).
\]

Now

\[
h(0)=0,
\]

and

\[
\boxed{
h'(y)=\frac{y^2}{2(1+y)^2}\ge0.}
\]

Therefore

\[
h(y)>0\quad\text{for }y>0,
\]

so

\[
\boxed{
\frac{dG}{dx}>0
\quad\text{for }x>0.
}
\]

On `0<omega<pi`, `x=1-cos omega` is strictly increasing. Consequently

\[
\boxed{
\frac{d}{d\omega}G_{1/2}(\omega)>0,
\qquad 0<\omega<\pi.
}
\]

Thus the complete Fisher spectrum is **strictly high-pass over the entire Nyquist band**.

This is a theorem, not a numerical observation.

---

## 6. Exact endpoint

At `omega=pi`, `x=2`, so

\[
G_{1/2}(\pi)
=1-\frac14+\frac{\ln9}{32}
=\boxed{
\frac34+\frac{\ln3}{16}
}
\]

or numerically

\[
\boxed{G_{1/2}(\pi)\approx0.818663268.}
\]

Combining with DC,

\[
\boxed{
0=G_{1/2}(0)
<G_{1/2}(\omega)
<\frac34+\frac{\ln3}{16}
<1
}
\]

for `0<omega<pi`.

---

## 7. The theorem in words

> **Saturation-induced information high-pass theorem.**  For the autonomous one-bin paralyzable detector `Y_n=X_n(1-X_{n-1})` driven by independent Bernoulli events at the symmetric operating point `p=1/2`, the complete local source-normalized temporal Fisher spectrum is given by the closed form above. It vanishes quadratically at DC, increases strictly over the entire temporal Nyquist band, and reaches `3/4+ln(3)/16` at Nyquist.

This detector is therefore locally blind to a uniform intensity perturbation while retaining a large fraction of the incident information about rapidly alternating perturbations.

---

## 8. Conceptual consequence

The usual intuition

`dead time / recovery -> temporal low-pass`

is false even for an elementary high-flux event detector when performance is defined by the complete-record local Fisher information.

Here hidden Type-II memory produces the opposite behavior:

\[
\boxed{
\text{zero DC information}
\longrightarrow
\text{strictly increasing finite-frequency information}.
}
\]

The effect is not caused by a downstream filter. It is caused by the combinatorial information in **where runs begin**. Uniform changes at `p=1/2` are hidden by the symmetry `p<->1-p`, while temporal alternation breaks that symmetry and is visible in the output event pattern.

This is a concrete demonstration of why the general-channel Fisher spectrum is needed at high flux: a scalar count-rate slope, dead time, or recovery constant cannot rank temporal tasks.

---

## 9. Novelty posture

The underlying renewal, Bernoulli-run, conditional-score, and Fourier-series techniques are standard ingredients. The claim requiring novelty verification is their resulting photodetection information theorem:

- Type-II hidden dead time;
- complete-record local waveform FI rather than a task-specific range/intensity CRLB;
- exact closed temporal spectrum;
- exact DC nonidentifiability;
- strict high-pass information retention at the saturation point.

The current literature audit has found extensive paralyzable dead-time count statistics and task-specific CRLB work, but no predecessor for this exact temporal Fisher-spectrum result. **Do not yet make a priority/first claim.**

---

## 10. Next step

The highest-value next question is whether the continuous-time paralyzable Poisson counter exhibits an analogous phenomenon near the classical saturation point

\[
\lambda\tau_d=1,
\]

where its mean recorded count rate

\[
r=\lambda e^{-\lambda\tau_d}
\]

has zero derivative with respect to `lambda`.

If the complete timestamp record retains nonzero finite-frequency Fisher information at that point while DC FI collapses or is strongly suppressed, the discrete theorem would become the exact solvable prototype of a continuous-time physical result.
