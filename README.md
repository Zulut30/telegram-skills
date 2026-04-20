# BotForge

> **The Telegram Bot Engineering Skill for AI**
> Production-ready skill pack for Claude Code, Codex, Cursor and any LLM.

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
| [`.claude/skills/botforge/`](.claude/skills/botforge/) | Skill для **Claude Code** (формат Agent Skills) |
| [`cursor/.cursorrules`](cursor/.cursorrules) | Правила для **Cursor** |
| [`codex/AGENTS.md`](codex/AGENTS.md) | Инструкция для **OpenAI Codex / Codex CLI** |
| [`docs/INSTALL.md`](docs/INSTALL.md) | Как установить в каждый инструмент |
| [`docs/USAGE.md`](docs/USAGE.md) | Как пользоваться: режимы, промпт-форматы, сессии |
| [`docs/CHANGELOG.md`](docs/CHANGELOG.md) | История версий и roadmap |
| [`examples/`](examples/) | Кейсы ботов, сгенерированных через skill |

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
- ✅ Платный доступ / VIP / подписки (Telegram Stars, ЮKassa, CryptoBot, Stripe)
- ✅ Рассылки (сегментированные, отложенные, A/B, rate-limited)
- ✅ Сбор заявок / лидогенерация / CRM-sync
- ✅ Админ-панели с ролями
- ✅ Интеграции: OpenAI, Anthropic, Google Sheets, WordPress, Notion, Airtable
- ✅ Мультиязычные боты (i18n middleware)
- ✅ Webhook-деплой (VPS, Fly.io, Railway)
- ✅ FSM-сценарии, inline-меню, callback-фабрики
- ✅ Логирование, Sentry, retry, throttling, idempotency

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
