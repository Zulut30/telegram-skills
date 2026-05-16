PYTHON ?= python3

.PHONY: help install-claude install-cursor install-codex install-agent-adapters install-all-agents sync-check validate golden example-test lint clean

help:
	@echo "BotForge — repository maintenance targets"
	@echo ""
	@echo "  make install-claude       Install skill globally into ~/.claude/"
	@echo "  make install-cursor       Copy Cursor MDC rule to ./.cursor/rules/"
	@echo "  make install-codex        Copy AGENTS.md to current dir"
	@echo "  make install-agent-adapters Copy cross-agent adapters to current dir"
	@echo "  make install-all-agents   Install Claude project + Cursor + adapters"
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

install-agent-adapters:
	bash install.sh agent-adapters .

install-all-agents:
	bash install.sh all-agents .

sync-check:
	$(PYTHON) tests/check_sync.py

version-check:
	$(PYTHON) tests/check_version_sync.py

bump-patch:
	$(PYTHON) tests/bump_version.py patch

bump-minor:
	$(PYTHON) tests/bump_version.py minor

bump-major:
	$(PYTHON) tests/bump_version.py major

validate:
	$(PYTHON) tests/validate_plugin_manifest.py
	$(PYTHON) tests/validate_frontmatter.py
	$(PYTHON) tests/validate_agent_adapters.py
	$(PYTHON) tests/check_sync.py
	$(PYTHON) tests/check_version_sync.py

golden:
	$(PYTHON) tests/run_golden.py

example-test:
	cd examples/01-vip-media-bot && pytest tests/ -v

lint:
	@command -v markdownlint-cli2 >/dev/null 2>&1 && markdownlint-cli2 "**/*.md" --config .markdownlint.yaml || echo "install markdownlint-cli2 for lint"

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .mypy_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .ruff_cache -exec rm -rf {} + 2>/dev/null || true
