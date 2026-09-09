#!/usr/bin/env bash
# Build the site locally from content/. Does NOT touch the live server --
# that's scripts/deploy.sh, run separately once you're ready to go live.
#
# Usage: scripts/publish.sh
set -euo pipefail

GIT_ROOT=$(git rev-parse --show-toplevel)
cd "$GIT_ROOT"

echo "== 1. validate content/posts frontmatter =="
uv run python3 scripts/validate_posts.py

echo "== 2. render content/ -> live site tree =="
uv run python3 scripts/build-site.py

echo "== 3. regenerate sitemap.xml =="
uv run python3 scripts/gen-sitemap.py

echo
echo "Built. Review the changes, then:"
echo "  git status"
echo "  git add -A && git commit -m '...'"
echo "  scripts/deploy.sh    # when ready to go live"
