"""Basic linear regression helpers."""

from __future__ import annotations


def estimatePrice(x: float, theta0: float, theta1: float) -> float:
    """Return the predicted value ``theta0 + theta1 * x``."""

    return float(theta0) + float(theta1) * float(x)


def estimate_price(theta0: float, theta1: float, x: float) -> float:
    """Backwards-compatible snake_case wrapper around :func:`estimatePrice`."""

    return estimatePrice(x, theta0, theta1)
