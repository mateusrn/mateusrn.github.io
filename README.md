# THINK — Obsidian + Jekyll

A minimal personal writing site inspired by the sparse article style of Niklas Gruhn, with **THINK** as the site identity.

## Architecture

```text
Obsidian Vault
    │
    └── writing/3-published/
              │
              ▼
        scripts/publish.py
              │
              ▼
          _posts/ + assets/
              │
              ▼
            GitHub
              │
              ▼
        GitHub Pages / Jekyll
              │
              ▼
            THINK
```

Your Obsidian vault remains private. Only `writing/3-published/` is published.

## Quick start

1. Put this project in your THINK GitHub repository.
2. Check `_config.yml` and set `url` / `baseurl` for your repository.
3. Install Ruby/Jekyll dependencies:
   ```bash
   bundle install
   ```
4. Publish notes from your Obsidian vault:
   ```bash
   python scripts/publish.py "/path/to/Epicurus Garden/writing"
   ```
5. Preview:
   ```bash
   bundle exec jekyll serve
   ```
6. Commit and push.

See `PRIVATE_WORKFLOW.md` for the detailed private workflow guide.

## Obsidian structure

The publisher expects:

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

Only `3-published/` is public.

Images can be stored anywhere under `writing/assets/`; the publisher searches recursively.

## Public pages

About and Bookshelf are maintained in Obsidian. Add them to `writing/3-published/` with `type: page` and their respective permalinks. The publisher generates the website copies.
