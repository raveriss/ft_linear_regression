"""Visualize the dataset and fitted regression line."""

from __future__ import annotations

import argparse
import math
from pathlib import Path
from statistics import NormalDist, median, stdev
from typing import Any, Iterable, Sequence, cast

import matplotlib.pyplot as plt

from linear_regression import estimatePrice
from metrics import evaluate
from predict.predict import load_theta
from train.train import read_data


def _build_parser() -> argparse.ArgumentParser:
    """Return a command-line argument parser."""

    parser = argparse.ArgumentParser(description="Visualize data and model")
    parser.add_argument("--data", default="data.csv", help="path to CSV data")
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to model coefficients",
    )
    parser.add_argument(
        "--show-eq",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="display regression equation",
    )
    parser.add_argument(
        "--show-residuals",
        action="store_true",
        default=False,
        help="display residuals as vertical lines",
    )
    parser.add_argument(
        "--show-median",
        action="store_true",
        default=False,
        help="display median of y as horizontal line",
    )
    parser.add_argument(
        "--confidence",
        nargs="?",
        type=float,
        const=0.95,
        default=None,
        help="display prediction confidence band at given level",
    )
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

    The line is drawn between the minimum and maximum values of ``xs``.
    """

    min_x = min(xs)
    max_x = max(xs)
    line_x = [min_x, max_x]
    line_y = [estimatePrice(x, theta0, theta1) for x in line_x]
    return line_x, line_y


def plot_regression_line(
    ax: Any,
    xs: Iterable[float],
    theta0: float,
    theta1: float,
    show_eq: bool,
) -> None:
    """Plot the regression line on ``ax`` and optionally annotate its equation."""

    line_x, line_y = _line_points(xs, theta0, theta1)
    ax.plot(line_x, line_y, color="red", label="theta0 + theta1 * x")

    if show_eq:
        equation = f"price = {theta0:.2f} + {theta1:.2f} * km"
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
    """Display vertical lines between actual and predicted values."""

    for x, y in data:
        y_hat = estimatePrice(x, theta0, theta1)
        plt_mod.vlines(x, y, y_hat, colors="gray", linewidth=0.5)


def plot_confidence_band(
    plt_mod: Any,
    xs: Iterable[float],
    data: Iterable[tuple[float, float]],
    theta0: float,
    theta1: float,
    level: float,
) -> None:
    """Shade the prediction confidence band at the given level."""

    xs_list = list(xs)
    if len(xs_list) <= 2:
        return
    mean_x = sum(xs_list) / len(xs_list)
    s_xx = sum((x - mean_x) ** 2 for x in xs_list)
    residuals = [y - estimatePrice(x, theta0, theta1) for x, y in data]
    sigma2 = sum(r**2 for r in residuals) / (len(xs_list) - 2)
    sigma = math.sqrt(sigma2)
    line_x = [
        min(xs_list) + (max(xs_list) - min(xs_list)) * i / 100 for i in range(101)
    ]
    y_hat_band = [estimatePrice(x, theta0, theta1) for x in line_x]
    z = NormalDist().inv_cdf(0.5 + level / 2)
    se = [
        sigma * math.sqrt(1 / len(xs_list) + ((x - mean_x) ** 2) / s_xx) for x in line_x
    ]
    lower = [y - z * e for y, e in zip(y_hat_band, se)]
    upper = [y + z * e for y, e in zip(y_hat_band, se)]
    plt_mod.fill_between(line_x, lower, upper, color="red", alpha=0.1)


def plot_central_tendency(plt_mod: Any, ys: Sequence[float], show_median: bool) -> None:
    """Draw mean and optionally median of ``ys``."""

    mean_y = sum(ys) / len(ys)
    plt_mod.axhline(mean_y, color="blue", linestyle="--", label="mean(y)")
    if show_median:
        median_y = median(ys)
        plt_mod.axhline(median_y, color="green", linestyle=":", label="median(y)")


def split_outliers(
    data: Sequence[tuple[float, float]],
    theta0: float,
    theta1: float,
    k: float,
) -> tuple[list[tuple[float, float]], list[tuple[float, float]]]:
    """Return ``(inliers, outliers)`` based on residual standard deviation."""

    residuals = [y - estimatePrice(x, theta0, theta1) for x, y in data]
    sigma = stdev(residuals) if len(residuals) > 1 else 0.0
    inliers = [(x, y) for (x, y), r in zip(data, residuals) if abs(r) <= k * sigma]
    outliers = [(x, y) for (x, y), r in zip(data, residuals) if abs(r) > k * sigma]
    return inliers, outliers


def plot_points(
    plt_mod: Any,
    inliers: Sequence[tuple[float, float]],
    outliers: Sequence[tuple[float, float]],
) -> None:
    """Scatter inliers and outliers with appropriate colors."""

    if inliers:
        plt_mod.scatter(
            [x for x, _ in inliers],
            [y for _, y in inliers],
            label="data",
        )
    if outliers:
        plt_mod.scatter(
            [x for x, _ in outliers],
            [y for _, y in outliers],
            color="orange",
            label="outliers",
        )


def main(argv: list[str] | None = None) -> None:
    """Visualize the dataset and the line defined by ``theta0 + theta1 * x``."""

    args = _build_parser().parse_args(argv)
    data = read_data(Path(args.data))
    theta0, theta1, *_ = load_theta(args.theta)
    rmse, r2 = evaluate(args.data, args.theta)
    xs = [x for x, _ in data]
    ys = [y for _, y in data]
    inliers, outliers = split_outliers(data, theta0, theta1, args.sigma_k)

    # Matplotlib n’est pas bien typé : on cast "plt" en Any pour ce bloc
    plt_any = cast(Any, plt)
    plot_points(plt_any, inliers, outliers)
    ax = plt_any.gca()
    if args.show_residuals:
        plot_residuals(plt_any, data, theta0, theta1)
    if args.confidence is not None:
        plot_confidence_band(plt_any, xs, data, theta0, theta1, args.confidence)
    plot_regression_line(ax, xs, theta0, theta1, args.show_eq)
    plot_central_tendency(plt_any, ys, args.show_median)

    plt_any.suptitle(f"RMSE: {rmse:.2f}, R2: {r2:.2f}")

    plt_any.xlabel("km")
    plt_any.ylabel("price")

    _, labels = ax.get_legend_handles_labels()  # évite reportUnusedVariable
    if any(labels):
        plt_any.legend()

    plt_any.show()


if __name__ == "__main__":  # pragma: no cover - convenience script
    main()
