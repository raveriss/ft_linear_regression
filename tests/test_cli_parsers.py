import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from predict.predict import build_parser as build_predict_parser  # noqa: E402
from predict.predict import parse_args as parse_predict_args  # noqa: E402
from train.__main__ import build_parser as build_train_parser  # noqa: E402


def test_predict_parser_definition() -> None:
    parser = build_predict_parser()
    assert parser.description == "Predict a car price from mileage"
    km_action = next(a for a in parser._actions if a.dest == "km")
    theta_action = next(a for a in parser._actions if a.dest == "theta")
    assert km_action.option_strings == ["--km"]
    assert km_action.help == "mileage in kilometers"
    assert theta_action.option_strings == ["--theta"]
    assert theta_action.help == "path to theta JSON"

    args = parser.parse_args(["--km", "12.5"])
    assert isinstance(args.km, float)
    assert args.km == pytest.approx(12.5)
    assert args.theta == "theta.json"

    args2 = parser.parse_args(["--theta", "file.json"])
    assert args2.theta == "file.json" and args2.km is None

    with pytest.raises(SystemExit):
        parser.parse_args(["--km", "oops"])


def test_parse_args_with_explicit_values() -> None:
    km, theta = parse_predict_args(["--km", "5", "--theta", "file.json"])
    assert km == pytest.approx(5.0)
    assert theta == "file.json"


def test_parse_args_interactive(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    # Simulate running without CLI arguments and with invalid then valid input
    monkeypatch.setattr(sys, "argv", ["predict"])
    inputs = iter(["bad", "42"])
    prompts: list[str] = []

    def fake_input(prompt: str) -> str:
        prompts.append(prompt)
        return next(inputs)

    monkeypatch.setattr("builtins.input", fake_input)
    km, theta = parse_predict_args()
    out = capsys.readouterr().out
    assert prompts == ["Enter mileage: ", "Enter mileage: "]
    assert out == "Invalid mileage. Please enter a number.\n"
    assert km == pytest.approx(42.0)
    assert theta == "theta.json"


def test_train_parser_definition() -> None:
    parser = build_train_parser()
    assert parser.description == "Train the linear regression model"
    actions = {a.dest: a for a in parser._actions}
    assert actions["data"].option_strings == ["--data"]
    assert actions["data"].help == "path to training data CSV"
    assert actions["data"].required is True
    assert actions["alpha"].option_strings == ["--alpha"]
    help_text = actions["alpha"].help or ""
    assert help_text.startswith("learning rate")
    assert actions["alpha"].required is False
    assert actions["alpha"].default == pytest.approx(0.1)
    assert actions["iters"].option_strings == ["--iters"]
    assert actions["iters"].help == "number of iterations"
    assert actions["iters"].required is False
    assert actions["iters"].default == 1000
    assert actions["theta"].option_strings == ["--theta"]
    assert actions["theta"].help == "path to theta JSON"
    assert actions["theta"].required is False

    args = parser.parse_args(["--data", "data.csv"])
    assert args.data == "data.csv"
    assert args.alpha == pytest.approx(0.1)
    assert args.iters == 1000
    assert args.theta == "theta.json"

    args2 = parser.parse_args(
        ["--data", "d", "--alpha", "0.5", "--iters", "10", "--theta", "t.json"]
    )
    assert args2.alpha == pytest.approx(0.5)
    assert args2.iters == 10
    assert args2.theta == "t.json"

    # boundary value should be accepted
    args3 = parser.parse_args(["--data", "d", "--alpha", "1"])
    assert args3.alpha == pytest.approx(1.0)

    with pytest.raises(SystemExit):
        parser.parse_args(["--data", "d", "--alpha", "0"])
    with pytest.raises(SystemExit):
        parser.parse_args(["--data", "d", "--alpha", "2"])
    with pytest.raises(SystemExit):
        parser.parse_args(["--data", "d", "--alpha", "bad"])
    with pytest.raises(SystemExit):
        parser.parse_args(["--data", "d", "--iters", "bad"])
    with pytest.raises(SystemExit):
        parser.parse_args(["--alpha", "0.1", "--iters", "10"])


def test_alpha_type_error_messages(capsys: pytest.CaptureFixture[str]) -> None:
    parser = build_train_parser()
    with pytest.raises(SystemExit):
        parser.parse_args(["--data", "d", "--alpha", "bad"])
    err = capsys.readouterr().err
    assert err.strip().endswith("alpha must be a floating point number")
    with pytest.raises(SystemExit):
        parser.parse_args(["--data", "d", "--alpha", "2"])
    err = capsys.readouterr().err
    assert err.strip().endswith("alpha must be in the range (0, 1]")
