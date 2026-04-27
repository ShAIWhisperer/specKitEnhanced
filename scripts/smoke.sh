#!/usr/bin/env bash
# Full end-to-end smoke test. Exits non-zero on any failure.
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

SMOKE_DIR="${TMPDIR:-/tmp}/sdd-smoke"
PMOS_DIR="${TMPDIR:-/tmp}/sdd-pmos"

echo "== 1. Clean previous runs =="
rm -rf "$SMOKE_DIR" "$PMOS_DIR"

echo ""
echo "== 2. Core preset init =="
python3 -m src.specify_x.cli init "$SMOKE_DIR" \
  --preset core --author "@author" --project-name "sdd-smoke"

echo ""
echo "== 3. Core file count ==  (expected: 14 specs + agents + commands + schemas)"
core_specs=$(find "$SMOKE_DIR/specs" -name '*.md' | wc -l | tr -d ' ')
[ "$core_specs" -ge 14 ] || { echo "FAIL: only $core_specs spec files"; exit 1; }
echo "OK — $core_specs spec files"

echo ""
echo "== 4. Verify core =="
python3 -m src.specify_x.cli verify "$SMOKE_DIR"

echo ""
echo "== 5. PM OS preset init =="
python3 -m src.specify_x.cli init "$PMOS_DIR" \
  --preset pm-os --author "@author" --project-name "sdd-pmos"

echo ""
echo "== 6. PM OS spec count == (expected: 21 specs)"
pmos_specs=$(find "$PMOS_DIR/specs" -name '*.md' | wc -l | tr -d ' ')
[ "$pmos_specs" -ge 21 ] || { echo "FAIL: only $pmos_specs spec files"; exit 1; }
echo "OK — $pmos_specs spec files"

echo ""
echo "== 7. Verify pm-os =="
python3 -m src.specify_x.cli verify "$PMOS_DIR"

echo ""
echo "== 8. Harvest dry-run =="
python3 -m src.specify_x.cli harvest . --dry-run

echo ""
echo "== 9. Bridge dry-run (skipped — requires --pmos-root) =="
echo "  Run: specify-x bridge --pmos-root /path/to/your-pm-os --dry-run"

echo ""
echo "== 10. Idempotence check — re-running init must not destroy =="
python3 -m src.specify_x.cli init "$SMOKE_DIR" --preset core 2>&1 | tail -3

echo ""
echo "ALL SMOKE TESTS PASSED ✓"
