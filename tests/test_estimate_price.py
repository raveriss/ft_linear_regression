import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from train.train import estimatePrice


def test_estimate_price_returns_non_null_value():
    result = estimatePrice(42)
    assert result is not None
