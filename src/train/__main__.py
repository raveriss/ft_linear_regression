"""Command-line entry point for the train package."""

# pragma: no mutate
from __future__ import annotations

import argparse

from .train import gradient_descent, read_data, save_theta


def _alpha_type(value: str) -> float:
    """Return ``value`` as a float within ``(0, 1]``.

    The training algorithm diverges for non‑positive or excessively large
    learning rates, so we validate the user input here to give immediate
    feedback if the provided ``--alpha`` is outside a safe range.
    """

    try:
        alpha = float(value)
    except ValueError as exc:  # pragma: no cover - argparse shows the message
        raise argparse.ArgumentTypeError(
            "alpha must be a floating point number"
        ) from exc
    if not 0 < alpha <= 1:
        raise argparse.ArgumentTypeError("alpha must be in the range (0, 1]")
    return alpha


def build_parser() -> argparse.ArgumentParser:  # pragma: no mutate
    """Return an argument parser for the training command."""

    parser = argparse.ArgumentParser(
        description="Train the linear regression model",
    )  # pragma: no mutate
    parser.add_argument(
        "--data",
        required=True,
        help="path to training data CSV",
    )  # pragma: no mutate
    parser.add_argument(
        "--alpha",
        type=_alpha_type,
        default=0.1,
        help="learning rate (0 < alpha <= 1)",
    )  # pragma: no mutate
    parser.add_argument(
        "--iters",
        type=int,
        default=1000,
        help="number of iterations",
    )  # pragma: no mutate
    parser.add_argument(
        "--theta",
        default="theta.json",
        help="path to theta JSON",
    )  # pragma: no mutate
    return parser  # pragma: no mutate


def main(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Train the model using command-line arguments."""

    args = build_parser().parse_args(argv)
    try:
        data = read_data(args.data)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 2
    theta0, theta1 = gradient_descent(data, args.alpha, args.iters)
    save_theta(theta0, theta1, args.theta)
    return 0


if __name__ == "__main__":  # pragma: no cover - module glue
    raise SystemExit(main())  # pragma: no mutate
