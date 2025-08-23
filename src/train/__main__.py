"""Command-line entry point for the train package."""

from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    """Return an argument parser for the training command."""
    parser = argparse.ArgumentParser(description="Train the linear regression model")
    parser.add_argument("--data", help="path to training data CSV")
    parser.add_argument("--alpha", type=float, help="learning rate")
    parser.add_argument("--iters", type=int, help="number of iterations")
    parser.add_argument("--theta", help="path to theta JSON", default="theta.json")
    return parser


def main(argv: list[str] | None = None) -> int:
    """Parse arguments and run the training stub."""
    _ = build_parser().parse_args(argv)
    print("training routine not yet implemented")
    return 0


if __name__ == "__main__":  # pragma: no cover - module glue
    raise SystemExit(main())
