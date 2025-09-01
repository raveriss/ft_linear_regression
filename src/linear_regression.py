"""Helpers de base pour la régression linéaire.

But:
    Fournir des fonctions de prédiction simples et compatibles.
"""

# Active les annotations différées (compatibilité Python <3.11)
from __future__ import annotations


def estimatePrice(x: float, theta0: float, theta1: float) -> float:
    """Return the predicted value ``theta0 + theta1 * x``.

    But:
        Calculer la valeur estimée à partir des coefficients du modèle.
    """

    # Force chaque terme en float pour éviter erreurs de type
    return float(theta0) + float(theta1) * float(x)


def estimate_price(theta0: float, theta1: float, x: float) -> float:
    """Backwards-compatible snake_case wrapper around :func:`estimatePrice`.

    But:
        Maintenir une API rétrocompatible en snake_case.
    """

    # Délègue le calcul à estimatePrice (version camelCase)
    return estimatePrice(x, theta0, theta1)
