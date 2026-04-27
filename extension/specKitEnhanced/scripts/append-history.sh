#!/usr/bin/env bash
# Appends a dated entry to specs/history.md.
# Usage: append-history.sh <specs_root> "<headline>" ["<body>"]
set -euo pipefail

specs_root="${1:?usage: append-history.sh <specs_root> <headline> [body]}"
headline="${2:?missing headline}"
body="${3:-}"
today="$(date +%Y-%m-%d)"
f="${specs_root}/history.md"

if [ ! -f "$f" ]; then
  echo "ERROR: ${f} does not exist. Run /speckit.x.history to scaffold first." >&2
  exit 1
fi

{
  printf '\n### %s — %s\n\n' "$today" "$headline"
  [ -n "$body" ] && printf '%s\n' "$body"
} >> "$f"

echo "Appended to $f"
