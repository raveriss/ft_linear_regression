"""Basic linear regression helpers."""

from __future__ import annotations


def estimate_price(theta0: float, theta1: float, x: float) -> float:
    """Estimate the price using a simple linear regression model.

    Args:
        theta0: Intercept coefficient of the regression.
        theta1: Slope coefficient of the regression.
        x:      Input feature (e.g., mileage).

    Returns:
        The predicted value calculated as ``theta0 + theta1 * x``.
    """
    return float(theta0) + float(theta1) * float(x)


# Backwards compatibility with CamelCase name used in some examples.
estimatePrice = estimate_price
