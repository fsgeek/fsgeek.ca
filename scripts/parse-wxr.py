#!/usr/bin/env python3
"""Extract posts, pages, and the media manifest out of a WordPress WXR export.

Raw content:encoded HTML is preserved as-is (no markdown conversion) so this
is a lossless intermediate form, not a finished site. Output:
  content/posts/<slug>.html   (frontmatter + raw HTML body)
  content/pages/<...>.html    (mirrors WordPress page hierarchy)
  tmp/media-manifest.tsv      (url, local relative path, parent post_id)
"""
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

NS = {
    'wp': 'http://wordpress.org/export/1.2/',
    'content': 'http://purl.org/rss/1.0/modules/content/',
    'excerpt': 'http://purl.org/rss/1.0/excerpt/',
    'dc': 'http://purl.org/dc/elements/1.1/',
}

CONTROL_CHARS = re.compile(r'[\x00-\x08\x0B\x0C\x0E-\x1F]')


def load(path):
    raw = Path(path).read_text(encoding='utf-8')
    stripped = []
    for m in CONTROL_CHARS.finditer(raw):
        ctx = raw[max(0, m.start() - 20):m.start() + 20].replace('\n', ' ')
        stripped.append((hex(ord(m.group())), ctx))
    clean = CONTROL_CHARS.sub('', raw)
    return ET.fromstring(clean), stripped


def txt(item, tag):
    e = item.find(tag, NS)
    return e.text if e is not None and e.text else ''


def terms(item, domain):
    return [c.text for c in item.findall('category')
            if c.attrib.get('domain') == domain and c.text]


def yaml_str(s):
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'


def yaml_list(items):
    if not items:
        return '[]'
    return '[' + ', '.join(yaml_str(i) for i in items) + ']'


def slugify_fallback(title, post_id):
    base = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
    return f"{base or 'untitled'}-{post_id}"


def frontmatter(item, extra=None):
    lines = ['---']
    lines.append(f"title: {yaml_str(txt(item, 'title'))}")
    lines.append(f"date: {yaml_str(txt(item, 'wp:post_date'))}")
    lines.append(f"status: {yaml_str(txt(item, 'wp:status'))}")
    lines.append(f"original_url: {yaml_str(txt(item, 'link'))}")
    lines.append(f"post_id: {txt(item, 'wp:post_id')}")
    cats = terms(item, 'category')
    tags = terms(item, 'post_tag')
    if cats:
        lines.append(f"categories: {yaml_list(cats)}")
    if tags:
        lines.append(f"tags: {yaml_list(tags)}")
    if extra:
        for k, v in extra.items():
            lines.append(f"{k}: {v}")
    lines.append('---')
    return '\n'.join(lines)


def write_item(item, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    body = txt(item, 'content:encoded')
    path.write_text(frontmatter(item) + '\n\n' + body + '\n', encoding='utf-8')


def main():
    xml_path = sys.argv[1] if len(sys.argv) > 1 else 'tmp/afilesystemgeek.WordPress.2026-07-28.xml'
    root, stripped = load(xml_path)
    items = root.find('channel').findall('item')

    if stripped:
        print(f"stripped {len(stripped)} invalid XML control chars (source-data corruption, not touched further):")
        for code, ctx in stripped:
            print(f"  {code}: ...{ctx}...")
        print()

    posts = [it for it in items if txt(it, 'wp:post_type') == 'post']
    pages = [it for it in items if txt(it, 'wp:post_type') == 'page']
    attachments = [it for it in items if txt(it, 'wp:post_type') == 'attachment']

    out_root = Path('content')
    posts_dir = out_root / 'posts'
    pages_dir = out_root / 'pages'

    seen_slugs = {}
    for it in posts:
        slug = txt(it, 'wp:post_name')
        pid = txt(it, 'wp:post_id')
        if not slug:
            slug = slugify_fallback(txt(it, 'title'), pid)
        if slug in seen_slugs:
            slug = f"{slug}-{pid}"
        seen_slugs[slug] = pid
        write_item(it, posts_dir / f"{slug}.html")

    # Build page id -> slug map, then resolve full paths via post_parent chain.
    page_by_id = {txt(p, 'wp:post_id'): p for p in pages}

    def page_path(p, seen=None):
        seen = seen or set()
        pid = txt(p, 'wp:post_id')
        if pid in seen:
            raise ValueError(f"cycle in page hierarchy at post_id {pid}")
        seen.add(pid)
        slug = txt(p, 'wp:post_name') or slugify_fallback(txt(p, 'title'), pid)
        parent_id = txt(p, 'wp:post_parent')
        if parent_id and parent_id != '0' and parent_id in page_by_id:
            return page_path(page_by_id[parent_id], seen) / slug
        return Path(slug)

    for p in pages:
        rel = page_path(p)
        write_item(p, pages_dir / rel.with_suffix('.html'))

    manifest_path = Path('tmp/media-manifest.tsv')
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    with manifest_path.open('w', encoding='utf-8') as f:
        f.write('url\tparent_post_id\tattached_file\n')
        for a in attachments:
            url = txt(a, 'wp:attachment_url')
            parent = txt(a, 'wp:post_parent')
            attached = ''
            for meta in a.findall('wp:postmeta', NS):
                key = meta.find('wp:meta_key', NS)
                if key is not None and key.text == '_wp_attached_file':
                    val = meta.find('wp:meta_value', NS)
                    attached = val.text if val is not None and val.text else ''
            if url:
                f.write(f"{url}\t{parent}\t{attached}\n")

    print(f"posts: {len(posts)} -> {posts_dir}")
    print(f"pages: {len(pages)} -> {pages_dir}")
    print(f"attachments: {len(attachments)} -> {manifest_path}")


if __name__ == '__main__':
    main()
