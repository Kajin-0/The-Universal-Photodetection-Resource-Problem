# WP11 — Global Static Nonidentifiability of the Ideal Paralyzable Timestamp Process

**Status:** exact corollary of the classical extended-dead-time interval transform. The two-branch count-rate ambiguity is well known; the purpose here is to state the stronger complete-timestamp statistical equivalence and connect it to WP07's Fisher zero. Do not claim priority without a dedicated historical search.

## 1. Starting point

For a homogeneous Poisson input of rate `lambda` passed through an ideal deterministic paralyzable / extended dead time `tau`, the recorded events form a stationary renewal process.

The classical Laplace transform of the inter-recording interval `D` is

\[
\psi_\lambda(s)
=\frac{\lambda e^{-(\lambda+s)\tau}}
{s+\lambda e^{-(\lambda+s)\tau}}.
\]

This transform goes back to classical extended-dead-time renewal theory (Takacs/Feller/Muller literature; see J. W. Muller, *Dead-time problems*, Nucl. Instrum. Methods 112, 47--57 (1973), DOI `10.1016/0029-554X(73)90773-8`, and earlier BIPM reports).

Define the observed stationary event rate

\[
\boxed{r(\lambda)=\lambda e^{-\lambda\tau}.}
\]

Then the interval transform simplifies exactly to

\[
\boxed{
\psi_\lambda(s)
=\frac{r(\lambda)e^{-s\tau}}
{s+r(\lambda)e^{-s\tau}}.
}
\]

Thus the **entire inter-recording interval distribution depends on `lambda` only through the scalar `r(lambda)`** when `tau` is fixed.

---

## 2. Exact equality of complete stationary timestamp laws

Let `lambda_1` and `lambda_2` satisfy

\[
\boxed{
lambda_1e^{-lambda_1\tau}
=lambda_2e^{-lambda_2\tau}=r.
}
\]

Then

\[
\psi_{\lambda_1}(s)=\psi_{\lambda_2}(s)
\qquad\forall s\ge0.
\]

Hence the iid renewal-interval laws are identical.

A stationary simple renewal point process is determined by its interval law together with the equilibrium origin convention. Since the mean interval is likewise identical,

\[
E[D]=1/r,
\]

the complete stationary output point-process distributions coincide:

\[
\boxed{
\mathcal L_{\lambda_1}(Y)
=\mathcal L_{\lambda_2}(Y).
}
\]

This equality concerns the **full accessible timestamp record**, not merely its mean count rate or a finite set of moments.

Therefore, within the ideal paralyzable model with known `tau`, no estimator using stationary output timestamps alone can distinguish `lambda_1` from `lambda_2` if they lie on the same observed-rate level set.

---

## 3. The two Lambert-W branches

Write

\[
\rho=\lambda\tau,
\qquad
q=r\tau.
\]

Then

\[
q=\rho e^{-\rho}.
\]

For

\[
0<q<e^{-1},
\]

there are exactly two positive solutions:

\[
\boxed{
\rho_-=-W_0(-q),
\qquad
\rho_+=-W_{-1}(-q),
}
\]

with

\[
0<\rho_-<1<\rho_+.
\]

Equivalently,

\[
\boxed{
\lambda_-=-\frac1\tau W_0(-r\tau),
\qquad
\lambda_+=-\frac1\tau W_{-1}(-r\tau).
}
\]

The ordinary count-rate ambiguity between these branches is well known. For example, the Lambert-W dead-time correction literature explicitly notes the two solutions and normally chooses the principal branch by assuming operation below the paralysis maximum (e.g. DOI `10.1186/s40658-020-00296-w`).

The stronger statement here is that, for the ideal timestamp model, **higher-order stationary timestamp statistics do not remove the branch ambiguity**, because the complete renewal law itself is the same.

---

## 4. Branch coalescence at the paralysis maximum

The two branches meet at

\[
\boxed{
\rho=1,
\qquad
r_{\max}=\frac{1}{e\tau}.
}
\]

Since

\[
\frac{dr}{d\lambda}
=e^{-\rho}(1-\rho),
\]

the mapping from incident rate to output experiment has a fold singularity there.

WP07's exact result

\[
\boxed{G_1(0)=0}
\]

is therefore the local Fisher manifestation of this global two-to-one statistical map.

The DC score vanishes not because only the first moment has an extremum, but because the complete stationary output law moves only through `r(lambda)`, whose derivative vanishes at the branch-coalescence point.

---

## 5. Static ambiguity versus dynamic identifiability

The global equivalence above applies to **homogeneous/static** illumination.

For a time-dependent intensity

\[
\lambda_\epsilon(t)=\lambda[1+\epsilon u(t)],
\]

the exact mean recorded intensity is

\[
r_\epsilon(t)
=\lambda_\epsilon(t)
\exp\!\left[-\int_{t-\tau}^{t}\lambda_\epsilon(s)ds\right].
\]

Temporal structure enters through the finite-memory integral, not only through the static scalar `r(lambda)`.

At `rho=1`, WP07 proves

\[
G_1(0)=0
\]

but

\[
\boxed{G_1(\omega)>0\quad\text{for every }\omega\ne0.}
\]

Thus temporal modulation **breaks the static branch degeneracy**.

This yields a clean conceptual distinction:

\[
\boxed{
\text{static complete-record nonidentifiability}
\quad\not\Rightarrow\quad
\text{dynamic waveform nonidentifiability}.
}
\]

A detector can contain no local information about the baseline intensity direction while still carrying substantial information about changes in time.

---

## 6. Information-geometric interpretation

Let the family of homogeneous output experiments be parameterized by `lambda`.

Because

\[
Q_\lambda=Q_{r(\lambda)},
\]

the statistical model is a one-dimensional curve traced twice in output-distribution space for `0<r<r_max`.

At `lambda*tau=1`, the tangent vector of that curve with respect to `lambda` vanishes.

Hence the Fisher metric pulled back to the incident-rate coordinate is singular there:

\[
F_{\lambda\lambda}^{\rm out}=0.
\]

Finite-frequency temporal tangents point outside this collapsed static direction and need not vanish.

This geometric picture may be useful in Paper 2, but it should not be overformalized unless it helps the final exposition.

---

## 7. Prior-art boundary

Known / old:

- `r=lambda exp(-lambda tau)` for paralyzable dead time;
- the maximum at `lambda*tau=1`;
- two true-rate solutions below the maximum;
- Lambert-W inversion and branch ambiguity;
- the classical inter-recording interval transform for extended dead time;
- renewal-process characterization of the output.

Potentially less commonly stated, but **not yet certified novel**:

> the two Lambert-W branches are not merely mean-rate ambiguous; they are exactly equivalent as complete stationary timestamp experiments in the ideal deterministic Type-II model.

Because this follows rapidly from a classical interval-transform formula, it should be presented as an illuminating corollary unless a deeper historical search shows that the full-law equivalence has not been noted previously.

The genuinely stronger Paper-2 result remains the **dynamic escape from the static equivalence**, quantified by the temporal Fisher spectrum.

---

## 8. Practical consequence

If an ideal paralyzable detector is operated without an external prior telling the analyst which side of the paralysis maximum it occupies, stationary timestamp data cannot resolve the true constant incident rate branch.

Possible ways to break the ambiguity require an additional resource, for example:

- known attenuation / flux stepping;
- an independent monitor channel;
- a detector state/mark that exposes hidden arrivals;
- controlled temporal modulation.

The last option is directly connected to WP07: nonzero temporal frequencies restore local distinguishability even at the branch-coalescence point.

---

## 9. Research value

WP11 strengthens the conceptual narrative of Paper 2:

1. paralyzable saturation creates an exact global static identification failure;
2. the local DC Fisher zero is the differential signature of that failure;
3. temporal modulation restores information;
4. therefore detector information loss must be treated as a **task-resolved spectrum**, not inferred from the static count-rate curve.

This is an interpretation/corollary layer around WP07, not a substitute for the general-channel theorem or the exact Type-II spectral results.
