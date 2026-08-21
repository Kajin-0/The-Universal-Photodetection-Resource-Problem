#!/usr/bin/env python3
"""Generate the Physical Review Applied submission copy from Rev10."""
from pathlib import Path

SRC = Path('event_resource_theorem_rev10.tex')
OUT = Path('event_resource_theorem_rev10_prapplied.tex')
s = SRC.read_text(encoding='utf-8')
assert r'\author{Anonymous}' in s
assert r'\affiliation{Anonymous}' in s
assert r'\input{section_worked_irf_example_rev10}' in s
assert s.count(r'\appendix') == 1
assert r'\section*{Data Availability}' not in s

compliance = r'''
% APS SUBMISSION TODO -- REQUIRED BEFORE ACTUAL SUBMISSION:
% Add a truthful Acknowledgments disclosure of substantive AI use that states
% (i) the AI tool name/version, (ii) how it assisted, and (iii) how the HUMAN
% author directed and verified its output. See submission/AI_DISCLOSURE_DRAFT_REV10.md.

\section*{Data Availability}
No new experimental data were generated in this study. The worked example in Sec.~\ref{sec:workedIRF} uses an approximate graphical digitization of the normalized detector impulse-response curves published in Fig.~3 of Spinelli \emph{et al.}, IEEE Journal of Quantum Electronics \textbf{34}, 817--821 (1998), DOI 10.1109/3.668769. The digitized points and analysis script are included with the manuscript source files. All other figures can be reproduced directly from the presented equations.

'''
out = s.replace('\\appendix\n', compliance + '\\appendix\n', 1)
assert out.count(r'\section*{Data Availability}') == 1
assert out.count('APS SUBMISSION TODO') == 1
OUT.write_text(out, encoding='utf-8')
print(f'wrote {OUT}')
