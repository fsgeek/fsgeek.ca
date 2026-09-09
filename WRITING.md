# Writing a new post

1. Create `content/posts/<slug>.md`:

   ```
   ---
   title: "Your Title Here"
   date: "2026-09-09"
   status: "publish"
   section: "log"
   ---

   Body in Markdown. Standard stuff: **bold**, _italic_, [links](https://example.com),
   lists, code fences, > blockquotes.
   ```

   Frontmatter fields, all required:

   - `title` -- plain text, no markup.
   - `date` -- `YYYY-MM-DD`.
   - `status` -- `publish` or `draft`. A `draft` post is skipped entirely
     (not built, not in the sitemap) until you flip it to `publish`.
   - `section` -- `log`, `research`, or `teaching`. Controls the small tag
     shown next to the post in the log list. If you're not sure, use `log`.

   `<slug>` becomes the URL: `content/posts/my-thing.md` -> `/log/my-thing/`.
   Use lowercase, hyphens, no spaces.

2. Images: put them under `media/<slug>/` and reference them as
   `![alt text](/media/<slug>/filename.jpg)`.

3. Build and check it locally:

   ```
   scripts/publish.sh
   ```

   This validates every post's frontmatter (bad date, missing field, wrong
   `status`/`section` value, a slug that collides with an old `.html` post,
   or an image reference that doesn't exist -- all of these stop the build
   with a specific error, nothing gets built halfway), then renders the
   site into `log/`, `research/`, etc., then regenerates `sitemap.xml`.

   Open the generated `log/<slug>/index.html` in a browser if you want to
   eyeball it before committing.

4. Commit and push as usual:

   ```
   git add -A
   git commit -m "..."
   git push
   ```

5. Go live, when you're ready (this is a separate, deliberate step -- pushing
   to `main` does not automatically publish):

   ```
   scripts/deploy.sh
   ```

   This SSHes to the server, pulls, and spot-checks that the site responds.

## Notes

- Old posts imported from WordPress are `content/posts/*.html`, written as
  raw HTML with WordPress-era frontmatter (`categories`, `tags`). They still
  build fine as-is -- you don't need to touch or convert them. Just write
  new posts in Markdown.
- `scripts/ots-upgrade.sh` (OpenTimestamps) is unrelated to publishing a
  post -- it's run separately, hours after a commit, to anchor timestamps to
  Bitcoin. Not part of this workflow.
