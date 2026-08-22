from pathlib import Path

main_src = Path("energy_survival_temporal_fisher_rev9_prxq.tex")
main_dst = Path("energy_survival_temporal_fisher_rev10_prxq.tex")
spec_src = Path("rev9_spectral_theorems.tex")
spec_dst = Path("rev10_spectral_theorems.tex")

main = main_src.read_text(encoding="utf-8")
spec = spec_src.read_text(encoding="utf-8")


def replace_once(text: str, old: str, new: str) -> str:
    count = text.count(old)
    assert count == 1, f"Expected exactly one match, found {count}: {old!r}"
    return text.replace(old, new, 1)


# Rev10 is a narrow referee-closure revision on top of Rev9.  It keeps the
# finite-copy theorem, continuum survival theorem, Herglotz theorem, and
# extremizer theorem unchanged, but closes two scope/formal issues and adds a
# clean achievability witness proving the high-retention divergence exponent
# is sharp up to constants.
main = replace_once(
    main,
    r"\input{rev9_spectral_theorems.tex}",
    r"\input{rev10_spectral_theorems.tex}",
)
main = replace_once(
    main,
    "A second resource effect appears when the detector measurement is held fixed across frequencies.",
    "A second resource effect appears when one fixed one-copy detector POVM is held fixed across frequencies.",
)
main = replace_once(
    main,
    "thus approaching unit retention at any nonzero frequency requires divergent mean excess energy.",
    "thus approaching unit retention at any nonzero frequency requires divergent mean excess energy.  A finite-chain sine-profile family attains the same $(1-q)^{-1/2}$ scaling, so this divergence exponent is sharp.",
)

# Continuum Bochner step: normalized positive definiteness alone does not imply
# the standard finite-measure representation on R.  State continuity at zero
# explicitly (which also implies continuity everywhere for a pd function).
spec = replace_once(
    spec,
    "In a controlled periodic-to-continuum family whose one-copy common-measurement retention functions converge while preserving normalized positive definiteness, Bochner's theorem gives\n$R(\\nu)=\\int\\cos(\\nu t)J(\\dd t)$.",
    "In a controlled periodic-to-continuum family whose one-copy common-measurement retention functions converge to a normalized positive-definite function that is continuous at the origin, Bochner's theorem gives\n$R(\\nu)=\\int\\cos(\\nu t)J(\\dd t)$.",
)

sharpness = r'''

\begin{proposition}[Sharp high-retention exponent]
\label{prop:sharp-high-retention-exponent}
The exponent $1/2$ in Eq.~\eqref{eq:high-retention-divergence} is optimal up to a multiplicative constant.  For every integer $L\geq2$, define the normalized finite-chain amplitudes
\begin{equation}
 a_n^{(L)}=\sqrt{\frac{2}{L+1}}
 \sin\!\left(\frac{(n+1)\pi}{L+1}\right),
 \qquad n=0,\ldots,L-1,
 \label{eq:sine-profile}
\end{equation}
with sector populations $q_n^{(L)}=|a_n^{(L)}|^2$ and zero population above $L-1$.  Under the canonical phase POVM,
\begin{align}
 R_L(1)&=\cos^2\!\left(\frac{\pi}{L+1}\right),
 \label{eq:sine-retention}\\
 \bar n_L&=\frac{L-1}{2}.
 \label{eq:sine-mean}
\end{align}
Consequently
\begin{equation}
 \bar n_L
 =\frac{\pi}{2\arccos\sqrt{R_L(1)}}-1
 =\frac{\pi}{2\sqrt{1-R_L(1)}}[1+o(1)].
 \label{eq:sine-sharpness}
\end{equation}
Thus there exist normalized semibounded sources and one fixed one-copy POVM for which the energetic cost of $R(1)\uparrow1$ scales as $(1-R)^{-1/2}$.  The divergence exponent in Corollary~\ref{cor:high-retention} is therefore sharp, although the optimal asymptotic constant is not determined here.
\end{proposition}

\begin{proof}
Normalization follows from the standard finite sine sum.  Writing $\vartheta=\pi/(L+1)$, the amplitudes obey the path-eigenvector recursion
\begin{equation}
 a_{n-1}^{(L)}+a_{n+1}^{(L)}
 =2\cos\vartheta\,a_n^{(L)},
\end{equation}
with $a_{-1}^{(L)}=a_L^{(L)}=0$.  Multiplying by $a_n^{(L)}$, summing over $n$, and using normalization gives
$\sum_{n=0}^{L-2}a_n^{(L)}a_{n+1}^{(L)}=\cos\vartheta$.  The canonical phase POVM therefore has first-harmonic retention equal to the squared adjacent-amplitude overlap, proving Eq.~\eqref{eq:sine-retention}.  Since
$q_n^{(L)}=q_{L-1-n}^{(L)}$, reflection symmetry gives Eq.~\eqref{eq:sine-mean}.  Eliminating $L$ yields the first equality in Eq.~\eqref{eq:sine-sharpness}; the second follows from $\arccos\sqrt{1-\epsilon}\sim\sqrt{\epsilon}$.  Finite-support sine states are established phase-estimation constructions~\cite{BerryWiseman2000}; their role here is only to witness achievability of the new retention--energy divergence exponent.
\end{proof}
'''

anchor = (
    "The $m=1$ term gives $A(q)\\geq q$, so the original pointwise law is contained in "
    "Eq.~\\eqref{eq:high-retention-energy}; the cross-harmonic constraint becomes strictly stronger "
    "once additional positive cosine terms enter."
)
assert spec.count(anchor) == 1
spec = spec.replace(anchor, sharpness + "\n\n" + anchor, 1)

assert "continuous at the origin" in spec
assert r"\begin{proposition}[Sharp high-retention exponent]" in spec
assert "one fixed one-copy detector POVM is held fixed across frequencies" in main
assert "this divergence exponent is sharp" in main
assert r"\input{rev10_spectral_theorems.tex}" in main
assert r"\input{rev9_spectral_theorems.tex}" not in main

spec_dst.write_text(spec, encoding="utf-8")
main_dst.write_text(main, encoding="utf-8")
print(f"Wrote {spec_dst}")
print(f"Wrote {main_dst}")
