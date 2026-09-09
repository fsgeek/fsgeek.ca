#!/usr/bin/env python3
"""Tests for validate_posts.py. Run: python3 scripts/test_validate_posts.py"""
import shutil
import tempfile
import unittest
from pathlib import Path

from validate_posts import ValidationResult, validate_all, validate_post_file

GOOD = '''---
title: "A Fine Post"
date: "2026-09-09"
status: "publish"
section: "log"
---

Body text here.
'''


class TestValidatePosts(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp())
        (self.root / 'content/posts').mkdir(parents=True)
        (self.root / 'media').mkdir()

    def tearDown(self):
        shutil.rmtree(self.root)

    def write_post(self, name, text):
        path = self.root / 'content/posts' / name
        path.write_text(text, encoding='utf-8')
        return path

    def test_valid_post_passes(self):
        path = self.write_post('good.md', GOOD)
        result = ValidationResult()
        validate_post_file(path, self.root, result)
        self.assertTrue(result.ok)
        self.assertEqual(result.errors, [])

    def test_missing_required_field(self):
        text = GOOD.replace('status: "publish"\n', '')
        path = self.write_post('bad.md', text)
        result = ValidationResult()
        validate_post_file(path, self.root, result)
        self.assertFalse(result.ok)
        self.assertTrue(any('status' in e for e in result.errors))

    def test_blank_required_field(self):
        text = GOOD.replace('title: "A Fine Post"', 'title: ""')
        path = self.write_post('bad.md', text)
        result = ValidationResult()
        validate_post_file(path, self.root, result)
        self.assertFalse(result.ok)
        self.assertTrue(any('title' in e for e in result.errors))

    def test_malformed_date(self):
        text = GOOD.replace('date: "2026-09-09"', 'date: "Sept 9 2026"')
        path = self.write_post('bad.md', text)
        result = ValidationResult()
        validate_post_file(path, self.root, result)
        self.assertFalse(result.ok)
        self.assertTrue(any('date' in e for e in result.errors))

    def test_invalid_status(self):
        text = GOOD.replace('status: "publish"', 'status: "published"')
        path = self.write_post('bad.md', text)
        result = ValidationResult()
        validate_post_file(path, self.root, result)
        self.assertFalse(result.ok)
        self.assertTrue(any('status' in e for e in result.errors))

    def test_invalid_section(self):
        text = GOOD.replace('section: "log"', 'section: "misc"')
        path = self.write_post('bad.md', text)
        result = ValidationResult()
        validate_post_file(path, self.root, result)
        self.assertFalse(result.ok)
        self.assertTrue(any('section' in e for e in result.errors))

    def test_malformed_frontmatter_block(self):
        path = self.write_post('bad.md', 'title: no dashes at all\n\nBody.\n')
        result = ValidationResult()
        validate_post_file(path, self.root, result)
        self.assertFalse(result.ok)
        self.assertTrue(any('frontmatter' in e for e in result.errors))

    def test_missing_image_blocks(self):
        text = GOOD + '\n![alt](/media/nope.jpg)\n'
        path = self.write_post('good.md', text)
        result = ValidationResult()
        validate_post_file(path, self.root, result)
        self.assertFalse(result.ok)
        self.assertTrue(any('nope.jpg' in e for e in result.errors))

    def test_existing_image_no_error(self):
        (self.root / 'media' / 'foo.jpg').write_bytes(b'')
        text = GOOD + '\n![alt](/media/foo.jpg)\n'
        path = self.write_post('good.md', text)
        result = ValidationResult()
        validate_post_file(path, self.root, result)
        self.assertEqual(result.errors, [])

    def test_slug_collision_between_md_and_html(self):
        self.write_post('dup.md', GOOD)
        self.write_post('dup.html', '---\ntitle: "x"\ndate: "2026-01-01"\nstatus: "publish"\n---\n\n<p>x</p>\n')
        result = validate_all(self.root)
        self.assertFalse(result.ok)
        self.assertTrue(any('dup' in e and 'both' in e for e in result.errors))

    def test_multiple_bad_posts_all_reported(self):
        self.write_post('bad1.md', GOOD.replace('status: "publish"', 'status: "bogus"'))
        self.write_post('bad2.md', GOOD.replace('section: "log"', 'section: "bogus"'))
        result = validate_all(self.root)
        self.assertFalse(result.ok)
        self.assertEqual(len(result.errors), 2)


if __name__ == '__main__':
    unittest.main()
