import sys
from argparse import ArgumentParser

from boltun.engine import Engine


def main():
    argument_parser = ArgumentParser(
        prog='boltun',
        description="Generates datasets from a template file",
        add_help=True)
    argument_parser.add_argument(
        "input", help="Input template")

    if not sys.argv[1:]:
        argument_parser.print_help()
        argument_parser.exit()

    args = argument_parser.parse_args()
    input_arg = args.input

    engine = Engine()
    for sample in engine.render(input_arg):
        print(str(sample))


if __name__ == '__main__':
    main()
