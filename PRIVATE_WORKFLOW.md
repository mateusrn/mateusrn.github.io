# THINK — Private Obsidian Workflow

This file is intentionally private and is ignored by Git.

## The basic idea

**Obsidian is the workshop. THINK is the public shelf.**

Your existing writing structure is the source of truth:

```text
writing/
├── 0-inbox/
├── 1-journal/
├── 2-drafts/
├── 3-published/
├── 4-references/
├── assets/
└── _templates/
```

Only `3-published/` is sent to the website.

## Writing workflow

1. Capture ideas in `0-inbox/`.
2. Develop them in `2-drafts/`.
3. Move finished pieces to `3-published/`.
4. Put images/attachments used by published writing in `assets/`.
5. Run the publisher.
6. Preview the site locally.
7. Commit and push the website repository.

Your `1-journal/` and `4-references/` folders remain private.

## Publishing

From the THINK repository:

```bash
python scripts/publish.py "/path/to/Epicurus Garden/writing"
```

The publisher will:

- read Markdown files under `writing/3-published/`
- create corresponding Jekyll posts under `_posts/`
- convert `![[image.png]]` embeds into web images
- search for images under `writing/assets/`
- copy those images into the website
- convert simple `[[Note]]` links into THINK post links

## Images

Recommended convention:

```text
writing/
└── assets/
    ├── figures/
    ├── diagrams/
    ├── photos/
    └── ...
```

You can also keep the assets folder flat. The publisher searches recursively.

In an Obsidian note:

```markdown
![[my-diagram.png]]
```

The image can live anywhere under `writing/assets/`.

## Frontmatter

You can optionally give a published note explicit metadata:

```yaml
---
title: The Problem With Problems
date: 2026-09-09
---
```

If there is no date, the publisher uses the file modification date.

## Local preview

From the THINK repository:

```bash
bundle install
bundle exec jekyll serve
```

Then open:

```text
http://localhost:4000/think/
```

## Publishing to GitHub Pages

After checking the local preview:

```bash
git add .
git commit -m "Publish new notes"
git push
```

GitHub Actions builds and deploys the site.

## Important

`writing/3-published/` is a **public publishing boundary**.

Anything placed there should be considered intended for publication.

The website repository does not contain your private Obsidian vault.

## About and Bookshelf

Keep these pages in Obsidian too. Put them directly in `writing/3-published/`.

About:
```yaml
---
type: page
title: About
permalink: /about/
---
```

Bookshelf:
```yaml
---
type: page
title: Bookshelf
permalink: /bookshelf/
---
```

The publisher generates the website pages from these notes. Do not edit the generated copies by hand.
