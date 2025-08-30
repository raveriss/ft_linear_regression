"""Prediction utilities for the linear regression project."""

# Active l’évaluation différée des annotations pour compatibilité typing.
from __future__ import annotations

# Permet de définir une CLI robuste et auto-documentée.
import argparse

# Permet de sérialiser/désérialiser les paramètres appris (theta).
import json

# Uniformise la gestion de chemins pour lire le fichier theta.
from pathlib import Path

# Permet d'annoter des types génériques et clarifier les contrats.
from typing import Any

# Réutilise la fonction de prédiction entraînée pour éviter la duplication.
from linear_regression import estimatePrice


# Expose un parseur dédié pour centraliser la définition de la CLI.
def build_parser() -> argparse.ArgumentParser:
    """Create a command-line argument parser for prediction."""
    # Instancie le parseur pour gérer options et messages d’aide.
    parser = argparse.ArgumentParser(
        # Précise l’usage au user, améliore l’ergonomie CLI.
        description="Predict a car price from mileage",
    )
    # Rend l’argument km optionnel pour supporter le mode interactif.
    parser.add_argument("km", nargs="?", type=float, help="mileage in kilometers")
    # Permet de choisir une autre source de coefficients sans recompilation.    
    parser.add_argument("--theta", default="theta.json", help="path to theta JSON")
    # Retourne le parseur pour réutilisation dans parse_args().
    return parser


def _prompt_mileage() -> float:
    """Isole l’entrée interactive pour testabilité et réutilisation."""

    # Boucle jusqu’à obtenir une valeur utilisable, évite l’échec brutal.
    while True:
        try:
            # Convertit l’entrée pour normaliser le type attendu par le modèle.
            km = float(input("Enter mileage: "))
        except ValueError:
            # Informe l’utilisateur et relance sans quitter le programme.
            print("Invalid mileage. Please enter a number.")
            # Reprend la saisie après erreur, améliore UX.
            continue
        # Rejette les valeurs négatives car non physiques pour un kilométrage.
        if km < 0:
            # Explique la contrainte métier à l’utilisateur.
            print("Invalid mileage. Must be a non-negative number.")
            continue
        # Termine la boucle en renvoyant une valeur correcte.
        return km


def parse_args(argv: list[str] | None = None) -> tuple[float, str]:
    """ Centralise le parsing et la politique d’entrée pour cohérence CLI."""
    # Construit le parseur une seule fois pour config unique de la CLI.
    parser = build_parser()
    # Permet d’ignorer des arguments inconnus et de les contrôler ensuite.
    args, extra = parser.parse_known_args(argv)
    # Détecte une mauvaise utilisation de la CLI et guide l’utilisateur.
    if extra:
        print("Too many arguments")
        print("Usage:")
        print("  make predict            # interactive")
        print("  make predict <km>       # direct prediction")
        print("  make train              # train the model")
        raise SystemExit(2)
    # Récupère la valeur fournie afin d’éviter re-saisie inutile.
    km = args.km
    if km is None:
        # En CLI pure, évite l’interactif pour rester scriptable.
        km = _prompt_mileage() if argv is None else 0.0
    # Valide la contrainte métier même en mode non interactif.
    elif km < 0:
        # Explique l’échec pour diagnostiquer les appels fautifs.
        print("ERROR: invalid mileage (must be a non-negative number)")
        # Interrompt avec code conventionnel pour automatisation fiable.
        raise SystemExit(2)
    # Retourne km et chemin theta pour les étapes suivantes.
    return km, args.theta


def _read_theta(theta_path: Path) -> dict[str, Any]:
    """Encapsule la lecture brute de theta et la validation de structure."""
    try:
        # Charge le JSON depuis disque, source de vérité des coefficients.
        raw = json.loads(theta_path.read_text())
        # Imposé dict pour éviter des formats inattendus et fragiles.
        if not isinstance(raw, dict):
            # Force la gestion d’erreur unifiée dans l’except.
            raise ValueError
        # Expose l’objet validé aux parseurs de types aval.
        return raw
    except (OSError, json.JSONDecodeError, ValueError):
        # Fournit un message clair pour corriger le fichier cassé.
        print(f"ERROR: invalid theta file: {theta_path}")
        # Stoppe proprement pour éviter des prédictions incohérentes.
        raise SystemExit(2)


def _parse_float(value: Any, theta_path: Path) -> float:
    """Normalise une valeur vers float et unifie le traitement d’erreur."""
    # Défense interne: garantit une trace de contexte en cas d’appel fautif.
    if theta_path is None:
        raise AssertionError
    try:
        # Convertit pour respecter l’interface numérique du modèle.
        return float(value)
    except (TypeError, ValueError):
        # Localise l’erreur à la source pour faciliter la correction.
        print(f"ERROR: invalid theta values in {theta_path}")
        # Interrompt pour éviter des calculs avec paramètres corrompus.
        raise SystemExit(2)


def _parse_optional_float(value: Any, theta_path: Path) -> float | None:
    """Gère la présence d’optionnels tout en validant les non-nuls."""
    # Défense interne: garde le contexte fichier pour diagnostics.
    if theta_path is None:
        raise AssertionError
    # Laisse None passer, sinon applique la validation stricte.
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

    # Convertit en Path pour opérations de FS portables et explicites.
    theta_path = Path(path)
    # Autorise un flux “zéro modèle” sans plantage du binaire.
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    # Lit et valide la structure du fichier avant conversion de champs.
    raw = _read_theta(theta_path)
    # Récupère l’ordonnée à l’origine avec valeur par défaut sûre.
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    # Récupère la pente avec valeur par défaut sûre.
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    # Charge la borne basse des km si stockée, sinon None.
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    # Charge la borne haute des km si stockée, sinon None.
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    # Charge la borne basse du prix si stockée, sinon None.
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    # Charge la borne haute du prix si stockée, sinon None.
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    # Retourne coefficients et bornes pour la prédiction et les warnings.
    return theta0, theta1, min_km, max_km, min_price, max_price


def _warn_outside(
    value: float, bounds: tuple[float | None, float | None], label: str
) -> None:
    """Alerte si une valeur sort du domaine d’entraînement pour transparence."""
    # Déstructure pour lisibilité et évite accès par index plus loin.
    min_val, max_val = bounds
    # Désactive l’avertissement si les bornes sont inconnues.
    if min_val is None or max_val is None:
        return
    # Émet un warning non bloquant pour signaler une extrapolation.
    if not (min_val <= value <= max_val):
        print(f"WARNING: {label} {value} outside data range [{min_val}, {max_val}]")


def predict_price(km: float, theta_path: str = "theta.json") -> float:
    """Point d’accès unique pour produire un prix à partir d’un km fourni."""

    # Charge coefficients et bornes afin de contextualiser la prédiction.
    (
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    ) = load_theta(theta_path)
    # Retourne 0 si modèle non entraîné pour un comportement déterministe.
    if theta0 == 0.0 and theta1 == 0.0:
        return 0
    # Calcule le prix via la formule linéaire validée par l’entraînement.
    price = estimatePrice(km, theta0, theta1)
    # Prévient si le km demandé est hors du domaine observé.
    _warn_outside(km, (min_km, max_km), "mileage")
    # Prévient si le prix prédit est hors des prix observés.
    _warn_outside(price, (min_price, max_price), "price")
    # Expose la valeur calculée au reste du programme ou à la CLI.
    return price


# Limite l’API publique du module pour stabilité et clarté d’import.
__all__ = ["build_parser", "parse_args", "load_theta", "predict_price"]
