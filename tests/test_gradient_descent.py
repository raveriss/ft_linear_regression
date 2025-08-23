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
