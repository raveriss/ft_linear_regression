import json
from pathlib import Path

import pytest

from train.train import gradient_descent, save_theta


def test_gradient_descent_and_save(tmp_path: Path) -> None:
    data = [(0.0, 0.0), (1.0, 1.0)]
    theta0, theta1 = gradient_descent(data, alpha=0.1, iterations=2)
    assert theta0 == pytest.approx(0.0925)
    assert theta1 == pytest.approx(0.095)
    theta_path = tmp_path / "theta.json"
    save_theta(theta0, theta1, theta_path)
    content = json.loads(theta_path.read_text())
    assert content["theta0"] == pytest.approx(theta0)
    assert content["theta1"] == pytest.approx(theta1)


def test_save_theta_with_bounds(tmp_path: Path) -> None:
    theta_path = tmp_path / "theta.json"
    save_theta(
        1.0,
        2.0,
        theta_path,
        0.0,
        10.0,
        100.0,
        200.0,
    )
    content = json.loads(theta_path.read_text())
    assert content == {
        "theta0": pytest.approx(1.0),
        "theta1": pytest.approx(2.0),
        "min_km": pytest.approx(0.0),
        "max_km": pytest.approx(10.0),
        "min_price": pytest.approx(100.0),
        "max_price": pytest.approx(200.0),
    }


def test_save_theta_omits_none_bounds(tmp_path: Path) -> None:
    theta_path = tmp_path / "theta.json"
    save_theta(1.0, 2.0, theta_path, min_km=0.0)
    content = json.loads(theta_path.read_text())
    assert content == {
        "theta0": pytest.approx(1.0),
        "theta1": pytest.approx(2.0),
        "min_km": pytest.approx(0.0),
    }
