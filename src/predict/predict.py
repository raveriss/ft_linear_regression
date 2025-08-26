"""Prediction utilities for the linear regression project."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, cast

from linear_regression import estimatePrice


def build_parser() -> argparse.ArgumentParser:
    """Create a command-line argument parser for prediction."""
    parser = argparse.ArgumentParser(
        description="Predict a car price from mileage",
    )
    parser.add_argument("--km", type=float, help="mileage in kilometers")
    parser.add_argument("--theta", default="theta.json", help="path to theta JSON")
    return parser


def _prompt_mileage() -> float:
    """Interactively request a valid mileage from the user."""

    while True:
        try:
            km = float(input("Enter mileage: "))
        except ValueError:
            print("Invalid mileage. Please enter a number.")
            continue
        if km < 0:
            print("Invalid mileage. Must be a non-negative number.")
            continue
        return km


def parse_args(argv: list[str] | None = None) -> tuple[float, str]:
    """Parse CLI arguments and prompt for mileage if needed."""

    args = build_parser().parse_args(argv)
    km = args.km
    if km is None:
        km = _prompt_mileage() if argv is None else 0.0
    elif km < 0:
        print("ERROR: invalid mileage (must be a non-negative number)")
        raise SystemExit(2)
    return km, args.theta


def _read_theta(theta_path: Path) -> dict[str, Any]:
    try:
        return cast(dict[str, Any], json.loads(theta_path.read_text()))
    except (OSError, json.JSONDecodeError):
        print(f"ERROR: invalid theta file: {theta_path}")
        raise SystemExit(2)


def _parse_float(value: Any, theta_path: Path) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        print(f"ERROR: invalid theta values in {theta_path}")
        raise SystemExit(2)


def _parse_optional_float(value: Any, theta_path: Path) -> float | None:
    return None if value is None else _parse_float(value, theta_path)


def load_theta(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    When ``path`` does not exist, default coefficients are returned without
    raising an error so that predictions before training yield ``0``.  If the
    file exists but cannot be parsed or contains invalid values, an error
    message is printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    if not theta_path.exists():
        return 0.0, 0.0, None, None, None, None
    raw = _read_theta(theta_path)
    theta0 = _parse_float(raw.get("theta0", 0.0), theta_path)
    theta1 = _parse_float(raw.get("theta1", 0.0), theta_path)
    min_km = _parse_optional_float(raw.get("min_km"), theta_path)
    max_km = _parse_optional_float(raw.get("max_km"), theta_path)
    min_price = _parse_optional_float(raw.get("min_price"), theta_path)
    max_price = _parse_optional_float(raw.get("max_price"), theta_path)
    return theta0, theta1, min_km, max_km, min_price, max_price


def _warn_outside(
    value: float, bounds: tuple[float | None, float | None], label: str
) -> None:
    min_val, max_val = bounds
    if min_val is None or max_val is None:
        return
    if not (min_val <= value <= max_val):
        print(f"WARNING: {label} {value} outside data range [{min_val}, {max_val}]")


def predict_price(km: float, theta_path: str = "theta.json") -> float:
    """Predict the car price for ``km`` using coefficients from ``theta_path``."""

    (
        theta0,
        theta1,
        min_km,
        max_km,
        min_price,
        max_price,
    ) = load_theta(theta_path)
    if theta0 == 0.0 and theta1 == 0.0:
        return 0.0
    price = estimatePrice(km, theta0, theta1)
    _warn_outside(km, (min_km, max_km), "mileage")
    _warn_outside(price, (min_price, max_price), "price")
    return price


__all__ = ["build_parser", "parse_args", "load_theta", "predict_price"]
