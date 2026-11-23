import argparse
import json


def load_json_file(filepath):
    with open(filepath, encoding="utf-8") as file:
        return json.load(file)


def main():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference.",
    )

    parser.add_argument("first_file")
    parser.add_argument("second_file")

    parser.add_argument(
        "-f",
        "--format",
        metavar="FORMAT",
        help="set format of output",
    )

    args = parser.parse_args()

    load_json_file(args.first_file)
    load_json_file(args.second_file)


if __name__ == "__main__":
    main()
