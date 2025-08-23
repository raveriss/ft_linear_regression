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


def test_read_data_invalid_km(tmp_path: Path) -> None:
    bad = tmp_path / "bad_km.csv"
    bad.write_text("km,price\nabc,1000\n")
    with pytest.raises(ValueError, match="invalid row 2"):
        read_data(str(bad))


def test_read_data_nan_km(tmp_path: Path) -> None:
    bad = tmp_path / "nan_km.csv"
    bad.write_text("km,price\nnan,1000\n")
    with pytest.raises(ValueError, match="invalid row 2"):
        read_data(str(bad))


def test_read_data_missing_value(tmp_path: Path) -> None:
    bad = tmp_path / "missing.csv"
    bad.write_text("km,price\n1000\n")
    with pytest.raises(ValueError, match="invalid row 2: missing value"):
        read_data(str(bad))


def test_read_data_invalid_header(tmp_path: Path) -> None:
    bad = tmp_path / "bad_header.csv"
    bad.write_text("a,b\n1,2\n")
    with pytest.raises(
        ValueError, match=r"^invalid CSV format \(expected columns: km,price\)$"
    ):
        read_data(str(bad))


def test_read_data_no_rows(tmp_path: Path) -> None:
    bad = tmp_path / "empty.csv"
    bad.write_text("km,price\n")
    with pytest.raises(ValueError, match=r"^no data rows found$"):
        read_data(str(bad))


def test_read_data_missing_file(tmp_path: Path) -> None:
    missing = tmp_path / "missing.csv"
    with pytest.raises(
        ValueError, match=f"^data file not found: {missing}$"
    ):
        read_data(str(missing))
