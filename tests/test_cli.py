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
    actions = {a.dest: a for a in parser._actions}
    km_action = actions["km"]
    theta_action = actions["theta"]
    assert km_action.option_strings == []
    assert km_action.help == "mileage in kilometers"
    assert theta_action.option_strings == ["--theta"]
    assert theta_action.help == "path to theta JSON"

    args = parser.parse_args(["12.5"])
    assert isinstance(args.km, float)
    assert args.km == pytest.approx(12.5)
    assert args.theta == "theta.json"

    args2 = parser.parse_args(["--theta", "file.json"])
    assert args2.theta == "file.json" and args2.km is None

    with pytest.raises(SystemExit):
        parser.parse_args(["oops"])


def test_parse_args_with_explicit_values(
    capsys: pytest.CaptureFixture[str],
) -> None:
    km, theta = parse_predict_args(["5", "--theta", "file.json"])
    assert km == pytest.approx(5.0)
    assert theta == "file.json"
    km_zero, _ = parse_predict_args(["0"])
    assert km_zero == pytest.approx(0.0)
    capsys.readouterr()
    with pytest.raises(SystemExit) as exc:
        parse_predict_args(["-1"])
    assert exc.value.code == 2
    assert (
        capsys.readouterr().out.strip()
        == "ERROR: invalid mileage (must be a non-negative number)"
    )


def test_parse_args_interactive(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    # Simulate running without CLI arguments and with invalid then valid input
    monkeypatch.setattr(sys, "argv", ["predict"])
    inputs = iter(["bad", "-1", "0"])
    prompts: list[str] = []

    def fake_input(prompt: str) -> str:
        prompts.append(prompt)
        return next(inputs)

    monkeypatch.setattr("builtins.input", fake_input)
    km, theta = parse_predict_args()
    out = capsys.readouterr().out
    assert prompts == ["Enter mileage: ", "Enter mileage: ", "Enter mileage: "]
    assert out == (
        "Invalid mileage. Please enter a number.\n"
        "Invalid mileage. Must be a non-negative number.\n"
    )
    assert km == pytest.approx(0.0)
    assert theta == "theta.json"


def test_parse_args_default_km() -> None:
    km, theta = parse_predict_args(["--theta", "file.json"])
    assert km == pytest.approx(0.0)
    assert theta == "file.json"


def test_parse_args_too_many(capsys: pytest.CaptureFixture[str]) -> None:
    with pytest.raises(SystemExit) as exc:
        parse_predict_args(["1", "2"])
    assert exc.value.code == 2
    out = capsys.readouterr().out.strip().splitlines()
    assert out == [
        "Too many arguments",
        "Usage:",
        "  make predict            # interactive",
        "  make predict <km>       # direct prediction",
        "  make train              # train the model",
    ]


def test_train_parser_definition() -> None:
    parser = build_train_parser()
    assert parser.description == "Train the linear regression model"
    actions = {a.dest: a for a in parser._actions}
    assert actions["data"].option_strings == ["--data"]
    assert actions["data"].help == "path to training data CSV"
    assert actions["data"].required is True
    # Doit au minimum exposer --alpha, tolère des alias additionnels
    assert "--alpha" in actions["alpha"].option_strings
    help_text = actions["alpha"].help or ""
    assert help_text.startswith("learning rate")
    assert actions["alpha"].required is False
    assert actions["alpha"].default == pytest.approx(0.1)
    # Doit au minimum exposer --iters, tolère des alias additionnels
    assert "--iters" in actions["iters"].option_strings
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
        parser.parse_args(["--data", "d", "--iters", "0"])
    with pytest.raises(SystemExit):
        parser.parse_args(["--data", "d", "--iters", "-1"])
    with pytest.raises(SystemExit):
        parser.parse_args(["--alpha", "0.1", "--iters", "10"])


def test_train_parser_aliases() -> None:
    parser = build_train_parser()
    args = parser.parse_args(
        ["--data", "d", "--taux-apprentissage", "0.3", "--nb-iterations", "7"]
    )
    assert args.alpha == pytest.approx(0.3)
    assert args.iters == 7


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


def test_iters_type_error_messages(capsys: pytest.CaptureFixture[str]) -> None:
    parser = build_train_parser()
    with pytest.raises(SystemExit):
        parser.parse_args(["--data", "d", "--iters", "bad"])
    err = capsys.readouterr().err
    assert err.strip().endswith("iters must be a positive integer")
    with pytest.raises(SystemExit):
        parser.parse_args(["--data", "d", "--iters", "0"])
    err = capsys.readouterr().err
    assert err.strip().endswith("iters must be a positive integer")
