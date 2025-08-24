from pathlib import Path
import json
import pytest

from train.train import save_theta
from predict.predict import load_theta


def test_save_and_load_theta(tmp_path: Path) -> None:
    theta_path = tmp_path / "theta.json"
    save_theta(1.0, 2.0, theta_path)
    theta0, theta1, *_ = load_theta(str(theta_path))
    assert theta0 == pytest.approx(1.0)
    assert theta1 == pytest.approx(2.0)


def test_load_theta_invalid_json(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    theta_path = tmp_path / "theta.json"
    theta_path.write_text("not json")
    with pytest.raises(SystemExit) as exc:
        load_theta(str(theta_path))
    assert exc.value.code == 2
    assert (
        capsys.readouterr().out.strip()
        == f"ERROR: theta file not found: {theta_path}"
    )


def test_load_theta_missing_values(tmp_path: Path) -> None:
    theta_path = tmp_path / "theta.json"
    theta_path.write_text(json.dumps({"theta0": 3.0}))
    theta0, theta1, *_ = load_theta(str(theta_path))
    assert theta0 == pytest.approx(3.0)
    assert theta1 == pytest.approx(0.0)
