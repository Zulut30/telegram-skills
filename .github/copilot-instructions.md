# BotForge v1.8.0 — GitHub Copilot Instructions

This repository ships BotForge, a production-grade Telegram bot engineering skill.

When the user asks to create, extend, refactor, review, test, secure, or deploy a Telegram bot, follow BotForge:

- Prefer the canonical instructions in `AGENTS.md`; if deeper detail is needed, read `.claude/skills/botforge/SKILL.md`.
- Use Python 3.12+, aiogram 3.x, SQLAlchemy 2 async, Alembic, PostgreSQL, Redis, pydantic-settings, httpx, tenacity, Docker, pytest, ruff, and mypy.
- Preserve the six-stage workflow for new bots: Business brief, ADR, Project tree, Files, Self-review, Deployment.
- Enforce hard bans: no secrets in code, no blocking I/O or `requests`, no invented Telegram/aiogram APIs, no ORM outside repositories, no business logic in handlers, no dead Telegram buttons.
- Use Telegram Bot API 10.0 constraints from `.claude/skills/botforge/references/telegram-api-spec.md`.

For repository maintenance, keep all agent adapters synchronized and run `make validate`.
