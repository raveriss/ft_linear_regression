"""Command-line entry point for the predict package."""

from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    """Return an argument parser for the prediction command."""
    parser = argparse.ArgumentParser(description="Predict a car price from mileage")
    parser.add_argument("--km", type=float, help="mileage in kilometers")
    parser.add_argument("--theta", help="path to theta JSON", default="theta.json")
    return parser


def main(argv: list[str] | None = None) -> int:
    """Parse arguments and run the prediction stub."""
    _ = build_parser().parse_args(argv)
    print("prediction routine not yet implemented")
    return 0


if __name__ == "__main__":  # pragma: no cover - module glue
    raise SystemExit(main())
