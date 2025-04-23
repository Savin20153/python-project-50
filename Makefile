install:
	uv sync

build:
	uv build

package-install:
	uv tool install dist/*.whl

uninstall:
	uv tool uninstall hexlet-code

gendiff:
	uv run gendiff

lint:
    ruff check gendiff

lint-fix:
    ruff check gendiff --fix

test:
    pytest

check: lint test