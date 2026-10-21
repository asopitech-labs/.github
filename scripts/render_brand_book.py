#!/usr/bin/env python3
"""Render the brand catalog and crop manifest; never modify the source marks.

Run from any directory with Python 3 and Pillow. Tile coordinates describe native
pixels, excluding all catalog labels. No individual export files are generated.
"""
from pathlib import Path
import json
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets/brand"
WIDTH, HEIGHT = 2752, 7488  # 2560px artwork + two 96px catalog margins
PINK, PALE = "#E57FC1", "#E7C0DD"
INK, WHITE, MAROON = "#0B0B0F", "#FFFFFF", "#4A1F26"

# This is the sole geometry definition, consumed by rendering AND the manifest.
TILES = [
    dict(name="lockup-asopitech-dark", x=608, y=256, w=1536, h=384,
         background="transparent", purpose="personal profile README hero, dark theme"),
    dict(name="lockup-asopitech-light", x=608, y=768, w=1536, h=384,
         background="transparent", purpose="personal profile README hero, light theme"),
    dict(name="lockup-labo-dark", x=608, y=1280, w=1536, h=384,
         background="transparent", purpose="lab profile README hero, dark theme"),
    dict(name="lockup-labo-light", x=608, y=1792, w=1536, h=384,
         background="transparent", purpose="lab profile README hero, light theme"),
    dict(name="social-asopitech", x=96, y=2368, w=2560, h=1280,
         background=MAROON, purpose="personal GitHub profile social link preview"),
    dict(name="social-labo", x=96, y=3776, w=2560, h=1280,
         background=MAROON, purpose="lab GitHub organization social link preview"),
    dict(name="banner-asopitech", x=96, y=5184, w=2560, h=640,
         background=MAROON, purpose="personal profile README wide header"),
    dict(name="banner-labo", x=96, y=5952, w=2560, h=640,
         background=WHITE, purpose="lab profile README wide header"),
    dict(name="mark-asopitech-square", x=608, y=6752, w=512, h=512,
         background="transparent", purpose="lettering-free personal site header logo at 24–48px"),
    dict(name="favicon-asopitech-plate", x=1632, y=6752, w=512, h=512,
         background="#000000", purpose="personal site favicon with black contrast plate at 16–48px"),
]

# Original pixel regions, not recreated artwork. The lower cone avoids the
# lettering band; the uppermost star is intact. Their placements share a 512px
# coordinate system for both small-mark tiles. No missing pixels are repainted.
MOTIF_PARTS = [
    dict(crop=(7, 134, 130, 213), position=(32, 205), size=(448, 288), largest_component=True),
    dict(crop=(57, 6, 117, 64), position=(272, 16), size=(208, 201), largest_component=True),
]


def motif_part(source, part):
    crop = source.crop(part["crop"])
    if part["largest_component"]:
        # Rectangular crops also catch disconnected ribbon tips. Keep only the
        # cone or star's existing connected pixels, omitting those fragments.
        # All retained RGBA values remain exactly those of the source PNG.
        alpha = crop.getchannel("A")
        remaining = {(x, y) for y in range(crop.height) for x in range(crop.width) if alpha.getpixel((x, y))}
        largest = set()
        while remaining:
            seed = remaining.pop()
            component, pending = {seed}, [seed]
            while pending:
                x, y = pending.pop()
                for dx, dy in ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)):
                    point = (x + dx, y + dy)
                    if point in remaining:
                        remaining.remove(point)
                        component.add(point)
                        pending.append(point)
            if len(component) > len(largest):
                largest = component
        kept = Image.new("RGBA", crop.size)
        for point in largest:
            kept.putpixel(point, crop.getpixel(point))
        crop = kept
    return crop


def small_mark(tile):
    im = Image.new("RGBA", (tile["w"], tile["h"]), (0, 0, 0, 0))
    with Image.open(OUT / "source/avatar-asopitech-512.png") as original:
        source = original.convert("RGBA")
    for part in MOTIF_PARTS:
        crop = motif_part(source, part)
        im.alpha_composite(crop.resize(part["size"], Image.Resampling.LANCZOS), part["position"])
    if tile["background"] != "transparent":
        plate = Image.new("RGBA", im.size, tile["background"])
        plate.alpha_composite(im)
        return plate
    return im


def first_font(candidates):
    for path in candidates:
        if Path(path).is_file():
            return path
    raise RuntimeError("Required font missing. Install a Japanese-capable font or update the font candidates.")


JP = first_font([
    "/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc",
    "/System/Library/Fonts/Hiragino Sans GB.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
    "/usr/share/fonts/truetype/noto/NotoSansJP-Regular.ttf",
])
LATIN = first_font([
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf", JP,
])
REGULAR = first_font([
    "/System/Library/Fonts/Supplemental/Arial.ttf", JP,
])


def font(size, kind="latin"):
    return ImageFont.truetype({"jp": JP, "latin": LATIN, "regular": REGULAR}[kind], size)


def text(im, xy, value, size, color, kind="latin"):
    """Use top-of-ink anchoring for consistent optical positioning."""
    ImageDraw.Draw(im).text(xy, value, font=font(size, kind), fill=color, anchor="lt")


def lines(im, xy, values, size, leading, color, kind="regular"):
    for i, value in enumerate(values):
        text(im, (xy[0], xy[1] + i * leading), value, size, color, kind)


def mark(im, brand, xy, size):
    """Composite the original full PNG, including its original alpha/background.

    Every application uses a plate with radius and equal four-sided padding of
    1/8 its width. Personal artwork retains its native black field; the lab's
    original white background blends into its white plate. Neither PNG is
    recolored, clipped, traced, or stripped of its background.
    """
    source = Image.open(OUT / "source" / f"avatar-{brand}-512.png").convert("RGBA")
    padding = size // 8
    available = size - 2 * padding
    scale = min(available / source.width, available / source.height)
    scaled = source.resize((round(source.width * scale), round(source.height * scale)), Image.Resampling.LANCZOS)
    # Supersample only the surrounding plate for smooth rounded corners.
    plate = Image.new("RGBA", (size * 4, size * 4), (0, 0, 0, 0))
    ImageDraw.Draw(plate).rounded_rectangle(
        (0, 0, size * 4 - 1, size * 4 - 1), radius=padding * 4,
        fill=WHITE if brand == "asopitech-labs" else "#000000")
    im.alpha_composite(plate.resize((size, size), Image.Resampling.LANCZOS), xy)
    offset = (xy[0] + (size - scaled.width) // 2, xy[1] + (size - scaled.height) // 2)
    im.alpha_composite(scaled, offset)


def dark_field(w, h):
    im = Image.new("RGBA", (w, h), MAROON)
    draw = ImageDraw.Draw(im)
    # A restrained tonal gradient using only the existing maroon family.
    start, end = (74, 31, 38), (122, 46, 53)
    for x in range(w):
        t = x / (w - 1)
        color = tuple(round(a + (b - a) * t) for a, b in zip(start, end)) + (255,)
        draw.line((x, 0, x, h - 1), fill=color)
    return im


def lockup(tile):
    im = Image.new("RGBA", (tile["w"], tile["h"]), (0, 0, 0, 0))
    lab = "labo" in tile["name"]
    dark = tile["name"].endswith("dark")
    mark(im, "asopitech-labs" if lab else "asopitech", (48, 48), 288)
    title = "Asopitech Labo" if lab else "asopitech"
    text(im, (400, 102), title, 112 if lab else 132, WHITE if dark else INK)
    text(im, (404, 258), "アソピテック・ラボ" if lab else "あそぴてっく", 39, PALE if dark else MAROON, "jp")
    return im


def social(tile):
    lab = tile["name"].endswith("labo")
    im = dark_field(tile["w"], tile["h"])
    draw = ImageDraw.Draw(im)
    fg, secondary = WHITE, PALE
    draw.rectangle((192, 168, 271, 177), fill=PINK)
    text(im, (192, 211), "RESEARCH & DEVELOPMENT" if lab else "INDEPENDENT DEVELOPER / OPEN SOURCE", 29, secondary)
    text(im, (184, 322), "Asopitech Labo" if lab else "asopitech", 151 if lab else 202, fg)
    mark(im, "asopitech-labs" if lab else "asopitech", (1792, 200), 576)
    if lab:
        text(im, (192, 642), "まず作って確かめる R&D ラボ", 55, WHITE, "jp")
        lines(im, (192, 861), ["An R&D lab that prototypes first and validates second"], 43, 62, PALE)
        text(im, (192, 1080), "asopi.tech/labo", 37, WHITE)
        text(im, (1792, 1087), "github.com/asopitech-labs", 33, PALE, "regular")
    else:
        lines(im, (192, 642), ["分散システム・データベース・言語・AI検索基盤の", "OSSエコシステムを個人で設計・実装"], 55, 86, WHITE, "jp")
        lines(im, (192, 861), ["An independent developer building an OSS ecosystem across", "distributed systems, databases, languages, and AI retrieval"], 43, 62, PALE)
        text(im, (192, 1080), "asopi.tech", 37, WHITE)
        text(im, (1792, 1087), "github.com/asopitech", 33, PALE, "regular")
    return im


def banner(tile):
    lab = tile["name"].endswith("labo")
    im = Image.new("RGBA", (2560, 640), WHITE) if lab else dark_field(2560, 640)
    draw = ImageDraw.Draw(im)
    mark(im, "asopitech-labs" if lab else "asopitech", (160, 128), 384)
    fg, secondary = (INK, MAROON) if lab else (WHITE, PALE)
    text(im, (632, 158), "Asopitech Labo" if lab else "asopitech", 148, fg)
    text(im, (640, 369), "まず作って確かめる R&D ラボ" if lab else "分散システム・データベース・言語・AI検索基盤", 44, secondary, "jp")
    draw.rectangle((640, 478, 719, 485), fill=PINK)
    text(im, (2000, 497), "asopi.tech/labo" if lab else "asopi.tech", 32, secondary, "regular")
    return im


def validate(book, manifest):
    assert book.mode == "RGBA" and book.size == (WIDTH, HEIGHT)
    boxes = []
    for tile in manifest["tiles"]:
        x, y, w, h = (tile[k] for k in ("x", "y", "w", "h"))
        assert all(isinstance(v, int) for v in (x, y, w, h))
        assert 0 <= x < x + w <= WIDTH and 0 <= y < y + h <= HEIGHT
        for ax, ay, bx, by in boxes:
            assert x + w + 48 <= ax or bx + 48 <= x or y + h + 48 <= ay or by + 48 <= y
        boxes.append((x, y, x + w, y + h))
        alpha = book.getchannel("A").crop(boxes[-1])
        assert alpha.getextrema() == ((0, 255) if tile["background"] == "transparent" else (255, 255))


def main():
    book = Image.new("RGBA", (WIDTH, HEIGHT), INK)
    text(book, (96, 66), "asopitech / Asopitech Labo", 56, WHITE)
    text(book, (98, 148), "IDENTITY CATALOG     /     01     /     ORIGINAL MARKS + DIGITAL APPLICATIONS", 23, PALE, "regular")
    manifest = {"canvas": {"width": WIDTH, "height": HEIGHT}, "tiles": []}
    for i, tile in enumerate(TILES, 1):
        art = render_tile(tile)
        # paste WITHOUT a mask is intentional: tile alpha replaces the catalog
        # background, leaving truly transparent lockup pixels in the master PNG.
        book.paste(art, (tile["x"], tile["y"]))
        text(book, (tile["x"], tile["y"] - 45), f"{i:02d}   {tile['name']}", 24, PALE, "regular")
        if tile["name"].startswith("lockup"):
            text(book, (96, tile["y"] + 120), "TRANSPARENT", 22, PINK)
            text(book, (96, tile["y"] + 163), "1536 × 384 px", 23, PALE, "regular")
            text(book, (96, tile["y"] + 205), "For " + ("dark" if tile["name"].endswith("dark") else "light") + " surfaces", 23, PALE, "regular")
            small = [800, 200]
        elif tile["name"].startswith(("social", "banner")):
            small = [1280, tile["h"] // 2]
        else:
            small = None
        entry = dict(tile)
        sizes = [[tile["w"], tile["h"]], small] if small else [
            [s, s] for s in ([512, 256, 96, 48] if tile["name"].startswith("mark-") else [512, 180, 48, 32, 16])]
        entry["export"] = [
            {"path": tile["name"] + ("" if index == 0 else f"-{size[0]}") + ".png", "size": size}
            for index, size in enumerate(sizes)]
        manifest["tiles"].append(entry)
    text(book, (96, HEIGHT - 80), "10 APPLICATIONS     /     SOURCE PIXELS PRESERVED     /     NATIVE PIXEL GEOMETRY", 22, PALE, "regular")
    validate(book, manifest)
    OUT.mkdir(parents=True, exist_ok=True)
    book.save(OUT / "design-book.png")
    (OUT / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with Image.open(OUT / "design-book.png") as saved:
        saved.load()
        validate(saved, manifest)
    print(f"Verified {WIDTH} × {HEIGHT} RGBA catalog; {len(TILES)} tiles; bounds, gutters and alpha valid.")
    print(f"Japanese font: {JP}")


def render_tile(tile):
    if tile["name"].startswith("lockup"):
        return lockup(tile)
    if tile["name"].startswith("social"):
        return social(tile)
    if tile["name"].startswith("banner"):
        return banner(tile)
    return small_mark(tile)


if __name__ == "__main__":
    main()
