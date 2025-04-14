from gendiff.diff_builder import build_diff
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish
from gendiff.parsers import load_file


def generate_diff(file_path1, file_path2, format_name='stylish'):
    file1 = load_file(file_path1)
    file2 = load_file(file_path2)
    diff = build_diff(file1, file2)
    
    if format_name == 'stylish':
        return format_stylish(diff)
    if format_name == 'plain':
        return format_plain(diff)
    raise ValueError(f"Unknown format: {format_name}")