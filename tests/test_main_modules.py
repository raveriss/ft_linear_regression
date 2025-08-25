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
    assert result["theta0"] == pytest.approx(1.0)
    assert result["theta1"] == pytest.approx(0.0)
    assert result["min_km"] == pytest.approx(1.0)
    assert result["max_km"] == pytest.approx(1.0)
    assert result["min_price"] == pytest.approx(1.0)
    assert result["max_price"] == pytest.approx(1.0)


def test_predict_main_runs(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    theta = tmp_path / "theta.json"
    theta.write_text(json.dumps({"theta0": 1.0, "theta1": 2.0}))
    assert predict_main(["--km", "3", "--theta", str(theta)]) == 0
    captured = capsys.readouterr()
    assert float(captured.out.strip()) == pytest.approx(7.0)


def test_predict_main_system_exit_str(monkeypatch: pytest.MonkeyPatch) -> None:
    def fake_parse_args(_argv: list[str] | None = None) -> tuple[float, str]:
        raise SystemExit("boom")

    monkeypatch.setattr("predict.__main__.parse_args", fake_parse_args)
    assert predict_main([]) == 1


def test_train_main_missing_csv(capsys: pytest.CaptureFixture[str]) -> None:
    code = train_main(["--data", "missing.csv"])
    captured = capsys.readouterr()
    assert code == 2
    assert "ERROR: data file not found: missing.csv" in captured.out


def test_train_main_learns_line(tmp_path: Path) -> None:
    data = tmp_path / "data.csv"
    data.write_text("km,price\n2,2\n4,4\n")
    theta = tmp_path / "theta.json"
    assert (
        train_main(
            [
                "--data",
                str(data),
                "--alpha",
                "0.1",
                "--iters",
                "1000",
                "--theta",
                str(theta),
            ]
        )
        == 0
    )
    result = json.loads(theta.read_text())
    assert result["theta0"] == pytest.approx(0.0, abs=1e-2)
    assert result["theta1"] == pytest.approx(1.0, abs=1e-2)
