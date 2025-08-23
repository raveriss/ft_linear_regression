# AGENTS.md — Blueprint de Développement, Qualité, Checklist & Loi de Murphy (ft_linear_regression)

**Contexte cible** : Ubuntu 22.04.5 (Jammy), Python 3.10.18, **pas de sudo**, **Poetry**, exécution **uniquement sur Ubuntu**.

Ce document sert de **plan d’action exécutable** pour implémenter `ft_linear_regression` à la 42, avec une posture **défense‑proof** : TDD systématique, couverture **100 %** (statements **et** branches), **diff=100 %**, contrôle **par fichier**, CI Ubuntu‑only. Les bonus CI perso sont isolés.

---

## 0) 🏗️ Fondations techniques & outillage

### 0.1 Git & hygiène de repo
- [ ] Init repo + `README.md` (usage, séquence de soutenance, badges CI si voulu)
- [ ] `LICENSE` (MIT) + `author`
- [ ] `.gitignore` : `theta.json`, `htmlcov/`, `.coverage*`, `.pytest_cache/`, `__pycache__/`, `*.pyc`
- [ ] Convention commits : `feat:`, `fix:`, `refactor:`, `test:`, `docs:`

### 0.2 Environnement & dépendances (Poetry, no‑sudo)
- [ ] Installer Poetry (utilisateur) :
  ```bash
  curl -sSL https://install.python-poetry.org | python3 -
  export PATH="$HOME/.local/bin:$PATH"
  poetry config virtualenvs.in-project true
  poetry env use 3.10
  ```
- [ ] `pyproject.toml` — **versions Python verrouillées** :
  ```toml
  [tool.poetry]
  name = "ft-linear-regression"
  version = "0.1.0"
  description = "42 ft_linear_regression (Ubuntu-only, Poetry)"
  authors = ["raveriss <you@example.com>"]

  [tool.poetry.dependencies]
  python = ">=3.10,<3.11"

  [tool.poetry.group.dev.dependencies]
  pytest = "^8.3"
  pytest-cov = "^5.0"
  pytest-timeout = "^2.3"
  pytest-randomly = "^3.15"
  mypy = "^1.10"
  ruff = "^0.5"
  mutmut = "^3.0"

  [tool.poetry.group.viz]
  optional = true
  [tool.poetry.group.viz.dependencies]
  matplotlib = "^3.9"

  [tool.ruff]
  line-length = 88
  [tool.ruff.lint]
  select = ["E","F","W","I"]
  [tool.ruff.format]
  quote-style = "double"
  ```
- [ ] **Fallback 42 (sans Poetry)** : générer un `requirements.txt` pour exécuter sur une machine sans Poetry
  ```bash
  poetry export -f requirements.txt -o requirements.txt --without-hashes
  python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt
  ```

### 0.2bis Exécution sans Poetry (fallback “défense 42”)
- Objectif : garantir que le correcteur puisse lancer le projet sans Poetry.
- Procédure locale (sans sudo) :
```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
# Lancement direct (module ou fichier)
python3 -m src.train --data data.csv --alpha 1e-7 --iters 100000 --theta theta.json
python3 -m src.predict --km 85000 --theta theta.json
# ou
python3 src/train/train.py --data data.csv --alpha 1e-7 --iters 100000 --theta theta.json
python3 src/predict/predict.py --km 85000 --theta theta.json

```
### 0.3 Makefile (raccourcis non intrusifs)
```Makefile
.PHONY: install lint format type test cov mut run-train run-predict reqs install-venv run-train-nopoetry run-predict-nopoetry mut
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
	poetry run mutmut run --simple-output
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
	
mut:
	poetry run mutmut run --paths-to-mutate src --tests-dir tests --runner "pytest -q" --use-coverage --simple-output

```

### 0.4 CI/CD (GitHub Actions) — **Ubuntu‑only**
`.github/workflows/ci.yml`
```yaml
name: ci
on:
  push:
  pull_request:
jobs:
  tests:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.10' }
      - name: Install Poetry
        run: curl -sSL https://install.python-poetry.org | python3 -
      - name: Configure Poetry
        run: |
          echo "$HOME/.local/bin" >> $GITHUB_PATH
          poetry config virtualenvs.in-project true
          poetry install --no-root --with dev
      - name: Lint & type
        run: |
          poetry run ruff check .
          poetry run mypy src
      - name: Tests & coverage (100 % global, diff 100 %)
        run: |
          poetry run coverage run -m pytest -q
          poetry run coverage json -o coverage.json
          poetry run coverage xml -o coverage.xml
          poetry run coverage report --fail-under=100
      - name: Enforce per-file 100 %
        run: |
          python - << 'PY'
import json,sys
j=json.load(open('coverage.json'))
miss=[f for f in j['files'].values() if f['summary']['percent_covered']<100]
if miss:
    print('Files below 100%:', [k for k,v in j['files'].items() if v in miss])
    sys.exit(1)
PY
      - name: Upload coverage HTML (artifact)
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: htmlcov
          path: htmlcov/

  smoke-no-poetry:
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: { python-version: '3.10' }
      - name: Install with pip (no Poetry)
        run: |
          python -m venv .venv
          . .venv/bin/activate
          pip install -r requirements.txt
      - name: Smoke run train & predict (no Poetry)
        run: |
          . .venv/bin/activate
          python -m src.train --data data.csv --alpha 1e-7 --iters 10 --theta theta.json
          python -m src.predict --km 85000 --theta theta.json

```

### 0.5 TDD — Red → Green → Refactor (règle d’or)
- **Definition of Ready** : pas de code sans **au moins un test qui échoue**.
- **Definition of Done** : tests verts, **100 %** couverture (branches), CLI/doc à jour.
- **Hooks (local)** :
  - `pre-commit` : `ruff format --check`, `ruff check`, `mypy` (rapide)

---

## 1) 🧩 Architecture minimale (agents)
- **`src/train/train.py`** : entraînement par **descente de gradient** ; MAJ **simultanée** de `θ0, θ1` via temporaires ; sauvegarde `theta.json`.
- **`src/predict/predict.py`** : prédiction **interactive par défaut**. Si `--km` absent → **prompt** utilisateur. Charge `theta.json`.
- **`src/io_utils.py`** : lecture CSV robuste (colonnes `km`,`price`), validation/parse.
- **`tests/`** : unitaires + E2E + erreurs I/O + contrats.
- **Bonus isolé** : `src/viz.py` (groupe Poetry `viz`) — **évalué uniquement si mandatory parfait**.

> **Main guard requis** partout : `if __name__ == "__main__": main()` et exécution via `python3 -m src.train` / `python3 -m src.predict`.

---

## 2) 📜 Exigences 42 — conformité stricte
- [ ] **Deux programmes distincts** : `train.py`, `predict.py`.
- [ ] Hypothèse **exacte** : `estimatePrice(x) = θ0 + θ1 * x`.
- [ ] **Initialisation** : `θ0 = 0`, `θ1 = 0`.
- [ ] **Mise à jour simultanée** : calculer `tmpθ0`, `tmpθ1` à partir des `θ` **courants**, puis assigner `θ ← θ − tmpθ` en **fin** d’itération.
- [ ] **Avant entraînement** : prédire **0** pour tout `km`.
- [ ] **Pas de lib magique** : **interdit** `numpy.polyfit`, `sklearn.LinearRegression`.
- [ ] **Persistance** : `theta.json` UTF‑8 (`{"theta0":..., "theta1":...}`) ; messages + codes retour ≠0 si manquant/corrompu.
- [ ] **CLI** : options `--alpha`, `--iters`, `--theta` ; **pas de magic numbers** en dur.
- [ ] **Predict interactif par défaut** : prompt si `--km` non fourni.
- [ ] **Prédiction avant entraînement = 0** : tant que theta.json n’a pas été entraîné/écrit, predict doit renvoyer 0 pour tout kilométrage (hypothèse avec θ0=0, θ1=0). Testable en défense.
**Scénario E2E “défense” (à garder en sous‑puces) :**
- [ ] Étape A : supprimer theta.json ; exécuter python -m src.predict --km 12345 → 0.
- [ ] Étape B : entraîner (python -m src.train --data data.csv --alpha 1e-7 --iters 100000 --theta theta.json).
- [ ] Étape C : relancer predict avec le même km → prix non nul, cohérent avec la droite apprise.

---

## 3) 🧪 Plan de tests (défense‑proof)
**Objectifs** : 100 % couverture (branches + diff), **contrôle par fichier**, tests rapides.

### 3.1 Unitaires
- `estimatePrice`, gradients, MAJ **simultanée** (test dédié qui échoue si l’ordre est séquentiel)
- I/O : CSV manquant, colonnes inattendues, valeurs non numériques (`"12 300"`, `"6,3"`, `NaN`)
- JSON `theta` : absent/corrompu/droits → message clair + **exit ≠ 0**
- Tolérances float (`rtol/atol`), **jamais** `==` sur floats

### 3.2 E2E
- `predict(0)=0` → `train` → `predict(km_csv) ≈ price`
- CLI `--help` (exit 0), erreurs d’options (exit ≠ 0, message)
- **Entrée interactive** : prompt si `--km` manquant, gestion EOF/pipe

### 3.3 Couverture (outil `coverage`)
- `.coveragerc` implicite via commandes : `branch=True`, `--skip-empty`, `--show-contexts`
- Générer `coverage.json` → script CI vérifie **100 % par fichier**
- **Diff=100 %** (chaque patch couvert)
- CI verrouillée sur **Ubuntu 22.04 uniquement** (pas de Windows/macOS)
- Upload vers **Codecov** (`coverage.xml`) → badge obligatoire pour mandatory

### 3.4 Mutation (CI perso)
- Outil : `mutmut` avec **scope global** sur tout le code **mandatory** (`src/`), pas seulement l’algorithme.
- Commande de référence :
  `mutmut run --paths-to-mutate src --tests-dir tests --runner "pytest -q" --use-coverage --simple-output`
- Objectif : **≥ 90 % de mutants tués** sur l’ensemble du code mandatory.
- Exclusions permises (documentées) : bonus (`src/viz.py`) et tout point d’entrée `__main__` pure glue non testable.
- Tout mutant survivant sur les zones **critiques** (formules, MAJ simultanée, I/O de `theta.json`, gestion d’erreurs CLI) = **échec** jusqu’à ajout de tests.
- CI : publier le rapport des survivants en artefact et lister les justifications résiduelles.

### 3.5 Tolérances numériques (si tests internes)
- Ne jamais comparer des floats avec `==`.
- Si vous écrivez des tests E2E, utilisez `pytest.approx(..., rel=1e-2)`.

## 4) ⚙️ Spécifications d’implémentation

### 4.1 Formules
- `estimatePrice(x) = θ0 + θ1 * x`
- Gradients (m = nb échantillons)
  - `dθ0 = (1/m) * Σ( (θ0 + θ1*x_i) - y_i )`
  - `dθ1 = (1/m) * Σ( ((θ0 + θ1*x_i) - y_i) * x_i )`
- Mise à jour **simultanée** :
  - `tmpθ0 = α * dθ0`, `tmpθ1 = α * dθ1`
  - `θ0 ← θ0 − tmpθ0`, `θ1 ← θ1 − tmpθ1`

### 4.2 CLI (exemples)
```bash
python3 -m src.train --data data.csv --alpha 1e-7 --iters 100000 --theta theta.json
python3 -m src.predict --km 85000 --theta theta.json
# sans --km → prompt interactif
```

### 4.3 Persistance
- Fichier `theta.json` à la racine du projet (ou chemin passé via `--theta`)
- Format stable :
  ```json
  {"theta0": 0.0, "theta1": 0.0}
  ```
- **Ne jamais** committer `theta.json` (listé dans `.gitignore`)

### 4.4 Structure projet
```
.
├── data.csv
├── pyproject.toml
├── README.md
├── Makefile
├── requirements.txt        # généré (fallback)
├── src/
│   ├── __init__.py
│   ├── predict/
│   │   ├── __init__.py
│   │   └── predict.py
│   ├── train/
│   │   ├── __init__.py
│   │   └── train.py
│   ├── __init__.py
│   ├── io_utils.py
│   └── viz.py              # bonus (groupe poetry [viz])
└── tests/
    ├── test_train.py
    ├── test_predict.py
    ├── test_io.py
    └── test_cli.py
```

---

## 5) 🛡️ Loi de Murphy — risques & contre‑mesures (condensé)
- **CSV** absent/mal formé/UTF‑8/CRLF → parse robuste + messages clairs + exit ≠ 0
- **Entrées** non numériques/virgule décimale/vides → validation + prompts
- **α** trop grand/petit → tests qui détectent divergence/lenteur (borne α)
- **MAJ non simultanée** → test dédié qui échoue si l’ordre est faux
- **θ** absent/corrompu/droits → tests I/O + codes retour
- **Extrapolation** hors plage → message d’avertissement (bonus UX)
- **Normalisation** → **hors mandatory** (si faite en bonus, **dénormaliser** à la prédiction)

---

## 6) ✅ Procédure de validation finale (soutenance)
1. `pytest -q` → **tout vert**
2. `coverage run -m pytest && coverage json && coverage report --fail-under=100` (branches)
3. **Contrôle par fichier** : script CI sur `coverage.json` → **100 % partout**
3bis. **Upload vers Codecov** (`coverage.xml`) + vérif diff=100 %
4. **Mutation testing (scope global mandatory) ≥ 90 %** + aucun survivant sur les zones critiques.
5. Démo E2E : `predict(0)=0` → `train` → `predict≈csv` (MAJ simultanée validée)
6. Vérif visuelle `htmlcov/` (tout vert)
7. README : commande `predict→train→predict`, aucune mention de lib “magique”
8. Vérif environnement : exécution validée uniquement sous **Ubuntu 22.04** (soutenance école 42)


---

## 7) 📎 Annexes — extraits utiles

### 7.1 Bloc d’aide minimal (à snapshot en test)
```
usage: train.py --data DATA --alpha ALPHA --iters ITERS [--theta PATH]
usage: predict.py [--km KM] [--theta PATH]
```

### 7.2 Modèle de messages d’erreurs (tests de régression)
- `ERROR: theta file not found: <path>` (exit 2)
- `ERROR: invalid CSV format (expected columns: km,price)` (exit 2)
- `ERROR: invalid mileage (must be a non-negative number)` (exit 2)

---

## 8) 🔭 Bonus CI perso (hors soutenance 42)
- `vulture`, `bandit`, `radon/xenon` (analyse dead‑code/sécurité/complexité)
- Job Python 3.11 Ubuntu (smoke) en plus du 3.10

---

## 9) Pourquoi cette version ?
- **Alignée 42** : Ubuntu‑only, Python 3.10, no‑sudo, 2 programmes, MAJ simultanée, prédiction=0 avant train
- **Efficace** : CI courte, messages d’erreurs testés, contrôle par fichier
- **Évolutive** : bonus CI perso **isolés** ; viz en groupe Poetry optionnel
- **Lisible** : checklists concises, extraits directement copiables

