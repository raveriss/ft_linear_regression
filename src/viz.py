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
    xs: Iterable[float], theta0: float, theta1: float
) -> tuple[list[float], list[float]]:
    """Return ``(x_points, y_points)`` for the regression line.

    But:
        Déterminer les extrémités et valeurs de la droite ajustée.
    """

    # Cherche l’abscisse minimale de l’échantillon
    min_x = min(xs)
    # Cherche l’abscisse maximale de l’échantillon
    max_x = max(xs)
    # Définit les deux points extrêmes à tracer
    line_x = [min_x, max_x]
    # Calcule ŷ sur ces deux abscisses pour la droite
    line_y = [estimatePrice(x, theta0, theta1) for x in line_x]
    return line_x, line_y


def plot_regression_line(
    ax: Any,
    xs: Iterable[float],
    theta0: float,
    theta1: float,
    show_eq: bool,
) -> None:
    """Plot the regression line on ``ax`` and optionally annotate its equation.

    But:
        Afficher la droite et, si demandé, son équation.
    """

    # Prépare les deux points extrêmes de la droite
    line_x, line_y = _line_points(xs, theta0, theta1)
    ax.plot(line_x, line_y, color="red", label="theta0 + theta1 * x")
    # Trace la droite sur les axes courants

    # Ajoute l’annotation de l’équation si activée
    if show_eq:
        # Formate l’équation pour une lecture rapide
        equation = f"price = {theta0:.2f} + {theta1:.2f} * km"
        # Positionne le texte relatif au cadre des axes
        ax.annotate(
            equation,
            xy=(0.05, 0.95),
            xycoords="axes fraction",
            ha="left",
            va="top",
        )


def plot_residuals(
    plt_mod: Any,
    data: Iterable[tuple[float, float]],
    theta0: float,
    theta1: float,
) -> None:
    """Display vertical lines between actual and predicted values.

    But:
        Visualiser l’écart y - ŷ pour chaque point.
    """

    # Itère sur chaque point pour tracer le résidu
    for x, y in data:
        # Calcule la prédiction pour l’abscisse
        y_hat = estimatePrice(x, theta0, theta1)
        # Trace un segment vertical entre y et ŷ
        plt_mod.vlines(x, y, y_hat, colors="gray", linewidth=0.5)


def _stats(xs_list: Sequence[float]) -> tuple[float, float]:
    """Return mean of ``xs_list`` and centered sum of squares."""

    mean_x = sum(xs_list) / len(xs_list)
    s_xx = sum((x - mean_x) ** 2 for x in xs_list)
    return mean_x, s_xx


def _residual_sigma(
    data: Iterable[tuple[float, float]],
    theta0: float,
    theta1: float,
    n: int,
) -> float:
    """Return standard deviation of residuals."""

    residuals = [y - estimatePrice(x, theta0, theta1) for x, y in data]
    sigma2 = sum(r**2 for r in residuals) / (n - 2)
    return math.sqrt(sigma2)


def _band_grid(xs_list: Sequence[float]) -> list[float]:
    """Return regular grid covering ``xs_list`` range."""

    min_x, max_x = min(xs_list), max(xs_list)
    return [min_x + (max_x - min_x) * i / 100 for i in range(101)]


def _std_errors(
    line_x: Sequence[float],
    xs_list: Sequence[float],
    sigma: float,
    mean_x: float,
    s_xx: float,
) -> list[float]:
    """Return pointwise standard errors for ``line_x``."""

    n = len(xs_list)
    return [sigma * math.sqrt(1 / n + ((x - mean_x) ** 2) / s_xx) for x in line_x]


def _band_bounds(
    y_hat_band: Sequence[float], se: Sequence[float], z: float
) -> tuple[list[float], list[float]]:
    """Return lower and upper bounds of the band."""

    lower = [y - z * e for y, e in zip(y_hat_band, se)]
    upper = [y + z * e for y, e in zip(y_hat_band, se)]
    return lower, upper


def plot_confidence_band(
    plt_mod: Any,
    xs: Iterable[float],
    data: Iterable[tuple[float, float]],
    theta0: float,
    theta1: float,
    level: float,
) -> None:
    """Shade the prediction confidence band at the given level.

    But:
        Afficher l’incertitude de prédiction au niveau donné.
    """

    # Matérialise xs pour stats et bornes
    xs_list = list(xs)
    # Si moins de 3 points, pas d’estimation fiable
    if len(xs_list) <= 2:
        return
    mean_x, s_xx = _stats(xs_list)
    # Si toutes les abscisses sont identiques, la variance est nulle et la bande
    # de confiance serait indéfinie. Dans ce cas, on abandonne silencieusement.
    if math.isclose(s_xx, 0.0):
        return
    sigma = _residual_sigma(data, theta0, theta1, len(xs_list))
    line_x = _band_grid(xs_list)
    y_hat_band = [estimatePrice(x, theta0, theta1) for x in line_x]
    # Calcule le quantile z de la loi normale pour le niveau de confiance.
    # (ex: 1.96 si 95 %)
    z = NormalDist().inv_cdf(0.5 + level / 2)
    se = _std_errors(line_x, xs_list, sigma, mean_x, s_xx)
    lower, upper = _band_bounds(y_hat_band, se, z)
    plt_mod.fill_between(line_x, lower, upper, color="red", alpha=0.1)


def plot_central_tendency(plt_mod: Any, ys: Sequence[float], show_median: bool) -> None:
    """Draw mean and optionally median of ``ys``.

    But:
        Visualiser tendance centrale pour lecture rapide.
    """

    # Calcule la moyenne des ordonnées
    mean_y = sum(ys) / len(ys)
    # Trace la ligne horizontale de la moyenne
    plt_mod.axhline(mean_y, color="blue", linestyle="--", label="mean(y)")
    # Optionnellement trace la médiane
    if show_median:
        # Calcule la médiane (robuste aux outliers)
        median_y = median(ys)
        # Trace la ligne horizontale de la médiane
        plt_mod.axhline(median_y, color="green", linestyle=":", label="median(y)")


def split_outliers(
    data: Sequence[tuple[float, float]],
    theta0: float,
    theta1: float,
    k: float,
) -> tuple[list[tuple[float, float]], list[tuple[float, float]]]:
    """Return ``(inliers, outliers)`` based on residual standard deviation.

    But:
        Séparer points selon |résidu| ≤/> k·σ pour styliser le nuage.
    """

    # Calcule les résidus sur l’échantillon
    residuals = [y - estimatePrice(x, theta0, theta1) for x, y in data]
    # Estime σ des résidus (0 si <2 points)
    sigma = stdev(residuals) if len(residuals) > 1 else 0.0
    # Conserve points dont le résidu est dans k·σ
    inliers = [(x, y) for (x, y), r in zip(data, residuals) if abs(r) <= k * sigma]
    # Marque points dont le résidu dépasse k·σ
    outliers = [(x, y) for (x, y), r in zip(data, residuals) if abs(r) > k * sigma]
    return inliers, outliers


def plot_points(
    plt_mod: Any,
    inliers: Sequence[tuple[float, float]],
    outliers: Sequence[tuple[float, float]],
) -> None:
    """Scatter inliers and outliers with appropriate colors.

    But:
        Dessiner nuage de points et surligner les outliers.
    """

    # Dispersion des inliers si présents
    if inliers:
        # Trace les inliers sans couleur forcée
        plt_mod.scatter(
            [x for x, _ in inliers],
            [y for _, y in inliers],
            label="data",
        )
    # Dispersion des outliers si présents
    if outliers:
        # Trace les outliers avec couleur distinctive
        plt_mod.scatter(
            [x for x, _ in outliers],
            [y for _, y in outliers],
            color="orange",
            label="outliers",
        )


def main(argv: list[str] | None = None) -> None:
    """Visualize the dataset and the line defined by ``theta0 + theta1 * x``.

    But:
        Orchestrer chargement, évaluation et tracés Matplotlib.
    """

    # Parse les arguments passés à la commande
    args = _build_parser().parse_args(argv)
    # Charge et valide les données depuis le CSV
    data = read_data(Path(args.data))
    # Charge theta et ignore champs additionnels
    theta0, theta1, *_ = load_theta(args.theta)
    # Calcule RMSE et R² pour annotation
    rmse, r2 = evaluate(args.data, args.theta)
    # Extrait la liste des abscisses
    xs = [x for x, _ in data]
    # Extrait la liste des ordonnées
    ys = [y for _, y in data]
    # Sépare inliers/outliers selon k·σ
    inliers, outliers = split_outliers(data, theta0, theta1, args.sigma_k)

    # Neutralise le typage de plt pour appels dynamiques
    plt_any = cast(Any, plt)
    # Trace les points avec style outliers
    plot_points(plt_any, inliers, outliers)
    # Récupère les axes courants pour tracer la droite
    ax = plt_any.gca()
    # Si demandé, trace les segments de résidu
    if args.show_residuals:
        plot_residuals(plt_any, data, theta0, theta1)
    # Si niveau fourni, affiche la bande de confiance
    if args.confidence is not None:
        plot_confidence_band(plt_any, xs, data, theta0, theta1, args.confidence)
    # Trace la droite de régression et optionnellement l’équation
    plot_regression_line(ax, xs, theta0, theta1, args.show_eq)
    # Trace moyenne et éventuellement médiane des y
    plot_central_tendency(plt_any, ys, args.show_median)

    # Ajoute un titre synthétique avec métriques clés
    plt_any.suptitle(f"RMSE: {rmse:.2f}, R2: {r2:.2f}")

    # Étiquette l’axe des abscisses en kilomètres
    plt_any.xlabel("km")
    # Étiquette l’axe des ordonnées en prix
    plt_any.ylabel("price")

    # Récupère labels pour décider d’afficher la légende
    _, labels = ax.get_legend_handles_labels()  # évite reportUnusedVariable
    # Affiche la légende seulement si au moins un label existe
    if any(labels):
        plt_any.legend()

    # Ouvre la fenêtre de rendu des figures
    plt_any.show()


# Autorise l’exécution comme script utilitaire
if __name__ == "__main__":  # pragma: no cover - convenience script
    main()
