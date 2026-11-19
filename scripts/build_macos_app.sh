#!/bin/bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRM_ROOT="$(cd "$ROOT/../srm_1d" && pwd)"
VENV="${VENV:-$ROOT/../.venv-srm}"

if [[ ! -x "$VENV/bin/python" ]]; then
    echo "Python environment not found: $VENV" >&2
    echo "Set VENV=/path/to/your/environment" >&2
    exit 1
fi

"$VENV/bin/python" -m pip install --upgrade pyinstaller
cd "$ROOT"

OPENMOTOR_SRM1D_PATH="$SRM_ROOT" \
SRM1D_OPENMOTOR_PATH="$ROOT" \
"$VENV/bin/python" -m PyInstaller \
    --clean --noconfirm \
    pyinstaller/macOneFile.spec

echo "Built app: $ROOT/dist/openMotor.app"
