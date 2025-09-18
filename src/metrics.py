"""Métriques d'évaluation pour la régression linéaire.

But:
    Fournir des fonctions pour charger les paramètres et calculer RMSE, R².
"""

# On active les annotations différées pour rester compatible avec Python < 3.11
# et limiter les dépendances croisées lors des imports
from __future__ import annotations

# On utilise JSON car c’est un format
# standard et interopérable pour stocker theta
import json

# On importe math pour bénéficier de sqrt et éviter
# d’implémenter nos propres racines carrées
import math

# On passe par Path pour garantir des opérations fichiers robustes
# et portables (multi-OS)
from pathlib import Path

# On réutilise la fonction de prédiction du modèle afin d’évaluer
# la cohérence entre entraînement et prédiction → pas de duplicata de logique
from linear_regression import estimate_price

# On charge la fonction de lecture des données pour assurer que
# l’évaluation se base sur exactement le même parsing que l’entraînement
from train.train import read_data


def read_theta(path: str | Path) -> tuple[float, float]:
    """Return ``(theta0, theta1)`` loaded from ``path``.

    But:
        Charger et valider les coefficients du modèle depuis un JSON.
    """

    # On force en Path pour fiabiliser les opérations disque
    theta_path = Path(path)
    try:
        # On tente de lire et désérialiser le JSON pour obtenir un dict Python
        # car c’est la structure la plus naturelle pour stocker les coefficients
        data = json.loads(theta_path.read_text())
    except (OSError, json.JSONDecodeError) as exc:  # pragma: no cover - simple
        # On renvoie une ValueError claire afin de signaler un problème
        # lié au fichier plutôt que de laisser fuiter des erreurs systèmes opaques
        raise ValueError(f"theta file not found: {theta_path}") from exc
    try:
        # On force la conversion en float pour éviter des types inattendus
        # (ex : str, None) qui casseraient le calcul
        theta0 = float(data["theta0"])
        theta1 = float(data["theta1"])
    except (KeyError, TypeError, ValueError) as exc:
        # On détecte et signale explicitement toute incohérence dans le fichier
        # afin d’éviter que des coefficients invalides ne contaminent l’évaluation
        raise ValueError(f"invalid theta values in {theta_path}") from exc
    return theta0, theta1


def evaluate(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    But:
        Évaluer la qualité prédictive du modèle avec RMSE et R².
    """

    # On recharge les données réelles pour garantir que l’évaluation
    # se fait bien sur le même dataset que l’entraînement
    data = read_data(data_path)

    # On recharge les coefficients sauvegardés pour utiliser
    # le modèle tel qu’il a été entraîné
    theta0, theta1 = read_theta(theta_path)

    # On extrait les prix réels pour constituer la vérité terrain (y_true)
    y_true = [price for _, price in data]

    # On calcule les prix prédits avec le modèle → nécessaire
    # pour comparer directement vérité terrain et prédictions
    y_pred = [estimate_price(km, theta0, theta1) for km, _ in data]

    # Nombre d’échantillons pour normaliser les erreurs et éviter
    # qu’elles dépendent de la taille du dataset
    m = len(y_true)

    # RMSE = erreur quadratique moyenne → mesure robuste des écarts
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)

    # Moyenne des prix réels pour centrer les calculs de variance
    y_mean = sum(y_true) / m

    # Somme des carrés des résidus : quantité d’erreur non expliquée par le modèle
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))

    # Somme totale des carrés : variance totale des données
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)

    # Calcule R² avec garde pour ss_tot = 0
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def main() -> None:
    # On évalue rapidement sur les fichiers par défaut pour fournir
    # une démonstration immédiate du bon fonctionnement du module
    rmse, r2 = evaluate("data.csv", "theta.json")

    # On affiche RMSE car il indique la précision absolue des prédictions
    print(f"RMSE: {rmse}")

    # On affiche R² car il reflète la proportion de variance expliquée par le modèle
    print(f"R2: {r2}")


# On expose explicitement uniquement les fonctions utiles publiquement
# afin de limiter la surface d’API accessible via import *
__all__ = ["read_theta", "evaluate", "main"]

# On permet une exécution directe comme script, pratique pour tester rapidement
if __name__ == "__main__":  # pragma: no cover - manual execution
    main()
