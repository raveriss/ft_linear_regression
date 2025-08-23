"""Command-line entry point for the train package."""

# pragma: no mutate
from __future__ import annotations

import argparse

from .train import gradient_descent, read_data, save_theta


def build_parser() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""
    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data", required=True, help="path to training data CSV"
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha", type=float, required=True, help="learning rate"
    )  # pragma: no mutate
    parser.add_argument(
        "--iters", type=int, required=True, help="number of iterations"
    )  # pragma: no mutate
    parser.add_argument(
        "--theta", help="path to theta JSON", default="theta.json"
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def main(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""
    args = build_parser().parse_args(argv)
    data = read_data(args.data)
    theta0, theta1 = gradient_descent(data, args.alpha, args.iters)
    save_theta(theta0, theta1, args.theta)
    return 0


if __name__ == "__main__":  # pragma: no cover - module glue
    raise SystemExit(main())  # pragma: no mutate
