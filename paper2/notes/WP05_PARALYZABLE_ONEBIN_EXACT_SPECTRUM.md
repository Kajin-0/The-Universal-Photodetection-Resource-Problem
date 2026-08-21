# WP05 — Exact One-Bin Paralyzable Detector: Information-Spectral Inversion at Saturation

**Status:** exact discrete-time theorem derived; numerical/Monte-Carlo verification performed independently. This is the first Paper-2 example showing genuinely frequency-dependent high-flux Fisher retention from hidden detector state.

## 1. Why this model

The ideal nonparalyzable detector in WP04 loses a frequency-independent live-time fraction because its live/dead gate is exactly reconstructible from the output timestamps.

For a paralyzable (Type-II) detector, hidden incident events can extend the dead state without appearing in the output. The detector state is therefore not reconstructible from the accessible record. This is the simplest mechanism expected to generate a nontrivial Fisher spectrum.

To isolate the phenomenon exactly, use a one-bin discrete-time model.

---

## 2. Source and detector

Let

\[
X_n\sim\operatorname{Bernoulli}(p_n)
\]

independently across integer time bins.

For a weak fractional temporal perturbation,

\[
p_n(\epsilon)=p[1+\epsilon u_n],
\qquad 0<p<1,
\]

with `epsilon` sufficiently small.

The one-bin paralyzable detector outputs

\[
\boxed{Y_n=X_n(1-X_{n-1}).}
\]

Thus an event is registered only if the current bin contains an incident event and the preceding bin does not. Every incident event, including an unrecorded one, suppresses registration in the following bin. A run `111...` therefore produces only its first `1` as a registered event.

This is exactly a one-bin Type-II/retriggered dead-time rule.

The channel is stationary/autonomous at constant baseline `p`, but it is history dependent and the hidden input state `X_{n-1}` is not determined by `Y`.

---

## 3. Incident score and Fisher information

At `epsilon=0`, one input bin contributes score

\[
\xi_n u_n,
\qquad
\xi_n=\frac{X_n-p}{q},
\qquad q=1-p.
\]

Indeed,

\[
\partial_\epsilon\log P_\epsilon(X_n)|_0
=
\begin{cases}
u_n,&X_n=1,\\
-(p/q)u_n,&X_n=0.
\end{cases}
\]

Since the `X_n` are independent,

\[
F_{\rm in}[u,v]
=\frac{p}{q}\sum_nu_nv_n.
\]

Hence the normalized source tangent is scalar `ell^2(Z)`, and the stationary general-channel theorem implies a discrete temporal multiplier `G_p(omega)` with `0<=G_p<=1`.

---

## 4. Output is a renewal process at baseline

A registered event is the first `1` after a run of one or more zeros. Starting from a registered `1`, let

- `A>=1` be the length of the current run of ones;
- `B>=1` be the following run of zeros;
- `D=A+B` be the interval to the next registered event.

At baseline,

\[
P(A=a) = p^{a-1}q,
\qquad
P(B=b)=q^{b-1}p,
\]

independently, so

\[
\boxed{
P(D=d,A=a)=p^a q^{d-a},
\quad
1\le a\le d-1,
\quad d\ge2.
}
\]

Therefore

\[
P_D(d)=\sum_{a=1}^{d-1}p^a q^{d-a}
=
\begin{cases}
\displaystyle pq\frac{p^{d-1}-q^{d-1}}{p-q},&p\ne q,\\[1ex]
\displaystyle \frac{d-1}{2^d},&p=q=1/2.
\end{cases}
\]

and

\[
\boxed{E[D]=\frac1p+\frac1q=\frac1{pq}.}
\]

The stationary registered-event rate is therefore `pq` per bin.

---

## 5. Exact conditional score given the complete output record

Between two successive output events separated by `D=d`, the only hidden ambiguity is the switch point `A=a`:

\[
11\cdots1\,00\cdots0\,1.
\]

Conditional on `D=d`,

\[
P(A=a|D=d)
=\frac{p^aq^{d-a}}{P_D(d)}.
\]

For bins `1<=n<=d-1` after the previous registered event,

\[
X_n=1\iff A>n.
\]

Define the conditional score coefficient

\[
\boxed{
c_{d,n}
=\frac{P(A>n|D=d)-p}{q},
\qquad 1\le n<d,
}
\]

and note that the endpoint `X_d=1` is known from the next output event, so

\[
\boxed{c_{d,d}=1.}
\]

For an arbitrary waveform, the exact output score contribution of that renewal interval is

\[
\boxed{
R_d[u]=\sum_{n=1}^{d}c_{d,n}u_{T+n},
}
\]

where `T` is the preceding output time.

This is simply the general identity `S_out=E[S_in|Y]` evaluated exactly for this hidden-state detector.

---

## 6. Exact frequency-domain renewal formula

Complexify the tangent space and set

\[
u_n=z^n,
\qquad z=e^{i\omega}.
\]

Define the interval response

\[
\boxed{
A_d(z)=\sum_{n=1}^{d}c_{d,n}z^n.
}
\]

For iid renewal intervals `D_i`, the score reward from interval `i` is

\[
R_i=z^{T_{i-1}}A_{D_i}(z).
\]

Let

\[
\alpha(z)=E[A_D(z)],
\]

\[
\beta(z)=E[A_D(z)z^{-D}],
\]

\[
\phi(z)=E[z^{-D}].
\]

For frequencies with `phi(z) != 1`, renewal summation gives the asymptotic complex-score variance per renewal interval

\[
\boxed{
V(z)
=E|A_D(z)|^2
+2\operatorname{Re}
\frac{\beta(z)\alpha(z)^*}{1-\phi(z)}.
}
\]

Dividing by `E[D]` and by the incident complex-waveform FI rate `p/q` gives

\[
\boxed{
G_p(\omega)
=\frac{q}{pE[D]}V(e^{i\omega})
=q^2V(e^{i\omega}).
}
\]

The removable zero-frequency limit is obtained directly from the constant-waveform score.

This is an exact convergent series representation of the complete Fisher spectrum of the one-bin paralyzable detector.

---

## 7. Symmetric saturation point `p=q=1/2`

At

\[
p=q=\frac12,
\]

we have

\[
P_D(d)=\frac{d-1}{2^d}.
\]

Moreover the hidden run length is uniform conditional on `D=d`:

\[
P(A=a|D=d)=\frac1{d-1},
\qquad a=1,\ldots,d-1.
\]

Hence for `1<=n<d`,

\[
P(A>n|D=d)=\frac{d-1-n}{d-1},
\]

and therefore

\[
\boxed{
c_{d,n}=\frac{d-1-2n}{d-1},
\quad n<d,
\qquad c_{d,d}=1.
}
\]

---

## 8. Exact DC blindness

For a uniform perturbation `u_n=1`, each interval score is

\[
A_d(1)
=\sum_{n=1}^{d-1}\frac{d-1-2n}{d-1}+1.
\]

But

\[
\sum_{n=1}^{d-1}(d-1-2n)=-(d-1),
\]

so

\[
\boxed{A_d(1)=0\quad\text{for every }d.}
\]

Therefore the complete output score for a spatially uniform/DC fractional intensity perturbation vanishes interval by interval in the long-record interior:

\[
\boxed{G_{1/2}(0)=0.}
\]

This is stronger than saying the *mean count rate* has zero derivative. At `p=1/2`, the **entire stationary output renewal law** is locally insensitive to a uniform change in `p`, because its interval law is symmetric under `p <-> 1-p`.

The detector is locally nonidentifiable for the DC intensity direction despite retaining a complete timestamp record.

---

## 9. Exact Nyquist information survives

Now take the alternating temporal mode

\[
u_n=(-1)^n,
\qquad \omega=\pi.
\]

Using the coefficients above,

\[
A_d(-1)
=\sum_{n=1}^{d-1}
\frac{d-1-2n}{d-1}(-1)^n
+(-1)^d.
\]

Direct summation gives

\[
\boxed{
A_d(-1)=
\begin{cases}
-2,&d\text{ odd},\\[1ex]
\displaystyle\frac{d}{d-1},&d\text{ even}.
\end{cases}
}
\]

At `p=1/2`,

\[
E[A_D(-1)]=0,
\]

so different renewal-interval score rewards are uncorrelated for the alternating mode. Therefore

\[
G_{1/2}(\pi)
=\frac{1}{E[D]}E[A_D(-1)^2]
=\frac14E[A_D(-1)^2].
\]

The odd-`d` contribution is

\[
\sum_{k\ge1}
\frac{2k}{2^{2k+1}}\,4
=\frac{16}{9}.
\]

For even `d=2k`,

\[
\sum_{k\ge1}
\frac{2k-1}{2^{2k}}
\left(\frac{2k}{2k-1}\right)^2
=\sum_{k\ge1}
\frac{4k^2}{(2k-1)4^k}.
\]

Using

\[
\frac{4k^2}{2k-1}=2k+1+\frac1{2k-1}
\]

and

\[
\sum_{k\ge1}\frac{1}{(2k-1)4^k}
=\frac14\ln3,
\]

this even contribution is

\[
\frac{11}{9}+\frac14\ln3.
\]

Thus

\[
E[A_D(-1)^2]
=3+\frac14\ln3,
\]

and finally

\[
\boxed{
G_{1/2}(\pi)
=\frac34+\frac{\ln3}{16}
\approx0.818663268.
}
\]

---

## 10. Information-spectral inversion

At the same operating point,

\[
\boxed{
G_{1/2}(0)=0,
\qquad
G_{1/2}(\pi)\approx0.8187.
}
\]

This is the central result of WP05.

An ideal Type-II detector at its symmetric saturation point can be **completely locally blind to uniform/DC intensity changes while preserving more than 81% of the incident local Fisher information in the fastest alternating temporal mode.**

This is not a low-pass response. It is strongly frequency selective in the opposite sense.

A scalar recovery time or saturated count-rate slope therefore cannot characterize temporal information transfer in a history-dependent detector.

---

## 11. Physical interpretation

The registered events are starts of runs of incident photons. At `p=1/2`, increasing the probability of a `1` uniformly lengthens runs of ones while shortening runs of zeros in a locally symmetric way. The distribution of sums `D=A+B` therefore has zero first-order sensitivity to uniform `p`.

An alternating perturbation breaks that symmetry. It changes the odds of hidden run boundaries differently on even and odd bins, and the exact output timestamps retain substantial information about that modulation.

Hence high-flux saturation is **task dependent**: loss of DC rate sensitivity does not imply loss of temporal waveform sensitivity.

---

## 12. Relation to Jorgensen–Johnson 2026

Jorgensen & Johnson treat nonparalyzable dead time with causal gating and explicitly leave paralyzable/Type-II dead time as future work. Their activation-frequency result explains why WP04's predictable-gate case is flat.

WP05 is structurally different:

- every hidden incident event can alter future detector availability;
- the live state is not reconstructible from the output record;
- the source perturbation changes the posterior hidden-state law;
- the complete FI becomes frequency dependent;
- the symmetric operating point exhibits exact DC nonidentifiability but strong finite-frequency information.

A dedicated search is still required before any priority claim.

---

## 13. Validation already performed

Two independent calculations agree:

1. the renewal-interval conditional-score formula above;
2. a sequential hidden-state filtering calculation in which the baseline posterior `q_n=P(X_n=1|Y_{<=n})` and its tangent derivative are propagated through the exact binary observation recursion.

Monte-Carlo time averaging of squared score innovations agrees with the renewal formula across frequencies and multiple `p`, including the analytic value at `p=1/2, omega=pi`.

A repository reproduction script should be added next.

---

## 14. Next gates

1. Add an exact/numerical reproduction script and convergence tests.
2. Search specifically for FI/LAN of paralyzable Type-II dead-time channels and for the one-bin transition-observation model.
3. Derive or simplify the full `G_{1/2}(omega)` curve, if possible.
4. Determine whether `G_{1/2}(omega)` is monotone on `[0,pi]`; numerics suggest a strong high-pass trend but this is not yet proved.
5. Generalize to `d`-bin paralyzable dead time and look for spectral zeros/passbands.
6. Build the continuous-time Type-II analogue, where hidden events restart a fixed dead interval.
7. Use the general Paper-2 theorem to state this as a corollary rather than an isolated HMM calculation.
