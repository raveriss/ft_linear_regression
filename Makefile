# ========================================================================================
# Makefile - Automatisation pour le projet ft_linear_regression
# Objectifs :
#   - Simplifier l’installation et la gestion de l’environnement (Poetry / venv)
#   - Automatiser les vérifications (lint, format, type-check, tests, coverage, mutation)
#   - Fournir des commandes pratiques pour l’entraînement et la prédiction du modèle
# ========================================================================================

.PHONY: install lint format type test cov mut run-train run-predict reqs install-venv run-train-nopoetry run-predict-nopoetry

# Utilisation raccourcie de Poetry
POETRY = poetry run

# ----------------------------------------------------------------------------------------
# Installation des dépendances (dev inclus)
# ----------------------------------------------------------------------------------------
install:
	poetry install --with dev

# Export des dépendances en requirements.txt (utile pour venv ou déploiement hors Poetry)
reqs:
	poetry export -f requirements.txt -o requirements.txt --without-hashes

# ----------------------------------------------------------------------------------------
# Vérifications de qualité du code
# ----------------------------------------------------------------------------------------

# Linting avec Ruff (analyse statique rapide)
lint:
	$(POETRY) ruff check .

# Formatage + correction auto avec Ruff
format:
	$(POETRY) ruff format . && $(POETRY) ruff check --fix .

# Vérification des types avec Mypy
type:
	$(POETRY) mypy src

# ----------------------------------------------------------------------------------------
# Tests et couverture
# ----------------------------------------------------------------------------------------

# Exécution des tests unitaires
test:
	$(POETRY) pytest -q

# Analyse de la couverture avec rapport JSON, HTML et console (100% requis)
cov:
	$(POETRY) coverage run -m pytest && \
	$(POETRY) coverage json -o coverage.json && \
	$(POETRY) coverage html --skip-empty --show-contexts && \
	$(POETRY) coverage report --fail-under=100

# Mutation testing avec Mutmut (robustesse des tests)
mut:
	$(POETRY) mutmut run
	$(POETRY) mutmut results > mutmut-results.txt

# ----------------------------------------------------------------------------------------
# Commandes liées au modèle (Poetry)
# ----------------------------------------------------------------------------------------

# Entraînement du modèle : génère le fichier theta.json
run-train:
	$(POETRY) train --data data.csv --alpha 0.1 --iters 1000 --theta theta.json

# Prédiction du prix pour une valeur donnée (km)
run-predict:
	$(POETRY) predict --km 85000 --theta theta.json

# ----------------------------------------------------------------------------------------
# Version sans Poetry (utilise un venv manuel)
# ----------------------------------------------------------------------------------------

# Création d’un venv Python classique et installation des dépendances
install-venv:
	python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

# Entraînement via venv (sans Poetry)
run-train-nopoetry:
	. .venv/bin/activate && python3 -m src.train --data data.csv --alpha 0.1 --iters 1000 --theta theta.json

# Prédiction via venv (sans Poetry)
run-predict-nopoetry:
	. .venv/bin/activate && python3 -m src.predict --km 85000 --theta theta.json
