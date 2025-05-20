#!/usr/bin/env bash

set -euo pipefail

if [ $# -ne 2 ]; then
    echo "Usage: seal.sh <template_file> <output_file>" >&2
    exit 1
fi

TEMPLATE_FILE="$1"
OUTPUT_FILE="$2"
source .env
./scripts/render.py "$TEMPLATE_FILE" | kubeseal  --format yaml > "$OUTPUT_FILE"
