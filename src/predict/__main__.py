"""Command-line entry point for the predict package."""

# pragma: no mutate
from __future__ import annotations

from .predict import parse_args, predict_price


def main(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Parse arguments, run the prediction and print the result."""
    try:
        km, theta = parse_args(argv)
        price = predict_price(km, theta)
    except SystemExit as exc:  # pragma: no cover - propagate exit codes
        return exc.code if isinstance(exc.code, int) else 1  # pragma: no cover
    print("0" if price == 0 else f"Predicted price: {price:.2f} €")
    return 0


if __name__ == "__main__":  # pragma: no cover - module glue
    raise SystemExit(main())  # pragma: no mutate
