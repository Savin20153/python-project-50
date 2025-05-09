import json

import yaml


def load_file(file_path):
    if file_path.endswith('.json'):
        return json.load(open(file_path))
    elif file_path.endswith('.yml') or file_path.endswith('.yaml'):
        return yaml.safe_load(open(file_path))
    else:
        raise ValueError("Unsupported file format")