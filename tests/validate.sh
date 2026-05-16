#!/usr/bin/env bash
set -e
shopt -s nullglob
REPO="$(cd "$(dirname "$0")/.." && pwd)"
ERRORS=0

# Check plugin.json exists and has required fields
MANIFEST="$REPO/.claude-plugin/plugin.json"
if [[ ! -f "$MANIFEST" ]]; then
  echo "FAIL: .claude-plugin/plugin.json missing"
  ERRORS=$((ERRORS+1))
else
  for field in name description version; do
    if ! python3 -c "import json,sys; d=json.load(open('$MANIFEST')); assert '$field' in d, '$field missing'" 2>/dev/null; then
      echo "FAIL: plugin.json missing field: $field"
      ERRORS=$((ERRORS+1))
    fi
  done
  echo "PASS: plugin.json"
fi

# Check each SKILL.md has required frontmatter
for skill_dir in "$REPO"/skills/*/; do
  skill_name=$(basename "$skill_dir")
  skill_file="$skill_dir/SKILL.md"
  if [[ ! -f "$skill_file" ]]; then
    echo "FAIL: $skill_name missing SKILL.md"
    ERRORS=$((ERRORS+1))
    continue
  fi
  for field in name description; do
    if ! grep -q "^$field:" "$skill_file"; then
      echo "FAIL: $skill_name/SKILL.md missing frontmatter field: $field"
      ERRORS=$((ERRORS+1))
    fi
  done
  echo "PASS: $skill_name/SKILL.md"
done

[[ $ERRORS -eq 0 ]] && echo "All checks passed." && exit 0
echo "$ERRORS check(s) failed." && exit 1
