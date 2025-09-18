"""Point d'entrée CLI pour le package train.

But:
    Fournir les imports et directives nécessaires pour exécuter la commande.
"""

# pragma: no mutate
from __future__ import annotations

# argparse est utilisé pour offrir une interface CLI robuste
# → évite d’avoir à parser manuellement sys.argv et garantit une aide auto-générée
import argparse

# On importe uniquement les briques cœur de l’entraînement
# → séparation claire : la CLI reste une fine couche au-dessus du moteur
from .train import gradient_descent, read_data, save_theta


def _alpha_type(value: str) -> float:
    """Convertit une chaîne en taux d’apprentissage dans (0, 1].

    But:
        Valider --alpha et rejeter les valeurs non numériques ou hors borne.
    """

    # On encadre la conversion pour détecter des entrées invalides
    # → protège l’utilisateur contre des formats inattendus ("abc", virgules, etc.)
    try:
        # Conversion stricte; 'nan'/'inf' passent ici, filtrés plus bas.
        alpha = float(value)
    # On transforme une ValueError brute en ArgumentTypeError
    # → permet à argparse de fournir un message d’erreur clair côté CLI
    except ValueError as exc:  # pragma: no cover - argparse shows the message
        # Élève une erreur typée; conserve la cause pour le débogage.
        raise argparse.ArgumentTypeError(
            "alpha must be a floating point number"
        ) from exc

    # On impose la contrainte métier 0 < alpha ≤ 1
    # → évite des valeurs qui rendraient l’entraînement instable ou divergent
    if not 0 < alpha <= 1:
        # Erreur utilisateur: valeur hors domaine fonctionnel.
        raise argparse.ArgumentTypeError("alpha must be in the range (0, 1]")

    # On retourne un float validé, garanti conforme au domaine attendu
    return alpha


def _iters_type(value: str) -> int:
    """Convertit une chaîne en entier positif.

    But:
        Valider --iters et garantir un entier strictement positif.
    """

    # On encadre la conversion en int pour intercepter les formats incorrects
    # → l’utilisateur reçoit un message CLI clair plutôt qu’un crash Python
    try:
        # Force un entier décimal; ValueError si format invalide.
        iters = int(value)
    # On mappe l’exception sur ArgumentTypeError
    # → cohérence avec l’API argparse et retour utilisateur explicite
    except ValueError as exc:  # pragma: no cover - argparse shows the message
        # Message explicite; conserve la cause pour le débogage.
        raise argparse.ArgumentTypeError("iters must be a positive integer") from exc

    # On interdit zéro ou négatif
    # → empêche une boucle vide (0) ou incohérente (négatif) à l’entraînement
    if iters <= 0:
        # Stoppe avec message normé pour une saisie non valide.
        raise argparse.ArgumentTypeError("iters must be a positive integer")
    # On retourne un entier validé, strictement supérieur à zéro
    return iters


def build_parser() -> argparse.ArgumentParser:  # pragma: no mutate
    """Construit le parseur d’arguments de l’entraînement.

    But:
        Définir les options, types et valeurs par défaut de la CLI.
    """

    # On crée un parseur dédié à l’entraînement pour isoler cette CLI
    # et fournir un message d’aide clair dès la ligne de commande
    # Message pour guider l’utilisateur directement depuis --help
    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate

    # On impose à l’utilisateur de fournir un dataset
    # afin de garantir que l’entraînement ne démarre jamais à vide
    parser.add_argument(
        "--data",
        required=True,
        # Aide pour que l’utilisateur comprenne l’attendu
        help="path to training data CSV",
    )  # pragma: no mutate

    # On propose un alias français (--taux-apprentissage) pour l’accessibilité
    # tout en fixant dest="alpha" pour préserver un contrat stable
    # avec les tests/scripts
    parser.add_argument(
        "--taux-apprentissage",
        "--alpha",
        dest="alpha",
        type=_alpha_type,
        default=0.1,
        # Explication pédagogique pour l’utilisateur
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate

    # On autorise deux syntaxes (--nb-iterations et --iters)
    # afin de satisfaire à la fois les francophones et les habitués
    # des conventions anglaises
    parser.add_argument(
        "--nb-iterations",
        "--iters",
        dest="iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate

    # On expose le chemin du fichier de sauvegarde des coefficients
    # pour donner le choix à l’utilisateur et éviter un fichier imposé
    parser.add_argument(
        "--theta",
        default="theta.json",
        # Aide pour localiser les coefficients après entraînement
        help="path to theta JSON",
    )  # pragma: no mutate

    # On retourne le parseur ici pour centraliser toute la configuration CLI
    # et garantir que tous les appels utilisent la même logique d’entrée
    return parser  # pragma: no mutate


def main(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Entraîne le modèle via la ligne de commande.

    But:
        Parser, normaliser, optimiser, dénormaliser, puis sauvegarder.
    """

    # On passe par argparse pour garantir une CLI standardisée et claire,
    # et ainsi éviter les entrées mal formées ou ambiguës
    args = build_parser().parse_args(argv)

    # Encadre la lecture des données pour gérer les erreurs utilisateur.
    try:
        # On centralise la lecture/validation des données ici afin
        # de protéger l’utilisateur contre les CSV corrompus ou incomplets
        data = read_data(args.data)
    # Capture une erreur de format/valeur et passe en sortie contrôlée.
    except ValueError as exc:
        # On affiche une erreur simple et lisible à l’utilisateur
        # plutôt qu’un traceback Python illisible
        print(f"ERROR: {exc}")
        # Retour ≠ 0 pour signaler un échec de parsing ou de dataset
        return 2

    # On décompose explicitement km/prix pour traiter chaque dimension
    # séparément (notamment pour la normalisation qui suit)
    kms, prices = zip(*data)

    # On calcule les bornes min/max pour ramener les valeurs
    # dans une plage stable, et éviter que le gradient soit dominé
    # par des échelles trop grandes
    min_km, max_km = min(kms), max(kms)
    min_price, max_price = min(prices), max(prices)

    # On impose une borne non nulle pour éviter une division par zéro
    # dans les cas dégénérés (ex: tous les km ou prix identiques)
    km_range = max_km - min_km or 1.0  # pragma: no mutate
    price_range = max_price - min_price or 1.0  # pragma: no mutate

    # On normalise les données dans [0,1] pour :
    #  - améliorer la stabilité numérique
    #  - accélérer la convergence du gradient
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    # On entraîne le modèle sur données normalisées pour éviter
    # les biais liés aux unités ou aux ordres de grandeur
    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)

    # On ramène les paramètres du modèle à l’échelle réelle
    # pour que les prédictions soient exprimées en km/prix d’origine
    theta1 = theta1_n * price_range / km_range
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    # On sauvegarde les paramètres et bornes pour que `predict.py`
    # puisse reproduire exactement le même contexte de calcul
    save_theta(
        theta0,
        theta1,
        args.theta,
        min_km,
        max_km,
        min_price,
        max_price,
    )
    # Succès nominal.
    return 0


if __name__ == "__main__":  # pragma: no cover - module glue
    # Propage code retour de main() au système (exit code ≠0 si échec métier).
    raise SystemExit(main())  # pragma: no mutate
