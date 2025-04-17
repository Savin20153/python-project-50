import os
import pytest
from gendiff.generator import generate_diff

TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'test_data')

FILE1_JSON = os.path.join(TEST_DATA_DIR, 'file1.json')
FILE2_JSON = os.path.join(TEST_DATA_DIR, 'file2.json')
FILE1_YML = os.path.join(TEST_DATA_DIR, 'file1.yml')
FILE2_YML = os.path.join(TEST_DATA_DIR, 'file2.yml')

EXPECTED_STYLISH = os.path.join(TEST_DATA_DIR, 'expected_output_stylish.txt')
EXPECTED_PLAIN = os.path.join(TEST_DATA_DIR, 'expected_output_plain.txt')
EXPECTED_JSON = os.path.join(TEST_DATA_DIR, 'expected_output_json.txt')

def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read().strip()

def normalize(text):
    """Удаляет лишние пробелы и переносы строк для сравнения."""
    return '\n'.join(line.strip() for line in text.splitlines() if line.strip())

@pytest.mark.parametrize("file1, file2, expected_output, format_name", [
    (FILE1_JSON, FILE2_JSON, EXPECTED_STYLISH, 'stylish'),
    (FILE1_YML, FILE2_YML, EXPECTED_STYLISH, 'stylish'),
    (FILE1_JSON, FILE2_JSON, EXPECTED_PLAIN, 'plain'),
    (FILE1_YML, FILE2_YML, EXPECTED_PLAIN, 'plain'),
    (FILE1_JSON, FILE2_JSON, EXPECTED_JSON, 'json'),
    (FILE1_YML, FILE2_YML, EXPECTED_JSON, 'json'),
])
def test_gendiff(file1, file2, expected_output, format_name):
    expected = normalize(read_file(expected_output))
    result = normalize(generate_diff(file1, file2, format_name))
    assert result == expected, (
        f"Формат: {format_name}\n"
        f"Файлы: {file1}, {file2}\n"
        f"Ожидаемый вывод:\n{expected}\n"
        f"Фактический вывод:\n{result}"
    )