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

## State Semantics

### `idle`

Default resting state. Use this when Codex is present but not actively doing
anything attention-worthy in the current moment.

Tarsy should look alive but quiet: a tiny blink, a subtle body bob, or a small
servo-breathing motion. This row must be low-distraction because it can sit on
screen for a long time. The first frame also needs to work as a static
reduced-motion pet.

### `running-right`

Directional movement to the right. Use this when the pet overlay needs a
rightward locomotion/drag animation, for example when the pet is repositioning
or moving across the overlay.

Tarsy should clearly travel or lean right through body mechanics only. Avoid
speed lines, dust, shadows, or external effects; the direction should be clear
from the robot's pose and block movement.

### `running-left`

Directional movement to the left. This is the left-facing counterpart to
`running-right`, used for leftward movement/repositioning.

It can be mirrored from `running-right` only if the design remains visually
correct after mirroring. If face details, asymmetrical panels, marks, or lighting
make mirroring look wrong, redraw/export a dedicated left-facing row.

### `waving`

Greeting or attention state. Use this when the pet is being woken, introduced,
selected, or otherwise needs a friendly "hello, I'm here" gesture.

Tarsy should do a restrained mechanical salute or panel wave. Keep the gesture
clear inside the body silhouette. Do not add wave marks, sparkles, symbols, or
floating punctuation.

### `jumping`

Playful hop, lift, or excited acknowledgement. Use this when a small celebratory
or energetic reaction is appropriate, such as a successful activation or a
lightweight positive moment.

Tarsy should compress, rise, hit a peak, descend, and settle. Show motion by
body height and pose only. Avoid floor shadows, impact marks, dust, or bounce
pads because those become extraction noise in a transparent pet atlas.

### `failed`

Failure, cancellation, or blocked/error state. Use this when a task fails,
stops, gets cancelled, or reaches a state that should read as "something went
wrong."

Tarsy should slump, dim, fold inward, or look mildly defeated. Attached smoke or
tiny attached sparks are acceptable if they remain part of the sprite, but avoid
red X marks, detached symbols, and dramatic UI-like error graphics.

### `waiting`

Blocked-on-user-input state. Use this when Codex is waiting for approval,
clarification, credentials, a permission prompt, or another user decision.

Tarsy should look patient and expectant, not broken. A small lean, raised screen
eyes, or polite pause pose works well. This must be visually distinct from
`idle`, because it means the user needs to do something.

### `running`

Active work state. Use this while Codex is executing a command, editing files,
thinking through a task, generating output, running tests, or otherwise actively
working.

Despite the name, this is not foot-running. Tarsy should look like it is
processing: panels clicking, eyes scanning, inner light pulsing, tiny mechanical
busy motion. Avoid directional travel, sprinting poses, speed lines, or dust.

### `review`

Ready-for-review or inspection state. Use this when Codex has produced a result,
finished a meaningful step, or wants the user to inspect changes/output.

Tarsy should look focused and evaluative: a lean, narrowed eyes, screen tilt, or
precise inspection posture. This should feel competent and dry, not celebratory.

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
