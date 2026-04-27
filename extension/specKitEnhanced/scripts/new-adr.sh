#!/usr/bin/env bash
# Allocates next ADR-NNNN id by scanning specs/adr/*.md and prints it.
# Usage: new-adr.sh <specs_root> <slug>
set -euo pipefail

specs_root="${1:-specs}"
slug="${2:-change}"
adr_dir="${specs_root}/adr"
mkdir -p "${adr_dir}"

max=0
for f in "${adr_dir}"/ADR-[0-9][0-9][0-9][0-9]-*.md 2>/dev/null; do
  [ -f "$f" ] || continue
  n="$(basename "$f" | sed -E 's/^ADR-([0-9]{4})-.*/\1/')"
  n="${n#0}"; n="${n#0}"; n="${n#0}"
  [ -z "$n" ] && n=0
  if [ "$n" -gt "$max" ]; then max="$n"; fi
done
next=$((max + 1))
printf "%04d\n" "$next"
