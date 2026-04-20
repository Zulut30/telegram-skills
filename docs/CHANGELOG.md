# Changelog

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
