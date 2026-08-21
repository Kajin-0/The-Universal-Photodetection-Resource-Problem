# WP16 — Hostile Prior-Art Audit of Random Type-II Identifiability

**Status:** major positioning correction. The generalized random-Type-II stochastic-process formulas used in WP13/WP15 have substantially closer and older prior art than the existing notes stated. The deterministic-recovery Fisher singularity and full-law aliasing uniqueness remain plausible derived novelty candidates, but must now be presented as information-theoretic/identifiability consequences of classical counter and `M/G/infinity` structure rather than as new renewal or correlation formulas.

## 1. Scope of this audit

This round tested the strongest post-WP12 claims against old Type-II counter theory, `M/G/infinity` busy-cycle theory, inverse queueing, and photon-correlation dead-time literature.

The target model is unchanged:

- incident events are homogeneous Poisson with rate `lambda`;
- every incident event starts an iid positive recovery/dead interval `T` with CDF `F` and mean `m`;
- the detector is dead whenever at least one event-generated interval is active;
- registered events are arrivals finding the system empty, equivalently starts of `M/G/infinity` busy clusters.

The strongest current candidate conclusions are

\[
G_*(0)=0\quad\Longleftrightarrow\quad T=m\ \text{a.s.}
\]

at `lambda*m=1`, and

\[
\text{two distinct equal-output-rate branches have identical complete registered-timestamp laws}
\quad\Longleftrightarrow\quad T=m\ \text{a.s.}
\]

for fixed known recovery law.

This audit materially narrows what surrounding ingredients can be claimed.

---

## 2. Random Type-II recovery itself is old

Dvurecenskij and Ososkov, **“Note on type II counter problem,”** *Aplikace matematiky* 29, 237–249 (1984), DOI `10.21136/AM.1984.104092`, formulate essentially the same generalized Type-II model:

- a recurrent primary process of incident particles;
- iid random impulse/recovery durations independent of the arrivals;
- every incident particle starts an impulse;
- a particle is registered iff all previous impulses have expired.

They explicitly identify the registered-particle process as recurrent and study the distribution/Laplace transform of the distance between successive registered particles. Their Poisson-primary Example 1 allows an **arbitrary impulse-duration distribution** and gives an explicit transform. They cite still earlier work by Takacs, Pollaczek, Smith, Pyke, Afanaseva and Mikhailova, and others.

Therefore Paper 2 must not claim novelty for:

- iid random Type-II/paralyzable recovery;
- the `M/G/infinity` representation;
- renewal structure of registered cluster starts;
- the inter-registration law or its Laplace-transform characterization in general.

Relevant older foundations include Pyke, *Ann. Math. Stat.* 29, 737–754 (1958), and Takacs, *Introduction to the Theory of Queues* (1962).

---

## 3. The WP13 renewal-density formula is explicitly classical

WP13 uses

\[
U_\lambda(t)=\lambda F(t)e^{-\lambda A(t)},
\qquad
A(t)=\int_0^t[1-F(v)]\,dv=E[\min(T,t)].
\]

This should no longer be described merely as a formula whose “structure is classical.” It is directly the classical `M/G/infinity` **busy-cycle renewal density**.

For an `M/G/infinity` system initially empty,

\[
p_{00}(t)
=\exp\!\left[-\lambda\int_0^t(1-F(v))\,dv\right]
=e^{-\lambda A(t)}.
\]

The renewal function of busy-period starts satisfies the standard Takacs/Ferreira relation

\[
R'(t)=\lambda F(t)p_{00}(t).
\]

Hence

\[
\boxed{R'(t)=\lambda F(t)e^{-\lambda A(t)}=U_\lambda(t).}
\]

A modern accessible statement is M. A. M. Ferreira, **“M|G|∞ queue busy cycle renewal function for some particular service time distributions,”** *Quantitative Methods in Economics* (2004), pp. 42–47; the same formula is reproduced in arXiv:2210.11480. Ferreira credits the underlying `M/G/infinity` formulas to Takacs and related classical queueing work.

### Mandatory positioning correction

The exact renewal-density identity itself is **not a Paper-2 novelty claim**. It is a classical input to the Fisher/identifiability argument.

Recommended manuscript wording, if used:

> Using the classical `M/G/infinity` busy-cycle renewal density `U_lambda(t)=lambda F(t) exp[-lambda A(t)]`, we derive the following Fisher-identifiability consequences for generalized Type-II photodetection.

---

## 4. WP15's random-Type-II pair-correlation identity also has direct prior art

WP15 derived

\[
\boxed{g_Y^{(2)}(t)=F(t)e^{\lambda R(t)},}
\qquad
R(t)=m-A(t)=E[(T-t)_+].
\]

A much closer predecessor is V. V. Apanasovich and S. V. Paltsev,
**“Distortion of photon-correlation functions in detection systems with paralyzable dead-time effects,”** *J. Opt. Soc. Am. B* 12, 1550–1554 (1995), DOI `10.1364/JOSAB.12.001550`.

They derive the registered second-order product density for a Poisson input passed through a paralyzable detector with an **arbitrary random dead-time distribution**. Specializing their Eq. (22) to a stationary Poisson intensity `lambda`, writing their dead-time CDF as our `F`, and taking positive lag `t`, gives

\[
\rho_Y^{(2)}(0,t)
=\lambda^2F(t)
\exp[-\lambda m]
\exp[-\lambda A(t)].
\]

The stationary registered intensity is the classical

\[
r=\lambda e^{-\lambda m}.
\]

Therefore

\[
\frac{\rho_Y^{(2)}(0,t)}{r^2}
=F(t)e^{\lambda[m-A(t)]}
=F(t)e^{\lambda R(t)},
\]

which is exactly the WP15 normalized pair-correlation identity.

### Consequence

The identity

\[
g_Y^{(2)}(t)=F(t)e^{\lambda E[(T-t)_+]}
\]

is **not a safe novelty claim**. It is a direct stationary specialization/normalization of the 1995 random-paralyzable correlation formula.

Larsen and Kostinski (2009) already supplied an additional independent warning that pair-correlation dead-time inversion is established methodology.

The one-lag rearrangement

\[
\lambda
=\frac{\ln[g_Y^{(2)}(t)/F(t)]}{E[(T-t)_+]}
\]

for `F(t)>0` and `E[(T-t)_+]>0` remains a useful operational corollary, but because it follows algebraically from an old correlation identity it should **not** be elevated as a standalone novelty theorem absent evidence that the inversion/uniqueness observation itself carries independent significance.

---

## 5. Inverse `M/G/infinity` literature is substantial

The inverse problem of learning hidden service/recovery distributions from indirect `M/G/infinity` observations is old.

Important examples include:

- L. L. George and A. C. Agrawal, **“Estimation of a hidden service distribution of an M/G/infinity system,”** *Naval Research Logistics Quarterly* 20, 549–555 (1973), DOI `10.1002/nav.3800200314`;
- P. Hall and J. Park, **“Nonparametric inference about service time distribution from indirect measurements,”** *J. R. Stat. Soc. B* 66 (2004), DOI `10.1111/j.1467-9868.2004.B5725.x`, including inference from busy-period/cluster observations;
- later nonparametric `M/G/infinity` inference literature using queue-length, busy-period, and indirect output observations.

These observation schemes are not all identical to retaining only cluster-start timestamps, so they do not automatically settle the WP13 fixed-`F` theorem. But they eliminate any broad claim that recovery-law inference or output-flow identifiability is new.

---

## 6. A 1973 inverse-output-flow paper is an unresolved historical blocker

Dvurecenskij and Ososkov explicitly cite:

L. G. Afanaseva and I. V. Mikhailova,
**“On recovering characteristics of some queueing systems from the output flow”**
(Russian: `О восстановлении характеристик некоторых систем массового обслуживания по выходящему потоку`),
*Proceedings of the Mathematical Faculty, Voronezh State University*, issue 9 (1973), pp. 132–138.

Bibliographic records are confirmed, but a readable full text was not located in this audit.

Because the title is directly about recovering queue characteristics from the output flow and the paper is cited inside the classical Type-II/`M/G/infinity` literature, it is a **high-priority unresolved novelty risk**. No priority language for the WP13 identifiability theorem is justified until this source, or a reliable abstract/review of its theorem content, is checked.

Absence of an online full text is not evidence of novelty.

---

## 7. What remains potentially distinctive after this audit

### 7.1 Deterministic recovery as the unique DC Fisher singularity

At the common mean-rate maximum `lambda*m=1`, all equal-mean recovery laws satisfy

\[
r'(\lambda)=0.
\]

The complete registered-timestamp result

\[
\boxed{G_*(0)=0\iff T=m\ \text{a.s.}}
\]

has **not** been located in the searched counter, queueing, correlation, renewal-Fisher, or inverse-queueing literature.

However, its proof is now correctly understood as a short synthesis of:

1. the classical busy-cycle renewal density;
2. the derivative
   \[
   \dot U_*(t)=U_*(t)[1-A(t)/m];
   \]
3. standard renewal-process Fisher information/DQM;
4. the support identity
   \[
   m-A(t)=E[(T-t)_+].
   \]

Thus the novelty target is the **Fisher singularity characterization and detector interpretation**, not the underlying stochastic-process formula.

### 7.2 Deterministic recovery as the unique full-law branch-aliasing case

For two distinct incident rates with equal conventional output rate,

\[
\lambda_1e^{-\lambda_1m}=\lambda_2e^{-\lambda_2m},
\]

equality of complete cluster-start timestamp laws implies equality of the classical renewal densities. For every `t` with `F(t)>0`,

\[
\ln\frac{\lambda_1}{\lambda_2}
=(\lambda_1-\lambda_2)A(t).
\]

Equal mean rates separately give the same equation with `m` in place of `A(t)`, hence `A(t)=m` throughout the relevant support and therefore `T=m` a.s.

The converse is the familiar deterministic Type-II branch aliasing.

No exact historical statement of this **iff** characterization was located in the current search.

Again, it is an elementary but nontrivial corollary of classical formulas. Its significance is strongest when tied to the information geometry:

- deterministic recovery gives a global two-to-one static experiment map;
- the two branches coalesce at `lambda*m=1`;
- the vanishing DC Fisher tangent is the local signature of that fold;
- every nondegenerate recovery law destroys the collapse by retaining interval-shape information.

### 7.3 The recovery-shape Fisher witness

WP14's `W_s` lower bound remains a plausible detector-specific information result, but it too is built from standard stop-loss transforms, renewal Laplace identities, and the standard information inequality. It should be presented as a quantitative consequence of the Fisher singularity theorem, not as invention of a new stochastic-process transform.

---

## 8. Revised novelty hierarchy

After this audit the safest hierarchy is:

### Strongest candidate Paper-2 contribution

1. **General autonomous-channel Fisher-spectrum theorem (WP10)** plus exact high-flux hidden-memory consequences.

### Strong physical theorem candidates

2. **Continuous deterministic Type-II spectral survival (WP07):**
   \[
   G_1(0)=0,\quad G_1(\omega)>0\ (\omega\ne0),\quad G_1(\infty)=e^{-1}.
   \]
3. **Deterministic-recovery information singularity inside the iid Type-II class (WP13):**
   \[
   G_*(0)=0\iff T=m\ \text{a.s.}
   \]
   plus the corresponding full-law branch-aliasing uniqueness.

### Supporting/operational consequences, not lead novelty claims

4. rate-versus-shape Fisher decomposition;
5. `W_s` recovery-shape witness;
6. pair-correlation operational inversion.

The last item is now explicitly demoted because the underlying pair-correlation identity is already contained in Apanasovich–Paltsev 1995.

---

## 9. Mandatory claim corrections for any manuscript

Do **not** claim novelty for:

- `U_lambda(t)=lambda F(t) exp[-lambda A(t)]`;
- random-Type-II renewal/busy-cycle theory;
- the arbitrary-random-dead-time registered pair-correlation identity;
- generic recovery-law inference in `M/G/infinity` systems;
- generic pair-correlation dead-time inversion;
- renewal-process Fisher information or rate-vs-shape information decomposition.

Preferred language:

> Classical Type-II and `M/G/infinity` theory gives the complete renewal and correlation structure. We use that structure to expose a detector-information singularity that the conventional saturation curve hides: among iid recovery laws of a fixed mean, deterministic recovery is uniquely capable of collapsing the complete static cluster-start experiment at the common paralysis maximum.

No `first`, `unprecedented`, or priority statement is currently warranted.

---

## 10. Research decision

This prior-art correction **does not kill Paper 2**. It improves its focus.

The random-recovery branch should not be sold as new queueing or correlation theory. Its value is as a sharp physical consequence of the general Fisher-channel framework:

\[
\text{same conventional paralysis curve}
\not\Rightarrow
\text{same complete information channel},
\]

with deterministic recovery forming a unique information-singular boundary.

That result is substantially more defensible when explicitly built on, and credited to, classical counter/queueing formulas.

---

## 11. Next gates

1. **Finish the historical inverse-output audit**, especially Afanaseva–Mikhailova (1973), before assigning novelty confidence to the deterministic-uniqueness theorem.
2. Search older photon-correlation and nuclear-counting literature for explicit source-rate recovery from random paralyzable pair correlations; do not assume the one-lag inversion wording is new.
3. Harden WP10 with publication-grade DQM-under-Markov and translation-multiplier references and measurable trajectory-space wording.
4. Only after those gates revisit the variance-insufficiency direction. If pursued, add a durable reproducible same-mean/same-variance counterexample rather than relying on handoff-only gamma/lognormal numerics.
5. Keep WP08 provisional until its high-frequency residue proof is strengthened.
