import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

import predict.predict  # noqa: F401,E402
import train.train  # noqa: F401,E402
from linear_regression import estimate_price, estimatePrice  # noqa: E402


def test_estimate_price_returns_linear_combination() -> None:
    theta0, theta1, x = 1.5, 2.0, 3.0
    expected = theta0 + theta1 * x
    assert estimatePrice(x, theta0, theta1) == pytest.approx(expected)
    assert estimate_price(theta0, theta1, x) == pytest.approx(expected)
