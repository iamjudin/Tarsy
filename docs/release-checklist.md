# Release Checklist

Use this before tagging a public Tarsy release.

- Replace placeholder branding assets:
  - `assets/tarsy-github-banner.png`
  - `plugins/tarsy/assets/icon.png`
- Confirm the optional pet package:
  - `plugins/tarsy/pets/tarsy/pet.json`
  - `plugins/tarsy/pets/tarsy/spritesheet.webp`
- Validate the plugin:

```bash
PYTHONPATH=/private/tmp/tarsy-yaml-shim python3 \
  /Users/iamjudin/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py \
  plugins/tarsy
```

- Run script checks:

```bash
bash -n scripts/install-pet.sh
bash -n plugins/tarsy/scripts/install-pet.sh
git diff --check
```

- Smoke test the marketplace locally:

```bash
codex plugin marketplace add /Users/iamjudin/Desktop/Plugins/Tarsy
codex plugin add tarsy@tarsy
scripts/install-pet.sh
```

- Publish:
  - push `main` to `iamjudin/Tarsy`;
  - tag `v0.1.0`;
  - create the GitHub Release;
  - test install with `codex plugin marketplace add iamjudin/Tarsy`.
