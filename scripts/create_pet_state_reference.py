#!/usr/bin/env python3
"""Create a schematic Tarsy pet state reference sheet."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "pet-state-reference.png"

CELL_W = 112
CELL_H = 104
LABEL_W = 188
HEADER_H = 68
ROWS = [
    ("idle", 6, "blink + calm bob"),
    ("running-right", 8, "drag right"),
    ("running-left", 8, "drag left"),
    ("waving", 4, "panel salute"),
    ("jumping", 5, "compress, lift, settle"),
    ("failed", 8, "slump + dim eyes"),
    ("waiting", 6, "expectant lean"),
    ("running", 6, "processing, not jogging"),
    ("review", 6, "focused inspect"),
]

BLUE = (38, 135, 255)
BLUE_2 = (95, 178, 255)
DARK = (18, 28, 43)
INK = (28, 32, 38)
MUTED = (93, 103, 116)
GRID = (222, 228, 236)
BG = (250, 252, 255)
TRANSPARENT_HINT = (238, 244, 252)


def font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


FONT_TITLE = font(26, True)
FONT_LABEL = font(15, True)
FONT_SMALL = font(12)
FONT_TINY = font(10)


def rounded(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], radius: int, fill, outline=None, width: int = 1) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def draw_tarsy(draw: ImageDraw.ImageDraw, cx: int, cy: int, state: str, frame: int, frames: int) -> None:
    t = frame / max(frames - 1, 1)
    bob = 0
    lean = 0
    arm = 0
    scale_y = 1.0
    eye_h = 5
    eye_y = 0
    smoke = False

    if state == "idle":
        bob = -2 if frame in (1, 2) else 0
        eye_h = 2 if frame == 2 else 5
    elif state == "running-right":
        cx += int((t - 0.5) * 34)
        lean = 5
        bob = -4 if frame % 2 else 2
    elif state == "running-left":
        cx -= int((t - 0.5) * 34)
        lean = -5
        bob = -4 if frame % 2 else 2
    elif state == "waving":
        arm = [0, -18, -24, -8][frame]
    elif state == "jumping":
        offsets = [10, 0, -22, -10, 8]
        squish = [0.86, 1.0, 1.05, 1.0, 0.92]
        bob = offsets[frame]
        scale_y = squish[frame]
    elif state == "failed":
        lean = -5
        bob = 8
        eye_h = 2
        smoke = frame in (3, 4, 5)
    elif state == "waiting":
        lean = -3
        bob = -2 if frame in (2, 3) else 1
        eye_y = -2
    elif state == "running":
        bob = -2 if frame % 2 else 1
        eye_h = 4
        arm = -8 if frame % 2 else 5
    elif state == "review":
        lean = 4
        eye_h = 3
        eye_y = -1

    body_w = 42
    body_h = int(58 * scale_y)
    x0 = cx - body_w // 2 + lean
    y0 = cy - body_h // 2 + bob
    x1 = x0 + body_w
    y1 = y0 + body_h

    rounded(draw, (x0, y0, x1, y1), 10, BLUE, DARK, 2)
    rounded(draw, (x0 + 6, y0 + 8, x1 - 6, y0 + 25), 5, DARK)

    eye_offset = 7
    rounded(draw, (cx - eye_offset - 5 + lean, y0 + 14 + eye_y, cx - eye_offset + 5 + lean, y0 + 14 + eye_y + eye_h), 2, BLUE_2)
    rounded(draw, (cx + eye_offset - 5 + lean, y0 + 14 + eye_y, cx + eye_offset + 5 + lean, y0 + 14 + eye_y + eye_h), 2, BLUE_2)

    for i in range(3):
        yy = y0 + 33 + i * 8
        draw.line((x0 + 9, yy, x1 - 9, yy), fill=(16, 84, 160), width=2)

    left_leg = (x0 + 8, y1 - 1, x0 + 17, y1 + 16 + (3 if state in {"running-right", "running-left"} and frame % 2 else 0))
    right_leg = (x1 - 17, y1 - 1, x1 - 8, y1 + 16 + (0 if state in {"running-right", "running-left"} and frame % 2 else 3))
    rounded(draw, left_leg, 4, BLUE, DARK, 1)
    rounded(draw, right_leg, 4, BLUE, DARK, 1)

    arm_y = y0 + 34
    if state in {"waving", "running"}:
        draw.line((x1 - 1, arm_y, x1 + 18, arm_y + arm), fill=DARK, width=5)
        draw.line((x1, arm_y, x1 + 17, arm_y + arm), fill=BLUE_2, width=3)
    else:
        rounded(draw, (x1 - 1, arm_y, x1 + 11, arm_y + 25), 5, BLUE_2, DARK, 1)

    rounded(draw, (x0 - 11, arm_y, x0 + 1, arm_y + 25), 5, BLUE_2, DARK, 1)

    if smoke:
        draw.ellipse((x1 - 2, y0 - 4, x1 + 11, y0 + 8), fill=(120, 149, 180), outline=DARK)


def main() -> None:
    width = LABEL_W + CELL_W * 8 + 36
    height = HEADER_H + CELL_H * len(ROWS) + 48
    image = Image.new("RGB", (width, height), BG)
    draw = ImageDraw.Draw(image)

    draw.text((18, 10), "Tarsy pet state reference", font=FONT_TITLE, fill=INK)
    draw.text((18, 42), "8 atlas columns; unused cells should be transparent", font=FONT_SMALL, fill=MUTED)

    y = HEADER_H
    for row_idx, (state, frames, note) in enumerate(ROWS):
        row_top = y + row_idx * CELL_H
        fill = (255, 255, 255) if row_idx % 2 == 0 else (246, 249, 253)
        draw.rectangle((0, row_top, width, row_top + CELL_H), fill=fill)
        draw.line((0, row_top, width, row_top), fill=GRID)

        draw.text((18, row_top + 18), f"{row_idx}. {state}", font=FONT_LABEL, fill=INK)
        draw.text((18, row_top + 40), f"{frames} frames", font=FONT_SMALL, fill=MUTED)
        draw.text((18, row_top + 59), note, font=FONT_TINY, fill=MUTED)

        for col in range(8):
            x = LABEL_W + col * CELL_W
            box = (x + 8, row_top + 8, x + CELL_W - 8, row_top + CELL_H - 8)
            if col < frames:
                rounded(draw, box, 8, (255, 255, 255), GRID, 1)
                draw_tarsy(draw, x + CELL_W // 2, row_top + 52, state, col, frames)
                draw.text((x + 14, row_top + CELL_H - 24), f"f{col + 1}", font=FONT_TINY, fill=MUTED)
            else:
                rounded(draw, box, 8, TRANSPARENT_HINT, GRID, 1)
                draw.line((box[0] + 10, box[1] + 10, box[2] - 10, box[3] - 10), fill=(205, 216, 230), width=1)
                draw.line((box[0] + 10, box[3] - 10, box[2] - 10, box[1] + 10), fill=(205, 216, 230), width=1)

    draw.line((0, height - 31, width, height - 31), fill=GRID)
    draw.text((18, height - 23), "Schematic only: final pet must be generated as a transparent 1536x1872 spritesheet.", font=FONT_SMALL, fill=MUTED)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    image.save(OUT)
    print(OUT)


if __name__ == "__main__":
    main()
