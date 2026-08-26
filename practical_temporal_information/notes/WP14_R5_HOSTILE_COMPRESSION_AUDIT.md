# WP14 — R5 hostile compression audit

**Date:** 2026-08-25

**Status:** **PASS FOR A NARROW R6.** R5 is scientifically clean and not structurally bloated, but a controlled prose-only reduction of about 500 words is justified. No theorem, equation, proof, figure, caption, disclosure, or bibliography change is warranted.

## Purpose

Read frozen R5 as a skeptical Physical Review Applied editor/referee and ask whether publication compression can materially improve precision without reopening scientific content.

## Frozen baseline

R5:

- run `32915363157` PASS;
- artifact `9588018384`;
- PDF 10 pages / 429432 bytes;
- SHA-256 `fd451a59ca5b70731b61f7ce237bd06a1d5f7105305e064cfe21bbb588e6bf48`;
- all ten pages render-clean.

WP12 figures are independently frozen and must remain byte-identical.

## Audit conclusion

A broad rewrite is **not** justified. The technical density is already appropriate. The main removable material is repeated roadmap/recap prose that became redundant after the four figures were integrated.

A candidate R6 transform tested against the exact R5 source removes approximately:

- `526` token-like words under a simple lexical count;
- `3725` source characters;
- about `13%` of the R5 main-source lexical count;

while leaving the external support-theorem section completely untouched.

The expected benefit is a sharper Introduction/Discussion and potentially one less typeset page depending on float placement.

## Explicit allowed-edit map

R6 may make **only** the following six prose edits in the generated R5 main source:

1. **Delete the Introduction roadmap paragraph** beginning `The paper has four main steps.`
   - Reason: it repeats the abstract and section headings almost verbatim.

2. **Delete the NEP dimensional-units sentence** beginning `The units are consistent:`.
   - Reason: correct but tutorial-level once the conventions/units have already been stated explicitly.

3. **Delete the one-sentence colored-noise gloss** beginning `This is an ordinary colored-noise structure:`.
   - Reason: the equation and Fig. 1 already make the roll-off visually and mathematically explicit.

4. **Compress the two post-theorem memory paragraphs** into one paragraph.
   - Must preserve: same-curve/different-timestamp conclusion, companion attribution, model-discrimination interpretation, and statement that this is not itself a resource-law challenge.

5. **Compress the two closing falsification-hierarchy paragraphs** into one paragraph.
   - Must preserve: Level-I-first interpretation and the condition that Level II requires independently verified state family, coordinates, support/radius or curvature, and Fisher likelihood.

6. **Compress the seven-paragraph Discussion to four paragraphs.**
   - Must preserve:
     - FI complements rather than replaces standard detector specifications;
     - frequency-resolved NEP and Type-II memory lessons;
     - exact support crossover and independent measurement routes;
     - resonant benchmark is not thermodynamic work;
     - different platforms may test different components;
     - no experimental data are reported;
     - real-device imperfections are Level-I/model issues first.

## Byte-frozen content in R6

R6 must preserve exactly:

- the abstract;
- all four R5 figure blocks and captions;
- all equations and equation labels;
- the external `sections/support_crossover_r2.tex` theorem/proposition/proof source;
- section and subsection headings;
- the seven explicit falsification test entries;
- Data Availability;
- AI-Assisted Research and Verification;
- bibliography source;
- all companion citations and novelty-boundary language outside the six mapped edits.

## Required R6 gate

The R6 checker must reconstruct the entire expected R6 file from R5 using exactly the six approved replacements and require byte equality. It must additionally require:

- each frozen R5 figure block appears exactly once and byte-identically;
- figure paths and labels unchanged;
- all `\begin{equation}`, `\begin{align}`, labels, and citation commands unchanged in count and sequence;
- the support-section `\input{sections/support_crossover_r2}` unchanged;
- disclosures unchanged;
- no new overclaiming phrase.

## Next

Implement R6 only through the deterministic map above, compile in clean CI, compare page count and render quality against R5, and freeze R6 only if it is visually at least as clean and substantively sharper. If R6 does not improve the manuscript, retain R5 as canonical.
