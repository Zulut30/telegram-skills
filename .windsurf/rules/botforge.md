---
trigger: model_decision
description: BotForge v1.8.0 — use for Telegram bot creation, extension, review, refactor, deploy, Mini Apps, payments, admin panels, broadcasts, i18n, and aiogram 3 production architecture.
---

# BotForge v1.8.0 — Windsurf Rule

When Cascade decides this rule is relevant, read `AGENTS.md` first. For complete workflow details, read `.claude/skills/botforge/SKILL.md` and then the specific reference needed from `.claude/skills/botforge/references/`.

BotForge defaults:

- Python 3.12+, aiogram 3.x, Bot API 10.0.
- Layered architecture: handlers are transport only; services hold business logic; repositories own ORM/SQL.
- New bot workflow: Business brief, ADR, Project tree, Files, Self-review, Deployment.
- Hard bans: secrets in code, blocking I/O, `requests`, invented Telegram/aiogram APIs, bypassed payment/webhook verification, dead buttons.
