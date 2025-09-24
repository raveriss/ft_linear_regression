"""Utilitaires de données d'entraînement pour la régression linéaire.

But:
    Fournir des fonctions pour charger, valider et sauver les données.
"""

# Active les annotations différées pour éviter les problèmes d’ordre d’import
# et améliorer la compatibilité avec Python <3.11
from __future__ import annotations

# On importe csv pour lire/écrire des fichiers tabulaires de façon fiable
# → évite les parsings manuels fragiles et garantit portabilité inter-OS
import csv

# On importe json pour sérialiser/désérialiser les coefficients entraînés
# → permet de sauvegarder/charger un modèle dans un format universel et lisible
import json

# On importe math pour gérer les cas numériques particuliers (ex: NaN, inf)
# → évite d’introduire des valeurs invalides dans les calculs du modèle
import math

# On importe Path pour manipuler les fichiers de manière uniforme et robuste
# → évite les différences Windows/Linux et fournit une API riche (.open, .exists, etc.)
from pathlib import Path


def _float_field(value: str, line_number: int) -> float:
    """Convertit une valeur texte en float. Gère erreurs de parsing."""

    try:
        result = float(value)
    except ValueError:
        # On refuse immédiatement les chaînes non numériques
        # pour éviter que du texte corrompu n'entre dans les calculs
        raise ValueError(f"invalid row {line_number}: non-numeric value") from None

    # On interdit explicitement NaN car cela se propage silencieusement
    # et rendrait toutes les moyennes/régressions instables
    if math.isnan(result):
        # Rejette explicitement les valeurs NaN pour éviter des calculs instables
        raise ValueError(f"invalid row {line_number}: NaN value")
    return result


def _valider_ligne(row: dict[str, str | None], line_number: int) -> tuple[float, float]:
    """Convert a CSV row to a ``(km, price)`` pair."""

    # On récupère les champs nommés pour détecter explicitement
    # une absence de colonne plutôt qu'une simple erreur d'index
    km_str = row.get("km")
    price_str = row.get("price")

    # On refuse toute ligne incomplète afin d'éviter
    # que des valeurs None ne contaminent la suite du calcul
    if km_str is None or price_str is None:
        raise ValueError(f"invalid row {line_number}: missing value")

    # On force la conversion en float ici pour détecter immédiatement
    # les données non numériques (ex: "abc") au lieu de propager du texte brut
    km = _float_field(km_str, line_number)
    price = _float_field(price_str, line_number)

    # Les km négatifs n'ont pas de sens dans un contexte automobile,
    # donc on bloque cette incohérence à la source
    if km < 0:
        raise ValueError(f"invalid row {line_number}: negative km")

    # Un prix négatif n'est pas réaliste économiquement,
    # donc on lève une erreur plutôt que de laisser passer une valeur absurde
    if price < 0:
        raise ValueError(f"invalid row {line_number}: negative price")
    return km, price


def read_data(path: str | Path) -> list[tuple[float, float]]:
    """Load ``(km, price)`` pairs from ``path``.

    But:
        Charger un CSV validé et convertir en liste de tuples floats.
    """

    # On convertit en Path pour garantir un accès cohérent et portable aux fichiers
    # → évite les différences de séparateurs entre Windows (\) et Linux (/)
    # → donne accès à une API uniforme (open(), .exists(), .stem(), etc.)
    #   au lieu de manipuler des chaînes fragiles
    csv_path = Path(path)
    try:
        # On impose UTF-8 + newline="" pour garantir une lecture portable,
        # éviter les soucis d'accents et gérer correctement les fins de lignes
        with csv_path.open(encoding="utf-8", newline="") as f:  # pragma: no mutate
            # DictReader est utilisé pour accéder aux colonnes par leur nom
            # au lieu d'index numériques → code plus robuste et lisible
            lecteur_csv = csv.DictReader(f)
            # Vérification stricte : on refuse tout CSV dont l'en-tête diffère
            # pour prévenir des erreurs silencieuses ou colonnes manquantes
            if lecteur_csv.fieldnames != ["km", "price"]:
                raise ValueError("invalid CSV format (expected columns: km,price)")
            # Parse chaque ligne et valide à partir de la ligne 2
            donnees_km_prix = [
                _valider_ligne(contenu_ligne, numero_ligne)
                for numero_ligne, contenu_ligne in enumerate(lecteur_csv, start=2)
            ]
    except OSError as exc:  # pragma: no cover - simple error propagation
        # On lève une ValueError claire (et non OSError brut)
        # pour que l'appelant comprenne immédiatement que c'est lié au fichier
        raise ValueError(f"data file not found: {csv_path}") from exc
    # On interdit les CSV vides afin d'éviter que le modèle
    # ne s'exécute sur une absence totale de données
    if not donnees_km_prix:
        raise ValueError("no data rows found")
    return donnees_km_prix


def gradient_descent(
    donnees_km_prix: list[tuple[float, float]],
    taux_apprentissage: float,
    nb_iterations: int,
) -> tuple[float, float]:
    """Ajuste une droite de régression par descente de gradient.

    L'équation a la forme ``prix = theta0 + theta1 * km``.

    But:
        Estimer theta0 (intercept) et theta1 (pente)
        en minimisant l’erreur entre prédictions et données réelles.
    """

    # On note theta0 = prix de base (ordonnée à l’origine)
    # et theta1 = pente (variation du prix par km)
    theta0 = 0.0
    theta1 = 0.0

    # m = nombre d’exemples (taille du dataset)
    # → il sert au calcul du facteur 1/m dans la formule du sujet
    m = float(len(donnees_km_prix))

    # On répète la mise à jour plusieurs fois
    # → une seule correction ne suffit pas à atteindre le minimum
    for _ in range(nb_iterations):
        # Erreur de prédiction pour chaque point :
        # (h_theta(x_i) - y_i) avec h_theta(x) = theta0 + theta1 * x
        erreurs = [(theta0 + theta1 * km) - prix for km, prix in donnees_km_prix]

        # Formule officielle :
        # Δθ0 = α * (1/m) * Σ (h_theta(x_i) - y_i)
        delta_theta0 = taux_apprentissage * (1 / m) * sum(erreurs)

        # Formule officielle :
        # Δθ1 = α * (1/m) * Σ ( (h_theta(x_i) - y_i) * x_i )
        delta_theta1 = (
            taux_apprentissage
            * (1 / m)
            * sum(erreur * km for (erreur, (km, _)) in zip(erreurs, donnees_km_prix))
        )

        # Mise à jour simultanée :
        # θ0 := θ0 - Δθ0
        # θ1 := θ1 - Δθ1
        # → garantit que les deux corrections sont cohérentes
        theta0 -= delta_theta0
        theta1 -= delta_theta1

    # On retourne les coefficients entraînés
    # → ce sont les paramètres optimaux de la droite ajustée
    return theta0, theta1


def save_theta(
    theta0: float,
    theta1: float,
    path: str | Path,
    min_km: float | None = None,
    max_km: float | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
) -> None:
    """Write training results and data bounds as JSON to ``path``.

    But:
        Sauvegarder les paramètres et bornes éventuelles dans un fichier JSON.
    """

    # On force l’utilisation d’un Path pour fiabiliser les opérations disque
    # et garder une API uniforme quel que soit l’OS
    theta_path = Path(path)

    # On stocke systématiquement les coefficients du modèle (theta0, theta1),
    # car ils sont indispensables pour toute prédiction future
    data: dict[str, float] = {"theta0": float(theta0), "theta1": float(theta1)}

    # On prépare un conteneur séparé pour les bornes, afin de ne les inclure
    # que si elles existent → évite d’écrire des champs inutiles ou ambigus
    bounds: dict[str, float] = {}

    # On parcourt les bornes possibles pour n’ajouter que celles
    # qui apportent une information réelle sur le dataset utilisé
    for key, value in [
        ("min_km", min_km),
        ("max_km", max_km),
        ("min_price", min_price),
        ("max_price", max_price),
    ]:
        # Si une borne est absente, on ne l’écrit pas :
        # cela différencie clairement “pas de donnée disponible”
        # d’une valeur numérique explicite
        if value is not None:
            bounds[key] = float(value)

    # On fusionne les bornes avec les coefficients pour obtenir
    # une seule source de vérité, simple à charger par predict/train
    data.update(bounds)

    # On écrit tout en JSON pour garantir portabilité et lisibilité :
    # ce format est standard, facile à parser et indépendant du langage
    theta_path.write_text(json.dumps(data))


# Spécifie les symboles exportés pour import *
__all__ = ["read_data", "gradient_descent", "save_theta"]
