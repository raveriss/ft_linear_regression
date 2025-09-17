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

    parser = argparse.ArgumentParser(
        # On donne une description globale pour aider l’utilisateur
        # à comprendre immédiatement la finalité du programme
        description="Visualize data and model",
    )

    parser.add_argument(
        # On choisit une option (--data) pour permettre à l’utilisateur
        # de charger un jeu de données spécifique sans modifier le code
        "--data",
        # On fixe "data.csv" comme valeur par défaut
        # pour offrir une expérience clé en main
        default="data.csv",
        # On ajoute un message d’aide afin que l’utilisateur
        # sache à quoi sert ce paramètre en un coup d’œil
        help="path to CSV data",
    )

    parser.add_argument(
        # On choisit une option (--theta) pour permettre à l’utilisateur
        # de fournir les coefficients entraînés séparément des données
        "--theta",
        # On fixe "theta.json" comme valeur par défaut
        # pour standardiser l’échange de paramètres du modèle
        default="theta.json",
        # On précise l’aide pour que l’utilisateur comprenne
        # qu’il s’agit du fichier contenant les coefficients du modèle
        help="path to model coefficients",
    )

    parser.add_argument(
        # On choisit une option nommée (--show-eq) pour donner à l’utilisateur
        # le contrôle explicite sur l’affichage de l’équation dans le graphique
        "--show-eq",
        # On utilise BooleanOptionalAction pour permettre un interrupteur double
        # (--show-eq / --no-show-eq), afin d’offrir flexibilité et ergonomie
        action=argparse.BooleanOptionalAction,
        # On définit True par défaut pour que l’équation soit affichée
        # sans intervention explicite de l’utilisateur → transparence immédiate
        default=True,
        # On précise un message d’aide pour que l’utilisateur comprenne
        # la finalité de l’option → éviter toute ambiguïté à l’usage
        help="display regression equation",
    )

    parser.add_argument(
        # On choisit une option (--show-residuals) pour rendre visibles
        # les erreurs du modèle et aider l’utilisateur à diagnostiquer l’ajustement
        "--show-residuals",
        # On utilise un flag booléen simple
        # pour ne tracer les résidus que si explicitement demandé
        action="store_true",
        # On définit False par défaut afin de ne pas surcharger le graphe
        # avec des détails tant que ce n’est pas utile
        default=False,
        # On ajoute une aide claire pour signaler
        # que l’option trace les erreurs comme segments verticaux
        help="display residuals as vertical lines",
    )

    parser.add_argument(
        # On choisit une option (--show-median) pour permettre à l’utilisateur
        # de comparer la régression avec une mesure centrale robuste
        "--show-median",
        # On active la médiane seulement si explicitement demandé
        # car ce n’est pas toujours pertinent dans l’analyse
        action="store_true",
        # On définit False par défaut pour garder le graphe épuré
        default=False,
        # On précise une aide pour montrer
        # que l’option ajoute la médiane des prix comme ligne horizontale
        help="display median of y as horizontal line",
    )

    parser.add_argument(
        # On choisit une option (--confidence) pour donner la possibilité
        # d’afficher une bande d’incertitude autour de la régression
        "--confidence",
        # On autorise un paramètre optionnel
        # afin que l’utilisateur puisse définir le niveau de confiance voulu
        nargs="?",
        # On impose un type float pour refléter un pourcentage numérique
        type=float,
        # On fournit une valeur par défaut implicite (0.95) si l’option
        # est appelée sans argument → convention usuelle en statistique
        const=0.95,
        # On définit None par défaut si l’option n’est pas utilisée
        # pour ne pas afficher de bande inutilement
        default=None,
        # On ajoute un message d’aide clair pour indiquer
        # le rôle statistique de cette bande
        help="display prediction confidence band at given level",
    )

    parser.add_argument(
        # On choisit une option (--sigma-k) pour contrôler le seuil
        # qui définit les points considérés comme atypiques (outliers)
        "--sigma-k",
        # On impose un type float pour permettre de régler finement
        # le multiplicateur d’écart-type
        type=float,
        # On fixe 2.0 comme valeur par défaut
        # car c’est un seuil courant pour détecter les outliers
        default=2.0,
        # On ajoute une aide pour expliciter que cette option
        # met en évidence les points qui dépassent k·σ
        help="highlight points where |residual| > k * sigma",
    )

    return parser


def _line_points(
    liste_kilometres: Iterable[float],
    coefficient_intercept: float,
    coefficient_pente: float,
) -> tuple[list[float], list[float]]:
    """Construit deux points de la droite de régression.

    But:
        Déterminer les extrémités de la droite ajustée (km, prix).
    """

    # On prend le kilomètre minimum de l’échantillon
    # → garantit que la droite démarre au tout début des observations
    km_min = min(liste_kilometres)

    # On prend le kilomètre maximum de l’échantillon
    # → garantit que la droite s’étend jusqu’au dernier point observé
    km_max = max(liste_kilometres)

    # On forme la liste des deux extrêmes
    # → deux points suffisent pour représenter toute la droite
    kilometres_extremes = [km_min, km_max]

    # On calcule les prix prédits pour ces deux kilomètres
    # → permet de tracer un segment qui résume l’ensemble de la régression
    prix_extremes = [
        estimatePrice(km, coefficient_intercept, coefficient_pente)
        for km in kilometres_extremes
    ]

    # On retourne les deux listes synchronisées (km, prix)
    # → ces paires sont prêtes à être tracées dans la figure
    return kilometres_extremes, prix_extremes


def plot_regression_line(
    axes_courants: Any,
    liste_kilometres: Iterable[float],
    coefficient_intercept: float,
    coefficient_pente: float,
    afficher_equation: bool,
) -> None:
    """Trace la droite de régression et optionnellement son équation.

    But:
        Visualiser la droite ajustée et annoter sa formule.
    """

    # On calcule deux points extrêmes (min et max km) de la droite
    # → il suffit de relier ces deux extrêmes pour représenter la régression
    #   car une droite est définie par deux points
    kilometres_extremes, prix_extremes = _line_points(
        liste_kilometres, coefficient_intercept, coefficient_pente
    )

    # On trace la droite rouge dans le graphe
    # → rend visible la tendance centrale trouvée par le modèle
    # → permet de comparer visuellement les données aux prédictions
    axes_courants.plot(
        kilometres_extremes,
        prix_extremes,
        color="red",
        label="theta0 + theta1 * km",
    )

    # Si demandé, on ajoute l’équation de la droite sur le graphe
    if afficher_equation:
        # On formate l’équation pour la rendre lisible à l’utilisateur
        # → aide à interpréter numériquement la pente et l’intercept
        texte_equation = (
            f"price = {coefficient_intercept:.2f} + {coefficient_pente:.2f} * km"
        )

        # On place le texte directement dans le repère
        # → l’utilisateur garde en mémoire la formule exacte
        #   tout en voyant son tracé graphique
        axes_courants.annotate(
            texte_equation,
            xy=(0.05, 0.95),
            xycoords="axes fraction",
            ha="left",
            va="top",
        )


def plot_residuals(
    module_matplotlib: Any,
    donnees_reelles: Iterable[tuple[float, float]],
    coefficient_intercept: float,
    coefficient_pente: float,
) -> None:
    """Trace les segments verticaux des résidus.

    But:
        Visualiser l'écart entre prix réel et prix prédit en fonction du kilométrage.
    """

    # On parcourt chaque point observé pour comparer réalité et modèle
    for kilometre, prix_reel in donnees_reelles:
        # On calcule le prix estimé → permet de matérialiser l’écart au modèle
        prix_prevu = estimatePrice(kilometre, coefficient_intercept, coefficient_pente)

        # On trace un segment vertical reliant le prix réel au prix prédit
        # → rend visible la magnitude et la direction de l’erreur
        # → plus le segment est long, plus l’erreur est importante
        # → segments au-dessus et en dessous de la droite indiquent
        #   respectivement une sous-estimation ou une surestimation
        module_matplotlib.vlines(
            kilometre, prix_reel, prix_prevu, colors="gray", linewidth=0.5
        )


def _stats(valeurs: Sequence[float]) -> tuple[float, float]:
    """Compute mean and centered sum of squares.

    But:
        Fournir la moyenne et la somme des carrés centrés pour valeurs.
    """

    # On calcule la moyenne car c’est le point de référence
    # nécessaire pour mesurer la dispersion autour du centre
    moyenne = sum(valeurs) / len(valeurs)

    # On calcule la somme des carrés centrés :
    #   Σ(x - x̄)²
    #
    # → mesure globale de la variabilité
    # → étape indispensable pour le calcul de variance,
    #   d’écarts-types ou pour pondérer les intervalles de confiance
    somme_ecarts_carres = sum((valeur - moyenne) ** 2 for valeur in valeurs)

    # On retourne la paire (moyenne, somme des carrés centrés)
    # → ce duo résume à la fois la tendance centrale et la dispersion,
    #   deux ingrédients essentiels pour l’inférence statistique
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

    # On calcule les résidus = différence entre prix réel (observé)
    # et prix estimé par le modèle → reflète l’erreur de prédiction
    residus = [
        valeur_observee - estimatePrice(valeur_entree, intercept, pente)
        for valeur_entree, valeur_observee in donnees
    ]

    # Formule de la variance des résidus :
    #   σ² = Σ(residu²) / (n - 2)
    #
    # → on divise par (n - 2) car on a estimé 2 paramètres (θ0 et θ1),
    #   ce qui réduit les degrés de liberté
    # → plus la variance est grande, plus le modèle s’écarte des données
    variance = sum(residu**2 for residu in residus) / (taille_echantillon - 2)

    # On prend la racine carrée pour revenir à l’unité d’origine (prix)
    # → l’écart-type rend l’ampleur de l’erreur directement interprétable
    return math.sqrt(variance)


def _band_grid(kilometres_observes: Sequence[float]) -> list[float]:
    """Grille régulière sur l'intervalle des kilomètres observés.

    But:
        Générer 101 points uniformes entre min et max des kilomètres.
    """

    # On prend le minimum observé comme borne gauche
    # → garantit que la grille couvre exactement le domaine d’observation
    borne_min_km = min(kilometres_observes)

    # On prend le maximum observé comme borne droite
    # → garantit que la bande de confiance s’étend jusqu’au dernier point connu
    borne_max_km = max(kilometres_observes)

    # Formule d’interpolation linéaire :
    #   valeur = min + (max - min) × (indice / 100)
    #
    # → génère 101 points régulièrement espacés
    # → assez dense pour dessiner une courbe lisse sans alourdir le calcul
    # → si min == max, la grille est plate (tous les points identiques),
    #   ce qui reste cohérent avec un dataset dégénéré
    return [
        # Interpolation linéaire entre bornes avec pas 1/100
        borne_min_km + (borne_max_km - borne_min_km) * indice / 100
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

    # On mesure la taille de l’échantillon car plus il y a de points,
    # plus l’estimation est fiable → la variance diminue avec n
    nombre_points_regression = len(liste_points_regression)

    # Formule : erreur_standard(x) =
    #   σ_residus × √(1/n + (x - x̄)² / Σ(x - x̄)²)
    #
    # → le premier terme (1/n) reflète l’incertitude globale liée à
    #   la taille de l’échantillon (toujours présent, même au centre)
    # → le second terme ((x - x̄)² / Σ(x - x̄)²) reflète l’effet levier :
    #   plus un point s’éloigne de la moyenne des x, plus son incertitude
    #   prédictive augmente
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
    # → représente la limite basse de l’incertitude,
    #   où la marge est calibrée par le niveau de confiance choisi
    liste_bornes_inferieures = [
        prediction - quantile_normal * erreur_standard
        for prediction, erreur_standard in zip(
            liste_predictions, liste_erreurs_standard
        )
    ]

    # Borne supérieure = prédiction + marge (quantile × erreur standard)
    # → représente la limite haute de l’incertitude,
    #   symétrique à la borne basse pour former la bande complète
    liste_bornes_superieures = [
        prediction + quantile_normal * erreur_standard
        for prediction, erreur_standard in zip(
            liste_predictions, liste_erreurs_standard
        )
    ]

    # On retourne les deux listes pour permettre de tracer directement
    # la zone d’incertitude qui encadre la prédiction du modèle
    return liste_bornes_inferieures, liste_bornes_superieures


def plot_confidence_band(
    module_matplotlib: Any,
    kilometres_iterable: Iterable[float],
    donnees_reelles: Iterable[tuple[float, float]],
    coefficient_intercept: float,
    coefficient_pente: float,
    niveau_confiance: float,
) -> None:
    """Trace la bande de confiance autour de la régression.

    But:
        Visualiser l'incertitude prédictive (prix en fonction du kilométrage).
    """

    # On convertit en liste pour permettre plusieurs parcours (stats, grille, tracé)
    # sans réévaluer un itérable potentiellement consommable une seule fois
    liste_kilometres = list(kilometres_iterable)

    # On exige au moins 3 points : en dessous, l’estimation de variance résiduelle
    # et des erreurs standard devient instable ou non définie
    if len(liste_kilometres) <= 2:
        return

    # On calcule moyenne et somme des carrés centrés pour caractériser la dispersion
    # du kilométrage : ces grandeurs servent à normaliser l’incertitude le long de x
    moyenne_km, somme_carre_centre = _stats(liste_kilometres)

    # Si la dispersion des km est quasi nulle, la droite est indéterminée sur x :
    # inutile de tracer une bande de confiance (elle serait dégénérée)
    if math.isclose(somme_carre_centre, 0.0):
        return

    # On estime l’écart-type des résidus pour quantifier le bruit inexpliqué
    # par le modèle : c’est la base de l’incertitude prédictive
    ecart_type_residus = _ecart_type_residus(
        donnees_reelles,
        coefficient_intercept,
        coefficient_pente,
        len(liste_kilometres),
    )

    # On génère une grille régulière de x pour obtenir une bande lisse et lisible,
    # plutôt que d’onduler uniquement sur les points d’entraînement
    grille_km = _band_grid(liste_kilometres)

    # On calcule les prédictions du modèle sur cette grille pour servir
    # de centre à la bande de confiance
    liste_prix_predits = [
        estimatePrice(km, coefficient_intercept, coefficient_pente) for km in grille_km
    ]

    # On prend le quantile normal correspondant au niveau de confiance demandé
    # (par ex. 1.96 pour 95 %) pour dimensionner la largeur de la bande
    quantile_normal = NormalDist().inv_cdf(0.5 + niveau_confiance / 2)

    # On calcule l’erreur standard en chaque x : l’incertitude n’est pas uniforme,
    # elle augmente loin de la moyenne de x (effet levier)
    liste_erreurs_standard = _std_errors(
        grille_km,
        liste_kilometres,
        ecart_type_residus,
        moyenne_km,
        somme_carre_centre,
    )

    # On combine prédiction ± z * SE pour obtenir les bornes de la bande :
    # c’est l’intervalle où on s’attend à voir la valeur moyenne prédite
    liste_bornes_inferieures, liste_bornes_superieures = _band_bounds(
        liste_prix_predits, liste_erreurs_standard, quantile_normal
    )

    # On remplit la zone entre les deux bornes avec une transparence faible :
    # assez visible pour indiquer l’incertitude, sans masquer les données
    module_matplotlib.fill_between(
        grille_km,
        liste_bornes_inferieures,
        liste_bornes_superieures,
        color="red",
        alpha=0.1,
    )


def plot_central_tendency(
    module_matplotlib: Any,
    liste_prix: Sequence[float],
    afficher_mediane: bool,
) -> None:
    """Trace la moyenne et éventuellement la médiane des prix.

    But:
        Montrer rapidement la tendance centrale des prix.
    """

    # On calcule la moyenne car c’est l’indicateur le plus courant
    # pour résumer un ensemble de valeurs → donne une vision globale
    moyenne_prix = sum(liste_prix) / len(liste_prix)

    # On trace une ligne horizontale pour rendre immédiatement visible
    # ce niveau moyen et permettre de comparer chaque point à cette référence
    module_matplotlib.axhline(
        moyenne_prix, color="blue", linestyle="--", label="moyenne(prix)"
    )

    # On n’affiche la médiane que si l’utilisateur l’a demandée,
    # car elle est surtout utile en présence de valeurs extrêmes
    if afficher_mediane:
        # On calcule la médiane pour obtenir une mesure robuste
        # qui ne soit pas influencée par quelques outliers
        mediane_prix = median(liste_prix)

        # On trace une ligne horizontale distincte pour fournir
        # une comparaison visuelle immédiate avec la moyenne
        module_matplotlib.axhline(
            mediane_prix, color="green", linestyle=":", label="mediane(prix)"
        )


def split_outliers(
    donnees_csv: Sequence[tuple[float, float]],
    coefficient_intercept: float,
    coefficient_pente: float,
    seuil_ecart_type: float,
) -> tuple[list[tuple[float, float]], list[tuple[float, float]]]:
    """Sépare les points en inliers et outliers.

    But:
        Identifier les points atypiques selon |résidu| ≤/> k·σ.
    """

    # On calcule les résidus (différence prix réel - prix prédit)
    # pour mesurer directement l’écart entre modèle et observation
    liste_residus = [
        prix_reel - estimatePrice(km, coefficient_intercept, coefficient_pente)
        for km, prix_reel in donnees_csv
    ]

    # On estime l’écart-type des résidus pour disposer d’une mesure
    # de la dispersion typique → sert de seuil pour définir “atypique”
    # Cas particulier : si moins de 2 points, σ n’est pas défini, on force à 0
    ecart_type_residus = stdev(liste_residus) if len(liste_residus) > 1 else 0.0

    # On conserve les points dont l’écart est ≤ k·σ
    # car ils représentent le comportement “normal” du modèle
    liste_inliers = [
        (km, prix_reel)
        for (km, prix_reel), residu in zip(donnees_csv, liste_residus)
        if abs(residu) <= seuil_ecart_type * ecart_type_residus
    ]

    # On isole les points dont l’écart est > k·σ
    # car ils sont susceptibles d’être aberrants et d’influencer fortement la régression
    liste_outliers = [
        (km, prix_reel)
        for (km, prix_reel), residu in zip(donnees_csv, liste_residus)
        if abs(residu) > seuil_ecart_type * ecart_type_residus
    ]

    # On retourne les deux groupes distincts pour permettre
    # un tracé différencié et une interprétation plus transparente
    return liste_inliers, liste_outliers


def plot_points(
    module_matplotlib: Any,
    inliers_km_prix: Sequence[tuple[float, float]],
    outliers_km_prix: Sequence[tuple[float, float]],
) -> None:
    """Trace un nuage de points avec inliers et outliers.

    But:
        Visualiser les données CSV (km, prix) et mettre en évidence les outliers.
    """

    # On ne trace les inliers que s’il y en a pour ne pas polluer le graphe
    # avec des appels vides → évite bruit visuel inutile
    if inliers_km_prix:
        # On affiche les points "normaux" pour révéler la tendance principale
        # sans couleur spéciale afin que la droite de régression reste la référence visuelle
        module_matplotlib.scatter(
            [km for km, _ in inliers_km_prix],  # axe X = kilométrage
            [prix for _, prix in inliers_km_prix],  # axe Y = prix observé
            label="donnees",  # étiquette légende pour interprétation claire
        )

    # On ne trace les outliers que s’il y en a pour éviter d’attirer l’attention
    # sur une catégorie inexistante → graphes plus lisibles
    if outliers_km_prix:
        # On affiche les points atypiques avec une couleur spécifique
        # pour les distinguer immédiatement et alerter sur leur influence possible
        module_matplotlib.scatter(
            [km for km, _ in outliers_km_prix],  # km suspects
            [prix for _, prix in outliers_km_prix],  # prix atypiques
            color="orange",  # couleur vive pour signaler qu’ils s’écartent de la norme
            label="outliers",  # légende claire pour interprétation par l’utilisateur
        )


def main(arguments_ligne_commande: list[str] | None = None) -> None:
    """Visualise le jeu de données (km, prix) et la droite θ0 + θ1·km.

    But:
        Charger, évaluer et tracer les éléments avec Matplotlib.
    """

    # On centralise la politique d’entrée pour garantir une CLI cohérente
    # et éviter des usages ambigus ou des valeurs par défaut implicites
    arguments = _build_parser().parse_args(arguments_ligne_commande)

    # On relit les données via la même filière de validation que l’entraînement
    # pour éviter tout écart de parsing entre train et viz
    donnees_csv = read_data(Path(arguments.data))

    # On récupère les coefficients appris afin d’afficher une droite
    # qui reflète exactement le dernier état du modèle
    coefficient_intercept, coefficient_pente, *_ = load_theta(arguments.theta)

    # On calcule RMSE et R² pour donner un contexte quantitatif au graphe
    # et permettre d’interpréter visuellement la qualité du modèle
    racine_mse, coefficient_determination = evaluate(arguments.data, arguments.theta)

    # On isole les km pour faciliter les appels aux fonctions de tracé
    # et éviter de recalculer des compréhensions à chaque étape
    liste_km = [km for km, _ in donnees_csv]

    # On isole les prix pour pouvoir tracer tendances centrales
    # et synthèses sans recouper la liste des tuples
    liste_prix = [prix for _, prix in donnees_csv]

    # On sépare inliers/outliers pour rendre lisible l’influence des points extrêmes
    # et éviter qu’ils ne masquent la structure globale sur le scatter
    inliers_km_prix, outliers_km_prix = split_outliers(
        donnees_csv,
        coefficient_intercept,
        coefficient_pente,
        arguments.sigma_k,
    )

    # On neutralise le typage de plt pour autoriser des appels dynamiques
    # (certaines backends/versions diffèrent), sans se battre avec l’IDE
    module_matplotlib = cast(Any, plt)

    # On trace d’abord les points afin que la droite et les éléments dérivés
    # se superposent sur un fond de données déjà visible
    plot_points(module_matplotlib, inliers_km_prix, outliers_km_prix)

    # On récupère les axes actifs pour s’assurer que les éléments suivants
    # (droite, légende) s’appliquent au même contexte graphique
    axes_courants = module_matplotlib.gca()

    # On affiche les résidus à la demande pour expliciter l’erreur point par point
    # sans surcharger le graphe si l’utilisateur ne le souhaite pas
    if arguments.show_residuals:
        plot_residuals(
            module_matplotlib,
            donnees_csv,
            coefficient_intercept,
            coefficient_pente,
        )

    # On trace la bande de confiance seulement si un niveau est spécifié
    # afin de matérialiser l’incertitude sans imposer d’hypothèse par défaut
    if arguments.confidence is not None:
        plot_confidence_band(
            module_matplotlib,
            liste_km,
            donnees_csv,
            coefficient_intercept,
            coefficient_pente,
            arguments.confidence,
        )

    # On dessine la droite de régression pour montrer la relation apprise
    # et, à la demande, son équation pour la transparence du modèle
    plot_regression_line(
        axes_courants,
        liste_km,
        coefficient_intercept,
        coefficient_pente,
        arguments.show_eq,
    )

    # On ajoute des indicateurs de tendance (moyenne, optionnellement médiane)
    # pour aider à juger visuellement les biais et la dispersion
    plot_central_tendency(module_matplotlib, liste_prix, arguments.show_median)

    # On titre le graphique avec RMSE et R² pour relier visuel et métriques
    # et éviter de devoir consulter la console pour les chiffres clés
    module_matplotlib.suptitle(
        f"RMSE: {racine_mse:.2f}, R2: {coefficient_determination:.2f}"
    )

    # On étiquette les axes pour lever toute ambiguïté d’unité/interprétation
    module_matplotlib.xlabel("km")
    module_matplotlib.ylabel("price")

    # On n’affiche une légende que s’il y a des éléments nommés,
    # pour éviter un cadre vide inutile et garder le graphe épuré
    _, liste_labels = axes_courants.get_legend_handles_labels()
    if any(liste_labels):
        module_matplotlib.legend()

    # On ouvre la fenêtre de rendu pour fournir un feedback visuel immédiat
    # (choix privilégié pour l’exploration interactive)
    module_matplotlib.show()


# Autorise l’exécution comme script utilitaire
if __name__ == "__main__":  # pragma: no cover - convenience script
    main()
