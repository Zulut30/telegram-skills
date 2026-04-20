# Changelog

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
