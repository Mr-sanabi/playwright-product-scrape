import csv

import pytest

from src.main import positive_int
from src.writer import save_csv


def test_save_csv_creates_nested_output(tmp_path):
    path = tmp_path / "nested" / "quotes.csv"
    assert save_csv(path, [{"quote": "Hello", "author": "Ada", "source_url": "https://example.com"}])
    with path.open(encoding="utf-8", newline="") as file:
        assert list(csv.DictReader(file))[0]["author"] == "Ada"


def test_positive_int_rejects_zero():
    with pytest.raises(Exception):
        positive_int("0")
