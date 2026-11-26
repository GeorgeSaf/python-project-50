import json
import sys
from pathlib import Path

from gendiff import generate_diff
from gendiff.scripts.gendiff import main

DATA_DIR = Path(__file__).parent / "test_data"


def get_expected():
    return (DATA_DIR / "expected.txt").read_text(
        encoding="utf-8"
    ).rstrip("\n")


def test_flat_json_diff():
    result = generate_diff(
        DATA_DIR / "file1.json",
        DATA_DIR / "file2.json",
    )

    assert result == get_expected()


def test_identical_files(tmp_path):
    filepath = tmp_path / "same.json"

    data = {
        "timeout": 50,
        "follow": False,
        "empty": None,
    }

    filepath.write_text(
        json.dumps(data),
        encoding="utf-8",
    )

    expected = (
        "{\n"
        "    empty: null\n"
        "    follow: false\n"
        "    timeout: 50\n"
        "}"
    )

    assert generate_diff(filepath, filepath) == expected


def test_different_value_types(tmp_path):
    first = tmp_path / "first.json"
    second = tmp_path / "second.json"

    first.write_text('{"value": true}', encoding="utf-8")
    second.write_text('{"value": 1}', encoding="utf-8")

    expected = (
        "{\n"
        "  - value: true\n"
        "  + value: 1\n"
        "}"
    )

    assert generate_diff(first, second) == expected


def test_cli_output(monkeypatch, capsys):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "gendiff",
            "-f",
            "stylish",
            str(DATA_DIR / "file1.json"),
            str(DATA_DIR / "file2.json"),
        ],
    )

    main()

    captured = capsys.readouterr()

    assert captured.out == get_expected() + "\n"
