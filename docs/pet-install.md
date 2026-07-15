# Pet Install And Troubleshooting

Tarsy includes an optional Codex pet package at `plugins/tarsy/pets/tarsy`.

## Install

After adding the marketplace, run:

```bash
~/.codex/.tmp/marketplaces/tarsy/scripts/install-pet.sh
```

The script copies:

- `pet.json` to `~/.codex/pets/tarsy/pet.json`;
- `spritesheet.webp` to `~/.codex/pets/tarsy/spritesheet.webp`.

## Update

After a marketplace upgrade, run the installer again:

```bash
codex plugin marketplace upgrade tarsy
~/.codex/.tmp/marketplaces/tarsy/scripts/install-pet.sh
```

Then restart Codex or reselect the pet so cached sprites are reloaded. Yes, cache invalidation remains everyone's favorite tiny ceremony.

## If The Pet Does Not Appear

Check that the files exist:

```bash
ls -la ~/.codex/pets/tarsy
```

Expected files:

```text
pet.json
spritesheet.webp
```

Check that `pet.json` references the sheet:

```json
{
  "spriteVersionNumber": 2,
  "spritesheetPath": "spritesheet.webp"
}
```

If the files are correct but Codex still shows an older pet, restart Codex. If that does not help, temporarily select another pet and then select Tarsy again.

## If The Installer Path Does Not Exist

Make sure the marketplace was added first:

```bash
codex plugin marketplace add iamjudin/Tarsy
```

Then install Tarsy from Plugins before running the pet installer.

For local development, run from the repository root instead:

```bash
scripts/install-pet.sh
```
