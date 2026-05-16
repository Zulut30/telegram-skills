# BotForge Agent Compatibility Audit

**Version:** 1.8.0
**Date:** 2026-05-16

## Audit findings

1. **Root `AGENTS.md` was missing.** `codex/AGENTS.md` was strong, but many agents auto-load only a root-level `AGENTS.md`. This weakened Codex, Copilot, VS Code, Windsurf, Junie, Zed, OpenCode, Aider, and AGENTS-compatible tools.
2. **Tool-specific adapters were uneven.** Claude Code and Cursor were first-class; GitHub Copilot, Gemini CLI, Cline, Windsurf, Continue, Aider, Junie, and Zed needed native entrypoints or bridge files.
3. **Validation did not protect adapters.** Existing checks covered the main skill formats, but not adapter presence, frontmatter, or version drift across new agent files.
4. **Installation flow was too narrow.** `install.sh` had Claude/Cursor/Codex/system-prompt targets, but no one-command project adapter install.
5. **Docs undersold compatibility.** README and sync checklist described four/five formats, while the repo now needs a clearer compatibility matrix.

## Compatibility matrix

| Agent or app | Native file now supported | Notes |
|---|---|---|
| Claude Code / Claude Agent | `.claude/skills/botforge/SKILL.md`, `.claude/commands/*.md`, `CLAUDE.md` | Canonical skill remains here. |
| Codex / OpenAI Codex / OpenCode | `AGENTS.md` | Root universal entrypoint. |
| Cursor | `cursor/.cursor/rules/botforge.mdc`, `cursor/.cursorrules`, `AGENTS.md` | MDC remains primary; root `AGENTS.md` adds portability. |
| GitHub Copilot / VS Code | `.github/copilot-instructions.md`, `.github/instructions/botforge.instructions.md`, `AGENTS.md` | Repo-wide plus file-scoped instructions. |
| Gemini CLI | `GEMINI.md`, `.gemini/skills/botforge/SKILL.md`, `AGENTS.md` | Workspace memory plus skill bridge. |
| Windsurf Cascade | `.windsurf/rules/botforge.md`, `AGENTS.md` | `model_decision` rule keeps context cost low. |
| Cline | `.cline/skills/botforge/SKILL.md`, `.clinerules/botforge.md`, `.claude/skills/botforge/SKILL.md`, `AGENTS.md` | Skill bridge plus concise rule. |
| Continue | `.continue/rules/botforge.md` | Local rule with globs and description. |
| Aider | `CONVENTIONS.md`, `.aider.conf.yml`, `AGENTS.md` | `CONVENTIONS.md` is loaded read-only. |
| Junie / JetBrains | `.junie/AGENTS.md`, `AGENTS.md` | Junie-specific preferred location plus root fallback. |
| Zed | `.rules`, `AGENTS.md`, `.github/copilot-instructions.md` | `.rules` prevents Zed from stopping at a weaker compatibility file. |
| Generic LLM apps / APIs | `system_prompt.txt` | Raw prompt fallback for ChatGPT, Claude Projects, Anthropic/OpenAI API, and custom agents. |

## Improvement plan

1. Keep `.claude/skills/botforge/SKILL.md` canonical and concise; move detailed domain knowledge to references.
2. Treat root `AGENTS.md` as the universal, portable control plane.
3. Keep tool adapters as small bridges unless the tool requires enough always-on context to avoid a missed activation.
4. Update installer targets so projects can install all adapters in one command.
5. Extend `make validate` to check adapter files, required frontmatter, version sync, and canonical references.
6. Keep docs current whenever a new agent adapter is added or an existing tool changes its discovery path.

## Quality bar

- Every adapter must include `BotForge v<version>` and a route to `AGENTS.md` or `.claude/skills/botforge/SKILL.md`.
- Tool-specific frontmatter must stay valid.
- No adapter may weaken safety/integrity bans.
- No adapter should duplicate the full skill unless the tool cannot reliably read references.
- `make validate` must pass before release.

## Sources checked

- Claude Code skills: https://code.claude.com/docs/en/skills
- Cursor rules: https://docs.cursor.com/en/context
- GitHub Copilot custom instructions: https://docs.github.com/en/copilot/how-tos/copilot-cli/add-custom-instructions
- Gemini CLI memory and skills: https://github.com/google-gemini/gemini-cli/blob/main/docs/reference/tools.md
- Windsurf rules: https://docs.windsurf.com/windsurf/cascade/memories
- Cline rules and skills: https://docs.cline.bot/customization/cline-rules and https://docs.cline.bot/customization/skills
- Continue rules: https://docs.continue.dev/customize/rules
- Zed rules: https://zed.dev/docs/ai/rules
- Junie guidelines: https://www.jetbrains.com/help/junie/customize-guidelines.html
- Aider conventions: https://github.com/Aider-AI/conventions
