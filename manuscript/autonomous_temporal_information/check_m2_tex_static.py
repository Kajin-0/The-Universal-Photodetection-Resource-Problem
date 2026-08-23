#!/usr/bin/env python3
"""Static integrity checks for the autonomous temporal-information manuscript.

This is deliberately lightweight and uses only the Python standard library.
It is not a TeX parser. It catches repository-level mistakes that should fail
before LaTeX is invoked: duplicate labels, undefined refs, missing BibTeX keys,
missing input files, and obvious internal-draft markers in canonical roots.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOTS = [
    HERE / "autonomous_temporal_resource_law_m2r1.tex",
    HERE / "autonomous_temporal_resource_law_supplement_m2r1.tex",
    HERE / "autonomous_temporal_resource_law_prxq_r1.tex",
]
BIB = HERE / "references.bib"

INPUT_RE = re.compile(r"\\input\{([^}]+)\}")
LABEL_RE = re.compile(r"\\label\{([^}]+)\}")
REF_RE = re.compile(r"\\(?:eqref|ref|pageref|autoref)\{([^}]+)\}")
CITE_RE = re.compile(r"\\cite(?:\[[^\]]*\])?\{([^}]+)\}")
BIBKEY_RE = re.compile(r"@\w+\s*\{\s*([^,\s]+)\s*,", re.MULTILINE)

BANNED_MARKERS = (
    "INTERNAL PROOF MAP",
    "INTERNAL SCOPE LOCK",
    "SOURCE:",
    "SOURCES:",
    "Working theorem-first abstract",
    "TODO",
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


def bib_keys() -> set[str]:
    text = BIB.read_text(encoding="utf-8")
    keys = set(BIBKEY_RE.findall(text))
    if not keys:
        raise RuntimeError("no BibTeX keys parsed from references.bib")
    return keys


def check_root(root: Path, keys: set[str]) -> list[str]:
    errors: list[str] = []
    try:
        text = read_expanded(root.resolve())
    except Exception as exc:
        return [f"{root.name}: input expansion failed: {exc}"]

    labels = LABEL_RE.findall(text)
    refs = REF_RE.findall(text)
    cites: list[str] = []
    for group in CITE_RE.findall(text):
        cites.extend(k.strip() for k in group.split(",") if k.strip())

    counts: dict[str, int] = {}
    for label in labels:
        counts[label] = counts.get(label, 0) + 1
    dup = sorted(k for k, n in counts.items() if n > 1)
    if dup:
        errors.append(f"{root.name}: duplicate labels: {', '.join(dup)}")

    undefined = sorted(set(refs) - set(labels))
    if undefined:
        errors.append(f"{root.name}: undefined refs: {', '.join(undefined)}")

    missing_cites = sorted(set(cites) - keys)
    if missing_cites:
        errors.append(f"{root.name}: missing BibTeX keys: {', '.join(missing_cites)}")

    for marker in BANNED_MARKERS:
        if marker in text:
            errors.append(f"{root.name}: canonical source still contains draft marker {marker!r}")

    if re.search(r"\\nu_y\s*=\s*\\frac\{\\Tr\(XM_y\)", text):
        errors.append(f"{root.name}: found \\nu_y where bilateral score vector must be u_y")

    print(
        f"{root.name}: labels={len(labels)} refs={len(refs)} "
        f"citations={len(cites)} expanded_chars={len(text)}"
    )
    return errors


def main() -> int:
    if not BIB.exists():
        print("ERROR: references.bib missing", file=sys.stderr)
        return 1
    keys = bib_keys()
    errors: list[str] = []
    for root in ROOTS:
        errors.extend(check_root(root, keys))

    if errors:
        for err in errors:
            print(f"ERROR: {err}", file=sys.stderr)
        return 1

    print(f"Static TeX integrity PASS; BibTeX keys={len(keys)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
