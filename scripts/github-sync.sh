#!/usr/bin/env bash
set -euo pipefail

# Usage:
#   bash scripts/github-sync.sh <repo-url> [branch]
# Example:
#   bash scripts/github-sync.sh https://github.com/username/doserly.git work

REPO_URL="${1:-}"
BRANCH="${2:-$(git branch --show-current)}"

if [[ -z "$REPO_URL" ]]; then
  echo "❌ لازم تضيف رابط الريبو على GitHub."
  echo "مثال: bash scripts/github-sync.sh https://github.com/username/doserly.git work"
  exit 1
fi

if ! git rev-parse --git-dir >/dev/null 2>&1; then
  echo "❌ المجلد الحالي ليس Git repository."
  exit 1
fi

if ! git remote get-url origin >/dev/null 2>&1; then
  git remote add origin "$REPO_URL"
else
  git remote set-url origin "$REPO_URL"
fi

git push -u origin "$BRANCH"
echo "✅ تم رفع الفرع '$BRANCH' إلى GitHub."
