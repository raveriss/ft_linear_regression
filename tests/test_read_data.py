from pathlib import Path

import pytest

from train.train import read_data


def test_read_data_valid() -> None:
    data_path = Path(__file__).resolve().parents[1] / "data.csv"
    rows = read_data(str(data_path))
    assert rows[0] == pytest.approx((240000.0, 3650.0))
    assert len(rows) > 0


def test_read_data_invalid_value(tmp_path: Path) -> None:
    bad = tmp_path / "bad.csv"
    bad.write_text("km,price\n1000,abc\n")
    with pytest.raises(ValueError, match="invalid row 2"):
        read_data(str(bad))


def test_read_data_nan(tmp_path: Path) -> None:
    bad = tmp_path / "bad_nan.csv"
    bad.write_text("km,price\n1000,nan\n")
    with pytest.raises(ValueError, match="invalid row 2"):
        read_data(str(bad))
