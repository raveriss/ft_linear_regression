import json
from pathlib import Path

import pytest

from predict.predict import (
    _parse_float,
    _parse_optional_float,
    load_theta,
)
from train.train import save_theta


def test_save_and_load_theta(tmp_path: Path) -> None:
    theta_path = tmp_path / "theta.json"
    save_theta(1.0, 2.0, theta_path)
    theta0, theta1, *_ = load_theta(str(theta_path))
    assert theta0 == pytest.approx(1.0)
    assert theta1 == pytest.approx(2.0)


def test_load_theta_invalid_json(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    theta_path = tmp_path / "theta.json"
    theta_path.write_text("not json")
    with pytest.raises(SystemExit) as exc:
        load_theta(str(theta_path))
    assert exc.value.code == 2
    assert capsys.readouterr().out.strip() == f"ERROR: invalid theta file: {theta_path}"


def test_load_theta_missing_values(tmp_path: Path) -> None:
    theta_path = tmp_path / "theta.json"
    theta_path.write_text(json.dumps({"theta0": 3.0}))
    theta0, theta1, *_ = load_theta(str(theta_path))
    assert theta0 == pytest.approx(3.0)
    assert theta1 == pytest.approx(0.0)


def test_load_theta_nondict_json(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    theta_path = tmp_path / "theta.json"
    theta_path.write_text(json.dumps([1, 2, 3]))
    with pytest.raises(SystemExit) as exc:
        load_theta(str(theta_path))
    assert exc.value.code == 2
    assert (
        capsys.readouterr().out.strip()
        == f"ERROR: invalid theta file: {theta_path}"
    )


def test_parse_float_asserts_path() -> None:
    with pytest.raises(AssertionError):
        _parse_float(0.0, None)  # type: ignore[arg-type]


def test_parse_optional_float_asserts_path() -> None:
    with pytest.raises(AssertionError):
        _parse_optional_float(0.0, None)  # type: ignore[arg-type]
