.PHONY: install format lint static test test-cov clean help

help:
	@echo "Available commands:"
	@echo "  make install    - Install dependencies with uv"
	@echo "  make format     - Format code with Black"
	@echo "  make format-check - Check code formatting without changes"
	@echo "  make lint       - Lint code with Ruff"
	@echo "  make static     - Run static type checking with MyPy"
	@echo "  make test       - Run tests with pytest"
	@echo "  make test-cov   - Run tests with coverage report"
	@echo "  make quality    - Run all quality checks (format-check, lint, static)"
	@echo "  make all        - Run quality checks and tests"
	@echo "  make clean      - Remove cache and temporary files"

install:
	uv sync --all-extras

format:
	uv run black .

format-check:
	uv run black --check .

lint:
	uv run ruff check .

lint-fix:
	uv run ruff check --fix .

static:
	uv run mypy .

test:
	uv run pytest

test-cov:
	uv run pytest --cov=app --cov-report=term-missing --cov-report=html

quality: format-check lint static

all: quality test

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	find . -type d -name "htmlcov" -exec rm -rf {} +
	find . -type f -name ".coverage" -delete
	find . -type f -name "*.pyc" -delete
