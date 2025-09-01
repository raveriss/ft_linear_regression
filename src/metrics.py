"""Métriques d'évaluation pour la régression linéaire.

But:
    Fournir des fonctions pour charger les paramètres et calculer RMSE, R².
"""

# Active les annotations différées (compatibilité Python <3.11)
from __future__ import annotations

# Lecture/écriture JSON pour paramètres theta
import json
# Outils mathématiques (racine carrée, etc.)
import math
# Gestion robuste des chemins multiplateformes
from pathlib import Path

# Import de la fonction de prédiction du modèle
from linear_regression import estimatePrice
# Import de la fonction de chargement de données
from train.train import read_data


def read_theta(path: str | Path) -> tuple[float, float]:
    """Return ``(theta0, theta1)`` loaded from ``path``.

    But:
        Charger et valider les coefficients du modèle depuis un JSON.
    """

    # Normalise le chemin fourni en Path
    theta_path = Path(path)
    try:
        # Lit et désérialise le contenu JSON du fichier
        data = json.loads(theta_path.read_text())
    except (OSError, json.JSONDecodeError) as exc:  # pragma: no cover - simple
        # Convertit erreurs de lecture/JSON en ValueError explicite
        raise ValueError(f"theta file not found: {theta_path}") from exc
    try:
        # Convertit la clé "theta0" en float
        theta0 = float(data["theta0"])
        # Convertit la clé "theta1" en float
        theta1 = float(data["theta1"])
    except (KeyError, TypeError, ValueError) as exc:
        # Erreur si valeurs absentes ou invalides
        raise ValueError(f"invalid theta values in {theta_path}") from exc
    return theta0, theta1


def evaluate(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    But:
        Évaluer la qualité prédictive du modèle avec RMSE et R².
    """

    # Charge les données d'entraînement
    data = read_data(data_path)
    # Charge les coefficients du modèle
    theta0, theta1 = read_theta(theta_path)
    # Extrait les valeurs réelles de prix
    y_true = [price for _, price in data]
    # Calcule les valeurs prédites avec estimatePrice
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    # Nombre d'échantillons
    m = len(y_true)
    # Calcule la racine de l'erreur quadratique moyenne
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
     # Moyenne des valeurs réelles
    y_mean = sum(y_true) / m
    # Somme des carrés des résidus
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    # Somme totale des carrés
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    # Calcule R² avec garde pour ss_tot = 0
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def main() -> None:
    # Exécute une évaluation rapide sur fichiers par défaut
    rmse, r2 = evaluate("data.csv", "theta.json")
    # Affiche le RMSE calculé
    print(f"RMSE: {rmse}")
    # Affiche le coefficient R² calculé
    print(f"R2: {r2}")


# Spécifie les symboles exportés par import *
__all__ = ["read_theta", "evaluate", "main"]

# Permet l'exécution directe du module comme script
if __name__ == "__main__":  # pragma: no cover - manual execution
    main()
