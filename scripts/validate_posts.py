#!/usr/bin/env python3
"""Validate content/posts/*.md frontmatter before it reaches build-site.py.

Every check here is blocking: missing/blank required fields, a malformed
date, an invalid status/section value, an unparseable frontmatter block,
a slug that collides between a .md and .html post, or an image reference
that doesn't exist under media/. Loud and immediate beats a quietly
broken link discovered later by a reader.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

REQUIRED_FIELDS = ('title', 'date', 'status', 'section')
VALID_STATUS = {'publish', 'draft'}
VALID_SECTION = {'log', 'research', 'teaching'}

FM_RE = re.compile(r'^---\n(.*?)\n---\n\n?(.*)$', re.DOTALL)
IMG_RE = re.compile(r'!\[[^\]]*\]\((/media/[^)\s]+)\)')


@dataclass
class ValidationResult:
    errors: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def parse_frontmatter(text: str, label: str, result: ValidationResult) -> tuple[dict, str] | None:
    m = FM_RE.match(text)
    if not m:
        result.errors.append(f'{label}: missing or malformed frontmatter block (expected --- ... --- at top of file)')
        return None

    fm: dict[str, str] = {}
    for lineno, line in enumerate(m.group(1).splitlines(), start=2):
        if not line.strip():
            continue
        if ':' not in line:
            result.errors.append(f'{label}: line {lineno}: not a "key: value" line: {line!r}')
            continue
        key, _, val = line.partition(':')
        val = val.strip()
        if val.startswith('"') and val.endswith('"') and len(val) >= 2:
            val = val[1:-1]
        fm[key.strip()] = val
    return fm, m.group(2)


def validate_frontmatter_fields(fm: dict, label: str, result: ValidationResult) -> None:
    for field_name in REQUIRED_FIELDS:
        if not fm.get(field_name, '').strip():
            result.errors.append(f'{label}: missing required field "{field_name}"')

    raw_date = fm.get('date', '').strip()
    if raw_date:
        try:
            date.fromisoformat(raw_date)
        except ValueError:
            result.errors.append(
                f'{label}: field "date" is {raw_date!r}, expected YYYY-MM-DD'
            )

    status = fm.get('status', '').strip()
    if status and status not in VALID_STATUS:
        result.errors.append(
            f'{label}: field "status" is {status!r}, expected one of {sorted(VALID_STATUS)}'
        )

    section = fm.get('section', '').strip()
    if section and section not in VALID_SECTION:
        result.errors.append(
            f'{label}: field "section" is {section!r}, expected one of {sorted(VALID_SECTION)}'
        )


def validate_images(body: str, label: str, root: Path, result: ValidationResult) -> None:
    for m in IMG_RE.finditer(body):
        rel = m.group(1).lstrip('/')
        if not (root / rel).exists():
            result.errors.append(f'{label}: referenced image not found: {m.group(1)}')


def validate_post_file(path: Path, root: Path, result: ValidationResult) -> None:
    label = str(path.relative_to(root)) if path.is_relative_to(root) else str(path)
    text = path.read_text(encoding='utf-8')
    parsed = parse_frontmatter(text, label, result)
    if parsed is None:
        return
    fm, body = parsed
    validate_frontmatter_fields(fm, label, result)
    validate_images(body, label, root, result)


def validate_all(root: Path) -> ValidationResult:
    result = ValidationResult()

    md_posts = sorted((root / 'content/posts').glob('*.md'))
    html_posts = sorted((root / 'content/posts').glob('*.html'))

    md_slugs = {p.stem for p in md_posts}
    html_slugs = {p.stem for p in html_posts}
    for slug in sorted(md_slugs & html_slugs):
        result.errors.append(
            f'content/posts/{slug}: both {slug}.md and {slug}.html exist — ambiguous, pick one'
        )

    for path in md_posts:
        validate_post_file(path, root, result)

    return result


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    result = validate_all(root)

    for e in result.errors:
        print(f'error: {e}')

    if not result.ok:
        print(f'\n{len(result.errors)} error(s) — nothing was built.')
        return 1

    print('all posts valid.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
