#!/usr/bin/env python3
"""Generate sitemap.xml from content/posts and content/pages frontmatter.

Mirrors the URL logic in build-site.py: posts -> /log/<slug>/, pages ->
mapped path with my-research->research and about-me->about renames, raw
passthrough pages -> /teaching/<stem>/. Skips anything build-site.py would
skip (status != publish, SKIP_PAGES).

Re-run this after publishing or removing content and redeploy sitemap.xml
to the server (it lives at repo root, alongside robots.txt).
"""
import re
from pathlib import Path

RENAME_ROOT = {'my-research': 'research', 'about-me': 'about'}
RAW_PASSTHROUGH = {'ai-development-environment-setup', 'cloud-development-kit'}
SKIP_PAGES = {'prior-classes-1442', 'privacy', 'privacy-policy'}

FM_RE = re.compile(r'^---\n(.*?)\n---\n\n(.*)$', re.DOTALL)

STATIC_URLS = [
    'https://fsgeek.ca/',
    'https://fsgeek.ca/log/',
    'https://fsgeek.ca/privacy/',
]


def parse_fm(path):
    text = path.read_text(encoding='utf-8')
    m = FM_RE.match(text)
    fm = {}
    for line in m.group(1).splitlines():
        k, _, v = line.partition(':')
        v = v.strip()
        if v.startswith('"') and v.endswith('"'):
            v = v[1:-1]
        fm[k.strip()] = v
    return fm


def main():
    root = Path('.')
    urls = list(STATIC_URLS)

    for f in sorted((root / 'content/posts').glob('*.html')):
        fm = parse_fm(f)
        if fm.get('status') != 'publish':
            continue
        urls.append(f'https://fsgeek.ca/log/{f.stem}/')

    for f in sorted((root / 'content/pages').glob('**/*.html')):
        rel = f.relative_to(root / 'content/pages')
        rel_no_ext = str(rel.with_suffix('')).replace('\\', '/')
        stem = f.stem
        if stem in SKIP_PAGES:
            continue
        fm = parse_fm(f)
        if fm.get('status') != 'publish':
            continue
        if stem in RAW_PASSTHROUGH:
            urls.append(f'https://fsgeek.ca/teaching/{stem}/')
            continue
        parts = rel_no_ext.split('/')
        mapped_parts = [RENAME_ROOT.get(parts[0], parts[0])] + parts[1:]
        urls.append('https://fsgeek.ca/' + '/'.join(mapped_parts) + '/')

    urls = sorted(set(urls))

    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        lines.append(f'  <url><loc>{u}</loc></url>')
    lines.append('</urlset>')

    out = root / 'sitemap.xml'
    out.write_text('\n'.join(lines) + '\n', encoding='utf-8')
    print(f'wrote {len(urls)} URLs to {out}')


if __name__ == '__main__':
    main()
