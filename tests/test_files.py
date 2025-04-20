import pytest
import json
import os
from gendiff.generator import generate_diff

def get_path(filename):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'test_data', filename)

def read_file(filepath):
    with open(filepath, 'r') as f:
        return f.read().strip()

def normalize_stylish(output):
    """Нормализует stylish-вывод для сравнения"""
    lines = [line.strip() for line in output.splitlines() if line.strip()]
    return '\n'.join(lines)

test_cases = [
    ('file1.json', 'file2.json', 'expected_output_stylish.txt', 'stylish'),
    ('file1.yml', 'file2.yml', 'expected_output_stylish.txt', 'stylish'),
    ('file1.json', 'file2.json', 'expected_output_plain.txt', 'plain'),
    ('file1.yml', 'file2.yml', 'expected_output_plain.txt', 'plain'),
    ('file1.json', 'file2.json', 'expected_output_json.txt', 'json'),
    ('file1.yml', 'file2.yml', 'expected_output_json.txt', 'json')
]

@pytest.mark.parametrize("file1, file2, expected_file, format_name", test_cases)
def test_gendiff(file1, file2, expected_file, format_name):
    file1_path = get_path(file1)
    file2_path = get_path(file2)
    expected_path = get_path(expected_file)
    
    expected = read_file(expected_path)
    result = generate_diff(file1_path, file2_path, format_name).strip()

    if format_name == 'json':
        assert json.loads(result) == json.loads(expected)
    elif format_name == 'plain':
        assert result.splitlines() == expected.splitlines()
    else:  # stylish format
        assert normalize_stylish(result) == normalize_stylish(expected)