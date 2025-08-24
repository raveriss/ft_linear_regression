"""Training data utilities for the linear regression project."""

from __future__ import annotations

import csv
import json
import math
from pathlib import Path


def _float_field(value: str, line_number: int) -> float:
    try:
        result = float(value)
    except ValueError:
        raise ValueError(f"invalid row {line_number}: non-numeric value") from None
    if math.isnan(result):
        raise ValueError(f"invalid row {line_number}: NaN value")
    return result


def _parse_row(row: dict[str, str | None], line_number: int) -> tuple[float, float]:
    """Convert a CSV row to a ``(km, price)`` pair."""

    km_str = row.get("km")
    price_str = row.get("price")
    if km_str is None or price_str is None:
        raise ValueError(f"invalid row {line_number}: missing value")
    km = _float_field(km_str, line_number)
    price = _float_field(price_str, line_number)
    if km < 0:
        raise ValueError(f"invalid row {line_number}: negative km")
    if price < 0:
        raise ValueError(f"invalid row {line_number}: negative price")
    return km, price


def read_data(path: str | Path) -> list[tuple[float, float]]:
    """Load ``(km, price)`` pairs from ``path``.

    The CSV file is expected to have ``km`` and ``price`` columns. Each value
    is converted to ``float``. A :class:`ValueError` is raised if a row contains
    non‑numeric values or ``NaN``.
    """

    csv_path = Path(path)
    try:
        with csv_path.open(encoding="utf-8", newline="") as f:  # pragma: no mutate
            reader = csv.DictReader(f)
            if reader.fieldnames != ["km", "price"]:
                raise ValueError("invalid CSV format (expected columns: km,price)")
            rows = [_parse_row(row, line) for line, row in enumerate(reader, start=2)]
    except OSError as exc:  # pragma: no cover - simple error propagation
        raise ValueError(f"data file not found: {csv_path}") from exc
    if not rows:
        raise ValueError("no data rows found")
    return rows


def gradient_descent(
    data: list[tuple[float, float]], alpha: float, iterations: int
) -> tuple[float, float]:
    """Return coefficients computed via gradient descent.

    ``tmp_theta0`` and ``tmp_theta1`` are calculated before updating the
    coefficients so that the update is truly simultaneous.
    """

    theta0 = 0.0
    theta1 = 0.0
    m = float(len(data))
    for _ in range(iterations):
        dtheta0 = sum((theta0 + theta1 * x) - y for x, y in data) / m
        dtheta1 = sum(((theta0 + theta1 * x) - y) * x for x, y in data) / m
        tmp_theta0 = alpha * dtheta0
        tmp_theta1 = alpha * dtheta1
        theta0 -= tmp_theta0
        theta1 -= tmp_theta1
    return theta0, theta1


def save_theta(
    theta0: float,
    theta1: float,
    path: str | Path,
    min_km: float | None = None,
    max_km: float | None = None,
    min_price: float | None = None,
    max_price: float | None = None,
) -> None:
    """Write training results and data bounds as JSON to ``path``."""

    theta_path = Path(path)
    data = {"theta0": theta0, "theta1": theta1}
    if None not in (min_km, max_km, min_price, max_price):
        data.update(
            {
                "min_km": min_km,
                "max_km": max_km,
                "min_price": min_price,
                "max_price": max_price,
            }
        )
    theta_path.write_text(json.dumps(data))


__all__ = ["read_data", "gradient_descent", "save_theta"]
