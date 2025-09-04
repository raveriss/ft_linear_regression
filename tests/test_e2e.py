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

    result_train = subprocess.run(
        [
            sys.executable,
            "-m",
            "src.train",
            "--data",
            str(data_path),
            "--alpha",
            "0.1",
            "--iters",
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
    price_after = float(result_predict_after.stdout.strip().split()[-2])
    assert price_after == pytest.approx(5305.823492473339, rel=1e-2)

    theta_path.unlink(missing_ok=True)
    assert not theta_path.exists()
