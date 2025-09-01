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
    # Instancie le parseur CLI; cadre d’usage et aide globale.
    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    # Exige le chemin CSV; fail fast si manquant. Contrat: transmis à read_data.
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    # Valide alpha via _alpha_type; par défaut stable 0.1.
    # Invariant: 0<alpha≤1 garanti par _alpha_type.    
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    # Valide un entier positif; impacte coût O(iters).
    parser.add_argument(
        "--iters",
        type=_iters_type,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    # Chemin de sortie des paramètres; permet override par l’utilisateur.
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    # Post: parseur prêt pour parse_args(argv).
    return parser  # pragma: no mutate


def main(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Entraîne le modèle via la ligne de commande.

    But:
        Parser, normaliser, optimiser, dénormaliser, puis sauvegarder.
    """
    # Parse la CLI; si argv=None, lit sys.argv implicitement.
    args = build_parser().parse_args(argv)
    # Encadre la lecture des données pour gérer les erreurs utilisateur.
    try:
        # Charge et valide le dataset depuis le chemin fourni.
        data = read_data(args.data)
    # Capture une erreur de format/valeur et passe en sortie contrôlée.
    except ValueError as exc:
        # Signale l'erreur à l'utilisateur sans traceback verbeux.
        print(f"ERROR: {exc}")
        # Code de retour ≠0 pour indiquer l'échec d'entrée.
        return 2

    # Sépare X et y; pré: chaque élément est un (km, price) numérique.
    kms, prices = zip(*data)
    # Calcule les bornes des kms pour normaliser.
    min_km, max_km = min(kms), max(kms)
    # Calcule les bornes des prix pour normaliser.
    min_price, max_price = min(prices), max(prices)

    # Évite div/0 si tous les kms sont identiques.
    km_range = max_km - min_km or 1.0  # pragma: no mutate
    # Évite div/0 si tous les prix sont identiques.
    price_range = max_price - min_price or 1.0  # pragma: no mutate
    # Mise à l'échelle [0,1] pour stabilité et vitesse du gradient.
    normalized = [
        ((km - min_km) / km_range, (price - min_price) / price_range)
        for km, price in data
    ]

    # Optimise sur données normalisées; pré: alpha∈(0,1], iters>0
    theta0_n, theta1_n = gradient_descent(normalized, args.alpha, args.iters)
    # Restaure la pente à l'échelle d'origine.# Restaure la pente à l'échelle d'origine.
    theta1 = theta1_n * price_range / km_range
    # Recalcule l'ordonnée à l'origine dans l'échelle réelle.
    theta0 = theta0_n * price_range + min_price - theta1 * min_km  # pragma: no mutate

    # Persiste paramètres et bornes pour les futures prédictions.
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
    raise SystemExit(main())  # pragma: no mutate
