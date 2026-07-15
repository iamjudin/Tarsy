#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

try:
    from PIL import Image, ImageSequence
except ImportError as exc:
    raise SystemExit("Pillow is required. Install with: python3 -m pip install pillow") from exc

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "tarsy"
EXPECTED_ROW_COUNTS = [6, 8, 8, 4, 5, 8, 6, 6, 6, 8, 8]


def fail(message: str) -> None:
    print(f"[fail] {message}", file=sys.stderr)
    raise SystemExit(1)


def ok(message: str) -> None:
    print(f"[ok] {message}")


def load_json(path: Path) -> dict:
    if not path.exists():
        fail(f"missing {path.relative_to(ROOT)}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")


def require_file(path: Path) -> None:
    if not path.is_file():
        fail(f"missing file {path.relative_to(ROOT)}")


def require_image_size(path: Path, size: tuple[int, int], *, animated: bool | None = None) -> None:
    require_file(path)
    with Image.open(path) as image:
        if image.size != size:
            fail(f"{path.relative_to(ROOT)} has size {image.size}, expected {size}")
        if animated is True and getattr(image, "n_frames", 1) < 2:
            fail(f"{path.relative_to(ROOT)} should be animated")
        if animated is False and getattr(image, "n_frames", 1) != 1:
            fail(f"{path.relative_to(ROOT)} should be static")
    ok(f"{path.relative_to(ROOT)} size is {size[0]}x{size[1]}")


def validate_marketplace() -> None:
    marketplace = load_json(ROOT / ".agents" / "plugins" / "marketplace.json")
    if marketplace.get("name") != "tarsy":
        fail("marketplace name must be tarsy")
    entries = marketplace.get("plugins")
    if not isinstance(entries, list):
        fail("marketplace plugins must be a list")
    entry = next((item for item in entries if item.get("name") == "tarsy"), None)
    if not entry:
        fail("marketplace must include tarsy entry")
    if entry.get("source", {}).get("path") != "./plugins/tarsy":
        fail("marketplace tarsy source path must be ./plugins/tarsy")
    policy = entry.get("policy", {})
    if policy.get("installation") != "AVAILABLE" or policy.get("authentication") != "ON_INSTALL":
        fail("marketplace tarsy policy must be AVAILABLE / ON_INSTALL")
    ok("marketplace entry is valid")


def validate_manifest() -> None:
    manifest = load_json(PLUGIN / ".codex-plugin" / "plugin.json")
    if manifest.get("name") != "tarsy":
        fail("plugin name must be tarsy")
    version = manifest.get("version", "")
    if not re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?", version):
        fail(f"unexpected plugin version: {version}")
    if manifest.get("skills") != "./skills/":
        fail("manifest skills path must be ./skills/")
    interface = manifest.get("interface", {})
    for key in ("displayName", "shortDescription", "longDescription", "developerName", "category"):
        if not interface.get(key):
            fail(f"manifest interface.{key} is required")
    for icon_key in ("composerIcon", "logo"):
        icon_path = interface.get(icon_key)
        if not icon_path:
            fail(f"manifest interface.{icon_key} is required")
        require_file(PLUGIN / icon_path)
    ok(f"plugin manifest is valid ({version})")


def validate_skill() -> None:
    skill_path = PLUGIN / "skills" / "tarsy" / "SKILL.md"
    require_file(skill_path)
    text = skill_path.read_text(encoding="utf-8")
    if "name: tarsy" not in text.split("---", 2)[1]:
        fail("skill frontmatter must contain name: tarsy")
    for required in ("Sarcasm changes style only", "honesty", "factual"):
        if required not in text:
            fail(f"skill is missing expected guardrail text: {required}")
    ok("skill guardrails are present")


def validate_pet() -> None:
    pet_dir = PLUGIN / "pets" / "tarsy"
    pet = load_json(pet_dir / "pet.json")
    if pet.get("id") != "tarsy":
        fail("pet id must be tarsy")
    if pet.get("spriteVersionNumber") != 2:
        fail("pet spriteVersionNumber must be 2")
    if pet.get("spritesheetPath") != "spritesheet.webp":
        fail("pet spritesheetPath must be spritesheet.webp")

    sheet_path = pet_dir / "spritesheet.webp"
    require_file(sheet_path)
    with Image.open(sheet_path) as sheet:
        if sheet.size != (1536, 2288):
            fail(f"spritesheet size is {sheet.size}, expected (1536, 2288)")
        rgba = sheet.convert("RGBA")
        cell_w = sheet.width // 8
        cell_h = sheet.height // 11
        counts: list[int] = []
        for row in range(11):
            count = 0
            for col in range(8):
                crop = rgba.crop((col * cell_w, row * cell_h, (col + 1) * cell_w, (row + 1) * cell_h))
                if crop.getbbox() is not None:
                    count += 1
            counts.append(count)
    if counts != EXPECTED_ROW_COUNTS:
        fail(f"spritesheet non-empty row counts are {counts}, expected {EXPECTED_ROW_COUNTS}")
    ok("pet spritesheet is v2 and row counts match")


def validate_assets() -> None:
    require_image_size(ROOT / "assets" / "tarsy-github-banner.png", (1280, 640), animated=False)
    require_image_size(ROOT / "assets" / "tarsy-github-banner.gif", (1280, 640), animated=True)
    icon_path = PLUGIN / "assets" / "icon_tarsy.png"
    require_file(icon_path)
    with Image.open(icon_path) as icon:
        if icon.width != icon.height or icon.width < 512:
            fail(f"{icon_path.relative_to(ROOT)} must be square and at least 512x512, got {icon.size}")
        if getattr(icon, "n_frames", 1) != 1:
            fail(f"{icon_path.relative_to(ROOT)} should be static")
    ok(f"{icon_path.relative_to(ROOT)} is a square {icon.width}x{icon.height} icon")


def validate_gif_frames() -> None:
    path = ROOT / "assets" / "tarsy-github-banner.gif"
    with Image.open(path) as image:
        frames = sum(1 for _ in ImageSequence.Iterator(image))
    if frames != 6:
        fail(f"banner GIF has {frames} frames, expected 6")
    ok("banner GIF has 6 frames")


def main() -> None:
    validate_marketplace()
    validate_manifest()
    validate_skill()
    validate_pet()
    validate_assets()
    validate_gif_frames()
    ok("Tarsy repository validation passed")


if __name__ == "__main__":
    main()
