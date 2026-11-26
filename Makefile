.PHONY: install check lint test test-coverage

install:
	uv sync

check:
	uv check

lint:
	uv run ruff check .

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=term-missing
