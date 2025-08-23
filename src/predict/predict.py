"""Prediction utilities for the linear regression project."""

from __future__ import annotations

import argparse


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


__all__ = ["build_parser", "parse_args"]
