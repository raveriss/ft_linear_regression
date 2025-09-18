"""Helpers de base pour la régression linéaire.

But:
    Fournir des fonctions de prédiction simples et compatibles.
"""

# Active les annotations différées (compatibilité Python <3.11)
from __future__ import annotations


def estimate_price(x: float, theta0: float, theta1: float) -> float:
    """Return the predicted value ``theta0 + theta1 * x``.

    But:
        Calculer la valeur estimée à partir des coefficients du modèle.
    estimate_price
    """

    # Force chaque terme en float pour éviter erreurs de type
    return float(theta0) + float(theta1) * float(x)
