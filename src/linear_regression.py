"""Helpers de base pour la régression linéaire.

But:
    Fournir des fonctions de prédiction simples et compatibles.
"""

# On active les annotations différées pour améliorer la compatibilité
# avec d’anciennes versions de Python (avant 3.11) et réduire les dépendances
from __future__ import annotations


def estimate_price(theta0: float, theta1: float, x: float) -> float:
    """Return the predicted value ``theta0 + theta1 * x``.

    But:
        Calculer la valeur estimée à partir des coefficients du modèle.
    """

    # On force chaque terme en float pour garantir que le calcul reste
    # numérique même si des entiers ou d’autres types “float-like”
    # sont passés par erreur → robustesse et cohérence du résultat
    return float(theta0) + float(theta1) * float(x)


# Alias camelCase conservé uniquement pour compatibilité descendante.
# À terme, seule la version snake_case devrait être utilisée.
estimatePrice = estimate_price  # noqa: N815
