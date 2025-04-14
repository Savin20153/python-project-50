from gendiff.cli import parse_args
from gendiff.generator import generate_diff


def main():
    file1, file2, format_name = parse_args()
    result = generate_diff(file1, file2, format_name)
    print(result)


if __name__ == "__main__":
    main()