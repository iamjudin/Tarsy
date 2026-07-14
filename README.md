# Tarsy

Tarsy adds dry sarcastic tone to Codex.

It keeps the useful parts boringly intact: honesty, accuracy, safety, and engineering judgment do not become adjustable settings. The sarcasm is tone only.

Tarsy also includes an optional Codex pet: a small Codex-blue robot companion.

## Install

In Terminal, run:

```bash
codex plugin marketplace add iamjudin/Tarsy
```

Then open Plugins in Codex, find **Tarsy**, click Add, and start a new chat.

Use Tarsy in a chat:

```text
$tarsy
```

## Install the pet

After adding the marketplace, install the optional pet from the marketplace snapshot:

```bash
~/.codex/.tmp/marketplaces/tarsy/scripts/install-pet.sh
```

If Codex already had Tarsy selected, restart Codex or reselect the pet so the app reloads the spritesheet.

## Update

In Terminal, run:

```bash
codex plugin marketplace upgrade tarsy
```

Then reinstall or upgrade Tarsy in Plugins and start a new chat.

To refresh the pet after an update, run:

```bash
~/.codex/.tmp/marketplaces/tarsy/scripts/install-pet.sh
```

## Development

Validate the plugin from the repository root:

```bash
PYTHONPATH=/private/tmp/tarsy-yaml-shim   python3 /Users/iamjudin/.codex/skills/.system/plugin-creator/scripts/validate_plugin.py plugins/tarsy
git diff --check
```

## License

Tarsy is source-available under the [PolyForm Noncommercial 1.0.0](LICENSE) license. It is free to use, modify, and redistribute for noncommercial purposes.
