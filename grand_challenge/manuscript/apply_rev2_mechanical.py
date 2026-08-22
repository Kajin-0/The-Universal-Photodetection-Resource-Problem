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


def unwrap_balanced_command(source: str, command: str) -> str:
    """Replace every command{balanced content} by balanced content."""
    needle = command + "{"
    out = []
    pos = 0
    count = 0
    while True:
        start = source.find(needle, pos)
        if start < 0:
            out.append(source[pos:])
            break
        out.append(source[pos:start])
        content_start = start + len(needle)
        depth = 1
        i = content_start
        while i < len(source) and depth:
            if source[i] == "{" and (i == 0 or source[i - 1] != "\\"):
                depth += 1
            elif source[i] == "}" and (i == 0 or source[i - 1] != "\\"):
                depth -= 1
            i += 1
        if depth != 0:
            raise ValueError(f"Unbalanced braces while unwrapping {command} at {start}")
        out.append(source[content_start : i - 1])
        pos = i
        count += 1
    repaired = "".join(out)
    return repaired, count


# APS REVTeX production guidance excludes \boxed markup.  Remove only the
# presentation wrapper; the enclosed mathematical expression is unchanged.
text, n_boxed = unwrap_balanced_command(text, r"\boxed")
assert n_boxed > 0, "Expected boxed expressions were not found"
assert r"\boxed{" not in text, "Boxed markup remains after mechanical repair"

# Rev2 is mechanical only: theorem statements, mathematical expressions,
# citations, and prose are otherwise unchanged.
dst.write_text(text, encoding="utf-8")
print(f"Wrote {dst}; unwrapped {n_boxed} boxed expressions")
