# Release Checklist

Use this before tagging a public Tarsy release.

## Assets

- Confirm branding assets:
  - `assets/tarsy-github-banner.gif`
  - `assets/tarsy-github-banner.png`
  - `plugins/tarsy/assets/icon.png`
- Confirm the optional pet package:
  - `plugins/tarsy/pets/tarsy/pet.json`
  - `plugins/tarsy/pets/tarsy/spritesheet.webp`

## Validation

Run from the repository root:

```bash
scripts/validate.sh
git diff --check
```

## Local Smoke Test

```bash
codex plugin marketplace add /Users/iamjudin/Desktop/Plugins/Tarsy
codex plugin add tarsy@tarsy
scripts/install-pet.sh
```

Start a new Codex chat and invoke:

```text
$tarsy
```

Confirm:

- the skill changes tone only;
- the plugin card shows the latest icon and metadata;
- the pet appears after selecting Tarsy and restarting/reselecting if needed.

## Publish

- Push `main` to `iamjudin/Tarsy`.
- Tag `v0.1.0` when the release is ready.
- Create the GitHub Release.
- Test public install with:

```bash
codex plugin marketplace add iamjudin/Tarsy
```
