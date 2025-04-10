import argparse
from gendiff.parsers import load_file  # Или from parsers import load_file

def get_files():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format', default='stylish',
        help='set format of output'
    )

    args = parser.parse_args()

    first_file = load_file(args.first_file)
    second_file = load_file(args.second_file)

    return [first_file, second_file]