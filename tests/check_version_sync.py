"""Verify VERSION file matches plugin.json and latest CHANGELOG entry.

Single source of truth: VERSION.
Exits non-zero if any of the three places disagree.
"""

from __future__ import annotations

import json
import pathlib
import re
import sys


def main() -> int:
    version_file = pathlib.Path("VERSION").read_text(encoding="utf-8").strip()

    manifest = json.loads(
        pathlib.Path(".claude-plugin/plugin.json").read_text(encoding="utf-8")
    )
    manifest_version = manifest["version"]

    changelog = pathlib.Path("docs/CHANGELOG.md").read_text(encoding="utf-8")
    match = re.search(r"^## v(\d+\.\d+(?:\.\d+)?)", changelog, re.MULTILINE)
    if not match:
        print("CHANGELOG: cannot find latest version header")
        return 1
    changelog_version = match.group(1)

    # plugin.json may carry a patch version (1.6.0), changelog may use minor (1.6)
    def normalize(v: str) -> tuple[int, ...]:
        parts = [int(p) for p in v.split(".")]
        while len(parts) < 3:
            parts.append(0)
        return tuple(parts)

    versions = {
        "VERSION": normalize(version_file),
        "plugin.json": normalize(manifest_version),
        "CHANGELOG.md": normalize(changelog_version),
    }

    if len(set(versions.values())) != 1:
        print("Version mismatch:")
        for src, v in versions.items():
            print(f"  {src}: {'.'.join(map(str, v))}")
        return 1

    print(f"Version sync OK: {version_file}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
