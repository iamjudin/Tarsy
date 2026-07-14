#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLUGIN_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
SOURCE_DIR="$PLUGIN_DIR/pets/tarsy"
TARGET_DIR="${CODEX_HOME:-$HOME/.codex}/pets/tarsy"

if [[ ! -f "$SOURCE_DIR/pet.json" || ! -f "$SOURCE_DIR/spritesheet.webp" ]]; then
  echo "Tarsy pet package not found at $SOURCE_DIR" >&2
  exit 1
fi

mkdir -p "$TARGET_DIR"
cp "$SOURCE_DIR/pet.json" "$TARGET_DIR/pet.json"
cp "$SOURCE_DIR/spritesheet.webp" "$TARGET_DIR/spritesheet.webp"

echo "Installed Tarsy pet to $TARGET_DIR"
echo "Restart Codex or reselect Tarsy if the old pet is cached."
