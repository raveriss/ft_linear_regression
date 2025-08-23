"""Evaluation metrics for the linear regression project."""

from __future__ import annotations

import json
import math
from pathlib import Path

from linear_regression import estimatePrice
from train.train import read_data


def read_theta(path: str | Path) -> tuple[float, float]:
    """Return ``(theta0, theta1)`` loaded from ``path``.

    Raises :class:`ValueError` if the file cannot be read or contains invalid
    values.
    """

    theta_path = Path(path)
    try:
        data = json.loads(theta_path.read_text())
    except (OSError, json.JSONDecodeError) as exc:  # pragma: no cover - simple
        raise ValueError(f"theta file not found: {theta_path}") from exc
    try:
        theta0 = float(data["theta0"])
        theta1 = float(data["theta1"])
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError(f"invalid theta values in {theta_path}") from exc
    return theta0, theta1


def evaluate(data_path: str | Path, theta_path: str | Path) -> tuple[float, float]:
    """Return ``(rmse, r2)`` for the model specified by ``theta_path`` on data.

    ``rmse`` is the root mean squared error. ``r2`` is the coefficient of
    determination.
    """

    data = read_data(data_path)
    theta0, theta1 = read_theta(theta_path)
    y_true = [price for _, price in data]
    y_pred = [estimatePrice(km, theta0, theta1) for km, _ in data]
    m = len(y_true)
    rmse = math.sqrt(sum((p - y) ** 2 for p, y in zip(y_pred, y_true)) / m)
    y_mean = sum(y_true) / m
    ss_res = sum((y - p) ** 2 for p, y in zip(y_pred, y_true))
    ss_tot = sum((y - y_mean) ** 2 for y in y_true)
    r2 = 1.0 if ss_tot == 0.0 else 1 - ss_res / ss_tot
    return rmse, r2


def main() -> None:
    rmse, r2 = evaluate("data.csv", "theta.json")
    print(f"RMSE: {rmse}")
    print(f"R2: {r2}")


__all__ = ["read_theta", "evaluate", "main"]

if __name__ == "__main__":  # pragma: no cover - manual execution
    main()
