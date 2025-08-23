"""Command-line entry point for the predict package."""

# pragma: no mutate
from __future__ import annotations

from .predict import build_parser, parse_args


def main(argv: list[str] | None = None) -> int:  # pragma: no mutate
    """Parse arguments and run the prediction stub."""
    _km, _theta = parse_args(argv)
    print("prediction routine not yet implemented")  # pragma: no mutate
    return 0  # pragma: no mutate


if __name__ == "__main__":  # pragma: no cover - module glue
    raise SystemExit(main())  # pragma: no mutate
