import argparse


def get_parser():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    parser.add_argument('first_file', help='Path to the first file')
    parser.add_argument('second_file', help='Path to the second file')
    parser.add_argument(
        '-f', '--format',
        default='stylish',
        choices=['stylish', 'plain', 'json'], 
        help='Output format (default: "stylish")'
    )
    return parser


def parse_args():
    parser = get_parser()
    args = parser.parse_args()
    return args.first_file, args.second_file, args.format