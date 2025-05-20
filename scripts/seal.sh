#!/usr/bin/env bash

set -euo pipefail

if [ $# -ne 1 ]; then
    echo "Usage: seal.sh <template_file>" >&2
    exit 1
fi

source .env
TEMPLATE_FILE="$1"
TEMPLATE_FILE_NAME="$(basename "$1")"
OUTPUT_FILE="$OUTPUT_DIR/$TEMPLATE_FILE_NAME"
touch "$OUTPUT_FILE"
./scripts/render.py "$TEMPLATE_FILE" | kubeseal  --format yaml > "$OUTPUT_FILE"
