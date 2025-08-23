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


def parse_args(argv: list[str] | None = None) -> tuple[float | None, str]:
    """Parse CLI arguments and prompt for mileage if needed."""
    args = build_parser().parse_args(argv)
    km = args.km
    if km is None and argv is None:
        while True:
            try:
                km = float(input("Enter mileage: "))
                break
            except ValueError:
                print("Invalid mileage. Please enter a number.")
    return km, args.theta


def load_theta(path: str) -> tuple[float, float]:
    """Return ``(theta0, theta1)`` from ``path`` or zeros if file is missing."""

    theta_path = Path(path)
    if not theta_path.is_file():
        return 0.0, 0.0
    try:
        data = json.loads(theta_path.read_text())
    except (OSError, json.JSONDecodeError):
        return 0.0, 0.0
    return float(data.get("theta0", 0.0)), float(data.get("theta1", 0.0))


def predict_price(km: float, theta_path: str = "theta.json") -> float:
    """Predict the car price for ``km`` using coefficients from ``theta_path``."""

    theta0, theta1 = load_theta(theta_path)
    if theta0 == 0.0 and theta1 == 0.0:
        return 0.0
    return estimatePrice(km, theta0, theta1)


__all__ = ["build_parser", "parse_args", "load_theta", "predict_price"]
