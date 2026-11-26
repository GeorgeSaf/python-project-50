import json
from pathlib import Path

from .parser import parse


def load_file(filepath):
    path = Path(filepath)
    content = path.read_text(encoding="utf-8")
    return parse(content, path.suffix.lower())


def format_value(value):
    if isinstance(value, str):
        return value

    return json.dumps(value, ensure_ascii=False)


def generate_diff(first_file, second_file):
    first_data = load_file(first_file)
    second_data = load_file(second_file)

    all_keys = sorted(first_data.keys() | second_data.keys())

    lines = ["{"]

    for key in all_keys:
        if key not in first_data:
            value = format_value(second_data[key])
            lines.append(f"  + {key}: {value}")

        elif key not in second_data:
            value = format_value(first_data[key])
            lines.append(f"  - {key}: {value}")

        elif (
            first_data[key] == second_data[key]
            and type(first_data[key]) is type(second_data[key])
        ):
            value = format_value(first_data[key])
            lines.append(f"    {key}: {value}")

        else:
            old_value = format_value(first_data[key])
            new_value = format_value(second_data[key])

            lines.append(f"  - {key}: {old_value}")
            lines.append(f"  + {key}: {new_value}")

    lines.append("}")

    return "\n".join(lines)
