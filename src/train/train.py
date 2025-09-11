"""Utilitaires de données d'entraînement pour la régression linéaire.

But:
    Fournir des fonctions pour charger, valider et sauver les données.
"""

# Active les annotations différées (compatibilité Python <3.11)
from __future__ import annotations

# Fournit les primitives pour lire/écrire des fichiers CSV
import csv

# Fournit la sérialisation et désérialisation en JSON
import json

# Fournit les fonctions mathématiques (NaN, etc.)
import math

# Fournit un objet chemin multiplateforme pour fichiers
from pathlib import Path


def _float_field(value: str, line_number: int) -> float:
    """Convertit une valeur texte en float. Gère erreurs de parsing."""

    try:
        result = float(value)
    except ValueError:
        # Rejette les valeurs non numériques avec indication de ligne
        raise ValueError(f"invalid row {line_number}: non-numeric value") from None
    if math.isnan(result):
        # Rejette explicitement les valeurs NaN pour éviter des calculs instables
        raise ValueError(f"invalid row {line_number}: NaN value")
    return result


def _parse_row(row: dict[str, str | None], line_number: int) -> tuple[float, float]:
    """Convert a CSV row to a ``(km, price)`` pair."""

    # Extrait le champ "km" de la ligne CSV
    km_str = row.get("km")
    # Extrait le champ "price" de la ligne CSV
    price_str = row.get("price")

    # Vérifie qu'aucune des deux valeurs n'est manquante
    if km_str is None or price_str is None:
        raise ValueError(f"invalid row {line_number}: missing value")

    # Convertit km en float et vérifie validité
    km = _float_field(km_str, line_number)
    # Convertit price en float et vérifie validité
    price = _float_field(price_str, line_number)
    # Interdit les kilomètres négatifs
    if km < 0:
        raise ValueError(f"invalid row {line_number}: negative km")
    # Interdit les prix négatifs
    if price < 0:
        raise ValueError(f"invalid row {line_number}: negative price")
    return km, price


def read_data(path: str | Path) -> list[tuple[float, float]]:
    """Load ``(km, price)`` pairs from ``path``.

    But:
        Charger un CSV validé et convertir en liste de tuples floats.
    """

    # Normalise le chemin fourni en objet Path
    csv_path = Path(path)
    try:
        # Ouvre le fichier CSV en lecture texte UTF-8
        with csv_path.open(encoding="utf-8", newline="") as f:  # pragma: no mutate
            # Utilise DictReader pour map colonnes -> valeurs
            reader = csv.DictReader(f)
            # Vérifie que les colonnes sont exactement ["km","price"]
            if reader.fieldnames != ["km", "price"]:
                raise ValueError("invalid CSV format (expected columns: km,price)")
            # Parse chaque ligne et valide à partir de la ligne 2
            rows = [_parse_row(row, line) for line, row in enumerate(reader, start=2)]
    except OSError as exc:  # pragma: no cover - simple error propagation
        # Remonte une erreur claire si le fichier est absent/inaccessible
        raise ValueError(f"data file not found: {csv_path}") from exc
    # Rejette les fichiers CSV vides (aucune donnée)
    if not rows:
        raise ValueError("no data rows found")
    return rows


# def gradient_descent(
#     donnees_km_prix: list[tuple[float, float]],
#     taux_apprentissage: float,
#     nb_iterations: int,
# ) -> tuple[float, float]:
#     """Ajuste une droite de régression (prix = prix_base + pente * km) par descente de gradient.

#     But:
#         Estimer prix_base (valeur à 0 km) et pente (variation par km)
#         pour réduire au minimum l'écart entre estimation et données CSV.
#     """

#     # Correspondance des notations :
#     #   prix = pente * km + prix_base
#     #   équivalent à : y = θ1 * x + θ0
#     #   où pente = θ1 (coefficient directeur, a)
#     #       prix_base = θ0 (ordonnée à l'origine, b)

#     # Prix de base à 0 km (équivalent de θ0 ou b dans y = ax + b)
#     prix_base = 0.0
#     # Pente de la droite (équivalent de θ1 ou a dans y = ax + b)
#     pente = 0.0
#     # Nombre total d’exemples pour la moyenne
#     nb_exemples = float(len(donnees_km_prix))

#     # Répète le calcul sur un nombre fixé d’itérations
#     for _ in range(nb_iterations):
#         # Erreur moyenne globale sur toutes les prédictions → ajuste le prix de base
#         ajustement_prix_base = (
#             sum((prix_base + pente * km) - prix for km, prix in donnees_km_prix)
#             / nb_exemples
#         )

#         # Erreur moyenne pondérée par les km → ajuste la pente
#         ajustement_pente = (
#             sum(((prix_base + pente * km) - prix) * km for km, prix in donnees_km_prix)
#             / nb_exemples
#         )

#         # Mise à l’échelle par le taux d’apprentissage
#         correction_prix_base = taux_apprentissage * ajustement_prix_base
#         correction_pente = taux_apprentissage * ajustement_pente

#         # Mise à jour simultanée des coefficients
#         prix_base -= correction_prix_base
#         pente -= correction_pente

#         # --- Affichage de debug par itération ---
#         print(f"=== Itération {_} ===")
#         print(f"prix_base: {prix_base:.6f}, pente: {pente:.6f}")
#         print(f"ajustement_prix_base: {ajustement_prix_base:.6f}, ajustement_pente: {ajustement_pente:.6f}")
#         print(f"correction_prix_base: {correction_prix_base:.6f}, correction_pente: {correction_pente:.6f}")
#         print("")

#     return prix_base, pente


def gradient_descent(
    donnees_km_prix: list[tuple[float, float]],
    taux_apprentissage: float,
    nb_iterations: int,
) -> tuple[float, float]:
    """Ajuste une droite (prix = prix_base + pente * km) sur les données km/prix.

    But:
        Trouver prix_base (prix estimé à 0 km) et pente (variation par km)
        qui rapprochent au mieux les estimations des prix réels.
    """

    prix_base = 0.0  # Prix estimé à 0 km
    pente = 0.0  # Variation du prix en fonction des km
    nb_exemples = float(len(donnees_km_prix))

    # Seulement 3 étapes de calcul
    for numero_etape in range(nb_iterations):
        print(f"=== Étape {numero_etape} ===")

        for km, prix_reel in donnees_km_prix:
            estimation = prix_base + pente * km
            erreur = estimation - prix_reel
            print(
                f"km={km}, prix_reel={prix_reel}, estimation={estimation:.6f}, erreur={erreur:.6f}"
            )

        ajustement_prix_base = (
            sum((prix_base + pente * km) - prix for km, prix in donnees_km_prix)
            / nb_exemples
        )
        ajustement_pente = (
            sum(((prix_base + pente * km) - prix) * km for km, prix in donnees_km_prix)
            / nb_exemples
        )

        correction_prix_base = taux_apprentissage * ajustement_prix_base
        correction_pente = taux_apprentissage * ajustement_pente

        prix_base -= correction_prix_base
        pente -= correction_pente

        print(f"prix_base: {prix_base:.6f}, pente: {pente:.6f}")
        print("")

    return prix_base, pente


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

    # Normalise le chemin cible en objet Path
    theta_path = Path(path)
    # Prépare le dictionnaire avec les coefficients
    data: dict[str, float] = {"theta0": float(theta0), "theta1": float(theta1)}
    # Prépare un dictionnaire pour stocker les bornes optionnelles
    bounds: dict[str, float] = {}
    # Itère sur chaque borne potentielle à sauvegarder
    for key, value in [
        ("min_km", min_km),
        ("max_km", max_km),
        ("min_price", min_price),
        ("max_price", max_price),
    ]:
        # N'ajoute que si la borne est définie
        if value is not None:
            bounds[key] = float(value)
    # Fusionne bornes dans les données principales
    data.update(bounds)
    # Écrit le dictionnaire complet en JSON dans le fichier
    theta_path.write_text(json.dumps(data))


# Spécifie les symboles exportés pour import *
__all__ = ["read_data", "gradient_descent", "save_theta"]
