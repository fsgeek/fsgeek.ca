#!/usr/bin/env bash
# Put the last-pushed commit on main live: ssh in and git pull.
# Run this deliberately, after you've reviewed and pushed -- it does not
# run automatically on push.
#
# Usage: scripts/deploy.sh
set -euo pipefail

HOST="activitycontext.work"
REMOTE="/var/www/fsgeek.ca"
PUBLIC="https://fsgeek.ca"

echo "== 1. pull latest main on $HOST =="
ssh -o BatchMode=yes "$HOST" "cd $REMOTE && git pull"

echo "== 2. spot-check the live site =="
fail=0
for path in / /log/; do
  code=$(curl -s -o /dev/null -w '%{http_code}' --max-time 15 "$PUBLIC$path")
  printf '  %-8s -> %s\n' "$path" "$code"
  [[ "$code" == "200" ]] || fail=1
done

if (( fail )); then
  echo "SITE DID NOT RESPOND 200 after deploy -- check it by hand." >&2
  exit 1
fi

echo
echo "Deployed."
