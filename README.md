# ft_linear_regression 

<div align="center">

![License](https://img.shields.io/github/license/raveriss/ft_linear_regression)
![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)
[![CI](https://github.com/raveriss/ft_linear_regression/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/raveriss/ft_linear_regression/actions)
[![Coverage](https://codecov.io/gh/raveriss/ft_linear_regression/branch/main/graph/badge.svg)](https://codecov.io/gh/raveriss/ft_linear_regression)
[![Lint](https://img.shields.io/badge/lint-ruff%20✔-yellow.svg)]()
[![Typing](https://img.shields.io/badge/mypy-checked-purple.svg)]()
[![Mutation](https://img.shields.io/badge/mutmut-≥90%25-orange.svg)]() 
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?label=pre--commit)]()

</div>

---

## 🚀 Objectif du projet
Implémenter **un premier algorithme de Machine Learning** : une **régression linéaire simple**.  

👉 Prédire le **prix d’une voiture** en fonction de son kilométrage via :  
```math
estimatePrice(x) = θ₀ + θ₁ * x
```

- **Deux programmes obligatoires** :  
  - `train.py` → entraîne le modèle (descente de gradient, mise à jour simultanée de θ).  
  - `predict.py` → prédit un prix à partir d’un kilométrage (0 avant entraînement).  

🎯 Conformité stricte à l’énoncé 42 :  
- Pas de `numpy.polyfit` / `sklearn.LinearRegression`.  
- θ sauvegardés entre runs dans `theta.json`.  
- Prédiction = **0 avant tout entraînement**.  
- Pas de crash en soutenance.

---

## 🧰 Stack technologique
- **Python** : 3.10.18 (Ubuntu 22.04.5 Jammy)  
- **Gestion dépendances** : [Poetry](https://python-poetry.org/)  
- **Qualité / CI** : `pytest`, `coverage`, `ruff`, `mypy`, `mutmut` (mutation testing)  
- Visualisation (**bonus uniquement**) : matplotlib (installé **sur demande** via `poetry install --with viz`)


---

## ⚡ Démarrage rapide

> En cas d’entrée invalide (ex. `--km` négatif ou non numérique) : le programme écrit un message `ERROR: ...` sur **stderr** et quitte avec **exit 2**.


### 🔧 Installation
```bash
# Avec Poetry (recommandé)
poetry install --with dev

# Fallback soutenance 42 (sans Poetry)
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

> ℹ️ Bonus non installé par défaut  
> Pour activer **uniquement** la visualisation bonus :  
> `poetry install --with viz --with dev`


### ▶️ Lancement
```bash
# Entraînement
poetry run train --data data.csv --alpha 0.1 --iters 1000 --theta theta.json

# Prédiction
poetry run predict --km 85000 --theta theta.json
```

> ℹ️ Si la droite rouge affichée par `viz` reste quasiment horizontale, vérifiez
> le contenu de `theta.json`. Une valeur de `--alpha` trop faible (par exemple
> `1e-7`) laisse les coefficients proches de zéro. Utilisez `--alpha 0.1` (ou
> `0.01`) et suffisamment d'itérations pour obtenir une pente négative réaliste.

## 🧪 Procédure de soutenance (E2E “défense-proof”)

Scénario officiel à démontrer en soutenance, en trois étapes **obligatoires** :

**Étape A :** prédiction avant tout entraînement  
Suppression du fichier de paramètres
```bash
rm -f theta.json
python3 -m src.predict --km 50000 --theta theta.json
```
→ Résultat attendu : 0 (θ₀=0, θ₁=0 par défaut)

**Étape B :** entraînement du modèle

```bash
poetry run train --data data.csv --alpha 0.1 --iters 1000 --theta theta.json
```
→ Apprentissage des paramètres θ₀ et θ₁, sauvegardés dans theta.json

**Étape C :** prédiction après entraînement
→ Résultat attendu : prix non nul, cohérent avec la droite apprise (≈ CSV)
```bash
python3 -m src.predict --km 50000 --theta theta.json
```
⚠️ Ces trois étapes doivent être **reproductibles à l’identique** devant le jury.
Tout écart (crash, valeur incohérente, absence de 0 en étape A, MAJ non simultanée de θ) = **échec en défense.**

### (Bonus) Visualisation
> Évaluable **uniquement si le mandatory est parfait**. Non requis pour la soutenance.
### Si vous avez installé le groupe bonus viz :
```bash
poetry run python -m src.viz --data data.csv --theta theta.json
```
<p align="center">
  <img src="docs/assets/readme/price-vs-km-regression.svg" alt="Régression linéaire (price vs km)" width="760">
  <br><em>Nuage de points et droite θ₀ + θ₁·x (après entraînement).</em>
</p>

---

## 📦 Utilisation
- **Mode interactif** : `predict.py` demande un kilométrage si non fourni.  
- **End-to-End** : `predict (0)` → `train` → `predict ≈ prix`.  

---

## 📝 Données
- Fichier : [`data.csv`](./data.csv) (colonnes `km,price`).  
- Hypothèses :  
  - km ≥ 0  
  - valeurs numériques uniquement  
  - 24 lignes d’exemple (corrélation ≈ −0,86)  

---

## 🧠 Architecture
```
.
├── data.csv
├── pyproject.toml
├── requirements.txt
├── src/
│   ├── train.py      # descente de gradient (MAJ simultanée θ)
│   ├── predict.py    # prédiction (0 avant train)
│   ├── io_utils.py   # lecture CSV robuste
│   └── viz.py        # (BONUS uniquement) visualisation – non installé par défaut
└── tests/            # unitaires + E2E + erreurs I/O
```

*(Bonus : `viz.py` affiche données + droite de régression)*
*Les tests E2E vérifient aussi les **messages d’erreurs exacts** (snapshot) et les **codes de sortie** (0/1/2).*

---

## 🛠️ Fichiers de configuration
- `pyproject.toml` (Poetry, dépendances, lint, type check)  
- `requirements.txt` (fallback sans Poetry)  
- `.coveragerc`, `.gitignore`, `Makefile` (raccourcis CI/CD)  
- **Note** : `theta.json` est listé dans `.gitignore` → *ne jamais le versionner*.  
- `pyproject.toml` contient un **groupe Poetry optionnel** `[tool.poetry.group.viz]`.  
  Ce groupe **n’est pas installé** par défaut : il est réservé au **bonus**.


---

## 🧪 Tests
- Portée des tests (mandatory) : `train.py`, `predict.py`, `io_utils.py`, CLI, I/O θ, stratégie GD.  
- `viz.py` est **hors** mandatory et **hors périmètre** des exigences minimales (peut être testé si le bonus est activé).

### Unitaire
- Comparaisons float avec `pytest.approx` uniquement (`rtol=1e-2`), jamais `==`.  
- Test dédié qui échoue si la mise à jour des θ n’est pas **simultanée** (utilisation de temporaires).  
- Tests robustesse I/O : CSV manquant, colonnes inattendues, valeurs non numériques, JSON `theta` absent/corrompu.  
- Vérification des **messages d’erreurs et codes retour** (exemples attendus) :  
  - `ERROR: invalid CSV format (expected columns: km,price)` → exit 2  
  - `ERROR: invalid mileage (must be a non-negative number)` → exit 2  
  - `ERROR: theta file not found: <path>` → exit 2  

### End-to-End
- `predict(0)=0` → `train` → `predict(km_csv) ≈ price`.  
- CLI `--help` (exit 0), erreurs d’options (exit ≠ 0, message).  
- Entrée interactive : prompt si `--km` manquant, gestion EOF/pipe.

### Couverture stricte (100 % global + diff + contrôle par fichier)
```bash
pytest -q
coverage run -m pytest
coverage json
coverage report --fail-under=100
coverage html --skip-empty --show-contexts
```

## 🧾 Codes de sortie & messages d’erreur (contrat “défense‑proof”)

Les programmes doivent **imprimer ces messages à l’identique sur stderr** et quitter avec le **code indiqué**.

- `ERROR: theta file not found: <path>` → **exit 2**
- `ERROR: invalid CSV format (expected columns: km,price)` → **exit 2**
- `ERROR: invalid mileage (must be a non-negative number)` → **exit 2**

Règles générales :
- **0** : exécution nominale (train/predict OK).
- **2** : erreur d’usage/entrée/I‑O/validation (fichier manquant, CSV invalide, saisie invalide, etc.).
- **1** : erreur interne inattendue (exception non prévue).

Tests recommandés :
- Snapshot minimal des messages d’aide (`--help`) et d’erreur (texte essentiel, stable).
- Asserts explicites sur `returncode` (0, 1 ou 2 selon les cas).

✅ **Objectifs qualité (mandatory)** :  
- Coverage **100 %** (statements + branches + diff + contrôle fichier).  
- Mutation testing **≥90 %** (scope global mandatory, avec survivants justifiés).  
- **Tolérance floats stricte** : toujours utiliser `pytest.approx(..., rel=1e-2)` (jamais `==` sur floats).  
- **Test dédié “MAJ simultanée”** : un test échoue explicitement si θ₀, θ₁ sont mis à jour séquentiellement (sans temporaires).  
- Tests E2E : `predict(0)=0 → train → predict≈csv`.  
- Tests robustesse I/O : CSV manquant, mal formé, km négatif, NaN, EOF/pipe.  
- Tests CLI : `--help`, erreurs d’options → exit ≠ 0 avec message clair.  
- Codes retour : 0 succès, ≠0 échec.  

---

## 🔍 Qualité du code
- Formatage & imports : `ruff format`, `isort`.  
- Typage statique : `mypy`.  
- Lint : `ruff check`.  
- CI/CD Ubuntu-only (GitHub Actions).  
- Hooks `pre-commit` pour vérifier format/lint/tests rapides avant commit.  

## 📚 Documentation liée
- [`AGENTS.md`](./AGENTS.md) → Blueprint complet CI/CD + checklist défense-proof.  
- [`ft_linear_regression_checklist_défense-proof.txt`](./ft_linear_regression_checklist_défense-proof.txt) → Qualité tests & couverture.  
- [`ft_linear_regression_murphy_law.txt`](./ft_linear_regression_murphy_law.txt) → Risques & contre-mesures.  
- Énoncé officiel : [ft_linear_regression.en.subject.pdf](./ft_linear_regression.en.subject.pdf).  
- Le bonus est **cloisonné** : il ne doit pas interférer avec le mandatory ni impacter la CI de base.

---

## 🛡️ Licence
MIT © 2025 — raveriss  
