import json
from pathlib import Path

import pytest

from predict.predict import load_theta, predict_price


def test_load_theta_missing_and_predict(tmp_path: Path) -> None:
    theta_path = tmp_path / "theta.json"
    theta0, theta1 = load_theta(str(theta_path))
    assert theta0 == pytest.approx(0.0)
    assert theta1 == pytest.approx(0.0)
    assert predict_price(123.0, str(theta_path)) == pytest.approx(0.0)


def test_predict_price_with_file(tmp_path: Path) -> None:
    theta_path = tmp_path / "theta.json"
    theta_path.write_text(json.dumps({"theta0": 1.5, "theta1": 2.0}))
    theta0, theta1 = load_theta(str(theta_path))
    assert theta0 == pytest.approx(1.5)
    assert theta1 == pytest.approx(2.0)
    assert predict_price(3.0, str(theta_path)) == pytest.approx(1.5 + 2.0 * 3.0)
