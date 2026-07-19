![Tarsy banner](assets/tarsy-github-banner.gif)

# Tarsy

Tarsy adds default-on dry sarcastic tone to Codex when enabled.

It keeps the useful parts boringly intact: honesty, accuracy, safety, and engineering judgment do not become adjustable settings. The sarcasm is tone only. Yes, apparently we are preserving reality as a feature.

Tarsy also includes an optional Codex pet: a small Codex-blue robot companion.

## Features

- Default-on dry sarcastic tone for Codex once Tarsy is enabled.
- No `$tarsy` prompt required; installation and enablement are the opt-in.
- Strong compatibility rules: functional plugins keep their job, while Tarsy keeps the conversational voice unless another plugin is explicitly about tone, persona, brand voice, or formal domain style.
- No sarcasm levels, honesty sliders, or other knobs pretending to be product strategy.
- Safety, factuality, uncertainty, and engineering discipline stay unchanged.
- Optional animated Tarsy pet for Codex.
- Marketplace-ready package layout under `plugins/tarsy`.

## Install

Add the marketplace from GitHub:

```bash
codex plugin marketplace add iamjudin/Tarsy
```

Then open Plugins in Codex, find **Tarsy**, click Add, and start a new chat.

When enabled, Tarsy is the default conversational voice in new chats. You do not need to invoke `$tarsy`; apparently enabling a tone plugin now means using the tone plugin. Progress.

Tarsy stays in charge of conversational tone when other functional plugins are active, as long as it does not change their task, validation, artifact format, or safety requirements. It steps back for plugins that are explicitly about tone, persona, brand voice, formal domain style, or when you ask for a neutral/formal response. The sarcasm is allowed to have boundaries. Advanced civilization, apparently.

Tarsy can be suppressed when you ask for a neutral, strict, formal, or non-sarcastic response, for example:

```text
without Tarsy
```

## Install The Pet

After adding the marketplace, install the optional pet from the marketplace snapshot:

```bash
~/.codex/.tmp/marketplaces/tarsy/scripts/install-pet.sh
```

If Codex already had Tarsy selected, restart Codex or reselect the pet so the app reloads the spritesheet.

More details and troubleshooting live in [docs/pet-install.md](docs/pet-install.md).

## Update

Upgrade the marketplace snapshot:

```bash
codex plugin marketplace upgrade tarsy
```

Then reinstall or upgrade Tarsy in Plugins and start a new chat.

Refresh the pet after an update:

```bash
~/.codex/.tmp/marketplaces/tarsy/scripts/install-pet.sh
```

## Development

Validate the repository from the root:

```bash
scripts/validate.sh
```

Local marketplace smoke test:

```bash
codex plugin marketplace add /path/to/Tarsy
codex plugin add tarsy@tarsy
scripts/install-pet.sh
```

The plugin source package is in `plugins/tarsy`. The root repository contains release docs, GitHub assets, and helper scripts.

## Contributing

Issues and pull requests are welcome for bug reports, docs improvements, packaging fixes, and pet asset refinements. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Tarsy is source-available under the [PolyForm Noncommercial 1.0.0](LICENSE) license. It is free to use, modify, and redistribute for noncommercial purposes.
