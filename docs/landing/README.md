# BotForge Landing

Static HTML landing deployed automatically to GitHub Pages on pushes to `main`.

- Live URL: https://zulut30.github.io/telegram-skills/
- Source: [`index.html`](index.html)
- Workflow: [`.github/workflows/pages.yml`](../../.github/workflows/pages.yml)

## Editing

Single HTML file with inline CSS/JS and local optimized visual assets. Keep it build-free and dependency-free.

## Assets

Generated visuals live in `assets/visuals/` for the site bundle and are mirrored in the repository root under `assets/visuals/` for README/social reuse.

## Preview locally

```bash
cd docs/landing && python -m http.server 8000
# open http://localhost:8000
```
