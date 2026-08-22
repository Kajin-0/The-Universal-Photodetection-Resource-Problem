from pathlib import Path

src = Path("energy_survival_temporal_fisher_rev1.tex")
dst = Path("energy_survival_temporal_fisher_rev2.tex")

text = src.read_text(encoding="utf-8")

anchor = r"\usepackage{hyperref}" + "\n"
assert anchor in text, "Expected hyperref preamble anchor not found"
assert r"\begin{theorem}" in text, "Expected theorem environment not found"
assert r"\begin{corollary}" in text, "Expected corollary environment not found"
assert r"\begin{proof}" in text, "Expected proof environment not found"

insertion = r"""\newtheorem{theorem}{Theorem}
\newtheorem{corollary}{Corollary}
% REVTeX permits \newtheorem but APS production guidance excludes amsthm.
% REVTeX 4.2 already defines \endproof but not the opening \proof command.
\providecommand{\proof}{\par\noindent\textit{Proof.}\ }
"""

text = text.replace(anchor, anchor + insertion, 1)

# Rev2 is mechanical only: no theorem statement, equation, citation, or prose is changed.
dst.write_text(text, encoding="utf-8")
print(f"Wrote {dst}")
