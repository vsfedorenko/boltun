import sys
from argparse import ArgumentParser


def main():
    argument_parser = ArgumentParser(
        prog='boltun',
        description="Generates datasets from a template file",
        add_help=True)
    argument_parser.add_argument(
        "input_path", help="Path to template file")
    argument_parser.add_argument(
        "-o", "--output", dest="output_path",
        help="Output file path", required=False, default=None)

    if sys.argv[1:]:
        argument_parser.print_help()
        argument_parser.exit()

    args = argument_parser.parse_args()

    input_path = args.input_path
    output_path = args.output_path


if __name__ == '__main__':
    main()
