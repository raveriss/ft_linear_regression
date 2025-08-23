"""Training data utilities for the linear regression project."""

from __future__ import annotations

import csv
import math
from pathlib import Path


def _parse_row(row: dict[str, str | None], line_number: int) -> tuple[float, float]:
    """Convert a CSV row to a ``(km, price)`` pair."""

    try:
        km = float(row["km"])
        price = float(row["price"])
    except (TypeError, ValueError):
        raise ValueError(f"invalid row {line_number}: non-numeric value") from None
    if any(math.isnan(v) for v in (km, price)):
        raise ValueError(f"invalid row {line_number}: NaN value")
    return km, price


def read_data(path: str | Path) -> list[tuple[float, float]]:
    """Load ``(km, price)`` pairs from ``path``.

    The CSV file is expected to have ``km`` and ``price`` columns. Each value
    is converted to ``float``. A :class:`ValueError` is raised if a row contains
    non‑numeric values or ``NaN``.
    """

    csv_path = Path(path)
    with csv_path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != ["km", "price"]:
            raise ValueError("invalid CSV format (expected columns: km,price)")
        rows = [_parse_row(row, line) for line, row in enumerate(reader, start=2)]
    if not rows:
        raise ValueError("no data rows found")
    return rows


__all__ = ["read_data"]
