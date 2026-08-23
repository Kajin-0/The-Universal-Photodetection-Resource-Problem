#!/usr/bin/env python3
"""Apply final non-scientific submission cleanup to generated M2R2 sources.

This pass implements only final editorial/presentation cleanup:
1. remove rendered internal work-package nomenclature from the mixed-bridge proof module;
2. simplify Theorem 6 branch prose in the main manuscript;
3. suppress visible hyperlink-border rectangles in the submission PDFs.

It does not alter any theorem, equation, coefficient, proof step, citation, or resource definition.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
MAIN = HERE / "autonomous_temporal_resource_law_m2r2.tex"
SUPP = HERE / "autonomous_temporal_resource_law_supplement_m2r2.tex"
MIXED_PROOF = HERE / "proofs" / "noncommuting_mixed_bridge_proof_r1.tex"


def replace_once(path: Path, old: str, new: str, label: str) -> None:
    text = path.read_text(encoding="utf-8")
    if text.count(old) != 1:
        raise RuntimeError(f"{label}: expected exactly one occurrence, found {text.count(old)}")
    path.write_text(text.replace(old, new, 1), encoding="utf-8")
    print(f"{path.name}: applied {label}")


def main() -> None:
    replace_once(
        MIXED_PROOF,
        "which is exactly the one-sided WP18 coefficient.",
        "which exactly recovers the one-sided autonomous coefficient stated in the main text.",
        "remove internal WP18 label",
    )

    replace_once(
        MAIN,
        "When both synthesized orientations are nonzero with $g_+,g_->0$, every finite-$N$ collective POVM obeys, for each available finite internal branch,",
        "When both synthesized orientations are nonzero with $g_+,g_->0$, the bound is the minimum over the available finite internal branches:",
        "simplify Theorem 6 branch wording",
    )
    replace_once(
        MAIN,
        "where unavailable internal branches are omitted from the minimum. The corresponding one-sided, support-only, and zero-cost cases are stated explicitly in the Supplemental Material.",
        "The corresponding one-sided, support-only, and zero-cost cases are stated explicitly in the Supplemental Material.",
        "remove redundant branch sentence",
    )

    for path in (MAIN, SUPP):
        replace_once(
            path,
            "\\usepackage{hyperref}",
            "\\usepackage{hyperref}\n\\hypersetup{hidelinks}",
            "hide hyperlink borders",
        )


if __name__ == "__main__":
    main()
