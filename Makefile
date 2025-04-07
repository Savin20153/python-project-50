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
	uv run ruff check gendiff

lint-fix:
	uv run ruff check gendiff --fix