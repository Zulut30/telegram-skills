"""Bump version across VERSION, plugin.json, and CHANGELOG scaffolding.

Usage:
    python3 tests/bump_version.py patch      # 1.5.0 → 1.5.1
    python3 tests/bump_version.py minor      # 1.5.0 → 1.6.0
    python3 tests/bump_version.py major      # 1.5.0 → 2.0.0
    python3 tests/bump_version.py 1.7.2      # explicit

Prints new version. Does NOT commit or tag — intentional, so you can review.
"""

from __future__ import annotations

import pathlib
import re
import sys


def current() -> tuple[int, int, int]:
    raw = pathlib.Path("VERSION").read_text(encoding="utf-8").strip()
    parts = [int(p) for p in raw.split(".")]
    while len(parts) < 3:
        parts.append(0)
    return tuple(parts[:3])  # type: ignore[return-value]


def bump(level: str) -> tuple[int, int, int]:
    major, minor, patch = current()
    if level == "major":
        return (major + 1, 0, 0)
    if level == "minor":
        return (major, minor + 1, 0)
    if level == "patch":
        return (major, minor, patch + 1)
    if re.fullmatch(r"\d+\.\d+\.\d+", level):
        return tuple(int(p) for p in level.split("."))  # type: ignore[return-value]
    raise SystemExit(f"unknown level: {level!r} (use major|minor|patch|X.Y.Z)")


def write_version_file(v: tuple[int, int, int]) -> None:
    pathlib.Path("VERSION").write_text(".".join(map(str, v)) + "\n", encoding="utf-8")


def update_plugin_manifest(v: tuple[int, int, int]) -> None:
    path = pathlib.Path(".claude-plugin/plugin.json")
    new_str = ".".join(map(str, v))
    text = path.read_text(encoding="utf-8")
    new_text, n = re.subn(
        r'("version":\s*")\d+\.\d+\.\d+(")',
        rf"\g<1>{new_str}\2",
        text,
        count=1,
    )
    if n != 1:
        raise SystemExit(f"could not update version in {path}")
    path.write_text(new_text, encoding="utf-8")


#: Human-readable version markers that should track VERSION. Changelog history
#: is intentionally excluded; release notes are edited manually.
_VERSION_TEXT_TARGETS: tuple[pathlib.Path, ...] = (
    pathlib.Path("AGENTS.md"),
    pathlib.Path(".claude/skills/botforge/SKILL.md"),
    pathlib.Path("SKILL.md"),
    pathlib.Path("system_prompt.txt"),
    pathlib.Path("codex/AGENTS.md"),
    pathlib.Path("cursor/.cursor/rules/botforge.mdc"),
    pathlib.Path("cursor/.cursorrules"),
    pathlib.Path(".github/copilot-instructions.md"),
    pathlib.Path(".github/instructions/botforge.instructions.md"),
    pathlib.Path("GEMINI.md"),
    pathlib.Path(".gemini/skills/botforge/SKILL.md"),
    pathlib.Path(".cline/skills/botforge/SKILL.md"),
    pathlib.Path(".clinerules/botforge.md"),
    pathlib.Path(".windsurf/rules/botforge.md"),
    pathlib.Path(".continue/rules/botforge.md"),
    pathlib.Path(".junie/AGENTS.md"),
    pathlib.Path(".rules"),
    pathlib.Path("CONVENTIONS.md"),
    pathlib.Path("docs/AGENT-COMPATIBILITY.md"),
)


def update_version_markers(v: tuple[int, int, int]) -> list[pathlib.Path]:
    """Patch BotForge version markers in active prompt and adapter files."""
    new_str = ".".join(map(str, v))
    new_minor = ".".join(map(str, v[:2]))
    patched: list[pathlib.Path] = []
    for path in _VERSION_TEXT_TARGETS:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        new_text = re.sub(
            r"(BotForge v)\d+\.\d+\.\d+",
            rf"\g<1>{new_str}",
            text,
        )
        new_text = re.sub(
            r"(BotForge v)\d+\.\d+(?=\s+—)",
            rf"\g<1>{new_minor}",
            new_text,
        )
        new_text = re.sub(
            r"(\*\*Version:\*\*\s*)\d+\.\d+\.\d+",
            rf"\g<1>{new_str}",
            new_text,
        )
        new_text = re.sub(
            r"(Version:\s*)\d+\.\d+\.\d+",
            rf"\g<1>{new_str}",
            new_text,
        )
        if new_text != text:
            path.write_text(new_text, encoding="utf-8")
            patched.append(path)
    return patched


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 1

    level = sys.argv[1]
    new = bump(level)
    new_str = ".".join(map(str, new))

    write_version_file(new)
    update_plugin_manifest(new)
    patched = update_version_markers(new)

    print(f"Bumped to {new_str}")
    for p in patched:
        print(f"  patched header in {p}")
    print("Remember to:")
    print(f"  1. Prepend a new section to docs/CHANGELOG.md: ## v{new_str} — YYYY-MM-DD")
    print("  2. Commit: git commit -am 'chore: bump version to " f"{new_str}'")
    print(f"  3. Tag:    git tag v{new_str}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
