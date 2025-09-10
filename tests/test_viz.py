import json
import sys
from pathlib import Path
from typing import Any, Iterable

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
    calls: dict[str, Any] = {
        "scatter": False,
        "plot_rl": None,
        "show": False,
        "eval": None,
        "suptitle": None,
        "vlines": 0,
        "axhlines": [],
        "fill_between": 0,
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

    def fake_vlines(*args: object, **kwargs: object) -> None:
        calls["vlines"] += 1

    def fake_axhline(y: float, *, label: str, **_: object) -> None:
        calls["axhlines"].append((y, label))

    def fake_fill_between(*_: object, **__: object) -> None:
        calls["fill_between"] += 1

    class FakeAx:
        def get_legend_handles_labels(self) -> tuple[list[object], list[str]]:
            return ([], [])

    monkeypatch.setattr(plt, "scatter", fake_scatter)
    monkeypatch.setattr(plt, "show", fake_show)
    monkeypatch.setattr(plt, "gca", lambda: FakeAx())
    monkeypatch.setattr(plt, "xlabel", lambda *a, **k: None)
    monkeypatch.setattr(plt, "ylabel", lambda *a, **k: None)
    monkeypatch.setattr(plt, "suptitle", fake_suptitle)
    monkeypatch.setattr(plt, "vlines", fake_vlines)
    monkeypatch.setattr(plt, "axhline", fake_axhline)
    monkeypatch.setattr(plt, "fill_between", fake_fill_between)
    monkeypatch.setattr(viz, "plot_regression_line", fake_plot_reg_line)
    monkeypatch.setattr(viz, "evaluate", fake_eval)

    data = tmp_path / "data.csv"
    data.write_text("km,price\n0,1\n1,1\n2,1\n")
    theta = tmp_path / "theta.json"
    theta.write_text(json.dumps({"theta0": 1.0, "theta1": 0.0}))

    viz.main(["--data", str(data), "--theta", str(theta)])
    assert calls == {
        "scatter": True,
        "plot_rl": True,
        "show": True,
        "eval": (str(data), str(theta)),
        "suptitle": "RMSE: 0.00, R2: 1.00",
        "vlines": 0,
        "axhlines": [(1.0, "moyenne(prix)")],
        "fill_between": 0,
    }

    calls.update(
        {
            "scatter": False,
            "plot_rl": None,
            "show": False,
            "eval": None,
            "suptitle": None,
            "vlines": 0,
            "axhlines": [],
            "fill_between": 0,
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
        "vlines": 0,
        "axhlines": [(1.0, "moyenne(prix)")],
        "fill_between": 0,
    }

    calls.update(
        {
            "scatter": False,
            "plot_rl": None,
            "show": False,
            "eval": None,
            "suptitle": None,
            "vlines": 0,
            "axhlines": [],
            "fill_between": 0,
        }
    )
    viz.main(
        [
            "--data",
            str(data),
            "--theta",
            str(theta),
            "--show-residuals",
        ]
    )
    assert calls == {
        "scatter": True,
        "plot_rl": True,
        "show": True,
        "eval": (str(data), str(theta)),
        "suptitle": "RMSE: 0.00, R2: 1.00",
        "vlines": 3,
        "axhlines": [(1.0, "moyenne(prix)")],
        "fill_between": 0,
    }

    calls.update(
        {
            "scatter": False,
            "plot_rl": None,
            "show": False,
            "eval": None,
            "suptitle": None,
            "vlines": 0,
            "axhlines": [],
            "fill_between": 0,
        }
    )
    viz.main(
        [
            "--data",
            str(data),
            "--theta",
            str(theta),
            "--show-median",
        ]
    )
    assert calls == {
        "scatter": True,
        "plot_rl": True,
        "show": True,
        "eval": (str(data), str(theta)),
        "suptitle": "RMSE: 0.00, R2: 1.00",
        "vlines": 0,
        "axhlines": [(1.0, "moyenne(prix)"), (1.0, "mediane(prix)")],
        "fill_between": 0,
    }

    calls.update(
        {
            "scatter": False,
            "plot_rl": None,
            "show": False,
            "eval": None,
            "suptitle": None,
            "vlines": 0,
            "axhlines": [],
            "fill_between": 0,
        }
    )
    viz.main(
        [
            "--data",
            str(data),
            "--theta",
            str(theta),
            "--confidence",
        ]
    )
    assert calls == {
        "scatter": True,
        "plot_rl": True,
        "show": True,
        "eval": (str(data), str(theta)),
        "suptitle": "RMSE: 0.00, R2: 1.00",
        "vlines": 0,
        "axhlines": [(1.0, "moyenne(prix)")],
        "fill_between": 1,
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


def test_highlight_outliers(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    plt = pytest.importorskip("matplotlib.pyplot")
    calls: list[dict[str, Any]] = []

    def fake_scatter(x: Iterable[float], y: Iterable[float], **kwargs: Any) -> None:
        calls.append({"x": list(x), "y": list(y), "kwargs": kwargs})

    class FakeAx:
        def get_legend_handles_labels(self) -> tuple[list[object], list[str]]:
            return ([], [])

    monkeypatch.setattr(plt, "scatter", fake_scatter)
    monkeypatch.setattr(plt, "show", lambda: None)
    monkeypatch.setattr(plt, "legend", lambda *a, **k: None)
    monkeypatch.setattr(plt, "gca", lambda: FakeAx())
    monkeypatch.setattr(plt, "xlabel", lambda *a, **k: None)
    monkeypatch.setattr(plt, "ylabel", lambda *a, **k: None)
    monkeypatch.setattr(plt, "suptitle", lambda *a, **k: None)
    monkeypatch.setattr(plt, "axhline", lambda *a, **k: None)
    monkeypatch.setattr(viz, "plot_regression_line", lambda *a, **k: None)
    monkeypatch.setattr(viz, "evaluate", lambda *a, **k: (0.0, 0.0))

    data = tmp_path / "data.csv"
    data.write_text("km,price\n0,0\n1,1\n2,2\n3,3\n4,4\n5,20\n")
    theta = tmp_path / "theta.json"
    theta.write_text(json.dumps({"theta0": 0.0, "theta1": 1.0}))

    viz.main(["--data", str(data), "--theta", str(theta)])

    assert len(calls) == 2
    assert calls[0]["kwargs"].get("label") == "donnees"
    assert calls[1]["kwargs"].get("label") == "outliers"
    assert calls[1]["kwargs"].get("color") == "orange"


def test_plot_confidence_band_identical_points(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    plt = pytest.importorskip("matplotlib.pyplot")
    called = {"fill_between": False}

    def fake_fill_between(*_: object, **__: object) -> None:
        called["fill_between"] = True

    monkeypatch.setattr(plt, "fill_between", fake_fill_between)
    xs = [50000.0] * 5
    data = [(50000.0, 10000.0)] * 5
    viz.plot_confidence_band(plt, xs, data, 0.0, 0.0, 0.95)
    assert not called["fill_between"]
