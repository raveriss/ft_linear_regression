"""Command-line entry point for the predict package."""

# pragma: no mutate
from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the prediction command."""
    parser = argparse.ArgumentParser(
        description="Predict a car price from mileage"
    )  # pragma: no mutate
    parser.add_argument(
        "--km", type=float, help="mileage in kilometers"
    )  # pragma: no mutate
    parser.add_argument(
        "--theta", help="path to theta JSON", default="theta.json"
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def main(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Parse arguments and run the prediction stub."""
    _ = build_parser().parse_args(argv)  # pragma: no mutate
    print("prediction routine not yet implemented")  # pragma: no mutate
    return 0  # pragma: no mutate


if __name__ == "__main__":  # pragma: no cover - module glue
    raise SystemExit(main())  # pragma: no mutate
