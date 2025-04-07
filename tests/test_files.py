import pathlib
from gendiff.generate_diff import generate_diff
from gendiff.get_files import get_files


file1_json = pathlib.Path('tests/test_data/file1.json')
file2_json = pathlib.Path('tests/test_data/file2.json')
expected_output = pathlib.Path('tests/test_data/expected_output.txt')

def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read().strip()


def test_generate_diff(file1_json, file2_json, expected_output):
    diff = generate_diff(file1_json, file2_json)
    expected_result = read_file(expected_output)
    assert diff == expected_result


