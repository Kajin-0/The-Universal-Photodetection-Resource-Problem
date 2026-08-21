# Research Log Round 20 — Published-IRF worked example

**Date:** 2026-08-20

## Trigger

A new review judged Rev9 materially stronger than Rev6 but identified one remaining applied-readiness gap for Physical Review Applied: the paper had equations and a histogram estimator but no worked numerical example on an actual published detector IRF.

## Source chosen

A. Spinelli, M. A. Ghioni, S. D. Cova, and L. M. Davis, *Avalanche Detector with Ultraclean Response for Time-Resolved Photon Counting*, IEEE Journal of Quantum Electronics 34, 817–821 (1998), DOI `10.1109/3.668769`.

This paper is unusually suitable because its Fig. 3 plots normalized IRFs for a DJ-SPAD and an MCP in the same axes, while Table I reports FWHM 35 ps for the DJ-SPAD and 25 ps for the MCP. The MCP therefore wins under FWHM despite having visibly broader bumps/tails.

## Calculation

For a nonnegative plotted trace `c(t)`, arbitrary vertical normalization cancels:

`B_FI = 0.5 * integral(c^2 dt) / [integral(c dt)]^2`.

Approximate graphical digitization of the two Fig. 3 traces over the displayed 0–1000 ps interval gives:

- DJ-SPAD: `B_FI = 9.160 GHz`;
- MCP: `B_FI = 5.977 GHz`.

For comparison, assuming a Gaussian law from FWHM alone would give:

- DJ-SPAD, 35 ps: `9.490 GHz`;
- MCP, 25 ps: `13.286 GHz`.

Thus the conventional FWHM ranking reverses under the full-shape Fisher-equivalent bandwidth. `B_FI(DJ)/B_FI(MCP)=1.533`. The Gaussian-from-FWHM proxy overestimates the MCP value by a factor of about 2.22 but changes the DJ-SPAD value by only a few percent.

## Interpretation

This is the concrete applied demonstration the paper lacked. It shows on a real published detector comparison that a narrower FWHM need not imply greater temporal-information bandwidth when the response contains broad low-amplitude structure.

The manuscript is explicit that this is approximate graphical digitization, not a reanalysis of Spinelli et al.'s raw TCSPC events. The finite plotting window and line thickness limit precision. The example is intended to demonstrate the ranking effect, not establish a new precision measurement of those devices.

## Durable files

- `manuscript/section_worked_irf_example_rev10.tex`
- `manuscript/spinelli1998_fig3_digitized_rev10.csv`
- `manuscript/analyze_spinelli1998_fig3_rev10.py`
- `manuscript/apply_rev10_literature_example.py`
- `manuscript/REV10_SHA256SUMS.txt`
- `submission/PRAPPLIED_PACKAGE_VALIDATION_REV10.md`
- `submission/SUBMISSION_PACKAGE_CHECKLIST_REV10.md`

## Version decision

This addition is versioned as **Rev10** because it introduces analysis of a published experimental figure and changes the Data Availability statement. The Rev9 theorem stack is unchanged.

## Stop condition

The applied-readiness gap identified by the review is now closed. Do not add more worked examples or literature mining by default. Reopen only for a concrete mathematical defect, a specific referee request, or a demonstrably stronger published-data example that changes an actual conclusion.
