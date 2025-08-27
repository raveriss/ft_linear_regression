"""Visualize the dataset and fitted regression line."""

from __future__ import annotations

import argparse
from pathlib import Path
from statistics import median
from typing import Any, Iterable, cast

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


def main(argv: list[str] | None = None) -> None:
    """Visualize the dataset and the line defined by ``theta0 + theta1 * x``."""

    args = _build_parser().parse_args(argv)
    data = read_data(Path(args.data))
    theta0, theta1, *_ = load_theta(args.theta)
    rmse, r2 = evaluate(args.data, args.theta)

    xs = [x for x, _ in data]
    ys = [y for _, y in data]

    # Matplotlib n’est pas bien typé : on cast "plt" en Any pour ce bloc
    plt_any = cast(Any, plt)
    plt_any.scatter(xs, ys, label="data")
    ax = plt_any.gca()
    if args.show_residuals:
        for x, y in data:
            y_hat = estimatePrice(x, theta0, theta1)
            plt_any.vlines(x, y, y_hat, colors="gray", linewidth=0.5)
    plot_regression_line(ax, xs, theta0, theta1, args.show_eq)

    mean_y = sum(ys) / len(ys)
    plt_any.axhline(mean_y, color="blue", linestyle="--", label="mean(y)")
    if args.show_median:
        median_y = median(ys)
        plt_any.axhline(median_y, color="green", linestyle=":", label="median(y)")

    plt_any.suptitle(f"RMSE: {rmse:.2f}, R2: {r2:.2f}")

    plt_any.xlabel("km")
    plt_any.ylabel("price")

    _, labels = ax.get_legend_handles_labels()  # évite reportUnusedVariable
    if any(labels):
        plt_any.legend()

    plt_any.show()


if __name__ == "__main__":  # pragma: no cover - convenience script
    main()
