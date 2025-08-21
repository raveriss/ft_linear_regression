# Work Breakdown Structure (WBS) — ft_linear_regression

## 0) Initialisation projet
- **0.1 Repo & fichiers de base**
  - [ ] Init Git repo, ajouter `README.md`, `LICENSE`, `.gitignore`
  - [ ] Convention de commits (`feat:`, `fix:`, `test:`)
- **0.2 Environnement**
  - [ ] Installer Poetry (`python3.10`, no-sudo)
  - [ ] Créer `pyproject.toml` (dépendances : pytest, mypy, ruff, mutmut, matplotlib en bonus)
  - [ ] Export fallback `requirements.txt` (venv)
- **0.3 CI/CD**
  - [ ] Créer workflow GitHub Actions (Ubuntu 22.04, Python 3.10)
  - [ ] Étapes : lint, type, tests, coverage=100 % par fichier, Codecov, mutmut
- **0.4 Makefile**
  - [ ] Cibles : `install`, `lint`, `type`, `test`, `cov`, `mut`, `run-train`, `run-predict`
- **0.5 Données**
  - [ ] Ajouter `data.csv` (24 lignes `km,price`)
  - [ ] Vérifier parsing correct UTF-8, LF, colonnes exactes

---

## 1) Implémentation obligatoire (mandatory)

### 1.1 Hypothèse de prédiction
- **Red** : écrire un test unitaire échouant pour `estimatePrice(x)` attendu.
- **Green** : implémenter `estimatePrice(x) = θ0 + θ1 * x`.
- **Refactor** : ajouter docstring, typing, tests `pytest.approx`.

### 1.2 Programme `predict.py`
- [ ] Gestion CLI (`--km`, `--theta`) + prompt interactif si absent
- [ ] Avant entraînement → retourne toujours 0
- [ ] Chargement `theta.json` robuste (fichier manquant, corrompu, droits)  
  - **Red** : test E2E échouant si fichier absent
  - **Green** : gestion erreur avec message `ERROR: theta file not found`
  - **Refactor** : codes retour (0 nominal, 2 entrée invalide)

### 1.3 Programme `train.py`
- [ ] Lire `data.csv` (parse robuste : int, float, NaN, valeurs invalides)
- [ ] Implémenter descente de gradient :
  - Formules exactes (tmpθ0, tmpθ1)
  - MAJ **simultanée** (test dédié échouant si MAJ séquentielle)
  - Sauvegarde `theta.json`
- [ ] Paramètres CLI : `--alpha`, `--iters`, `--theta`
- [ ] Gestion erreurs I/O CSV + message clair

---

## 2) Tests (défense-proof)

### 2.1 Unitaires
- [ ] `estimatePrice` avec plusieurs km
- [ ] Gradient descent (valeurs connues → θ attendus ~ OLS)
- [ ] CSV parser (bon/mauvais format)
- [ ] JSON θ (absent/corrompu)
- [ ] CLI erreurs (mauvais arguments)

### 2.2 E2E (procédure soutenance)
- **Étape A** : predict avant entraînement → 0  
- **Étape B** : train → produit `theta.json`  
- **Étape C** : predict après entraînement → prix ≈ CSV  
- Vérification snapshot messages + codes retour

### 2.3 Couverture
- [ ] Activer branch coverage
- [ ] Générer `coverage.json`, `coverage.xml`
- [ ] Script CI échoue si fichier <100 %

### 2.4 Mutation testing
- [ ] Lancer `mutmut` sur `src/`
- [ ] Objectif ≥ 90 % mutants tués
- [ ] Survivants documentés (uniquement glue `__main__`/bonus)

---

## 3) Qualité du code
- [ ] Formatage (`ruff format`, `isort`)
- [ ] Lint (`ruff check`)
- [ ] Typage (`mypy`)
- [ ] Dead code (`vulture`)
- [ ] Pre-commit hooks

---

## 4) Bonus (seulement si mandatory parfait)
- [ ] `viz.py` : afficher `data.csv` + droite de régression
- [ ] Programme `accuracy.py` (métrique RMSE, R²)
- [ ] Tests bonus isolés (non intrusifs)

---

## 5) Loi de Murphy – garde-fous
- [ ] CSV absent, colonnes mal nommées → message clair, exit ≠0
- [ ] Entrée non numérique ou km <0 → erreur
- [ ] α trop grand/petit → borne + avertissement
- [ ] θ absent/corrompu → tests I/O robustes
- [ ] Prédiction hors plage → warning (bonus)
- [ ] Aucun crash, aucun segfault → sinon note = 0

---

## 6) Soutenance – Checklist finale
1. `pytest -q` → tout vert
2. `coverage report --fail-under=100` → OK par fichier
3. `mutmut run` ≥ 90 % mutants tués
4. Démo E2E A/B/C
5. Vérif visuelle `htmlcov/`
6. README → aucune mention de lib magique, procédure claire
7. CI GitHub verte (Ubuntu-only)
