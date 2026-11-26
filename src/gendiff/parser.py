import json

import yaml


def parse(content, file_format):
    if file_format == ".json":
        return json.loads(content)

    if file_format in (".yml", ".yaml"):
        return yaml.safe_load(content)

    raise ValueError(f"Unsupported file format: {file_format}")
