#!/usr/bin/env bash
# BotForge one-liner installer.
# Usage:
#   curl -fsSL https://raw.githubusercontent.com/Zulut30/telegram-skills/main/install.sh | bash
#   curl -fsSL https://raw.githubusercontent.com/Zulut30/telegram-skills/main/install.sh | bash -s -- cursor
#   curl -fsSL https://raw.githubusercontent.com/Zulut30/telegram-skills/main/install.sh | bash -s -- codex /path/to/project

set -euo pipefail

TARGET="${1:-claude}"
PROJECT_DIR="${2:-.}"
REPO_URL="${BOTFORGE_REPO:-https://github.com/Zulut30/telegram-skills.git}"
REF="${BOTFORGE_REF:-main}"

say() { printf "\033[36m[BotForge]\033[0m %s\n" "$*"; }
die() { printf "\033[31m[BotForge] error:\033[0m %s\n" "$*" >&2; exit 1; }

command -v git >/dev/null 2>&1 || die "git is required"

TMPDIR="$(mktemp -d)"
trap 'rm -rf "$TMPDIR"' EXIT

say "cloning $REPO_URL@$REF …"
git clone --depth 1 --branch "$REF" "$REPO_URL" "$TMPDIR" >/dev/null 2>&1

case "$TARGET" in
  claude)
    DEST="${HOME}/.claude"
    mkdir -p "$DEST/skills" "$DEST/commands"
    cp -r "$TMPDIR/.claude/skills/botforge" "$DEST/skills/"
    cp -r "$TMPDIR/.claude/commands/"*.md "$DEST/commands/"
    say "installed to $DEST (global — available in every project)"
    ;;
  claude-project)
    [[ -d "$PROJECT_DIR" ]] || die "project dir not found: $PROJECT_DIR"
    mkdir -p "$PROJECT_DIR/.claude/skills" "$PROJECT_DIR/.claude/commands"
    cp -r "$TMPDIR/.claude/skills/botforge" "$PROJECT_DIR/.claude/skills/"
    cp -r "$TMPDIR/.claude/commands/"*.md "$PROJECT_DIR/.claude/commands/"
    cp "$TMPDIR/.claude-plugin/plugin.json" "$PROJECT_DIR/.claude-plugin/" 2>/dev/null || \
      (mkdir -p "$PROJECT_DIR/.claude-plugin" && cp "$TMPDIR/.claude-plugin/plugin.json" "$PROJECT_DIR/.claude-plugin/")
    say "installed to $PROJECT_DIR/.claude (per-project)"
    ;;
  cursor)
    [[ -d "$PROJECT_DIR" ]] || die "project dir not found: $PROJECT_DIR"
    mkdir -p "$PROJECT_DIR/.cursor/rules"
    cp "$TMPDIR/cursor/.cursor/rules/botforge.mdc" "$PROJECT_DIR/.cursor/rules/"
    [[ -f "$PROJECT_DIR/.cursorrules" ]] || cp "$TMPDIR/cursor/.cursorrules" "$PROJECT_DIR/.cursorrules"
    say "installed Cursor rules to $PROJECT_DIR/.cursor/rules/botforge.mdc"
    ;;
  codex)
    [[ -d "$PROJECT_DIR" ]] || die "project dir not found: $PROJECT_DIR"
    cp "$TMPDIR/codex/AGENTS.md" "$PROJECT_DIR/AGENTS.md"
    say "installed Codex AGENTS.md to $PROJECT_DIR/AGENTS.md"
    ;;
  system-prompt)
    cp "$TMPDIR/system_prompt.txt" "$PROJECT_DIR/botforge_system_prompt.txt"
    say "copied raw system prompt to $PROJECT_DIR/botforge_system_prompt.txt"
    ;;
  *)
    die "unknown target: $TARGET (valid: claude, claude-project, cursor, codex, system-prompt)"
    ;;
esac

say "done. Try: /botforge-help (in Claude Code) or see docs/QUICKSTART.md"
