from gendiff.generate_diff import generate_diff
from gendiff.get_files import get_files


def main():
    first_file, second_file = get_files()
    diff = generate_diff(first_file, second_file)
    print('{')
    for key, value in diff.items():
        print(f'    {key}: {value}')
    print('}')


if __name__ == '__main__':
    main()