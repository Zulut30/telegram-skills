"""Bump version across VERSION, plugin.json, and CHANGELOG scaffolding.

Usage:
    python tests/bump_version.py patch      # 1.5.0 → 1.5.1
    python tests/bump_version.py minor      # 1.5.0 → 1.6.0
    python tests/bump_version.py major      # 1.5.0 → 2.0.0
    python tests/bump_version.py 1.7.2      # explicit

Prints new version. Does NOT commit or tag — intentional, so you can review.
"""

from __future__ import annotations

import json
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
    match level:
        case "major":
            return (major + 1, 0, 0)
        case "minor":
            return (major, minor + 1, 0)
        case "patch":
            return (major, minor, patch + 1)
        case _:
            if re.fullmatch(r"\d+\.\d+\.\d+", level):
                return tuple(int(p) for p in level.split("."))  # type: ignore[return-value]
            raise SystemExit(f"unknown level: {level!r} (use major|minor|patch|X.Y.Z)")


def write_version_file(v: tuple[int, int, int]) -> None:
    pathlib.Path("VERSION").write_text(".".join(map(str, v)) + "\n", encoding="utf-8")


def update_plugin_manifest(v: tuple[int, int, int]) -> None:
    path = pathlib.Path(".claude-plugin/plugin.json")
    manifest = json.loads(path.read_text(encoding="utf-8"))
    manifest["version"] = ".".join(map(str, v))
    path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 1

    level = sys.argv[1]
    new = bump(level)
    new_str = ".".join(map(str, new))

    write_version_file(new)
    update_plugin_manifest(new)

    print(f"Bumped to {new_str}")
    print("Remember to:")
    print(f"  1. Prepend a new section to docs/CHANGELOG.md: ## v{new_str} — YYYY-MM-DD")
    print("  2. Commit: git commit -am 'chore: bump version to " f"{new_str}'")
    print(f"  3. Tag:    git tag v{new_str}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
