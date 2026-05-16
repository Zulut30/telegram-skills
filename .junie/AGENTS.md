# Junie Guidelines — BotForge v1.8.0

Use these guidelines for JetBrains Junie and Junie CLI.

Read root `AGENTS.md` first. It is the canonical universal agent file. If the task is about Telegram bot creation, extension, review, refactor, deployment, payments, Mini Apps, admin panels, broadcasts, i18n, or observability, use the full skill in `.claude/skills/botforge/SKILL.md`.

For this repository, maintain adapter compatibility and run `make validate` after skill or adapter changes.

For generated bot projects, enforce Python 3.12+, aiogram 3.x, Bot API 10.0, handlers/services/repositories layering, PostgreSQL, SQLAlchemy 2 async, Alembic, Redis, Docker, httpx, tenacity, pytest, ruff, mypy, no secrets, no blocking I/O, no invented APIs, and no dead Telegram UI.
