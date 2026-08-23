#!/usr/bin/env python3
"""Static integrity checks for the autonomous temporal-information manuscript.

This is deliberately lightweight and uses only the Python standard library.
It is not a TeX parser. It catches manuscript-package mistakes that should fail
before LaTeX is invoked: duplicate labels, undefined refs, missing BibTeX keys,
missing input files, internal draft markers, personal-repository leakage, and
PRX Quantum's requirement that references cited in Supplemental Material also
appear in the main bibliography.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
M2R2_MAIN = HERE / "autonomous_temporal_resource_law_m2r2.tex"
SUPPLEMENT = HERE / "autonomous_temporal_resource_law_supplement_m2r2.tex"
PRXQ_MAIN = HERE / "autonomous_temporal_resource_law_prxq_r2.tex"
ROOTS = [M2R2_MAIN, SUPPLEMENT, PRXQ_MAIN]
BIB = HERE / "references.bib"

INPUT_RE = re.compile(r"\\input\{([^}]+)\}")
LABEL_RE = re.compile(r"\\label\{([^}]+)\}")
REF_RE = re.compile(r"\\(?:eqref|ref|pageref|autoref)\{([^}]+)\}")
CITE_RE = re.compile(r"\\cite(?:\[[^\]]*\])?\{([^}]+)\}")
NOCITE_RE = re.compile(r"\\nocite\{([^}]+)\}")
BIBKEY_RE = re.compile(r"@\w+\s*\{\s*([^,\s]+)\s*,", re.MULTILINE)

BANNED_MARKERS = (
    "INTERNAL PROOF MAP",
    "INTERNAL SCOPE LOCK",
    "SOURCE:",
    "SOURCES:",
    "Working theorem-first abstract",
    "TODO",
)

# Submission files must be fully standalone and must never expose a personal
# source-control identity or rely on a private/public project repository.
FORBIDDEN_SUBMISSION_TOKENS = (
    "github",
    "kajin-0",
    "UniversalPhotodetectionResourceRepo2026",
    "The Universal Photodetection Resource Problem",
)


def strip_comments(text: str) -> str:
    out: list[str] = []
    for line in text.splitlines():
        m = re.search(r"(?<!\\)%", line)
        if m:
            line = line[: m.start()]
        out.append(line)
    return "\n".join(out)


def read_expanded(path: Path, stack: tuple[Path, ...] = ()) -> str:
    if path in stack:
        chain = " -> ".join(str(p.relative_to(HERE)) for p in (*stack, path))
        raise RuntimeError(f"recursive \\input cycle: {chain}")
    if not path.exists():
        raise FileNotFoundError(path)

    raw = path.read_text(encoding="utf-8")
    clean = strip_comments(raw)

    def repl(match: re.Match[str]) -> str:
        rel = match.group(1)
        child = path.parent / rel
        if child.suffix == "":
            child = child.with_suffix(".tex")
        return read_expanded(child.resolve(), (*stack, path))

    return INPUT_RE.sub(repl, clean)


def extract_citations(text: str, include_nocite: bool = True) -> set[str]:
    keys: set[str] = set()
    for group in CITE_RE.findall(text):
        keys.update(k.strip() for k in group.split(",") if k.strip())
    if include_nocite:
        for group in NOCITE_RE.findall(text):
            keys.update(k.strip() for k in group.split(",") if k.strip() and k.strip() != "*")
    return keys


def bib_text_and_keys() -> tuple[str, set[str]]:
    text = BIB.read_text(encoding="utf-8")
    keys = set(BIBKEY_RE.findall(text))
    if not keys:
        raise RuntimeError("no BibTeX keys parsed from references.bib")
    return text, keys


def forbidden_token_errors(name: str, text: str) -> list[str]:
    low = text.lower()
    return [
        f"{name}: forbidden personal-repository token present: {token!r}"
        for token in FORBIDDEN_SUBMISSION_TOKENS
        if token.lower() in low
    ]


def inspect_root(root: Path, keys: set[str]) -> tuple[list[str], str, set[str]]:
    errors: list[str] = []
    try:
        text = read_expanded(root.resolve())
    except Exception as exc:
        return [f"{root.name}: input expansion failed: {exc}"], "", set()

    labels = LABEL_RE.findall(text)
    refs = REF_RE.findall(text)
    cites = extract_citations(text)

    counts: dict[str, int] = {}
    for label in labels:
        counts[label] = counts.get(label, 0) + 1
    dup = sorted(k for k, n in counts.items() if n > 1)
    if dup:
        errors.append(f"{root.name}: duplicate labels: {', '.join(dup)}")

    undefined = sorted(set(refs) - set(labels))
    if undefined:
        errors.append(f"{root.name}: undefined refs: {', '.join(undefined)}")

    missing_cites = sorted(cites - keys)
    if missing_cites:
        errors.append(f"{root.name}: missing BibTeX keys: {', '.join(missing_cites)}")

    for marker in BANNED_MARKERS:
        if marker in text:
            errors.append(f"{root.name}: canonical source still contains draft marker {marker!r}")

    errors.extend(forbidden_token_errors(root.name, text))

    if re.search(r"\\nu_y\s*=\s*\\frac\{\\Tr\(XM_y\)", text):
        errors.append(f"{root.name}: found \\nu_y where bilateral score vector must be u_y")

    if root in (M2R2_MAIN, PRXQ_MAIN) and "F^{\\mathrm{tan}}" not in text:
        errors.append(f"{root.name}: R2 boundary score-Fisher notation missing")

    print(
        f"{root.name}: labels={len(labels)} refs={len(refs)} "
        f"citations={len(cites)} expanded_chars={len(text)}"
    )
    return errors, text, cites


def main() -> int:
    if not BIB.exists():
        print("ERROR: references.bib missing", file=sys.stderr)
        return 1

    bib_text, keys = bib_text_and_keys()
    errors: list[str] = forbidden_token_errors(BIB.name, bib_text)
    inspected: dict[Path, tuple[str, set[str]]] = {}

    for root in ROOTS:
        root_errors, text, cites = inspect_root(root, keys)
        errors.extend(root_errors)
        inspected[root] = (text, cites)

    if SUPPLEMENT in inspected and PRXQ_MAIN in inspected:
        supp_cites = inspected[SUPPLEMENT][1]
        main_cites = inspected[PRXQ_MAIN][1]
        missing_from_main = sorted(supp_cites - main_cites)
        if missing_from_main:
            errors.append(
                "PRXQ packaging: supplement citations absent from generated main bibliography: "
                + ", ".join(missing_from_main)
            )
        else:
            print(
                f"PRXQ supplement-reference coverage PASS; "
                f"supplement_keys={len(supp_cites)}"
            )

    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        return 1

    print(f"Static TeX integrity PASS; BibTeX keys={len(keys)}")
    print("Standalone-submission identity leak gate PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
