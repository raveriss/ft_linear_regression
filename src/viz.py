"""Visualize the dataset and fitted regression line."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any, Iterable, cast

import matplotlib.pyplot as plt  # type: ignore[import-not-found]

from linear_regression import estimatePrice
from predict.predict import load_theta
from train.train import read_data

def _build_parser() -> argparse.ArgumentParser:
    """Return a command-line argument parser."""

    parser = argparse.ArgumentParser(description="Visualize data and model")
    parser.add_argument("--data", default="data.csv", help="path to CSV data")
    parser.add_argument(
        "--theta", default="theta.json", help="path to model coefficients"
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


def main(argv: list[str] | None = None) -> None:
    """Visualize the dataset and the line defined by ``theta0 + theta1 * x``."""

    args = _build_parser().parse_args(argv)
    data = read_data(Path(args.data))
    theta0, theta1, *_ = load_theta(args.theta)

    xs = [x for x, _ in data]
    ys = [y for _, y in data]

    # Matplotlib n’est pas bien typé : on cast "plt" en Any pour ce bloc
    plt_any = cast(Any, plt)
    plt_any.scatter(xs, ys, label="data")

    line_x, line_y = _line_points(xs, theta0, theta1)
    plt_any.plot(line_x, line_y, color="red", label="theta0 + theta1 * x")

    plt_any.xlabel("km")
    plt_any.ylabel("price")

    ax = plt_any.gca()
    _, labels = ax.get_legend_handles_labels()  # évite reportUnusedVariable
    if any(labels):
        plt_any.legend()

    plt_any.show()



if __name__ == "__main__":  # pragma: no cover - convenience script
    main()
