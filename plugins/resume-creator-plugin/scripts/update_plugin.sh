#!/usr/bin/env bash
set -euo pipefail

PLUGIN_ROOT="${1:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
HOME_DIR="${2:-$HOME}"
INSTALL_SCRIPT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/install_plugin.sh"

if [[ ! -f "$INSTALL_SCRIPT" ]]; then
  echo "Missing install script at $INSTALL_SCRIPT" >&2
  exit 1
fi

echo "Updating plugin from $PLUGIN_ROOT"
bash "$INSTALL_SCRIPT" "$PLUGIN_ROOT" "$HOME_DIR"
