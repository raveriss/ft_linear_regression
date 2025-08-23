.PHONY: install lint format type test cov mut run-train run-predict reqs install-venv run-train-nopoetry run-predict-nopoetry

install:
	poetry install --with dev

reqs:
	poetry export -f requirements.txt -o requirements.txt --without-hashes

lint:
	poetry run ruff check .

format:
	poetry run ruff format . && poetry run ruff check --fix .

type:
	poetry run mypy src

test:
	poetry run pytest -q

cov:
	poetry run coverage run -m pytest && \
	poetry run coverage json -o coverage.json && \
	poetry run coverage html --skip-empty --show-contexts && \
	poetry run coverage report --fail-under=100

mut:
	poetry run mutmut run --paths-to-mutate src --tests-dir tests --runner "pytest -q" --use-coverage --simple-output

run-train:
	poetry run python3 -m src.train --data data.csv --alpha 1e-7 --iters 100000

run-predict:
	poetry run python3 -m src.predict --km 85000

install-venv:
	python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

run-train-nopoetry:
	. .venv/bin/activate && python3 -m src.train --data data.csv --alpha 1e-7 --iters 100000 --theta theta.json

run-predict-nopoetry:
	. .venv/bin/activate && python3 -m src.predict --km 85000 --theta theta.json
