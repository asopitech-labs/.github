#!/usr/bin/env python3
"""Crop the shipped brand assets out of the design book.

`scripts/render_brand_book.py` draws one large catalog image
(`assets/brand/design-book.png`) plus `manifest.json`, which records the exact
pixel box of every tile and the sizes it ships at. This script is the second
half of that pipeline: it slices the catalog into the individual files that the
profile READMEs reference.

Run after any change to the design book:

    python3 scripts/render_brand_book.py
    python3 scripts/export_brand_assets.py

The marks themselves are not generated: `assets/brand/source/` holds the
existing avatars, which the design book composites. Do not redraw them.
"""
from __future__ import annotations

import json
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
BRAND = ROOT / "assets" / "brand"
BOOK = BRAND / "design-book.png"
MANIFEST = BRAND / "manifest.json"


def target_size(size) -> tuple[int, int]:
    """Manifest convention: an integer is a square edge, a pair is (w, h)."""
    if isinstance(size, (list, tuple)):
        width, height = size
        return int(width), int(height)
    return int(size), int(size)


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    book = Image.open(BOOK)
    book.load()

    canvas = manifest["canvas"]
    if book.size != (canvas["width"], canvas["height"]):
        raise SystemExit(
            f"design-book.png is {book.size}, manifest claims "
            f"{(canvas['width'], canvas['height'])} — re-run render_brand_book.py"
        )

    written: list[str] = []
    for tile in manifest["tiles"]:
        exports = tile.get("export") or []
        if not exports:
            continue

        x, y, w, h = (tile[k] for k in ("x", "y", "w", "h"))
        if x < 0 or y < 0 or x + w > book.width or y + h > book.height:
            raise SystemExit(f"tile {tile['name']} falls outside the canvas")

        crop = book.crop((x, y, x + w, y + h))
        opaque = tile.get("background", "transparent") != "transparent"

        for export in exports:
            size = target_size(export["size"])
            out = crop if size == crop.size else crop.resize(size, Image.LANCZOS)
            if opaque:
                out = out.convert("RGB")
            out.save(BRAND / export["path"], optimize=True)
            written.append(export["path"])

    print(f"Exported {len(written)} files to {BRAND.relative_to(ROOT)}:")
    for name in written:
        print(f"  {name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
