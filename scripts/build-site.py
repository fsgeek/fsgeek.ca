#!/usr/bin/env python3
"""Render content/posts and content/pages into the live static site tree.

Posts (status=publish) -> log/<slug>/index.html
Pages (status=publish) -> research/... or teaching/... or about/... etc,
  mirroring the directory structure content/pages already has, with
  my-research/ renamed to research/ and about-me/ renamed to about/.

Two pages (ai-development-environment-setup, cloud-development-kit) are
full standalone HTML documents pasted into WordPress whole; they're
relocated verbatim rather than run through the template, since merging
their embedded <style>/<script> into our template risks breaking them.

Draft/private content is skipped entirely (prior-classes-1442 among them).
"""
import re
from pathlib import Path

MONO = '"IBM Plex Mono", ui-monospace, monospace'
RENAME_ROOT = {'my-research': 'research', 'about-me': 'about'}
RAW_PASSTHROUGH = {'ai-development-environment-setup', 'cloud-development-kit'}
SKIP_PAGES = {
    'prior-classes-1442',  # draft; caught by status filter too, kept explicit for clarity
    'privacy',             # superseded by the hand-written /privacy/ (see write_privacy)
    'privacy-policy',      # superseded by the hand-written /privacy/ (see write_privacy)
}

FM_RE = re.compile(r'^---\n(.*?)\n---\n\n(.*)$', re.DOTALL)


def parse(path):
    text = path.read_text(encoding='utf-8')
    m = FM_RE.match(text)
    fm_raw, body = m.group(1), m.group(2)
    fm = {}
    for line in fm_raw.splitlines():
        key, _, val = line.partition(':')
        val = val.strip()
        if val.startswith('"') and val.endswith('"'):
            val = val[1:-1].replace('\\"', '"')
        elif val.startswith('['):
            val = [v.strip(' "') for v in val[1:-1].split(',') if v.strip(' "')]
        fm[key.strip()] = val
    return fm, body


def clean_body(body):
    body = re.sub(r'<!--\s*/?wp:.*?-->\n?', '', body)
    body = re.sub(r'\s+class=""', '', body)
    body = re.sub(r'<p\s+>', '<p>', body)
    body = re.sub(r'class="wp-block-heading"\s*', '', body)
    body = re.sub(r'<(strong|em) class="wpc-darklup-observer--node darklup--text wpc--darklup--observed">', r'<\1>', body)
    body = re.sub(r'https://i0\.wp\.com/fsgeek\.ca/wp-content/uploads/([^"?]+)\?[^"]*', r'/media/\1', body)
    body = re.sub(r'https?://fsgeek\.ca/wp-content/uploads/', '/media/', body)
    body = re.sub(r'\n{3,}', '\n\n', body).strip()
    return body


def wing_tag(categories):
    return 'teaching' if 'Teaching' in (categories or []) else 'research'


def breadcrumb(parts):
    crumbs = ['<a href="/">~</a>']
    acc = ''
    for i, p in enumerate(parts):
        acc += '/' + p
        if i == len(parts) - 1:
            crumbs.append(p)
        else:
            crumbs.append(f'<a href="{acc}/">{p}</a>')
    return ' / '.join(crumbs)


HEADER = '''<header class="site">
  <div class="wrap-wide site-row">
    <a class="wordmark" href="/"><span class="prompt">~/</span>fsgeek.ca</a>
    <nav class="primary" aria-label="Primary">
      <a href="/research/"{research_current}>research</a>
      <a href="/teaching/" class="teaching-link"{teaching_current}>teaching</a>
      <a href="/log/"{log_current}>log</a>
      <a href="https://wamason.com/">wamason.com</a>
    </nav>
  </div>
</header>'''

FOOTER = '''<footer class="site">
  <div class="wrap-wide">
    <a href="mailto:fsgeek@cs.ubc.ca">fsgeek@cs.ubc.ca</a>
    &middot; <a href="https://wamason.com/">wamason.com</a>
    &middot; <a href="https://github.com/fsgeek">github.com/fsgeek</a>
    &middot; <a href="/privacy/">privacy</a>
  </div>
</footer>'''


def header_for(section):
    return HEADER.format(
        research_current=' aria-current="page"' if section == 'research' else '',
        teaching_current=' aria-current="page"' if section == 'teaching' else '',
        log_current=' aria-current="page"' if section == 'log' else '',
    )


def page_shell(title, description, canonical, section, breadcrumb_html, body_html):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} &middot; fsgeek.ca</title>
  <meta name="description" content="{description}">
  <link rel="canonical" href="{canonical}">
  <link rel="stylesheet" href="/static/style.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>

{header_for(section)}

<main id="main">
  <div class="wrap">
    <div class="breadcrumb">{breadcrumb_html}</div>
{body_html}
  </div>
</main>

{FOOTER}

</body>
</html>
'''


def article_block(title, meta_html, body_html):
    return f'''    <article class="entry">
      <h1>{title}</h1>
      <div class="entry-meta">{meta_html}</div>
      <div class="entry-body">
{body_html}
      </div>
    </article>'''


def dirlisting(entries):
    rows = []
    for slug, href, desc, teaching in entries:
        cls = ' class="teaching-link"' if teaching else ''
        rows.append(
            f'        <div class="entry">\n'
            f'          <span class="perm">drwxr-xr-x</span>\n'
            f'          <span class="name"><a{cls} href="{href}">{slug}/</a></span>\n'
            f'          <span class="desc">{desc}</span>\n'
            f'        </div>'
        )
    return '      <div class="dirlisting">\n' + '\n'.join(rows) + '\n      </div>'


def pagelist(entries):
    items = '\n'.join(f'          <li><a href="{href}">{title}</a></li>' for _, href, title, _ in entries)
    return f'      <ul class="pagelist">\n{items}\n      </ul>'


def out_path_for_page(rel_no_ext):
    parts = rel_no_ext.split('/')
    parts[0] = RENAME_ROOT.get(parts[0], parts[0])
    return Path(*parts) / 'index.html'


def main():
    root = Path('.')
    posts_written = pages_written = skipped = raw_written = 0

    # ---- posts -> log/<slug>/ ----
    log_entries = []  # (date, tag, title, href) for homepage
    for f in sorted((root / 'content/posts').glob('*.html')):
        fm, body = parse(f)
        if fm.get('status') != 'publish':
            skipped += 1
            continue
        slug = f.stem
        out_dir = root / 'log' / slug
        out_dir.mkdir(parents=True, exist_ok=True)
        tag = wing_tag(fm.get('categories'))
        date = fm['date'][:10]
        meta_html = f'<span>{date}</span>\n        <span class="log-tag{" teaching" if tag == "teaching" else ""}">{tag}</span>'
        body_html = clean_body(body)
        page = page_shell(
            title=fm['title'],
            description=fm['title'],
            canonical=f'https://fsgeek.ca/log/{slug}/',
            section='log',
            breadcrumb_html=breadcrumb(['log', slug]),
            body_html=article_block(fm['title'], meta_html, body_html),
        )
        (out_dir / 'index.html').write_text(page, encoding='utf-8')
        log_entries.append((date, tag, fm['title'], f'/log/{slug}/'))
        posts_written += 1

    log_entries.sort(reverse=True)

    # ---- pages ----
    page_files = sorted((root / 'content/pages').glob('**/*.html'))
    # children_of[output-parent-dir-as-posix] = [(slug, href, title, is_teaching)]
    children_of = {}

    def register_child(parent_rel_parts, slug, href, title, is_teaching):
        key = '/'.join(parent_rel_parts)
        children_of.setdefault(key, []).append((slug, href, title, is_teaching))

    parsed_pages = []
    for f in page_files:
        rel = f.relative_to(root / 'content/pages')
        rel_no_ext = str(rel.with_suffix('')).replace('\\', '/')
        stem = f.stem
        if stem in SKIP_PAGES:
            skipped += 1
            continue
        fm, body = parse(f)
        if fm.get('status') != 'publish':
            skipped += 1
            continue

        if stem in RAW_PASSTHROUGH:
            out_dir = root / 'teaching' / stem
            out_dir.mkdir(parents=True, exist_ok=True)
            raw_body_full = f.read_text(encoding='utf-8')
            raw_doc = raw_body_full.split('---', 2)[2]
            raw_doc = re.sub(r'<!--\s*/?wp:.*?-->\n?', '', raw_doc).strip()
            (out_dir / 'index.html').write_text(raw_doc + '\n', encoding='utf-8')
            raw_written += 1
            continue

        parsed_pages.append((rel_no_ext, fm, body))

    for rel_no_ext, fm, body in parsed_pages:
        out_file = out_path_for_page(rel_no_ext)
        parts = rel_no_ext.split('/')
        mapped_parts = [RENAME_ROOT.get(parts[0], parts[0])] + parts[1:]
        section = mapped_parts[0] if mapped_parts[0] in ('research', 'teaching') else ''
        is_teaching = section == 'teaching'
        child_title = fm['title']
        href = '/' + '/'.join(mapped_parts) + '/'
        # register with its parent (one level up) so the parent can list it
        register_child(mapped_parts[:-1], mapped_parts[-1], href, child_title, is_teaching)

    for rel_no_ext, fm, body in parsed_pages:
        parts = rel_no_ext.split('/')
        mapped_parts = [RENAME_ROOT.get(parts[0], parts[0])] + parts[1:]
        section = mapped_parts[0] if mapped_parts[0] in ('research', 'teaching') else ''
        title = fm['title']
        out_file = root / out_path_for_page(rel_no_ext)
        out_file.parent.mkdir(parents=True, exist_ok=True)

        body_html = clean_body(body)
        kids = children_of.get('/'.join(mapped_parts), [])
        extra = ''
        if kids:
            use_fancy = rel_no_ext in ('my-research', 'teaching')
            kids_sorted = sorted(kids, key=lambda k: k[2])
            if use_fancy:
                entries = [(k[0], k[1], k[2], k[3]) for k in kids_sorted]
                extra = '\n' + dirlisting(entries)
            else:
                extra = '\n' + pagelist(kids_sorted)

        meta_html = f'<span>{fm["date"][:10]}</span>'
        page = page_shell(
            title=title,
            description=title,
            canonical=f'https://fsgeek.ca{"/" + "/".join(mapped_parts) + "/"}',
            section=section,
            breadcrumb_html=breadcrumb(mapped_parts),
            body_html=article_block(title, meta_html, body_html + extra),
        )
        out_file.write_text(page, encoding='utf-8')
        pages_written += 1

    write_homepage(root, log_entries[:12])
    write_log_index(root, log_entries)
    write_404(root)
    write_privacy(root)

    print(f'posts written: {posts_written}  pages written: {pages_written}  raw passthrough: {raw_written}  skipped (draft/private): {skipped}')
    return log_entries


def write_homepage(root, recent):
    log_rows = '\n'.join(
        f'''        <li class="log-line">
          <span class="log-date">{date}</span>
          <span class="log-tag{" teaching" if tag == "teaching" else ""}">{tag}</span>
          <span class="log-title"><a href="{href}">{title}</a></span>
        </li>'''
        for date, tag, title, href in recent
    )
    body = f'''    <section class="hero" aria-label="Site sections">
      <div class="hero-line"><span class="cwd">tony@fsgeek</span>:~$ ls -la</div>
      <div class="dirlisting">
        <div class="entry">
          <span class="perm">drwxr-xr-x</span>
          <span class="name"><a href="/research/">research/</a></span>
          <span class="desc">a decade of filesystems, memory, and how we find things again</span>
        </div>
        <div class="entry">
          <span class="perm">drwxr-xr-x</span>
          <span class="name"><a class="teaching-link" href="/teaching/">teaching/</a></span>
          <span class="desc">CPSC 416 (distributed systems) &middot; CPSC 436C (cloud computing)</span>
        </div>
        <div class="entry">
          <span class="perm">drwxr-xr-x</span>
          <span class="name"><a href="/log/">log/</a></span>
          <span class="desc">{len(recent)} shown here, the full run is under /log/</span>
        </div>
        <div class="entry">
          <span class="perm">-rw-r--r--</span>
          <span class="name"><a href="/about/">about</a></span>
          <span class="desc">the short version&nbsp;&mdash;&nbsp;the long version lives at <a href="https://wamason.com/about/">wamason.com</a></span>
        </div>
        <div class="entry"><span class="perm">&nbsp;</span><span class="cursor" aria-hidden="true"></span></div>
      </div>
    </section>

    <section class="log" aria-label="Recent entries">
      <h2>Recent</h2>
      <ul class="log-list">
{log_rows}
      </ul>
    </section>'''

    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>fsgeek.ca &mdash; Tony Mason</title>
  <meta name="description" content="A decade of notes on filesystems, distributed systems, and how systems remember: research, teaching, and an ongoing log.">
  <link rel="canonical" href="https://fsgeek.ca/">
  <link rel="stylesheet" href="/static/style.css">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>

{header_for('')}

<main id="main">
  <div class="wrap-wide">
{body}
  </div>
</main>

{FOOTER}

</body>
</html>
'''
    (root / 'index.html').write_text(page, encoding='utf-8')


def write_log_index(root, entries):
    log_rows = '\n'.join(
        f'''        <li class="log-line">
          <span class="log-date">{date}</span>
          <span class="log-tag{" teaching" if tag == "teaching" else ""}">{tag}</span>
          <span class="log-title"><a href="{href}">{title}</a></span>
        </li>'''
        for date, tag, title, href in entries
    )
    body = f'''    <article class="entry">
      <h1>log</h1>
      <div class="entry-meta"><span>{len(entries)} entries</span></div>
      <div class="entry-body">
      <ul class="log-list">
{log_rows}
      </ul>
      </div>
    </article>'''
    page = page_shell(
        title='log',
        description=f'The full log: {len(entries)} entries, most recent first.',
        canonical='https://fsgeek.ca/log/',
        section='log',
        breadcrumb_html=breadcrumb(['log']),
        body_html=body,
    )
    out_dir = root / 'log'
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / 'index.html').write_text(page, encoding='utf-8')


def write_404(root):
    body = '''    <article class="entry">
      <h1>404</h1>
      <div class="entry-meta"><span>no such file or directory</span></div>
      <div class="entry-body">
        <p>Whatever this path pointed to isn't here. The WordPress-to-static move renamed most permalinks, so if you followed an old link, try <a href="/log/">the log</a>, <a href="/research/">research</a>, or <a href="/teaching/">teaching</a> instead.</p>
      </div>
    </article>'''
    page = page_shell(
        title='404',
        description='Page not found.',
        canonical='https://fsgeek.ca/404.html',
        section='',
        breadcrumb_html=breadcrumb(['404']),
        body_html=body,
    )
    (root / '404.html').write_text(page, encoding='utf-8')


def write_privacy(root):
    body = '''    <article class="entry">
      <h1>Privacy &amp; terms</h1>
      <div class="entry-meta"><span>same policy as wamason.com, same server</span></div>
      <div class="entry-body">
        <h2>Privacy</h2>
        <p>This site collects nothing directly. There are no forms, no cookies, no analytics scripts, and no fonts, embeds, or other third-party resources loaded into the pages.</p>
        <p>Two things happen outside the pages themselves:</p>
        <ul>
          <li><strong>Server logs.</strong> The web server records each request's IP address, timestamp, page requested, referring page, and browser identification string. Logs are kept 14 days, then deleted.</li>
          <li><strong>Cloudflare.</strong> This site is served through Cloudflare as a reverse proxy. Cloudflare sees and logs the same request data before it reaches this server, under its own retention policy.</li>
        </ul>
        <p>No data collected here is sold, shared, or used for advertising. There is nothing else to disclose.</p>
        <h2>Terms</h2>
        <p>Content on this site &mdash; research notes, teaching materials, and the log &mdash; is the author's own, not professional or legal advice. Course pages reflect the state of a given term and are not maintained after that term ends; check with the instructor for anything current.</p>
      </div>
    </article>'''
    page = page_shell(
        title='Privacy & terms',
        description="What this site collects, what it doesn't, and terms covering the content here.",
        canonical='https://fsgeek.ca/privacy/',
        section='',
        breadcrumb_html=breadcrumb(['privacy']),
        body_html=body,
    )
    out_dir = root / 'privacy'
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / 'index.html').write_text(page, encoding='utf-8')


if __name__ == '__main__':
    main()
