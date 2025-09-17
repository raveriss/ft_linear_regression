"""Point d'entrée CLI pour le package train.

But:
    Fournir les imports et directives nécessaires pour exécuter la commande.
"""

# pragma: no mutate
from __future__ import annotations

# Charge argparse pour définir et valider l'interface CLI
import argparse

# Importe les fonctions cœur de l'entraînement (I/O et descente de gradient)
from .train import gradient_descent, read_data, save_theta


def _alpha_type(value: str) -> float:
    """Convertit une chaîne en taux d’apprentissage dans (0, 1].

    But:
        Valider --alpha et rejeter les valeurs non numériques ou hors borne.
    """
    # Convertit l'entrée en float; détecte format invalide (ex: virgule).
    try:
        # Conversion stricte; 'nan'/'inf' passent ici, filtrés plus bas.
        alpha = float(value)
    # Remappe ValueError en ArgumentTypeError pour message CLI clair.
    except ValueError as exc:  # pragma: no cover - argparse shows the message
        # Élève une erreur typée; conserve la cause pour le débogage.
        raise argparse.ArgumentTypeError(
            "alpha must be a floating point number"
        ) from exc
    # Invariant domaine: 0 < alpha ≤ 1; NaN/inf rejetés par comparaison.
    if not 0 < alpha <= 1:
        # Erreur utilisateur: valeur hors domaine fonctionnel.
        raise argparse.ArgumentTypeError("alpha must be in the range (0, 1]")
    # Post-condition: retourne un float strictement dans (0, 1].
    return alpha


def _iters_type(value: str) -> int:
    """Convertit une chaîne en entier positif.

    But:
        Valider --iters et garantir un entier strictement positif.
    """
    # Encadre la conversion pour produire une erreur CLI cohérente.
    try:
        # Force un entier décimal; ValueError si format invalide.
        iters = int(value)
    # Remappe ValueError en ArgumentTypeError pour l'utilisateur.
    except ValueError as exc:  # pragma: no cover - argparse shows the message
        # Message explicite; conserve la cause pour le débogage.
        raise argparse.ArgumentTypeError("iters must be a positive integer") from exc
    # Rejette zéro et négatif; évite boucle vide ou divergence
    if iters <= 0:
        # Stoppe avec message normé pour une saisie non valide.
        raise argparse.ArgumentTypeError("iters must be a positive integer")
    # Post: retourne un entier strictement supérieur à 0.
    return iters


def build_parser() -> argparse.ArgumentParser:  # pragma: no mutate
    """Construit le parseur d’arguments de l’entraînement.

    But:
        Définir les options, types et valeurs par défaut de la CLI.
    """

    # On crée un parseur dédié à l’entraînement pour isoler cette CLI
    # et fournir un message d’aide clair dès la ligne de commande
    parser = argparse.ArgumentParser(
        description="Train the linear regression model",  # message pour guider l’utilisateur
    )  # pragma: no mutate

    # On impose à l’utilisateur de fournir un dataset
    # afin de garantir que l’entraînement ne démarre jamais à vide
    parser.add_argument(
        "--data",
        required=True,  # obligatoire pour éviter un comportement implicite
        help="path to training data CSV",  # aide pour que l’utilisateur comprenne l’attendu
    )  # pragma: no mutate

    # On propose un alias français (--taux-apprentissage) pour l’accessibilité
    # tout en fixant dest="alpha" pour préserver un contrat stable avec les tests/scripts
    parser.add_argument(
        "--taux-apprentissage",
        "--alpha",  # alias anglais conservé pour cohérence avec la littérature ML
        dest="alpha",  # nom interne unique et stable
        type=_alpha_type,  # validation dédiée pour éviter des valeurs hors borne
        default=0.1,  # valeur par défaut sûre qui converge sur petits datasets
        help="learning rate (0 < alpha <= 1)",  # explication pédagogique pour l’utilisateur
    )  # pragma: no mutate

    # On autorise deux syntaxes (--nb-iterations et --iters)
    # afin de satisfaire à la fois les francophones et les habitués des conventions anglaises
    parser.add_argument(
        "--nb-iterations",
        "--iters",  # alias anglais pour compatibilité avec d’autres outils ML
        dest="iters",  # nom interne stable et cohérent
        type=_iters_type,  # validation stricte pour éviter itérations négatives ou nulles
        default=1000,  # valeur par défaut classique en descente de gradient
        help="number of iterations",  # message clair pour la documentation CLI
    )  # pragma: no mutate

    # On expose le chemin du fichier de sauvegarde des coefficients
    # pour donner le choix à l’utilisateur et éviter un fichier imposé
    parser.add_argument(
        "--theta",
        default="theta.json",  # fichier standard par défaut si l’utilisateur ne précise rien
        help="path to theta JSON",  # aide pour localiser les coefficients après entraînement
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

    try:
        # On centralise la lecture/validation des données ici afin
        # de protéger l’utilisateur contre les CSV corrompus ou incomplets
        data = read_data(args.data)
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

    # Retour 0 → succès nominal, conforme aux conventions Unix
    return 0


if __name__ == "__main__":  # pragma: no cover - module glue
    # Propage code retour de main() au système (exit code ≠0 si échec métier).
    raise SystemExit(main())  # pragma: no mutate
