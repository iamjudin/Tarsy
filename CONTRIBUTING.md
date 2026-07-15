# Contributing

Thanks for helping improve Tarsy. Keep changes focused, easy to review, and boringly verifiable. Naturally, the robot approves of boring verification.

## Good Contributions

- Fix plugin packaging or marketplace install issues.
- Improve the Tarsy skill while preserving the tone-only contract.
- Improve pet assets, pet docs, or validation checks.
- Clarify README, changelog, or release instructions.

## Tone Rules

Tarsy may be sarcastic, but the plugin must not become hostile. Keep these constraints intact:

- Sarcasm changes style only.
- Honesty, accuracy, safety, and uncertainty disclosure are not configurable.
- Do not add numeric sarcasm levels or an honesty setting.
- Keep user-facing sarcasm dry and restrained.

## Development

Run validation before opening a pull request:

```bash
scripts/validate.sh
```

If you touch pet assets, confirm that:

- `plugins/tarsy/pets/tarsy/pet.json` still points to `spritesheet.webp`;
- the spritesheet is a Codex v2 sheet: 1536x2288, 8 columns, 11 rows;
- the row frame counts match the expected Tarsy actions.

## Pull Requests

Please include:

- what changed;
- how you tested it;
- screenshots or GIFs for visual pet changes;
- any install/update notes users should know.
