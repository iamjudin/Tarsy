# Tarsy Pet States Reference

This is the working reference for the Tarsy Codex pet. It describes the fixed
Codex pet atlas contract and the intended visual meaning of each animation row.

## Atlas Contract

- Final spritesheet: `1536x1872`
- Grid: `8` columns by `9` rows
- Cell size: `192x208`
- Format: `spritesheet.webp`
- Background: transparent
- Unused cells: fully transparent

## Rows

| Row | State | Frames | Purpose | Tarsy visual direction |
| --- | --- | ---: | --- | --- |
| 0 | `idle` | 6 | Calm resting baseline. | Tiny screen blink, subtle body bob, quiet servo breathing. First frame must work as static reduced-motion pet. |
| 1 | `running-right` | 8 | Dragging/moving right. | Modular blue blocks tilt and step right; no speed lines or dust. |
| 2 | `running-left` | 8 | Dragging/moving left. | Same as rightward movement, mirrored or redrawn safely; cadence must still alternate. |
| 3 | `waving` | 4 | Greeting/attention gesture. | One hinged panel/arm lifts in a dry little salute. No wave marks or floating effects. |
| 4 | `jumping` | 5 | Playful hop/hover. | Compressed body, lift, peak, descent, settle. No shadows, dust, or floor marks. |
| 5 | `failed` | 8 | Error, blocked, cancelled, or failed. | Slumped panels, dimmer eyes, tiny attached smoke puff if needed. No red X or detached symbols. |
| 6 | `waiting` | 6 | Waiting for approval, help, or user input. | Expectant lean, screen eyes looking up, small polite pause pose. Distinct from idle. |
| 7 | `running` | 6 | Codex is actively working. | Busy processing motion: panels click, eyes scan, inner light pulses. Not literal running. |
| 8 | `review` | 6 | Ready for review or inspecting output. | Focused lean/head tilt, narrowed screen eyes, precise inspection posture. |

## Naming

- Plugin/repo folder: `Tarsy`
- Pet id: `tarsy`
- Display name: `Tarsy`
- Russian name: `Тарси`

## Visual Brief

Tarsy should read as a native Codex-blue companion: compact, funny, modular, and
robotic. The shape can borrow the idea of hinged block mechanics from a dry
space-assistant archetype, but should not copy a film-accurate silhouette,
materials, markings, or proportions.

Useful constraints:

- Compact whole-body silhouette readable inside `192x208`.
- Strong Codex-blue palette with dark screen eyes and a few lighter highlights.
- No text, logos, UI, speech bubbles, floating punctuation, or scenery.
- No shadows, glows, detached dust, speed lines, or guide marks.
- Same face, proportions, material, palette, and block layout across all rows.

## Output Package

When the pet is built, the local custom pet package should be:

```text
${CODEX_HOME:-$HOME/.codex}/pets/tarsy/
├── pet.json
└── spritesheet.webp
```

`pet.json`:

```json
{
  "id": "tarsy",
  "displayName": "Tarsy",
  "description": "A dry little Codex-blue robot named Тарси with adjustable sarcasm.",
  "spritesheetPath": "spritesheet.webp"
}
```
