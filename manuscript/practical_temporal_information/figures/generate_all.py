from __future__ import annotations

import hashlib
import json
from pathlib import Path

import fig1_same_specs
import fig2_memory_benchmark
import fig3_support_crossover
import fig4_resonant_implementation
from common import OUT

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    OUT.mkdir(parents=True, exist_ok=True)

    for p in OUT.glob("*"):
        if p.is_file():
            p.unlink()

    locked = {
        "figure_1": fig1_same_specs.main(),
        "figure_2": fig2_memory_benchmark.main(),
        "figure_3": fig3_support_crossover.main(),
        "figure_4": fig4_resonant_implementation.main(),
    }
    (OUT / "locked_values.json").write_text(json.dumps(locked, indent=2, sort_keys=True) + "\n")

    expected_stems = [
        fig1_same_specs.STEM,
        fig2_memory_benchmark.STEM,
        fig3_support_crossover.STEM,
        fig4_resonant_implementation.STEM,
    ]
    for stem in expected_stems:
        pdf = OUT / f"{stem}.pdf"
        png = OUT / f"{stem}.png"
        assert pdf.exists() and pdf.stat().st_size > 10_000
        assert png.exists() and png.stat().st_size > 20_000
        assert pdf.read_bytes().startswith(b"%PDF")
        assert png.read_bytes().startswith(b"\x89PNG\r\n\x1a\n")

    manifest = {}
    for path in sorted(OUT.iterdir()):
        if path.is_file():
            manifest[path.name] = {
                "bytes": path.stat().st_size,
                "sha256": sha256(path),
            }
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
    print("WP12 deterministic figure package: PASS")
    for name, item in manifest.items():
        print(f"{item['sha256']}  {item['bytes']:>8}  {name}")

if __name__ == "__main__":
    main()
