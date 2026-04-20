# BotForge

> **The Telegram Bot Engineering Skill for AI**
> Production-ready skill pack for Claude Code, Codex, Cursor and any LLM.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-compatible-8A2BE2)](https://claude.com/claude-code)
[![Cursor](https://img.shields.io/badge/Cursor-rules-000000)](https://cursor.com)
[![Codex](https://img.shields.io/badge/Codex-AGENTS.md-10A37F)](https://openai.com)
[![aiogram](https://img.shields.io/badge/aiogram-3.x-2CA5E0)](https://docs.aiogram.dev/)
[![Python](https://img.shields.io/badge/Python-3.12%2B-3776AB)](https://www.python.org/)
[![Bot API](https://img.shields.io/badge/Bot%20API-9.6-0088CC)](https://core.telegram.org/bots/api)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

BotForge превращает AI-ассистента в senior Telegram-инженера. Вместо одноразового `main.py` на 800 строк AI проектирует и собирает **модульного, масштабируемого, production-ready Telegram-бота** — с архитектурой, БД, миграциями, админкой, платежами, рассылками, Docker и деплоем.

---

## Три обещания

1. **Не монолит.** Слоёная архитектура (handlers / services / repositories / integrations) из коробки.
2. **Не черновик.** Docker + Postgres + Alembic + `.env` + деплой-инструкции в первой же генерации.
3. **Не разваливается.** Пятую фичу добавляете так же легко, как первую.

---

## Что внутри

| Файл | Назначение |
|---|---|
| [`SKILL.md`](SKILL.md) | Полный skill-документ (манифест, system prompt, правила, паттерны, примеры) |
| [`system_prompt.txt`](system_prompt.txt) | Голый system prompt для вставки в любой LLM |
| [`.claude/skills/botforge/`](.claude/skills/botforge/) | Skill для **Claude Code** (формат Agent Skills) + references |
| [`.claude/commands/`](.claude/commands/) | 18 slash-команд Claude Code: `/botforge-new`, `/botforge-miniapp`, `/botforge-payments` и др. |
| [`.claude-plugin/plugin.json`](.claude-plugin/plugin.json) | Plugin manifest для Claude Code marketplace |
| [`cursor/.cursor/rules/botforge.mdc`](cursor/.cursor/rules/botforge.mdc) | Правила для **Cursor** (MDC format) |
| [`cursor/.cursorrules`](cursor/.cursorrules) | Legacy Cursor правила |
| [`codex/AGENTS.md`](codex/AGENTS.md) | Инструкция для **OpenAI Codex / Codex CLI / Aider** |
| [`docs/QUICKSTART.md`](docs/QUICKSTART.md) | **Start here** — 5 минут от нуля до бота |
| [`docs/INSTALL.md`](docs/INSTALL.md) | Детальная установка в каждый инструмент |
| [`docs/USAGE.md`](docs/USAGE.md) | Режимы, промпт-форматы, сессии |
| [`docs/CHANGELOG.md`](docs/CHANGELOG.md) | История версий и roadmap |
| [`examples/01-vip-media-bot/`](examples/01-vip-media-bot/) | **Рабочий** VIP-бот на Telegram Stars |

---

## Технический стек, который skill навязывает

- **Python 3.12+**
- **aiogram 3.x** (async, routers, FSM, middleware)
- **SQLAlchemy 2.x async** + **Alembic** миграции
- **PostgreSQL** primary (SQLite только в Lite-режиме)
- **Redis** для FSM, throttling, кэшей
- **pydantic-settings**, **structlog**, **httpx**, **tenacity**
- **Docker** multi-stage + **docker-compose**
- **pytest**, **ruff**, **mypy --strict**

---

## Четыре режима

| Режим | Когда | Отличия |
|---|---|---|
| **Lite** | MVP за вечер, проверка гипотезы | SQLite, polling, без Docker |
| **Pro** (default) | Коммерческий бот | Полный production-стандарт |
| **Media** | Контент, каналы, gated-доступ | + CMS-sync, сегментированные рассылки, UTM |
| **SaaS** | Подписки, VIP, billing | + plans/trials/proration, multi-provider payments |

Переключение — первой строкой запроса: `BotForge: SaaS`.

---

## Быстрый старт

### Claude Code
```bash
git clone https://github.com/Zulut30/telegram-skills.git
cp -r telegram-skills/.claude/skills/botforge ~/.claude/skills/
# или в корень проекта: <project>/.claude/skills/botforge/
```
В сессии: `/skill botforge` или попросите Claude: «используй skill botforge и собери бота…».

### Cursor
```bash
cp telegram-skills/cursor/.cursorrules <your-project>/.cursorrules
```

### Codex / Codex CLI
```bash
cp telegram-skills/codex/AGENTS.md <your-project>/AGENTS.md
```

### Любой LLM (Claude.ai, ChatGPT, API)
Скопируйте содержимое [`system_prompt.txt`](system_prompt.txt) в **System Instructions** / Project Instructions / Custom GPT Instructions.

---

## Формат запроса

```
BotForge: Pro
Задача: бот-витрина онлайн-курсов с оплатой ЮKassa и закрытым каналом
Ограничения: VPS, до 50k пользователей, запуск через 2 недели
```

AI ответит:
1. Бизнес-брифинг (≤5 вопросов)
2. ADR (Architecture Decision Record)
3. Дерево проекта
4. Файлы в порядке зависимости
5. Self-review checklist
6. Инструкция по деплою

---

## Что покрывает skill

- ✅ Контент-боты и медиа-проекты
- ✅ Gated-контент с проверкой подписки на канал(ы)
- ✅ Платный доступ / VIP / подписки (Telegram Stars, ЮKassa, CryptoBot, Stripe, Tribute) — единый интерфейс
- ✅ **Telegram Mini Apps**: FastAPI backend + React/Vue + initData HMAC + JWT
- ✅ **Auth**: роли, ban, Mini App initData, OAuth bridging, API keys
- ✅ Рассылки (сегментированные, отложенные, A/B, rate-limited 25 msg/s)
- ✅ Сбор заявок / лидогенерация / CRM-sync
- ✅ Админ-панели (inline или Mini App) + audit log
- ✅ Интеграции: OpenAI, Anthropic, Google Sheets, WordPress, Notion, Airtable
- ✅ Мультиязычные боты (i18n middleware)
- ✅ Webhook-деплой (VPS, Fly.io, Railway)
- ✅ FSM-сценарии, inline-меню, CallbackData-фабрики
- ✅ Test suite: pytest + aiogram mocks + testcontainers
- ✅ Логирование, Sentry, retry, throttling, idempotency

## Grounded in official Telegram Bot API

Skill опирается на **Bot API 9.6 (apr 2026)** и официальную документацию:
- `core.telegram.org/bots/api` — методы, ошибки, webhook
- `core.telegram.org/bots/faq` — rate limits (1/sec per user, 20/min per group, 30/sec broadcast)
- `core.telegram.org/bots/webapps` — Mini Apps initData, events, CloudStorage
- `core.telegram.org/bots/payments-stars` — Telegram Stars (XTR)
- `core.telegram.org/bots` — deep links, BotCommandScope, MarkdownV2

Полная спецификация и лимиты — в [`references/telegram-api-spec.md`](.claude/skills/botforge/references/telegram-api-spec.md). Skill автоматически применяет эти ограничения: throttling до 25 msg/s, экранирование MarkdownV2, валидация initData HMAC, обработка `TelegramRetryAfter`/`Forbidden` и др.

## Slash-команды Claude Code

18 готовых команд в [`.claude/commands/`](.claude/commands/):

```
Создание/развитие:
/botforge-new            создать новый бот
/botforge-extend         добавить фичу
/botforge-review         code review
/botforge-refactor       рефакторинг монолита

Модули:
/botforge-miniapp        подключить Mini App
/botforge-auth           auth-слой (roles/miniapp/oauth/api-keys)
/botforge-payments       платежи (stars/yookassa/cryptobot/stripe/tribute)
/botforge-broadcast      система рассылок
/botforge-admin          админ-панель
/botforge-scheduler      scheduled tasks (apscheduler/arq/cron)
/botforge-inline         inline-режим (@botname query)
/botforge-i18n           мультиязычность (gettext + Babel)

Операции:
/botforge-test           тесты
/botforge-deploy         деплой (docker/fly/railway/vps)
/botforge-security       security-аудит
/botforge-botfather      BotFather setup + тексты
/botforge-observability  logging + Sentry + Prometheus + audit
/botforge-help           справка
```

## Полностью рабочий пример

В [`examples/01-vip-media-bot/`](examples/01-vip-media-bot/) — готовый VIP-бот на Telegram Stars, сгенерированный через skill. ~25 Python-файлов, Docker Compose, Alembic-миграции, webhook-режим, rate-limited throttling.

```bash
cd examples/01-vip-media-bot
cp .env.example .env   # заполни BOT_TOKEN, ADMIN_IDS
make up
make logs
```

Деплой на Fly.io / Railway / VPS — [`DEPLOY.md`](examples/01-vip-media-bot/docs/DEPLOY.md).

**Пример:** одной цепочкой собрать SaaS-бот с Mini App и платежами:
```
/botforge-new SaaS бот-витрина курсов с VIP
/botforge-payments yookassa подписка 499/мес
/botforge-miniapp каталог + личный кабинет
/botforge-admin webapp
/botforge-deploy fly webhook
/botforge-security all
```

---

## Для кого

- Фрилансеры и агентства, делающие ботов на заказ
- Владельцы Telegram-каналов и медиа-проектов
- SaaS-продукты с TG-дистрибуцией
- Команды, которым нужен единый стандарт
- Джуны, которым нужна «правильная» архитектура с первого дня

---

## Экономика

- **−15 часов** скаффолдинга на каждом боте
- **−80%** «давайте перепишем» через 3 месяца
- **+100%** скорость онбординга новых разработчиков на проект

---

## Лицензия

MIT. Используйте в коммерческих проектах. Атрибуция приветствуется, но не обязательна.

---

## Версия

**v1.0 Pro** — 2026-04-20. См. [CHANGELOG](docs/CHANGELOG.md) и [roadmap](docs/CHANGELOG.md#roadmap).
