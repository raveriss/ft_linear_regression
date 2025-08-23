import csv
from pathlib import Path


def test_data_csv_parses_correctly() -> None:
    path = Path(__file__).resolve().parents[1] / "data.csv"
    content = path.read_bytes()
    content.decode("utf-8")
    assert b"\r" not in content, "expected LF line endings"
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        assert reader.fieldnames == ["km", "price"]
        rows = list(reader)
    assert rows, "data.csv must contain rows"
    for row in rows:
        assert set(row.keys()) == {"km", "price"}
        int(row["km"])
        int(row["price"])
