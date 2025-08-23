"""Command-line entry point for the train package."""

# pragma: no mutate
from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""
    parser = argparse.ArgumentParser(
        description="Train the linear regression model"
    )  # pragma: no mutate
    parser.add_argument("--data", help="path to training data CSV")  # pragma: no mutate
    parser.add_argument(
        "--alpha", type=float, help="learning rate"
    )  # pragma: no mutate
    parser.add_argument(
        "--iters", type=int, help="number of iterations"
    )  # pragma: no mutate
    parser.add_argument(
        "--theta", help="path to theta JSON", default="theta.json"
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def main(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Parse arguments and run the training stub."""
    _ = build_parser().parse_args(argv)  # pragma: no mutate
    print("training routine not yet implemented")  # pragma: no mutate
    return 0  # pragma: no mutate


if __name__ == "__main__":  # pragma: no cover - module glue
    raise SystemExit(main())  # pragma: no mutate
