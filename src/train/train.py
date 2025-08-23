"""Training data utilities for the linear regression project."""

from __future__ import annotations

import csv
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
    return _float_field(km_str, line_number), _float_field(price_str, line_number)


def read_data(path: str | Path) -> list[tuple[float, float]]:
    """Load ``(km, price)`` pairs from ``path``.

    The CSV file is expected to have ``km`` and ``price`` columns. Each value
    is converted to ``float``. A :class:`ValueError` is raised if a row contains
    non‑numeric values or ``NaN``.
    """

    csv_path = Path(path)
    with csv_path.open(encoding="utf-8", newline="") as f:  # pragma: no mutate
        reader = csv.DictReader(f)
        if reader.fieldnames != ["km", "price"]:
            raise ValueError("invalid CSV format (expected columns: km,price)")
        rows = [_parse_row(row, line) for line, row in enumerate(reader, start=2)]
    if not rows:
        raise ValueError("no data rows found")
    return rows


__all__ = ["read_data"]
