---
name: botforge
description: Production-grade Telegram bot engineering skill for Gemini CLI. Use when creating, extending, refactoring, reviewing, testing, securing, or deploying Telegram bots in Python with aiogram 3, Bot API 10.0, PostgreSQL, Redis, Docker, payments, Mini Apps, admin panels, or broadcast systems.
---

# BotForge v1.8.0 for Gemini CLI

Load the canonical BotForge instructions from `AGENTS.md`. If the task needs the full skill workflow or detailed references, read `.claude/skills/botforge/SKILL.md` and only the specific reference file needed from `.claude/skills/botforge/references/`.

Use the six-stage workflow for new bots: Business brief, ADR, Project tree, Files, Self-review, Deployment. For small fixes, use the Bypass Protocol in `AGENTS.md`.

Hard bans remain active: no secrets in code, no blocking I/O or `requests`, no invented Telegram/aiogram APIs, no ORM outside repositories, no business logic in handlers, no unverified payments/webhooks, no dead Telegram UI.
