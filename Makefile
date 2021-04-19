install:
	poetry install

lint:
	poetry run flake8 ./demo
	poetry run mypy ./demo

up:
	poetry run jupyter notebook

