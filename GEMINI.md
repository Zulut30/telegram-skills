# GEMINI.md — BotForge v1.8.0

Gemini CLI should treat this repository as the BotForge skill distribution. For a task about creating, extending, refactoring, reviewing, or deploying a Telegram bot, activate the BotForge behavior in `AGENTS.md`.

Canonical routing:

- Universal agent instructions: `AGENTS.md`
- Claude/Gemini/Cline-style skill package: `.claude/skills/botforge/SKILL.md`
- Gemini workspace skill bridge: `.gemini/skills/botforge/SKILL.md`
- Raw prompt fallback: `system_prompt.txt`
- Deep references: `.claude/skills/botforge/references/`

Core constraints: Python 3.12+, aiogram 3.x, Bot API 10.0, PostgreSQL + SQLAlchemy 2 async + Alembic, Redis, Docker, async httpx, tenacity, pytest, ruff, mypy. Never generate secrets in code, blocking I/O, invented Telegram/aiogram APIs, ORM outside repositories, or dead Telegram UI.

When maintaining this repo, run `make validate` after changing skill behavior or adapter files.
