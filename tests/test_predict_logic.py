import json
from pathlib import Path

import pytest

from predict.predict import load_theta, predict_price


def test_load_theta_missing_and_predict(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    theta_path = tmp_path / "theta.json"
    theta0, theta1, *_ = load_theta(str(theta_path))
    assert (theta0, theta1) == (0.0, 0.0)
    assert capsys.readouterr().out == ""

    price = predict_price(123.0, str(theta_path))
    assert price == pytest.approx(0.0)
    assert capsys.readouterr().out == ""


def test_predict_price_with_file(tmp_path: Path) -> None:
    theta_path = tmp_path / "theta.json"
    theta_path.write_text(json.dumps({"theta0": 1.5, "theta1": 2.0}))
    theta0, theta1, *_ = load_theta(str(theta_path))
    assert theta0 == pytest.approx(1.5)
    assert theta1 == pytest.approx(2.0)
    assert predict_price(3.0, str(theta_path)) == pytest.approx(1.5 + 2.0 * 3.0)


def test_load_theta_invalid_json(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    theta_path = tmp_path / "theta.json"
    theta_path.write_text("not json")
    with pytest.raises(SystemExit) as exc:
        load_theta(str(theta_path))
    assert exc.value.code == 2
    assert (
        capsys.readouterr().out.strip() == f"ERROR: invalid theta file: {theta_path}"
    )


def test_load_theta_missing_keys(tmp_path: Path) -> None:
    theta_path = tmp_path / "theta.json"
    theta_path.write_text(json.dumps({"theta0": 2.5}))
    assert load_theta(str(theta_path))[:2] == (2.5, 0.0)
    theta_path.write_text(json.dumps({"theta1": 3.5}))
    assert load_theta(str(theta_path))[:2] == (0.0, 3.5)


@pytest.mark.parametrize(
    "theta0,theta1,km,expected",
    [
        (1.0, 0.0, 3.0, 1.0),
        (0.0, 1.0, 3.0, 3.0),
    ],
)
def test_predict_price_single_theta(
    tmp_path: Path, theta0: float, theta1: float, km: float, expected: float
) -> None:
    theta_path = tmp_path / "theta.json"
    theta_path.write_text(json.dumps({"theta0": theta0, "theta1": theta1}))
    assert predict_price(km, str(theta_path)) == pytest.approx(expected)


def test_predict_price_zero_theta(tmp_path: Path) -> None:
    theta_path = tmp_path / "theta.json"
    theta_path.write_text(json.dumps({"theta0": 0.0, "theta1": 0.0}))
    assert predict_price(10.0, str(theta_path)) == pytest.approx(0.0)


def test_predict_price_default_theta_path(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    theta_path = tmp_path / "theta.json"
    theta_path.write_text(json.dumps({"theta0": 1.0, "theta1": 1.0}))
    monkeypatch.chdir(tmp_path)
    assert predict_price(2.0) == pytest.approx(3.0)


def test_load_theta_invalid_values(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    theta_path = tmp_path / "theta.json"
    theta_path.write_text(json.dumps({"theta0": "bad"}))
    with pytest.raises(SystemExit) as exc:
        load_theta(str(theta_path))
    assert exc.value.code == 2
    assert (
        capsys.readouterr().out.strip()
        == f"ERROR: invalid theta values in {theta_path}"
    )


def test_predict_price_warns_outside_bounds(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    theta_path = tmp_path / "theta.json"
    theta_path.write_text(
        json.dumps(
            {
                "theta0": 0.0,
                "theta1": 1.0,
                "min_km": 0.0,
                "max_km": 10.0,
                "min_price": 0.0,
                "max_price": 10.0,
            }
        )
    )
    price = predict_price(20.0, str(theta_path))
    out = capsys.readouterr().out
    assert price == pytest.approx(20.0)
    assert "WARNING: mileage 20.0 outside data range [0.0, 10.0]" in out
    assert "WARNING: price 20.0 outside data range [0.0, 10.0]" in out


def test_predict_price_no_warning_at_bounds(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    theta_path = tmp_path / "theta.json"
    theta_path.write_text(
        json.dumps(
            {
                "theta0": 0.0,
                "theta1": 1.0,
                "min_km": 0.0,
                "max_km": 10.0,
                "min_price": 0.0,
                "max_price": 10.0,
            }
        )
    )
    predict_price(0.0, str(theta_path))
    assert capsys.readouterr().out == ""
    predict_price(10.0, str(theta_path))
    assert capsys.readouterr().out == ""


def test_predict_price_partial_bounds(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    theta_path = tmp_path / "theta.json"
    # Only mileage lower bound provided
    theta_path.write_text(json.dumps({"theta0": 0.0, "theta1": 1.0, "min_km": 0.0}))
    predict_price(20.0, str(theta_path))
    assert capsys.readouterr().out == ""
    # Only price lower bound provided
    theta_path.write_text(json.dumps({"theta0": 0.0, "theta1": 1.0, "min_price": 0.0}))
    predict_price(20.0, str(theta_path))
    assert capsys.readouterr().out == ""
