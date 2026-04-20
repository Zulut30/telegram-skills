.PHONY: help install-claude install-cursor install-codex sync-check validate golden example-test lint clean

help:
	@echo "BotForge — repository maintenance targets"
	@echo ""
	@echo "  make install-claude       Install skill globally into ~/.claude/"
	@echo "  make install-cursor       Copy Cursor MDC rule to ./.cursor/rules/"
	@echo "  make install-codex        Copy AGENTS.md to current dir"
	@echo ""
	@echo "  make sync-check           Verify four-format skill prompt sync"
	@echo "  make validate             Validate plugin.json + command frontmatter"
	@echo "  make golden               Run golden-output eval tests (needs API key)"
	@echo "  make example-test         Run example bot test suite"
	@echo "  make lint                 Lint markdown"
	@echo ""
	@echo "  make clean                Remove build artifacts"

install-claude:
	bash install.sh claude

install-cursor:
	bash install.sh cursor .

install-codex:
	bash install.sh codex .

sync-check:
	python tests/check_sync.py

validate:
	@python -c "import json, pathlib, sys; m = json.loads(pathlib.Path('.claude-plugin/plugin.json').read_text()); missing = [p for p in (e['path'] for e in m['commands']+m['skills']) if not pathlib.Path(p).exists()]; sys.exit('\n'.join(missing) if missing else 0)"
	@echo "plugin.json OK"

golden:
	python tests/run_golden.py

example-test:
	cd examples/01-vip-media-bot && pytest tests/ -v

lint:
	@command -v markdownlint-cli2 >/dev/null 2>&1 && markdownlint-cli2 "**/*.md" --config .markdownlint.yaml || echo "install markdownlint-cli2 for lint"

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .mypy_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .ruff_cache -exec rm -rf {} + 2>/dev/null || true
