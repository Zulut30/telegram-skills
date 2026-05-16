# BotForge v1.8.0 — Aider Conventions

Use these conventions when Aider works on BotForge or on a Telegram bot project that uses BotForge.

- Read `AGENTS.md` first. It is the universal agent instruction file.
- Use `.claude/skills/botforge/SKILL.md` for the complete BotForge workflow and reference map.
- For new bots, follow Brief → ADR → Tree → Files → Self-review → Deploy.
- Use Python 3.12+, aiogram 3.x, Bot API 10.0, SQLAlchemy 2 async, Alembic, PostgreSQL, Redis, pydantic-settings, httpx, tenacity, Docker, pytest, ruff, and mypy.
- Keep handlers thin; services hold business logic; repositories own ORM/SQL.
- Never write secrets in code, blocking `requests`, invented Telegram/aiogram APIs, business logic in handlers, ORM outside repositories, or dead Telegram buttons.
- When editing this repository, preserve user changes and run `make validate`.
