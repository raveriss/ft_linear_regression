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
    calls = {
        "scatter": False,
        "plot_rl": None,
        "show": False,
        "eval": None,
        "suptitle": None,
    }

    def fake_scatter(*args: object, **kwargs: object) -> None:
        calls["scatter"] = True

    def fake_show() -> None:
        calls["show"] = True

    def fake_plot_reg_line(
        ax: object,
        xs: object,
        theta0: float,
        theta1: float,
        show_eq: bool,
    ) -> None:
        calls["plot_rl"] = show_eq

    def fake_eval(data_path: str, theta_path: str) -> tuple[float, float]:
        calls["eval"] = (data_path, theta_path)
        return 0.0, 1.0

    def fake_suptitle(text: str) -> None:
        calls["suptitle"] = text

    class FakeAx:
        def get_legend_handles_labels(self) -> tuple[list[object], list[str]]:
            return ([], [])

    monkeypatch.setattr(plt, "scatter", fake_scatter)
    monkeypatch.setattr(plt, "show", fake_show)
    monkeypatch.setattr(plt, "gca", lambda: FakeAx())
    monkeypatch.setattr(plt, "xlabel", lambda *a, **k: None)
    monkeypatch.setattr(plt, "ylabel", lambda *a, **k: None)
    monkeypatch.setattr(plt, "suptitle", fake_suptitle)
    monkeypatch.setattr(viz, "plot_regression_line", fake_plot_reg_line)
    monkeypatch.setattr(viz, "evaluate", fake_eval)

    data = tmp_path / "data.csv"
    data.write_text("km,price\n0,1\n1,1\n")
    theta = tmp_path / "theta.json"
    theta.write_text(json.dumps({"theta0": 1.0, "theta1": 0.0}))

    viz.main(["--data", str(data), "--theta", str(theta)])
    assert calls == {
        "scatter": True,
        "plot_rl": True,
        "show": True,
        "eval": (str(data), str(theta)),
        "suptitle": "RMSE: 0.00, R2: 1.00",
    }

    calls.update(
        {
            "scatter": False,
            "plot_rl": None,
            "show": False,
            "eval": None,
            "suptitle": None,
        }
    )
    viz.main(
        ["--data", str(data), "--theta", str(theta), "--no-show-eq"],
    )
    assert calls == {
        "scatter": True,
        "plot_rl": False,
        "show": True,
        "eval": (str(data), str(theta)),
        "suptitle": "RMSE: 0.00, R2: 1.00",
    }


def test_plot_regression_line(monkeypatch: pytest.MonkeyPatch) -> None:
    calls: dict[str, object] = {"plot": False, "annotate": None}

    class FakeAx:
        def plot(self, *_: object, **__: object) -> None:
            calls["plot"] = True

        def annotate(self, text: str, *_: object, **__: object) -> None:
            calls["annotate"] = text

        def get_legend_handles_labels(self) -> tuple[list[object], list[str]]:
            return ([], [])

    ax = FakeAx()
    xs = [0.0, 1.0]
    viz.plot_regression_line(ax, xs, 1.234, 2.345, True)
    assert calls["plot"]
    assert calls["annotate"] == "price = 1.23 + 2.35 * km"

    calls.update({"plot": False, "annotate": None})
    viz.plot_regression_line(ax, xs, 1.0, 2.0, False)
    assert calls["plot"]
    assert calls["annotate"] is None
