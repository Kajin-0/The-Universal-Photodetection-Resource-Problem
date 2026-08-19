# WP3 — Multi-Gateway Extension Using Only Aggregate EPR and Activity

**Date:** 2026-08-19

## Executive result

The single-gateway theorem in `WP3_GATEWAY_RESOURCE_THEOREM.md` extends to an arbitrary finite set of reversible optical entrance/gateway channels, although aggregate thermodynamic budgets produce a substantially weaker high-frequency envelope.

The key distinction is:

- with one gateway (or edge-resolved resource control), a definite post-absorption escape-rate ceiling produces a Lorentzian information rolloff;
- with many gateways and only **total** EPR/activity control, a small fraction of optical traffic can be routed through very high-affinity, very fast channels. The total information transfer is still forced to vanish at high frequency, but only through a weak optimized envelope.

This establishes mathematically that **aggregate resources and edge-resolved resources are not equivalent for detector bandwidth**.

**Status:** PROVED under the independent-event proper-transducer assumptions stated below. Novelty remains OPEN.

---

# 1. Model

Let the detector possess a finite set of signal-facing gateway states indexed by \(k=1,\dots,m\).

For gateway \(k\), define:

- stationary forward optical capture traffic \(f_k>0\);
- fixed reverse optical transition rate \(d_k>0\);
- stationary gateway occupation \(\pi_k\);
- reverse optical traffic \(r_k=d_k\pi_k\);
- total escape rate from the gateway state \(\lambda_k\).

Assume every signal-facing optical edge is in the net-forward/capture regime,

\[
f_k\ge r_k>0.
\]

Define

\[
z_k=\frac{f_k}{r_k}\ge1,
\qquad
F=\sum_k f_k,
\qquad
w_k=\frac{f_k}{F}.
\]

Thus \(w_k\) is the fraction of captured optical events entering gateway \(k\).

Assume a useful total capture-throughput floor

\[
\boxed{F\ge F_*>0.}
\]

Assume the reverse optical rates are bounded by a specified microscopic optical scale

\[
\boxed{d_k\le d_{\max}<\infty.}
\]

Let total stationary entropy-production rate and total one-way activity satisfy

\[
\sigma_{\rm tot}\le\Sigma,
\qquad
\mathcal A_{\rm tot}\le\mathcal A.
\]

---

# 2. Aggregate optical EPR becomes a moment constraint

For optical edge \(k\), its stochastic entropy-production contribution is

\[
\sigma_k=(f_k-r_k)\ln\frac{f_k}{r_k}.
\]

Define

\[
g(z)=\left(1-\frac1z\right)\ln z,
\qquad z\ge1.
\]

Then

\[
\sigma_k=f_k g(z_k).
\]

Since all reversible-edge EPR contributions are nonnegative,

\[
\sum_k f_k g(z_k)
\le\sigma_{\rm tot}
\le\Sigma.
\]

Dividing by \(F\),

\[
\boxed{
\mathbb E_w[g(Z)]
=\sum_k w_k g(z_k)
\le\frac{\Sigma}{F}
\le c_*
\equiv\frac{\Sigma}{F_*}.
}
\]

Thus finite total EPR controls an average of the optical forward/reverse flux ratio, not its maximum.

**Status:** PROVED.

---

# 3. Aggregate activity becomes a weighted kinetic constraint

Because

\[
r_k=d_k\pi_k=\frac{f_k}{z_k},
\]

we have

\[
\pi_k=\frac{f_k}{d_k z_k}.
\]

The total activity contains the escape traffic from every gateway state:

\[
\mathcal A_{\rm tot}
\ge\sum_k\pi_k\lambda_k
=\sum_k\frac{f_k\lambda_k}{d_k z_k}.
\]

Since \(d_k\le d_{\max}\),

\[
\mathcal A
\ge\frac{F}{d_{\max}}
\sum_k w_k\frac{\lambda_k}{z_k}.
\]

Therefore

\[
\boxed{
\mathbb E_w\!\left[\frac{\Lambda}{Z}\right]
\le
\frac{\mathcal A d_{\max}}{F}
\le
\ell_*
\equiv
\frac{\mathcal A d_{\max}}{F_*}.
}
\]

\(\ell_*\) has units of inverse time.

**Status:** PROVED.

---

# 4. Why no maximum escape-rate bound follows

The constraints

\[
\mathbb E_w[g(Z)]\le c_*,
\qquad
\mathbb E_w[\Lambda/Z]\le\ell_*
\]

do **not** bound \(\max_k\lambda_k\).

A channel carrying a very small optical weight \(w_k\) may have simultaneously large \(z_k\) and large \(\lambda_k\), while its weighted EPR and activity costs remain finite.

This is the multi-channel analogue of the rare-fast-state mechanism. Therefore the one-gateway Lorentzian cannot survive unchanged under aggregate resource control.

---

# 5. Information available after the first gateway exit

Now impose the independent-event / proper-transducer structure:

1. captured photons form independent Poisson event substreams with fractions \(w_k\);
2. a capture into gateway \(k\) starts in that gateway state;
3. the electrical detector has no direct access to the optical modulation before the first exit from the gateway;
4. downstream processing depends on the optical signal only through the gateway-exit trajectory.

For gateway \(k\), the first-exit waiting time is

\[
T_k\sim\mathrm{Exp}(\lambda_k).
\]

If the gateway identity is retained as a label, the first-exit record is **more informative** than any downstream electrical record, so data processing gives

\[
\eta_{\mathcal I}^{\rm elec}(\omega)
\le
\eta_{\mathcal I}^{\rm exit}(\omega).
\]

For a sinusoidally modulated Poisson input, the labeled first-exit substream for channel \(k\) retains the fraction

\[
\psi_\omega(\lambda_k)
=\left|\frac{\lambda_k}{\lambda_k+i\omega}\right|^2
=\frac{\lambda_k^2}{\lambda_k^2+\omega^2}
\]

of that substream's temporal Fisher information. Since independent labeled Poisson Fisher informations add,

\[
\boxed{
\eta_{\mathcal I}^{\rm exit}(\omega)
=\mathbb E_w[\psi_\omega(\Lambda)].
}
\]

Consequently,

\[
\boxed{
\eta_{\mathcal I}^{\rm elec}(\omega)
\le
\mathbb E_w\left[
\frac{\Lambda^2}{\Lambda^2+\omega^2}
\right].
}
\]

This upper bound deliberately grants the observer the gateway label; discarding that label can only reduce information.

**Status:** PROVED for the stated independent-event Poisson class.

---

# 6. Aggregate thermokinetic high-frequency theorem

For \(x\ge0\),

\[
\frac{x^2}{1+x^2}\le\frac{x}{2},
\]

because \((x-1)^2\ge0\).

Therefore, for \(\omega\neq0\),

\[
\psi_\omega(\lambda)
\le\frac{\lambda}{2|\omega|}.
\]

Choose any threshold \(\zeta>1\) and split the optical channels into

\[
G_\zeta=\{k:z_k\le\zeta\},
\qquad
B_\zeta=\{k:z_k>\zeta\}.
\]

Because \(g(z)\) is monotone increasing,

\[
\Pr_w(B_\zeta)
\le\frac{\mathbb E_w[g(Z)]}{g(\zeta)}
\le\frac{c_*}{g(\zeta)}.
\]

On the good set,

\[
\mathbb E_w[\Lambda\,\mathbf1_{G_\zeta}]
\le
\zeta\,\mathbb E_w[(\Lambda/Z)\mathbf1_{G_\zeta}]
\le\zeta\ell_*.
\]

Thus

\[
\begin{aligned}
\eta_{\mathcal I}^{\rm elec}(\omega)
&\le
\mathbb E_w[\psi_\omega(\Lambda)\mathbf1_{G_\zeta}]
+\Pr_w(B_\zeta)\\
&\le
\frac{\zeta\ell_*}{2|\omega|}
+rac{c_*}{g(\zeta)}.
\end{aligned}
\]

Since this is valid for every \(\zeta>1\),

\[
\boxed{
\eta_{\mathcal I}^{\rm elec}(\omega)
\le
\mathcal E(\omega;c_*,\ell_*)
\equiv
\min\left\{
1,
\inf_{\zeta>1}
\left[
\frac{\zeta\ell_*}{2|\omega|}
+
\frac{c_*}{g(\zeta)}
\right]
\right\}.
}
\]

where

\[
c_*=\frac{\Sigma}{F_*},
\qquad
\ell_*=\frac{\mathcal A d_{\max}}{F_*}.
\]

This is an architecture-independent pointwise information ceiling for the stated multi-gateway event-transducer class.

**Status:** PROVED.

---

# 7. The bound necessarily vanishes at high frequency

For finite \(c_*\) and \(\ell_*\), choose for example

\[
\zeta(\omega)=\sqrt{1+|\omega|/\ell_*}.
\]

Then

\[
\frac{\zeta\ell_*}{2|\omega|}
=O(|\omega|^{-1/2})
\]

while

\[
g(\zeta)\to\infty
\]

logarithmically, so

\[
\frac{c_*}{g(\zeta)}\to0.
\]

Hence

\[
\boxed{
\lim_{|\omega|\to\infty}
\eta_{\mathcal I}^{\rm elec}(\omega)=0.
}
\]

Thus fixed reverse optical kinetics plus finite aggregate EPR/activity and finite useful capture throughput are sufficient to forbid perfect arbitrarily high-frequency information transfer, even when no individual gateway escape rate is bounded.

**Status:** PROVED.

---

# 8. Worst-case asymptotic scaling

For large \(\zeta\),

\[
g(\zeta)\sim\ln\zeta.
\]

In the high-frequency regime where the optimized first term is small, approximate

\[
\mathcal E
\lesssim
\frac{\ell_*\zeta}{2|\omega|}
+
\frac{c_*}{\ln\zeta}.
\]

Setting the derivative to zero gives the asymptotic stationarity equation

\[
\boxed{
\zeta(\ln\zeta)^2
\sim
\frac{2c_*|\omega|}{\ell_*}.
}
\]

Let

\[
X=\frac{2c_*|\omega|}{\ell_*}.
\]

Writing \(y=\ln\zeta\), the solution of \(e^y y^2=X\) is

\[
\boxed{
y=2W\!\left(\frac{\sqrt X}{2}\right)},
\]

where \(W\) is the Lambert W function. Therefore the optimized envelope behaves parametrically as

\[
\boxed{
\mathcal E(\omega)
=O\!\left(
\frac{c_*}
{W\!\left(\sqrt{c_*|\omega|/(2\ell_*)}\right)}
\right)
=O\!\left(\frac{c_*}{\ln|\omega|}\right)
}
\]

up to logarithmic corrections and constants.

The slow logarithmic worst-case decay has a clear interpretation: aggregate EPR permits a shrinking fraction of photons to use exponentially high-affinity fast pathways.

**Status:** ASYMPTOTIC DERIVATION / VERIFIED scaling; exact optimized envelope is the theorem.

---

# 9. Comparison with the single-gateway result

## Single gateway

A single flux ratio \(z\) must itself satisfy

\[
g(z)\le\Sigma/f_*.
\]

This directly bounds the gateway occupation and escape rate, giving

\[
\eta_{\mathcal I}(\omega)
\lesssim
\frac{\Lambda_*^2}{\Lambda_*^2+\omega^2},
\]

a Lorentzian \(\omega^{-2}\) tail.

## Multiple gateways with aggregate budgets only

Only the average

\[
\mathbb E_w[g(Z)]
\]

is controlled. Individual \(z_k\) can be arbitrarily large on sufficiently low-weight channels. The guaranteed envelope can therefore be much weaker, asymptotically only logarithmic in the worst-case bound derived above.

This yields an important design/theorem distinction:

\[
\boxed{
\text{edge-resolved thermodynamic control}
\gg
\text{aggregate EPR control}
\quad\text{for bounding broadband information transfer.}
}
\]

---

# 10. Edge-resolved corollary

If a stronger assumption holds for every signal-facing channel,

\[
\frac{\sigma_k}{f_k}=g(z_k)\le c_{\rm edge},
\]

then

\[
z_k\le Z_{\rm edge}=g^{-1}(c_{\rm edge})
\]

for all \(k\). Activity then gives a flux-weighted mean escape-rate bound

\[
\mathbb E_w[\Lambda]
\le
\frac{\mathcal A d_{\max}Z_{\rm edge}}{F_*}.
\]

This is much stronger than aggregate EPR control, although a maximum individual escape rate still need not be finite without a lower bound on each channel's optical weight.

---

# 11. Why this does not conflict with first-passage TURs

First-passage TURs generally lower-bound fluctuations of a first-passage time or counting observable using integrated entropy production and/or integrated activity. Here the object is different:

- the input is a temporally modulated optical Poisson process;
- each capture channel acts as a random-delay transducer;
- information is measured about the external modulation parameter;
- the theorem upper-bounds the fraction of optical Fisher information surviving to a downstream record at each modulation frequency.

First-passage results remain important adjacent theory, but the present derivation is not merely a coefficient-of-variation bound.

---

# 12. Remaining physical caveats

The theorem still assumes:

- independent low-overlap signal events;
- Markovian exponentially distributed gateway exit times;
- fixed finite reverse optical rates \(d_k\);
- net-forward optical channels \(f_k\ge r_k\);
- all signal influence reaches the electrical record through the gateway-exit trajectory;
- no coherent quantum information bypasses the classical gateway;
- stationary stochastic EPR is an appropriate accounting of the signal-facing optical transitions.

A fully quantum fixed-frequency optical mode requires replacing these assumptions by a Hamiltonian/input-output formulation.

---

# 13. Next target

The classical Markov theory now has a hierarchy:

1. **No source-band constraint:** no finite all-frequency information-bandwidth objective.
2. **Aggregate activity + net EPR without fixed optical reverse kinetics:** rare-fast counterexample.
3. **One fixed reversible optical gateway:** strong Lorentzian information bound.
4. **Many fixed reversible optical gateways + aggregate EPR/activity:** weaker but universal optimized high-frequency envelope.
5. **Quantum detector:** OPEN; likely requires an interaction-Hamiltonian or system-bath coupling resource.

The next high-value task is to convert this hierarchy into a formal no-go-and-repair theorem and then determine the quantum analogue.