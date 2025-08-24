"""Prediction utilities for the linear regression project."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

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
    if km is not None and km < 0:
        print("ERROR: invalid mileage (must be a non-negative number)")
        raise SystemExit(2)
    if km is None and argv is None:
        km = _prompt_mileage()
    if km is None:
        km = 0.0
    return km, args.theta


def load_theta(
    path: str,
) -> tuple[float, float, float | None, float | None, float | None, float | None]:
    """Return training coefficients and data bounds from ``path``.

    If the file cannot be read or contains invalid values, an error message is
    printed and the program exits with code ``2``.
    """

    theta_path = Path(path)
    try:
        raw = json.loads(theta_path.read_text())
    except (OSError, json.JSONDecodeError):
        print(f"ERROR: theta file not found: {theta_path}")
        raise SystemExit(2)
    try:
        theta0 = float(raw.get("theta0", 0.0))
        theta1 = float(raw.get("theta1", 0.0))
        bounds: dict[str, float | None] = {}
        for key in ("min_km", "max_km", "min_price", "max_price"):
            value = raw.get(key)
            bounds[key] = float(value) if value is not None else None
    except (TypeError, ValueError):
        print(f"ERROR: invalid theta values in {theta_path}")
        raise SystemExit(2)
    return (
        theta0,
        theta1,
        bounds["min_km"],
        bounds["max_km"],
        bounds["min_price"],
        bounds["max_price"],
    )


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
    if min_km is not None and max_km is not None and not (min_km <= km <= max_km):
        print(f"WARNING: mileage {km} outside data range [{min_km}, {max_km}]")
    if (
        min_price is not None
        and max_price is not None
        and not (min_price <= price <= max_price)
    ):
        print(f"WARNING: price {price} outside data range [{min_price}, {max_price}]")
    return price


__all__ = ["build_parser", "parse_args", "load_theta", "predict_price"]
