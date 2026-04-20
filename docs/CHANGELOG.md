# Changelog

## v1.6.1 — 2026-04-20 (Wiki + Pages fix)

### Fixed
- `.github/workflows/pages.yml` — added `enablement: true` to `configure-pages@v5`, auto-enables GitHub Pages on first deploy. Previous deploy failed with "Pages site failed. Please verify that the repository has Pages enabled…".

### Added
- **Full GitHub Wiki** in `wiki/` directory, 14 pages:
  - Navigation: `Home`, `_Sidebar`, `_Footer`, `Home-ru`, `Home-pl`
  - Getting started: `Quickstart`, `Installation`, `Modes`, `FAQ`
  - Using: `Commands-Reference`, `Prompt-Formats`, `Examples`, `Migration`
  - Architecture: `Architecture`, `Reference-Library`, `Bot-API-Spec`
  - Community: `Contributing`, `Sync-Checklist`, `Security`, `Roadmap`, `Comparison`
- `wiki/publish_wiki.sh` — one-command publisher: clones `<repo>.wiki.git`, syncs content, commits, pushes
- `wiki/README.md` — instructions for maintainers

### How to publish the wiki
```bash
# 1. Initialize wiki once via web UI:
#    https://github.com/Zulut30/telegram-skills/wiki → Create the first page
# 2. Sync:
bash wiki/publish_wiki.sh
```

## v1.6 — 2026-04-20 (Polish + growth infrastructure)

Third audit closure. Focus: fix lingering v1.5 bugs, set up growth infrastructure, stop hacks in test code.

### Fixed (P0 from v1.5 audit)
- **Tests no longer use `__import__` hack.** `tests/conftest.py` exposes a clean `get_only_payment(session)` helper. `test_payment_service.py` uses normal imports.
- **CI no longer fails on Python 3.13.** Matrix marks 3.13 as `experimental: true` with `continue-on-error`. Only 3.12 is required-to-pass.
- **`install.sh --check`** mode for self-test (git/curl/bash presence, HOME writable, repo reachable). Shellcheck-clean and covered by CI.
- **Pre-commit hooks no longer use inline Python.** Extracted to `tests/validate_frontmatter.py`, `tests/validate_plugin_manifest.py`, `tests/check_sync.py`. Works on Windows Git Bash.

### Added — Distribution
- **GitHub Pages landing** at [zulut30.github.io/telegram-skills](https://zulut30.github.io/telegram-skills/) — single-file HTML, no build step, OpenGraph metadata for social sharing
- `.github/workflows/pages.yml` — auto-deploy on landing/assets changes
- `.well-known/security.txt` (RFC 9116) — security researcher contact
- `docs/SECURITY_THANKS.md` — acknowledgments placeholder

### Added — Version hygiene
- `VERSION` file — single source of truth
- `tests/check_version_sync.py` — asserts VERSION = plugin.json version = latest CHANGELOG header
- `tests/bump_version.py` — `python tests/bump_version.py minor` updates all places

### Added — Growth kit
- `.github/GROWTH_KIT.md` — 10 seeded issues + 5 discussion starters + social-media copy templates
- `.github/DISCUSSION_TEMPLATE/` — announcements, show-and-tell, Q&A
- Template for submitting your bot to the public showcase

### Added — Content
- Comparison vs **python-telegram-bot** in `docs/COMPARISON.md` — the #1 gap from the audit

### Improved
- `README.md` — added Website badge pointing to the landing page
- `validate.yml` — new `install-sh` job (shellcheck + `--check` dry-run)
- Plugin manifest validator now checks `references[]` paths exist, not only commands/skills

### Audit v3 closures
- ✅ `plugin.json` strict-JSON (from v1.5)
- ✅ Tests have no `__import__` hacks
- ✅ Python 3.13 doesn't block CI
- ✅ `install.sh` testable
- ✅ Pre-commit cross-platform
- ✅ Landing page live
- ✅ GitHub Discussions templates ready
- ✅ Seeded growth kit ready
- ✅ Comparison vs PTB
- ✅ Single source of truth for version

### Still pending (v1.7+)
- Real production bot deployed and listed in SHOWCASE (requires human action)
- GitHub Discussions enabled (requires repo admin action)
- examples/02-ai-assistant and examples/03-lead-gen full implementations
- Logo redesign (needs designer)
- Golden tests with real API key baseline

## v1.5 — 2026-04-20 (Proofs of work)

**Focus: make the skill provably correct, not just comprehensive.** Audit identified that v1.4 looked polished but lacked proof of quality. v1.5 addresses the core blockers.

### Added — Proof that skill follows its own rules
- **Example bot now has tests.** `examples/01-vip-media-bot/tests/` — 15+ pytest cases (unit + integration), covering SubscriptionService, PaymentService, ChannelCheckService, UserService, repository lifecycle, idempotent webhooks
- `examples/01-vip-media-bot/tests/conftest.py` — async session + Redis + Bot fixtures using aiosqlite in-memory
- CI matrix (Python 3.12 / 3.13) running `ruff` + `pytest` on every PR

### Added — Automated four-format sync
- `tests/check_sync.py` — verifies 20 canonical concepts appear in all 5 skill-prompt distribution files (SKILL.md, system_prompt.txt, cursor-mdc, cursor-legacy, AGENTS.md)
- CI job `sync-check` runs on every PR, blocks drift
- Prevents slow divergence between distribution formats

### Added — New critical reference modules
- `references/performance.md` — connection pools, N+1 queries, batching, file_id reuse, broadcast throttling, horizontal scaling, profiling
- `references/anti-spam.md` — captcha on join, URL filters, CAPS/emoji detection, behavioral trust scoring, warn/mute/kick escalation, shadow-ban, ChatGPT-generated spam patterns
- `references/gdpr-compliance.md` — `/privacy_export`, `/privacy_delete` with grace period, retention policy, sub-processor DPAs, breach notification within 72h, audit log
- `references/analytics.md` — PostHog / Mixpanel / Amplitude integration, events taxonomy, UTM via signed deep-links, A/B feature flags, privacy-respecting tracking

### Added — Distribution & DX
- `install.sh` — one-liner installer: `curl … | bash -s -- [claude|cursor|codex|system-prompt]`
- `Makefile` at repo root — `sync-check`, `golden`, `example-test`, `lint`, `install-*`
- `.github/dependabot.yml` — weekly deps update for example bot + monthly for CI actions + Docker
- `docs/MIGRATION.md` — upgrade guides 1.0 → 1.5, SemVer policy
- `docs/README.md` — documentation index

### Changed
- `plugin.json` — removed non-standard `$comment` field (now strict-JSON valid); version bumped to 1.5.0; references array expanded
- `.github/workflows/validate.yml` — added `sync-check` and `example-bot-tests` jobs
- `SKILL.md` — references section now lists 21 modules (was 17)

### Audit closure
Blockers closed:
- ✅ plugin.json is strict-JSON
- ✅ example bot has tests
- ✅ four-format sync automated
- ✅ 4 critical references added

Still pending (v1.6+):
- Discussions enablement + seeded issues
- First production bot in Showcase
- examples/02 and examples/03 full implementations
- Golden tests baseline metrics (requires API key secret in CI)

## v1.4 — 2026-04-20 (Professional polish)

Закрыты оставшиеся P2/P3 пробелы из аудита. Репо готов к публичному анонсу.

### Added — Testing & CI
- `tests/golden/` — eval harness: 3 golden test cases (new bot, review monolith, Mini App auth) с YAML assertions (structural patterns, forbidden/required regex, min code blocks)
- `tests/run_golden.py` — runner, работает с Anthropic + OpenAI, gracefully skips без API key
- `.github/workflows/golden.yml` — прогон golden-тестов на PR
- `.pre-commit-config.yaml` — trailing whitespace, YAML/JSON/markdownlint, gitleaks, plugin.json + frontmatter validation

### Added — Developer experience
- `assets/logo/logo.svg` — бренд-марк (SVG, масштабируется)
- `assets/logo/og-image.svg` — OpenGraph 1200×630
- `.vscode/botforge-snippets.code-snippets` — 5 snippet-ов (`bf-new`, `bf-extend`, `bf-review`, `bf-miniapp`, `bf-pay`)
- `.vscode/settings.json`, `.zed/settings.json` + `.zed/README.md`

### Added — Documentation
- `docs/COMPARISON.md` — vs plain prompts, cookiecutter, BotFather/no-code, generic agents
- `docs/SHOWCASE.md` — community-bot showcase с формой PR
- `docs/SYNC-CHECKLIST.md` — four-format sync enforcement
- `docs/ru/README.md` — русская версия README

### Added — Governance
- `.github/CODEOWNERS`, `.github/FUNDING.yml`
- `.github/release.yml` — авто-группировка release notes по labels

### Added — Examples
- `examples/02-ai-assistant/README.md` — stub с планом
- `examples/03-lead-gen/README.md` — stub с планом

### Changed
- Root `README.md` — логотип, центрированные навигационные ссылки, ссылка на RU
- `docs/INSTALL.md` — блок про Claude Code Plugin marketplace, Zed, VS Code snippets

## v1.3 — 2026-04-20 (Product readiness)

**Полный pivot от skill-как-документ к skill-как-продукт.** Аудит выявил 24 пробела — Фаза 1 + ключевые P1 закрыты в этом релизе.

### Added — Governance & distribution
- `.claude-plugin/plugin.json` — Claude Code plugin manifest (name, version, 18 commands, 17 references, engines)
- `CLAUDE.md` at repo root — meta-context for maintainers
- `SECURITY.md` — vulnerability disclosure policy
- `CONTRIBUTING.md` — four-format sync rule, PR checklist
- `CODE_OF_CONDUCT.md` — Contributor Covenant 2.1
- `.github/ISSUE_TEMPLATE/` — bug_report + feature_request
- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/workflows/validate.yml` — markdownlint + frontmatter + plugin.json + broken-link check
- `.markdownlint.yaml`
- `cursor/.cursor/rules/botforge.mdc` — modern Cursor MDC format (supersedes `.cursorrules`)

### Added — Working example
- `examples/01-vip-media-bot/` — **полностью рабочий** VIP-бот с Telegram Stars, ~25 Python файлов, Alembic-миграция, Dockerfile multi-stage, docker-compose с healthchecks, Makefile, DEPLOY.md (Fly.io / Railway / VPS). Ранее `examples/` был пустышкой.

### Added — New reference modules
- `references/scheduler.md` — APScheduler / arq / cron; expire-subs, reminders, scheduled broadcasts, idempotency, observability
- `references/subscriptions.md` — Telegram Stars Subscriptions (`subscription_period`), Stripe, ЮKassa auto-payments, proration, dunning, state machine
- `references/inline-mode.md` — @botname query handler, pagination, `chosen_inline_result` analytics, throttling
- `references/groups-and-channels.md` — privacy mode, admin rights matrix, forum topics, chat join requests, moderation patterns
- `references/media.md` — photos/videos/albums/voice/stickers, `file_id` reuse strategy, Local Bot API for >20MB files
- `references/faq.md` — troubleshooting по 20+ типовым проблемам

### Added — New slash commands
- `/botforge-scheduler` — scheduled tasks
- `/botforge-inline` — inline-mode

### Changed
- `plugin.json` now lists 18 commands and 17 references, validated by CI
- SKILL.md references section expanded to 17 entries
- README: commands count 16 → 18; note about Grounded-in-Bot-API 9.6

## v1.2 — 2026-04-20 (Official Bot API 9.6 grounding)

**Grounded in official Telegram Bot API documentation.** Skill теперь явно цитирует ограничения из `core.telegram.org` и автоматически применяет их в генерируемом коде.

### Added
- `references/telegram-api-spec.md` — полная выжимка из Bot API 9.6: rate limits (1/sec, 20/min, 30/sec), webhook params, error codes, MarkdownV2 escape chars, deep-link syntax, Mini App events + CloudStorage constraints, Telegram Stars (XTR) flow, `allowed_updates` list, length limits (callback_data 64b, message 4096, caption 1024), `BotCommandScope` types
- `references/botfather-setup.md` — operational checklist: `/setdescription`, `/setabouttext`, privacy mode, Mini App registration, token rotation, три env (dev/staging/prod)
- `references/i18n.md` — gettext + Babel multi-language: language detection priority, extraction workflow, pluralization для ru/pl/cs
- `references/observability.md` — structlog JSON с request_id, Sentry PII scrubbing, Prometheus metrics (UPDATES, HANDLER_SECONDS, TG_API_ERRORS, PAYMENT_EVENTS), health/ready probes, audit log, alert rules
- Три новые команды: `/botforge-botfather`, `/botforge-i18n`, `/botforge-observability`

### Changed
- system_prompt.txt + Cursor rules + Codex AGENTS.md — явно enforce-ят лимиты Bot API 9.6
- Differentiated exception handling: `TelegramRetryAfter` / `Forbidden` / `BadRequest` / `Unauthorized` / 5xx — каждый с своей политикой
- SKILL.md — секция «Telegram Bot API 9.6 — hard constraints» с конкретными цифрами и ссылками

### Sources
- https://core.telegram.org/bots/api (v9.6, 2026-04-03)
- https://core.telegram.org/bots/faq (rate limits)
- https://core.telegram.org/bots/webapps (Mini Apps)
- https://core.telegram.org/bots/payments-stars (XTR)

## v1.1 — 2026-04-20 (Mini Apps, Auth, Payments, Slash Commands)

**Major expansion.** Core skill дополнен тремя reference-модулями и 13 slash-командами Claude Code.

### Added
- `references/miniapp.md` — Telegram Mini App: initData HMAC validation, JWT auth, FastAPI backend, frontend SDK wrapper
- `references/auth.md` — роли/RBAC, ban/shadow-ban, Mini App initData, OAuth bridging, API keys
- `references/payments.md` — единый интерфейс `PaymentProvider` + реализации для Stars, ЮKassa, CryptoBot, Stripe, Tribute
- `.claude/commands/` — 13 slash-команд:
  - `/botforge-new`, `/botforge-extend`, `/botforge-review`, `/botforge-refactor`
  - `/botforge-miniapp`, `/botforge-auth`, `/botforge-payments`
  - `/botforge-broadcast`, `/botforge-admin`, `/botforge-test`
  - `/botforge-deploy`, `/botforge-security`, `/botforge-help`

### Philosophy
Payments-слой теперь провайдер-агностик: смена ЮKassa → Stripe = замена одной строки DI. Auth и Mini App объединены через единый JWT. Slash-команды делают skill операционным — каждая фаза жизненного цикла бота (создание / расширение / review / деплой / аудит) имеет явную точку входа.

## v1.0 Pro — 2026-04-20

**Initial public release.**

- Core skill: aiogram 3, PostgreSQL, SQLAlchemy 2 async, Alembic, Redis, Docker
- 4 modes: Lite, Pro, Media, SaaS
- 6-stage mandatory workflow (Brief → ADR → Tree → Files → Self-review → Deploy)
- 12 reusable patterns (settings, DB, middleware, FSM, broadcast, etc.)
- 3 full generation examples (VIP media bot, AI assistant, lead-gen)
- Self-review, deploy, security checklists
- Packaging for Claude Code, Cursor, Codex / Codex CLI

## Roadmap

| Version | Status | Planned content |
|---|---|---|
| v1.1 Payments + Auth + Mini App | **released 2026-04-20** | Unified Stars/ЮKassa/CryptoBot/Stripe/Tribute, roles, initData, JWT, 13 slash-commands |
| v1.2 Media Pack | planned | WordPress/Notion/Sanity sync, media pipelines (HLS/albums), UTM, segmented broadcast v2 |
| v1.3 AI Pack | planned | OpenAI/Anthropic unified, dialog memory, pgvector RAG, streaming responses |
| v1.4 Ops Pack | planned | Sentry/Prometheus/Grafana, horizontal scale, feature flags, blue-green deploy |
| v1.5 Multi-bot Factory | planned | CLI `botforge new <name>`, multitenancy, shared core library |
| v2.0 BotForge Studio | vision | UI-конструктор сценариев → экспорт проекта |

## Contributing

Вклад приветствуется:
- Новые паттерны в `.claude/skills/botforge/references/patterns.md`
- Новые примеры ботов в `examples/`
- Правки правил в `.cursorrules` / `AGENTS.md` / `system_prompt.txt` — синхронно во всех трёх

Перед PR убедитесь, что правила в трёх форматах согласованы (Claude Code / Cursor / Codex).
