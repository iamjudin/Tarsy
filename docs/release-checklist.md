# Release Checklist

Use this before tagging a public Tarsy release and after every public-facing change.

## Assets

- Confirm branding assets:
  - `assets/tarsy-github-banner.gif`
  - `assets/tarsy-github-banner.png`
  - `plugins/tarsy/assets/icon_tarsy.png`
- Confirm the optional pet package:
  - `plugins/tarsy/pets/tarsy/pet.json`
  - `plugins/tarsy/pets/tarsy/spritesheet.webp`

## Validation

Run from the repository root before pushing:

```bash
scripts/validate.sh
git diff --check
```

## Publish Flow

All user-facing changes must go through the public GitHub repository. Do not use a local marketplace as the final verification path.

```bash
git push origin main
```

Then confirm GitHub sees the pushed version:

```bash
gh repo view iamjudin/Tarsy --json nameWithOwner,visibility,url,defaultBranchRef,description,pushedAt
gh run list --repo iamjudin/Tarsy --limit 3
curl -L https://raw.githubusercontent.com/iamjudin/Tarsy/main/README.md
curl -L https://raw.githubusercontent.com/iamjudin/Tarsy/main/plugins/tarsy/.codex-plugin/plugin.json
```

If README wording, plugin metadata, icon paths, install commands, pet paths, or GitHub description changed, update the GitHub page/metadata in the same pass. Apparently public documentation does not update itself. Bold choice, universe.

## Public Smoke Test

Run README instructions in a clean temporary Codex home:

```bash
rm -rf /private/tmp/tarsy-readme-smoke
mkdir -p /private/tmp/tarsy-readme-smoke
CODEX_HOME=/private/tmp/tarsy-readme-smoke codex plugin marketplace add iamjudin/Tarsy
CODEX_HOME=/private/tmp/tarsy-readme-smoke codex plugin add tarsy@tarsy
HOME=/private/tmp/tarsy-readme-smoke CODEX_HOME=/private/tmp/tarsy-readme-smoke /private/tmp/tarsy-readme-smoke/.tmp/marketplaces/tarsy/scripts/install-pet.sh
```

Confirm:

- `tarsy@tarsy` installs from `/private/tmp/tarsy-readme-smoke/.tmp/marketplaces/tarsy`.
- Installed plugin version matches public `plugin.json`.
- Installed icon path matches manifest, currently `assets/icon_tarsy.png`.
- No stale `assets/icon.png` exists in the installed public plugin.
- Pet install creates `pet.json` and `spritesheet.webp` under the temporary `CODEX_HOME`.

## Codex App Check

After public smoke test, install or upgrade from the public marketplace in the real Codex app:

```bash
codex plugin marketplace add iamjudin/Tarsy
codex plugin add tarsy@tarsy
```

Start a new Codex chat and invoke:

```text
$tarsy
```

Confirm:

- the plugin card shows the latest icon and metadata;
- the skill changes tone only;
- semantic auto-activation works for obvious brainstorming/reflection prompts;
- Tarsy steps back for functional plugin workflows and structured artifacts;
- the pet appears after selecting Tarsy and restarting/reselecting if needed.

## Release

- Tag `v0.1.0` when the release is ready.
- Create the GitHub Release.
- Re-run the public smoke test after the release is visible.
