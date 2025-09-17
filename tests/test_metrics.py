import json
import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from metrics import evaluate, read_theta  # noqa: E402


def test_evaluate_perfect_fit(tmp_path: Path) -> None:
    data = tmp_path / "data.csv"
    data.write_text("km,price\n0,0\n1,2\n")
    theta = tmp_path / "theta.json"
    theta.write_text(json.dumps({"theta0": 0.0, "theta1": 2.0}))
    rmse, r2 = evaluate(data, theta)
    assert rmse == pytest.approx(0.7071067811865476)
    assert r2 == pytest.approx(0.5)


def test_evaluate_nonperfect(tmp_path: Path) -> None:
    data = tmp_path / "data.csv"
    data.write_text("km,price\n0,0\n1,3\n")
    theta = tmp_path / "theta.json"
    theta.write_text(json.dumps({"theta0": 0.0, "theta1": 0.0}))
    rmse, r2 = evaluate(data, theta)
    assert rmse == pytest.approx(1.4142135623730951)
    assert r2 == pytest.approx(0.11111111111111116)


def test_evaluate_constant_prices(tmp_path: Path) -> None:
    data = tmp_path / "data.csv"
    data.write_text("km,price\n0,1\n1,1\n")
    theta = tmp_path / "theta.json"
    theta.write_text(json.dumps({"theta0": 1.0, "theta1": 0.0}))
    rmse, r2 = evaluate(data, theta)
    assert rmse == pytest.approx(0.7071067811865476)
    assert r2 == 1.0


def test_evaluate_small_variance_not_constant(tmp_path: Path) -> None:
    data = tmp_path / "data.csv"
    data.write_text("km,price\n0,0.0\n1,0.5\n")
    theta = tmp_path / "theta.json"
    theta.write_text(json.dumps({"theta0": 0.0, "theta1": 0.0}))
    rmse, r2 = evaluate(data, theta)
    assert rmse == pytest.approx(0.3535533905932738)
    assert r2 == pytest.approx(-1.0)


def test_evaluate_almost_constant_variance(tmp_path: Path) -> None:
    data = tmp_path / "data.csv"
    data.write_text("km,price\n0,1.0\n0,1.0000000000001\n")
    theta = tmp_path / "theta.json"
    theta.write_text(json.dumps({"theta0": 1.0, "theta1": 1.0}))
    rmse, r2 = evaluate(data, theta)
    assert rmse == pytest.approx(7.071067811865475e-14)
    assert r2 == 1.0


def test_read_theta_missing(tmp_path: Path) -> None:
    theta = tmp_path / "missing.json"
    with pytest.raises(ValueError, match=f"theta file not found: {theta}"):
        read_theta(theta)


def test_read_theta_invalid_values(tmp_path: Path) -> None:
    theta = tmp_path / "theta.json"
    theta.write_text("{}")
    with pytest.raises(ValueError, match=f"invalid theta values in {theta}"):
        read_theta(theta)
