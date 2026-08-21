#!/usr/bin/env python3
"""Generate Rev10 from Rev9 by adding one literature-IRF worked example."""
from pathlib import Path
src = Path('event_resource_theorem_rev9.tex')
out = Path('event_resource_theorem_rev10.tex')
section = Path('section_worked_irf_example_rev10.tex')
assert src.exists() and section.exists()
s = src.read_text(encoding='utf-8')
anchor = r'\input{section_empirical_grounding_rev9}'
assert s.count(anchor) == 1
s = s.replace(anchor, anchor + '\n\n' + r'\input{section_worked_irf_example_rev10}', 1)
old = (
    r'For direct use with existing timing data, we give closed-form mappings for canonical timing laws and '
    r'a fit-free estimator of $B_{\rm FI}$ from digitized impulse-response histograms. We then '
)
new = (
    r'For direct use with existing timing data, we give closed-form mappings for canonical timing laws, '
    r'a fit-free estimator of $B_{\rm FI}$ from digitized impulse-response histograms, and a worked '
    r'literature-IRF example in which FWHM and Fisher-equivalent bandwidth rank two detectors oppositely. We then '
)
assert s.count(old) == 1
s = s.replace(old, new, 1)
assert s.count(r'\input{section_worked_irf_example_rev10}') == 1
assert 'rank two detectors oppositely' in s
out.write_text(s, encoding='utf-8')
print(f'generated {out}')
