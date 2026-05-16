"""Validate cross-agent adapter files for BotForge.

This intentionally checks structure, not exact wording. The goal is to catch
missing adapter files, broken frontmatter, and version drift before release.
"""

from __future__ import annotations

import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()

ADAPTERS_WITH_VERSION = (
    "AGENTS.md",
    ".github/copilot-instructions.md",
    ".github/instructions/botforge.instructions.md",
    "GEMINI.md",
    ".gemini/skills/botforge/SKILL.md",
    ".cline/skills/botforge/SKILL.md",
    ".clinerules/botforge.md",
    ".windsurf/rules/botforge.md",
    ".continue/rules/botforge.md",
    ".junie/AGENTS.md",
    ".rules",
    "CONVENTIONS.md",
    "docs/AGENT-COMPATIBILITY.md",
)

REQUIRED_FILES = ADAPTERS_WITH_VERSION + (".aider.conf.yml",)

FRONTMATTER_REQUIRED: dict[str, dict[str, str | None]] = {
    ".github/instructions/botforge.instructions.md": {"applyTo": None},
    ".windsurf/rules/botforge.md": {
        "trigger": "model_decision",
        "description": None,
    },
    ".continue/rules/botforge.md": {
        "name": "BotForge",
        "description": None,
        "alwaysApply": "false",
        "globs": None,
    },
    ".gemini/skills/botforge/SKILL.md": {
        "name": "botforge",
        "description": None,
    },
    ".cline/skills/botforge/SKILL.md": {
        "name": "botforge",
        "description": None,
    },
}


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---", 4)
    if end == -1:
        return {}
    raw = text[4:end].strip()
    data: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def has_version(text: str) -> bool:
    needles = (
        f"BotForge v{VERSION}",
        f"**Version:** {VERSION}",
        f"Version: {VERSION}",
    )
    return any(needle in text for needle in needles)


def main() -> int:
    errors: list[str] = []

    for rel in REQUIRED_FILES:
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing adapter: {rel}")
            continue
        if not path.is_file():
            errors.append(f"adapter is not a file: {rel}")

    for rel in ADAPTERS_WITH_VERSION:
        path = ROOT / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if "BotForge" not in text:
            errors.append(f"{rel}: missing BotForge marker")
        if not has_version(text):
            errors.append(f"{rel}: missing version {VERSION}")
        if rel != "AGENTS.md" and not (
            "AGENTS.md" in text
            or ".claude/skills/botforge/SKILL.md" in text
            or "system_prompt.txt" in text
        ):
            errors.append(f"{rel}: missing route to canonical instructions")

    aider_conf = ROOT / ".aider.conf.yml"
    if aider_conf.exists() and "read: CONVENTIONS.md" not in aider_conf.read_text(
        encoding="utf-8"
    ):
        errors.append(".aider.conf.yml: must load CONVENTIONS.md")

    for rel, required in FRONTMATTER_REQUIRED.items():
        path = ROOT / rel
        if not path.exists():
            continue
        data = parse_frontmatter(path.read_text(encoding="utf-8"))
        if not data:
            errors.append(f"{rel}: missing YAML frontmatter")
            continue
        for key, expected in required.items():
            if key not in data:
                errors.append(f"{rel}: missing frontmatter key {key!r}")
            elif expected is not None and data[key] != expected:
                errors.append(
                    f"{rel}: frontmatter {key!r} expected {expected!r}, got {data[key]!r}"
                )

    if errors:
        print("Agent adapter validation failed:\n")
        for err in errors:
            print(f"  ✗ {err}")
        return 1

    print(f"Agent adapters OK: {len(REQUIRED_FILES)} files, version {VERSION}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
