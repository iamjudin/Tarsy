# Tarsy Face States Reference

Use these as component property variants for the robot face:

```text
face=neutral
face=blink
face=annoyed
face=waiting
face=failed
face=review
face=processing
```

The face should stay simple enough to read inside a `192x208` pet cell. Prefer
two eye shapes on a dark screen panel. Avoid tiny pupils, text, eyebrows that
become noise, and mouth details unless they remain readable at pet size.

| Face | Emoji vibe | Eye sketch | Figma shape guidance | Use in rows |
| --- | --- | --- | --- | --- |
| `neutral` | `🙂` / `😐` | `●  ●` | Two small rounded cyan capsules or dots, horizontally level. | `idle`, first frame of most states |
| `blink` | `😌` | `—  —` | Two short horizontal rounded bars; same positions as neutral eyes. | `idle`, `review`, transition frames |
| `annoyed` | `🙄` / `😒` | `▰  ▰` angled inward | Narrow slanted rounded rectangles, slight asymmetry if readable. | sarcastic idle accents, `review` |
| `waiting` | `🥺` / `🙂?` | `○  ○` raised | Slightly larger round eyes, placed a bit higher; optional tiny tilt of the whole screen, no question mark. | `waiting` |
| `failed` | `😵` / `😞` | `⌒  ⌒` or `×  ×` | Prefer dim drooping arcs or flat closed eyes. Use X eyes only if they read clearly and do not look like UI error icons. | `failed` |
| `review` | `🧐` / `🤨` | `◐  ◑` or `−  ●` | One eye narrowed or both narrowed; keep it precise and focused, not angry. | `review` |
| `processing` | `🤖` / `😶‍🌫️` | `▮ ▯` alternating | Two vertical or capsule bars that can alternate/pulse across frames. No code text or loading dots. | `running` |

## Recommended Variant Details

### `neutral`

Default dry little robot face. Keep it calm and almost expressionless. This is
the safest fallback when a row is more about body movement than emotion.

### `blink`

Use as a one-frame or two-frame micro-animation. The blink should not move the
screen or change the body pose by itself.

### `annoyed`

This is the sarcasm face. It should feel dry, unimpressed, and lightly comedic,
not hostile. Best shape: two narrow slanted capsules.

### `waiting`

Use when Codex needs approval or user input. The expression should look patient
and expectant. Bigger eyes are okay; floating punctuation is not.

### `failed`

Use for blocked, cancelled, or failed states. Prefer dim closed arcs because
they are softer and less UI-like than red/error symbols.

### `review`

Use when the work is ready for review. It should read as focused inspection:
narrowed eyes, one-eye squint, or a small head/screen tilt.

### `processing`

Use while Codex is working. The face can pulse between simple bar shapes across
frames. Keep it abstract; avoid literal code, terminal text, loading spinners,
or small UI marks.

## Figma Component Setup

Create a nested component set named `Tarsy Face` with these variants:

```text
face=neutral
face=blink
face=annoyed
face=waiting
face=failed
face=review
face=processing
```

Then place `Tarsy Face` inside the robot body component as a component
property. Keep the face component centered inside the screen so changing
variants does not shift the robot's silhouette or frame alignment.
