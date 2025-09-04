# ========================================================================================
# Makefile - Automatisation pour le projet ft_linear_regression
# Objectifs :
#   - Simplifier l’installation et la gestion de l’environnement (Poetry / venv)
#   - Automatiser les vérifications (lint, format, type-check, tests, coverage, mutation)
#   - Fournir des commandes pratiques pour l’entraînement et la prédiction du modèle
# ========================================================================================

.PHONY: install lint format type test cov mut train predict-nocheck viz tv tv-all

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
train:
	$(POETRY) train --data $(DATA) --alpha $(ALPHA) --iters $(ITERS) --theta $(THETA)

# Prédiction du prix pour une valeur donnée (km)
predict-nocheck:
	@$(POETRY) predict --theta $(THETA) $(filter-out $@,$(MAKECMDGOALS)) || true

# Visualisation des données + droite (theta0 + theta1 * x)
viz:
	$(POETRY) python -m src.viz --data $(DATA) --theta $(THETA) --show-residuals --confidence

# Usage interactif par liste : make tv data.csv data_noise.csv ...
tv: $(addprefix tv-,$(filter-out $@,$(MAKECMDGOALS)))
	@:

# Règle unitaire : make tv-<fichier.csv>
tv-%:
	@$(MAKE) --no-print-directory train DATA=$* THETA=theta_$*.json
	@$(MAKE) --no-print-directory viz   DATA=$* THETA=theta_$*.json

# Tout ce qui matche data*.csv
tv-all:
	@for f in data*.csv; do \
	  b=$${f%.csv}; \
	  $(MAKE) --no-print-directory train DATA=$$f THETA=theta_$${b}.json; \
	  $(MAKE) --no-print-directory viz   DATA=$$f THETA=theta_$${b}.json; \
	done

# ----------------------------------------------------------------------------------------
# Règle générique pour ignorer les cibles numériques (ex. make predict-nocheck 23000)
# ----------------------------------------------------------------------------------------
%:
	@:
