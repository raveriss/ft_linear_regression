from pathlib import Path

import pytest

from train.train import read_data


def test_read_data_valid(tmp_path: Path) -> None:
    good = tmp_path / "good.csv"
    good.write_text("km,price\n240000,3650\n")
    rows = read_data(str(good))
    assert rows == [(240000.0, 3650.0)]


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
