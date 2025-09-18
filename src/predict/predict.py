"""Prediction utilities for the linear regression project."""

# Active l’évaluation différée des annotations pour compatibilité typing.
from __future__ import annotations

# Permet de définir une CLI robuste et auto-documentée.
import argparse

# Permet de sérialiser/désérialiser les paramètres appris (theta).
import json

# Outils numériques pour comparer des flottants de manière robuste.
import math

# Uniformise la gestion de chemins pour lire le fichier theta.
from pathlib import Path

# Permet d'annoter des types génériques et clarifier les contrats.
from typing import Any, cast

# Réutilise la fonction de prédiction entraînée pour éviter la duplication.
from linear_regression import estimate_price


# Expose un parseur dédié pour centraliser la définition de la CLI.
def build_parser() -> argparse.ArgumentParser:
    """Create a command-line argument parser for prediction."""

    # On fournit une description explicite pour guider l'utilisateur
    # et rendre la CLI auto-documentée sans devoir consulter le code
    parser = argparse.ArgumentParser(
        # Précise l’usage au user, améliore l’ergonomie CLI.
        description="Predict a car price from mileage",
    )
    # On rend l'argument "km" optionnel : ainsi l'outil peut fonctionner
    # en mode interactif (demande à l'utilisateur) ou en mode scriptable
    parser.add_argument("km", nargs="?", type=float, help="mileage in kilometers")

    # On expose un paramètre pour choisir un fichier de coefficients,
    # ce qui permet de réutiliser différents modèles sans recompiler
    parser.add_argument("--theta", default="theta.json", help="path to theta JSON")

    # On renvoie le parseur afin de garantir une seule définition centralisée,
    # évitant les duplications et incohérences dans la CLI
    return parser


def _prompt_mileage() -> float:
    """Isole l’entrée interactive pour testabilité et réutilisation."""

    # On boucle jusqu'à obtenir une valeur valide pour éviter que
    # le programme ne s'arrête brutalement sur une mauvaise saisie
    while True:
        try:
            # On force la conversion en float ici pour garantir
            # que la valeur soit directement exploitable par le modèle
            km = float(input("Enter mileage: "))
        except ValueError:
            # On affiche un message clair et on redemande,
            # afin de préserver l'expérience utilisateur au lieu de planter
            print("Invalid mileage. Please enter a number.")
            # Reprend la saisie après erreur, améliore UX.
            continue

        # On interdit explicitement les km négatifs car ils n'ont aucun
        # sens métier et pourraient fausser complètement la prédiction
        if km < 0:
            # On explique la règle métier à l'utilisateur pour qu'il
            # comprenne l'échec et corrige sa saisie
            print("Invalid mileage. Must be a non-negative number.")
            continue

        # On sort seulement quand on a une valeur cohérente,
        # garantissant que le modèle ne reçoive jamais d'entrée invalide
        return km


def parse_args(argv: list[str] | None = None) -> tuple[float, str]:
    """Centralise le parsing et la politique d’entrée pour cohérence CLI."""

    # On réutilise un seul parseur pour garantir une configuration uniforme
    # entre toutes les commandes, et éviter les divergences de logique
    parser = build_parser()

    # On tolère temporairement des arguments inconnus pour détecter
    # et signaler une mauvaise utilisation de la CLI avec un message clair
    args, extra = parser.parse_known_args(argv)

    # Si des arguments en trop apparaissent, on bloque immédiatement
    # afin d'éviter des comportements implicites ou ambigus
    if extra:
        print("Too many arguments")
        print("Usage:")
        print("  make predict            # interactive")
        print("  make predict <km>       # direct prediction")
        print("  make train              # train the model")
        # On termine avec un code de sortie ≠ 0 pour que
        # les scripts externes sachent qu'il s'agit d'une erreur d'usage
        raise SystemExit(2)

    # Récupère la valeur fournie afin d’éviter re-saisie inutile.
    km = args.km
    if km is None:
        # Si aucun km n'est fourni, on privilégie l'interactif
        # uniquement en mode humain (argv=None), mais on fixe 0.0
        # en mode script pour rester totalement automatisable
        km = _prompt_mileage() if argv is None else 0.0
    # Valide la contrainte métier même en mode non interactif.
    elif km < 0:
        # On interdit explicitement les km négatifs car ils n'ont
        # aucun sens métier et risqueraient de biaiser le modèle
        print("ERROR: invalid mileage (must be a non-negative number)")
        # On coupe immédiatement avec un code clair pour que
        # l'erreur soit détectable en CI ou dans les pipelines
        raise SystemExit(2)

    # On renvoie la paire (km, theta) car ce sont les seules
    # infos nécessaires à la suite, évitant ainsi la redondance
    return km, args.theta


def _read_theta(theta_path: Path) -> dict[str, Any]:
    """Encapsule la lecture brute de theta et la validation de structure.

    But:
        Garantir qu’on retourne un dictionnaire clé/valeur validé,
        afin que le reste du pipeline (parsing typé) travaille sur une base sûre.
    """
    try:
        # On désérialise le JSON depuis disque : source unique de vérité des coefficients.
        # → tout le reste (prédiction/évaluation) dépend de l’intégrité de ce fichier.
        raw: Any = json.loads(theta_path.read_text())

        # On exige un dict pour éviter des formats inattendus (liste, str, etc.)
        # → ces formats ne correspondent pas au contrat “clé/valeur” attendu par le modèle.
        if not isinstance(raw, dict):
            # On déclenche un ValueError pour unifier la gestion d’erreur plus bas.
            raise ValueError

        # On informe le type-checker que le contenu est bien un dict[str, Any]
        # → évite les “dict[Unknown, Unknown]” et rend les accès aux champs sûrs/typés.
        typed_raw = cast(dict[str, Any], raw)

        # On ne retourne que l’objet validé pour éviter de propager une structure fragile.
        return typed_raw

    except (OSError, ValueError):
        # On explique clairement la cause probable (fichier manquant/corrompu/mal formé)
        # → l’utilisateur sait quoi corriger (chemin, contenu JSON).
        print(f"ERROR: invalid theta file: {theta_path}")
        # On stoppe net : continuer avec des coefficients invalides produirait des prédictions fausses.
        raise SystemExit(2)


def _parse_float(value: Any, theta_path: Path) -> float:
    """Normalise une valeur vers float et unifie le traitement d’erreur."""
    # Défense interne: garantit une trace de contexte en cas d’appel fautif.
    if theta_path is None:  # type: ignore[unreachable]
        raise AssertionError
    try:
        # On impose la conversion en float pour s'assurer que
        # les coefficients lus soient bien numériques et directement
        # utilisables par le modèle de régression.
        return float(value)
    except (TypeError, ValueError):
        # On relie l'erreur au fichier theta concerné pour que
        # l'utilisateur sache exactement où corriger le problème
        print(f"ERROR: invalid theta values in {theta_path}")

        # On interrompt immédiatement l'exécution pour éviter que
        # des paramètres invalides contaminent les calculs du modèle
        raise SystemExit(2)


def _maybe_float(value: Any, theta_path: Path) -> float | None:
    """Gère la présence d’optionnels tout en validant les non-nuls."""
    # Défense interne → protège contre un appel incohérent
    # même si l’annotation interdit None (utile pour mutation testing)
    if theta_path is None:  # type: ignore[unreachable]
        raise AssertionError
    # Retourne None si valeur absente → distinction claire "pas de donnée".
    # Sinon applique _parse_float pour valider/convertir en float sûr.
    return None if value is None else _parse_float(value, theta_path)


def load_theta(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    # On convertit en Path pour garantir un traitement cohérent et portable
    # des fichiers, quelle que soit la plateforme utilisée
    theta_path = Path(path)

    # Si aucun fichier n'existe, on fournit des coefficients neutres
    # (theta0=theta1=0.0) afin que le programme reste utilisable
    # même avant tout entraînement → évite un plantage inutile
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None

    # On valide la structure JSON avant d'exploiter les valeurs
    # pour éviter que des données corrompues n'entrent dans le modèle
    raw = _read_theta(theta_path)

    # On récupère l'ordonnée à l'origine (theta0), en tombant
    # sur une valeur par défaut sûre si elle est absente
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)

    # On récupère la pente (theta1), en protégeant là aussi contre
    # l'absence ou la corruption des données
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)

    # Les bornes des km sont optionnelles : on renvoie None si elles
    # ne sont pas stockées pour distinguer absence réelle de données
    min_km = _maybe_float(raw.get("min_km"), theta_path)
    max_km = _maybe_float(raw.get("max_km"), theta_path)

    # Même logique pour les bornes de prix : None signifie
    # “pas d'information disponible” plutôt qu'une valeur fausse
    min_price = _maybe_float(raw.get("min_price"), theta_path)
    max_price = _maybe_float(raw.get("max_price"), theta_path)

    # On retourne coefficients + bornes : indispensables pour
    # calibrer correctement les prédictions et produire
    # des avertissements cohérents (ex. extrapolation hors plage)
    return theta0, theta1, min_km, max_km, min_price, max_price


def _warn_outside(
    value: float, bounds: tuple[float | None, float | None], label: str
) -> None:
    """Alerte si une valeur sort du domaine d’entraînement pour transparence."""

    # On déstructure les bornes pour renforcer la clarté du code
    # et éviter des accès par index qui seraient moins lisibles
    min_val, max_val = bounds

    # Si les bornes ne sont pas définies (cas de modèle partiel ou données
    # incomplètes), on évite d'émettre des
    # warnings trompeurs → silence volontaire
    if min_val is None or max_val is None:
        return

    # On prévient l'utilisateur lorsque sa requête sort du domaine appris,
    # car une extrapolation réduit fortement la fiabilité du modèle.
    # Le message est volontairement non bloquant : il informe sans casser
    # le flux
    if not (min_val <= value <= max_val):
        print(f"WARNING: {label} {value} outside data range [{min_val}, {max_val}]")


def predict_price(km: float, theta_path: str = "theta.json") -> float:
    """Point d’accès unique pour produire un prix à partir d’un km fourni."""

    # On recharge systématiquement les coefficients et bornes sauvegardés
    # pour garantir que la prédiction reflète bien
    # le dernier entraînement effectué
    (
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    ) = load_theta(theta_path)

    # Test explicite : on sait que load_theta() renvoie exactement 0.0
    # par défaut si le modèle n'a pas été entraîné → pas de risque d'imprécision
    if math.isclose(theta0, 0.0) and math.isclose(theta1, 0.0):
        return 0

    # On applique la formule linéaire issue de l'entraînement
    # car c'est la relation validée par descente de gradient
    price = estimate_price(km, theta0, theta1)

    # On informe l'utilisateur si le kilométrage demandé sort du domaine appris,
    # car au-delà de cette plage la fiabilité du modèle est fortement réduite
    _warn_outside(km, (min_km, max_km), "mileage")

    # Même principe pour le prix : un avertissement accroît la transparence
    # et permet d'interpréter correctement une extrapolation
    _warn_outside(price, (min_price, max_price), "price")

    # On retourne la valeur finale pour qu'elle soit utilisée en CLI
    # ou dans d'autres parties du programme
    return price


# Limite l’API publique du module pour stabilité et clarté d’import.
__all__ = ["build_parser", "parse_args", "load_theta", "predict_price"]
