import json
import sys
from pathlib import Path

import pytest

pytest.importorskip("matplotlib")

ROOT = Path(__file__).resolve().parents[1]
if not (ROOT / "src/viz.py").exists():
    ROOT = ROOT.parent
sys.path.append(str(ROOT / "src"))

import viz  # noqa: E402
from linear_regression import estimatePrice  # noqa: E402


def test_line_points() -> None:
    xs = [1.0, 3.0, 2.0]
    theta0, theta1 = 0.5, 2.0
    line_x, line_y = viz._line_points(xs, theta0, theta1)
    assert line_x == [1.0, 3.0]
    assert line_y == [
        estimatePrice(1.0, theta0, theta1),
        estimatePrice(3.0, theta0, theta1),
    ]


def test_main_plots(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    plt = pytest.importorskip("matplotlib.pyplot")
    calls = {"scatter": False, "plot": False, "show": False}

    def fake_scatter(*args: object, **kwargs: object) -> None:
        calls["scatter"] = True

    def fake_plot(*args: object, **kwargs: object) -> None:
        calls["plot"] = True

    def fake_show() -> None:
        calls["show"] = True

    monkeypatch.setattr(plt, "scatter", fake_scatter)
    monkeypatch.setattr(plt, "plot", fake_plot)
    monkeypatch.setattr(plt, "show", fake_show)

    data = tmp_path / "data.csv"
    data.write_text("km,price\n0,0\n1,1\n")
    theta = tmp_path / "theta.json"
    theta.write_text(json.dumps({"theta0": 0.0, "theta1": 1.0}))

    viz.main(["--data", str(data), "--theta", str(theta)])

    assert calls["scatter"]
    assert calls["plot"]
    assert calls["show"]
