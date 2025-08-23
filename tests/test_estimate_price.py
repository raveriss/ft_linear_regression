import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

import predict.predict  # noqa: F401,E402
import train.train  # noqa: F401,E402
from linear_regression import estimatePrice  # noqa: E402


def test_estimate_price_returns_linear_combination() -> None:
    theta0, theta1, x = 1.5, 2.0, 3.0
    assert estimatePrice(x, theta0, theta1) == pytest.approx(theta0 + theta1 * x)
