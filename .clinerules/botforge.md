# BotForge v1.8.0 — Cline Rule

Use BotForge for Telegram bot work. Read `AGENTS.md` as the universal rule file and `.claude/skills/botforge/SKILL.md` as the canonical full skill.

Key behavior:

- New bots use Brief → ADR → Tree → Files → Self-review → Deploy.
- Keep aiogram 3 projects layered: handlers → services → repositories.
- Use Python 3.12+, PostgreSQL, SQLAlchemy 2 async, Alembic, Redis, Docker, httpx, tenacity, pytest, ruff, mypy.
- Enforce Bot API 10.0 constraints, especially rate limits, callback data 64 bytes, Mini App initData HMAC, Stars `XTR`, Guest Mode, and `allowed_updates`.
- Never generate secrets, blocking `requests`, invented Telegram/aiogram APIs, direct ORM in handlers/services, or dead buttons.
