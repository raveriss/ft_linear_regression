"""End-to-end tests for the CLI entry points."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

import pytest


def test_predict_then_train(tmp_path: Path) -> None:
    """Run predict and train commands sequentially and verify their outputs."""

    theta_path = tmp_path / "theta.json"

    project_root = Path(__file__).resolve().parent.parent
    repo_root = project_root.parent if project_root.name == "mutants" else project_root
    data_path = repo_root / "data/samples/data.csv"

    env = {k: v for k, v in os.environ.items() if not k.startswith("MUTMUT_")}
    original_path = env.get("PYTHONPATH", "")
    cleaned = [
        p
        for p in original_path.split(os.pathsep)
        if "mutants" not in p and ".mutmut-cache" not in p and p
    ]
    env["PYTHONPATH"] = os.pathsep.join(
        [str(repo_root), str(repo_root / "src"), *cleaned]
    )

    # prédiction initiale
    result_predict = subprocess.run(
        [
            sys.executable,
            "-m",
            "src.predict",
            "0",
            "--theta",
            str(theta_path),
        ],
        capture_output=True,
        text=True,
        env=env,
        cwd=str(repo_root),
    )
    assert result_predict.returncode == 0
    assert result_predict.stdout.strip() == "0"

    # entraînement avec tes nouveaux noms
    result_train = subprocess.run(
        [
            sys.executable,
            "-m",
            "src.train",
            "--data",
            str(data_path),
            "--taux-apprentissage",
            "0.1",
            "--nb-iterations",
            "10",
            "--theta",
            str(theta_path),
        ],
        capture_output=True,
        text=True,
        env=env,
        cwd=str(repo_root),
    )
    assert result_train.returncode == 0
    assert result_train.stdout == ""
    assert theta_path.exists()

    # prédiction après entraînement
    result_predict_after = subprocess.run(
        [
            sys.executable,
            "-m",
            "src.predict",
            "0",
            "--theta",
            str(theta_path),
        ],
        capture_output=True,
        text=True,
        env=env,
        cwd=str(repo_root),
    )
    assert result_predict_after.returncode == 0
    # Prix affiché par le binaire
    price_after = float(result_predict_after.stdout.strip().split()[-2])

    # Attendu déterministe sans import du package:
    # la prédiction pour km=0 est exactement theta0 sauvegardé.
    import json

    with open(theta_path, "r", encoding="utf-8") as f:
        thetas = json.load(f)
    expected_price = float(thetas["theta0"])
    assert price_after == pytest.approx(expected_price, rel=1e-6)

    theta_path.unlink(missing_ok=True)
    assert not theta_path.exists()
