import json
from pathlib import Path
from gendiff.generate_diff import generate_diff

def format_diff(diff):
    lines = []
    for key in sorted(diff.keys(), key=lambda x: x[2:] if x[0] in '+-' else x.strip()):
        lines.append(f"  {key}: {json.dumps(diff[key])}")
    return "{\n" + "\n".join(lines) + "\n}"

def test_generate_diff():
    base_path = Path(__file__).parent / 'test_data'

    with open(base_path / 'file1.json') as f1:
        file1 = json.load(f1)

    with open(base_path / 'file2.json') as f2:
        file2 = json.load(f2)

    with open(base_path / 'expected_output.txt') as expected_file:
        expected_output = expected_file.read().strip()

    diff = generate_diff(file1, file2)
    result_str = format_diff(diff).strip()

    assert result_str == expected_output
