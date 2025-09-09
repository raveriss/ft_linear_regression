"""Visualiser le dataset et la droite de régression.

But:
    Offrir une CLI et des tracés pour diagnostiquer le modèle.
"""

# Active les annotations différées (compatibilité Python <3.11)
from __future__ import annotations

# Parse la CLI pour piloter l’affichage
import argparse

# Fournit sqrt et autres pour intervalles de confiance
import math

# Gère les chemins fichier de manière portable
from pathlib import Path

# Donne loi normale et stats robustes (médiane, stdev)
from statistics import NormalDist, median, stdev

# Types utilitaires pour signatures et cast
from typing import Any, Iterable, Sequence, cast

# Backend plotting pour générer les figures
import matplotlib.pyplot as plt

# Fonction de prédiction du modèle linéaire
from linear_regression import estimatePrice

# Calcule RMSE et R² pour le titre/diagnostic
from metrics import evaluate

# Charge les paramètres du modèle depuis fichier
from predict.predict import load_theta

# Charge et valide le CSV des données
from train.train import read_data


def _build_parser() -> argparse.ArgumentParser:
    """Return a command-line argument parser.

    But:
        Définir les options CLI pour contrôler les tracés.
    """

    # Construit l’objet parseur avec une description courte
    parser = argparse.ArgumentParser(description="Visualize data and model")
    # Ajoute l’option du chemin des données CSV
    parser.add_argument("--data", default="data.csv", help="path to CSV data")
    # Ajoute l’option du chemin des coefficients
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to model coefficients",
    )
    # Ajoute un flag pour afficher l’équation
    parser.add_argument(
        "--show-eq",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="display regression equation",
    )
    # Ajoute un flag pour tracer les résidus
    parser.add_argument(
        "--show-residuals",
        action="store_true",
        default=False,
        help="display residuals as vertical lines",
    )
    # Ajoute un flag pour tracer la médiane
    parser.add_argument(
        "--show-median",
        action="store_true",
        default=False,
        help="display median of y as horizontal line",
    )
    # Ajoute un niveau optionnel pour la bande de confiance
    parser.add_argument(
        "--confidence",
        nargs="?",
        type=float,
        const=0.95,
        default=None,
        help="display prediction confidence band at given level",
    )
    # Ajoute le seuil k en sigma pour marquer les outliers
    parser.add_argument(
        "--sigma-k",
        type=float,
        default=2.0,
        help="highlight points where |residual| > k * sigma",
    )
    return parser


def _line_points(
    liste_abscisses: Iterable[float],
    coefficient_intercept: float,
    coefficient_pente: float,
) -> tuple[list[float], list[float]]:
    """Construit deux points de la droite de régression.

    But:
        Déterminer les extrémités de la droite ajustée.
    """

    # Identifie l'abscisse minimale de l'échantillon
    abscisse_minimale = min(liste_abscisses)
    # Identifie l'abscisse maximale de l'échantillon
    abscisse_maximale = max(liste_abscisses)
    # Définit la liste des deux abscisses extrêmes
    liste_abscisses_extremes = [abscisse_minimale, abscisse_maximale]
    # Calcule les ordonnées correspondantes via le modèle
    liste_ordonnees_extremes = [
        estimatePrice(abscisse, coefficient_intercept, coefficient_pente)
        for abscisse in liste_abscisses_extremes
    ]
    # Retourne les deux listes synchronisées (x, y)
    return liste_abscisses_extremes, liste_ordonnees_extremes


def plot_regression_line(
    axes_courants: Any,
    liste_abscisses: Iterable[float],
    coefficient_intercept: float,
    coefficient_pente: float,
    afficher_equation: bool,
) -> None:
    """Trace la droite de régression et optionnellement son équation.

    But:
        Visualiser la droite ajustée et annoter sa formule.
    """

    # Calcule les deux points extrêmes de la droite de régression
    liste_abscisses_extremes, liste_ordonnees_extremes = _line_points(
        liste_abscisses, coefficient_intercept, coefficient_pente
    )
    # Trace la droite rouge sur les axes
    axes_courants.plot(
        liste_abscisses_extremes,
        liste_ordonnees_extremes,
        color="red",
        label="theta0 + theta1 * x",
    )

    # Vérifie si l'affichage de l'équation est demandé
    if afficher_equation:
        # Formate l'équation de la droite pour affichage lisible
        texte_equation = (
            f"price = {coefficient_intercept:.2f} + {coefficient_pente:.2f} * km"
        )
        # Positionne l'équation dans le repère des axes
        axes_courants.annotate(
            texte_equation,
            xy=(0.05, 0.95),
            xycoords="axes fraction",
            ha="left",
            va="top",
        )


def plot_residuals(
    module_matplotlib: Any,
    donnees_points: Iterable[tuple[float, float]],
    coefficient_intercept: float,
    coefficient_pente: float,
) -> None:
    """Trace les segments verticaux des résidus.

    But:
        Visualiser l'écart entre valeur réelle et prédiction.
    """

    # Parcourt chaque point du jeu de données
    for abscisse, ordonnee in donnees_points:
        # Calcule la valeur prédite par le modèle
        ordonnee_predite = estimatePrice(
            abscisse, coefficient_intercept, coefficient_pente
        )
        # Trace un segment vertical entre la valeur réelle et la prédite
        module_matplotlib.vlines(
            abscisse, ordonnee, ordonnee_predite, colors="gray", linewidth=0.5
        )


def _stats(valeurs: Sequence[float]) -> tuple[float, float]:
    """Compute mean and centered sum of squares.

    But:
        Fournir la moyenne et la somme des carrés centrés pour valeurs.
    """

    # Calcule la moyenne, suppose valeurs non vide
    moyenne = sum(valeurs) / len(valeurs)
    # Calcule somme des écarts², risque NaN/inf si valeurs contient tel
    somme_ecarts_carres = sum((valeur - moyenne) ** 2 for valeur in valeurs)
    # Retourne couple (moyenne, somme carrés centrés)
    return moyenne, somme_ecarts_carres


def _ecart_type_residus(
    donnees: Iterable[tuple[float, float]],
    intercept: float,
    pente: float,
    taille_echantillon: int,
) -> float:
    """Retourne l'écart-type des résidus.

    But:
        Mesurer la dispersion des écarts entre valeurs observées et prédites.
    """

    residus = [
        valeur_observee - estimatePrice(valeur_entree, intercept, pente)
        for valeur_entree, valeur_observee in donnees
    ]
    variance = sum(residu**2 for residu in residus) / (taille_echantillon - 2)
    return math.sqrt(variance)


def _band_grid(abscisses_observees: Sequence[float]) -> list[float]:
    """Grille régulière sur l'intervalle des abscisses observées.

    But:
        Générer 101 points uniformes entre min et max des abscisses.
    """

    # Calcule la borne min; exige séquence non vide; ValueError sinon
    borne_min_abscisse = min(abscisses_observees)
    # Calcule la borne max; même hypothèse; O(n) temps cumulé min+max
    borne_max_abscisse = max(abscisses_observees)
    # Construit la grille dans [min,max]; 101 points; O(101) mémoire
    # NaN/inf dans les bornes se propagent dans le résultat
    # Si min == max: renvoie 101 copies de la même valeur; acceptable
    return [
        # Interpolation linéaire entre bornes avec pas 1/100
        borne_min_abscisse + (borne_max_abscisse - borne_min_abscisse) * indice / 100
        # Itère indice 0..100 pour espacement égal
        for indice in range(101)
    ]


def _std_errors(
    liste_points_cible: Sequence[float],
    liste_points_regression: Sequence[float],
    ecart_type_residus: float,
    moyenne_points_regression: float,
    somme_carre_centre: float,
) -> list[float]:
    """Calcule les erreurs standard ponctuelles.

    But:
        Fournir l'incertitude des prédictions pour chaque abscisse.
    """

    # Mesure la taille de l'échantillon pour la régression
    nombre_points_regression = len(liste_points_regression)
    # Calcule l'erreur standard pour chaque point cible
    return [
        ecart_type_residus
        * math.sqrt(
            1 / nombre_points_regression
            + ((point_cible - moyenne_points_regression) ** 2) / somme_carre_centre
        )
        for point_cible in liste_points_cible
    ]


def _band_bounds(
    liste_predictions: Sequence[float],
    liste_erreurs_standard: Sequence[float],
    quantile_normal: float,
) -> tuple[list[float], list[float]]:
    """Calcule les bornes inférieure et supérieure de la bande.

    But:
        Définir l'intervalle de confiance autour des prédictions.
    """

    # Borne inférieure = prédiction - marge (quantile × erreur standard)
    liste_bornes_inferieures = [
        prediction - quantile_normal * erreur_standard
        for prediction, erreur_standard in zip(
            liste_predictions, liste_erreurs_standard
        )
    ]
    # Borne supérieure = prédiction + marge (quantile × erreur standard)
    liste_bornes_superieures = [
        prediction + quantile_normal * erreur_standard
        for prediction, erreur_standard in zip(
            liste_predictions, liste_erreurs_standard
        )
    ]
    # Retourne les deux bornes pour chaque point prédictif
    return liste_bornes_inferieures, liste_bornes_superieures


def plot_confidence_band(
    module_matplotlib: Any,
    abscisses_iterable: Iterable[float],
    donnees_points: Iterable[tuple[float, float]],
    coefficient_intercept: float,
    coefficient_pente: float,
    niveau_confiance: float,
) -> None:
    """Trace la bande de confiance autour de la régression.

    But:
        Visualiser l'incertitude prédictive pour un niveau donné.
    """

    # Convertit l'itérable d'abscisses en liste exploitable
    liste_abscisses = list(abscisses_iterable)
    # Vérifie qu'il y a au moins 3 points, sinon variance résiduelle invalide
    if len(liste_abscisses) <= 2:
        return
    # Calcule la moyenne et la somme des carrés centrés
    moyenne_abscisses, somme_carre_centre = _stats(liste_abscisses)
    # Vérifie que la variance des abscisses n'est pas nulle
    if math.isclose(somme_carre_centre, 0.0):
        return
    # Estime l'écart-type des résidus selon les coefficients et données
    ecart_type_residus = _ecart_type_residus(
        donnees_points,
        coefficient_intercept,
        coefficient_pente,
        len(liste_abscisses),
    )
    # Crée une grille régulière d'abscisses pour tracer la bande
    grille_abscisses = _band_grid(liste_abscisses)
    # Calcule les prédictions du modèle sur la grille
    liste_predictions = [
        estimatePrice(abscisse, coefficient_intercept, coefficient_pente)
        for abscisse in grille_abscisses
    ]
    # Calcule le quantile z correspondant au niveau de confiance choisi
    quantile_normal = NormalDist().inv_cdf(0.5 + niveau_confiance / 2)
    # Calcule les erreurs standard ponctuelles
    liste_erreurs_standard = _std_errors(
        grille_abscisses,
        liste_abscisses,
        ecart_type_residus,
        moyenne_abscisses,
        somme_carre_centre,
    )
    # Calcule les bornes inférieures et supérieures de la bande
    liste_bornes_inferieures, liste_bornes_superieures = _band_bounds(
        liste_predictions, liste_erreurs_standard, quantile_normal
    )
    # Dessine la zone ombrée représentant la bande de confiance
    module_matplotlib.fill_between(
        grille_abscisses,
        liste_bornes_inferieures,
        liste_bornes_superieures,
        color="red",
        alpha=0.1,
    )


def plot_central_tendency(
    module_matplotlib: Any,
    liste_ordonnees: Sequence[float],
    afficher_mediane: bool,
) -> None:
    """Trace la moyenne et éventuellement la médiane des valeurs.

    But:
        Montrer rapidement la tendance centrale des données.
    """

    # Calcule la moyenne arithmétique des valeurs
    moyenne_ordonnees = sum(liste_ordonnees) / len(liste_ordonnees)
    # Trace une ligne horizontale représentant la moyenne
    module_matplotlib.axhline(
        moyenne_ordonnees, color="blue", linestyle="--", label="moyenne(y)"
    )
    # Vérifie si l'option d'affichage de la médiane est activée
    if afficher_mediane:
        # Calcule la médiane, robuste aux valeurs extrêmes
        mediane_ordonnees = median(liste_ordonnees)
        # Trace une ligne horizontale représentant la médiane
        module_matplotlib.axhline(
            mediane_ordonnees, color="green", linestyle=":", label="mediane(y)"
        )


def split_outliers(
    donnees_points: Sequence[tuple[float, float]],
    coefficient_intercept: float,
    coefficient_pente: float,
    seuil_ecart_type: float,
) -> tuple[list[tuple[float, float]], list[tuple[float, float]]]:
    """Sépare les points en inliers et outliers.

    But:
        Identifier les points atypiques selon |résidu| ≤/> k·σ.
    """

    # Calcule les résidus = écart entre valeur réelle et prédiction
    liste_residus = [
        ordonnee - estimatePrice(abscisse, coefficient_intercept, coefficient_pente)
        for abscisse, ordonnee in donnees_points
    ]
    # Estime l'écart-type des résidus si au moins 2 points
    ecart_type_residus = stdev(liste_residus) if len(liste_residus) > 1 else 0.0
    # Conserve les points dont le résidu est inférieur au seuil k·σ
    liste_inliers = [
        (abscisse, ordonnee)
        for (abscisse, ordonnee), residu in zip(donnees_points, liste_residus)
        if abs(residu) <= seuil_ecart_type * ecart_type_residus
    ]
    # Conserve les points dont le résidu dépasse le seuil k·σ
    liste_outliers = [
        (abscisse, ordonnee)
        for (abscisse, ordonnee), residu in zip(donnees_points, liste_residus)
        if abs(residu) > seuil_ecart_type * ecart_type_residus
    ]
    # Retourne les deux groupes de points
    return liste_inliers, liste_outliers


def plot_points(
    module_matplotlib: Any,
    liste_inliers: Sequence[tuple[float, float]],
    liste_outliers: Sequence[tuple[float, float]],
) -> None:
    """Trace un nuage de points avec inliers et outliers.

    But:
        Visualiser données et mettre en évidence les outliers.
    """

    # Vérifie si des inliers existent
    if liste_inliers:
        # Dispersion des inliers sans couleur spécifique
        module_matplotlib.scatter(
            [abscisse for abscisse, _ in liste_inliers],
            [ordonnee for _, ordonnee in liste_inliers],
            label="donnees",
        )
    # Vérifie si des outliers existent
    if liste_outliers:
        # Dispersion des outliers avec couleur distinctive
        module_matplotlib.scatter(
            [abscisse for abscisse, _ in liste_outliers],
            [ordonnee for _, ordonnee in liste_outliers],
            color="orange",
            label="outliers",
        )


def main(arguments_ligne_commande: list[str] | None = None) -> None:
    """Visualise le jeu de données et la droite θ0 + θ1·x.

    But:
        Charger, évaluer et tracer les éléments avec Matplotlib.
    """

    # Construit l'analyseur d'arguments et lit les options
    arguments = _build_parser().parse_args(arguments_ligne_commande)
    # Charge et valide les données depuis le fichier CSV
    donnees_points = read_data(Path(arguments.data))
    # Charge les coefficients du modèle et ignore champs additionnels
    coefficient_intercept, coefficient_pente, *_ = load_theta(arguments.theta)
    # Calcule RMSE et R² pour évaluer le modèle
    racine_mse, coefficient_determination = evaluate(arguments.data, arguments.theta)
    # Extrait la liste des abscisses des données
    liste_abscisses = [abscisse for abscisse, _ in donnees_points]
    # Extrait la liste des ordonnées des données
    liste_ordonnees = [ordonnee for _, ordonnee in donnees_points]
    # Sépare les points inliers et outliers selon le seuil k·σ
    liste_inliers, liste_outliers = split_outliers(
        donnees_points,
        coefficient_intercept,
        coefficient_pente,
        arguments.sigma_k,
    )

    # Neutralise le typage de plt pour appels dynamiques
    module_matplotlib = cast(Any, plt)
    # Trace les inliers et outliers
    plot_points(module_matplotlib, liste_inliers, liste_outliers)
    # Récupère les axes courants pour tracer la droite
    axes_courants = module_matplotlib.gca()
    # Si demandé, trace les segments représentant les résidus
    if arguments.show_residuals:
        plot_residuals(
            module_matplotlib,
            donnees_points,
            coefficient_intercept,
            coefficient_pente,
        )
    # Si un niveau de confiance est défini, trace la bande correspondante
    if arguments.confidence is not None:
        plot_confidence_band(
            module_matplotlib,
            liste_abscisses,
            donnees_points,
            coefficient_intercept,
            coefficient_pente,
            arguments.confidence,
        )
    # Trace la droite de régression et éventuellement son équation
    plot_regression_line(
        axes_courants,
        liste_abscisses,
        coefficient_intercept,
        coefficient_pente,
        arguments.show_eq,
    )
    # Trace la moyenne et éventuellement la médiane des ordonnées
    plot_central_tendency(module_matplotlib, liste_ordonnees, arguments.show_median)

    # Ajoute un titre synthétique avec les métriques d'évaluation
    module_matplotlib.suptitle(
        f"RMSE: {racine_mse:.2f}, R2: {coefficient_determination:.2f}"
    )

    # Étiquette l'axe des abscisses en kilomètres
    module_matplotlib.xlabel("km")
    # Étiquette l'axe des ordonnées en prix
    module_matplotlib.ylabel("price")

    # Récupère labels pour décider si légende à afficher
    _, liste_labels = axes_courants.get_legend_handles_labels()
    # Affiche la légende si au moins un label est présent
    if any(liste_labels):
        module_matplotlib.legend()

    # Ouvre la fenêtre de rendu graphique
    module_matplotlib.show()


# Autorise l’exécution comme script utilitaire
if __name__ == "__main__":  # pragma: no cover - convenience script
    main()
