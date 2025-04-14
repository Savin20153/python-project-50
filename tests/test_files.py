import json
import yaml
from pathlib import Path
from gendiff.generator import generate_diff

def format_diff(diff):
    lines = []
    for key in sorted(diff.keys(), key=lambda x: x[2:] if x[0] in '+-' else x.strip()):
        lines.append(f" {key}: {json.dumps(diff[key])}")
    return "{\n" + "\n".join(lines) + "\n}"

def load_file(file_path):
    file_path_str = str(file_path) 
    if file_path_str.endswith('.json'):
        with open(file_path) as f:
            return json.load(f)
    elif file_path_str.endswith('.yml') or file_path_str.endswith('.yaml'):
       with open(file_path) as f:
          return yaml.safe_load(f)
    else:
        raise ValueError("Unsupported file format")

def test_generate_diff_json():
    base_path = Path(__file__).parent / 'test_data'
    file1 = load_file(base_path / 'file1.json')
    file2 = load_file(base_path / 'file2.json')
    with open(base_path / 'expected_output_stylish.txt') as expected_file:
        expected_output = expected_file.read().strip()
    diff_result = generate_diff(file1, file2)
    formatted_diff = format_diff(diff_result)
    assert formatted_diff == expected_output

def test_generate_diff_yml():
    base_path = Path(__file__).parent / 'test_data'
    file1 = load_file(base_path / 'file1.yml')
    file2 = load_file(base_path / 'file2.yml')
    with open(base_path / 'expected_output_stylish.txt') as expected_file:
        expected_output = expected_file.read().strip()
    diff_result = generate_diff(file1, file2)
    formatted_diff = format_diff(diff_result)
    assert formatted_diff == expected_output

def test_generate_diff_mixed():
    base_path = Path(__file__).parent / 'test_data'
    file1 = load_file(base_path / 'file1.json')
    file2 = load_file(base_path / 'file2.yml')
    with open(base_path / 'expected_output_stylish.txt') as expected_file:
        expected_output = expected_file.read().strip()
    diff_result = generate_diff(file1, file2)
    formatted_diff = format_diff(diff_result)
    assert formatted_diff == expected_output