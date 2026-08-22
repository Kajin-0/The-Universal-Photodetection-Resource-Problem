from pathlib import Path

path = Path("energy_survival_temporal_fisher_rev9_prxq.tex")
text = path.read_text(encoding="utf-8")

start = text.index(r"\begin{abstract}")
end = text.index(r"\end{abstract}", start)

abstract = r'''\begin{abstract}
Temporal resolution is usually summarized by a response time or transfer function, but those quantities do not determine how much information about a time-dependent source reaches an accessible record.  We study a fixed quantum excitation emitted at a latent random time, with weak temporal structure encoded in Fourier coefficients of the random-time distribution.  For harmonic $k$, every joint measurement on any finite number $N$ of independently encoded excitations obeys the operational bound $\Tr F_N^{(k)}/N\leq\sum_{m\geq k}q_m$, where the right-hand side is the excitation population above the corresponding semibounded generator gap.  Controlled periodic-to-continuum limits give the survival law $R(\nu)\leq\Pr(\Omega\geq\nu)$.  For one fixed one-copy POVM, the entire multi-harmonic retention sequence is additionally a positive-definite Herglotz sequence.  Combining that cross-frequency consistency with the energy tails yields $\bar E^+\geq\hbar\nu A(q)$, where $q=R(\nu)$ and $A(q)\sim[2(1-q)]^{-1/2}$; thus approaching unit retention at any nonzero frequency requires divergent mean excess energy.  On the full contiguous pure-sector chain, exact one-copy saturation is completely classified: it occurs exactly for mixtures of geometric sector laws, equivalently Hausdorff-moment survival sequences, and one source-adapted POVM then saturates every harmonic simultaneously.  Exponential mixtures generate a completely monotone continuum equality cone.  The modewise law is inherited by independent quantum-marked Poisson sources under arbitrary parameter-independent source-to-field and detector dynamics, while an explicit coherent-sideband counterexample shows why arbitrary parameter-dependent waveform synthesis requires additional control-resource accounting.
'''

text = text[:start] + abstract + text[end:]
assert text.count(r"\begin{abstract}") == 1
assert "positive-definite Herglotz sequence" in text
assert "approaching unit retention" in text
path.write_text(text, encoding="utf-8")
print(f"Compressed abstract in {path}")
