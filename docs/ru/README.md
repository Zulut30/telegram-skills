# BotForge

> **Skill для AI, создающий production-ready Telegram-ботов.**
> Готовый пакет для Claude Code, Cursor, Codex и любого LLM.

[English version](../../README.md) · [Установка](../INSTALL.md) · [Quickstart](../QUICKSTART.md)

---

## Что это

BotForge превращает AI-ассистента в **senior-инженера Telegram-ботов**. Вместо одноразового `main.py` на 800 строк AI проектирует и собирает модульного, масштабируемого production-ready бота — с архитектурой, БД, миграциями, админкой, платежами, рассылками, Docker и деплоем.

## Три обещания

1. **Не монолит.** Слоёная архитектура (handlers / services / repositories / integrations) из коробки.
2. **Не черновик.** Docker + Postgres + Alembic + `.env` + инструкции деплоя в первой же генерации.
3. **Не разваливается.** Пятую фичу добавляете так же легко, как первую.

## Почему это работает

- **Опирается на официальные доки Telegram Bot API 9.6** — rate limits (1/сек, 20/мин, 30/сек broadcast), MarkdownV2 escape, Mini App initData HMAC, `CallbackData` 64 байта, все константы цитируются из `core.telegram.org`.
- **Обязательный 6-stage workflow** — Brief → ADR → Tree → Files → Self-review → Deploy. AI не может «срезать» до генерации кода.
- **Hard bans** — секреты в коде, `requests`, SQL в handlers, монолит — блокируются на уровне правил skill, а не стилем.
- **Единый интерфейс платежей** — смена ЮKassa → Stripe = замена одной строки DI.

## Быстрый старт

```bash
git clone https://github.com/Zulut30/telegram-skills.git
cp -r telegram-skills/.claude/skills/botforge ~/.claude/skills/
cp -r telegram-skills/.claude/commands ~/.claude/
```

В Claude Code:
```
/botforge-new SaaS
Задача: бот-витрина онлайн-курсов с VIP-доступом за 499 ₽/мес
Хостинг: VPS, Docker Compose, webhook
```

AI задаст уточняющие вопросы, предложит ADR, построит дерево, сгенерирует все файлы, прогонит self-review и выдаст команды деплоя.

## 18 slash-команд

```
Создание/развитие:   /botforge-new /botforge-extend /botforge-review /botforge-refactor
Модули:              /botforge-miniapp /botforge-auth /botforge-payments
                     /botforge-broadcast /botforge-admin /botforge-scheduler
                     /botforge-inline /botforge-i18n
Операции:            /botforge-test /botforge-deploy /botforge-security
                     /botforge-botfather /botforge-observability /botforge-help
```

## Рабочий пример

[`examples/01-vip-media-bot/`](../../examples/01-vip-media-bot/) — VIP-бот на Telegram Stars, ~25 Python-файлов, всё как надо.

```bash
cd examples/01-vip-media-bot
cp .env.example .env   # BOT_TOKEN, ADMIN_IDS
make up
```

## Четыре режима

| Режим | Когда | Особенности |
|---|---|---|
| **Lite** | MVP за вечер | SQLite, polling, без Docker |
| **Pro** (default) | Коммерческий бот | Полный production-стандарт |
| **Media** | Контент/каналы | + CMS-sync, сегментированные рассылки, UTM |
| **SaaS** | Подписки/VIP | + biling, multi-provider payments, admin metrics |

## Документация

- [QUICKSTART](../QUICKSTART.md) — 5 минут от нуля до бота
- [INSTALL](../INSTALL.md) — детальная установка в каждый инструмент
- [USAGE](../USAGE.md) — режимы, промпт-форматы, сессии
- [CHANGELOG](../CHANGELOG.md) — история версий + roadmap
- [COMPARISON](../COMPARISON.md) — vs альтернатив (cookiecutter, no-code, generic agents)
- [SHOWCASE](../SHOWCASE.md) — примеры живых ботов

## Reference-модули

17 глубоких ссылочных документов по всем аспектам: архитектура, 12 паттернов, Mini App, auth, платежи (5 провайдеров), Telegram API 9.6, BotFather setup, i18n, observability, scheduler, subscriptions, inline mode, groups/channels, media, FAQ.

## Лицензия

MIT. Используйте в коммерческих проектах без ограничений.

## Контрибьюции

См. [CONTRIBUTING](../../CONTRIBUTING.md) и [SECURITY](../../SECURITY.md). PR приветствуются.
