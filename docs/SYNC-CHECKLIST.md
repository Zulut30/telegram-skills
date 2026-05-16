# Agent sync checklist

The skill prompt must stay synchronized across core deployment formats and lightweight adapters. Use this checklist before any commit that changes skill behavior.

## Core prompt formats

| File | Target |
|---|---|
| `.claude/skills/botforge/SKILL.md` | Claude Code Agent Skill (canonical) |
| `system_prompt.txt` | Raw prompt for any LLM (Anthropic/OpenAI API, Custom GPT, Claude Projects) |
| `cursor/.cursor/rules/botforge.mdc` | Cursor (new MDC format) |
| `cursor/.cursorrules` | Cursor (legacy, kept for older versions) |
| `codex/AGENTS.md` | Legacy Codex install copy |
| `AGENTS.md` | Universal entrypoint for AGENTS-compatible tools |

## Adapter files

| File | Target |
|---|---|
| `.github/copilot-instructions.md` | GitHub Copilot / VS Code repository instructions |
| `.github/instructions/botforge.instructions.md` | GitHub Copilot / VS Code file-scoped instructions |
| `GEMINI.md` | Gemini CLI memory |
| `.gemini/skills/botforge/SKILL.md` | Gemini CLI skill bridge |
| `.cline/skills/botforge/SKILL.md` | Cline skill bridge |
| `.clinerules/botforge.md` | Cline rule |
| `.windsurf/rules/botforge.md` | Windsurf Cascade workspace rule |
| `.continue/rules/botforge.md` | Continue local rule |
| `.junie/AGENTS.md` | JetBrains Junie guidelines |
| `.rules` | Zed project rule |
| `CONVENTIONS.md` + `.aider.conf.yml` | Aider conventions |

## Before committing

If your change touches the **skill prompt**, sync across all core files:

- [ ] Updated `SKILL.md`
- [ ] Updated `system_prompt.txt`
- [ ] Updated `cursor/.cursor/rules/botforge.mdc`
- [ ] Updated `cursor/.cursorrules`
- [ ] Updated `codex/AGENTS.md`
- [ ] Updated `AGENTS.md`
- [ ] Sections match: workflow stages, tech standard, hard bans, UX navigation, modes, API constraints

If your change touches **agent compatibility**:

- [ ] Updated adapter files that need new routing/version text
- [ ] Updated `docs/AGENT-COMPATIBILITY.md`
- [ ] Updated README compatibility table if a new tool is added
- [ ] Updated `install.sh` if installation should copy the adapter
- [ ] Ran `python3 tests/validate_agent_adapters.py`

If your change touches **only a reference file** (`.claude/skills/botforge/references/*.md`):

- [ ] Updated the reference
- [ ] Referenced from `SKILL.md` if new
- [ ] Referenced from `codex/AGENTS.md` "File references" section if new
- [ ] Added to `plugin.json` `references` array if new

If your change adds a **new slash command**:

- [ ] Created `.claude/commands/botforge-<name>.md` with frontmatter
- [ ] Registered in `.claude-plugin/plugin.json` commands array
- [ ] Added row to `.claude/commands/botforge-help.md`
- [ ] Mentioned in root `README.md`
- [ ] Added entry to `CHANGELOG.md`

## Automated enforcement

CI (`.github/workflows/validate.yml`) checks:
- `plugin.json` references existing files
- Command markdown files have valid YAML frontmatter with `description`
- Agent adapters exist, carry the current version, and have valid required frontmatter
- Core prompt files carry mandatory BotForge concepts
- Version sync across skill/adapters
- Markdown files lint clean when markdownlint is available

## Common drift sources

- Adding a constraint to `SKILL.md` but forgetting `system_prompt.txt`
- Renaming a mode in one file but not others
- Updating Bot API version (10.0 → next) in only `telegram-api-spec.md` without propagating to system prompts
- Adding a new adapter but not adding it to `tests/validate_agent_adapters.py`

## Fast sync tip

Cmd/Ctrl + Shift + F on the repo for `Bot API 10.0`, `BotForge v`, or any versioned token → ensure all matches update together.
