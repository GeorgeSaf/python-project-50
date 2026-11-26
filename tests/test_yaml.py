from pathlib import Path

import pytest

from gendiff import generate_diff

DATA_DIR = Path(__file__).parent / "test_data"


@pytest.mark.parametrize(
    ("first_name", "second_name"),
    [
        ("file1.yml", "file2.yml"),
        ("file1.yml", "file2.yaml"),
        ("file1.json", "file2.yaml"),
        ("file1.yml", "file2.json"),
    ],
)
def test_yaml_diff(first_name, second_name):
    expected = (DATA_DIR / "expected.txt").read_text(
        encoding="utf-8"
    ).rstrip("\n")

    result = generate_diff(
        DATA_DIR / first_name,
        DATA_DIR / second_name,
    )

    assert result == expected
