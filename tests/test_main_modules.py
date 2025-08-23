import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from predict.__main__ import main as predict_main  # noqa: E402
from train.__main__ import main as train_main  # noqa: E402


def test_train_main_runs(capsys: pytest.CaptureFixture[str]) -> None:
    assert train_main([]) == 0
    captured = capsys.readouterr()
    assert "not yet implemented" in captured.out.lower()


def test_predict_main_runs(capsys: pytest.CaptureFixture[str]) -> None:
    assert predict_main([]) == 0
    captured = capsys.readouterr()
    assert "not yet implemented" in captured.out.lower()
