import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
if not (ROOT / "src/metrics.py").exists():
    ROOT = ROOT.parent
sys.path.append(str(ROOT / "src"))

from metrics import main as accuracy_main  # noqa: E402


def test_accuracy_main_outputs(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    data = tmp_path / "data.csv"
    data.write_text("km,price\n0,0\n1,2\n")
    theta = tmp_path / "theta.json"
    theta.write_text(json.dumps({"theta0": 0.0, "theta1": 2.0}))

    monkeypatch.chdir(tmp_path)
    accuracy_main()
    out = capsys.readouterr().out
    rmse_line, r2_line = out.strip().splitlines()
    rmse = float(rmse_line.split(": ")[1])
    r2 = float(r2_line.split(": ")[1])
    assert rmse == pytest.approx(0.7071067811865476)
    assert r2 == pytest.approx(0.5)
