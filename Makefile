# ========================================================================================
# Makefile - Automatisation pour le projet ft_linear_regression
# Objectifs :
#   - Simplifier l’installation et la gestion de l’environnement (Poetry / venv)
#   - Automatiser les vérifications (lint, format, type-check, tests, coverage, mutation)
#   - Fournir des commandes pratiques pour l’entraînement et la prédiction du modèle
# ========================================================================================

.PHONY: install lint format type test cov mut train predict-nocheck viz tv-bench-all tv-bench-% activate deactivate

VENV = .venv
VENV_BIN = $(VENV)/bin/activate

# --- Benchmarks ---------------------------------------------------------------
BENCH_DIR   := data/benchmarks
BENCH_CSVS  := $(wildcard $(BENCH_DIR)/*.csv)

# Utilisation raccourcie de Poetry
POETRY = poetry run

# Paramètres par défaut (surchargables : make train DATA=... THETA=... ALPHA=... ITERS=...)
DATA  ?= data/samples/data.csv
THETA ?= theta.json
ALPHA ?= 0.1
ITERS ?= 1000

# ----------------------------------------------------------------------------------------
# Installation des dépendances (dev inclus)
# ----------------------------------------------------------------------------------------
install:
	poetry install --with dev

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
	$(POETRY) pytest -vv

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
train:
	$(POETRY) train --data $(DATA) --alpha $(ALPHA) --iters $(ITERS) --theta $(THETA)

# Prédiction du prix pour une valeur donnée (km)
predict-nocheck:
	@$(POETRY) predict --theta $(THETA) $(filter-out $@,$(MAKECMDGOALS)) || true

# Visualisation des données + droite (theta0 + theta1 * x)
viz:
	$(POETRY) python -m src.viz --data $(DATA) --theta $(THETA) --show-residuals --confidence --show-eq --show-median

# Tous les CSV de benchmarks : train + viz pour chacun
tv-bench-all:
	@set -e; \
	for f in $(BENCH_CSVS); do \
		b=$$(basename "$$f" .csv); \
		theta="theta_$${b}.json"; \
		echo "==> $$b"; \
		$(POETRY) train --data "$$f" --alpha $(ALPHA) --iters $(ITERS) --theta "$$theta"; \
		$(POETRY) python -m src.viz --data "$$f" --theta "$$theta" --show-residuals --confidence; \
	done

# Un dataset précis par nom de fichier sans extension
tv-bench-%:
	@set -e; \
	f="$(BENCH_DIR)/$*.csv"; \
	test -f "$$f" || { echo "absent: $$f"; exit 1; }; \
	theta="theta_$*.json"; \
	echo "==> $*"; \
	$(POETRY) train --data "$$f" --alpha $(ALPHA) --iters $(ITERS) --theta "$$theta"; \
	$(POETRY) python -m src.viz --data "$$f" --theta "$$theta" --show-residuals --confidence

# Affiche la commande pour activer le venv
activate:
	@echo "Chemin de l'environnement Poetry :"
	@poetry env info -p
	@echo
	@echo "Pour activer manuellement cet environnement :"
	@echo "  source $$(poetry env info -p)/bin/activate"

# Affiche la commande pour désactiver le venv
deactivate:
	@echo "Pour quitter l'environnement :"
	@echo "  deactivate"

# ----------------------------------------------------------------------------------------
# Règle générique pour ignorer les cibles numériques (ex. make predict-nocheck 23000)
# ----------------------------------------------------------------------------------------
%:
	@:
