.PHONY: lint test citations

lint:
	poetry run ruff check .
	poetry run black --check .
	poetry run mypy .

test:
	poetry run pytest --cov=.

citations:
	@echo "No citations step implemented yet"
