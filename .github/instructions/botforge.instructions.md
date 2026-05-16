---
applyTo: "**/*.py,**/*.md,**/*.toml,**/*.yml,**/*.yaml,**/Dockerfile,Dockerfile,**/*.env.example"
---

# BotForge v1.8.0

Use BotForge rules when working on Telegram bot code or this skill repository. Read `AGENTS.md` first, then `.claude/skills/botforge/SKILL.md` for the complete workflow and references.

Keep generated bot code layered: handlers call services, services call repositories, repositories own ORM/SQL. Use async I/O, timeouts, retries, structured logs, typed settings, Docker, Alembic, and tests. Never add secrets, blocking `requests`, invented Telegram/aiogram APIs, or unhandled keyboard callbacks.
