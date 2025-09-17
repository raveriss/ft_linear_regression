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
        # On refuse immédiatement les chaînes non numériques
        # pour éviter que du texte corrompu n'entre dans les calculs
        raise ValueError(f"invalid row {line_number}: non-numeric value") from None

    # On interdit explicitement NaN car cela se propage silencieusement
    # et rendrait toutes les moyennes/régressions instables
    if math.isnan(result):
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

    # On force l'utilisation de Path pour bénéficier d'une API unifiée (OS-indépendant)
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
            # On valide chaque ligne du CSV avec son numéro associé
            # pour repérer tôt les incohérences et signaler précisément
            # l’endroit de l’erreur (ex. "ligne 3 invalide").
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

    L'équation a la forme ``prix = prix_base + pente * km``.

    But:
        Estimer prix_base (valeur à 0 km) et pente (variation par km)
        pour réduire au minimum l'écart entre estimation et données CSV.
    """

    # Correspondance des notations :
    #   prix = pente * km + prix_base
    #   équivalent à : y = θ1 * x + θ0
    #   où pente = θ1 (coefficient directeur, a)
    #       prix_base = θ0 (ordonnée à l'origine, b)

    # On initialise à zéro pour donner un point de départ neutre
    # et laisser l’algorithme d’apprentissage corriger progressivement
    prix_base = 0.0
    pente = 0.0

    # On divise toujours par le nombre d’exemples pour obtenir une moyenne,
    # afin que l’ajustement ne dépende pas de la taille du dataset
    nb_exemples = float(len(donnees_km_prix))

    # On répète l’ajustement plusieurs fois pour converger vers la solution
    # car une seule correction ne suffit jamais à minimiser l’erreur
    for _ in range(nb_iterations):
        # L’ajustement du prix de base se fait en fonction de l’erreur moyenne :
        # si en moyenne nos prédictions sont trop hautes ou trop basses,
        # on corrige intercept pour recentrer la droite
        ajustement_prix_base = (
            sum((prix_base + pente * km) - prix for km, prix in donnees_km_prix)
            / nb_exemples
        )

        # L’ajustement de la pente prend en compte les kilomètres :
        # les erreurs sur des grands km doivent peser plus fort,
        # car elles influencent davantage la forme de la droite
        ajustement_pente = (
            sum(((prix_base + pente * km) - prix) * km for km, prix in donnees_km_prix)
            / nb_exemples
        )

        # On multiplie par le taux d’apprentissage pour contrôler la vitesse
        # de convergence et éviter de “sauter” par-dessus la solution optimale
        correction_prix_base = taux_apprentissage * ajustement_prix_base
        correction_pente = taux_apprentissage * ajustement_pente

        # On met à jour les coefficients en même temps pour garantir
        # une descente cohérente : si on corrigeait l’un après l’autre,
        # la mise à jour du second utiliserait déjà un premier biaisé
        prix_base -= correction_prix_base
        pente -= correction_pente

    # On retourne les coefficients ajustés : ce sont les paramètres
    # qui minimisent l’écart entre modèle et données observées
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
