"""Command-line interface for the homework 1 functions."""

from __future__ import annotations

import argparse
from pathlib import Path

from .exercises import avg_word_len, k_boom, max_even_seq


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    average_parser = subparsers.add_parser("average-word-length")
    average_parser.add_argument("input_file", type=Path)

    boom_parser = subparsers.add_parser("k-boom")
    boom_parser.add_argument("n", type=int)
    boom_parser.add_argument("k", type=int)

    sequence_parser = subparsers.add_parser("max-even-seq")
    sequence_parser.add_argument("n", type=int)
    sequence_parser.add_argument("k", type=int)
    return parser


def cli() -> None:
    arguments = build_parser().parse_args()
    try:
        if arguments.command == "average-word-length":
            avg_word_len(arguments.input_file)
            print("wrote output.txt")
        elif arguments.command == "k-boom":
            print(k_boom(arguments.n, arguments.k))
        else:
            print(max_even_seq(arguments.n, arguments.k))
    except (OSError, ValueError) as error:
        raise SystemExit(f"error: {error}") from error


if __name__ == "__main__":
    cli()
