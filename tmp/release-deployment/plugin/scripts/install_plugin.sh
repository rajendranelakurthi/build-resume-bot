#!/usr/bin/env bash
set -euo pipefail

PLUGIN_ROOT="${1:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
HOME_DIR="${2:-$HOME}"

PLUGIN_NAME="$(basename "$PLUGIN_ROOT")"
TARGET_PLUGIN_ROOT="$HOME_DIR/plugins/$PLUGIN_NAME"
MARKETPLACE_PATH="$HOME_DIR/.agents/plugins/marketplace.json"
SOURCE_MANIFEST_PATH="$PLUGIN_ROOT/.codex-plugin/plugin.json"
INSTALLED_MANIFEST_PATH="$TARGET_PLUGIN_ROOT/.codex-plugin/plugin.json"

SOURCE_VERSION="$(python3 - <<'PY' "$SOURCE_MANIFEST_PATH"
import json, sys
print(json.load(open(sys.argv[1], encoding='utf-8'))["version"])
PY
)"

PREVIOUS_VERSION=""
if [[ -f "$INSTALLED_MANIFEST_PATH" ]]; then
  PREVIOUS_VERSION="$(python3 - <<'PY' "$INSTALLED_MANIFEST_PATH"
import json, sys
print(json.load(open(sys.argv[1], encoding='utf-8'))["version"])
PY
)"
fi

mkdir -p "$(dirname "$TARGET_PLUGIN_ROOT")"
mkdir -p "$(dirname "$MARKETPLACE_PATH")"
rm -rf "$TARGET_PLUGIN_ROOT"
cp -R "$PLUGIN_ROOT" "$TARGET_PLUGIN_ROOT"

python3 - <<'PY' "$MARKETPLACE_PATH" "$PLUGIN_NAME"
import json, os, sys

marketplace_path = sys.argv[1]
plugin_name = sys.argv[2]

if os.path.exists(marketplace_path):
    with open(marketplace_path, encoding="utf-8") as fh:
        payload = json.load(fh)
else:
    payload = {
        "name": "local-plugins",
        "interface": {"displayName": "Local Plugins"},
        "plugins": [],
    }

plugins = payload.setdefault("plugins", [])
if not any(item.get("name") == plugin_name for item in plugins):
    plugins.append(
        {
            "name": plugin_name,
            "source": {"source": "local", "path": f"./plugins/{plugin_name}"},
            "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
            "category": "Productivity",
        }
    )

with open(marketplace_path, "w", encoding="utf-8") as fh:
    json.dump(payload, fh, indent=2)
PY

if [[ -n "$PREVIOUS_VERSION" ]]; then
  echo "Updated $PLUGIN_NAME from version $PREVIOUS_VERSION to $SOURCE_VERSION"
else
  echo "Installed $PLUGIN_NAME version $SOURCE_VERSION"
fi
echo "Installed plugin to $TARGET_PLUGIN_ROOT"
echo "Updated marketplace $MARKETPLACE_PATH"
echo "Restart Codex to pick up the plugin."
