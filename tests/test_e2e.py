"""End-to-end tests for the CLI entry points."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path


def test_predict_then_train(tmp_path: Path) -> None:
    """Run predict and train commands sequentially and verify their outputs."""

    theta_path = tmp_path / "theta.json"
    data_path = Path("data.csv")

    env = {k: v for k, v in os.environ.items() if not k.startswith("MUTMUT_")}
    env["PYTHONPATH"] = os.pathsep.join(
        [str(Path.cwd() / "src"), env.get("PYTHONPATH", "")]
    )

    result_predict = subprocess.run(
        [
            sys.executable,
            "-m",
            "src.predict",
            "--km",
            "0",
            "--theta",
            str(theta_path),
        ],
        capture_output=True,
        text=True,
        env=env,
    )
    assert result_predict.returncode == 0
    assert "prediction routine not yet implemented" in result_predict.stdout

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
    )
    assert result_train.returncode == 0
    assert result_train.stdout == ""
    assert theta_path.exists()

    result_predict_after = subprocess.run(
        [
            sys.executable,
            "-m",
            "src.predict",
            "--km",
            "0",
            "--theta",
            str(theta_path),
        ],
        capture_output=True,
        text=True,
        env=env,
    )
    assert result_predict_after.returncode == 0
    assert "prediction routine not yet implemented" in result_predict_after.stdout

    theta_path.unlink(missing_ok=True)
    assert not theta_path.exists()
