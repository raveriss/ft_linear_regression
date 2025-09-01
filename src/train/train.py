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


def gradient_descent(
    data: list[tuple[float, float]], alpha: float, iterations: int
) -> tuple[float, float]:
    """Return coefficients computed via gradient descent.

    But:
        Estimer theta0 et theta1 par itérations successives.
    """

    # Initialise theta0 à 0
    theta0 = 0.0
    # Initialise theta1 à 0
    theta1 = 0.0
    # Nombre d'échantillons converti en float pour divisions
    m = float(len(data))
    # Boucle d'optimisation sur nombre d'itérations demandé
    for _ in range(iterations):
        # Calcule le gradient partiel pour theta0
        dtheta0 = sum((theta0 + theta1 * x) - y for x, y in data) / m
        # Calcule le gradient partiel pour theta1
        dtheta1 = sum(((theta0 + theta1 * x) - y) * x for x, y in data) / m

        # Applique le taux d'apprentissage à dtheta0
        tmp_theta0 = alpha * dtheta0
        # Applique le taux d'apprentissage à dtheta1
        tmp_theta1 = alpha * dtheta1
        # Met à jour theta0 simultanément
        theta0 -= tmp_theta0
        # Met à jour theta1 simultanément
        theta1 -= tmp_theta1
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
