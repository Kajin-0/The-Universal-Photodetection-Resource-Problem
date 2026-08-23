#!/usr/bin/env python3
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "dynamical_rank_boundary_implementation_cost_supplement_d2.tex"
OUT = HERE / "dynamical_rank_boundary_implementation_cost_supplement_pra_r1.tex"

NEW_TITLE = (
    r"\title{Supplemental Material for ``Exact minimum dynamical cost of "
    r"prescribed rank-changing quantum-state curvature''}"
)


def main() -> None:
    text = SRC.read_text(encoding="utf-8")
    title_start = text.find(r"\title{")
    title_end = text.find("}\n", title_start)
    if title_start < 0 or title_end < 0:
        raise RuntimeError("supplement title not found")

    text = text[:title_start] + NEW_TITLE + text[title_end + 1:]
    OUT.write_text(text, encoding="utf-8")
    print(f"generated {OUT.name}")


if __name__ == "__main__":
    main()
