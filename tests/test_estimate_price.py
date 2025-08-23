import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

import predict.predict  # noqa: F401
import train.train  # noqa: F401
from linear_regression import estimate_price


def test_estimate_price_returns_linear_combination() -> None:
    theta0, theta1, x = 1.5, 2.0, 3.0
    result = estimate_price(theta0, theta1, x)
    assert result == pytest.approx(theta0 + theta1 * x)
