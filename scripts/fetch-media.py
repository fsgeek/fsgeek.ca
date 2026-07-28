#!/usr/bin/env python3
"""Download media referenced in tmp/media-manifest.tsv from the live site.

Preserves the WordPress uploads path layout under media/, e.g.
media/2016/11/llsfs4.jpg, so links already in content/ can be
rewritten later with a simple prefix swap.
"""
import csv
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

MANIFEST = Path('tmp/media-manifest.tsv')
OUT_DIR = Path('media')
USER_AGENT = 'fsgeek.ca-migration/1.0 (+https://fsgeek.ca)'


def target_path(url, attached_file):
    if attached_file:
        return OUT_DIR / attached_file
    # Fallback: everything after /wp-content/uploads/
    marker = '/wp-content/uploads/'
    idx = url.find(marker)
    if idx == -1:
        return OUT_DIR / '_unrecognized' / Path(url).name
    return OUT_DIR / url[idx + len(marker):]


def main():
    rows = list(csv.DictReader(MANIFEST.open(encoding='utf-8'), delimiter='\t'))
    total = len(rows)
    ok = skipped = failed = 0
    failures = []

    for i, row in enumerate(rows, 1):
        url = row['url']
        dest = target_path(url, row['attached_file'])
        if dest.exists() and dest.stat().st_size > 0:
            skipped += 1
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                dest.write_bytes(resp.read())
            ok += 1
        except (urllib.error.URLError, urllib.error.HTTPError) as e:
            failed += 1
            failures.append((url, str(e)))
        if i % 25 == 0 or i == total:
            print(f"{i}/{total}  ok={ok} skipped={skipped} failed={failed}")
        time.sleep(0.15)

    if failures:
        print("\nfailed:")
        for url, err in failures:
            print(f"  {url}  ({err})")

    print(f"\ndone: ok={ok} skipped={skipped} failed={failed} total={total}")
    return 1 if failures else 0


if __name__ == '__main__':
    sys.exit(main())
