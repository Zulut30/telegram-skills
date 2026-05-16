---
name: BotForge
description: BotForge v1.8.0 production Telegram bot engineering rules for aiogram 3, Bot API 10.0, layered architecture, payments, Mini Apps, admin panels, tests, and deploy.
alwaysApply: false
globs: "**/*.py,**/*.md,**/*.toml,**/*.yml,**/*.yaml,**/Dockerfile,Dockerfile"
---

# BotForge v1.8.0 — Continue Rule

Apply when the task involves Telegram bots or this BotForge skill repository.

Read `AGENTS.md` for universal guidance. Read `.claude/skills/botforge/SKILL.md` for the full skill and references.

Generate or review bots with strict layers, async I/O, typed settings, migrations, tests, Docker, structured logs, and explicit Telegram UX navigation. Never add secrets, blocking `requests`, invented Telegram/aiogram APIs, ORM outside repositories, or dead buttons.
