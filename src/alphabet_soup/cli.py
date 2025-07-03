"""
Command-line interface for the Alphabet Soup solver.
"""
import argparse
from alphabet_soup import __version__
from alphabet_soup.core import load_puzzle, find_word


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Solve a word-search puzzle and output answer key."
    )
    parser.add_argument(
        "-V", "--version",
        action="version",
        version=f"%(prog)s {__version__}"
    )
    parser.add_argument(
        "input_file",
        help="Path to the puzzle text file"
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    grid, words = load_puzzle(args.input_file)

    for word in words:
        pos = find_word(grid, word)
        if pos:
            (start, end) = pos
            print(f"{word} {start[0]}:{start[1]} {end[0]}:{end[1]}")
        else:
            print(f"{word} not found")


if __name__ == "__main__":
    main()