import csv
from pathlib import Path


def test_data_csv_parses_correctly() -> None:
    current = Path(__file__).resolve()
    for parent in [current.parent, *current.parents]:
        candidate = parent / "data.csv"
        if candidate.exists():
            path = candidate
            break
    else:  # pragma: no cover - defensive programming
        raise FileNotFoundError("data.csv not found")

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
