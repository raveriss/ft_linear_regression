import json
import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from predict.__main__ import main as predict_main  # noqa: E402
from train.__main__ import main as train_main  # noqa: E402


def test_train_main_runs(tmp_path: Path) -> None:
    data = tmp_path / "data.csv"
    data.write_text("km,price\n1,1\n")
    theta = tmp_path / "theta.json"
    assert (
        train_main(
            [
                "--data",
                str(data),
                "--alpha",
                "0.1",
                "--iters",
                "1",
                "--theta",
                str(theta),
            ]
        )
        == 0
    )
    result = json.loads(theta.read_text())
    assert result["theta0"] == pytest.approx(0.1)
    assert result["theta1"] == pytest.approx(0.1)
    assert result["min_km"] == pytest.approx(1.0)
    assert result["max_km"] == pytest.approx(1.0)
    assert result["min_price"] == pytest.approx(1.0)
    assert result["max_price"] == pytest.approx(1.0)


def test_predict_main_runs(capsys: pytest.CaptureFixture[str]) -> None:
    assert predict_main([]) == 0
    captured = capsys.readouterr()
    assert "not yet implemented" in captured.out.lower()


def test_train_main_missing_csv(capsys: pytest.CaptureFixture[str]) -> None:
    code = train_main(["--data", "missing.csv"])
    captured = capsys.readouterr()
    assert code == 2
    assert "ERROR: data file not found: missing.csv" in captured.out
